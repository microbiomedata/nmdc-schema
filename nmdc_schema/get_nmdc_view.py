import pkgutil

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import json_dumper


class ViewGetter:
    def get_view(self) -> SchemaView:
        nmdc_schema_bytes = pkgutil.get_data("nmdc_schema", "nmdc_materialized_patterns.yaml")
        nmdc_schema_yaml_string = str(nmdc_schema_bytes, "utf-8")
        nmdc_view = SchemaView(nmdc_schema_yaml_string)
        return nmdc_view
