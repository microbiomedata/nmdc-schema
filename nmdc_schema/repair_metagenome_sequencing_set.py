import json

update_list = []

file = open("/Users/aclum/Downloads/nmdc.metagenome_sequencing_activity_set.csv", "r")

for i in file.readlines():
    i = i.strip()
    value_array = i.split(",")
    update_list.append(
        {"q": {"id": value_array[1]}, "u": {"$set": {"has_input": [value_array[2]]}}}
    )

# print(update_list)
json_body = {"update": "metagenome_sequencing_activity_set", "updates": update_list}

with open("mg_seq_repair_inputs.json", "w") as f:
    json.dump(json_body, f)
