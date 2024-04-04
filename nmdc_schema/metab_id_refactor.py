from dataclasses import dataclass, field, asdict
import hashlib
from pathlib import Path
import os
from pprint import pprint
import re
from typing import List
import json

from dotenv import load_dotenv
import nmdc_schema.nmdc as nmdc
import oauthlib
from pymongo import MongoClient
from bson import json_util

import requests_oauthlib
import yaml

from bson import ObjectId
 
class JSONEncoder(json.JSONEncoder):
    def default(self, item):
        if isinstance(item, ObjectId):
            return str(item)
        return json.JSONEncoder.default(self, item)

envfile_path = "nmdc_mongo.env"

load_dotenv(envfile_path)
#nersc ssh tunnel required to connect to mongo
#ssh -L 37020:mongo-loadbalancer.nmdc-napa.production.svc.spin.nersc.org:27017 -o ServerAliveInterval=60 corilo@perlmutter.nersc.gov

napa_mongo_pw = 'xxxxxxxxxxxxxx'
#print("napa_mongo_pw:", os.environ['MONGO_NAPA_PW'])
#pprint(napa_mongo_pw)
#napa_mongo='mongodb://root:'+napa_mongo_pw+'@mongo-loadbalancer.nmdc-napa.production.svc.spin.nersc.org:27017/?authSource=admin'
napa_mongo='mongodb://xxxxxxx:'+napa_mongo_pw+'@localhost:37020/?authSource=admin'

#connection = MongoClient()
#db = connection.napa_mongo
#pprint(napa_mongo)

#connect to mongo
client = MongoClient(napa_mongo, directConnection=True)

#list database names
#for db in client.list_database_names():
#   pprint("db name: {} ".format(db))

#set mongo database name to nmdc'
mydb =client['nmdc']

#list collections
#for coll in mydb.list_collection_names():
#   pprint("collection name: {} ".format(coll))

dms_raw_old_ids = []

# omicsProcessing update, has_output --> raw data 
# omicsProcessing update, alternative_identifier --> nom_analysis_activity.was_informed_by

# nom_analysis_activity --> has_input (new raw file or update ID) 
# nom_analysis_activity --> has_output (data product file, update ID)
# nom_analysis_activity --> replace ids
# nom_analysis_activity --> was_informed_by -- id from alternative indetifier omics Processing
# dataObject --> replace id, and add alternative identifier, emsl:60592345


def mint_nmdc_payload(type, how_many):
   return {'schema_class' : {'id': type}, 'how_many': how_many}

@dataclass
class NMDC_Mint:
    
    schema_class: dict = field(default_factory= lambda: {
        'schema': None,
    })
    how_many:int = 1

    @property
    def __dict__(self):
        return asdict(self)

    @property
    def json(self):
        return json.dumps(self.__dict__)
    
@dataclass
class DataObject:
    
    nom_raw_data_object_type:str = "Direct Infusion FT ICR-MS Raw Data"
    nom_raw_data_object_description:str = "Raw 21T Direct Infusion Data"
    nom_dp_data_object_type:str = "FT ICR-MS Analysis Results"
    nom_dp_data_object_description:str = "EnviroMS FT ICR-MS natural organic matter workflow molecular formula assignment output details"

    metab_raw_data_object_type:str = "Direct Infusion FT ICR-MS Raw Data"
    metab_raw_data_object_description:str = "Raw 21T Direct Infusion Data"
    metab_dp_data_object_type:str = "GC-MS Metabolomics Results"
    metab_dp_data_object_description:str = "MetaMS GC-MS metabolomics output detail CSV file"

@dataclass
class NMDC_Types: 
    
    BioSample:str = "nmdc:Biosample"
    OmicsProcessing:str = "nmdc:OmicsProcessing"
    NomAnalysisActivity:str = "nmdc:NomAnalysisActivity"
    MetabolomicsAnalysisActivity:str = "nmdc:MetabolomicsAnalysisActivity"
    DataObject:str = "nmdc:DataObject"

def fix_nom_again():
    
    nom_activities_set = mydb.get_collection('nom_analysis_activity_set')
    data_object_set = mydb.get_collection('data_object_set')
    omics_processing_set = mydb.get_collection('omics_processing_set')

    processed_data_docs = set()
    raw_data_docs = set()
    n = 0
    for nom_activities_doc in nom_activities_set.find():
        
        n = n + 1
        omics_processing_doc = omics_processing_set.find_one({'id':nom_activities_doc.get('was_informed_by')})  

        processed_data_regx_string = '(^{})(.*[.]csv$).*$'.format(omics_processing_doc.get("name"))

        processed_data_regx = re.compile(processed_data_regx_string)
               
        for data_object_doc in data_object_set.find({"name":  {"$regex":processed_data_regx }}):
            
            processed_data_docs.add(data_object_doc.get("name"))
            
            #pprint(data_object_doc)

        raw_data_regx_string = '(^{})(.*[.](d|raw)$).*$'.format(omics_processing_doc.get("name"))

        raw_data_regx = re.compile(raw_data_regx_string)

        for data_object_doc in data_object_set.find({"name":  {"$regex":raw_data_regx }}):
            
            raw_data_docs.add(data_object_doc.get("name"))

    print(f'NA{n} OP{n} PD{len(processed_data_docs)} RD{len(raw_data_docs)}' )

def check_nom_records():
    
    data_products_id = set()
    raw_products_id = set()
    i = 0
    r = 0
    p = 0
    nom_activities_set = mydb.get_collection('nom_analysis_activity_set')
    data_object_set = mydb.get_collection('data_object_set')
    omics_processing_set = mydb.get_collection('omics_processing_set')

    for nom_activities_doc in nom_activities_set.find():
        
        omics_processing_doc = omics_processing_set.find_one({'id':nom_activities_doc.get('was_informed_by')})  
        
        raw_products_id.add(nom_activities_doc.get("has_input")[0])
        data_products_id.add(nom_activities_doc.get("has_output")[0])
        
        i = i + 1
        #omics_processing_set.update_one(omics_processing_doc, update_dict)
        raw_data_cursor = data_object_set.find({'id' : nom_activities_doc.get("has_input")[0]})
        process_data_cursor = data_object_set.find({'id' : nom_activities_doc.get("has_output")[0]})
        raw_data = [j for j in raw_data_cursor]
        processed_data = [j for j in process_data_cursor]
        
        if not processed_data[0].get('name').endswith('.csv'):
            pprint(processed_data)
        if raw_data:
            r = r +1
        if processed_data:
            p = p + 1
        
        #omics_processing_set.update_one(omics_processing_doc, update_dict)
    print(f'OP{i} AC{i} DP{len(data_products_id)} DP{len(raw_products_id)} FR{r} FP{p}')

def check_metab_records():
    
    data_products_id = set()
    raw_products_id = set()
    i = 0
    r = 0
    p = 0
    metab_activities_set = mydb.get_collection('metabolomics_analysis_activity_set')
    data_object_set = mydb.get_collection('data_object_set')
    omics_processing_set = mydb.get_collection('omics_processing_set')

    for metab_activities_doc in metab_activities_set.find():
        
        omics_processing_doc = omics_processing_set.find_one({'id':metab_activities_doc.get('was_informed_by')})  
        
        metab_activities_doc.pop('has_metabolite_quantifications')
        raw_products_id.add(metab_activities_doc.get("has_input")[0])
        data_products_id.add(metab_activities_doc.get("has_output")[0])
        
        pprint(omics_processing_doc)
        pprint(metab_activities_doc)

        raw_data_cursor = data_object_set.find({'id' : metab_activities_doc.get("has_output")[0]})
        process_data_cursor = data_object_set.find({'id' : metab_activities_doc.get("has_input")[0]})
        raw_data = [j for j in raw_data_cursor]
        processed_data = [j for j in process_data_cursor]
        
        if raw_data:
            r = r +1

        if processed_data:
            p = p + 1
        
        i = i + 1
        #omics_processing_set.update_one(omics_processing_doc, update_dict)
    print(f'OP{i} AC{i} DP{len(data_products_id)} DP{len(raw_products_id)} FR{r} FP{p}')

def update_has_calibration_object(has_calibration_id):

    data_object_set = mydb['data_object_set']

    for data_object_obj in data_object_set.find({'id' : has_calibration_id}):
                
        new_has_calibration_id = mint_nmdc_id(NMDC_Types.DataObject, 1)[0]
        
        has_calibration_data_update = { "$set": { "id": new_has_calibration_id } }
        
        data_object_set.update_one(data_object_obj, has_calibration_data_update)

def rename_alternative_identifiers():

    metab_activities_set = mydb.get_collection('nom_analysis_activity_set')
    data_object_set = mydb.get_collection('data_object_set')
    
    for metab_activities_doc in metab_activities_set.find({}):
        for has_input in metab_activities_doc["has_input"]:

            #pprint(type(metab_activities_doc.get('was_informed_by')))
            if not isinstance(metab_activities_doc.get('was_informed_by'), str):
                
                print(metab_activities_doc.get('was_informed_by'))        

                was_informed_by = metab_activities_doc.get('was_informed_by')[0]
               
                obj_update = { '$set': { 'was_informed_by': str(was_informed_by) } }
                
                metab_activities_set.update_one(metab_activities_doc, obj_update)
                
            for data_object_obj in data_object_set.find({'id' : has_input}):
                
                print(data_object_obj.get("alternative_identifiers"))
                
                data_object_obj_update = { "$set": { "alternative_identifiers": data_object_obj.get("alternative_identifiers")[0] } }

                data_object_set.update_one(data_object_obj, data_object_obj_update)

                data_object_obj_removal = { "$unset": { "alternative_identifiers": "" } }

                data_object_set.update_one(data_object_obj, data_object_obj_removal)

                new_has_calibration_id = mint_nmdc_id(NMDC_Types.DataObject, 1)[0]

                new_processed_data_id = mint_nmdc_id(NMDC_Types.DataObject, 1)[0]
                
                processed_data_update = { "$set": { "id": new_has_calibration_id } }
                
                print(processed_data_update)    
                
                data_object_set.update_one(data_object_obj, processed_data_update)

            metab_activity_update = { "$set": { "has_calibration": new_has_calibration_id } }
            print(metab_activity_update)    
            metab_activities_set.update_one(metab_activities_doc, metab_activity_update)

def fix_rachel_data():

    nom_analysis_activities = mydb.get_collection('nom_analysis_activity_set')
    data_object_set = mydb.get_collection('data_object_set')
    
    for nom_activities_doc in nom_analysis_activities.find({}):
        
        has_input = nom_activities_doc.get('has_input')

        has_output = nom_activities_doc.get('has_output')

        data_docs = data_object_set.find({'id' : has_output[0]})
    
        for doc in data_docs:
            if not doc.get('name').endswith('.csv'):
                print(doc)

def fix_ophans_activities():

    i = 0
    metab_activities_set = mydb.get_collection('metabolomics_analysis_activity_set')
    data_object_set = mydb.get_collection('data_object_set')
    omics_processing_set = mydb.get_collection('omics_processing_set')

    deleted_metab_activities = []
    deleted_metab_dataobjs = []
    for metab_activities_doc in metab_activities_set.find({}):
        metab_activities_doc.pop('has_metabolite_quantifications')
        for has_input in metab_activities_doc["has_input"]:
                    
            if has_input.startswith('emsl'):
                
                pprint(metab_activities_doc)
                
                metab_activities_set.delete_one(metab_activities_doc)
                deleted_metab_activities.append(metab_activities_doc)

                for data_file_doc in data_object_set.find({'id' : metab_activities_doc.get('has_output')[0] }):
                    i = i + 1
                    print(i)
                    print(data_file_doc)
                    deleted_metab_dataobjs.append(data_file_doc)
                    data_object_set.delete_one(data_file_doc)
    
    json.dump(deleted_metab_activities, open('./deleted_metab_analysis_activity.json', 'w'), cls=JSONEncoder)
    json.dump(deleted_metab_dataobjs, open('./deleted_metab_dataobjs.json', 'w'), cls=JSONEncoder)

def fix_raw_data_relationship():
    
    import re

    nom_analysis_activities = mydb.get_collection('nom_analysis_activity_set')
    data_object_set = mydb.get_collection('data_object_set')
    omics_processing_set = mydb.get_collection('omics_processing_set')
    
    i = 0
    for nom_activities_doc in nom_analysis_activities.find({}):
        for has_input in nom_activities_doc["has_input"]:
                #pprint(nom_activities_doc)
                has_raw_data = data_object_set.find({'id' : has_input})
                list_raw_files = list(has_raw_data)
                
                if len(list_raw_files) < 1:
                    
                    has_output = nom_activities_doc.get('has_output') #should be has input

                    has_input = nom_activities_doc.get('has_input') # this is the current id have to go into the data_object csv and be the has_output

                    updated_flipped_records_nom =  { "$set": { "has_input": has_output, "has_output" : has_input} }

                    nom_analysis_activities.update_one(nom_activities_doc, updated_flipped_records_nom)

                    omics_processing_docs = omics_processing_set.find({'id' : nom_activities_doc.get("was_informed_by")})
                    
                    for omics_processing_doc in omics_processing_docs:
                        
                        #print(omics_processing_doc.get("name"))
                        
                        #print(omics_processing_doc.get("has_output")[0], has_input)
                        #pprint(omics_processing_doc)
                        #pprint(nom_activities_doc)
                        #print()
                        
                        regx_string = '(^{})(.*[.]csv$).*$'.format(omics_processing_doc.get("name"))
                        
                        regx = re.compile(regx_string)
                        
                        already_used = False
                        
                        for data_object_doc in data_object_set.find({"name":  {"$regex":regx }}):
                            
                            pprint(data_object_doc)
                            
                            for nom_activities_doc in nom_analysis_activities.find({"has_output": data_object_doc.get('id')}):

                                "this step makes sure the dataobject of the processed data is not used somewhere else"
                                #pprint(nom_activities_doc)   
                                already_used = True 

                            if not already_used:
                                
                                i = i + 1
                                
                                print(has_input, nom_activities_doc.get('id'))
                                updated_processed_data_id =  {"$set": { "id": has_input[0], "was_generated_by": nom_activities_doc.get('id')} } 

                                data_object_set.update_one(data_object_doc, updated_processed_data_id)
                            #print(omics_processing_doc.get("has_output"), has_input)
                        #    pprint(omics_processing_doc)
                        #    pprint(nom_activities_doc)
                            
                        #    for nom_activities_doc in nom_analysis_activities.find({"has" : data_object_doc.get('id')}):
                        #       
                        #        print()
                        #        print(omics_processing_doc.get("has_output"), has_input)
                        #        pprint(data_object_doc)
                        #        pprint(nom_activities_doc)
                        #    raw_data_update = { "$set": { "id": has_input } }
                            #data_object_set.update_one(data_object_doc, raw_data_update)

                        #    was_generate_by_update = { "$set": { "was_generated_by": omics_processing_doc.get('id') } }
                            #data_object_set.update_one(data_object_doc, was_generate_by_update)

                else:
                    #pprint([i for i in list_raw_files])
                    pass
                    #i +=1
                    #print(i) 

def delete_data_objects():
    
    data_object_set = mydb['data_object_set']

    nom_activities_path  = './nom_activities_nom_deleted.json'
   
    nom_activities = json.load(open(nom_activities_path)) 
    
    i = 0
    for nom_activitiy in nom_activities:
        
        get_data_product_data_object = {'id': nom_activitiy.get("has_input")[0]}
        
        for data_product_objectdata_doc in data_object_set.find(get_data_product_data_object):
            
            #data_object_set.delete_one(data_product_objectdata_doc)
            print(data_product_objectdata_doc)
            i += 1
    
    print(i)

def fix_omics_processing():

    nom_analysis_activities = mydb.get_collection('nom_analysis_activity_set')
    data_object_set = mydb.get_collection('data_object_set')
    omics_processing_set = mydb.get_collection('omics_processing_set')

    for nom_activities_doc in nom_analysis_activities.find():
        
        omics_processing_doc = omics_processing_set.find_one({'id':nom_activities_doc.get('was_informed_by')})  
        update_dict = { "$set": { "has_output": nom_activities_doc.get('has_input') } }
        #print(update_dict)
        pprint(omics_processing_doc)
        pprint(nom_activities_doc)
        #omics_processing_set.update_one(omics_processing_doc, update_dict)

def fix_nom_data_products():
    
    nom_analysis_activities = mydb.get_collection('nom_analysis_activity_set')
    data_object_set = mydb.get_collection('data_object_set')
    omics_processing_set = mydb.get_collection('omics_processing_set')
    
    i = 0
    k = 0
    for nom_activities_doc in nom_analysis_activities.find():
        for has_output in nom_activities_doc["has_output"]:
                #print(has_output)
                #pprint(nom_activities_doc)
                has_processed_data = data_object_set.find({'id' : has_output})
                print(nom_activities_doc)
                all_data = [j for j in has_processed_data]
                id_data = (all_data[0].get('id'))
                if not id_data:
                    i = i + 1
                    print(i)
                    #continue
                    #pprint(nom_activities_doc)
                    omics_processing_doc = omics_processing_set.find_one({'id':nom_activities_doc.get('was_informed_by')})
                    pprint(omics_processing_doc)

                    regx_string = '(^{})(.*[.]csv$).*$'.format(omics_processing_doc.get("name"))
                        
                    regx = re.compile(regx_string)
                        
                    already_used = False
                        
                    for data_object_doc in data_object_set.find({"name":  {"$regex":regx }}):
                        k = k + 1
                        
                        update_dict = { "$set": { "id": has_output } }

                        print(data_object_doc)

                        #data_object_set.update_one(data_object_doc, update_dict)
    print('I', i)

def fix_nom_analysis_activities():

    nom_analysis_activities = mydb.get_collection('nom_analysis_activity_set')
    data_object_set = mydb.get_collection('data_object_set')
    omics_processing_set = mydb.get_collection('omics_processing_set')
    
    i = 0
    for nom_activities_doc in nom_analysis_activities.find():
        for has_input in nom_activities_doc["has_output"]:
                
                #pprint(nom_activities_doc)
                has_raw_data = data_object_set.find({'id' : has_input})
                
                all_data = [j for j in has_raw_data]
                
                if not all_data:
                    i +=1
                    print(i)
                    #continue
                    pprint(nom_activities_doc)
                   
                if nom_activities_doc.get('has_output')[0].startswith('nmdc:wfnom'):
                    
                    pass
                    #pprint(nom_activities_doc)
                    #pprint(nom_activities_doc)
                    
                    #new_processed_data_id = mint_nmdc_id(NMDC_Types.DataObject, 1)[0]
                    
                    #nom_activities_update = { "$set": { "has_output":[new_processed_data_id] } }
                    
                    #print(nom_activities_update)
                    #nom_analysis_activities.update_one(nom_activities_doc, nom_activities_update)
                    
                    #processed_data_update = { "$set": { "id": new_processed_data_id } }

                    
                    #for data_object_obj in has_processed_data:
                    #    pass
                    #    pprint(data_object_obj)
                    #     print(processed_data_update)
                    #     data_object_set.update_one(data_object_obj, processed_data_update)

def fix_metab_analysis_activities():

    metab_activities_set = mydb.get_collection('metabolomics_analysis_activity_set')
    data_object_set = mydb.get_collection('data_object_set')
    omics_processing_set = mydb.get_collection('omics_processing_set')

    for metab_activities_doc in metab_activities_set.find({}):
        for has_input in metab_activities_doc["has_input"]:
                    
            if not has_input.startswith('emsl'):    
                
                #for omics_processing_docs in omics_processing_set.find({}):
                #    has_output = omics_processing_docs.get("has_output")
                #    if has_output:
                 #       if has_input in has_output:
                 #           pprint(omics_processing_docs)
                #pprint(metab_activities_doc.get('id'))
                #new_metab_analys_id = mint_nmdc_id(NMDC_Types.MetabolomicsAnalysisActivity, 1)[0]

                metab_activities_doc.pop("has_metabolite_quantifications")
                #data_obj_id = (metab_activities_doc.get('has_output'))[0]
                pprint(metab_activities_doc)
                
                for data_object_obj in data_object_set.find({'id' : metab_activities_doc.get('has_calibration')}):
                    pass
                    pprint(data_object_obj)
                    #new_has_calibration_id = mint_nmdc_id(NMDC_Types.DataObject, 1)[0]

                #    new_processed_data_id = mint_nmdc_id(NMDC_Types.DataObject, 1)[0]
                    
                    #processed_data_update = { "$set": { "id": new_has_calibration_id } }
                    
                #    print(processed_data_update)    
                    
                    #data_object_set.update_one(data_object_obj, processed_data_update)

                #metab_activity_update = { "$set": { "has_calibration": new_has_calibration_id } }
                #print(metab_activity_update)    
                #metab_activities_set.update_one(metab_activities_doc, metab_activity_update)

def update_metab_omics_processing():

    activity_without_omics_processing = []
    activity_with_omics_processing = []
    omics_processing_with_activities = []
    omics_processing_set = mydb.get_collection('omics_processing_set')

    metab_activities_set = mydb.get_collection('metabolomics_analysis_activity_set')

    for metab_activities_doc in metab_activities_set.find({}):
    
        for has_input in metab_activities_doc["has_input"]:
                
                if has_input.startswith('emsl'):

                    get_parent_omics_processing = { "has_output" : metab_activities_doc["has_input"] }

                    omics_processing_docs = [omics_processing_doc for omics_processing_doc in omics_processing_set.find(get_parent_omics_processing)]
                    
                    if not omics_processing_docs:
                        
                        del(metab_activities_doc["has_metabolite_quantifications"])
                        activity_without_omics_processing.append(metab_activities_doc)

                    for omics_processing_doc in omics_processing_docs:
                        
                        new_raw_file_id = mint_nmdc_id(NMDC_Types.DataObject, 1)[0]

                        omics_processing_update = { "$set": { "has_output": [new_raw_file_id]} }    

                        omics_processing_set.update_one(omics_processing_doc, omics_processing_update)

                        new_omics_processing_id = omics_processing_doc['id']

                        new_data_product_id = mint_nmdc_id(NMDC_Types.DataObject, 1)[0]

                        metab_new_id = mint_nmdc_id(NMDC_Types.MetabolomicsAnalysisActivity, 1)[0]

                        update_has_calibration_object(metab_activities_doc.get('has_calibration'))

                        update_data_products(new_data_product_id, new_raw_file_id, omics_processing_doc.get("has_output"), metab_activities_doc, new_omics_processing_id, metab_new_id)
                        
                        metab_activity_update = { "$set": { "id": metab_new_id , "has_output":[new_data_product_id],
                                                "has_input":[new_raw_file_id], "was_informed_by": new_omics_processing_id} }

                        
                        activity_with_omics_processing.append(metab_activities_doc)
                        omics_processing_with_activities.append(omics_processing_doc)
                        metab_activities_set.update_one(metab_activities_doc, metab_activity_update)
    
    json.dump(activity_with_omics_processing, open('./metab_analysis_activity_with_omics_porcessing.json', 'w'), cls=JSONEncoder)
    json.dump(omics_processing_with_activities, open('./metab_omics_porcessing_with_analysis_activity.json', 'w'), cls=JSONEncoder)
    json.dump(activity_without_omics_processing, open('./metab_analysis_activity_without_omics_porcessing.json', 'w'), cls=JSONEncoder)

    omics_processing_to_delete = [] 
    for omics_processing_doc in omics_processing_set.find({}):
        
        #print(nom_activities_doc)
        has_outputs = omics_processing_doc.get("has_output")
        if has_outputs:
            if omics_processing_doc.get("processing_institution") == 'EMSL':
                for has_output in has_outputs:
                    if has_output.startswith('emsl'):
                        if omics_processing_doc['omics_type']['has_raw_value'] != 'Lipidomics':
                            #pprint(omics_processing_doc)     
                            omics_processing_to_delete.append(omics_processing_doc)                   

    json.dump(omics_processing_to_delete, open('./metab_omics_porcessing_without_analysis_activity.json', 'w'), cls=JSONEncoder)

def update_nom_omics_processing(raw_file_path=None):

    omics_processing_set = mydb.get_collection('omics_processing_set')

    nom_activities_set = mydb.get_collection('nom_analysis_activity_set')
    
    get_old_activities={ "id" : {"$regex":"^emsl" } }
    
    data_object_set = mydb['data_object_set']
    
    i = 0  
    j = 0
    k = 0 
    omics_processing_to_delete = [] 
    for omics_processing_doc in omics_processing_set.find({}):
        
        #print(nom_activities_doc)
        has_outputs = omics_processing_doc.get("has_output")
        if has_outputs:
            if omics_processing_doc.get("processing_institution") == 'EMSL':
                for has_output in has_outputs:
                    if has_output.startswith('emsl'):
                        if omics_processing_doc.get("description") == 'High resolution MS spectra only':
                            raw_file_id = omics_processing_doc.get("has_output")[0]
                            get_raw_file_data_object = { "id" : raw_file_id }
                            omics_processing_to_delete.append(omics_processing_doc)
                            #omics_processing_set.delete_one(omics_processing_doc)
                            i = i + 1
                            #raw_object_docs = [raw_objectdata_doc for raw_objectdata_doc in data_object_set.find(get_raw_file_data_object)] 
                            #for raw_object_doc in raw_object_docs:
                            #  j = j + 1
                            #print(raw_object_doc)
                        # i = i + 1
                            
                            #for nom_activities_doc in nom_activities_set.find({'was_informed_by': omics_processing_doc.get("alternative_identifiers")[0]}):
                            #    k = k + 1
                            #    #print(nom_activities_doc)                                              
                            
    print(i,j,k, 'Omics Processing')
    json.dump(omics_processing_to_delete, open('./omics_processing_nom_deleted.json', 'w'), cls=JSONEncoder)
    i = 0
    
    nom_activities_to_delete = []
    for nom_activities_doc in nom_activities_set.find({}):
        
        #print(nom_activities_doc)
        for has_input in nom_activities_doc["has_input"]:
            
            if has_input.startswith('emsl'):
                
                pprint(nom_activities_doc) #, nom_activities_doc['id'], nom_activities_doc.get("has_input"))
                nom_activities_to_delete.append(nom_activities_doc)
                #nom_activities_set.delete_one(nom_activities_doc)
                #print(nom_activities_doc.get("was_informed_by"))
                i = i + 1
                #get_parent_omics_processing ={ "has_output" : nom_activities_doc["has_input"] }
                get_parent_omics_processing ={ "alternative_identifiers" : nom_activities_doc["was_informed_by"] }

                #always going to be one omics processing
                
                for omics_processing_doc in omics_processing_set.find(get_parent_omics_processing):   
                    
                    print(omics_processing_doc)
                    
                    new_raw_file_id = mint_nmdc_id(NMDC_Types.DataObject, 1)[0]

                    omics_processing_update = { "$set": { "has_output": [new_raw_file_id]} }    

                    omics_processing_set.update_one(omics_processing_doc, omics_processing_update)

                    new_omics_processing_id = omics_processing_doc['id']

                    new_data_product_id = mint_nmdc_id(NMDC_Types.DataObject, 1)[0]

                    nom_new_id = mint_nmdc_id(NMDC_Types.NomAnalysisActivity, 1)[0]

                    update_data_products(new_data_product_id, new_raw_file_id, omics_processing_doc.get("has_output"), nom_activities_doc, new_omics_processing_id, nom_new_id)
                    
                    nom_activity_update = { "$set": { "id": nom_new_id , "has_output":[new_data_product_id],
                                            "has_input":[new_raw_file_id], "was_informed_by": new_omics_processing_id}, "$unset": {"has_calibration": ""} } 

                    nom_activities_set.update_one(nom_activities_doc, nom_activity_update)
        
       
    print(i, 'NOM Activities')
    json.dump(nom_activities_to_delete, open('./nom_activities_nom_deleted.json', 'w'),  cls=JSONEncoder)

def update_data_products(new_data_product_id, new_raw_file_id, old_dms_id, activities_doc, new_omics_processing_id:str, new_activity_id, raw_file_path:Path=None):
   
  raw_file_id = activities_doc.get("has_input")[0]

  dataproduct_id = activities_doc.get("has_output")[0]

  data_object_set = mydb['data_object_set']

  get_raw_file_data_object = { "id" : raw_file_id }
  get_data_product_data_object = { "id" : dataproduct_id }

  raw_object_docs = [raw_objectdata_doc for raw_objectdata_doc in data_object_set.find(get_raw_file_data_object)] 

  for data_product_objectdata_doc in data_object_set.find(get_data_product_data_object):
      
      data_product_object_update = { "$set": { "id": new_data_product_id, "was_generated_by": new_activity_id} } 

      data_object_set.update_one(data_product_objectdata_doc, data_product_object_update )

  if raw_object_docs:
     
     raw_object_update = { "$set": { "id": new_raw_file_id, 'alternative_identifiers': [old_dms_id]} }    
     
     data_object_set.update_one(raw_object_docs[0], raw_object_update )

  else:
     
     raw_file_name = activities_doc.get('name') 
     
     dms_raw_old_ids.append(old_dms_id)
     
     new_raw_data_object = get_raw_data_object(raw_file_name,
                                    was_generated_by=new_omics_processing_id, 
                                    alternative_identifier = old_dms_id,
                                    data_object_type =DataObject.nom_raw_data_object_type,
                                    description =DataObject.nom_raw_data_object_description)

     data_object_set.insert_one(new_raw_data_object)

def mint_nmdc_id(type:NMDC_Types, how_many:int = 1) -> List[str]: 
    
    config = yaml.safe_load(open('./config.yaml','r'))
    client = oauthlib.oauth2.BackendApplicationClient(client_id=config['client_id'])
    oauth = requests_oauthlib.OAuth2Session(client=client)
    #print('XXXXX', config['client_id'])
    #print('XXXXX', config['client_secret'])
    token = oauth.fetch_token(token_url='https://api.microbiomedata.org/token',
                              client_id=config['client_id'], 
                              client_secret=config['client_secret'])

    nmdc_mint_url = "https://api.microbiomedata.org/pids/mint"
    
    payload = mint_nmdc_payload(type, how_many)
    #response = s.post(nmdc_mint_url, data=payload.json, )
    #list_ids = response.json()
    response = oauth.post(nmdc_mint_url, data=json.dumps(payload))
    list_ids = response.json()
    #print(list_ids)
    return list_ids
    
def get_raw_data_object(raw_file_name, was_generated_by:str, alternative_identifier,

                data_object_type:str, description:str ) -> nmdc.DataObject:
    
    nmdc_id = mint_nmdc_id(NMDC_Types.DataObject)[0]

    data_dict = {
                'id': nmdc_id,
                "name": raw_file_name,
                #"file_size_bytes": file_path.stat().st_size,
                #"md5_checksum": hashlib.md5(file_path.open('rb').read()).hexdigest(),
                "was_generated_by": was_generated_by, #omics processing id
                "data_object_type": data_object_type,
                "description": description,
                "type": NMDC_Types.DataObject,
                "alternative_identifiers" : [alternative_identifier]
                } 
    
    data_object = nmdc.DataObject(**data_dict)

    return data_object

check_nom_records()

#fix_nom_again()

#check_nom_records()

#check_metab_records()

#rename_alternative_identifiers()

#test()

#fix_rachel_data()

#fix_omics_processing()

#fix_nom_data_products()

#fix_nom_analysis_activities()

#fix_ophans_activities()

#update_metab_omics_processing()

#delete_data_objects()

#mint_nmdc_id(NMDC_Types.DataObject, 1)

#update_omics_processing()

#pprint(dms_raw_old_ids)

#json.dump(dms_raw_old_ids, open('./dms_raw_old_ids.json', 'w'))


