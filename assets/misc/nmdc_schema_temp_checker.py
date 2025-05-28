from linkml_runtime import SchemaView
from src.scripts.make_typecode_to_class_map import get_collection_names_for_class_name
from nmdc_api_utilities.collection_search import CollectionSearch
import pandas as pd

schema_url = "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/refs/heads/main/nmdc_schema/nmdc_materialized_patterns.yaml"

schema_view = SchemaView(schema_url)

class_names = list(schema_view.all_classes().keys())

class_names.sort()

# make dictionary of class names, with slots, ranges, the collections the class belongs to
class_dict = {}
for c_name in class_names:

    class_dict[c_name] = {}

    #get specifics of this class in the schema
    ic = schema_view.induced_class(c_name)

    #what collections does this class belong to?
    collections = get_collection_names_for_class_name(c_name)
    
    #iterate through attributes for this class as key value pairs
    for ican, icav in ic.attributes.items():

        #record if attributes have a range constrained by a class in the schema (slots)
        if icav.range in class_names:
            class_dict[c_name][ican] = {"range": icav.range, 'collections': collections}
        else:
            class_dict[c_name][ican] = {"range": None, 'collections': collections}

# make dataframe
class_dfs = []
for c_name in class_dict.keys():
    if len(class_dict[c_name]) == 0:
        continue
    df = pd.DataFrame.from_dict(class_dict[c_name], orient='index')
    df['class'] = c_name
    df = df.explode('collections')
    df = df.reset_index()
    df = df.rename(columns={'index': 'slot'})
    df = df[['class', 'slot', 'range', 'collections']]
    class_dfs.append(df)
class_df = pd.concat(class_dfs, ignore_index=True)

# only keep rows where slot contains 'temp'
class_df = class_df[class_df['slot'].str.contains("temp")].reset_index(drop=True)

print(class_df)

#what does the data look like in mongo for these slots?
units_used = {}
records_no_units = {}
records = {}
for index, row, in class_df.iterrows():

    #get info from API on the slots/classes
    collection_client = CollectionSearch(row['collections'])
    mongo_collect_res = collection_client.get_record_by_filter(filter=f'{{"{row["slot"]}":{{"$exists":"True"}}, "type":{{"$regex":"^nmdc:{row["class"]}"}}}}',fields=str(row["slot"]))
    mongo_collect_res = pd.json_normalize(mongo_collect_res)

    #how many records have this class/slot populated?
    records[index] = len(mongo_collect_res)

    #how many of those records are missing a unit and may need it to be inferred + changesheet?
    if records[index] > 0 :
        if str(row['slot']) + '.has_unit' in mongo_collect_res.columns:
            records_w_units = mongo_collect_res.dropna(subset=[str(row['slot']) + '.has_unit']).shape[0]
        else:
            records_w_units = 0
        records_no_units[index] = records[index]-records_w_units

        #what are the units being used?
        units = mongo_collect_res[str(row['slot']) + '.has_unit'].unique()
        units_used[index] = units

class_df['records_w_slot_populated'] = pd.Series(records)
class_df['units_used_for_slot'] = pd.Series(units_used)
class_df['slotpopulated_but_missingunit'] = pd.Series(records_no_units)

# arrange by class and slot
class_df = class_df.sort_values(by=['class', 'slot'])

class_df.to_csv("nmdc_schema_class_tempslot.csv",index=False)
