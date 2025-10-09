import logging
from typing import Any, List, Dict
from importlib import resources
from pathlib import Path
from functools import lru_cache
import yaml
from nmdc_schema.nmdc_data import get_nmdc_schema_definition
from linkml_runtime import SchemaView

logger = logging.getLogger(__name__)

# TODO: Determine directory path and package path dynamically, instead of hard-coding them.
MIGRATOR_DIRECTORY = "nmdc_schema/migrators"
MIGRATOR_PACKAGE = "nmdc_schema.migrators"


def load_yaml_asset(path_to_asset_file: str) -> Any:
    """
    Safely loads the contents of a YAML file into a Python object. This function was designed specifically to
    work in both the `nmdc-schema` development environment and in environments that import the `nmdc-schema` package.

    Parameters:
        path_to_asset_file: Filesystem path to the YAML file, relative to the root of the `assets` directory.

    References:
    - https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.joinpath
    - https://docs.python.org/3/library/importlib.resources.html#importlib.resources.files
    - https://docs.python.org/3/library/importlib.resources.html#importlib.resources.as_file
    - https://realpython.com/python-yaml/#load-a-document-from-a-string-a-file-or-a-stream
    """
    # Define the Python path someone could use to `import` the package containing the `assets` directory.
    package_import_path = MIGRATOR_PACKAGE

    # Define the filesystem path to the `assets` directory (relative to that package).
    path_to_assets_directory = "assets"

    # Build a filesystem path to the specified asset file (also relative to that package).
    path_to_asset = Path(path_to_assets_directory).joinpath(path_to_asset_file)

    # Create a `Traversable` object that can be passed to the `resources.as_file()` function.
    traversable_resource_container = resources.files(package_import_path).joinpath(path_to_asset)

    # Use `resources.as_file()` to get an `open()`-able path to the asset file.
    with resources.as_file(traversable_resource_container) as file_path:
        # Finally, open the asset file and parse its contents as YAML.
        with open(file_path, "r") as f:
            obj = yaml.safe_load(f)  # the object type depends upon the YAML data

    return obj


def create_schema_view() -> SchemaView:
    """
    Returns a LinkML SchemaView instance that can be used to traverse the schema.
    
    >>> isinstance(create_schema_view(), SchemaView)
    True
    """
    schema_definition = get_nmdc_schema_definition()
    schema_view = SchemaView(schema_definition)
    return schema_view


# Constants for schema traversal
DATABASE_CLASS_NAME = "Database"


def get_classes_with_slots_by_range(schema_view: SchemaView, range_constraint: str) -> dict:
    """
    Returns a dictionary mapping class names to lists of their slot names that have the specified range.
    For each class, includes slots from the class AND all its subclasses to handle polymorphic storage.
    
    Args:
        schema_view: SchemaView instance
        range_constraint: The range type to search for (e.g., "QuantityValue", "TextValue", etc.)
        
    Returns:
        dict: {class_name: [slot_names_with_specified_range]}
    """
    classes_with_slots = {}
    
    # Get all classes in the schema
    for class_name in schema_view.all_classes():
        class_def = schema_view.get_class(class_name)
        if class_def:
            # Get all slots for this class
            induced_slots = schema_view.class_induced_slots(class_name)
            matching_slots = set()
            
            for slot_def in induced_slots:
                if slot_def.range == range_constraint:
                    matching_slots.add(slot_def.name)
            
            # Also get matching slots from all subclasses
            # This handles polymorphic storage where subclass records are stored in parent collections in mongodb
            subclass_slots = set()
            try:
                descendants = schema_view.class_descendants(class_name)
                for subclass_name in descendants:
                    subclass_induced_slots = schema_view.class_induced_slots(subclass_name)
                    for slot_def in subclass_induced_slots:
                        if slot_def.range == range_constraint:
                            subclass_slots.add(slot_def.name)
            except (AttributeError, KeyError, TypeError):
                # If class_descendants method doesn't exist or class is invalid, skip subclass processing
                pass
            
            # Combine parent and subclass slots
            all_slots = set(matching_slots) | subclass_slots
            
            if all_slots:
                classes_with_slots[class_name] = list(all_slots)
    
    return classes_with_slots


# TODO: Check whether this function can be replaced by a similar function from `refscan`.
def get_database_collections_for_class(schema_view: SchemaView, class_name: str) -> List[str]:
    """
    Returns the list of database collection names associated with the specified class.
    This function retrieves the collection names from the slots of the Database class
    that have the specified class as their range.

    Args:
        schema_view: SchemaView instance
        class_name: The name of the class to find collections for

    Returns:
        List[str]: List of collection names which permit storage of instances of the specified class
    """
    collection_names = set()

    for database_slot_name in schema_view.class_slots(DATABASE_CLASS_NAME):
        database_slot_def = schema_view.get_slot(database_slot_name, strict=True)
        database_slot_range_descendants = schema_view.class_descendants(database_slot_def.range, reflexive=True)
        if class_name in database_slot_range_descendants:
            collection_names.add(database_slot_name)

    return list(collection_names)