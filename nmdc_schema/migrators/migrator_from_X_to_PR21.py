from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import load_yaml_asset


class Migrator(MigratorBase):
    """Migrates data from schema X to PR21"""

    _from_version = "X"
    _to_version = "PR21"

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document(collection_name="study_set",
                                           pipeline=[self.move_relevant_protocols_to_protocol_link])

    def move_relevant_protocols_to_protocol_link(self, study: dict):
        r"""
        Moves any urls that exist in the relevant_protocols slot to a dictionary format (e.g. Protocol class is the range) 
        in the protocol_link slot. It then removes the relevant_protocols slot from the study.
        
        >>> m = Migrator()
        >>> m.move_relevant_protocols_to_protocol_link({'id': 123, 'relevant_protocols': ['www.ex1.org', 'www.ex2.gov']})
        {'id': 123, 'protocol_link': [{'url': 'www.ex1.org', 'type': 'nmdc:Protocol'}, {'url': 'www.ex2.gov', 'type': 'nmdc:Protocol'}]}
        >>> m.move_relevant_protocols_to_protocol_link({'id': 123, 'relevant_protocols': ['www.ex3.org']})
        {'id': 123, 'protocol_link': [{'url': 'www.ex3.org', 'type': 'nmdc:Protocol'}]}
        """

        if "relevant_protocols" in study:
            id = study["id"]
            study["protocol_link"] = []
            for protocol in study["relevant_protocols"]:
                new_protocol_struct = {
                    "url": protocol,
                    "type": "nmdc:Protocol"
                }
                study["protocol_link"].append(new_protocol_struct)
            self.logger.info(f"Moving {protocol} for study{id} from relevant_protocols slot to protocol_link")
        
            study.pop("relevant_protocols")  

        
        return study

    