import argparse
import logging
import time
from pathlib import Path
from typing import List, Any, Tuple

import pymongo


logger = logging.getLogger(Path(__file__).name)
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler(f'{Path(__file__).stem}_{time.strftime("%Y%m%d-%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)

def args() -> Tuple[str]:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--dry-run", help="Print, but not delete, all metaP proteomics records", action="store_true"
    )
    parser.add_argument("--mongo-uri", type=str, help="MongoDB URI", required=False, default="mongodb://localhost:27017",)
    return parser.parse_args()


class NMDCAccessor:
    def __init__(self, db):
        self.db = db

    def get_documents_from_collection(self, collection_name: str) -> Any:
        collection = self.db[collection_name]
        documents = list(collection.find({}))

        logger.info(f"Found {len(documents)} documents in {collection_name}")
        return documents

    def get_matching_msgf_data_objects_records(self) -> Any:
        collection = self.db["data_object_set"]
        query = {"description": {"$regex": "MSGF"}}
        documents = collection.find(query)

        return list(documents)

    def get_matching_msgf_data_object_ids(self) -> List[str]:
        records = self.get_matching_msgf_data_objects_records()

        return [record["id"] for record in records]

    def delete_matching_records_from_ids(
        self, collection_name: str, ids: List[str]
    ) -> None:
        collection = self.db[collection_name]
        filter = {"id": {"$in": ids}}

        result = collection.delete_many(filter)
        logger.info(f"Deleted {result.deleted_count} documents")

    def delete_matching_record_from_id(self, collection_name: str, id: str, delete=False, should_log_id=True) -> None:
        """
        Delete a record from a collection by ID.

        :param collection_name: The name of the collection to delete the record from.
        :param id: The ID of the record to delete.
        :param delete: If True, delete the record. If False, just log the record that would be deleted.
        :param should_log_id: If True, log the ID of the record that would be deleted. If False, do not log the ID since not all records have IDs.
        """
        collection = self.db[collection_name]
        filter = {"id": id}

        if should_log_id:
            self.__log_record_deletion_information(collection_name, id)

        if delete:
            result = collection.delete_one(filter)
            logger.info(f"Deleted {result.deleted_count} record(s) from {collection_name}")

    def delete_all_records_from_collection(self, collection_name: str, delete=False, should_log_id=True) -> Any:
        """
        A terrifying function for deleting ALL records in a collection.

        :param collection_name: The name of the collection to delete all records from.
        :param delete: If True, delete the records. If False, just log the records that would be deleted.
        :param should_log_id: If True, log the IDs of the records that would be deleted. If False, do not log the IDs since not all records have IDs.
        """
        logger.info(f"Deleting all records from {collection_name}")

        to_delete = self.get_documents_from_collection(collection_name)
        collection = self.db[collection_name]

        if should_log_id:
            ids = [doc["id"] for doc in to_delete]
            self.__log_record_deletion_information_many(collection_name, ids)

        if delete:
            result = collection.delete_many({})
            logger.info(f"Deleted {result.deleted_count} record(s) from {collection_name}")

    def delete_all_metaproteomics_records(self, delete = False) -> None:
        """
        Delete all metaproteomics records.

        :param delete: If True, delete the records. If False, just log the records that would be deleted.
        """
        metap_collection_name = "metap_gene_function_aggregation"
        metaproteomics_analy_collection_name = "metaproteomics_analysis_activity_set"
        data_objects_set_name = "data_object_set"

        # Drop all from metap gene function collection.
        self.delete_all_records_from_collection(metap_collection_name, delete=delete, should_log_id=False)

        # Drop all from metaproteomics analysis activity set collection.
        self.delete_all_records_from_collection(metaproteomics_analy_collection_name, delete=delete, should_log_id=True)

        # Get all IDs associated with protemics job outputs.
        # This search is broader than tracing down the outputs of the metaproteomics analysis activity set records' data objects
        # since there appear to be dangling data objects that are not associated with any metaproteomics analysis activity records,
        # but "MSGF" is in their description and absolutely associated with the proteomics pipeline
        ids = self.get_matching_msgf_data_object_ids()
        logger.info(f'Found {len(ids)} matching records in {data_objects_set_name}')
        for id in ids:
            self.delete_matching_record_from_id(data_objects_set_name, id, delete=delete, should_log_id=True)

    def __log_record_deletion_information_many(self, collection_name: str, ids: List[str]) -> None:
        for id in ids:
            self.__log_record_deletion_information(collection_name, id)

    def __log_record_deletion_information(self, collection_name: str, id: str) -> None:
        logger.info(f"Deleting record with ID: {id} from {collection_name}")

    @staticmethod
    def get_nmdc_db(mongo_uri: str) -> "NMDCAccessor":
        db = "nmdc"

        client = pymongo.MongoClient(
            mongo_uri,
            directConnection=True,
        )

        return NMDCAccessor(client[db])


def main():
    args_map = args()

    accessor = NMDCAccessor.get_nmdc_db(mongo_uri=args_map.mongo_uri)

    if args_map.dry_run:
        logger.info("Dry run: no records will be deleted")
    else:
        logger.info("Deleting all records")

    # Being very explicit about the deletion of records
    delete = not args_map.dry_run

    accessor.delete_all_metaproteomics_records(delete=delete)


if __name__ == "__main__":
    main()
