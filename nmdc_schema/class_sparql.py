import json
import re

import click
import pandas as pd
import sparql_dataframe
from curies import Converter
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

from io import StringIO

import pandas as pd

from SPARQLWrapper import SPARQLWrapper, CSV, SELECT, POST, POSTDIRECTLY

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# todo unpack bank node objects RECURSIVELY
# todo https://w3id.org/mixs/ or https://w3id.org/mixs-6-2-rc/ ?
# todo support for MULTIPLE constraints
# todo make more of these essentially CONSTANT declarations click options, directly or via a config file
# todo be on the lookout for "http" or GraphDB's default blank node prefix: "_:genid-" in the output (TSV)

prefixmaps_json_file = "../project/prefixmap/nmdc.yaml"  # todo oops
with open(prefixmaps_json_file, "r") as f:
    raw_prefixmaps_dict = json.load(f)

filtered_prefixmaps_dict = {}
for pk, pv in raw_prefixmaps_dict.items():
    if type(pv) == str:
        filtered_prefixmaps_dict[pk] = pv

supplementary_prefix_maps = {
    "BIOSAMPLE": "https://example.org/biosample/",
    "ENVO": "http://purl.obolibrary.org/obo/ENVO_",
    "GOLD": 'http://identifiers.org/gold/',
    "GOLD2": "https://example.org/gold/",
    "NCBITaxon": "http://purl.obolibrary.org/obo/NCBITaxon_",
    "img.taxon": "https://example.org/img.taxon/",
}

overwrite_prefix_maps = {
    "MASSIVE": "https://bioregistry.io/reference/massive:",
    # todo bioregistry and idot? prefer lowercase prefixes
    "SIO": "http://example.com/sio_lowercase:",
    "doi": "https://bioregistry.io/reference/doi:",
    "sio": "https://bioregistry.io/reference/sio:",
    # todo The DOI resolution factsheet specifies that https://doi.org/DOI is the preferred format:
}

for sk, sv in overwrite_prefix_maps.items():
    filtered_prefixmaps_dict[sk] = sv

for sk, sv in supplementary_prefix_maps.items():
    filtered_prefixmaps_dict[sk] = sv

converter = Converter.from_prefix_map(filtered_prefixmaps_dict)

prefixes_list = []
for k, v in filtered_prefixmaps_dict.items():
    prefixes_list.append(f"PREFIX {k}: <{v}>")
prefixes_string = "\n".join(prefixes_list)
# print(f"{prefixes_string}")  # todo includes a lot that won't be used

sparql_endpoint = "https://graphdb-dev.microbiomedata.org/repositories/nmdc-metadata"


def replace_colons_and_whitespace(any_string):
    return re.sub(r"[: ]", "_", any_string)


def contract_url(any_url):
    # converter = Converter.from_prefix_map(filtered_prefixmaps_dict)
    try:
        curie = converter.compress(any_url)
        if curie:
            return curie
        else:
            return any_url
    except Exception as e:
        print(f"WARNING on {any_url}: {e}")
        return any_url


def contract_multi_urls(any_url):
    if type(any_url) == str:
        urls = any_url.split("|")
        contracted_urls = []
        for current_url in urls:
            contracted_url = contract_url(current_url)
            contracted_urls.append(contracted_url)
        cleaned_urls = [item for item in contracted_urls if item is not None]
        pasted_urls = "|".join(cleaned_urls)
        return pasted_urls
    else:
        return any_url


def contact_column(df, column_name):
    column_as_list = df[column_name].tolist()
    contracted_list = [contract_multi_urls(i) for i in column_as_list]
    df[column_name] = contracted_list
    none_outputs = find_none_indices(contracted_list)
    un_compacted_inputs = get_values_at_indices(column_as_list,
                                                none_outputs)  # todo oops they have been removed already # also removes blank node ids
    # print(f"{column_name} {un_compacted_inputs = }")
    return df


def get_class_slot_usage(class_name):
    class_slot_usage_query = f"""
    \n{prefixes_string}\n
    select ?p (count(?{class_name}) as ?count) 
    where  {{ ?{class_name} a nmdc:{class_name} ; 
    ?p ?o . }}
    group by ?p
    # order by desc(count(?{class_name}))
    order by ?p
    """  # todo need better handling for class urls, classes names containing whitespace, etc. here
    df = sparql_dataframe.get(sparql_endpoint, class_slot_usage_query, post=True)
    p_list = df['p'].tolist()
    curie_list = [contract_url(p) for p in p_list]
    df['contracted'] = curie_list
    return df


def find_none_indices(list1):
    """
    Returns a list of the indices at which a Python list has a None value.

    Args:
      list1: The list to search.

    Returns:
      A list of the indices at which `list1` has a None value.
    """

    none_indices = []
    for i in range(len(list1)):
        if list1[i] is None:
            none_indices.append(i)

    return none_indices


def get_values_at_indices(list1, indices):
    """
    Returns the values in `list1` at the indices specified in `indices`.

    Args:
      list1: The list to get values from.
      indices: A list of indices.

    Returns:
      A list of the values in `list1` at the indices specified in `indices`.
    """

    values_at_indices = []
    for index in indices:
        values_at_indices.append(list1[index])

    return values_at_indices


def get_sparql_dataframe(endpoint, query, post=False):
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(query)
    if sparql.queryType != SELECT:
        raise QueryException("Only SPARQL SELECT queries are supported.")

    if post:
        sparql.setOnlyConneg(True)
        sparql.addCustomHttpHeader("Content-type", "application/sparql-query")
        sparql.addCustomHttpHeader("Accept", "text/csv")
        sparql.setMethod(POST)
        sparql.setRequestMethod(POSTDIRECTLY)

    sparql.setReturnFormat(CSV)
    results = sparql.query().convert()
    _csv = StringIO(results.decode('utf-8'))
    return pd.read_csv(_csv, sep=",", low_memory=False)


class LinkMLClassSparqlQuery:
    def __init__(self, target_class_name, graph_name, schema_file, make_distinct=False, do_group_concat=False,
                 concatenation_suffix="_cat", do_not_query=("id", "type")):
        self.schema_view = SchemaView(schema_file)

        self.concatenation_suffix = concatenation_suffix
        self.default_prefix = self.schema_view.schema.default_prefix
        self.do_group_concat = do_group_concat
        self.do_not_query = do_not_query
        self.graph_name = graph_name
        self.groupers = []
        self.make_distinct = make_distinct
        self.schema_file = schema_file
        self.select_line = []
        self.slot_dict = {}
        self.target_class_name = target_class_name
        self.target_class_slots = self.schema_view.class_induced_slots(target_class_name)
        self.triple_patterns = []
        self.vars_to_select = []
        self.class_slot_usage = {}

    def characterize_slots(self):
        for slot in self.target_class_slots:
            slot_range_element = self.schema_view.get_element(slot.range)
            slot_range_type = type(slot_range_element).class_name
            self.slot_dict[slot.name] = {
                "name": slot.name,
                "slot_uri": slot.slot_uri,
                "do_not_query": slot.name in self.do_not_query,
                "multivalued": slot.multivalued,
                "range": slot.range,
                "range_type": slot_range_type,
                "required": slot.required,
                "slot_slug": replace_colons_and_whitespace(slot.name),
            }
            if slot_range_type == "class_definition":
                if self.schema_view.get_identifier_slot(slot.range):
                    self.slot_dict[slot.name]['class_identifier_slot'] = self.schema_view.get_identifier_slot(
                        slot.range).name
            if not self.slot_dict[slot.name]['slot_uri']:
                self.slot_dict[slot.name][
                    'slot_uri'] = f"{self.default_prefix}:{self.slot_dict[slot.name]['slot_slug']}"
                pass

            all_usage = self.class_slot_usage[self.target_class_name]
            slot_usage = all_usage[all_usage['contracted'].eq(self.slot_dict[slot.name]['slot_uri'])]
            if slot_usage.empty:
                # print(f"WARNING: {self.slot_dict[slot.name]['slot_uri']} not used in {self.target_class_name}'s data")
                self.slot_dict[slot.name]['do_not_query'] = True

    def write_query(self):

        if self.schema_view.get_class(self.target_class_name).class_uri:
            type_query_object = self.schema_view.get_class(self.target_class_name).class_uri
        else:
            type_query_object = f"{self.default_prefix}:{self.target_class_name}"
        type_query = f"?{self.target_class_name} a {type_query_object} ."

        self.triple_patterns.append(type_query)

        for sk, sv in self.slot_dict.items():
            # print(f"{sk}")
            if sv['do_not_query']:
                continue

            if sv['range_type'] == "class_definition":
                pass
            else:
                if self.do_group_concat:
                    if sv['multivalued']:
                        self.vars_to_select.append(
                            f"(group_concat(distinct ?{sv['slot_slug']} ; SEPARATOR='|') as ?{sv['slot_slug']}{self.concatenation_suffix})")
                    else:
                        self.vars_to_select.append(f"?{sv['slot_slug']}")
                        self.groupers.append(f"?{sv['slot_slug']}")
            lines = self.write_line(sv)
            self.triple_patterns.extend(lines)

    def write_line(self, slot_dict):
        # print(slot_dict)
        # print(f"{slot_dict['name'] = } {slot_dict['range_type'] = }")

        if slot_dict['required']:
            line_prefix = ""
            line_suffix = ""
        else:
            line_prefix = "optional { "
            line_suffix = " }"

        if slot_dict['slot_uri']:
            predicate = slot_dict['slot_uri']
        else:
            predicate = f"{self.default_prefix}:{slot_dict['slot_slug']}"

        lines = [f"{line_prefix} ?{self.target_class_name} {predicate} ?{slot_dict['slot_slug']} "]

        if slot_dict['range_type'] == "class_definition":
            # print(f"{slot_dict['name'] = } {slot_dict['range_type'] = }")
            slot_type_query = f"optional {{ ?{slot_dict['slot_slug']} a ?{slot_dict['slot_slug']}_type . }} . "
            self.vars_to_select.append(f"?{slot_dict['slot_slug']}_type")
            self.groupers.append(f"?{slot_dict['slot_slug']}_type")
            lines.append(slot_type_query)
            range_slot = self.schema_view.get_identifier_slot(slot_dict['range'])
            if range_slot:
                # range_identifier = range_slot.name
                # print(f"{range_identifier = }")
                pass
            else:
                print(f"Also will need to account for {slot_dict['slot_slug']} -> {slot_dict['range']}'s slots")
                additional_slots = self.schema_view.class_induced_slots(slot_dict['range'])
                additional_slot_names = [i.name for i in additional_slots]
                for additional_slot_name in additional_slot_names:
                    additional_triple_pattern = f"optional {{ ?{slot_dict['slot_slug']} nmdc:{additional_slot_name} ?{slot_dict['slot_slug']}_{additional_slot_name} . }} . "
                    print(f"\t{additional_triple_pattern = }")
                    lines.append(additional_triple_pattern)
                    self.vars_to_select.append(f"?{slot_dict['slot_slug']}_{additional_slot_name}")
                    self.groupers.append(f"?{slot_dict['slot_slug']}_{additional_slot_name}")
                    # todo don't assume nmdc: prefix (also look for slot uri)
                    # todo reuse code already in this script
                    # todo recurse!
                    # todo don't assume optional
                    # todo account for multivalued slots esp in the context of outer multivalueds
                    # todo account for blank nodes ?
                    # todo add these variables to the select line

        lines.append(line_suffix)

        lines_pasted = "\n".join(lines)

        return [lines_pasted]

    def subsequent_queries(self, subject, predicate, obj_var_name, target_class_name):
        print(f"subsequent_queries({subject}, {predicate}, {obj_var_name}, {target_class_name})")
        subsequent_slots = self.schema_view.class_induced_slots(target_class_name)
        for slot in subsequent_slots:
            print(f"slot: {slot.name}")


class QueryException(Exception):
    pass


@click.command()
@click.option("--concatenation-suffix", default="_cat")
@click.option("--do-group-concat", is_flag=True, default=True)
@click.option("--do-not-query", multiple=True, default=("id", "type"))
@click.option("--graph-name", default="mongodb://mongo-loadbalancer.nmdc.production.svc.spin.nersc.gov:27017")
@click.option("--make-distinct", is_flag=True, default=False)
@click.option("--schema-file", default="nmdc_schema_accepting_legacy_ids.yaml")
@click.option("--target-class-name", default="Biosample")
@click.option("--target-p-o-constraint", default="dcterms:isPartOf q")
def main(target_class_name, graph_name, make_distinct, do_group_concat, concatenation_suffix, do_not_query,
         schema_file, target_p_o_constraint):
    query_support = LinkMLClassSparqlQuery(
        target_class_name=target_class_name,
        graph_name=graph_name,
        schema_file=schema_file,
        make_distinct=make_distinct,
        do_group_concat=do_group_concat,
        concatenation_suffix=concatenation_suffix,
        do_not_query=do_not_query,
    )

    query_support.class_slot_usage[target_class_name] = get_class_slot_usage(target_class_name)

    query_support.characterize_slots()
    query_support.write_query()

    query_support.vars_to_select.sort()
    if query_support.make_distinct:
        select_prefix = f"select distinct"
    else:
        select_prefix = "select"

    select_prefix = f"{select_prefix} (str(?{query_support.target_class_name}) as ?{query_support.target_class_name}_str)"

    query_support.vars_to_select = [select_prefix] + query_support.vars_to_select
    assembled_select_line = " ".join(query_support.vars_to_select)
    assembled_select_line = f"{assembled_select_line} where {{"
    if query_support.graph_name:
        assembled_select_line = f"{assembled_select_line} graph <{query_support.graph_name}> {{"
    else:
        assembled_select_line = f"{assembled_select_line}"

    query_support_string_lines = []

    query_support_string_lines.append(f"{assembled_select_line}")

    query_support.triple_patterns.sort()
    for i in query_support.triple_patterns:
        query_support_string_lines.append(i)

    if target_p_o_constraint:
        query_support_string_lines.append(f"?{query_support.target_class_name} {target_p_o_constraint} . ")

    query_support_string_lines.append("}")

    if query_support.graph_name:
        query_support_string_lines.append("}")

    if query_support.groupers:
        query_support.groupers = [f"?{query_support.target_class_name}"] + query_support.groupers
        grouping_line = f"group by {' '.join(query_support.groupers)}"
        query_support_string_lines.append(grouping_line)

    query_support_string = "\n".join(query_support_string_lines)
    query_support_string = prefixes_string + "\n" + query_support_string

    print("\n")
    print(query_support_string)

    df = get_sparql_dataframe(sparql_endpoint, query_support_string, post=True)

    for dfc in list(df.columns):
        # print(f"{dfc = }")
        df = contact_column(df, f"{dfc}")

    if target_p_o_constraint:
        target_p_o_constraint_parts = target_p_o_constraint.split(" ")
        constraint_label = target_p_o_constraint_parts[0]
        constraint_label = replace_colons_and_whitespace(constraint_label)
        constraint_value = target_p_o_constraint_parts[1]
        # df[constraint_label] = constraint_value
        new_column = pd.Series([constraint_value] * len(df), name=f"{target_class_name}_{constraint_label}")
        df = pd.concat([df, new_column], axis=1)

        df = df.dropna(axis=1, how='all')

    df.to_csv(f"{target_class_name}.tsv", index=False, sep="\t")


if __name__ == "__main__":
    main()
