from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import load_yaml_asset

class Migrator_from_X_to_PR21(MigratorBase):
    """Migrates data from schema X to PR21"""

    def __init__(self, *args, **kwargs) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__(*args, **kwargs)

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            study_set=[self.move_relevant_protocols_to_protocol_link],
        )

    def move_relevant_protocols_to_protocol_link(self, study: dict):
        r"""
        Transforms `websites` values that are dois into curies and moves them into the `associated_dois slot
        Removes the doi website values from the `websites slot.
        
        >>> m = Migrator_from_X_to_PR21()
        >>> m.move_relevant_protocols_to_protocol_link({'id': 123, 'relevant_protocols': ['www.ex1.org', 'www.ex2.gov']})
        {'id': 123, 'protocol_link': [{'url': 'www.ex1.org', 'type': 'nmdc:Protocol'}, {'url': 'www.ex2.gov', 'type': 'nmdc:Protocol'}]}
        >>> m.move_relevant_protocols_to_protocol_link({'id': 123, 'relevant_protocols': ['www.ex3.org']})
        {'id': 123, 'protocol_link': [{'url': 'www.ex3.org', 'type': 'nmdc:Protocol'}]}
        """

        if "relevant_protocols" in study:
            study["protocol_link"] = []
            for protocol in study["relevant_protocols"]:
                new_protocol_struct = {
                    "url": protocol,
                    "type": "nmdc:Protocol"
                }
                study["protocol_link"].append(new_protocol_struct)
        
            study.pop("relevant_protocols")  
        
        return study

    