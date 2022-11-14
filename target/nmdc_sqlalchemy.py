
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class Database(Base):
    """
    An abstract holder for any set of metadata and data. It does not need to correspond to an actual managed database top level holder class. When translated to JSON-Schema this is the 'root' object. It should contain pointers to other objects of interest
    """
    __tablename__ = 'Database'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='activity_set', mapping_type=None, target_class='WorkflowExecutionActivity', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    activity_set = relationship( "WorkflowExecutionActivity", foreign_keys="[WorkflowExecutionActivity.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='biosample_set', mapping_type=None, target_class='Biosample', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    biosample_set = relationship( "Biosample", foreign_keys="[Biosample.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='data_object_set', mapping_type=None, target_class='DataObject', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    data_object_set = relationship( "DataObject", foreign_keys="[DataObject.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='dissolving_activity_set', mapping_type=None, target_class='DissolvingActivity', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    dissolving_activity_set = relationship( "DissolvingActivity", foreign_keys="[DissolvingActivity.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='functional_annotation_set', mapping_type=None, target_class='FunctionalAnnotation', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    functional_annotation_set = relationship( "FunctionalAnnotation", foreign_keys="[FunctionalAnnotation.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='genome_feature_set', mapping_type=None, target_class='GenomeFeature', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    genome_feature_set = relationship( "GenomeFeature", foreign_keys="[GenomeFeature.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='mags_activity_set', mapping_type=None, target_class='MagsAnalysisActivity', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    mags_activity_set = relationship( "MagsAnalysisActivity", foreign_keys="[MagsAnalysisActivity.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='material_sample_set', mapping_type=None, target_class='MaterialSample', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    material_sample_set = relationship( "MaterialSample", foreign_keys="[MaterialSample.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='material_sampling_activity_set', mapping_type=None, target_class='MaterialSamplingActivity', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    material_sampling_activity_set = relationship( "MaterialSamplingActivity", foreign_keys="[MaterialSamplingActivity.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='metabolomics_analysis_activity_set', mapping_type=None, target_class='MetabolomicsAnalysisActivity', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    metabolomics_analysis_activity_set = relationship( "MetabolomicsAnalysisActivity", foreign_keys="[MetabolomicsAnalysisActivity.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='metagenome_annotation_activity_set', mapping_type=None, target_class='MetagenomeAnnotationActivity', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    metagenome_annotation_activity_set = relationship( "MetagenomeAnnotationActivity", foreign_keys="[MetagenomeAnnotationActivity.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='metagenome_assembly_set', mapping_type=None, target_class='MetagenomeAssembly', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    metagenome_assembly_set = relationship( "MetagenomeAssembly", foreign_keys="[MetagenomeAssembly.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='metaproteomics_analysis_activity_set', mapping_type=None, target_class='MetaproteomicsAnalysisActivity', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    metaproteomics_analysis_activity_set = relationship( "MetaproteomicsAnalysisActivity", foreign_keys="[MetaproteomicsAnalysisActivity.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='metatranscriptome_activity_set', mapping_type=None, target_class='MetatranscriptomeActivity', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    metatranscriptome_activity_set = relationship( "MetatranscriptomeActivity", foreign_keys="[MetatranscriptomeActivity.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='nom_analysis_activity_set', mapping_type=None, target_class='NomAnalysisActivity', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    nom_analysis_activity_set = relationship( "NomAnalysisActivity", foreign_keys="[NomAnalysisActivity.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='omics_processing_set', mapping_type=None, target_class='OmicsProcessing', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    omics_processing_set = relationship( "OmicsProcessing", foreign_keys="[OmicsProcessing.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='reaction_activity_set', mapping_type=None, target_class='ReactionActivity', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    reaction_activity_set = relationship( "ReactionActivity", foreign_keys="[ReactionActivity.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='read_qc_analysis_activity_set', mapping_type=None, target_class='ReadQcAnalysisActivity', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    read_qc_analysis_activity_set = relationship( "ReadQcAnalysisActivity", foreign_keys="[ReadQcAnalysisActivity.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='read_based_taxonomy_analysis_activity_set', mapping_type=None, target_class='ReadBasedTaxonomyAnalysisActivity', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    read_based_taxonomy_analysis_activity_set = relationship( "ReadBasedTaxonomyAnalysisActivity", foreign_keys="[ReadBasedTaxonomyAnalysisActivity.Database_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Database', source_slot='study_set', mapping_type=None, target_class='Study', target_slot='Database_id', join_class=None, uses_join_table=None, multivalued=False)
    study_set = relationship( "Study", foreign_keys="[Study.Database_id]")
    
    
    def __repr__(self):
        return f"Database(id={self.id},)"
        
    
        
    


class CreditAssociation(Base):
    """
    This class supports binding associated researchers to studies. There will be at least a slot for a CRediT Contributor Role (https://casrai.org/credit/) and for a person value Specifically see the associated researchers tab on the NMDC_SampleMetadata-V4_CommentsForUpdates at https://docs.google.com/spreadsheets/d/1INlBo5eoqn2efn4H2P2i8rwRBtnbDVTqXrochJEAPko/edit#gid=0
    """
    __tablename__ = 'CreditAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    applied_role = Column(Enum('Conceptualization', 'Data curation', 'Formal Analysis', 'Funding acquisition', 'Investigation', 'Methodology', 'Project administration', 'Resources', 'Software', 'Supervision', 'Validation', 'Visualization', 'Writing original draft', 'Writing review and editing', 'Principal Investigator', 'Submitter', name='credit enum'))
    type = Column(Text())
    Study_id = Column(Text(), ForeignKey('Study.id'))
    applies_to_person_id = Column(Text(), ForeignKey('PersonValue.id'))
    applies_to_person = relationship("PersonValue", uselist=False)
    
    
    applied_roles_rel = relationship( "CreditAssociationAppliedRoles" )
    applied_roles = association_proxy("applied_roles_rel", "applied_roles",
                                  creator=lambda x_: CreditAssociationAppliedRoles(applied_roles=x_))
    
    
    def __repr__(self):
        return f"CreditAssociation(id={self.id},applied_role={self.applied_role},type={self.type},Study_id={self.Study_id},applies_to_person_id={self.applies_to_person_id},)"
        
    
        
    


class NamedThing(Base):
    """
    a databased entity or concept/class
    """
    __tablename__ = 'NamedThing'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    
    
    alternative_identifiers_rel = relationship( "NamedThingAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: NamedThingAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"NamedThing(id={self.id},name={self.name},description={self.description},)"
        
    
        
    


class AttributeValue(Base):
    """
    The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and the structured value
    """
    __tablename__ = 'AttributeValue'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    has_raw_value = Column(Text())
    was_generated_by = Column(Text(), ForeignKey('Activity.id'))
    
    
    def __repr__(self):
        return f"AttributeValue(id={self.id},has_raw_value={self.has_raw_value},was_generated_by={self.was_generated_by},)"
        
    
        
    


class MagBin(Base):
    """
    
    """
    __tablename__ = 'MagBin'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    type = Column(Text())
    bin_name = Column(Text())
    number_of_contig = Column(Integer())
    completeness = Column(Float())
    contamination = Column(Float())
    gene_count = Column(Integer())
    bin_quality = Column(Text())
    num_16s = Column(Integer())
    num_5s = Column(Integer())
    num_23s = Column(Integer())
    num_t_rna = Column(Integer())
    gtdbtk_domain = Column(Text())
    gtdbtk_phylum = Column(Text())
    gtdbtk_class = Column(Text())
    gtdbtk_order = Column(Text())
    gtdbtk_family = Column(Text())
    gtdbtk_genus = Column(Text())
    gtdbtk_species = Column(Text())
    
    
    def __repr__(self):
        return f"MagBin(id={self.id},type={self.type},bin_name={self.bin_name},number_of_contig={self.number_of_contig},completeness={self.completeness},contamination={self.contamination},gene_count={self.gene_count},bin_quality={self.bin_quality},num_16s={self.num_16s},num_5s={self.num_5s},num_23s={self.num_23s},num_t_rna={self.num_t_rna},gtdbtk_domain={self.gtdbtk_domain},gtdbtk_phylum={self.gtdbtk_phylum},gtdbtk_class={self.gtdbtk_class},gtdbtk_order={self.gtdbtk_order},gtdbtk_family={self.gtdbtk_family},gtdbtk_genus={self.gtdbtk_genus},gtdbtk_species={self.gtdbtk_species},)"
        
    
        
    


class MetaboliteQuantification(Base):
    """
    This is used to link a metabolomics analysis workflow to a specific metabolite
    """
    __tablename__ = 'MetaboliteQuantification'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    
    
    alternative_identifiers_rel = relationship( "MetaboliteQuantificationAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: MetaboliteQuantificationAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"MetaboliteQuantification(id={self.id},)"
        
    
        
    


class PeptideQuantification(Base):
    """
    This is used to link a metaproteomics analysis workflow to a specific peptide sequence and related information
    """
    __tablename__ = 'PeptideQuantification'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    
    
    def __repr__(self):
        return f"PeptideQuantification(id={self.id},)"
        
    
        
    


class ProteinQuantification(Base):
    """
    This is used to link a metaproteomics analysis workflow to a specific protein
    """
    __tablename__ = 'ProteinQuantification'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    
    
    def __repr__(self):
        return f"ProteinQuantification(id={self.id},)"
        
    
        
    


class Activity(Base):
    """
    a provence-generating activity
    """
    __tablename__ = 'Activity'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    started_at_time = Column(DateTime())
    ended_at_time = Column(DateTime())
    was_informed_by = Column(Text(), ForeignKey('Activity.id'))
    used = Column(Text())
    was_associated_with_id = Column(Text(), ForeignKey('Agent.id'))
    was_associated_with = relationship("Agent", uselist=False)
    
    
    def __repr__(self):
        return f"Activity(id={self.id},name={self.name},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},was_informed_by={self.was_informed_by},used={self.used},was_associated_with_id={self.was_associated_with_id},)"
        
    
        
    


class Agent(Base):
    """
    a provence-generating agent
    """
    __tablename__ = 'Agent'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    was_informed_by = Column(Text(), ForeignKey('Activity.id'))
    acted_on_behalf_of_id = Column(Text(), ForeignKey('Agent.id'))
    acted_on_behalf_of = relationship("Agent", uselist=False)
    
    
    def __repr__(self):
        return f"Agent(id={self.id},was_informed_by={self.was_informed_by},acted_on_behalf_of_id={self.acted_on_behalf_of_id},)"
        
    
        
    


class DissolvingActivity(Base):
    """
    
    """
    __tablename__ = 'DissolvingActivity'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    dissolution_reagent = Column(Enum('deionized_water', 'methanol', 'chloroform', name='SolventEnum'))
    material_input = Column(Text(), ForeignKey('MaterialSample.id'))
    material_output = Column(Text(), ForeignKey('MaterialSample.id'))
    Database_id = Column(Text(), ForeignKey('Database.id'))
    dissolution_aided_by_id = Column(Text(), ForeignKey('LabDevice.id'))
    dissolution_aided_by = relationship("LabDevice", uselist=False)
    dissolution_volume_id = Column(Text(), ForeignKey('QuantityValue.id'))
    dissolution_volume = relationship("QuantityValue", uselist=False)
    dissolved_in_id = Column(Text(), ForeignKey('MaterialContainer.id'))
    dissolved_in = relationship("MaterialContainer", uselist=False)
    
    
    def __repr__(self):
        return f"DissolvingActivity(id={self.id},dissolution_reagent={self.dissolution_reagent},material_input={self.material_input},material_output={self.material_output},Database_id={self.Database_id},dissolution_aided_by_id={self.dissolution_aided_by_id},dissolution_volume_id={self.dissolution_volume_id},dissolved_in_id={self.dissolved_in_id},)"
        
    
        
    


class LabDevice(Base):
    """
    
    """
    __tablename__ = 'LabDevice'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    device_type = Column(Enum('orbital_shaker', 'thermomixer', name='DeviceTypeEnum'))
    activity_speed_id = Column(Text(), ForeignKey('QuantityValue.id'))
    activity_speed = relationship("QuantityValue", uselist=False)
    activity_temperature_id = Column(Text(), ForeignKey('QuantityValue.id'))
    activity_temperature = relationship("QuantityValue", uselist=False)
    activity_time_id = Column(Text(), ForeignKey('QuantityValue.id'))
    activity_time = relationship("QuantityValue", uselist=False)
    
    
    def __repr__(self):
        return f"LabDevice(id={self.id},device_type={self.device_type},activity_speed_id={self.activity_speed_id},activity_temperature_id={self.activity_temperature_id},activity_time_id={self.activity_time_id},)"
        
    
        
    


class MaterialContainer(Base):
    """
    
    """
    __tablename__ = 'MaterialContainer'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    container_type = Column(Enum('screw_top_conical', name='ContainerTypeEnum'))
    container_size_id = Column(Text(), ForeignKey('QuantityValue.id'))
    container_size = relationship("QuantityValue", uselist=False)
    
    
    def __repr__(self):
        return f"MaterialContainer(id={self.id},container_type={self.container_type},container_size_id={self.container_size_id},)"
        
    
        
    


class MaterialSamplingActivity(Base):
    """
    
    """
    __tablename__ = 'MaterialSamplingActivity'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    biosample_input = Column(Text(), ForeignKey('Biosample.id'))
    material_output = Column(Text(), ForeignKey('MaterialSample.id'))
    sampling_method = Column(Enum('weighing', name='SamplingMethodEnum'))
    Database_id = Column(Text(), ForeignKey('Database.id'))
    amount_collected_id = Column(Text(), ForeignKey('QuantityValue.id'))
    amount_collected = relationship("QuantityValue", uselist=False)
    collected_into_id = Column(Text(), ForeignKey('MaterialContainer.id'))
    collected_into = relationship("MaterialContainer", uselist=False)
    
    
    def __repr__(self):
        return f"MaterialSamplingActivity(id={self.id},biosample_input={self.biosample_input},material_output={self.material_output},sampling_method={self.sampling_method},Database_id={self.Database_id},amount_collected_id={self.amount_collected_id},collected_into_id={self.collected_into_id},)"
        
    
        
    


class ReactionActivity(Base):
    """
    
    """
    __tablename__ = 'ReactionActivity'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    material_input = Column(Text(), ForeignKey('MaterialSample.id'))
    material_output = Column(Text(), ForeignKey('MaterialSample.id'))
    reaction_temperature = Column(Text())
    Database_id = Column(Text(), ForeignKey('Database.id'))
    reaction_aided_by_id = Column(Text(), ForeignKey('LabDevice.id'))
    reaction_aided_by = relationship("LabDevice", uselist=False)
    reaction_time_id = Column(Text(), ForeignKey('QuantityValue.id'))
    reaction_time = relationship("QuantityValue", uselist=False)
    
    
    def __repr__(self):
        return f"ReactionActivity(id={self.id},material_input={self.material_input},material_output={self.material_output},reaction_temperature={self.reaction_temperature},Database_id={self.Database_id},reaction_aided_by_id={self.reaction_aided_by_id},reaction_time_id={self.reaction_time_id},)"
        
    
        
    


class GenomeFeature(Base):
    """
    A feature localized to an interval along a genome
    """
    __tablename__ = 'GenomeFeature'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    Database_id = Column(Text(), ForeignKey('Database.id'))
    
    
    def __repr__(self):
        return f"GenomeFeature(id={self.id},Database_id={self.Database_id},)"
        
    
        
    


class ReactionParticipant(Base):
    """
    Instances of this link a reaction to a chemical entity participant
    """
    __tablename__ = 'ReactionParticipant'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    
    
    def __repr__(self):
        return f"ReactionParticipant(id={self.id},)"
        
    
        
    


class FunctionalAnnotation(Base):
    """
    An assignment of a function term (e.g. reaction or pathway) that is executed by a gene product, or which the gene product plays an active role in. Functional annotations can be assigned manually by curators, or automatically in workflows. In the context of NMDC, all function annotation is performed automatically, typically using HMM or Blast type methods
    """
    __tablename__ = 'FunctionalAnnotation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    was_generated_by = Column(Text(), ForeignKey('MetagenomeAnnotationActivity.id'))
    subject = Column(Text(), ForeignKey('GeneProduct.id'))
    has_function = Column(Text())
    Database_id = Column(Text(), ForeignKey('Database.id'))
    
    
    def __repr__(self):
        return f"FunctionalAnnotation(id={self.id},was_generated_by={self.was_generated_by},subject={self.subject},has_function={self.has_function},Database_id={self.Database_id},)"
        
    
        
    


class DataObjectAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'DataObject_alternative_identifiers'
    
    DataObject_id = Column(Text(), ForeignKey('DataObject.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"DataObject_alternative_identifiers(DataObject_id={self.DataObject_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class BiosampleBiosampleCategories(Base):
    """
    
    """
    __tablename__ = 'Biosample_biosample_categories'
    
    Biosample_id = Column(Text(), ForeignKey('Biosample.id'), primary_key=True)
    biosample_categories = Column(Enum('LTER', 'SIP', 'SFA', 'FICUS', 'NEON', name='biosample_category_enum'), primary_key=True)
    
    
    def __repr__(self):
        return f"Biosample_biosample_categories(Biosample_id={self.Biosample_id},biosample_categories={self.biosample_categories},)"
        
    
        
    


class BiosamplePartOf(Base):
    """
    
    """
    __tablename__ = 'Biosample_part_of'
    
    Biosample_id = Column(Text(), ForeignKey('Biosample.id'), primary_key=True)
    part_of = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"Biosample_part_of(Biosample_id={self.Biosample_id},part_of={self.part_of},)"
        
    
        
    


class BiosampleAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'Biosample_alternative_identifiers'
    
    Biosample_id = Column(Text(), ForeignKey('Biosample.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Biosample_alternative_identifiers(Biosample_id={self.Biosample_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class BiosampleGoldSampleIdentifiers(Base):
    """
    
    """
    __tablename__ = 'Biosample_gold_sample_identifiers'
    
    Biosample_id = Column(Text(), ForeignKey('Biosample.id'), primary_key=True)
    gold_sample_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Biosample_gold_sample_identifiers(Biosample_id={self.Biosample_id},gold_sample_identifiers={self.gold_sample_identifiers},)"
        
    
        
    


class BiosampleAnalysisType(Base):
    """
    
    """
    __tablename__ = 'Biosample_analysis_type'
    
    Biosample_id = Column(Text(), ForeignKey('Biosample.id'), primary_key=True)
    analysis_type = Column(Enum('metabolomics', 'metagenomics', 'metaproteomics', 'metatranscriptomics', 'natural organic matter', name='analysis_type_enum'), primary_key=True)
    
    
    def __repr__(self):
        return f"Biosample_analysis_type(Biosample_id={self.Biosample_id},analysis_type={self.analysis_type},)"
        
    
        
    


class BiosampleSampleLink(Base):
    """
    
    """
    __tablename__ = 'Biosample_sample_link'
    
    Biosample_id = Column(Text(), ForeignKey('Biosample.id'), primary_key=True)
    sample_link = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Biosample_sample_link(Biosample_id={self.Biosample_id},sample_link={self.sample_link},)"
        
    
        
    


class StudyAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'Study_alternative_identifiers'
    
    Study_id = Column(Text(), ForeignKey('Study.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Study_alternative_identifiers(Study_id={self.Study_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class StudyGoldStudyIdentifiers(Base):
    """
    
    """
    __tablename__ = 'Study_gold_study_identifiers'
    
    Study_id = Column(Text(), ForeignKey('Study.id'), primary_key=True)
    gold_study_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Study_gold_study_identifiers(Study_id={self.Study_id},gold_study_identifiers={self.gold_study_identifiers},)"
        
    
        
    


class StudyAlternativeTitles(Base):
    """
    
    """
    __tablename__ = 'Study_alternative_titles'
    
    Study_id = Column(Text(), ForeignKey('Study.id'), primary_key=True)
    alternative_titles = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Study_alternative_titles(Study_id={self.Study_id},alternative_titles={self.alternative_titles},)"
        
    
        
    


class StudyAlternativeDescriptions(Base):
    """
    
    """
    __tablename__ = 'Study_alternative_descriptions'
    
    Study_id = Column(Text(), ForeignKey('Study.id'), primary_key=True)
    alternative_descriptions = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Study_alternative_descriptions(Study_id={self.Study_id},alternative_descriptions={self.alternative_descriptions},)"
        
    
        
    


class StudyAlternativeNames(Base):
    """
    
    """
    __tablename__ = 'Study_alternative_names'
    
    Study_id = Column(Text(), ForeignKey('Study.id'), primary_key=True)
    alternative_names = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Study_alternative_names(Study_id={self.Study_id},alternative_names={self.alternative_names},)"
        
    
        
    


class StudyWebsites(Base):
    """
    
    """
    __tablename__ = 'Study_websites'
    
    Study_id = Column(Text(), ForeignKey('Study.id'), primary_key=True)
    websites = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Study_websites(Study_id={self.Study_id},websites={self.websites},)"
        
    
        
    


class StudyPublications(Base):
    """
    
    """
    __tablename__ = 'Study_publications'
    
    Study_id = Column(Text(), ForeignKey('Study.id'), primary_key=True)
    publications = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Study_publications(Study_id={self.Study_id},publications={self.publications},)"
        
    
        
    


class StudyEssDiveDatasets(Base):
    """
    
    """
    __tablename__ = 'Study_ess_dive_datasets'
    
    Study_id = Column(Text(), ForeignKey('Study.id'), primary_key=True)
    ess_dive_datasets = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Study_ess_dive_datasets(Study_id={self.Study_id},ess_dive_datasets={self.ess_dive_datasets},)"
        
    
        
    


class StudyRelevantProtocols(Base):
    """
    
    """
    __tablename__ = 'Study_relevant_protocols'
    
    Study_id = Column(Text(), ForeignKey('Study.id'), primary_key=True)
    relevant_protocols = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Study_relevant_protocols(Study_id={self.Study_id},relevant_protocols={self.relevant_protocols},)"
        
    
        
    


class StudyFundingSources(Base):
    """
    
    """
    __tablename__ = 'Study_funding_sources'
    
    Study_id = Column(Text(), ForeignKey('Study.id'), primary_key=True)
    funding_sources = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Study_funding_sources(Study_id={self.Study_id},funding_sources={self.funding_sources},)"
        
    
        
    


class BiosampleProcessingHasInput(Base):
    """
    
    """
    __tablename__ = 'BiosampleProcessing_has_input'
    
    BiosampleProcessing_id = Column(Text(), ForeignKey('BiosampleProcessing.id'), primary_key=True)
    has_input = Column(Text(), ForeignKey('Biosample.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"BiosampleProcessing_has_input(BiosampleProcessing_id={self.BiosampleProcessing_id},has_input={self.has_input},)"
        
    
        
    


class BiosampleProcessingAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'BiosampleProcessing_alternative_identifiers'
    
    BiosampleProcessing_id = Column(Text(), ForeignKey('BiosampleProcessing.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"BiosampleProcessing_alternative_identifiers(BiosampleProcessing_id={self.BiosampleProcessing_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class OmicsProcessingHasInput(Base):
    """
    
    """
    __tablename__ = 'OmicsProcessing_has_input'
    
    OmicsProcessing_id = Column(Text(), ForeignKey('OmicsProcessing.id'), primary_key=True)
    has_input = Column(Text(), ForeignKey('Biosample.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"OmicsProcessing_has_input(OmicsProcessing_id={self.OmicsProcessing_id},has_input={self.has_input},)"
        
    
        
    


class OmicsProcessingHasOutput(Base):
    """
    
    """
    __tablename__ = 'OmicsProcessing_has_output'
    
    OmicsProcessing_id = Column(Text(), ForeignKey('OmicsProcessing.id'), primary_key=True)
    has_output = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"OmicsProcessing_has_output(OmicsProcessing_id={self.OmicsProcessing_id},has_output={self.has_output},)"
        
    
        
    


class OmicsProcessingPartOf(Base):
    """
    
    """
    __tablename__ = 'OmicsProcessing_part_of'
    
    OmicsProcessing_id = Column(Text(), ForeignKey('OmicsProcessing.id'), primary_key=True)
    part_of = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"OmicsProcessing_part_of(OmicsProcessing_id={self.OmicsProcessing_id},part_of={self.part_of},)"
        
    
        
    


class OmicsProcessingGoldSequencingProjectIdentifiers(Base):
    """
    
    """
    __tablename__ = 'OmicsProcessing_gold_sequencing_project_identifiers'
    
    OmicsProcessing_id = Column(Text(), ForeignKey('OmicsProcessing.id'), primary_key=True)
    gold_sequencing_project_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"OmicsProcessing_gold_sequencing_project_identifiers(OmicsProcessing_id={self.OmicsProcessing_id},gold_sequencing_project_identifiers={self.gold_sequencing_project_identifiers},)"
        
    
        
    


class OmicsProcessingInsdcExperimentIdentifiers(Base):
    """
    
    """
    __tablename__ = 'OmicsProcessing_insdc_experiment_identifiers'
    
    OmicsProcessing_id = Column(Text(), ForeignKey('OmicsProcessing.id'), primary_key=True)
    insdc_experiment_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"OmicsProcessing_insdc_experiment_identifiers(OmicsProcessing_id={self.OmicsProcessing_id},insdc_experiment_identifiers={self.insdc_experiment_identifiers},)"
        
    
        
    


class OmicsProcessingAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'OmicsProcessing_alternative_identifiers'
    
    OmicsProcessing_id = Column(Text(), ForeignKey('OmicsProcessing.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"OmicsProcessing_alternative_identifiers(OmicsProcessing_id={self.OmicsProcessing_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class CreditAssociationAppliedRoles(Base):
    """
    
    """
    __tablename__ = 'CreditAssociation_applied_roles'
    
    CreditAssociation_id = Column(Text(), ForeignKey('CreditAssociation.id'), primary_key=True)
    applied_roles = Column(Enum('Conceptualization', 'Data curation', 'Formal Analysis', 'Funding acquisition', 'Investigation', 'Methodology', 'Project administration', 'Resources', 'Software', 'Supervision', 'Validation', 'Visualization', 'Writing original draft', 'Writing review and editing', 'Principal Investigator', 'Submitter', name='credit enum'), primary_key=True)
    
    
    def __repr__(self):
        return f"CreditAssociation_applied_roles(CreditAssociation_id={self.CreditAssociation_id},applied_roles={self.applied_roles},)"
        
    
        
    


class WorkflowExecutionActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'WorkflowExecutionActivity_has_input'
    
    WorkflowExecutionActivity_id = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'), primary_key=True)
    has_input = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"WorkflowExecutionActivity_has_input(WorkflowExecutionActivity_id={self.WorkflowExecutionActivity_id},has_input={self.has_input},)"
        
    
        
    


class WorkflowExecutionActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'WorkflowExecutionActivity_has_output'
    
    WorkflowExecutionActivity_id = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'), primary_key=True)
    has_output = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"WorkflowExecutionActivity_has_output(WorkflowExecutionActivity_id={self.WorkflowExecutionActivity_id},has_output={self.has_output},)"
        
    
        
    


class WorkflowExecutionActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'WorkflowExecutionActivity_part_of'
    
    WorkflowExecutionActivity_id = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'), primary_key=True)
    part_of = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"WorkflowExecutionActivity_part_of(WorkflowExecutionActivity_id={self.WorkflowExecutionActivity_id},part_of={self.part_of},)"
        
    
        
    


class MetagenomeAssemblyHasInput(Base):
    """
    
    """
    __tablename__ = 'MetagenomeAssembly_has_input'
    
    MetagenomeAssembly_id = Column(Text(), ForeignKey('MetagenomeAssembly.id'), primary_key=True)
    has_input = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetagenomeAssembly_has_input(MetagenomeAssembly_id={self.MetagenomeAssembly_id},has_input={self.has_input},)"
        
    
        
    


class MetagenomeAssemblyHasOutput(Base):
    """
    
    """
    __tablename__ = 'MetagenomeAssembly_has_output'
    
    MetagenomeAssembly_id = Column(Text(), ForeignKey('MetagenomeAssembly.id'), primary_key=True)
    has_output = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetagenomeAssembly_has_output(MetagenomeAssembly_id={self.MetagenomeAssembly_id},has_output={self.has_output},)"
        
    
        
    


class MetagenomeAssemblyPartOf(Base):
    """
    
    """
    __tablename__ = 'MetagenomeAssembly_part_of'
    
    MetagenomeAssembly_id = Column(Text(), ForeignKey('MetagenomeAssembly.id'), primary_key=True)
    part_of = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetagenomeAssembly_part_of(MetagenomeAssembly_id={self.MetagenomeAssembly_id},part_of={self.part_of},)"
        
    
        
    


class MetatranscriptomeAssemblyHasInput(Base):
    """
    
    """
    __tablename__ = 'MetatranscriptomeAssembly_has_input'
    
    MetatranscriptomeAssembly_id = Column(Text(), ForeignKey('MetatranscriptomeAssembly.id'), primary_key=True)
    has_input = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetatranscriptomeAssembly_has_input(MetatranscriptomeAssembly_id={self.MetatranscriptomeAssembly_id},has_input={self.has_input},)"
        
    
        
    


class MetatranscriptomeAssemblyHasOutput(Base):
    """
    
    """
    __tablename__ = 'MetatranscriptomeAssembly_has_output'
    
    MetatranscriptomeAssembly_id = Column(Text(), ForeignKey('MetatranscriptomeAssembly.id'), primary_key=True)
    has_output = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetatranscriptomeAssembly_has_output(MetatranscriptomeAssembly_id={self.MetatranscriptomeAssembly_id},has_output={self.has_output},)"
        
    
        
    


class MetatranscriptomeAssemblyPartOf(Base):
    """
    
    """
    __tablename__ = 'MetatranscriptomeAssembly_part_of'
    
    MetatranscriptomeAssembly_id = Column(Text(), ForeignKey('MetatranscriptomeAssembly.id'), primary_key=True)
    part_of = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetatranscriptomeAssembly_part_of(MetatranscriptomeAssembly_id={self.MetatranscriptomeAssembly_id},part_of={self.part_of},)"
        
    
        
    


class MetagenomeAnnotationActivityGoldAnalysisProjectIdentifiers(Base):
    """
    
    """
    __tablename__ = 'MetagenomeAnnotationActivity_gold_analysis_project_identifiers'
    
    MetagenomeAnnotationActivity_id = Column(Text(), ForeignKey('MetagenomeAnnotationActivity.id'), primary_key=True)
    gold_analysis_project_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"MetagenomeAnnotationActivity_gold_analysis_project_identifiers(MetagenomeAnnotationActivity_id={self.MetagenomeAnnotationActivity_id},gold_analysis_project_identifiers={self.gold_analysis_project_identifiers},)"
        
    
        
    


class MetagenomeAnnotationActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'MetagenomeAnnotationActivity_has_input'
    
    MetagenomeAnnotationActivity_id = Column(Text(), ForeignKey('MetagenomeAnnotationActivity.id'), primary_key=True)
    has_input = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetagenomeAnnotationActivity_has_input(MetagenomeAnnotationActivity_id={self.MetagenomeAnnotationActivity_id},has_input={self.has_input},)"
        
    
        
    


class MetagenomeAnnotationActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'MetagenomeAnnotationActivity_has_output'
    
    MetagenomeAnnotationActivity_id = Column(Text(), ForeignKey('MetagenomeAnnotationActivity.id'), primary_key=True)
    has_output = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetagenomeAnnotationActivity_has_output(MetagenomeAnnotationActivity_id={self.MetagenomeAnnotationActivity_id},has_output={self.has_output},)"
        
    
        
    


class MetagenomeAnnotationActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'MetagenomeAnnotationActivity_part_of'
    
    MetagenomeAnnotationActivity_id = Column(Text(), ForeignKey('MetagenomeAnnotationActivity.id'), primary_key=True)
    part_of = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetagenomeAnnotationActivity_part_of(MetagenomeAnnotationActivity_id={self.MetagenomeAnnotationActivity_id},part_of={self.part_of},)"
        
    
        
    


class MetatranscriptomeAnnotationActivityGoldAnalysisProjectIdentifiers(Base):
    """
    
    """
    __tablename__ = 'MetatranscriptomeAnnotationActivity_gold_analysis_project_identifiers'
    
    MetatranscriptomeAnnotationActivity_id = Column(Text(), ForeignKey('MetatranscriptomeAnnotationActivity.id'), primary_key=True)
    gold_analysis_project_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"MetatranscriptomeAnnotationActivity_gold_analysis_project_identifiers(MetatranscriptomeAnnotationActivity_id={self.MetatranscriptomeAnnotationActivity_id},gold_analysis_project_identifiers={self.gold_analysis_project_identifiers},)"
        
    
        
    


class MetatranscriptomeAnnotationActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'MetatranscriptomeAnnotationActivity_has_input'
    
    MetatranscriptomeAnnotationActivity_id = Column(Text(), ForeignKey('MetatranscriptomeAnnotationActivity.id'), primary_key=True)
    has_input = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetatranscriptomeAnnotationActivity_has_input(MetatranscriptomeAnnotationActivity_id={self.MetatranscriptomeAnnotationActivity_id},has_input={self.has_input},)"
        
    
        
    


class MetatranscriptomeAnnotationActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'MetatranscriptomeAnnotationActivity_has_output'
    
    MetatranscriptomeAnnotationActivity_id = Column(Text(), ForeignKey('MetatranscriptomeAnnotationActivity.id'), primary_key=True)
    has_output = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetatranscriptomeAnnotationActivity_has_output(MetatranscriptomeAnnotationActivity_id={self.MetatranscriptomeAnnotationActivity_id},has_output={self.has_output},)"
        
    
        
    


class MetatranscriptomeAnnotationActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'MetatranscriptomeAnnotationActivity_part_of'
    
    MetatranscriptomeAnnotationActivity_id = Column(Text(), ForeignKey('MetatranscriptomeAnnotationActivity.id'), primary_key=True)
    part_of = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetatranscriptomeAnnotationActivity_part_of(MetatranscriptomeAnnotationActivity_id={self.MetatranscriptomeAnnotationActivity_id},part_of={self.part_of},)"
        
    
        
    


class MetatranscriptomeActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'MetatranscriptomeActivity_has_input'
    
    MetatranscriptomeActivity_id = Column(Text(), ForeignKey('MetatranscriptomeActivity.id'), primary_key=True)
    has_input = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetatranscriptomeActivity_has_input(MetatranscriptomeActivity_id={self.MetatranscriptomeActivity_id},has_input={self.has_input},)"
        
    
        
    


class MetatranscriptomeActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'MetatranscriptomeActivity_has_output'
    
    MetatranscriptomeActivity_id = Column(Text(), ForeignKey('MetatranscriptomeActivity.id'), primary_key=True)
    has_output = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetatranscriptomeActivity_has_output(MetatranscriptomeActivity_id={self.MetatranscriptomeActivity_id},has_output={self.has_output},)"
        
    
        
    


class MetatranscriptomeActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'MetatranscriptomeActivity_part_of'
    
    MetatranscriptomeActivity_id = Column(Text(), ForeignKey('MetatranscriptomeActivity.id'), primary_key=True)
    part_of = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetatranscriptomeActivity_part_of(MetatranscriptomeActivity_id={self.MetatranscriptomeActivity_id},part_of={self.part_of},)"
        
    
        
    


class MagsAnalysisActivityMagsList(Base):
    """
    
    """
    __tablename__ = 'MagsAnalysisActivity_mags_list'
    
    MagsAnalysisActivity_id = Column(Text(), ForeignKey('MagsAnalysisActivity.id'), primary_key=True)
    mags_list_id = Column(Text(), ForeignKey('MagBin.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MagsAnalysisActivity_mags_list(MagsAnalysisActivity_id={self.MagsAnalysisActivity_id},mags_list_id={self.mags_list_id},)"
        
    
        
    


class MagsAnalysisActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'MagsAnalysisActivity_has_input'
    
    MagsAnalysisActivity_id = Column(Text(), ForeignKey('MagsAnalysisActivity.id'), primary_key=True)
    has_input = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MagsAnalysisActivity_has_input(MagsAnalysisActivity_id={self.MagsAnalysisActivity_id},has_input={self.has_input},)"
        
    
        
    


class MagsAnalysisActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'MagsAnalysisActivity_has_output'
    
    MagsAnalysisActivity_id = Column(Text(), ForeignKey('MagsAnalysisActivity.id'), primary_key=True)
    has_output = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MagsAnalysisActivity_has_output(MagsAnalysisActivity_id={self.MagsAnalysisActivity_id},has_output={self.has_output},)"
        
    
        
    


class MagsAnalysisActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'MagsAnalysisActivity_part_of'
    
    MagsAnalysisActivity_id = Column(Text(), ForeignKey('MagsAnalysisActivity.id'), primary_key=True)
    part_of = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MagsAnalysisActivity_part_of(MagsAnalysisActivity_id={self.MagsAnalysisActivity_id},part_of={self.part_of},)"
        
    
        
    


class ReadQcAnalysisActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'ReadQcAnalysisActivity_has_input'
    
    ReadQcAnalysisActivity_id = Column(Text(), ForeignKey('ReadQcAnalysisActivity.id'), primary_key=True)
    has_input = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"ReadQcAnalysisActivity_has_input(ReadQcAnalysisActivity_id={self.ReadQcAnalysisActivity_id},has_input={self.has_input},)"
        
    
        
    


class ReadQcAnalysisActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'ReadQcAnalysisActivity_has_output'
    
    ReadQcAnalysisActivity_id = Column(Text(), ForeignKey('ReadQcAnalysisActivity.id'), primary_key=True)
    has_output = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"ReadQcAnalysisActivity_has_output(ReadQcAnalysisActivity_id={self.ReadQcAnalysisActivity_id},has_output={self.has_output},)"
        
    
        
    


class ReadQcAnalysisActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'ReadQcAnalysisActivity_part_of'
    
    ReadQcAnalysisActivity_id = Column(Text(), ForeignKey('ReadQcAnalysisActivity.id'), primary_key=True)
    part_of = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"ReadQcAnalysisActivity_part_of(ReadQcAnalysisActivity_id={self.ReadQcAnalysisActivity_id},part_of={self.part_of},)"
        
    
        
    


class ReadBasedTaxonomyAnalysisActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'ReadBasedTaxonomyAnalysisActivity_has_input'
    
    ReadBasedTaxonomyAnalysisActivity_id = Column(Text(), ForeignKey('ReadBasedTaxonomyAnalysisActivity.id'), primary_key=True)
    has_input = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"ReadBasedTaxonomyAnalysisActivity_has_input(ReadBasedTaxonomyAnalysisActivity_id={self.ReadBasedTaxonomyAnalysisActivity_id},has_input={self.has_input},)"
        
    
        
    


class ReadBasedTaxonomyAnalysisActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'ReadBasedTaxonomyAnalysisActivity_has_output'
    
    ReadBasedTaxonomyAnalysisActivity_id = Column(Text(), ForeignKey('ReadBasedTaxonomyAnalysisActivity.id'), primary_key=True)
    has_output = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"ReadBasedTaxonomyAnalysisActivity_has_output(ReadBasedTaxonomyAnalysisActivity_id={self.ReadBasedTaxonomyAnalysisActivity_id},has_output={self.has_output},)"
        
    
        
    


class ReadBasedTaxonomyAnalysisActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'ReadBasedTaxonomyAnalysisActivity_part_of'
    
    ReadBasedTaxonomyAnalysisActivity_id = Column(Text(), ForeignKey('ReadBasedTaxonomyAnalysisActivity.id'), primary_key=True)
    part_of = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"ReadBasedTaxonomyAnalysisActivity_part_of(ReadBasedTaxonomyAnalysisActivity_id={self.ReadBasedTaxonomyAnalysisActivity_id},part_of={self.part_of},)"
        
    
        
    


class MetabolomicsAnalysisActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'MetabolomicsAnalysisActivity_has_input'
    
    MetabolomicsAnalysisActivity_id = Column(Text(), ForeignKey('MetabolomicsAnalysisActivity.id'), primary_key=True)
    has_input = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetabolomicsAnalysisActivity_has_input(MetabolomicsAnalysisActivity_id={self.MetabolomicsAnalysisActivity_id},has_input={self.has_input},)"
        
    
        
    


class MetabolomicsAnalysisActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'MetabolomicsAnalysisActivity_has_output'
    
    MetabolomicsAnalysisActivity_id = Column(Text(), ForeignKey('MetabolomicsAnalysisActivity.id'), primary_key=True)
    has_output = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetabolomicsAnalysisActivity_has_output(MetabolomicsAnalysisActivity_id={self.MetabolomicsAnalysisActivity_id},has_output={self.has_output},)"
        
    
        
    


class MetabolomicsAnalysisActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'MetabolomicsAnalysisActivity_part_of'
    
    MetabolomicsAnalysisActivity_id = Column(Text(), ForeignKey('MetabolomicsAnalysisActivity.id'), primary_key=True)
    part_of = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetabolomicsAnalysisActivity_part_of(MetabolomicsAnalysisActivity_id={self.MetabolomicsAnalysisActivity_id},part_of={self.part_of},)"
        
    
        
    


class MetaproteomicsAnalysisActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'MetaproteomicsAnalysisActivity_has_input'
    
    MetaproteomicsAnalysisActivity_id = Column(Text(), ForeignKey('MetaproteomicsAnalysisActivity.id'), primary_key=True)
    has_input = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetaproteomicsAnalysisActivity_has_input(MetaproteomicsAnalysisActivity_id={self.MetaproteomicsAnalysisActivity_id},has_input={self.has_input},)"
        
    
        
    


class MetaproteomicsAnalysisActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'MetaproteomicsAnalysisActivity_has_output'
    
    MetaproteomicsAnalysisActivity_id = Column(Text(), ForeignKey('MetaproteomicsAnalysisActivity.id'), primary_key=True)
    has_output = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetaproteomicsAnalysisActivity_has_output(MetaproteomicsAnalysisActivity_id={self.MetaproteomicsAnalysisActivity_id},has_output={self.has_output},)"
        
    
        
    


class MetaproteomicsAnalysisActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'MetaproteomicsAnalysisActivity_part_of'
    
    MetaproteomicsAnalysisActivity_id = Column(Text(), ForeignKey('MetaproteomicsAnalysisActivity.id'), primary_key=True)
    part_of = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MetaproteomicsAnalysisActivity_part_of(MetaproteomicsAnalysisActivity_id={self.MetaproteomicsAnalysisActivity_id},part_of={self.part_of},)"
        
    
        
    


class NomAnalysisActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'NomAnalysisActivity_has_input'
    
    NomAnalysisActivity_id = Column(Text(), ForeignKey('NomAnalysisActivity.id'), primary_key=True)
    has_input = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"NomAnalysisActivity_has_input(NomAnalysisActivity_id={self.NomAnalysisActivity_id},has_input={self.has_input},)"
        
    
        
    


class NomAnalysisActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'NomAnalysisActivity_has_output'
    
    NomAnalysisActivity_id = Column(Text(), ForeignKey('NomAnalysisActivity.id'), primary_key=True)
    has_output = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"NomAnalysisActivity_has_output(NomAnalysisActivity_id={self.NomAnalysisActivity_id},has_output={self.has_output},)"
        
    
        
    


class NomAnalysisActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'NomAnalysisActivity_part_of'
    
    NomAnalysisActivity_id = Column(Text(), ForeignKey('NomAnalysisActivity.id'), primary_key=True)
    part_of = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"NomAnalysisActivity_part_of(NomAnalysisActivity_id={self.NomAnalysisActivity_id},part_of={self.part_of},)"
        
    
        
    


class NamedThingAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'NamedThing_alternative_identifiers'
    
    NamedThing_id = Column(Text(), ForeignKey('NamedThing.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"NamedThing_alternative_identifiers(NamedThing_id={self.NamedThing_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class OntologyClassAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'OntologyClass_alternative_identifiers'
    
    OntologyClass_id = Column(Text(), ForeignKey('OntologyClass.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"OntologyClass_alternative_identifiers(OntologyClass_id={self.OntologyClass_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class EnvironmentalMaterialTermAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'EnvironmentalMaterialTerm_alternative_identifiers'
    
    EnvironmentalMaterialTerm_id = Column(Text(), ForeignKey('EnvironmentalMaterialTerm.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"EnvironmentalMaterialTerm_alternative_identifiers(EnvironmentalMaterialTerm_id={self.EnvironmentalMaterialTerm_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class PersonValueWebsites(Base):
    """
    
    """
    __tablename__ = 'PersonValue_websites'
    
    PersonValue_id = Column(Text(), ForeignKey('PersonValue.id'), primary_key=True)
    websites = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"PersonValue_websites(PersonValue_id={self.PersonValue_id},websites={self.websites},)"
        
    
        
    


class PersonAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'Person_alternative_identifiers'
    
    Person_id = Column(Text(), ForeignKey('Person.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Person_alternative_identifiers(Person_id={self.Person_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class InstrumentAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'Instrument_alternative_identifiers'
    
    Instrument_id = Column(Text(), ForeignKey('Instrument.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Instrument_alternative_identifiers(Instrument_id={self.Instrument_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class MetaboliteQuantificationAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'MetaboliteQuantification_alternative_identifiers'
    
    MetaboliteQuantification_id = Column(Text(), ForeignKey('MetaboliteQuantification.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"MetaboliteQuantification_alternative_identifiers(MetaboliteQuantification_id={self.MetaboliteQuantification_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class ChemicalEntityAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'ChemicalEntity_alternative_identifiers'
    
    ChemicalEntity_id = Column(Text(), ForeignKey('ChemicalEntity.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"ChemicalEntity_alternative_identifiers(ChemicalEntity_id={self.ChemicalEntity_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class GeneProductAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'GeneProduct_alternative_identifiers'
    
    GeneProduct_id = Column(Text(), ForeignKey('GeneProduct.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"GeneProduct_alternative_identifiers(GeneProduct_id={self.GeneProduct_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class MaterialSampleAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'MaterialSample_alternative_identifiers'
    
    MaterialSample_id = Column(Text(), ForeignKey('MaterialSample.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"MaterialSample_alternative_identifiers(MaterialSample_id={self.MaterialSample_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class FunctionalAnnotationTermAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'FunctionalAnnotationTerm_alternative_identifiers'
    
    FunctionalAnnotationTerm_id = Column(Text(), ForeignKey('FunctionalAnnotationTerm.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"FunctionalAnnotationTerm_alternative_identifiers(FunctionalAnnotationTerm_id={self.FunctionalAnnotationTerm_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class PathwayAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'Pathway_alternative_identifiers'
    
    Pathway_id = Column(Text(), ForeignKey('Pathway.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Pathway_alternative_identifiers(Pathway_id={self.Pathway_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class ReactionAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'Reaction_alternative_identifiers'
    
    Reaction_id = Column(Text(), ForeignKey('Reaction.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Reaction_alternative_identifiers(Reaction_id={self.Reaction_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class OrthologyGroupAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'OrthologyGroup_alternative_identifiers'
    
    OrthologyGroup_id = Column(Text(), ForeignKey('OrthologyGroup.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"OrthologyGroup_alternative_identifiers(OrthologyGroup_id={self.OrthologyGroup_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class DataObject(NamedThing):
    """
    An object that primarily consists of symbols that represent information.   Files, records, and omics data are examples of data objects. 
    """
    __tablename__ = 'DataObject'
    
    file_size_bytes = Column(Integer())
    md5_checksum = Column(Text())
    data_object_type = Column(Enum('Metagenome Raw Reads', 'FT ICR-MS Analysis Results', 'GC-MS Metabolomics Results', 'Metaproteomics Workflow Statistics', 'Protein Report', 'Peptide Report', 'Unfiltered Metaproteomics Results', 'Read Count and RPKM', 'QC non-rRNA R2', 'QC non-rRNA R1', 'Metagenome Bins', 'CheckM Statistics', 'GOTTCHA2 Krona Plot', 'GOTTCHA2 Classification Report', 'GOTTCHA2 Report Full', 'Kraken2 Krona Plot', 'Centrifuge Krona Plot', 'Centrifuge output report file', 'Kraken2 Classification Report', 'Kraken2 Taxonomic Classification', 'Centrifuge Classification Report', 'Centrifuge Taxonomic Classification', 'Structural Annotation GFF', 'Functional Annotation GFF', 'Annotation Amino Acid FASTA', 'Annotation Enzyme Commission', 'Annotation KEGG Orthology', 'Assembly Coverage BAM', 'Assembly AGP', 'Assembly Scaffolds', 'Assembly Contigs', 'Assembly Coverage Stats', 'Filtered Sequencing Reads', 'QC Statistics', 'TIGRFam Annotation GFF', 'CRT Annotation GFF', 'Genmark Annotation GFF', 'Prodigal Annotation GFF', 'TRNA Annotation GFF', 'Misc Annotation GFF', 'RFAM Annotation GFF', 'TMRNA Annotation GFF', 'KO_EC Annotation GFF', 'Product Names', 'Gene Phylogeny tsv', 'Crisprt Terms', 'Clusters of Orthologous Groups (COG) Annotation GFF', 'CATH FunFams (Functional Families) Annotation GFF', 'SUPERFam Annotation GFF', 'SMART Annotation GFF', 'Pfam Annotation GFF', 'Direct Infusion FT ICR-MS Raw Data', name='file type enum'))
    compression_type = Column(Text())
    was_generated_by = Column(Text(), ForeignKey('Activity.id'))
    url = Column(Text())
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    Database_id = Column(Text(), ForeignKey('Database.id'))
    
    
    alternative_identifiers_rel = relationship( "DataObjectAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: DataObjectAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"DataObject(file_size_bytes={self.file_size_bytes},md5_checksum={self.md5_checksum},data_object_type={self.data_object_type},compression_type={self.compression_type},was_generated_by={self.was_generated_by},url={self.url},type={self.type},id={self.id},name={self.name},description={self.description},Database_id={self.Database_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Biosample(NamedThing):
    """
    Biological source material which can be characterized by an experiment.
    """
    __tablename__ = 'Biosample'
    
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    tot_nitro_cont_meth = Column(Text())
    water_cont_soil_meth = Column(Text())
    ecosystem = Column(Text())
    ecosystem_category = Column(Text())
    ecosystem_type = Column(Text())
    ecosystem_subtype = Column(Text())
    specific_ecosystem = Column(Text())
    add_date = Column(Text())
    community = Column(Text())
    habitat = Column(Text())
    host_name = Column(Text())
    identifier = Column(Text())
    location = Column(Text())
    mod_date = Column(Text())
    ncbi_taxonomy_name = Column(Text())
    proport_woa_temperature = Column(Text())
    salinity_category = Column(Text())
    sample_collection_site = Column(Text())
    soluble_iron_micromol = Column(Text())
    micro_biomass_meth = Column(Text())
    samp_collec_method = Column(Text())
    soil_texture_meth = Column(Text())
    dna_absorb1 = Column(Text())
    dna_absorb2 = Column(Text())
    dna_collect_site = Column(Text())
    dna_concentration = Column(Text())
    dna_cont_type = Column(Enum('plate', 'tube', name='dna_cont_type_enum'))
    dna_cont_well = Column(Text())
    dna_container_id = Column(Text())
    dna_dnase = Column(Enum('no', 'yes', name='dna_dnase_enum'))
    dna_isolate_meth = Column(Text())
    dna_organisms = Column(Text())
    dna_project_contact = Column(Text())
    dna_samp_id = Column(Text())
    dna_sample_format = Column(Enum('10 mM Tris-HCl', 'DNAStable', 'Ethanol', 'Low EDTA TE', 'MDA reaction buffer', 'PBS', 'Pellet', 'RNAStable', 'TE', 'Water', name='dna_sample_format_enum'))
    dna_sample_name = Column(Text())
    dna_seq_project = Column(Text())
    dna_seq_project_pi = Column(Text())
    dna_seq_project_name = Column(Text())
    dna_volume = Column(Text())
    proposal_dna = Column(Text())
    dnase_rna = Column(Enum('no', 'yes', name='dnase_rna_enum'))
    proposal_rna = Column(Text())
    rna_absorb1 = Column(Text())
    rna_absorb2 = Column(Text())
    rna_collect_site = Column(Text())
    rna_concentration = Column(Text())
    rna_cont_type = Column(Enum('plate', 'tube', name='rna_cont_type_enum'))
    rna_cont_well = Column(Text())
    rna_container_id = Column(Text())
    rna_isolate_meth = Column(Text())
    rna_organisms = Column(Text())
    rna_project_contact = Column(Text())
    rna_samp_id = Column(Text())
    rna_sample_format = Column(Enum('10 mM Tris-HCl', 'DNAStable', 'Ethanol', 'Low EDTA TE', 'MDA reaction buffer', 'PBS', 'Pellet', 'RNAStable', 'TE', 'Water', name='rna_sample_format_enum'))
    rna_sample_name = Column(Text())
    rna_seq_project = Column(Text())
    rna_seq_project_pi = Column(Text())
    rna_seq_project_name = Column(Text())
    rna_volume = Column(Text())
    collection_date_inc = Column(Text())
    collection_time = Column(Text())
    collection_time_inc = Column(Text())
    experimental_factor_other = Column(Text())
    filter_method = Column(Text())
    isotope_exposure = Column(Text())
    micro_biomass_c_meth = Column(Text())
    micro_biomass_n_meth = Column(Text())
    microbial_biomass_c = Column(Text())
    microbial_biomass_n = Column(Text())
    non_microb_biomass = Column(Text())
    non_microb_biomass_method = Column(Text())
    org_nitro_method = Column(Text())
    other_treatment = Column(Text())
    start_date_inc = Column(Text())
    start_time_inc = Column(Text())
    project_id = Column(Text())
    replicate_number = Column(Text())
    sample_shipped = Column(Text())
    sample_type = Column(Enum('soil', 'water_extract_soil', name='sample_type_enum'))
    technical_reps = Column(Text())
    name = Column(Text())
    description = Column(Text())
    Database_id = Column(Text(), ForeignKey('Database.id'))
    agrochem_addition_id = Column(Text(), ForeignKey('QuantityValue.id'))
    agrochem_addition = relationship("QuantityValue", uselist=False)
    alkalinity_id = Column(Text(), ForeignKey('QuantityValue.id'))
    alkalinity = relationship("QuantityValue", uselist=False)
    alkalinity_method_id = Column(Text(), ForeignKey('TextValue.id'))
    alkalinity_method = relationship("TextValue", uselist=False)
    alkyl_diethers_id = Column(Text(), ForeignKey('QuantityValue.id'))
    alkyl_diethers = relationship("QuantityValue", uselist=False)
    alt_id = Column(Text(), ForeignKey('QuantityValue.id'))
    alt = relationship("QuantityValue", uselist=False)
    al_sat_id = Column(Text(), ForeignKey('QuantityValue.id'))
    al_sat = relationship("QuantityValue", uselist=False)
    al_sat_meth_id = Column(Text(), ForeignKey('TextValue.id'))
    al_sat_meth = relationship("TextValue", uselist=False)
    aminopept_act_id = Column(Text(), ForeignKey('QuantityValue.id'))
    aminopept_act = relationship("QuantityValue", uselist=False)
    ammonium_id = Column(Text(), ForeignKey('QuantityValue.id'))
    ammonium = relationship("QuantityValue", uselist=False)
    annual_precpt_id = Column(Text(), ForeignKey('QuantityValue.id'))
    annual_precpt = relationship("QuantityValue", uselist=False)
    annual_temp_id = Column(Text(), ForeignKey('QuantityValue.id'))
    annual_temp = relationship("QuantityValue", uselist=False)
    bacteria_carb_prod_id = Column(Text(), ForeignKey('QuantityValue.id'))
    bacteria_carb_prod = relationship("QuantityValue", uselist=False)
    bishomohopanol_id = Column(Text(), ForeignKey('QuantityValue.id'))
    bishomohopanol = relationship("QuantityValue", uselist=False)
    bromide_id = Column(Text(), ForeignKey('QuantityValue.id'))
    bromide = relationship("QuantityValue", uselist=False)
    calcium_id = Column(Text(), ForeignKey('QuantityValue.id'))
    calcium = relationship("QuantityValue", uselist=False)
    carb_nitro_ratio_id = Column(Text(), ForeignKey('QuantityValue.id'))
    carb_nitro_ratio = relationship("QuantityValue", uselist=False)
    chem_administration_id = Column(Text(), ForeignKey('ControlledTermValue.id'))
    chem_administration = relationship("ControlledTermValue", uselist=False)
    chloride_id = Column(Text(), ForeignKey('QuantityValue.id'))
    chloride = relationship("QuantityValue", uselist=False)
    chlorophyll_id = Column(Text(), ForeignKey('QuantityValue.id'))
    chlorophyll = relationship("QuantityValue", uselist=False)
    collection_date_id = Column(Text(), ForeignKey('TimestampValue.id'))
    collection_date = relationship("TimestampValue", uselist=False)
    cur_land_use_id = Column(Text(), ForeignKey('TextValue.id'))
    cur_land_use = relationship("TextValue", uselist=False)
    cur_vegetation_id = Column(Text(), ForeignKey('TextValue.id'))
    cur_vegetation = relationship("TextValue", uselist=False)
    cur_vegetation_meth_id = Column(Text(), ForeignKey('TextValue.id'))
    cur_vegetation_meth = relationship("TextValue", uselist=False)
    crop_rotation_id = Column(Text(), ForeignKey('TextValue.id'))
    crop_rotation = relationship("TextValue", uselist=False)
    density_id = Column(Text(), ForeignKey('QuantityValue.id'))
    density = relationship("QuantityValue", uselist=False)
    depth_id = Column(Text(), ForeignKey('QuantityValue.id'))
    depth = relationship("QuantityValue", uselist=False)
    diss_carb_dioxide_id = Column(Text(), ForeignKey('QuantityValue.id'))
    diss_carb_dioxide = relationship("QuantityValue", uselist=False)
    diss_hydrogen_id = Column(Text(), ForeignKey('QuantityValue.id'))
    diss_hydrogen = relationship("QuantityValue", uselist=False)
    diss_inorg_carb_id = Column(Text(), ForeignKey('QuantityValue.id'))
    diss_inorg_carb = relationship("QuantityValue", uselist=False)
    diss_inorg_phosp_id = Column(Text(), ForeignKey('QuantityValue.id'))
    diss_inorg_phosp = relationship("QuantityValue", uselist=False)
    diss_org_carb_id = Column(Text(), ForeignKey('QuantityValue.id'))
    diss_org_carb = relationship("QuantityValue", uselist=False)
    diss_org_nitro_id = Column(Text(), ForeignKey('QuantityValue.id'))
    diss_org_nitro = relationship("QuantityValue", uselist=False)
    diss_oxygen_id = Column(Text(), ForeignKey('QuantityValue.id'))
    diss_oxygen = relationship("QuantityValue", uselist=False)
    drainage_class_id = Column(Text(), ForeignKey('TextValue.id'))
    drainage_class = relationship("TextValue", uselist=False)
    elev_id = Column(Text(), ForeignKey('QuantityValue.id'))
    elev = relationship("QuantityValue", uselist=False)
    env_package_id = Column(Text(), ForeignKey('TextValue.id'))
    env_package = relationship("TextValue", uselist=False)
    env_broad_scale_id = Column(Text(), ForeignKey('ControlledTermValue.id'))
    env_broad_scale = relationship("ControlledTermValue", uselist=False)
    env_local_scale_id = Column(Text(), ForeignKey('ControlledTermValue.id'))
    env_local_scale = relationship("ControlledTermValue", uselist=False)
    env_medium_id = Column(Text(), ForeignKey('ControlledTermValue.id'))
    env_medium = relationship("ControlledTermValue", uselist=False)
    extreme_event_id = Column(Text(), ForeignKey('TimestampValue.id'))
    extreme_event = relationship("TimestampValue", uselist=False)
    fao_class_id = Column(Text(), ForeignKey('TextValue.id'))
    fao_class = relationship("TextValue", uselist=False)
    fire_id = Column(Text(), ForeignKey('TimestampValue.id'))
    fire = relationship("TimestampValue", uselist=False)
    flooding_id = Column(Text(), ForeignKey('TimestampValue.id'))
    flooding = relationship("TimestampValue", uselist=False)
    geo_loc_name_id = Column(Text(), ForeignKey('TextValue.id'))
    geo_loc_name = relationship("TextValue", uselist=False)
    glucosidase_act_id = Column(Text(), ForeignKey('QuantityValue.id'))
    glucosidase_act = relationship("QuantityValue", uselist=False)
    heavy_metals_id = Column(Text(), ForeignKey('QuantityValue.id'))
    heavy_metals = relationship("QuantityValue", uselist=False)
    heavy_metals_meth_id = Column(Text(), ForeignKey('TextValue.id'))
    heavy_metals_meth = relationship("TextValue", uselist=False)
    horizon_id = Column(Text(), ForeignKey('TextValue.id'))
    horizon = relationship("TextValue", uselist=False)
    horizon_meth_id = Column(Text(), ForeignKey('TextValue.id'))
    horizon_meth = relationship("TextValue", uselist=False)
    lat_lon_id = Column(Text(), ForeignKey('GeolocationValue.id'))
    lat_lon = relationship("GeolocationValue", uselist=False)
    link_addit_analys_id = Column(Text(), ForeignKey('TextValue.id'))
    link_addit_analys = relationship("TextValue", uselist=False)
    link_class_info_id = Column(Text(), ForeignKey('TextValue.id'))
    link_class_info = relationship("TextValue", uselist=False)
    link_climate_info_id = Column(Text(), ForeignKey('TextValue.id'))
    link_climate_info = relationship("TextValue", uselist=False)
    local_class_id = Column(Text(), ForeignKey('TextValue.id'))
    local_class = relationship("TextValue", uselist=False)
    local_class_meth_id = Column(Text(), ForeignKey('TextValue.id'))
    local_class_meth = relationship("TextValue", uselist=False)
    magnesium_id = Column(Text(), ForeignKey('QuantityValue.id'))
    magnesium = relationship("QuantityValue", uselist=False)
    mean_frict_vel_id = Column(Text(), ForeignKey('QuantityValue.id'))
    mean_frict_vel = relationship("QuantityValue", uselist=False)
    mean_peak_frict_vel_id = Column(Text(), ForeignKey('QuantityValue.id'))
    mean_peak_frict_vel = relationship("QuantityValue", uselist=False)
    microbial_biomass_id = Column(Text(), ForeignKey('QuantityValue.id'))
    microbial_biomass = relationship("QuantityValue", uselist=False)
    microbial_biomass_meth_id = Column(Text(), ForeignKey('TextValue.id'))
    microbial_biomass_meth = relationship("TextValue", uselist=False)
    misc_param_id = Column(Text(), ForeignKey('QuantityValue.id'))
    misc_param = relationship("QuantityValue", uselist=False)
    n_alkanes_id = Column(Text(), ForeignKey('QuantityValue.id'))
    n_alkanes = relationship("QuantityValue", uselist=False)
    nitrate_id = Column(Text(), ForeignKey('QuantityValue.id'))
    nitrate = relationship("QuantityValue", uselist=False)
    nitrite_id = Column(Text(), ForeignKey('QuantityValue.id'))
    nitrite = relationship("QuantityValue", uselist=False)
    org_matter_id = Column(Text(), ForeignKey('QuantityValue.id'))
    org_matter = relationship("QuantityValue", uselist=False)
    org_nitro_id = Column(Text(), ForeignKey('QuantityValue.id'))
    org_nitro = relationship("QuantityValue", uselist=False)
    organism_count_id = Column(Text(), ForeignKey('QuantityValue.id'))
    organism_count = relationship("QuantityValue", uselist=False)
    oxy_stat_samp_id = Column(Text(), ForeignKey('TextValue.id'))
    oxy_stat_samp = relationship("TextValue", uselist=False)
    part_org_carb_id = Column(Text(), ForeignKey('QuantityValue.id'))
    part_org_carb = relationship("QuantityValue", uselist=False)
    perturbation_id = Column(Text(), ForeignKey('TextValue.id'))
    perturbation = relationship("TextValue", uselist=False)
    petroleum_hydrocarb_id = Column(Text(), ForeignKey('QuantityValue.id'))
    petroleum_hydrocarb = relationship("QuantityValue", uselist=False)
    ph_id = Column(Text(), ForeignKey('QuantityValue.id'))
    ph = relationship("QuantityValue", uselist=False)
    ph_meth_id = Column(Text(), ForeignKey('TextValue.id'))
    ph_meth = relationship("TextValue", uselist=False)
    phaeopigments_id = Column(Text(), ForeignKey('QuantityValue.id'))
    phaeopigments = relationship("QuantityValue", uselist=False)
    phosplipid_fatt_acid_id = Column(Text(), ForeignKey('QuantityValue.id'))
    phosplipid_fatt_acid = relationship("QuantityValue", uselist=False)
    pool_dna_extracts_id = Column(Text(), ForeignKey('TextValue.id'))
    pool_dna_extracts = relationship("TextValue", uselist=False)
    potassium_id = Column(Text(), ForeignKey('QuantityValue.id'))
    potassium = relationship("QuantityValue", uselist=False)
    pressure_id = Column(Text(), ForeignKey('QuantityValue.id'))
    pressure = relationship("QuantityValue", uselist=False)
    previous_land_use_id = Column(Text(), ForeignKey('TextValue.id'))
    previous_land_use = relationship("TextValue", uselist=False)
    previous_land_use_meth_id = Column(Text(), ForeignKey('TextValue.id'))
    previous_land_use_meth = relationship("TextValue", uselist=False)
    profile_position_id = Column(Text(), ForeignKey('TextValue.id'))
    profile_position = relationship("TextValue", uselist=False)
    redox_potential_id = Column(Text(), ForeignKey('QuantityValue.id'))
    redox_potential = relationship("QuantityValue", uselist=False)
    salinity_id = Column(Text(), ForeignKey('QuantityValue.id'))
    salinity = relationship("QuantityValue", uselist=False)
    salinity_meth_id = Column(Text(), ForeignKey('TextValue.id'))
    salinity_meth = relationship("TextValue", uselist=False)
    samp_collect_device_id = Column(Text(), ForeignKey('TextValue.id'))
    samp_collect_device = relationship("TextValue", uselist=False)
    samp_mat_process_id = Column(Text(), ForeignKey('ControlledTermValue.id'))
    samp_mat_process = relationship("ControlledTermValue", uselist=False)
    samp_store_dur_id = Column(Text(), ForeignKey('TextValue.id'))
    samp_store_dur = relationship("TextValue", uselist=False)
    samp_store_loc_id = Column(Text(), ForeignKey('TextValue.id'))
    samp_store_loc = relationship("TextValue", uselist=False)
    samp_store_temp_id = Column(Text(), ForeignKey('QuantityValue.id'))
    samp_store_temp = relationship("QuantityValue", uselist=False)
    samp_vol_we_dna_ext_id = Column(Text(), ForeignKey('QuantityValue.id'))
    samp_vol_we_dna_ext = relationship("QuantityValue", uselist=False)
    season_temp_id = Column(Text(), ForeignKey('QuantityValue.id'))
    season_temp = relationship("QuantityValue", uselist=False)
    season_precpt_id = Column(Text(), ForeignKey('QuantityValue.id'))
    season_precpt = relationship("QuantityValue", uselist=False)
    sieving_id = Column(Text(), ForeignKey('QuantityValue.id'))
    sieving = relationship("QuantityValue", uselist=False)
    size_frac_low_id = Column(Text(), ForeignKey('QuantityValue.id'))
    size_frac_low = relationship("QuantityValue", uselist=False)
    size_frac_up_id = Column(Text(), ForeignKey('QuantityValue.id'))
    size_frac_up = relationship("QuantityValue", uselist=False)
    slope_gradient_id = Column(Text(), ForeignKey('QuantityValue.id'))
    slope_gradient = relationship("QuantityValue", uselist=False)
    slope_aspect_id = Column(Text(), ForeignKey('QuantityValue.id'))
    slope_aspect = relationship("QuantityValue", uselist=False)
    sodium_id = Column(Text(), ForeignKey('QuantityValue.id'))
    sodium = relationship("QuantityValue", uselist=False)
    soil_type_id = Column(Text(), ForeignKey('TextValue.id'))
    soil_type = relationship("TextValue", uselist=False)
    soil_type_meth_id = Column(Text(), ForeignKey('TextValue.id'))
    soil_type_meth = relationship("TextValue", uselist=False)
    store_cond_id = Column(Text(), ForeignKey('TextValue.id'))
    store_cond = relationship("TextValue", uselist=False)
    sulfate_id = Column(Text(), ForeignKey('QuantityValue.id'))
    sulfate = relationship("QuantityValue", uselist=False)
    sulfide_id = Column(Text(), ForeignKey('QuantityValue.id'))
    sulfide = relationship("QuantityValue", uselist=False)
    temp_id = Column(Text(), ForeignKey('QuantityValue.id'))
    temp = relationship("QuantityValue", uselist=False)
    texture_id = Column(Text(), ForeignKey('QuantityValue.id'))
    texture = relationship("QuantityValue", uselist=False)
    texture_meth_id = Column(Text(), ForeignKey('TextValue.id'))
    texture_meth = relationship("TextValue", uselist=False)
    tillage_id = Column(Text(), ForeignKey('TextValue.id'))
    tillage = relationship("TextValue", uselist=False)
    tidal_stage_id = Column(Text(), ForeignKey('TextValue.id'))
    tidal_stage = relationship("TextValue", uselist=False)
    tot_carb_id = Column(Text(), ForeignKey('QuantityValue.id'))
    tot_carb = relationship("QuantityValue", uselist=False)
    tot_depth_water_col_id = Column(Text(), ForeignKey('QuantityValue.id'))
    tot_depth_water_col = relationship("QuantityValue", uselist=False)
    tot_diss_nitro_id = Column(Text(), ForeignKey('QuantityValue.id'))
    tot_diss_nitro = relationship("QuantityValue", uselist=False)
    tot_org_carb_id = Column(Text(), ForeignKey('QuantityValue.id'))
    tot_org_carb = relationship("QuantityValue", uselist=False)
    tot_org_c_meth_id = Column(Text(), ForeignKey('TextValue.id'))
    tot_org_c_meth = relationship("TextValue", uselist=False)
    tot_nitro_content_id = Column(Text(), ForeignKey('QuantityValue.id'))
    tot_nitro_content = relationship("QuantityValue", uselist=False)
    tot_phosp_id = Column(Text(), ForeignKey('QuantityValue.id'))
    tot_phosp = relationship("QuantityValue", uselist=False)
    water_content_id = Column(Text(), ForeignKey('QuantityValue.id'))
    water_content = relationship("QuantityValue", uselist=False)
    depth2_id = Column(Text(), ForeignKey('QuantityValue.id'))
    depth2 = relationship("QuantityValue", uselist=False)
    subsurface_depth_id = Column(Text(), ForeignKey('QuantityValue.id'))
    subsurface_depth = relationship("QuantityValue", uselist=False)
    subsurface_depth2_id = Column(Text(), ForeignKey('QuantityValue.id'))
    subsurface_depth2 = relationship("QuantityValue", uselist=False)
    air_temp_regm_id = Column(Text(), ForeignKey('QuantityValue.id'))
    air_temp_regm = relationship("QuantityValue", uselist=False)
    biotic_regm_id = Column(Text(), ForeignKey('TextValue.id'))
    biotic_regm = relationship("TextValue", uselist=False)
    biotic_relationship_id = Column(Text(), ForeignKey('TextValue.id'))
    biotic_relationship = relationship("TextValue", uselist=False)
    climate_environment_id = Column(Text(), ForeignKey('TextValue.id'))
    climate_environment = relationship("TextValue", uselist=False)
    experimental_factor_id = Column(Text(), ForeignKey('ControlledTermValue.id'))
    experimental_factor = relationship("ControlledTermValue", uselist=False)
    gaseous_environment_id = Column(Text(), ForeignKey('QuantityValue.id'))
    gaseous_environment = relationship("QuantityValue", uselist=False)
    growth_facil_id = Column(Text(), ForeignKey('ControlledTermValue.id'))
    growth_facil = relationship("ControlledTermValue", uselist=False)
    humidity_regm_id = Column(Text(), ForeignKey('QuantityValue.id'))
    humidity_regm = relationship("QuantityValue", uselist=False)
    light_regm_id = Column(Text(), ForeignKey('QuantityValue.id'))
    light_regm = relationship("QuantityValue", uselist=False)
    phosphate_id = Column(Text(), ForeignKey('QuantityValue.id'))
    phosphate = relationship("QuantityValue", uselist=False)
    rel_to_oxygen_id = Column(Text(), ForeignKey('TextValue.id'))
    rel_to_oxygen = relationship("TextValue", uselist=False)
    samp_size_id = Column(Text(), ForeignKey('QuantityValue.id'))
    samp_size = relationship("QuantityValue", uselist=False)
    soil_text_measure_id = Column(Text(), ForeignKey('QuantityValue.id'))
    soil_text_measure = relationship("QuantityValue", uselist=False)
    source_mat_id_id = Column(Text(), ForeignKey('TextValue.id'))
    source_mat_id = relationship("TextValue", uselist=False)
    watering_regm_id = Column(Text(), ForeignKey('QuantityValue.id'))
    watering_regm = relationship("QuantityValue", uselist=False)
    zinc_id = Column(Text(), ForeignKey('QuantityValue.id'))
    zinc = relationship("QuantityValue", uselist=False)
    manganese_id = Column(Text(), ForeignKey('QuantityValue.id'))
    manganese = relationship("QuantityValue", uselist=False)
    ammonium_nitrogen_id = Column(Text(), ForeignKey('QuantityValue.id'))
    ammonium_nitrogen = relationship("QuantityValue", uselist=False)
    nitrate_nitrogen_id = Column(Text(), ForeignKey('QuantityValue.id'))
    nitrate_nitrogen = relationship("QuantityValue", uselist=False)
    nitrite_nitrogen_id = Column(Text(), ForeignKey('QuantityValue.id'))
    nitrite_nitrogen = relationship("QuantityValue", uselist=False)
    lbc_thirty_id = Column(Text(), ForeignKey('QuantityValue.id'))
    lbc_thirty = relationship("QuantityValue", uselist=False)
    lbceq_id = Column(Text(), ForeignKey('QuantityValue.id'))
    lbceq = relationship("QuantityValue", uselist=False)
    
    
    biosample_categories_rel = relationship( "BiosampleBiosampleCategories" )
    biosample_categories = association_proxy("biosample_categories_rel", "biosample_categories",
                                  creator=lambda x_: BiosampleBiosampleCategories(biosample_categories=x_))
    
    
    # ManyToMany
    part_of = relationship( "NamedThing", secondary="Biosample_part_of")
    
    
    alternative_identifiers_rel = relationship( "BiosampleAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: BiosampleAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    gold_sample_identifiers_rel = relationship( "BiosampleGoldSampleIdentifiers" )
    gold_sample_identifiers = association_proxy("gold_sample_identifiers_rel", "gold_sample_identifiers",
                                  creator=lambda x_: BiosampleGoldSampleIdentifiers(gold_sample_identifiers=x_))
    
    
    analysis_type_rel = relationship( "BiosampleAnalysisType" )
    analysis_type = association_proxy("analysis_type_rel", "analysis_type",
                                  creator=lambda x_: BiosampleAnalysisType(analysis_type=x_))
    
    
    sample_link_rel = relationship( "BiosampleSampleLink" )
    sample_link = association_proxy("sample_link_rel", "sample_link",
                                  creator=lambda x_: BiosampleSampleLink(sample_link=x_))
    
    
    def __repr__(self):
        return f"Biosample(type={self.type},id={self.id},tot_nitro_cont_meth={self.tot_nitro_cont_meth},water_cont_soil_meth={self.water_cont_soil_meth},ecosystem={self.ecosystem},ecosystem_category={self.ecosystem_category},ecosystem_type={self.ecosystem_type},ecosystem_subtype={self.ecosystem_subtype},specific_ecosystem={self.specific_ecosystem},add_date={self.add_date},community={self.community},habitat={self.habitat},host_name={self.host_name},identifier={self.identifier},location={self.location},mod_date={self.mod_date},ncbi_taxonomy_name={self.ncbi_taxonomy_name},proport_woa_temperature={self.proport_woa_temperature},salinity_category={self.salinity_category},sample_collection_site={self.sample_collection_site},soluble_iron_micromol={self.soluble_iron_micromol},micro_biomass_meth={self.micro_biomass_meth},samp_collec_method={self.samp_collec_method},soil_texture_meth={self.soil_texture_meth},dna_absorb1={self.dna_absorb1},dna_absorb2={self.dna_absorb2},dna_collect_site={self.dna_collect_site},dna_concentration={self.dna_concentration},dna_cont_type={self.dna_cont_type},dna_cont_well={self.dna_cont_well},dna_container_id={self.dna_container_id},dna_dnase={self.dna_dnase},dna_isolate_meth={self.dna_isolate_meth},dna_organisms={self.dna_organisms},dna_project_contact={self.dna_project_contact},dna_samp_id={self.dna_samp_id},dna_sample_format={self.dna_sample_format},dna_sample_name={self.dna_sample_name},dna_seq_project={self.dna_seq_project},dna_seq_project_pi={self.dna_seq_project_pi},dna_seq_project_name={self.dna_seq_project_name},dna_volume={self.dna_volume},proposal_dna={self.proposal_dna},dnase_rna={self.dnase_rna},proposal_rna={self.proposal_rna},rna_absorb1={self.rna_absorb1},rna_absorb2={self.rna_absorb2},rna_collect_site={self.rna_collect_site},rna_concentration={self.rna_concentration},rna_cont_type={self.rna_cont_type},rna_cont_well={self.rna_cont_well},rna_container_id={self.rna_container_id},rna_isolate_meth={self.rna_isolate_meth},rna_organisms={self.rna_organisms},rna_project_contact={self.rna_project_contact},rna_samp_id={self.rna_samp_id},rna_sample_format={self.rna_sample_format},rna_sample_name={self.rna_sample_name},rna_seq_project={self.rna_seq_project},rna_seq_project_pi={self.rna_seq_project_pi},rna_seq_project_name={self.rna_seq_project_name},rna_volume={self.rna_volume},collection_date_inc={self.collection_date_inc},collection_time={self.collection_time},collection_time_inc={self.collection_time_inc},experimental_factor_other={self.experimental_factor_other},filter_method={self.filter_method},isotope_exposure={self.isotope_exposure},micro_biomass_c_meth={self.micro_biomass_c_meth},micro_biomass_n_meth={self.micro_biomass_n_meth},microbial_biomass_c={self.microbial_biomass_c},microbial_biomass_n={self.microbial_biomass_n},non_microb_biomass={self.non_microb_biomass},non_microb_biomass_method={self.non_microb_biomass_method},org_nitro_method={self.org_nitro_method},other_treatment={self.other_treatment},start_date_inc={self.start_date_inc},start_time_inc={self.start_time_inc},project_id={self.project_id},replicate_number={self.replicate_number},sample_shipped={self.sample_shipped},sample_type={self.sample_type},technical_reps={self.technical_reps},name={self.name},description={self.description},Database_id={self.Database_id},agrochem_addition_id={self.agrochem_addition_id},alkalinity_id={self.alkalinity_id},alkalinity_method_id={self.alkalinity_method_id},alkyl_diethers_id={self.alkyl_diethers_id},alt_id={self.alt_id},al_sat_id={self.al_sat_id},al_sat_meth_id={self.al_sat_meth_id},aminopept_act_id={self.aminopept_act_id},ammonium_id={self.ammonium_id},annual_precpt_id={self.annual_precpt_id},annual_temp_id={self.annual_temp_id},bacteria_carb_prod_id={self.bacteria_carb_prod_id},bishomohopanol_id={self.bishomohopanol_id},bromide_id={self.bromide_id},calcium_id={self.calcium_id},carb_nitro_ratio_id={self.carb_nitro_ratio_id},chem_administration_id={self.chem_administration_id},chloride_id={self.chloride_id},chlorophyll_id={self.chlorophyll_id},collection_date_id={self.collection_date_id},cur_land_use_id={self.cur_land_use_id},cur_vegetation_id={self.cur_vegetation_id},cur_vegetation_meth_id={self.cur_vegetation_meth_id},crop_rotation_id={self.crop_rotation_id},density_id={self.density_id},depth_id={self.depth_id},diss_carb_dioxide_id={self.diss_carb_dioxide_id},diss_hydrogen_id={self.diss_hydrogen_id},diss_inorg_carb_id={self.diss_inorg_carb_id},diss_inorg_phosp_id={self.diss_inorg_phosp_id},diss_org_carb_id={self.diss_org_carb_id},diss_org_nitro_id={self.diss_org_nitro_id},diss_oxygen_id={self.diss_oxygen_id},drainage_class_id={self.drainage_class_id},elev_id={self.elev_id},env_package_id={self.env_package_id},env_broad_scale_id={self.env_broad_scale_id},env_local_scale_id={self.env_local_scale_id},env_medium_id={self.env_medium_id},extreme_event_id={self.extreme_event_id},fao_class_id={self.fao_class_id},fire_id={self.fire_id},flooding_id={self.flooding_id},geo_loc_name_id={self.geo_loc_name_id},glucosidase_act_id={self.glucosidase_act_id},heavy_metals_id={self.heavy_metals_id},heavy_metals_meth_id={self.heavy_metals_meth_id},horizon_id={self.horizon_id},horizon_meth_id={self.horizon_meth_id},lat_lon_id={self.lat_lon_id},link_addit_analys_id={self.link_addit_analys_id},link_class_info_id={self.link_class_info_id},link_climate_info_id={self.link_climate_info_id},local_class_id={self.local_class_id},local_class_meth_id={self.local_class_meth_id},magnesium_id={self.magnesium_id},mean_frict_vel_id={self.mean_frict_vel_id},mean_peak_frict_vel_id={self.mean_peak_frict_vel_id},microbial_biomass_id={self.microbial_biomass_id},microbial_biomass_meth_id={self.microbial_biomass_meth_id},misc_param_id={self.misc_param_id},n_alkanes_id={self.n_alkanes_id},nitrate_id={self.nitrate_id},nitrite_id={self.nitrite_id},org_matter_id={self.org_matter_id},org_nitro_id={self.org_nitro_id},organism_count_id={self.organism_count_id},oxy_stat_samp_id={self.oxy_stat_samp_id},part_org_carb_id={self.part_org_carb_id},perturbation_id={self.perturbation_id},petroleum_hydrocarb_id={self.petroleum_hydrocarb_id},ph_id={self.ph_id},ph_meth_id={self.ph_meth_id},phaeopigments_id={self.phaeopigments_id},phosplipid_fatt_acid_id={self.phosplipid_fatt_acid_id},pool_dna_extracts_id={self.pool_dna_extracts_id},potassium_id={self.potassium_id},pressure_id={self.pressure_id},previous_land_use_id={self.previous_land_use_id},previous_land_use_meth_id={self.previous_land_use_meth_id},profile_position_id={self.profile_position_id},redox_potential_id={self.redox_potential_id},salinity_id={self.salinity_id},salinity_meth_id={self.salinity_meth_id},samp_collect_device_id={self.samp_collect_device_id},samp_mat_process_id={self.samp_mat_process_id},samp_store_dur_id={self.samp_store_dur_id},samp_store_loc_id={self.samp_store_loc_id},samp_store_temp_id={self.samp_store_temp_id},samp_vol_we_dna_ext_id={self.samp_vol_we_dna_ext_id},season_temp_id={self.season_temp_id},season_precpt_id={self.season_precpt_id},sieving_id={self.sieving_id},size_frac_low_id={self.size_frac_low_id},size_frac_up_id={self.size_frac_up_id},slope_gradient_id={self.slope_gradient_id},slope_aspect_id={self.slope_aspect_id},sodium_id={self.sodium_id},soil_type_id={self.soil_type_id},soil_type_meth_id={self.soil_type_meth_id},store_cond_id={self.store_cond_id},sulfate_id={self.sulfate_id},sulfide_id={self.sulfide_id},temp_id={self.temp_id},texture_id={self.texture_id},texture_meth_id={self.texture_meth_id},tillage_id={self.tillage_id},tidal_stage_id={self.tidal_stage_id},tot_carb_id={self.tot_carb_id},tot_depth_water_col_id={self.tot_depth_water_col_id},tot_diss_nitro_id={self.tot_diss_nitro_id},tot_org_carb_id={self.tot_org_carb_id},tot_org_c_meth_id={self.tot_org_c_meth_id},tot_nitro_content_id={self.tot_nitro_content_id},tot_phosp_id={self.tot_phosp_id},water_content_id={self.water_content_id},depth2_id={self.depth2_id},subsurface_depth_id={self.subsurface_depth_id},subsurface_depth2_id={self.subsurface_depth2_id},air_temp_regm_id={self.air_temp_regm_id},biotic_regm_id={self.biotic_regm_id},biotic_relationship_id={self.biotic_relationship_id},climate_environment_id={self.climate_environment_id},experimental_factor_id={self.experimental_factor_id},gaseous_environment_id={self.gaseous_environment_id},growth_facil_id={self.growth_facil_id},humidity_regm_id={self.humidity_regm_id},light_regm_id={self.light_regm_id},phosphate_id={self.phosphate_id},rel_to_oxygen_id={self.rel_to_oxygen_id},samp_size_id={self.samp_size_id},soil_text_measure_id={self.soil_text_measure_id},source_mat_id_id={self.source_mat_id_id},watering_regm_id={self.watering_regm_id},zinc_id={self.zinc_id},manganese_id={self.manganese_id},ammonium_nitrogen_id={self.ammonium_nitrogen_id},nitrate_nitrogen_id={self.nitrate_nitrogen_id},nitrite_nitrogen_id={self.nitrite_nitrogen_id},lbc_thirty_id={self.lbc_thirty_id},lbceq_id={self.lbceq_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Study(NamedThing):
    """
    A study summarizes the overall goal of a research initiative and outlines the key objective of its underlying projects.
    """
    __tablename__ = 'Study'
    
    id = Column(Text(), primary_key=True)
    related_identifiers = Column(Text())
    emsl_proposal_identifier = Column(Text())
    emsl_proposal_doi = Column(Text())
    mgnify_project_identifiers = Column(Text())
    ecosystem = Column(Text())
    ecosystem_category = Column(Text())
    ecosystem_type = Column(Text())
    ecosystem_subtype = Column(Text())
    specific_ecosystem = Column(Text())
    title = Column(Text())
    abstract = Column(Text())
    objective = Column(Text())
    type = Column(Text())
    name = Column(Text())
    description = Column(Text())
    Database_id = Column(Text(), ForeignKey('Database.id'))
    principal_investigator_id = Column(Text(), ForeignKey('PersonValue.id'))
    principal_investigator = relationship("PersonValue", uselist=False)
    doi_id = Column(Text(), ForeignKey('AttributeValue.id'))
    doi = relationship("AttributeValue", uselist=False)
    
    
    alternative_identifiers_rel = relationship( "StudyAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: StudyAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    gold_study_identifiers_rel = relationship( "StudyGoldStudyIdentifiers" )
    gold_study_identifiers = association_proxy("gold_study_identifiers_rel", "gold_study_identifiers",
                                  creator=lambda x_: StudyGoldStudyIdentifiers(gold_study_identifiers=x_))
    
    
    alternative_titles_rel = relationship( "StudyAlternativeTitles" )
    alternative_titles = association_proxy("alternative_titles_rel", "alternative_titles",
                                  creator=lambda x_: StudyAlternativeTitles(alternative_titles=x_))
    
    
    alternative_descriptions_rel = relationship( "StudyAlternativeDescriptions" )
    alternative_descriptions = association_proxy("alternative_descriptions_rel", "alternative_descriptions",
                                  creator=lambda x_: StudyAlternativeDescriptions(alternative_descriptions=x_))
    
    
    alternative_names_rel = relationship( "StudyAlternativeNames" )
    alternative_names = association_proxy("alternative_names_rel", "alternative_names",
                                  creator=lambda x_: StudyAlternativeNames(alternative_names=x_))
    
    
    websites_rel = relationship( "StudyWebsites" )
    websites = association_proxy("websites_rel", "websites",
                                  creator=lambda x_: StudyWebsites(websites=x_))
    
    
    publications_rel = relationship( "StudyPublications" )
    publications = association_proxy("publications_rel", "publications",
                                  creator=lambda x_: StudyPublications(publications=x_))
    
    
    ess_dive_datasets_rel = relationship( "StudyEssDiveDatasets" )
    ess_dive_datasets = association_proxy("ess_dive_datasets_rel", "ess_dive_datasets",
                                  creator=lambda x_: StudyEssDiveDatasets(ess_dive_datasets=x_))
    
    
    relevant_protocols_rel = relationship( "StudyRelevantProtocols" )
    relevant_protocols = association_proxy("relevant_protocols_rel", "relevant_protocols",
                                  creator=lambda x_: StudyRelevantProtocols(relevant_protocols=x_))
    
    
    funding_sources_rel = relationship( "StudyFundingSources" )
    funding_sources = association_proxy("funding_sources_rel", "funding_sources",
                                  creator=lambda x_: StudyFundingSources(funding_sources=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Study', source_slot='has_credit_associations', mapping_type=None, target_class='CreditAssociation', target_slot='Study_id', join_class=None, uses_join_table=None, multivalued=False)
    has_credit_associations = relationship( "CreditAssociation", foreign_keys="[CreditAssociation.Study_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Study', source_slot='study_image', mapping_type=None, target_class='ImageValue', target_slot='Study_id', join_class=None, uses_join_table=None, multivalued=False)
    study_image = relationship( "ImageValue", foreign_keys="[ImageValue.Study_id]")
    
    
    def __repr__(self):
        return f"Study(id={self.id},related_identifiers={self.related_identifiers},emsl_proposal_identifier={self.emsl_proposal_identifier},emsl_proposal_doi={self.emsl_proposal_doi},mgnify_project_identifiers={self.mgnify_project_identifiers},ecosystem={self.ecosystem},ecosystem_category={self.ecosystem_category},ecosystem_type={self.ecosystem_type},ecosystem_subtype={self.ecosystem_subtype},specific_ecosystem={self.specific_ecosystem},title={self.title},abstract={self.abstract},objective={self.objective},type={self.type},name={self.name},description={self.description},Database_id={self.Database_id},principal_investigator_id={self.principal_investigator_id},doi_id={self.doi_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class BiosampleProcessing(NamedThing):
    """
    A process that takes one or more biosamples as inputs and generates one or as outputs. Examples of outputs include samples cultivated from another sample or data objects created by instruments runs.
    """
    __tablename__ = 'BiosampleProcessing'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    
    
    # ManyToMany
    has_input = relationship( "Biosample", secondary="BiosampleProcessing_has_input")
    
    
    alternative_identifiers_rel = relationship( "BiosampleProcessingAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: BiosampleProcessingAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"BiosampleProcessing(id={self.id},name={self.name},description={self.description},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class WorkflowExecutionActivity(Activity):
    """
    Represents an instance of an execution of a particular workflow
    """
    __tablename__ = 'WorkflowExecutionActivity'
    
    execution_resource = Column(Text())
    git_url = Column(Text())
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    started_at_time = Column(DateTime())
    ended_at_time = Column(DateTime())
    was_informed_by = Column(Text(), ForeignKey('Activity.id'))
    was_associated_with = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'))
    used = Column(Text())
    Database_id = Column(Text(), ForeignKey('Database.id'))
    
    
    # ManyToMany
    has_input = relationship( "NamedThing", secondary="WorkflowExecutionActivity_has_input")
    
    
    # ManyToMany
    has_output = relationship( "NamedThing", secondary="WorkflowExecutionActivity_has_output")
    
    
    # ManyToMany
    part_of = relationship( "NamedThing", secondary="WorkflowExecutionActivity_part_of")
    
    
    def __repr__(self):
        return f"WorkflowExecutionActivity(execution_resource={self.execution_resource},git_url={self.git_url},type={self.type},id={self.id},name={self.name},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},was_informed_by={self.was_informed_by},was_associated_with={self.was_associated_with},used={self.used},Database_id={self.Database_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class OntologyClass(NamedThing):
    """
    
    """
    __tablename__ = 'OntologyClass'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    
    
    alternative_identifiers_rel = relationship( "OntologyClassAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: OntologyClassAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"OntologyClass(id={self.id},name={self.name},description={self.description},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class QuantityValue(AttributeValue):
    """
    A simple quantity, e.g. 2cm
    """
    __tablename__ = 'QuantityValue'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    has_unit = Column(Text())
    has_numeric_value = Column(Float())
    has_minimum_numeric_value = Column(Float())
    has_maximum_numeric_value = Column(Float())
    has_raw_value = Column(Text())
    was_generated_by = Column(Text(), ForeignKey('Activity.id'))
    
    
    def __repr__(self):
        return f"QuantityValue(id={self.id},has_unit={self.has_unit},has_numeric_value={self.has_numeric_value},has_minimum_numeric_value={self.has_minimum_numeric_value},has_maximum_numeric_value={self.has_maximum_numeric_value},has_raw_value={self.has_raw_value},was_generated_by={self.was_generated_by},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ImageValue(AttributeValue):
    """
    An attribute value representing an image.
    """
    __tablename__ = 'ImageValue'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    url = Column(Text())
    description = Column(Text())
    display_order = Column(Text())
    has_raw_value = Column(Text())
    was_generated_by = Column(Text(), ForeignKey('Activity.id'))
    Study_id = Column(Text(), ForeignKey('Study.id'))
    
    
    def __repr__(self):
        return f"ImageValue(id={self.id},url={self.url},description={self.description},display_order={self.display_order},has_raw_value={self.has_raw_value},was_generated_by={self.was_generated_by},Study_id={self.Study_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PersonValue(AttributeValue):
    """
    An attribute value representing a person
    """
    __tablename__ = 'PersonValue'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    orcid = Column(Text())
    profile_image_url = Column(Text())
    email = Column(Text())
    name = Column(Text())
    has_raw_value = Column(Text())
    was_generated_by = Column(Text(), ForeignKey('Activity.id'))
    
    
    websites_rel = relationship( "PersonValueWebsites" )
    websites = association_proxy("websites_rel", "websites",
                                  creator=lambda x_: PersonValueWebsites(websites=x_))
    
    
    def __repr__(self):
        return f"PersonValue(id={self.id},orcid={self.orcid},profile_image_url={self.profile_image_url},email={self.email},name={self.name},has_raw_value={self.has_raw_value},was_generated_by={self.was_generated_by},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Person(NamedThing):
    """
    represents a person, such as a researcher
    """
    __tablename__ = 'Person'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    
    
    alternative_identifiers_rel = relationship( "PersonAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: PersonAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"Person(id={self.id},name={self.name},description={self.description},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Instrument(NamedThing):
    """
    A material entity that is designed to perform a function in a scientific investigation, but is not a reagent[OBI].
    """
    __tablename__ = 'Instrument'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    
    
    alternative_identifiers_rel = relationship( "InstrumentAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: InstrumentAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"Instrument(id={self.id},name={self.name},description={self.description},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class GeneProduct(NamedThing):
    """
    A molecule encoded by a gene that has an evolved function
    """
    __tablename__ = 'GeneProduct'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    
    
    alternative_identifiers_rel = relationship( "GeneProductAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: GeneProductAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"GeneProduct(id={self.id},name={self.name},description={self.description},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class TextValue(AttributeValue):
    """
    A basic string value
    """
    __tablename__ = 'TextValue'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    language = Column(Text())
    has_raw_value = Column(Text())
    was_generated_by = Column(Text(), ForeignKey('Activity.id'))
    
    
    def __repr__(self):
        return f"TextValue(id={self.id},language={self.language},has_raw_value={self.has_raw_value},was_generated_by={self.was_generated_by},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class UrlValue(AttributeValue):
    """
    A value that is a string that conforms to URL syntax
    """
    __tablename__ = 'UrlValue'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    has_raw_value = Column(Text())
    was_generated_by = Column(Text(), ForeignKey('Activity.id'))
    
    
    def __repr__(self):
        return f"UrlValue(id={self.id},has_raw_value={self.has_raw_value},was_generated_by={self.was_generated_by},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class TimestampValue(AttributeValue):
    """
    A value that is a timestamp. The range should be ISO-8601
    """
    __tablename__ = 'TimestampValue'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    has_raw_value = Column(Text())
    was_generated_by = Column(Text(), ForeignKey('Activity.id'))
    
    
    def __repr__(self):
        return f"TimestampValue(id={self.id},has_raw_value={self.has_raw_value},was_generated_by={self.was_generated_by},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class IntegerValue(AttributeValue):
    """
    A value that is an integer
    """
    __tablename__ = 'IntegerValue'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    has_numeric_value = Column(Float())
    has_raw_value = Column(Text())
    was_generated_by = Column(Text(), ForeignKey('Activity.id'))
    
    
    def __repr__(self):
        return f"IntegerValue(id={self.id},has_numeric_value={self.has_numeric_value},has_raw_value={self.has_raw_value},was_generated_by={self.was_generated_by},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class BooleanValue(AttributeValue):
    """
    A value that is a boolean
    """
    __tablename__ = 'BooleanValue'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    has_boolean_value = Column(Boolean())
    has_raw_value = Column(Text())
    was_generated_by = Column(Text(), ForeignKey('Activity.id'))
    
    
    def __repr__(self):
        return f"BooleanValue(id={self.id},has_boolean_value={self.has_boolean_value},has_raw_value={self.has_raw_value},was_generated_by={self.was_generated_by},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ControlledTermValue(AttributeValue):
    """
    A controlled term or class from an ontology
    """
    __tablename__ = 'ControlledTermValue'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    has_raw_value = Column(Text())
    was_generated_by = Column(Text(), ForeignKey('Activity.id'))
    term_id = Column(Text(), ForeignKey('OntologyClass.id'))
    term = relationship("OntologyClass", uselist=False)
    
    
    def __repr__(self):
        return f"ControlledTermValue(id={self.id},has_raw_value={self.has_raw_value},was_generated_by={self.was_generated_by},term_id={self.term_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class GeolocationValue(AttributeValue):
    """
    A normalized value for a location on the earth's surface
    """
    __tablename__ = 'GeolocationValue'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    latitude = Column(Float())
    longitude = Column(Float())
    has_raw_value = Column(Text())
    was_generated_by = Column(Text(), ForeignKey('Activity.id'))
    
    
    def __repr__(self):
        return f"GeolocationValue(id={self.id},latitude={self.latitude},longitude={self.longitude},has_raw_value={self.has_raw_value},was_generated_by={self.was_generated_by},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MaterialSample(NamedThing):
    """
    
    """
    __tablename__ = 'MaterialSample'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    Database_id = Column(Text(), ForeignKey('Database.id'))
    
    
    alternative_identifiers_rel = relationship( "MaterialSampleAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: MaterialSampleAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"MaterialSample(id={self.id},name={self.name},description={self.description},Database_id={self.Database_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class OmicsProcessing(BiosampleProcessing):
    """
    The methods and processes used to generate omics data from a biosample or organism.
    """
    __tablename__ = 'OmicsProcessing'
    
    add_date = Column(Text())
    mod_date = Column(Text())
    instrument_name = Column(Text())
    ncbi_project_name = Column(Text())
    processing_institution = Column(Enum('UCSD', 'JGI', 'EMSL', name='processing_institution_enum'))
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    Database_id = Column(Text(), ForeignKey('Database.id'))
    omics_type_id = Column(Text(), ForeignKey('ControlledTermValue.id'))
    omics_type = relationship("ControlledTermValue", uselist=False)
    principal_investigator_id = Column(Text(), ForeignKey('PersonValue.id'))
    principal_investigator = relationship("PersonValue", uselist=False)
    samp_vol_we_dna_ext_id = Column(Text(), ForeignKey('QuantityValue.id'))
    samp_vol_we_dna_ext = relationship("QuantityValue", uselist=False)
    nucl_acid_ext_id = Column(Text(), ForeignKey('TextValue.id'))
    nucl_acid_ext = relationship("TextValue", uselist=False)
    nucl_acid_amp_id = Column(Text(), ForeignKey('TextValue.id'))
    nucl_acid_amp = relationship("TextValue", uselist=False)
    target_gene_id = Column(Text(), ForeignKey('TextValue.id'))
    target_gene = relationship("TextValue", uselist=False)
    target_subfragment_id = Column(Text(), ForeignKey('TextValue.id'))
    target_subfragment = relationship("TextValue", uselist=False)
    pcr_primers_id = Column(Text(), ForeignKey('TextValue.id'))
    pcr_primers = relationship("TextValue", uselist=False)
    pcr_cond_id = Column(Text(), ForeignKey('TextValue.id'))
    pcr_cond = relationship("TextValue", uselist=False)
    seq_meth_id = Column(Text(), ForeignKey('TextValue.id'))
    seq_meth = relationship("TextValue", uselist=False)
    seq_quality_check_id = Column(Text(), ForeignKey('TextValue.id'))
    seq_quality_check = relationship("TextValue", uselist=False)
    chimera_check_id = Column(Text(), ForeignKey('TextValue.id'))
    chimera_check = relationship("TextValue", uselist=False)
    
    
    # ManyToMany
    has_input = relationship( "Biosample", secondary="OmicsProcessing_has_input")
    
    
    # ManyToMany
    has_output = relationship( "NamedThing", secondary="OmicsProcessing_has_output")
    
    
    # ManyToMany
    part_of = relationship( "NamedThing", secondary="OmicsProcessing_part_of")
    
    
    gold_sequencing_project_identifiers_rel = relationship( "OmicsProcessingGoldSequencingProjectIdentifiers" )
    gold_sequencing_project_identifiers = association_proxy("gold_sequencing_project_identifiers_rel", "gold_sequencing_project_identifiers",
                                  creator=lambda x_: OmicsProcessingGoldSequencingProjectIdentifiers(gold_sequencing_project_identifiers=x_))
    
    
    insdc_experiment_identifiers_rel = relationship( "OmicsProcessingInsdcExperimentIdentifiers" )
    insdc_experiment_identifiers = association_proxy("insdc_experiment_identifiers_rel", "insdc_experiment_identifiers",
                                  creator=lambda x_: OmicsProcessingInsdcExperimentIdentifiers(insdc_experiment_identifiers=x_))
    
    
    alternative_identifiers_rel = relationship( "OmicsProcessingAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: OmicsProcessingAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"OmicsProcessing(add_date={self.add_date},mod_date={self.mod_date},instrument_name={self.instrument_name},ncbi_project_name={self.ncbi_project_name},processing_institution={self.processing_institution},type={self.type},id={self.id},name={self.name},description={self.description},Database_id={self.Database_id},omics_type_id={self.omics_type_id},principal_investigator_id={self.principal_investigator_id},samp_vol_we_dna_ext_id={self.samp_vol_we_dna_ext_id},nucl_acid_ext_id={self.nucl_acid_ext_id},nucl_acid_amp_id={self.nucl_acid_amp_id},target_gene_id={self.target_gene_id},target_subfragment_id={self.target_subfragment_id},pcr_primers_id={self.pcr_primers_id},pcr_cond_id={self.pcr_cond_id},seq_meth_id={self.seq_meth_id},seq_quality_check_id={self.seq_quality_check_id},chimera_check_id={self.chimera_check_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetagenomeAssembly(WorkflowExecutionActivity):
    """
    A workflow execution activity that converts sequencing reads into an assembled metagenome.
    """
    __tablename__ = 'MetagenomeAssembly'
    
    asm_score = Column(Float())
    scaffolds = Column(Float())
    scaf_logsum = Column(Float())
    scaf_powsum = Column(Float())
    scaf_max = Column(Float())
    scaf_bp = Column(Float())
    scaf_n50 = Column(Float())
    scaf_n90 = Column(Float())
    scaf_l50 = Column(Float())
    scaf_l90 = Column(Float())
    scaf_n_gt50k = Column(Float())
    scaf_l_gt50k = Column(Float())
    scaf_pct_gt50k = Column(Float())
    contigs = Column(Float())
    contig_bp = Column(Float())
    ctg_n50 = Column(Float())
    ctg_l50 = Column(Float())
    ctg_n90 = Column(Float())
    ctg_l90 = Column(Float())
    ctg_logsum = Column(Float())
    ctg_powsum = Column(Float())
    ctg_max = Column(Float())
    gap_pct = Column(Float())
    gc_std = Column(Float())
    gc_avg = Column(Float())
    num_input_reads = Column(Float())
    num_aligned_reads = Column(Float())
    insdc_assembly_identifiers = Column(Text())
    execution_resource = Column(Text())
    git_url = Column(Text())
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    started_at_time = Column(DateTime())
    ended_at_time = Column(DateTime())
    was_informed_by = Column(Text(), ForeignKey('Activity.id'))
    was_associated_with = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'))
    used = Column(Text())
    Database_id = Column(Text(), ForeignKey('Database.id'))
    
    
    # ManyToMany
    has_input = relationship( "NamedThing", secondary="MetagenomeAssembly_has_input")
    
    
    # ManyToMany
    has_output = relationship( "NamedThing", secondary="MetagenomeAssembly_has_output")
    
    
    # ManyToMany
    part_of = relationship( "NamedThing", secondary="MetagenomeAssembly_part_of")
    
    
    def __repr__(self):
        return f"MetagenomeAssembly(asm_score={self.asm_score},scaffolds={self.scaffolds},scaf_logsum={self.scaf_logsum},scaf_powsum={self.scaf_powsum},scaf_max={self.scaf_max},scaf_bp={self.scaf_bp},scaf_n50={self.scaf_n50},scaf_n90={self.scaf_n90},scaf_l50={self.scaf_l50},scaf_l90={self.scaf_l90},scaf_n_gt50k={self.scaf_n_gt50k},scaf_l_gt50k={self.scaf_l_gt50k},scaf_pct_gt50k={self.scaf_pct_gt50k},contigs={self.contigs},contig_bp={self.contig_bp},ctg_n50={self.ctg_n50},ctg_l50={self.ctg_l50},ctg_n90={self.ctg_n90},ctg_l90={self.ctg_l90},ctg_logsum={self.ctg_logsum},ctg_powsum={self.ctg_powsum},ctg_max={self.ctg_max},gap_pct={self.gap_pct},gc_std={self.gc_std},gc_avg={self.gc_avg},num_input_reads={self.num_input_reads},num_aligned_reads={self.num_aligned_reads},insdc_assembly_identifiers={self.insdc_assembly_identifiers},execution_resource={self.execution_resource},git_url={self.git_url},type={self.type},id={self.id},name={self.name},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},was_informed_by={self.was_informed_by},was_associated_with={self.was_associated_with},used={self.used},Database_id={self.Database_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetatranscriptomeAssembly(WorkflowExecutionActivity):
    """
    
    """
    __tablename__ = 'MetatranscriptomeAssembly'
    
    asm_score = Column(Float())
    scaffolds = Column(Float())
    scaf_logsum = Column(Float())
    scaf_powsum = Column(Float())
    scaf_max = Column(Float())
    scaf_bp = Column(Float())
    scaf_n50 = Column(Float())
    scaf_n90 = Column(Float())
    scaf_l50 = Column(Float())
    scaf_l90 = Column(Float())
    scaf_n_gt50k = Column(Float())
    scaf_l_gt50k = Column(Float())
    scaf_pct_gt50k = Column(Float())
    contigs = Column(Float())
    contig_bp = Column(Float())
    ctg_n50 = Column(Float())
    ctg_l50 = Column(Float())
    ctg_n90 = Column(Float())
    ctg_l90 = Column(Float())
    ctg_logsum = Column(Float())
    ctg_powsum = Column(Float())
    ctg_max = Column(Float())
    gap_pct = Column(Float())
    gc_std = Column(Float())
    gc_avg = Column(Float())
    num_input_reads = Column(Float())
    num_aligned_reads = Column(Float())
    insdc_assembly_identifiers = Column(Text())
    execution_resource = Column(Text())
    git_url = Column(Text())
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    started_at_time = Column(DateTime())
    ended_at_time = Column(DateTime())
    was_informed_by = Column(Text(), ForeignKey('Activity.id'))
    was_associated_with = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'))
    used = Column(Text())
    
    
    # ManyToMany
    has_input = relationship( "NamedThing", secondary="MetatranscriptomeAssembly_has_input")
    
    
    # ManyToMany
    has_output = relationship( "NamedThing", secondary="MetatranscriptomeAssembly_has_output")
    
    
    # ManyToMany
    part_of = relationship( "NamedThing", secondary="MetatranscriptomeAssembly_part_of")
    
    
    def __repr__(self):
        return f"MetatranscriptomeAssembly(asm_score={self.asm_score},scaffolds={self.scaffolds},scaf_logsum={self.scaf_logsum},scaf_powsum={self.scaf_powsum},scaf_max={self.scaf_max},scaf_bp={self.scaf_bp},scaf_n50={self.scaf_n50},scaf_n90={self.scaf_n90},scaf_l50={self.scaf_l50},scaf_l90={self.scaf_l90},scaf_n_gt50k={self.scaf_n_gt50k},scaf_l_gt50k={self.scaf_l_gt50k},scaf_pct_gt50k={self.scaf_pct_gt50k},contigs={self.contigs},contig_bp={self.contig_bp},ctg_n50={self.ctg_n50},ctg_l50={self.ctg_l50},ctg_n90={self.ctg_n90},ctg_l90={self.ctg_l90},ctg_logsum={self.ctg_logsum},ctg_powsum={self.ctg_powsum},ctg_max={self.ctg_max},gap_pct={self.gap_pct},gc_std={self.gc_std},gc_avg={self.gc_avg},num_input_reads={self.num_input_reads},num_aligned_reads={self.num_aligned_reads},insdc_assembly_identifiers={self.insdc_assembly_identifiers},execution_resource={self.execution_resource},git_url={self.git_url},type={self.type},id={self.id},name={self.name},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},was_informed_by={self.was_informed_by},was_associated_with={self.was_associated_with},used={self.used},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetagenomeAnnotationActivity(WorkflowExecutionActivity):
    """
    A workflow execution activity that provides functional and structural annotation of assembled metagenome contigs
    """
    __tablename__ = 'MetagenomeAnnotationActivity'
    
    execution_resource = Column(Text())
    git_url = Column(Text())
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    started_at_time = Column(DateTime())
    ended_at_time = Column(DateTime())
    was_informed_by = Column(Text(), ForeignKey('Activity.id'))
    was_associated_with = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'))
    used = Column(Text())
    Database_id = Column(Text(), ForeignKey('Database.id'))
    
    
    gold_analysis_project_identifiers_rel = relationship( "MetagenomeAnnotationActivityGoldAnalysisProjectIdentifiers" )
    gold_analysis_project_identifiers = association_proxy("gold_analysis_project_identifiers_rel", "gold_analysis_project_identifiers",
                                  creator=lambda x_: MetagenomeAnnotationActivityGoldAnalysisProjectIdentifiers(gold_analysis_project_identifiers=x_))
    
    
    # ManyToMany
    has_input = relationship( "NamedThing", secondary="MetagenomeAnnotationActivity_has_input")
    
    
    # ManyToMany
    has_output = relationship( "NamedThing", secondary="MetagenomeAnnotationActivity_has_output")
    
    
    # ManyToMany
    part_of = relationship( "NamedThing", secondary="MetagenomeAnnotationActivity_part_of")
    
    
    def __repr__(self):
        return f"MetagenomeAnnotationActivity(execution_resource={self.execution_resource},git_url={self.git_url},type={self.type},id={self.id},name={self.name},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},was_informed_by={self.was_informed_by},was_associated_with={self.was_associated_with},used={self.used},Database_id={self.Database_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetatranscriptomeAnnotationActivity(WorkflowExecutionActivity):
    """
    
    """
    __tablename__ = 'MetatranscriptomeAnnotationActivity'
    
    execution_resource = Column(Text())
    git_url = Column(Text())
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    started_at_time = Column(DateTime())
    ended_at_time = Column(DateTime())
    was_informed_by = Column(Text(), ForeignKey('Activity.id'))
    was_associated_with = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'))
    used = Column(Text())
    
    
    gold_analysis_project_identifiers_rel = relationship( "MetatranscriptomeAnnotationActivityGoldAnalysisProjectIdentifiers" )
    gold_analysis_project_identifiers = association_proxy("gold_analysis_project_identifiers_rel", "gold_analysis_project_identifiers",
                                  creator=lambda x_: MetatranscriptomeAnnotationActivityGoldAnalysisProjectIdentifiers(gold_analysis_project_identifiers=x_))
    
    
    # ManyToMany
    has_input = relationship( "NamedThing", secondary="MetatranscriptomeAnnotationActivity_has_input")
    
    
    # ManyToMany
    has_output = relationship( "NamedThing", secondary="MetatranscriptomeAnnotationActivity_has_output")
    
    
    # ManyToMany
    part_of = relationship( "NamedThing", secondary="MetatranscriptomeAnnotationActivity_part_of")
    
    
    def __repr__(self):
        return f"MetatranscriptomeAnnotationActivity(execution_resource={self.execution_resource},git_url={self.git_url},type={self.type},id={self.id},name={self.name},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},was_informed_by={self.was_informed_by},was_associated_with={self.was_associated_with},used={self.used},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetatranscriptomeActivity(WorkflowExecutionActivity):
    """
    A metatranscriptome activity that e.g. pools assembly and annotation activity.
    """
    __tablename__ = 'MetatranscriptomeActivity'
    
    execution_resource = Column(Text())
    git_url = Column(Text())
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    started_at_time = Column(DateTime())
    ended_at_time = Column(DateTime())
    was_informed_by = Column(Text(), ForeignKey('Activity.id'))
    was_associated_with = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'))
    used = Column(Text())
    Database_id = Column(Text(), ForeignKey('Database.id'))
    
    
    # ManyToMany
    has_input = relationship( "NamedThing", secondary="MetatranscriptomeActivity_has_input")
    
    
    # ManyToMany
    has_output = relationship( "NamedThing", secondary="MetatranscriptomeActivity_has_output")
    
    
    # ManyToMany
    part_of = relationship( "NamedThing", secondary="MetatranscriptomeActivity_part_of")
    
    
    def __repr__(self):
        return f"MetatranscriptomeActivity(execution_resource={self.execution_resource},git_url={self.git_url},type={self.type},id={self.id},name={self.name},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},was_informed_by={self.was_informed_by},was_associated_with={self.was_associated_with},used={self.used},Database_id={self.Database_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MagsAnalysisActivity(WorkflowExecutionActivity):
    """
    A workflow execution activity that uses computational binning tools to group assembled contigs into genomes
    """
    __tablename__ = 'MagsAnalysisActivity'
    
    input_contig_num = Column(Integer())
    binned_contig_num = Column(Integer())
    too_short_contig_num = Column(Integer())
    low_depth_contig_num = Column(Integer())
    unbinned_contig_num = Column(Integer())
    execution_resource = Column(Text())
    git_url = Column(Text())
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    started_at_time = Column(DateTime())
    ended_at_time = Column(DateTime())
    was_informed_by = Column(Text(), ForeignKey('Activity.id'))
    was_associated_with = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'))
    used = Column(Text())
    Database_id = Column(Text(), ForeignKey('Database.id'))
    
    
    # ManyToMany
    mags_list = relationship( "MagBin", secondary="MagsAnalysisActivity_mags_list")
    
    
    # ManyToMany
    has_input = relationship( "NamedThing", secondary="MagsAnalysisActivity_has_input")
    
    
    # ManyToMany
    has_output = relationship( "NamedThing", secondary="MagsAnalysisActivity_has_output")
    
    
    # ManyToMany
    part_of = relationship( "NamedThing", secondary="MagsAnalysisActivity_part_of")
    
    
    def __repr__(self):
        return f"MagsAnalysisActivity(input_contig_num={self.input_contig_num},binned_contig_num={self.binned_contig_num},too_short_contig_num={self.too_short_contig_num},low_depth_contig_num={self.low_depth_contig_num},unbinned_contig_num={self.unbinned_contig_num},execution_resource={self.execution_resource},git_url={self.git_url},type={self.type},id={self.id},name={self.name},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},was_informed_by={self.was_informed_by},was_associated_with={self.was_associated_with},used={self.used},Database_id={self.Database_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ReadQcAnalysisActivity(WorkflowExecutionActivity):
    """
    A workflow execution activity that performs quality control on raw Illumina reads including quality trimming, artifact removal, linker trimming, adapter trimming, spike-in removal, and human/cat/dog/mouse/microbe contaminant removal
    """
    __tablename__ = 'ReadQcAnalysisActivity'
    
    input_read_count = Column(Float())
    input_base_count = Column(Float())
    output_read_count = Column(Float())
    output_base_count = Column(Float())
    execution_resource = Column(Text())
    git_url = Column(Text())
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    started_at_time = Column(DateTime())
    ended_at_time = Column(DateTime())
    was_informed_by = Column(Text(), ForeignKey('Activity.id'))
    was_associated_with = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'))
    used = Column(Text())
    Database_id = Column(Text(), ForeignKey('Database.id'))
    
    
    # ManyToMany
    has_input = relationship( "NamedThing", secondary="ReadQcAnalysisActivity_has_input")
    
    
    # ManyToMany
    has_output = relationship( "NamedThing", secondary="ReadQcAnalysisActivity_has_output")
    
    
    # ManyToMany
    part_of = relationship( "NamedThing", secondary="ReadQcAnalysisActivity_part_of")
    
    
    def __repr__(self):
        return f"ReadQcAnalysisActivity(input_read_count={self.input_read_count},input_base_count={self.input_base_count},output_read_count={self.output_read_count},output_base_count={self.output_base_count},execution_resource={self.execution_resource},git_url={self.git_url},type={self.type},id={self.id},name={self.name},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},was_informed_by={self.was_informed_by},was_associated_with={self.was_associated_with},used={self.used},Database_id={self.Database_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ReadBasedTaxonomyAnalysisActivity(WorkflowExecutionActivity):
    """
    A workflow execution activity that performs taxonomy classification using sequencing reads
    """
    __tablename__ = 'ReadBasedTaxonomyAnalysisActivity'
    
    execution_resource = Column(Text())
    git_url = Column(Text())
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    started_at_time = Column(DateTime())
    ended_at_time = Column(DateTime())
    was_informed_by = Column(Text(), ForeignKey('Activity.id'))
    was_associated_with = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'))
    used = Column(Text())
    Database_id = Column(Text(), ForeignKey('Database.id'))
    
    
    # ManyToMany
    has_input = relationship( "NamedThing", secondary="ReadBasedTaxonomyAnalysisActivity_has_input")
    
    
    # ManyToMany
    has_output = relationship( "NamedThing", secondary="ReadBasedTaxonomyAnalysisActivity_has_output")
    
    
    # ManyToMany
    part_of = relationship( "NamedThing", secondary="ReadBasedTaxonomyAnalysisActivity_part_of")
    
    
    def __repr__(self):
        return f"ReadBasedTaxonomyAnalysisActivity(execution_resource={self.execution_resource},git_url={self.git_url},type={self.type},id={self.id},name={self.name},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},was_informed_by={self.was_informed_by},was_associated_with={self.was_associated_with},used={self.used},Database_id={self.Database_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetabolomicsAnalysisActivity(WorkflowExecutionActivity):
    """
    
    """
    __tablename__ = 'MetabolomicsAnalysisActivity'
    
    execution_resource = Column(Text())
    git_url = Column(Text())
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    started_at_time = Column(DateTime())
    ended_at_time = Column(DateTime())
    was_informed_by = Column(Text(), ForeignKey('Activity.id'))
    was_associated_with = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'))
    used = Column(Text(), ForeignKey('Instrument.id'))
    Database_id = Column(Text(), ForeignKey('Database.id'))
    
    
    # ManyToMany
    has_input = relationship( "NamedThing", secondary="MetabolomicsAnalysisActivity_has_input")
    
    
    # ManyToMany
    has_output = relationship( "NamedThing", secondary="MetabolomicsAnalysisActivity_has_output")
    
    
    # ManyToMany
    part_of = relationship( "NamedThing", secondary="MetabolomicsAnalysisActivity_part_of")
    
    
    def __repr__(self):
        return f"MetabolomicsAnalysisActivity(execution_resource={self.execution_resource},git_url={self.git_url},type={self.type},id={self.id},name={self.name},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},was_informed_by={self.was_informed_by},was_associated_with={self.was_associated_with},used={self.used},Database_id={self.Database_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetaproteomicsAnalysisActivity(WorkflowExecutionActivity):
    """
    
    """
    __tablename__ = 'MetaproteomicsAnalysisActivity'
    
    execution_resource = Column(Text())
    git_url = Column(Text())
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    started_at_time = Column(DateTime())
    ended_at_time = Column(DateTime())
    was_informed_by = Column(Text(), ForeignKey('Activity.id'))
    was_associated_with = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'))
    used = Column(Text(), ForeignKey('Instrument.id'))
    Database_id = Column(Text(), ForeignKey('Database.id'))
    
    
    # ManyToMany
    has_input = relationship( "NamedThing", secondary="MetaproteomicsAnalysisActivity_has_input")
    
    
    # ManyToMany
    has_output = relationship( "NamedThing", secondary="MetaproteomicsAnalysisActivity_has_output")
    
    
    # ManyToMany
    part_of = relationship( "NamedThing", secondary="MetaproteomicsAnalysisActivity_part_of")
    
    
    def __repr__(self):
        return f"MetaproteomicsAnalysisActivity(execution_resource={self.execution_resource},git_url={self.git_url},type={self.type},id={self.id},name={self.name},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},was_informed_by={self.was_informed_by},was_associated_with={self.was_associated_with},used={self.used},Database_id={self.Database_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class NomAnalysisActivity(WorkflowExecutionActivity):
    """
    
    """
    __tablename__ = 'NomAnalysisActivity'
    
    execution_resource = Column(Text())
    git_url = Column(Text())
    type = Column(Text())
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    started_at_time = Column(DateTime())
    ended_at_time = Column(DateTime())
    was_informed_by = Column(Text(), ForeignKey('Activity.id'))
    was_associated_with = Column(Text(), ForeignKey('WorkflowExecutionActivity.id'))
    used = Column(Text(), ForeignKey('Instrument.id'))
    Database_id = Column(Text(), ForeignKey('Database.id'))
    
    
    # ManyToMany
    has_input = relationship( "NamedThing", secondary="NomAnalysisActivity_has_input")
    
    
    # ManyToMany
    has_output = relationship( "NamedThing", secondary="NomAnalysisActivity_has_output")
    
    
    # ManyToMany
    part_of = relationship( "NamedThing", secondary="NomAnalysisActivity_part_of")
    
    
    def __repr__(self):
        return f"NomAnalysisActivity(execution_resource={self.execution_resource},git_url={self.git_url},type={self.type},id={self.id},name={self.name},started_at_time={self.started_at_time},ended_at_time={self.ended_at_time},was_informed_by={self.was_informed_by},was_associated_with={self.was_associated_with},used={self.used},Database_id={self.Database_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class EnvironmentalMaterialTerm(OntologyClass):
    """
    
    """
    __tablename__ = 'EnvironmentalMaterialTerm'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    
    
    alternative_identifiers_rel = relationship( "EnvironmentalMaterialTermAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: EnvironmentalMaterialTermAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"EnvironmentalMaterialTerm(id={self.id},name={self.name},description={self.description},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ChemicalEntity(OntologyClass):
    """
    An atom or molecule that can be represented with a chemical formula. Include lipids, glycans, natural products, drugs. There may be different terms for distinct acid-base forms, protonation states
    """
    __tablename__ = 'ChemicalEntity'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    
    
    alternative_identifiers_rel = relationship( "ChemicalEntityAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: ChemicalEntityAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"ChemicalEntity(id={self.id},name={self.name},description={self.description},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class FunctionalAnnotationTerm(OntologyClass):
    """
    Abstract grouping class for any term/descriptor that can be applied to a functional unit of a genome (protein, ncRNA, complex).
    """
    __tablename__ = 'FunctionalAnnotationTerm'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    
    
    alternative_identifiers_rel = relationship( "FunctionalAnnotationTermAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: FunctionalAnnotationTermAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"FunctionalAnnotationTerm(id={self.id},name={self.name},description={self.description},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Pathway(FunctionalAnnotationTerm):
    """
    A pathway is a sequence of steps/reactions carried out by an organism or community of organisms
    """
    __tablename__ = 'Pathway'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    
    
    alternative_identifiers_rel = relationship( "PathwayAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: PathwayAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"Pathway(id={self.id},name={self.name},description={self.description},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Reaction(FunctionalAnnotationTerm):
    """
    An individual biochemical transformation carried out by a functional unit of an organism, in which a collection of substrates are transformed into a collection of products. Can also represent transporters
    """
    __tablename__ = 'Reaction'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    
    
    alternative_identifiers_rel = relationship( "ReactionAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: ReactionAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"Reaction(id={self.id},name={self.name},description={self.description},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class OrthologyGroup(FunctionalAnnotationTerm):
    """
    A set of genes or gene products in which all members are orthologous
    """
    __tablename__ = 'OrthologyGroup'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    description = Column(Text())
    
    
    alternative_identifiers_rel = relationship( "OrthologyGroupAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: OrthologyGroupAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"OrthologyGroup(id={self.id},name={self.name},description={self.description},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


