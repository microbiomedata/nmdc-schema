from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.10.0"
    _to_version = "11.11.0.part_1"

    def upgrade(self, commit_changes: bool = True) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""
        self.adapter.do_for_each_document("biosample_set", self.check_for_fields)

    def check_for_fields(self, biosample: dict) -> None:
        r"""
        Check each biosample record to ensure none of the removed slots are being used. 
        List of the slots that were removed:
        - dna_absorb1
        - dna_absorb2
        - dna_collect_site
        - dna_concentration
        - dna_cont_type
        - dna_cont_well
        - dna_container_id
        - dna_dnase
        - dna_isolate_meth
        - dna_organisms
        - dna_project_contact
        - dna_samp_id
        - dna_sample_format
        - dna_sample_name
        - dna_seq_project
        - dna_seq_project_pi
        - dna_seq_project_name
        - dna_volume
        - proposal_dna
        - dnase_rna
        - proposal_rna
        - rna_absorb1
        - rna_absorb2
        - rna_collect_site
        - rna_concentration
        - rna_cont_type
        - rna_cont_well
        - rna_container_id
        - rna_isolate_meth
        - rna_organisms
        - rna_project_contact
        - rna_samp_id
        - rna_sample_format
        - rna_sample_name
        - rna_seq_project
        - rna_seq_project_pi
        - rna_seq_project_name
        - rna_volume
        - collection_date_inc

        >>> m = Migrator()
        >>> m.check_for_fields({"id":123, "type": "nmdc:Biosample", "dna_absorb1": "value"})
        Traceback (most recent call last):
        ...
        Exception: Field `dna_absorb1` present in biosample 123.
        >>> m.check_for_fields({"id":123, "type": "nmdc:Biosample", "dna_absorb1": ""})
        Traceback (most recent call last):
        ...
        Exception: Field `dna_absorb1` present in biosample 123.
        >>> m.check_for_fields({"id":123, "type": "nmdc:Biosample"})
        """
        id = biosample.get("id")
        removed_slots = [
            "dna_absorb1",
            "dna_absorb2",
            "dna_collect_site",
            "dna_concentration",
            "dna_cont_type",
            "dna_cont_well",
            "dna_container_id",
            "dna_dnase",
            "dna_isolate_meth",
            "dna_organisms",
            "dna_project_contact",
            "dna_samp_id",
            "dna_sample_format",
            "dna_sample_name",
            "dna_seq_project",
            "dna_seq_project_pi",
            "dna_seq_project_name",
            "dna_volume",
            "proposal_dna",
            "dnase_rna",
            "proposal_rna",
            "rna_absorb1",
            "rna_absorb2",
            "rna_collect_site",
            "rna_concentration",
            "rna_cont_type",
            "rna_cont_well",
            "rna_container_id",
            "rna_isolate_meth",
            "rna_organisms",
            "rna_project_contact",
            "rna_samp_id",
            "rna_sample_format",
            "rna_sample_name",
            "rna_seq_project",
            "rna_seq_project_pi",
            "rna_seq_project_name",
            "rna_volume",
            "collection_date_inc",
        ]
        for slot in removed_slots:
            if slot in biosample:
                raise Exception(f"Field `{slot}` present in biosample {id}.")

