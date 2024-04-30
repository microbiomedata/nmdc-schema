import csv
import json
import sys

# Read JSON data from stdin
json_data = sys.stdin.read()
data = json.loads(json_data)

# Create CSV writer for stdout
tsv_writer = csv.writer(sys.stdout, delimiter='\t')

# Write header row
header = ["ns", "size", "count", "avgObjSize", "storageSize", "totalIndexSize", "totalSize", "scaleFactor"]
tsv_writer.writerow(header)

# Write data rows
for item in data:
    row = [item.get('ns', '')]  # Get 'ns' with empty string if missing

    # Get storageStats values if present, otherwise use empty strings
    storage_stats = item.get('storageStats', {})
    row += [storage_stats.get(key, '') for key in header[1:]]

    tsv_writer.writerow(row)
