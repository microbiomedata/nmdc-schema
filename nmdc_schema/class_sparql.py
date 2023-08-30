import json
import re
from io import StringIO

import click
import pandas as pd
# import sparql_dataframe # copied and pasted, for addition of low_memory=False
from SPARQLWrapper import SPARQLWrapper, CSV, SELECT, POST, POSTDIRECTLY
from curies import Converter
from linkml_runtime import SchemaView

from SPARQLBurger.SPARQLQueryBuilder import *

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# todo unpack bank node objects RECURSIVELY
# todo https://w3id.org/mixs/ or https://w3id.org/mixs-6-2-rc/ ?
# todo support for MULTIPLE constraints
# todo make the extra prefix definitions click options, directly or via a config file
# todo (manually) be on the lookout for "http" or GraphDB's default blank node prefix: "_:genid-" in the output (TSV)
#  suggests that more prefix definitions are needed
# todo including a lot of prefixes that won't be used

# todo reuse code already in this script
# todo don't assume optional or multivalued

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


def replace_colons_and_whitespace(any_string):
    return re.sub(r"[: ]", "_", any_string)


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
    def __init__(self,
                 concatenation_suffix,
                 do_not_query,
                 graph_name,  # not being used by sparqlburger ?
                 prefix_maps_json,
                 schema_file,
                 sparql_endpoint,
                 target_class_name,
                 target_p_o_constraint,
                 do_group_concat=False,  # not being used by sparqlburger ?
                 make_distinct=False,  # not being used by sparqlburger ?
                 ):
        self.schema_view = SchemaView(schema_file)

        self.class_slot_usage = {}
        self.concatenation_suffix = concatenation_suffix
        self.converter = None
        self.default_prefix = self.schema_view.schema.default_prefix
        self.do_group_concat = do_group_concat
        self.do_not_query = do_not_query
        self.graph_name = graph_name
        self.groupers = []
        self.make_distinct = make_distinct
        self.prefix_maps_json = prefix_maps_json
        self.prefixes_string = ""
        self.schema_file = schema_file
        self.select_line = []
        self.slot_dict = {}
        self.target_class_name = target_class_name
        self.target_class_slots = self.schema_view.class_induced_slots(target_class_name)
        self.triple_patterns = []
        self.vars_to_select = []
        self.sparql_endpoint = sparql_endpoint
        self.target_p_o_constraint = target_p_o_constraint

    def get_class_slot_usage(self, class_name):
        class_slot_usage_query = f"""
        \n{self.prefixes_string}\n
        select ?p (count(?{class_name}) as ?count) 
        where  {{ 
          ?{class_name} a nmdc:{class_name} ; 
          ?p ?o . 
        }}
        group by ?p
        """  # todo need better handling for class urls, classes names containing whitespace, etc. here
        df = get_sparql_dataframe(self.sparql_endpoint, class_slot_usage_query, post=True)
        p_list = df['p'].tolist()
        curie_list = [self.contract_url(p) for p in p_list]
        df['contracted'] = curie_list
        return df

    def contract_column(self, df, column_name):
        column_as_list = df[column_name].tolist()
        contracted_list = [self.contract_multi_urls(i) for i in column_as_list]
        df[column_name] = contracted_list
        # none_outputs = find_none_indices(contracted_list)
        # un_compacted_inputs = get_values_at_indices(column_as_list,
        #                                             none_outputs)  # todo oops they have been removed already # also removes blank node ids
        # # print(f"{column_name} {un_compacted_inputs = }")
        return df

    def contract_multi_urls(self, any_url):
        if type(any_url) == str:
            urls = any_url.split("|")
            contracted_urls = []
            for current_url in urls:
                contracted_url = self.contract_url(current_url)
                contracted_urls.append(contracted_url)
            cleaned_urls = [item for item in contracted_urls if item is not None]
            pasted_urls = "|".join(cleaned_urls)
            return pasted_urls
        else:
            return any_url

    def contract_url(self, any_url):
        try:
            curie = self.converter.compress(any_url)
            if curie:
                return curie
            else:
                return any_url
        except Exception as e:
            print(f"WARNING on {any_url}: {e}")  # todo logging not printing
            return any_url

    def populate_prefix_maps(self):
        with open(self.prefix_maps_json, "r") as f:
            raw_prefixmaps_dict = json.load(f)

        filtered_prefixmaps_dict = {}
        for pk, pv in raw_prefixmaps_dict.items():
            if type(pv) == str:
                filtered_prefixmaps_dict[pk] = pv

        for sk, sv in overwrite_prefix_maps.items():
            filtered_prefixmaps_dict[sk] = sv

        for sk, sv in supplementary_prefix_maps.items():
            filtered_prefixmaps_dict[sk] = sv

        self.converter = Converter.from_prefix_map(filtered_prefixmaps_dict)

        prefixes_list = []
        for k, v in filtered_prefixmaps_dict.items():
            prefixes_list.append(f"PREFIX {k}: <{v}>")
        self.prefixes_string = "\n".join(prefixes_list)

    def characterize_slot(self, slot_name, all_usage=None):
        local_schema_view = self.schema_view
        slot_obj = local_schema_view.induced_slot(slot_name, self.target_class_name)
        slot_range_type_name = type(local_schema_view.get_element(slot_obj.range)).class_name

        local_slot_dict = {
            "name": slot_obj.name,
            "slot_uri": slot_obj.slot_uri,
            "do_not_query": slot_obj.name in self.do_not_query,
            "multivalued": slot_obj.multivalued,
            "range": slot_obj.range,
            "range_type": slot_range_type_name,
            "required": slot_obj.required,
            "slot_slug": replace_colons_and_whitespace(slot_obj.name),
        }

        if slot_range_type_name == "class_definition":
            if local_schema_view.get_identifier_slot(slot_obj.range):
                local_slot_dict['class_identifier_slot'] = local_schema_view.get_identifier_slot(
                    slot_obj.range).name

        if not local_slot_dict['slot_uri']:
            local_slot_dict['slot_uri'] = f"{self.default_prefix}:{local_slot_dict['slot_slug']}"

        if all_usage is not None:
            slot_usage = all_usage[all_usage['contracted'].eq(local_slot_dict['slot_uri'])]
            if slot_usage.empty:
                local_slot_dict['do_not_query'] = True

        return local_slot_dict

    def characterize_slots(self):
        all_usage = self.class_slot_usage[self.target_class_name]
        for slot in self.target_class_slots:
            local_slot_dict = self.characterize_slot(slot.name, all_usage)
            self.slot_dict[slot.name] = local_slot_dict

    def create_triple(self, subject, slot_dict):
        triple = Triple(subject=subject, predicate=slot_dict["slot_uri"],
                        object=f"{subject}_{slot_dict['slot_slug']}")
        return triple

    def build_with_sparql_burger(self):
        scalar_groupers = []

        select_query = SPARQLSelectQuery(distinct=True, include_popular_prefixes=False)  # limit=1_000_000
        # Create an empty graph pattern
        main_pattern = SPARQLGraphPattern()
        # Add prefixes
        for k, v in self.converter.prefix_map.items():
            select_query.add_prefix(prefix=Prefix(prefix=k, namespace=v))

        # determine the IRI for the target class
        if self.schema_view.get_class(self.target_class_name).class_uri:
            type_query_object = self.schema_view.get_class(self.target_class_name).class_uri
        else:
            type_query_object = f"{self.default_prefix}:{self.target_class_name}"

        # determine variable for type query
        type_query_variable = f"?{replace_colons_and_whitespace(self.target_class_name)}"

        # add the typing BGP
        main_pattern.add_triples(
            triples=[
                Triple(subject=type_query_variable, predicate="rdf:type", object=type_query_object),
            ]
        )

        # Add the type variable for selecting
        select_query.add_variables(variables=[type_query_variable])
        scalar_groupers.append(type_query_variable)

        for sk, sv in self.slot_dict.items():
            if sv['do_not_query']:
                continue

            deeper_triples = []
            type_pattern = None
            if sv['range_type'] == "class_definition":
                # assume optional multivalued
                type_triple = Triple(subject=f"{type_query_variable}_{sv['slot_slug']}", predicate="rdf:type",
                                     object=f"{type_query_variable}_{sv['slot_slug']}_rdf_type")
                type_pattern = SPARQLGraphPattern(optional=True)
                type_pattern.add_triples(triples=[type_triple])
                if 'class_identifier_slot' not in sv:
                    deeper_slots = self.schema_view.class_induced_slots(sv['range'])
                    for ds in deeper_slots:
                        deeper_slot_dict = self.characterize_slot(ds.name)
                        deeper_triple = self.create_triple(f"{type_query_variable}_{sv['slot_slug']}", deeper_slot_dict)
                        deeper_triples.append(deeper_triple)

            triple = self.create_triple(type_query_variable, sv)

            if sv['required']:
                main_pattern.add_triples(triples=[triple])
                if type_pattern:
                    main_pattern.add_nested_graph_pattern(type_pattern)
                    select_query.add_variables(variables=[
                        f"(group_concat(distinct {type_query_variable}_{sv['slot_slug']}_rdf_type; SEPARATOR='|') as {type_query_variable}_{sv['slot_slug']}_rdf_type{self.concatenation_suffix})"])
                for deeper_triple in deeper_triples:
                    select_query.add_variables(variables=[
                        f"(group_concat(distinct {deeper_triple.object}; SEPARATOR='|') as {deeper_triple.object}{self.concatenation_suffix})"])
                    deeper_pattern = SPARQLGraphPattern(optional=True)
                    deeper_pattern.add_triples(triples=[deeper_triple])
                    main_pattern.add_nested_graph_pattern(deeper_pattern)
            else:
                optional_pattern = SPARQLGraphPattern(optional=True)
                optional_pattern.add_triples(triples=[triple])
                if type_pattern:
                    optional_pattern.add_nested_graph_pattern(type_pattern)
                    select_query.add_variables(variables=[
                        f"(group_concat(distinct {type_query_variable}_{sv['slot_slug']}_rdf_type; SEPARATOR='|') as {type_query_variable}_{sv['slot_slug']}_rdf_type{self.concatenation_suffix})"])
                for deeper_triple in deeper_triples:
                    select_query.add_variables(variables=[
                        f"(group_concat(distinct {deeper_triple.object}; SEPARATOR='|') as {deeper_triple.object}{self.concatenation_suffix})"])
                    deeper_pattern = SPARQLGraphPattern(optional=True)
                    deeper_pattern.add_triples(triples=[deeper_triple])
                    optional_pattern.add_nested_graph_pattern(deeper_pattern)
                main_pattern.add_nested_graph_pattern(optional_pattern)

            if deeper_triples:
                pass  # don't include the variable in the projection
            else:
                if sv['multivalued']:
                    select_query.add_variables(variables=[
                        f"(group_concat(distinct {type_query_variable}_{sv['slot_slug']}; SEPARATOR='|') as {type_query_variable}_{sv['slot_slug']}{self.concatenation_suffix})"])
                else:
                    select_query.add_variables(variables=[f"{type_query_variable}_{sv['slot_slug']}"])
                    scalar_groupers.append(f"{type_query_variable}_{sv['slot_slug']}")

        select_query.add_group_by(group=GroupBy(variables=scalar_groupers))

        if self.target_p_o_constraint:
            target_p_o_constraint_parts = self.target_p_o_constraint.split(" ")
            constraint_p = target_p_o_constraint_parts[0]
            constraint_o = target_p_o_constraint_parts[1]
            main_pattern.add_triples(triples=[
                Triple(subject=type_query_variable, predicate=constraint_p, object=constraint_o)])

        # Set the WHERE part
        select_query.set_where_pattern(graph_pattern=main_pattern)

        # write a multi-line string to a text file
        with open(f"{self.target_class_name}.rq", "w") as f:
            f.write(select_query.get_text())

        df = get_sparql_dataframe(self.sparql_endpoint, select_query.get_text(), post=True)
        for dfc in list(df.columns):
            df = self.contract_column(df, f"{dfc}")

        df = df.dropna(axis=1, how='all')

        df.to_csv(f"{self.target_class_name}.tsv", index=False, sep="\t")

    # def write_query(self):
    #
    #     if self.schema_view.get_class(self.target_class_name).class_uri:
    #         type_query_object = self.schema_view.get_class(self.target_class_name).class_uri
    #     else:
    #         type_query_object = f"{self.default_prefix}:{self.target_class_name}"
    #     type_query = f"?{self.target_class_name} a {type_query_object} ."
    #
    #     self.triple_patterns.append(type_query)
    #
    #     for sk, sv in self.slot_dict.items():
    #         # print(f"{sk}")
    #         if sv['do_not_query']:
    #             continue
    #
    #         if sv['range_type'] == "class_definition":
    #             pass
    #         else:
    #             if self.do_group_concat:
    #                 if sv['multivalued']:
    #                     self.vars_to_select.append(
    #                         f"(group_concat(distinct ?{sv['slot_slug']} ; SEPARATOR='|') as ?{sv['slot_slug']}{self.concatenation_suffix})")
    #                 else:
    #                     self.vars_to_select.append(f"?{sv['slot_slug']}")
    #                     self.groupers.append(f"?{sv['slot_slug']}")
    #         lines = self.write_line(sv)
    #         self.triple_patterns.extend(lines)
    #
    # def write_line(self, slot_dict):
    #     # print(slot_dict)
    #     # print(f"{slot_dict['name'] = } {slot_dict['range_type'] = }")
    #
    #     if slot_dict['required']:
    #         line_prefix = ""
    #         line_suffix = ""
    #     else:
    #         line_prefix = "optional { "
    #         line_suffix = " }"
    #
    #     if slot_dict['slot_uri']:
    #         predicate = slot_dict['slot_uri']
    #     else:
    #         predicate = f"{self.default_prefix}:{slot_dict['slot_slug']}"
    #
    #     lines = [f"{line_prefix} ?{self.target_class_name} {predicate} ?{slot_dict['slot_slug']} "]
    #
    #     if slot_dict['range_type'] == "class_definition":
    #         # print(f"{slot_dict['name'] = } {slot_dict['range_type'] = }")
    #         slot_type_query = f"optional {{ ?{slot_dict['slot_slug']} a ?{slot_dict['slot_slug']}_type . }} . "
    #         self.vars_to_select.append(f"?{slot_dict['slot_slug']}_type")
    #         self.groupers.append(f"?{slot_dict['slot_slug']}_type")
    #         lines.append(slot_type_query)
    #         range_slot = self.schema_view.get_identifier_slot(slot_dict['range'])
    #         if range_slot:
    #             # range_identifier = range_slot.name
    #             # print(f"{range_identifier = }")
    #             pass
    #         else:
    #             # print(f"Also will need to account for {slot_dict['slot_slug']} -> {slot_dict['range']}'s slots")
    #             additional_slots = self.schema_view.class_induced_slots(slot_dict['range'])
    #             additional_slot_names = [i.name for i in additional_slots]
    #             for additional_slot_name in additional_slot_names:
    #                 additional_triple_pattern = f"optional {{ ?{slot_dict['slot_slug']} nmdc:{additional_slot_name} ?{slot_dict['slot_slug']}_{additional_slot_name} . }} . "
    #                 # print(f"\t{additional_triple_pattern = }")
    #                 lines.append(additional_triple_pattern)
    #                 self.vars_to_select.append(f"?{slot_dict['slot_slug']}_{additional_slot_name}")
    #                 self.groupers.append(f"?{slot_dict['slot_slug']}_{additional_slot_name}")
    #
    #     lines.append(line_suffix)
    #
    #     lines_pasted = "\n".join(lines)
    #
    #     return [lines_pasted]
    #
    # def subsequent_queries(self, subject, predicate, obj_var_name, target_class_name):
    #     print(f"subsequent_queries({subject}, {predicate}, {obj_var_name}, {target_class_name})")
    #     subsequent_slots = self.schema_view.class_induced_slots(target_class_name)
    #     for slot in subsequent_slots:
    #         print(f"slot: {slot.name}")


class QueryException(Exception):
    pass


@click.command()  # todo make the file options paths, not strings
@click.option("--concatenation-suffix", default="s")
@click.option("--do-group-concat", is_flag=True)
@click.option("--do-not-query", multiple=True)
@click.option("--graph-name", default="mongodb://mongo-loadbalancer.nmdc.production.svc.spin.nersc.gov:27017")
@click.option("--make-distinct", is_flag=True)
@click.option("--schema-file", default="nmdc_schema_accepting_legacy_ids.yaml")
@click.option("--target-class-name", default="Biosample")
@click.option("--target-p-o-constraint", default="dcterms:isPartOf nmdc:sty-11-34xj1150")
@click.option("--prefix-maps-json", default="../project/prefixmap/nmdc.yaml")
@click.option("--sparql-endpoint", default="https://graphdb-dev.microbiomedata.org/repositories/nmdc-metadata")
def main(
        concatenation_suffix,
        do_group_concat,
        do_not_query,
        graph_name,
        make_distinct,
        prefix_maps_json,
        schema_file,
        sparql_endpoint,
        target_class_name,
        target_p_o_constraint,
):
    # SETUP
    query_support = LinkMLClassSparqlQuery(
        concatenation_suffix=concatenation_suffix,
        do_group_concat=do_group_concat,
        do_not_query=do_not_query,
        graph_name=graph_name,
        make_distinct=make_distinct,
        prefix_maps_json=prefix_maps_json,
        schema_file=schema_file,
        sparql_endpoint=sparql_endpoint,
        target_class_name=target_class_name,
        target_p_o_constraint=target_p_o_constraint,
    )

    query_support.populate_prefix_maps()

    query_support.class_slot_usage[target_class_name] = query_support.get_class_slot_usage(target_class_name)

    query_support.characterize_slots()

    query_support.build_with_sparql_burger()

    # # BEGIN BUILDING SPARQL QUERY
    # query_support.write_query()
    #
    # query_support.vars_to_select.sort()
    # if query_support.make_distinct:
    #     select_prefix = f"select distinct"
    # else:
    #     select_prefix = "select"
    #
    # select_prefix = f"{select_prefix} (str(?{query_support.target_class_name}) as ?{query_support.target_class_name}_str)"
    #
    # query_support.vars_to_select = [select_prefix] + query_support.vars_to_select
    # assembled_select_line = " ".join(query_support.vars_to_select)
    # assembled_select_line = f"{assembled_select_line} where {{"
    # if query_support.graph_name:
    #     assembled_select_line = f"{assembled_select_line} graph <{query_support.graph_name}> {{"
    # else:
    #     assembled_select_line = f"{assembled_select_line}"
    #
    # query_support_string_lines = []
    #
    # query_support_string_lines.append(f"{assembled_select_line}")
    #
    # query_support.triple_patterns.sort()
    # for i in query_support.triple_patterns:
    #     query_support_string_lines.append(i)
    #
    # if target_p_o_constraint:
    #     query_support_string_lines.append(f"?{query_support.target_class_name} {target_p_o_constraint} . ")
    #
    # query_support_string_lines.append("}")
    #
    # if query_support.graph_name:
    #     query_support_string_lines.append("}")
    #
    # if query_support.groupers:
    #     query_support.groupers = [f"?{query_support.target_class_name}"] + query_support.groupers
    #     grouping_line = f"group by {' '.join(query_support.groupers)}"
    #     query_support_string_lines.append(grouping_line)
    #
    # query_support_string = "\n".join(query_support_string_lines)
    # query_support_string = query_support.prefixes_string + "\n" + query_support_string
    # # END BUILDING SPARQL QUERY
    #
    # # print("\n")
    # # print(query_support_string)
    #
    # # QUERY GETS EXECUTED HERE
    # df = get_sparql_dataframe(sparql_endpoint, query_support_string, post=True)
    # # END OF QUERY EXECUTION
    #
    # # BEGIN ENHANCING DATAFRAME
    # # contract IRIs to CURIEs based on the object's ???
    # for dfc in list(df.columns):
    #     df = query_support.contract_column(df, f"{dfc}")
    #
    # # add a column to report the constraint used
    # if target_p_o_constraint:
    #     target_p_o_constraint_parts = target_p_o_constraint.split(" ")
    #     constraint_label = target_p_o_constraint_parts[0]
    #     constraint_label = replace_colons_and_whitespace(constraint_label)
    #     constraint_value = target_p_o_constraint_parts[1]
    #     # df[constraint_label] = constraint_value # inefficient according to this warning: ???
    #     new_column = pd.Series([constraint_value] * len(df), name=f"{target_class_name}_{constraint_label}")
    #     df = pd.concat([df, new_column], axis=1)
    #
    # # remove empty columns
    # df = df.dropna(axis=1, how='all')
    #
    # # write to TSV
    # df.to_csv(f"{target_class_name}.tsv", index=False, sep="\t")


if __name__ == "__main__":
    main()
