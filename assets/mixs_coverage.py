# wasn't able to curl https://docs.google.com/spreadsheets/d/1cMlPKgjZh-v21aMYCm9x1TxzE5BwGQptBQcvuaYAtC8/edit#gid=1742830620
# even after having reformating the url
import csv
import pprint

in_file = "../assets/sheets-for-nmdc-submission-schema_import_slots_regardless.tsv"
out_file = "../assets/mixs_coverage.tsv"

# open data_file with a DictReader
min_list = []

with open(in_file, "r") as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        # min_dict = {k: row[k] for k in ('slot', 'destination class')}
        raw_dc = row['destination class']
        dc_list = raw_dc.split("|")
        for i in dc_list:
            min_list.append({"slot": row['slot'], "destination class": i})

# use DictWriter to save min_list to a new tsv file
with open(out_file, "w") as f:
    writer = csv.DictWriter(f, fieldnames=['slot', 'destination class'], delimiter="\t")
    writer.writeheader()
    writer.writerows(min_list)
