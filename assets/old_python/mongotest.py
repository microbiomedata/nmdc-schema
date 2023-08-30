from pymongo import MongoClient
from pymongo.errors import OperationFailure

host = "localhost"
port = "27777"
username = "mam"
password = "record-violet-cogito-041"
auth_source = "admin"
auth_mechanism = "SCRAM-SHA-256"
direct_connection = "true"  # or "false" based on your directConnection value

# Construct the server URI
server_uri = (f"mongodb://{username}:{password}@{host}:{port}" +
              f"/?authSource={auth_source}&authMechanism={auth_mechanism}&directConnection={direct_connection}")

# Replace <server_uri> with your MongoDB server URI
client = MongoClient(server_uri)

# List available database names
database_names = client.list_database_names()
print("Available databases:", database_names)

# Replace "your_database" with the actual name of your database
db_name = "nmdc"
db = client[db_name]

# List collection names in the connected database
collection_names = db.list_collection_names()
print("Collection names:", collection_names)

collections = db.list_collections()

for collection_info in collections:
    if collection_info["type"] == "view":
        print(f"Collection '{collection_info['name']}' is a view.")
    else:
        print(f"Collection '{collection_info['name']}' is a collection.")
        collection_name = collection_info['name']
        print(f"Checking permissions for collection '{collection_name}'...")
        collection = db[collection_name]
        try:
            document = collection.find_one(max_time_ms=500)
            if document is not None:
                print(f"You have read permission for collection '{collection_name}'.")
        except OperationFailure as e:
            if "not authorized" in str(e):
                print(f"You do not have read permission for collection '{collection_name}'.")

# Close connection
client.close()
