import json
import pymongo
import argparse
from pathlib import Path
from typing import List, Any, Dict, Tuple
from collections import defaultdict, Counter
from itertools import chain


def args() -> Tuple[str]:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--output_dir",
        type=str,
        help="The output directory to save results",
        required=False,
    )
    parser.add_argument(
        "-d", help="Delete all MetaP proteomics records", action="store_true"
    )
    parser.add_argument("--username", type=str, help="MongoDB username", required=True)
    parser.add_argument("--password", type=str, help="MongoDB password", required=True)
    return parser.parse_args()


class NMDCAccessor:
    def __init__(self, db):
        self.db = db

    def get_metaproteomics_analysis_activity_set_documents(self) -> Any:
        collection = self.db["metaproteomics_analysis_activity_set"]
        documents = collection.find({})

        return list(documents)

    def get_has_outputs_map(self) -> Dict[str, List[str]]:
        documents = self.get_metaproteomics_analysis_activity_set_documents()
        has_outputs_map = defaultdict(list)

        for document in documents:
            has_outputs_map[document["id"]].extend(document["has_output"])

        return dict(has_outputs_map)

    def get_data_object_set_documents(self, ids: List[str]) -> Any:
        collection = self.db["data_object_set"]
        query = {"id": {"$in": ids}}
        documents = collection.find(query)

        return list(documents)

    def get_data_objects_from_activity_set(self) -> Any:
        ids = self.get_has_outputs_map()
        flattened_ids = list(chain(*ids.values()))

        return self.get_data_object_set_documents(flattened_ids)

    def get_matching_msgf_data_objects_records(self) -> Any:
        collection = self.db["data_object_set"]
        query = {"description": {"$regex": "MSGF"}}
        documents = collection.find(query)

        return list(documents)

    def get_matching_msgf_data_object_ids(self) -> List[str]:
        records = self.get_matching_msgf_data_objects_records()

        return [record["id"] for record in records]

    def get_metap_gene_function_aggregation_documents(self) -> Any:
        collection = self.db["metap_gene_function_aggregation"]
        documents = collection.find({})

        return list(documents)

    def get_metaproteomics_collection_ids_to_delete_map(self) -> Dict[str, List[str]]:
        metap_analy_documents = (
            self.get_metaproteomics_analysis_activity_set_documents()
        )
        data_objects_documents = self.get_matching_msgf_data_objects_records()

        metap_ids = [
            metap_analy_document["id"] for metap_analy_document in metap_analy_documents
        ]
        data_objects_ids = [
            data_object_document["id"]
            for data_object_document in data_objects_documents
        ]

        return {
            "metaproteomics_analysis_activity_set": metap_ids,
            "data_object_set": data_objects_ids,
        }

    def delete_matching_records_from_ids(
        self, collection_name: str, ids: List[str]
    ) -> None:
        collection = self.db[collection_name]
        filter = {"id": {"$in": ids}}

        result = collection.delete_many(filter)
        print(f"Deleted {result.deleted_count} documents")

    def delete_matching_record_from_id(self, collection_name: str, id: str) -> None:
        collection = self.db[collection_name]
        filter = {"id": id}

        result = collection.delete_one(filter)
        print(f"Deleted {result.deleted_count} documents")

    def delete_all_records_from_collection(self, collection_name: str) -> Any:
        """
        A terrifying function for deleting ALL documents in a collection
        """

        collection = self.db[collection_name]

        result = collection.delete_many({})

        print(f"Deleted {result.deleted_count} documents")

    def delete_all_metaproteomics_records(self) -> None:
        metap_collection_name = "metap_gene_function_aggregation"
        metaproteomics_analy_collection_name = "metaproteomics_analysis_activity_set"
        data_objects_set_name = "data_object_set"

        # Drop all all from metap gene function collection.
        self.delete_all_records_from_collection(metap_collection_name)

        # Drop all from metaproteomics analysis activity set collection.
        self.delete_all_records_from_collection(metaproteomics_analy_collection_name)

        # Get all IDs associated with protemics job outputs.
        # This search is broader than tracing down the outputs of the metaproteomics analysis activity set records' data objects
        # since there appear to be dangling data objects that are not associated with any metaproteomics analysis activity records,
        # but "MSGF" is in their description and absolutely associated with the proteomics pipeline
        ids = self.get_matching_msgf_data_object_ids()

        for id in ids:
            self.delete_matching_record_from_id(data_objects_set_name, id)

    def save_metaproteomics_analysis_activity_set(self, output_dir: Path) -> None:
        output_file = output_dir.joinpath(
            Path("metaproteomics_analysis_activity_set.json")
        )
        documents = self.get_metaproteomics_analysis_activity_set_documents()

        with open(str(output_file), "w+") as fp:
            json.dump(documents, fp, default=str, indent=2)

    def save_has_outputs_map(self, output_dir: Path) -> None:
        output_file = output_dir.joinpath(Path("has_outputs_map.json"))
        has_outputs_map = self.get_has_outputs_map()

        with open(str(output_file), "w+") as fp:
            json.dump(has_outputs_map, fp, default=str, indent=2)

    def save_data_object_set(self, output_dir: Path) -> None:
        output_file = output_dir.joinpath(Path("matching_data_objects.json"))
        data_objects = self.get_data_objects_from_activity_set()

        with open(str(output_file), "w+") as fp:
            json.dump(data_objects, fp, default=str, indent=2)

    def save_all_metaproteomics_ids(self, output_dir: Path) -> None:
        output_file = output_dir.joinpath(Path("all_ids.json"))
        id_map = self.get_has_outputs_map()
        flattened_ids = list(chain(*id_map.values()))
        flattened_ids.extend(id_map.keys())

        with open(str(output_file), "w+") as fp:
            json.dump(flattened_ids, fp, default=str, indent=2)

    def save_matching_msgf_data_objects(self, output_dir: Path) -> None:
        output_file = output_dir.joinpath(Path("all_proteomics_data_objects.json"))
        data_objects = self.get_matching_msgf_data_objects_records()

        with open(str(output_file), "w+") as fp:
            json.dump(data_objects, fp, default=str, indent=2)

    def save_metap_gene_function_aggregation(self, output_dir: Path) -> None:
        output_file = output_dir.joinpath(Path("metap_gene_function_aggregation.json"))
        documents = self.get_metap_gene_function_aggregation_documents()

        with open(str(output_file), "w+") as fp:
            json.dump(documents, fp, default=str, indent=2)

    def save_all_to_delete_by_ids_map(self, output_dir: Path) -> None:
        output_file = output_dir.joinpath(Path("ids_to_delete.json"))
        to_delete_ids_map = self.get_metaproteomics_collection_ids_to_delete_map()

        with open(str(output_file), "w+") as fp:
            json.dump(to_delete_ids_map, fp, default=str, indent=2)

    def save_metap_gene_function_aggregation_stats(self, output_dir: Path) -> None:
        output_file = output_dir.joinpath(
            Path("metap_gene_function_aggregation_stats.json")
        )
        documents_function_agg = self.get_metap_gene_function_aggregation_documents()
        documents_metaproteomics_analy = (
            self.get_metaproteomics_analysis_activity_set_documents()
        )

        ids_function_agg: List[str] = [
            document["metaproteomic_analysis_id"] for document in documents_function_agg
        ]
        id_function_agg_counter: Counter = Counter(ids_function_agg)
        ids_metaproteomics_analy: set[str] = {
            document["id"] for document in documents_metaproteomics_analy
        }
        ids_in_metaproteomics_anly_set_map: Dict[str, int] = {
            id: id in ids_metaproteomics_analy for id in id_function_agg_counter.keys()
        }

        stats_json = {
            "id_count": len(ids_function_agg),
            "unique_id_count": len(id_function_agg_counter.keys()),
            "id_frequency_map": id_function_agg_counter,
            "id_found_in_metaproteomics_analysis_activity_set_map": ids_in_metaproteomics_anly_set_map,
        }

        with open(str(output_file), "w+") as fp:
            json.dump(stats_json, fp, default=str, indent=2)

    @staticmethod
    def get_nmdc_db(username: str, password: str) -> "NMDCAccessor":
        db = "nmdc"

        client = pymongo.MongoClient(
            "localhost",
            port=37020,
            username=username,
            password=password,
            authSource="admin",
            directConnection=True,
            authMechanism="DEFAULT",
        )

        return NMDCAccessor(client[db])


def main():
    args_map = args()

    accessor = NMDCAccessor.get_nmdc_db(args_map.username, args_map.password)

    if args_map.output_dir:
        output = Path(args_map.output_dir)
        print(f"Saving to {output}")
        accessor.save_data_object_set(output)
        accessor.save_metaproteomics_analysis_activity_set(output)
        accessor.save_has_outputs_map(output)
        accessor.save_all_metaproteomics_ids(output)
        accessor.save_matching_msgf_data_objects(output)
        accessor.save_metap_gene_function_aggregation_stats(output)
        accessor.save_all_to_delete_by_ids_map(output)
    if (
        args_map.d
    ):
        print("Deleting all records")
        accessor.delete_all_metaproteomics_records()


if __name__ == "__main__":
    main()
