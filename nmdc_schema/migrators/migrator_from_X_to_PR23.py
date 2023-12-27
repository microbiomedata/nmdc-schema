from nmdc_schema.migrators.migrator_base import MigratorBase
import difflib

class Migrator_from_X_to_PR23(MigratorBase):
    """Migrates data from schema 9.1.0 to 9.2.0"""

    def __init__(self, *args, **kwargs) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__(*args, **kwargs)

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            metagenome_assembly_set=[self.execution_resource_update], metagenome_annotation_activity_set=[self.execution_resource_update],
            metatranscriptome_activity_set=[self.execution_resource_update], mags_activity_set=[self.execution_resource_update],
            metagenome_sequencing_activity_set=[self.execution_resource_update], read_qc_analysis_activity_set=[self.execution_resource_update],
            read_based_taxonomy_analysis_activity_set=[self.execution_resource_update], metabolomics_analysis_activity_set=[self.execution_resource_update],
            metaproteomics_analysis_activity_set=[self.execution_resource_update], nom_analysis_activity_set=[self.execution_resource_update]
        )

    def execution_resource_update(self, workflow_execution: dict):
        r"""
        Transforms the values of the execution_resource slot for any subclasses of WorkflowExecutionActivity into the
        allowable permissible values of the ExecutionResourceEnum.
        
        >>> m = Migrator_from_X_to_PR23()
        >>> m.execution_resource_update({'id': 123, 'execution_resource': 'LANL B-div'})
        {'id': 123, 'execution_resource': 'LANL-B-div'}
        >>> m.execution_resource_update({'id': 234, 'execution_resource': 'NERSC - Cori'})
        {'id': 234, 'execution_resource': 'NERSC-Cori'}
        """

        workflow_id = workflow_execution["id"]

        # allowable permissible values
        allowed_execution_resources = ['NERSC-Cori', 'NERSC-Perlmutter', 'EMSL', 'EMSL-RZR', 'JGI', 'LANL-B-div']
        
        if 'execution_resource' in workflow_execution:
            
            workflow_resource_value = workflow_execution['execution_resource']

            # Get closest match with the maximum closest values to return is 1, and a cutoff is 0.8
            matches = difflib.get_close_matches(workflow_resource_value, allowed_execution_resources, n=1, cutoff = 0.8)
            
            if matches:

                if difflib.SequenceMatcher(None, workflow_resource_value, matches[0]).ratio() < 1:
                    # change value of the workflow_execution resource to the proper permissible value if the match is not 100%
                    self.logger.info(f"Changing the workflow {workflow_id} execution_resource value from {workflow_resource_value} to {matches[0]}")
                    workflow_execution['execution_resource'] = matches[0]

            else:
                self.logger.error(f"The workflow {workflow_id} has an execution_resource value of {workflow_resource_value}, but did not have any matches with the cutoff set at 0.8")

        return workflow_execution

    