import csv
from bs4 import BeautifulSoup
from linkml_runtime.utils.schemaview import SchemaView

import xml.etree.ElementTree as ET
import click
import requests
import pandas as pd


@click.group()
def cli():
    pass


# ==================================================================================== #
#              Creation of initial/unmapped NMDC NCBI mapping file                     #
# ==================================================================================== #
@click.command()
@click.option(
    "--tsv-output",
    "tsv_output_filepath",
    default="local/ncbi_attribute_mappings.tsv",
    show_default=True,
    help="Path to save initial TSV file which will need to be filled with mappings.",
)
def create_unmapped_ncbi_mapping_file(tsv_output_filepath):
    """Creates a TSV file with NMDC schema slot names that need to be mapped to NCBI Attribute names."""
    sv = SchemaView("src/schema/nmdc.yaml")
    classes_to_process = [
        "Biosample",
        "Extraction",
        "LibraryPreparation",
        "OmicsProcessing",
        "DataObject",
    ]

    with open(tsv_output_filepath, "w", newline="") as file:
        tsv_writer = csv.writer(file, delimiter="\t")

        tsv_writer.writerow(
            [
                "nmdc_schema_class",
                "nmdc_schema_slot",
                "nmdc_schema_slot_range",
                "ncbi_biosample_attribute_name",
                "static_value",
                "ignore",
            ]
        )

        for class_name in classes_to_process:
            induced_slots = sv.class_induced_slots(class_name)
            sorted_slots = sorted(induced_slots, key=lambda slot: slot.name)
            for slot in sorted_slots:
                tsv_writer.writerow([class_name, slot.name, slot.range, "", ""])

    click.echo(
        f"Unmapped NMDC-NCBI mapping TSV file '{tsv_output_filepath}' has been created."
    )


# ==================================================================================== #
#                                 Automated mapping                                    #
# Exact term matching of NMDC schema slots with NCBI BioSample Attribute names         #
# ==================================================================================== #
# Load dataframe containing all the slots from the NMDC schema that need to be mapped
# to "names" of NCBI BioSample Attributes. The slots that are being mapped belong to
# the following classes: Biosample, Extraction, LibraryPreparation, OmicsProcessing,
# DataObject. The "names" of the NCBI BioSample Attributes can be either the
# harmonized name, synonym, or attribute name (display name)
# The file at assets/ncbi_mappings/ncbi_attribute_mappings.tsv has been created by
# using SchemaView() to iterate over relevant classes and retrieving slots from the
# NMDC schema that are relevant to the NCBI BioSample mapping process


@click.command()
@click.option(
    "--tsv-input",
    "tsv_input_filepath",
    default="local/ncbi_attribute_mappings.tsv",
    show_default=True,
    required=True,
    type=click.Path(exists=True),
    help="Path to unmapped TSV file containg NMDC slot names that need to be mapped to \
    NCBI Attribute names.",
)
@click.option(
    "--xml-url",
    default="https://www.ncbi.nlm.nih.gov/biosample/docs/attributes/?format=xml",
    show_default=True,
    help="URL to fetch NCBI Attributes XML.",
)
@click.option(
    "--xml-output",
    "xml_filepath",
    default="local/ncbi_biosample.xml",
    show_default=True,
    help="Path to save NCBI Attributes XML to.",
)
@click.option(
    "--tsv-output",
    "tsv_output_filepath",
    default="local/ncbi_attribute_mappings_filled.tsv",
    show_default=True,
    help="Path to save TSV file to after exact term matching.",
)
def exact_term_matching(tsv_input_filepath, tsv_output_filepath, xml_url, xml_filepath):
    """Fetches NCBI BioSample Attributes XML and maps Attribute names to NMDC schema
    slot names."""
    # ncbi_biosample.xml: https://www.ncbi.nlm.nih.gov/biosample/docs/attributes/?format=xml
    # Parse the XML to create a dictionary of Attribute harmonized_names and their synonyms
    response = requests.get(xml_url)
    with open(xml_filepath, "wb") as foutput:
        foutput.write(response.content)

    # Read in the list of all NCBI BioSample Attribute names that are available in the
    # NCBI BioSample database
    tree = ET.parse(xml_filepath)
    root = tree.getroot()
    attribute_dict = {}
    for attribute in root.findall(".//Attribute"):
        harmonized_name = attribute.find("HarmonizedName").text
        attribute_name = attribute.find("Name").text
        synonyms = [synonym.text for synonym in attribute.findall("Synonym")]
        synonyms.append(attribute_name)
        attribute_dict[harmonized_name] = synonyms

    df = pd.read_csv(tsv_input_filepath, delimiter="\t")
    df["ncbi_biosample_attribute_name"] = df.apply(
        map_attributes, axis=1, args=(attribute_dict,)
    )
    df.to_csv(tsv_output_filepath, sep="\t", index=False)
    click.echo(f"Exact term matched TSV file saved to '{tsv_output_filepath}'")


def map_attributes(row, attribute_dict):
    for harmonized_name, aliases in attribute_dict.items():
        if (
            row["nmdc_schema_slot"].lower()
            in [harmonized_name.lower() for harmonized_name in aliases]
            or row["nmdc_schema_slot"].lower() == harmonized_name.lower()
        ):
            return harmonized_name
    return row["ncbi_biosample_attribute_name"]


# ==================================================================================== #
#                               Ignore irrelevant slots                                #
# Ignore slots coming from certain imports that are not relevant to NCBI               #
# ==================================================================================== #
@click.command()
@click.argument("tsv_filepath", type=click.Path(exists=True))
def ignore_import_schema_slots(tsv_filepath):
    """Marks entries in the TSV file as 'PROG_IGNORE' if they are not relevant to the
    NCBI Attribute name mapping process."""
    df = pd.read_csv(tsv_filepath, delimiter="\t")
    sv = SchemaView("src/schema/nmdc.yaml")
    classes_to_be_reported = [
        "Biosample",
        "Extraction",
        "LibraryPreparation",
        "OmicsProcessing",
        "DataObject",
    ]
    imports_to_be_ignored = [
        "https://w3id.org/nmdc/portal/emsl",
        "https://w3id.org/nmdc/portal/jgi_metagenomics",
        "https://w3id.org/nmdc/portal/jgi_metatranscriptomics",
        "https://w3id.org/nmdc/portal/mixs_inspired",
        "https://w3id.org/nmdc/portal/sample_id",
    ]

    if "ignore" not in df.columns or df["ignore"].dtype != "object":
        df["ignore"] = df["ignore"].astype("object")

    for class_name in classes_to_be_reported:
        class_slots = sv.class_induced_slots(class_name)
        for slot in class_slots:
            if slot.from_schema in imports_to_be_ignored:
                df.loc[df["nmdc_schema_slot"] == slot.name, "ignore"] = "PROG_IGNORE"
    df.to_csv(tsv_filepath, sep="\t", index=False)
    click.echo(
        f"'{tsv_filepath}' has been updated with slot/attribute names to be ignored."
    )


# ==================================================================================== #
#                                 Manual mapping                                       #
# Use individual Attribute names from specific NCBI packages to drive manual
# mapping/ignoring                                                                     #
# ==================================================================================== #
@click.command()
@click.option(
    "--xml-url",
    default="https://www.ncbi.nlm.nih.gov/biosample/docs/packages/MIMS.me.water.6.0/?format=xml",
    show_default=True,
    help="URL NCBI package-specific XML. It default to MIMS.me.water.6.0 package XML.",
)
@click.argument("tsv_filepath", type=click.Path(exists=True))
def package_specific_curation(xml_url, tsv_filepath):
    """Semi-automated mappig/curation of package-specific NCBI Attributes to aid in the
    maximal mapping of NMDC schema slots to NCBI BioSample Attributes."""
    response = requests.get(xml_url)
    xml_content = response.text

    soup = BeautifulSoup(xml_content, "xml")
    attributes = soup.find_all("Attribute")

    tsv_df = pd.read_csv(tsv_filepath, sep="\t")
    tsv_harmonized_names = tsv_df["ncbi_biosample_attribute_name"].values

    mandatory_attributes = []
    optional_attributes = []

    for attribute in attributes:
        harmonized_name = (
            attribute.find("HarmonizedName").text
            if attribute.find("HarmonizedName")
            else None
        )
        use = attribute.get("use", "optional")

        if harmonized_name and harmonized_name not in tsv_harmonized_names:
            if use == "mandatory":
                mandatory_attributes.append(harmonized_name)
            else:
                optional_attributes.append(harmonized_name)

    # if we can't figure out an appropriate NMDC slot to map it to, we can ignore it
    # by setting the value of the "ignore"  column to "MAN_IGNORE" to indicate that
    # it has been ignored after manual curation
    if mandatory_attributes:
        click.echo(
            f"Mandatory NCBI Attribute names that do not have NMDC slot mappings: {mandatory_attributes}"
        )

    if optional_attributes:
        click.echo(
            f"Optional NCBI Attribute names that do not have NMDC slot mappings: {optional_attributes}"
        )

    return mandatory_attributes, optional_attributes


cli.add_command(create_unmapped_ncbi_mapping_file)
cli.add_command(exact_term_matching)
cli.add_command(ignore_import_schema_slots)
cli.add_command(package_specific_curation)

if __name__ == "__main__":
    cli()
