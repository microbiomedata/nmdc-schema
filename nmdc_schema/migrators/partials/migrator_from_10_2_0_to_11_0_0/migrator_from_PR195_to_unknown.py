from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    Note: The `_to_version` is "unknown" because the schema to which this migrator migrates a database
          may not be one that resulted from a particular PR being merged in. We were motivated to write
          this migrator after seeing a validation error when testing some previously-written migrators.
    """

    _from_version = "PR195"
    _to_version = "unknown"

    # Initialize a mapping from `WorkflowChain.id` values to lists of gold analysis project identifiers.
    # Example: {'some_workflow_chain_id': ['some_gap_identifier', 'other_gap_identifier']}
    workflow_chain_ids_to_gap_identifiers = {}

    def upgrade(self) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        This migrator removes the `gold_analysis_project_identifiers` field from every document
        in the `workflow_execution_set` collection that is of `type` `nmdc:MetagenomeAnnotation`.
        If the field is non-empty, its value gets appended to the `gold_analysis_project_identifiers`
        field of the `workflow_chain_set` document that appears in the `nmdc:MetagenomeAnnotation`
        instance's `part_of` slot.

        Note: If this migrator had been design to be run _before_ the `migrator_from_PR195_to_PR104`
              migrator runs, it would have operated on the collection named `metagenome_annotation_set`;
              but that collection does not exist in a "post-PR104" database—its documents have been moved
              to the `workflow_execution_set` collection.
        """

        self.adapter.process_each_document(
            collection_name="workflow_execution_set",
            pipeline=[self.remove_gold_analysis_project_identifiers_field],
        )

        self.adapter.process_each_document(
            collection_name="workflow_chain_set",
            pipeline=[self.add_gold_analysis_project_identifiers_values],
        )

    def add_gold_analysis_project_identifiers_values(
        self, workflow_chain: dict
    ) -> dict:
        r"""
        Updates the `WorkflowChain` so that its `gold_analysis_project_identifiers` field contains all values that
        existed in the `gold_analysis_project_identifiers` field of any `WorkflowExecution`s that are part of that
        `WorkflowChain`.

        >>> m = Migrator()
        >>> f = m.add_gold_analysis_project_identifiers_values
        >>> m.workflow_chain_ids_to_gap_identifiers = {'x': ['a', 'b'], 'y': ['c', 'd']}
        >>> wfc = {'id': 'x', 'gold_analysis_project_identifiers': ['original']}
        >>> wfc_after = f(wfc)
        >>> wfc_after['id'] == 'x'
        True
        >>> 'gold_analysis_project_identifiers' in wfc_after
        True
        >>> 'a' in wfc_after['gold_analysis_project_identifiers']
        True
        >>> 'b' in wfc_after['gold_analysis_project_identifiers']
        True
        >>> 'original' in wfc_after['gold_analysis_project_identifiers']
        True
        """
        if workflow_chain["id"] in self.workflow_chain_ids_to_gap_identifiers.keys():
            workflow_chain_id = workflow_chain["id"]
            gap_identifiers = self.workflow_chain_ids_to_gap_identifiers[
                workflow_chain_id
            ]

            # Initialize the list if it doesn't already exist.
            if "gold_analysis_project_identifiers" not in workflow_chain:
                workflow_chain["gold_analysis_project_identifiers"] = []

            # Append the gold analysis project identifiers to the list.
            workflow_chain["gold_analysis_project_identifiers"].extend(gap_identifiers)

            # Eliminate duplicates.
            workflow_chain["gold_analysis_project_identifiers"] = list(
                set(workflow_chain["gold_analysis_project_identifiers"])
            )

        return workflow_chain

    def remove_gold_analysis_project_identifiers_field(
        self, workflow_execution: dict
    ) -> dict:
        r"""
        Removes the `gold_analysis_project_identifiers` field from the specified `WorkflowExecution`,
        if (a) that field exists and (b) the `WorkflowExecution`'s `type` is `nmdc:MetagenomeAnnotation`.

        If the field exists, this function stores its value(s) in a shared data structure, which will be used
        later to effectively store those same value(s) in the `gold_analysis_project_identifiers` field
        of the `WorkflowChain`(s) of which the original `WorkflowExecution` is a part.

        >>> m = Migrator()
        >>> f = m.remove_gold_analysis_project_identifiers_field
        >>> len(m.workflow_chain_ids_to_gap_identifiers.keys())
        0
        >>> wfe = {'type': 'nmdc:MetagenomeAnnotation',
        ...        'gold_analysis_project_identifiers': ['a', 'b'], 'part_of': ['x', 'y']}
        >>> f(wfe)
        {'type': 'nmdc:MetagenomeAnnotation', 'part_of': ['x', 'y']}
        >>> m.workflow_chain_ids_to_gap_identifiers
        {'x': ['a', 'b'], 'y': ['a', 'b']}
        """

        # Check whether this is a document we're interested in.
        if (
            workflow_execution["type"] == "nmdc:MetagenomeAnnotation"
            and "gold_analysis_project_identifiers" in workflow_execution
        ):
            # Remove the field and get its value.
            identifiers = workflow_execution.pop("gold_analysis_project_identifiers")
            assert type(identifiers) is list

            # Get each `workflow_chain_set` document whose `id` appears in the `part_of` field.
            workflow_chain_ids = workflow_execution["part_of"]
            assert type(workflow_chain_ids) is list

            # Record the `gold_analysis_project_identifiers` that we will later store
            # in a given `workflow_chain_set` document.
            for workflow_chain_id in workflow_chain_ids:
                # If this `workflow_chain_id` doesn't appear in the map yet, put it there now.
                if workflow_chain_id not in self.workflow_chain_ids_to_gap_identifiers:
                    self.workflow_chain_ids_to_gap_identifiers[workflow_chain_id] = []

                # Append these additional `gold_analysis_project_identifiers` to the list.
                self.workflow_chain_ids_to_gap_identifiers[workflow_chain_id].extend(
                    identifiers
                )

        return workflow_execution
