
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class MetaProteomicsAnalysisActivity(Base):
    """
    Schema for MetaProteomicsAnalysisActivity table
    """
    __tablename__ = 'MetaProteomicsAnalysisActivity'
    
    id = Column(Integer(), primary_key=True)
    execution_resource = Column(Text())
    git_url = Column(Text())
    name = Column(Text())
    started_at_time = Column(DateTime())
    type = Column(Text())
    used = Column(Text())
    ended_at_time = Column(DateTime())
    was_associated_with = Column(Text())
    was_informed_by = Column(Text())
    has_peptide_quantifications_id = Column(Integer())
    
    
    has_input_rel = relationship( "MetaProteomicsAnalysisActivityHasInput" )
    has_input = association_proxy("has_input_rel", "has_input",
                                  creator=lambda x_: MetaProteomicsAnalysisActivityHasInput(has_input=x_))
    
    
    has_output_rel = relationship( "MetaProteomicsAnalysisActivityHasOutput" )
    has_output = association_proxy("has_output_rel", "has_output",
                                  creator=lambda x_: MetaProteomicsAnalysisActivityHasOutput(has_output=x_))
    
    
    part_of_rel = relationship( "MetaProteomicsAnalysisActivityPartOf" )
    part_of = association_proxy("part_of_rel", "part_of",
                                  creator=lambda x_: MetaProteomicsAnalysisActivityPartOf(part_of=x_))
    
    
    def __repr__(self):
        return f"MetaProteomicsAnalysisActivity(id={self.id},execution_resource={self.execution_resource},git_url={self.git_url},name={self.name},started_at_time={self.started_at_time},type={self.type},used={self.used},ended_at_time={self.ended_at_time},was_associated_with={self.was_associated_with},was_informed_by={self.was_informed_by},has_peptide_quantifications_id={self.has_peptide_quantifications_id},)"
        
    
        
    


class AlembicVersion(Base):
    """
    AlembicVersion schema
    """
    __tablename__ = 'AlembicVersion'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    version_num = Column(Text())
    
    
    def __repr__(self):
        return f"AlembicVersion(id={self.id},version_num={self.version_num},)"
        
    
        
    


class FileTypeEnum(Base):
    """
    FileTypeEnum schema
    """
    __tablename__ = 'FileTypeEnum'
    
    id = Column(Integer(), primary_key=True)
    file_type_enum = Column(Enum('FT ICR-MS Analysis Results', 'GC-MS Metabolomics Results', 'Metaproteomics Workflow Statistics', 'Protein Report', 'Peptide Report', 'Unfiltered Metaproteomics Results', 'Read Count and RPKM', 'QC non-rRNA R2', 'QC non-rRNA R1', 'Metagenome Bins', 'CheckM Statistics', 'GOTTCHA2 Krona Plot', 'Kraken2 Krona Plot', 'Centrifuge Krona Plot', 'Kraken2 Classification Report', 'Kraken2 Taxonomic Classification', 'Centrifuge Classification Report', 'Centrifuge Taxonomic Classification', 'Structural Annotation GFF', 'Functional Annotation GFF', 'Annotation Amino Acid FASTA', 'Annotation Enzyme Commission', 'Annotation KEGG Orthology', 'Assembly Coverage BAM', 'Assembly AGP', 'Assembly Scaffolds', 'Assembly Contigs', 'Assembly Coverage Stats', 'Filtered Sequencing Reads', 'QC Statistics', 'TIGRFam Annotation GFF', 'Clusters of Orthologous Groups (COG) Annotation GFF', 'CATH FunFams (Functional Families) Annotation GFF', 'SUPERFam Annotation GFF', 'SMART Annotation GFF', 'Pfam Annotation GFF', 'Direct Infusion FT ICR-MS Raw Data', name='FileType'))
    
    
    def __repr__(self):
        return f"FileTypeEnum(id={self.id},file_type_enum={self.file_type_enum},)"
        
    
        
    


class MagBin(Base):
    """
    MagBin schema
    """
    __tablename__ = 'MagBin'
    
    id = Column(Integer(), primary_key=True)
    bin_name = Column(Text())
    bin_quality = Column(Text())
    completeness = Column(Float())
    contamination = Column(Float())
    gene_count = Column(Integer())
    gtdbtk_class = Column(Text())
    gtdbtk_domain = Column(Text())
    gtdbtk_family = Column(Text())
    gtdbtk_genus = Column(Text())
    gtdbtk_order = Column(Text())
    gtdbtk_phylum = Column(Text())
    gtdbtk_species = Column(Text())
    num_16s = Column(Integer())
    num_32s = Column(Integer())
    num_5s = Column(Integer())
    num_tRNA = Column(Integer())
    number_of_contig = Column(Integer())
    type = Column(Text())
    
    
    def __repr__(self):
        return f"MagBin(id={self.id},bin_name={self.bin_name},bin_quality={self.bin_quality},completeness={self.completeness},contamination={self.contamination},gene_count={self.gene_count},gtdbtk_class={self.gtdbtk_class},gtdbtk_domain={self.gtdbtk_domain},gtdbtk_family={self.gtdbtk_family},gtdbtk_genus={self.gtdbtk_genus},gtdbtk_order={self.gtdbtk_order},gtdbtk_phylum={self.gtdbtk_phylum},gtdbtk_species={self.gtdbtk_species},num_16s={self.num_16s},num_32s={self.num_32s},num_5s={self.num_5s},num_tRNA={self.num_tRNA},number_of_contig={self.number_of_contig},type={self.type},)"
        
    
        
    


class MetaboliteQuantification(Base):
    """
    MetaboliteQuantification Schema
    """
    __tablename__ = 'MetaboliteQuantification'
    
    id = Column(Integer(), primary_key=True)
    description = Column(Text())
    highest_similarity_score = Column(Integer())
    metabolite_quantified = Column(Text())
    
    
    alternative_identifiers_rel = relationship( "MetaboliteQuantificationAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: MetaboliteQuantificationAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"MetaboliteQuantification(id={self.id},description={self.description},highest_similarity_score={self.highest_similarity_score},metabolite_quantified={self.metabolite_quantified},)"
        
    
        
    


class Model(Base):
    """
    model schema
    """
    __tablename__ = 'model'
    
    id = Column(Integer(), primary_key=True)
    username = Column(Text())
    email = Column(Text())
    telephone_no = Column(Text())
    password_hash = Column(Text())
    
    
    def __repr__(self):
        return f"model(id={self.id},username={self.username},email={self.email},telephone_no={self.telephone_no},password_hash={self.password_hash},)"
        
    
        
    


class MolecularData(Base):
    """
    MolecularData schema
    """
    __tablename__ = 'MolecularData'
    
    id = Column(Integer(), primary_key=True)
    inchikey = Column(Text())
    name = Column(Text())
    formula = Column(Text())
    casno = Column(Text())
    inchi = Column(Text())
    chebi = Column(Text())
    smiles = Column(Text())
    kegg = Column(Text())
    iupac_name = Column(Text())
    traditional_name = Column(Text())
    common_name = Column(Text())
    match_nme = Column(Text())
    
    
    def __repr__(self):
        return f"MolecularData(id={self.id},inchikey={self.inchikey},name={self.name},formula={self.formula},casno={self.casno},inchi={self.inchi},chebi={self.chebi},smiles={self.smiles},kegg={self.kegg},iupac_name={self.iupac_name},traditional_name={self.traditional_name},common_name={self.common_name},match_nme={self.match_nme},)"
        
    
        
    


class NomAnalysisActivity(Base):
    """
    NomAnalysisActivity Schema
    """
    __tablename__ = 'NomAnalysisActivity'
    
    id = Column(Integer(), primary_key=True)
    ended_at_time = Column(DateTime())
    execution_resource = Column(Text())
    git_url = Column(Text())
    name = Column(Text())
    started_at_time = Column(DateTime())
    type = Column(Text())
    used = Column(Text())
    was_associated_with = Column(Text())
    was_informed_by = Column(Text())
    has_calibration = Column(Text())
    
    
    has_input_rel = relationship( "NomAnalysisActivityHasInput" )
    has_input = association_proxy("has_input_rel", "has_input",
                                  creator=lambda x_: NomAnalysisActivityHasInput(has_input=x_))
    
    
    has_output_rel = relationship( "NomAnalysisActivityHasOutput" )
    has_output = association_proxy("has_output_rel", "has_output",
                                  creator=lambda x_: NomAnalysisActivityHasOutput(has_output=x_))
    
    
    part_of_rel = relationship( "NomAnalysisActivityPartOf" )
    part_of = association_proxy("part_of_rel", "part_of",
                                  creator=lambda x_: NomAnalysisActivityPartOf(part_of=x_))
    
    
    def __repr__(self):
        return f"NomAnalysisActivity(id={self.id},ended_at_time={self.ended_at_time},execution_resource={self.execution_resource},git_url={self.git_url},name={self.name},started_at_time={self.started_at_time},type={self.type},used={self.used},was_associated_with={self.was_associated_with},was_informed_by={self.was_informed_by},has_calibration={self.has_calibration},)"
        
    
        
    


class OntologyClass(Base):
    """
    OntologyClass schema
    """
    __tablename__ = 'OntologyClass'
    
    id = Column(Integer(), primary_key=True)
    description = Column(Text())
    name = Column(Text())
    
    
    alternative_identifiers_rel = relationship( "OntologyClassAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: OntologyClassAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"OntologyClass(id={self.id},description={self.description},name={self.name},)"
        
    
        
    


class PeptideQuantification(Base):
    """
    PeptideQuantification Schema
    """
    __tablename__ = 'PeptideQuantification'
    
    id = Column(Integer(), primary_key=True)
    description = Column(Text())
    best_protein = Column(Text())
    min_q_value = Column(Float())
    peptide_sequence = Column(Text())
    peptide_spectral_count = Column(Integer())
    peptide_sum_masic_abundance = Column(Float())
    
    
    all_proteins_rel = relationship( "PeptideQuantificationAllProteins" )
    all_proteins = association_proxy("all_proteins_rel", "all_proteins",
                                  creator=lambda x_: PeptideQuantificationAllProteins(all_proteins=x_))
    
    
    def __repr__(self):
        return f"PeptideQuantification(id={self.id},description={self.description},best_protein={self.best_protein},min_q_value={self.min_q_value},peptide_sequence={self.peptide_sequence},peptide_spectral_count={self.peptide_spectral_count},peptide_sum_masic_abundance={self.peptide_sum_masic_abundance},)"
        
    
        
    


class WorkFlowExecutionActivity(Base):
    """
    WRITE DESCRIPTION
    """
    __tablename__ = 'WorkFlowExecutionActivity'
    
    id = Column(Integer(), primary_key=True)
    description = Column(Text())
    ended_at_time = Column(DateTime())
    execution_resource = Column(Text())
    git_url = Column(Text())
    name = Column(Text())
    started_at_time = Column(DateTime())
    type = Column(Text())
    used = Column(Text())
    was_associated_with = Column(Text())
    was_informed_by = Column(Text())
    
    
    has_input_rel = relationship( "WorkFlowExecutionActivityHasInput" )
    has_input = association_proxy("has_input_rel", "has_input",
                                  creator=lambda x_: WorkFlowExecutionActivityHasInput(has_input=x_))
    
    
    has_output_rel = relationship( "WorkFlowExecutionActivityHasOutput" )
    has_output = association_proxy("has_output_rel", "has_output",
                                  creator=lambda x_: WorkFlowExecutionActivityHasOutput(has_output=x_))
    
    
    part_of_rel = relationship( "WorkFlowExecutionActivityPartOf" )
    part_of = association_proxy("part_of_rel", "part_of",
                                  creator=lambda x_: WorkFlowExecutionActivityPartOf(part_of=x_))
    
    
    def __repr__(self):
        return f"WorkFlowExecutionActivity(id={self.id},description={self.description},ended_at_time={self.ended_at_time},execution_resource={self.execution_resource},git_url={self.git_url},name={self.name},started_at_time={self.started_at_time},type={self.type},used={self.used},was_associated_with={self.was_associated_with},was_informed_by={self.was_informed_by},)"
        
    
        
    


class MetabolomicsAnalysisActivity(Base):
    """
    MetabolomicsAnalysisActivity schema
    """
    __tablename__ = 'metabolomicsAnalysisActivity'
    
    id = Column(Integer(), primary_key=True)
    execution_resource = Column(Text())
    git_url = Column(Text())
    name = Column(Text())
    started_at_time = Column(DateTime())
    type = Column(Text())
    used = Column(Text())
    ended_at_time = Column(DateTime())
    was_associated_with = Column(Text())
    was_informed_by = Column(Text())
    has_calibration = Column(Text())
    has_metabolite_quantifications_id = Column(Integer())
    
    
    has_input_rel = relationship( "MetabolomicsAnalysisActivityHasInput" )
    has_input = association_proxy("has_input_rel", "has_input",
                                  creator=lambda x_: MetabolomicsAnalysisActivityHasInput(has_input=x_))
    
    
    has_output_rel = relationship( "MetabolomicsAnalysisActivityHasOutput" )
    has_output = association_proxy("has_output_rel", "has_output",
                                  creator=lambda x_: MetabolomicsAnalysisActivityHasOutput(has_output=x_))
    
    
    part_of_rel = relationship( "MetabolomicsAnalysisActivityPartOf" )
    part_of = association_proxy("part_of_rel", "part_of",
                                  creator=lambda x_: MetabolomicsAnalysisActivityPartOf(part_of=x_))
    
    
    def __repr__(self):
        return f"metabolomicsAnalysisActivity(id={self.id},execution_resource={self.execution_resource},git_url={self.git_url},name={self.name},started_at_time={self.started_at_time},type={self.type},used={self.used},ended_at_time={self.ended_at_time},was_associated_with={self.was_associated_with},was_informed_by={self.was_informed_by},has_calibration={self.has_calibration},has_metabolite_quantifications_id={self.has_metabolite_quantifications_id},)"
        
    
        
    


class MagsAnalysisActivity(Base):
    """
    magsAnalysisActivity schema
    """
    __tablename__ = 'magsAnalysisActivity'
    
    id = Column(Integer(), primary_key=True)
    execution_resource = Column(Text())
    git_url = Column(Text())
    name = Column(Text())
    started_at_time = Column(DateTime())
    type = Column(Text())
    used = Column(Text())
    ended_at_time = Column(DateTime())
    was_associated_with = Column(Text())
    was_informed_by = Column(Text())
    binned_contig_num = Column(Integer())
    input_contig_num = Column(Integer())
    lowDepth_contig_num = Column(Integer())
    too_short_contig_num = Column(Integer())
    unbinned_contig_num = Column(Integer())
    mags_list_id = Column(Integer())
    
    
    has_input_rel = relationship( "MagsAnalysisActivityHasInput" )
    has_input = association_proxy("has_input_rel", "has_input",
                                  creator=lambda x_: MagsAnalysisActivityHasInput(has_input=x_))
    
    
    has_output_rel = relationship( "MagsAnalysisActivityHasOutput" )
    has_output = association_proxy("has_output_rel", "has_output",
                                  creator=lambda x_: MagsAnalysisActivityHasOutput(has_output=x_))
    
    
    part_of_rel = relationship( "MagsAnalysisActivityPartOf" )
    part_of = association_proxy("part_of_rel", "part_of",
                                  creator=lambda x_: MagsAnalysisActivityPartOf(part_of=x_))
    
    
    def __repr__(self):
        return f"magsAnalysisActivity(id={self.id},execution_resource={self.execution_resource},git_url={self.git_url},name={self.name},started_at_time={self.started_at_time},type={self.type},used={self.used},ended_at_time={self.ended_at_time},was_associated_with={self.was_associated_with},was_informed_by={self.was_informed_by},binned_contig_num={self.binned_contig_num},input_contig_num={self.input_contig_num},lowDepth_contig_num={self.lowDepth_contig_num},too_short_contig_num={self.too_short_contig_num},unbinned_contig_num={self.unbinned_contig_num},mags_list_id={self.mags_list_id},)"
        
    
        
    


class DataObject(Base):
    """
    dataObject schema
    """
    __tablename__ = 'dataObject'
    
    id = Column(Integer(), primary_key=True)
    description = Column(Text())
    compression_type = Column(Text())
    file_size_bytes = Column(Integer())
    md5_checksum = Column(Text())
    name = Column(Text())
    type = Column(Text())
    url = Column(Text())
    was_generated_by = Column(Text())
    data_object_type_id = Column(Integer())
    
    
    alternative_identifiers_rel = relationship( "DataObjectAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: DataObjectAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    def __repr__(self):
        return f"dataObject(id={self.id},description={self.description},compression_type={self.compression_type},file_size_bytes={self.file_size_bytes},md5_checksum={self.md5_checksum},name={self.name},type={self.type},url={self.url},was_generated_by={self.was_generated_by},data_object_type_id={self.data_object_type_id},)"
        
    
        
    


class MassSpectrumObject(Base):
    """
    MassSpectrumObject schema
    """
    __tablename__ = 'massSpectrumObject'
    
    id = Column(Integer(), primary_key=True)
    type = Column(Text())
    source = Column(Text())
    version = Column(Text())
    collision_energy = Column(Text())
    precursor_ion = Column(Float())
    peak_count = Column(Integer())
    rt = Column(Float())
    mz = Column(Text())
    abundance = Column(Text())
    polarity = Column(Text())
    molecular_data_id = Column(Integer())
    
    
    def __repr__(self):
        return f"massSpectrumObject(id={self.id},type={self.type},source={self.source},version={self.version},collision_energy={self.collision_energy},precursor_ion={self.precursor_ion},peak_count={self.peak_count},rt={self.rt},mz={self.mz},abundance={self.abundance},polarity={self.polarity},molecular_data_id={self.molecular_data_id},)"
        
    
        
    


class DetectionActivity(Base):
    """
    detectionActivity schema
    """
    __tablename__ = 'detectionActivity'
    
    id = Column(Integer(), primary_key=True)
    type = Column(Text())
    analyzer = Column(Text())
    acquisition = Column(Text())
    ioniztion = Column(Text())
    rawdata_url = Column(Text())
    spectrum_id = Column(Integer())
    
    
    def __repr__(self):
        return f"detectionActivity(id={self.id},type={self.type},analyzer={self.analyzer},acquisition={self.acquisition},ioniztion={self.ioniztion},rawdata_url={self.rawdata_url},spectrum_id={self.spectrum_id},)"
        
    
        
    


class QuantityValue(Base):
    """
    QuantityValue schema
    """
    __tablename__ = 'quantityValue'
    
    id = Column(Integer(), primary_key=True)
    description = Column(Text())
    has_numeric_value = Column(Float())
    has_minimum_numeric_value = Column(Float())
    has_maximum_numeric_value = Column(Float())
    has_raw_value = Column(Text())
    type = Column(Text())
    has_unit = Column(Text())
    was_generated_by = Column(Text())
    
    
    def __repr__(self):
        return f"quantityValue(id={self.id},description={self.description},has_numeric_value={self.has_numeric_value},has_minimum_numeric_value={self.has_minimum_numeric_value},has_maximum_numeric_value={self.has_maximum_numeric_value},has_raw_value={self.has_raw_value},type={self.type},has_unit={self.has_unit},was_generated_by={self.was_generated_by},)"
        
    
        
    


class SeparationActivity(Base):
    """
    separationActivity schema
    """
    __tablename__ = 'separationActivity'
    
    id = Column(Integer(), primary_key=True)
    type = Column(Text())
    column = Column(Text())
    mobile_phase = Column(Text())
    gradient = Column(Text())
    flow_rate = Column(Text())
    instrument_name = Column(Text())
    column_temp = Column(Integer())
    sample_chamber_temp = Column(Integer())
    detection_id = Column(Integer())
    
    
    def __repr__(self):
        return f"separationActivity(id={self.id},type={self.type},column={self.column},mobile_phase={self.mobile_phase},gradient={self.gradient},flow_rate={self.flow_rate},instrument_name={self.instrument_name},column_temp={self.column_temp},sample_chamber_temp={self.sample_chamber_temp},detection_id={self.detection_id},)"
        
    
        
    


class LabDevice(Base):
    """
    labDevice schema
    """
    __tablename__ = 'labDevice'
    
    id = Column(Integer(), primary_key=True)
    description = Column(Text())
    device_type = Column(Enum('orbital_shaker', 'thermomixer', name='devicetypeenum'))
    activity_time_id = Column(Integer())
    activity_speed_id = Column(Integer())
    
    
    def __repr__(self):
        return f"labDevice(id={self.id},description={self.description},device_type={self.device_type},activity_time_id={self.activity_time_id},activity_speed_id={self.activity_speed_id},)"
        
    
        
    


class ContainerType(Base):
    """
    containerType schema
    """
    __tablename__ = 'containerType'
    
    id = Column(Integer(), primary_key=True)
    description = Column(Text())
    was_generated_by = Column(Text())
    container_size_id = Column(Integer())
    container_type = Column(Enum('screw_top_conical', name='containertypeenum'))
    
    
    def __repr__(self):
        return f"containerType(id={self.id},description={self.description},was_generated_by={self.was_generated_by},container_size_id={self.container_size_id},container_type={self.container_type},)"
        
    
        
    


class PersonValue(Base):
    """
    personValue schema
    """
    __tablename__ = 'personValue'
    
    id = Column(Integer(), primary_key=True)
    email = Column(Text())
    description = Column(Text())
    has_raw_value = Column(Text())
    name = Column(Text())
    orcid = Column(Text())
    profile_image_url = Column(Text())
    type = Column(Text())
    was_generated_by = Column(Text())
    
    
    websites_rel = relationship( "PersonValueWebsites" )
    websites = association_proxy("websites_rel", "websites",
                                  creator=lambda x_: PersonValueWebsites(websites=x_))
    
    
    def __repr__(self):
        return f"personValue(id={self.id},email={self.email},description={self.description},has_raw_value={self.has_raw_value},name={self.name},orcid={self.orcid},profile_image_url={self.profile_image_url},type={self.type},was_generated_by={self.was_generated_by},)"
        
    
        
    


class TextValue(Base):
    """
    textValue schema
    """
    __tablename__ = 'textValue'
    
    id = Column(Integer(), primary_key=True)
    description = Column(Text())
    language = Column(Text())
    has_raw_value = Column(Text())
    type = Column(Text())
    was_generated_by = Column(Text())
    
    
    def __repr__(self):
        return f"textValue(id={self.id},description={self.description},language={self.language},has_raw_value={self.has_raw_value},type={self.type},was_generated_by={self.was_generated_by},)"
        
    
        
    


class TimestampValue(Base):
    """
    timestampValue schema
    """
    __tablename__ = 'timestampValue'
    
    id = Column(Integer(), primary_key=True)
    description = Column(Text())
    has_raw_value = Column(Text())
    type = Column(Text())
    was_generated_by = Column(Text())
    
    
    def __repr__(self):
        return f"timestampValue(id={self.id},description={self.description},has_raw_value={self.has_raw_value},type={self.type},was_generated_by={self.was_generated_by},)"
        
    
        
    


class ControlledTermValue(Base):
    """
    ControlledTermValue schema
    """
    __tablename__ = 'controlledTermValue'
    
    id = Column(Integer(), primary_key=True)
    description = Column(Text())
    has_raw_value = Column(Text())
    was_generated_by = Column(Text())
    type = Column(Text())
    
    
    def __repr__(self):
        return f"controlledTermValue(id={self.id},description={self.description},has_raw_value={self.has_raw_value},was_generated_by={self.was_generated_by},type={self.type},)"
        
    
        
    


class GeolocationValue(Base):
    """
    geolocationValue schema
    """
    __tablename__ = 'geolocationValue'
    
    id = Column(Integer(), primary_key=True)
    description = Column(Text())
    has_raw_value = Column(Text())
    latitude = Column(Float())
    longitude = Column(Text())
    type = Column(Text())
    was_generated_by = Column(Text())
    
    
    def __repr__(self):
        return f"geolocationValue(id={self.id},description={self.description},has_raw_value={self.has_raw_value},latitude={self.latitude},longitude={self.longitude},type={self.type},was_generated_by={self.was_generated_by},)"
        
    
        
    


class SampleOperations(Base):
    """
    sampleOperations schema
    """
    __tablename__ = 'sampleOperations'
    
    id = Column(Integer(), primary_key=True)
    type = Column(Text())
    detection_id = Column(Integer())
    separation_id = Column(Integer())
    analyte_id = Column(Integer())
    container_type = Column(Text())
    volume_unit = Column(Text())
    sample_state = Column(Text())
    volume = Column(Integer())
    analyte_volume = Column(Integer())
    source_mat_id = Column(Integer())
    derivatization = Column(Integer())
    derivatization_agent = Column(Integer())
    device = Column(Integer())
    unit = Column(Integer())
    celsius_temperature = Column(Integer())
    duration = Column(Integer())
    mixing = Column(Integer())
    sample_volume = Column(Integer())
    speed = Column(Integer())
    concentration = Column(Integer())
    dry = Column(Text())
    value = Column(Integer())
    sample_mass = Column(Integer())
    starting_amount = Column(Integer())
    acid = Column(Text())
    pH = Column(Integer())
    filter = Column(Text())
    material_pore_size = Column(Integer())
    conditioning = Column(Integer())
    conditioning_volume = Column(Integer())
    separation_method = Column(Integer())
    container_size = Column(Integer())
    extractant = Column(Integer())
    material_component_separation = Column(Text())
    analytical_solution = Column(Integer())
    instrument = Column(Integer())
    sieve_size = Column(Integer())
    reactant = Column(Integer())
    
    
    def __repr__(self):
        return f"sampleOperations(id={self.id},type={self.type},detection_id={self.detection_id},separation_id={self.separation_id},analyte_id={self.analyte_id},container_type={self.container_type},volume_unit={self.volume_unit},sample_state={self.sample_state},volume={self.volume},analyte_volume={self.analyte_volume},source_mat_id={self.source_mat_id},derivatization={self.derivatization},derivatization_agent={self.derivatization_agent},device={self.device},unit={self.unit},celsius_temperature={self.celsius_temperature},duration={self.duration},mixing={self.mixing},sample_volume={self.sample_volume},speed={self.speed},concentration={self.concentration},dry={self.dry},value={self.value},sample_mass={self.sample_mass},starting_amount={self.starting_amount},acid={self.acid},pH={self.pH},filter={self.filter},material_pore_size={self.material_pore_size},conditioning={self.conditioning},conditioning_volume={self.conditioning_volume},separation_method={self.separation_method},container_size={self.container_size},extractant={self.extractant},material_component_separation={self.material_component_separation},analytical_solution={self.analytical_solution},instrument={self.instrument},sieve_size={self.sieve_size},reactant={self.reactant},)"
        
    
        
    


class SampleProcessing(Base):
    """
    sampleProcessing schema
    """
    __tablename__ = 'sampleProcessing'
    
    id = Column(Integer(), primary_key=True)
    description = Column(Text())
    add_date = Column(Text())
    mod_date = Column(Text())
    instrument_name = Column(Text())
    name = Column(Text())
    ncbi_project_name = Column(Text())
    processing_institution = Column(Enum('EMSL', 'JGI', 'USCD', name='processinginstitutionenum'))
    type = Column(Text())
    omics_type_id = Column(Integer())
    chimera_check_id = Column(Integer())
    nucl_acid_amp_id = Column(Integer())
    nucl_acid_ext_id = Column(Integer())
    pcr_cond_id = Column(Integer())
    pcr_primers_id = Column(Integer())
    principal_investigator_id = Column(Integer())
    samp_vol_we_dna_ext_id = Column(Integer())
    seq_meth_id = Column(Integer())
    seq_quality_check_id = Column(Integer())
    target_gene_id = Column(Integer())
    target_subfragment_id = Column(Integer())
    
    
    GOLD_sequencing_project_identifier_rel = relationship( "SampleProcessingGOLDSequencingProjectIdentifier" )
    GOLD_sequencing_project_identifier = association_proxy("GOLD_sequencing_project_identifier_rel", "GOLD_sequencing_project_identifier",
                                  creator=lambda x_: SampleProcessingGOLDSequencingProjectIdentifier(GOLD_sequencing_project_identifier=x_))
    
    
    INSDC_experiment_identifiers_rel = relationship( "SampleProcessingINSDCExperimentIdentifiers" )
    INSDC_experiment_identifiers = association_proxy("INSDC_experiment_identifiers_rel", "INSDC_experiment_identifiers",
                                  creator=lambda x_: SampleProcessingINSDCExperimentIdentifiers(INSDC_experiment_identifiers=x_))
    
    
    alternative_identifiers_rel = relationship( "SampleProcessingAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: SampleProcessingAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    has_input_rel = relationship( "SampleProcessingHasInput" )
    has_input = association_proxy("has_input_rel", "has_input",
                                  creator=lambda x_: SampleProcessingHasInput(has_input=x_))
    
    
    has_output_rel = relationship( "SampleProcessingHasOutput" )
    has_output = association_proxy("has_output_rel", "has_output",
                                  creator=lambda x_: SampleProcessingHasOutput(has_output=x_))
    
    
    part_of_rel = relationship( "SampleProcessingPartOf" )
    part_of = association_proxy("part_of_rel", "part_of",
                                  creator=lambda x_: SampleProcessingPartOf(part_of=x_))
    
    
    def __repr__(self):
        return f"sampleProcessing(id={self.id},description={self.description},add_date={self.add_date},mod_date={self.mod_date},instrument_name={self.instrument_name},name={self.name},ncbi_project_name={self.ncbi_project_name},processing_institution={self.processing_institution},type={self.type},omics_type_id={self.omics_type_id},chimera_check_id={self.chimera_check_id},nucl_acid_amp_id={self.nucl_acid_amp_id},nucl_acid_ext_id={self.nucl_acid_ext_id},pcr_cond_id={self.pcr_cond_id},pcr_primers_id={self.pcr_primers_id},principal_investigator_id={self.principal_investigator_id},samp_vol_we_dna_ext_id={self.samp_vol_we_dna_ext_id},seq_meth_id={self.seq_meth_id},seq_quality_check_id={self.seq_quality_check_id},target_gene_id={self.target_gene_id},target_subfragment_id={self.target_subfragment_id},)"
        
    
        
    


class BioSample(Base):
    """
    bioSample schema
    """
    __tablename__ = 'bioSample'
    
    id = Column(Integer(), primary_key=True)
    identifier = Column(Text())
    technical_reps = Column(Integer())
    replicate_number = Column(Integer())
    collection_date_inc = Column(Text())
    collection_time = Column(DateTime())
    collection_tim_inc = Column(DateTime())
    community = Column(Text())
    description = Column(Text())
    canary = Column(Text())
    add_date = Column(DateTime())
    mod_date = Column(DateTime())
    dna_absorb1 = Column(Text())
    dna_absorb2 = Column(Text())
    dna_collect_site = Column(Text())
    dna_cont_well = Column(Text())
    dna_container_id = Column(Text())
    dna_concentration = Column(Text())
    dna_isolate_meth = Column(Text())
    dna_organisms = Column(Text())
    dna_project_contact = Column(Text())
    dna_samp_ID = Column(Text())
    dna_sample_format = Column(Enum('10 mM Tris-HCl', 'DNAStable', 'Ethanol', 'Low EDTA TE', 'MDA reaction buffer', 'PBS', 'Pellet', 'RNAStable', 'TE', 'Water', name='dnasampleformatenum'))
    dna_sample_name = Column(Text())
    dna_seq_project = Column(Text())
    dna_seq_project_PI = Column(Text())
    dna_seq_project_name = Column(Text())
    dnase_rna = Column(Enum('True', 'False', name='dnasernaenum'))
    dna_volume = Column(Text())
    ecosystem = Column(Text())
    ecosystem_category = Column(Text())
    ecosystem_subtype = Column(Text())
    ecosystem_type = Column(Text())
    experimental_factor_other = Column(Text())
    EMSL_store_temp = Column(Text())
    filter_method = Column(Text())
    host_name = Column(Text())
    other_treatment = Column(Text())
    org_nitro_method = Column(Text())
    isotope_exposure = Column(Text())
    location = Column(Text())
    specific_ecosystem = Column(Text())
    habitat = Column(Text())
    micro_biomass_C_meth = Column(Text())
    micro_biomass_N_meth = Column(Text())
    micro_biomass_meth = Column(Text())
    microbial_biomass_N = Column(Text())
    microbial_biomass_C = Column(Text())
    non_microb_biomass = Column(Text())
    non_microb_biomass_method = Column(Text())
    name = Column(Text())
    ncbi_taxonomy_name = Column(Text())
    salinity_category = Column(Text())
    project_id = Column(Text())
    proport_woa_temperature = Column(Text())
    proposal_dna = Column(Text())
    proposal_rna = Column(Text())
    rna_absorb1 = Column(Text())
    rna_absorb2 = Column(Text())
    rna_collect_site = Column(Text())
    rna_concentration = Column(Text())
    rna_cont_type = Column(Enum('tube', 'plate', name='rnaconttypeenum'))
    rna_cont_well = Column(Text())
    rna_container_ID = Column(Text())
    rna_isolate_meth = Column(Text())
    rna_organisms = Column(Text())
    rna_project_contact = Column(Text())
    rna_samp_ID = Column(Text())
    rna_sample_format = Column(Enum('10 mM Tris-HCl', 'DNAStable', 'Ethanol', 'Low EDTA TE', 'MDA reaction buffer', 'PBS', 'Pellet', 'RNAStable', 'TE', 'Water', name='rnasampleformatenum'))
    rna_sample_name = Column(Text())
    rna_seq_project = Column(Text())
    rna_seq_project_PI = Column(Text())
    rna_seq_project_name = Column(Text())
    rna_volume = Column(Text())
    type = Column(Text())
    analysis_type = Column(Enum('culture environmental', 'mixed culture', 'plant associated', 'pore water', 'pure culture', 'sediment', 'soil', 'water', 'water extract biosolid', 'water extract soil', name='analysistypeenum'))
    dna_cont_type = Column(Enum('plate', 'tube', name='dnaconttypeenum'))
    dna_dnase = Column(Enum('True', 'False', name='dnadnaseenum'))
    samp_collec_method = Column(Text())
    sample_collection_site = Column(Text())
    sample_shipped = Column(Text())
    sample_type = Column(Enum('soil', 'water_extract_soil', name='sampletypeenum'))
    soil_texture_meth = Column(Text())
    soluble_iron_micromol = Column(Text())
    start_date_inc = Column(Text())
    start_time_inc = Column(Text())
    tot_nitro_cont_meth = Column(Text())
    water_cont_soil_meth = Column(Text())
    env_broad_scale_id = Column(Integer())
    env_local_scale_id = Column(Integer())
    env_medium_id = Column(Integer())
    alt_id = Column(Integer())
    air_temp_regm_id = Column(Integer())
    aminopept_act_id = Column(Integer())
    ammonium_id = Column(Integer())
    ammonium_nitrogen_id = Column(Integer())
    annual_precpt_id = Column(Integer())
    annual_temp_id = Column(Integer())
    bacteria_carb_prod_id = Column(Integer())
    bishomohopanol_id = Column(Integer())
    bromide_id = Column(Integer())
    calcium_id = Column(Integer())
    carb_nitro_ratio_id = Column(Integer())
    chloride_id = Column(Integer())
    chlorophyll_id = Column(Integer())
    collection_date_id = Column(Integer())
    crop_rotation_id = Column(Integer())
    density_id = Column(Integer())
    diss_carb_dioxide_id = Column(Integer())
    diss_hydrogen_id = Column(Integer())
    diss_inorg_carb_id = Column(Integer())
    diss_inorg_phosp_id = Column(Integer())
    diss_org_carb_id = Column(Integer())
    diss_org_nitro_id = Column(Integer())
    diss_oxygen_id = Column(Integer())
    elev_id = Column(Integer())
    glucosidase_act_id = Column(Integer())
    GrowthFacil_id = Column(Integer())
    humidity_regm_id = Column(Integer())
    magnesium_id = Column(Integer())
    manganese_id = Column(Integer())
    mean_frict_vel_id = Column(Integer())
    mean_peak_frict_vel_id = Column(Integer())
    microbial_biomass_id = Column(Integer())
    microbial_biomass_meth_id = Column(Integer())
    misc_param_id = Column(Integer())
    n_alkanse_id = Column(Integer())
    nitrate_id = Column(Integer())
    nitrate_nitrogen_id = Column(Integer())
    nitrite_id = Column(Integer())
    nitrite_nitrogen = Column(Integer())
    org_matter_id = Column(Integer())
    org_nitro_id = Column(Integer())
    organism_count_id = Column(Integer())
    samp_store_temp_id = Column(Integer())
    part_org_carb_id = Column(Integer())
    petroleum_hydrocarb_id = Column(Integer())
    ph_id = Column(Integer())
    ph_meth_id = Column(Integer())
    phaeopigments_id = Column(Integer())
    phosphate_id = Column(Integer())
    phosplipid_fatt_acid_id = Column(Integer())
    pool_dna_extracts_id = Column(Integer())
    potassium_id = Column(Integer())
    pressure_id = Column(Integer())
    profile_position_id = Column(Integer())
    redox_potential_id = Column(Integer())
    salinity_id = Column(Integer())
    samp_vol_we_dna_ext_id = Column(Integer())
    season_precpt_id = Column(Integer())
    season_temp_id = Column(Integer())
    sieving_id = Column(Integer())
    size_frac_low_id = Column(Integer())
    size_frac_up_id = Column(Integer())
    slope_aspect_id = Column(Integer())
    slope_gradient_id = Column(Integer())
    sodium_id = Column(Integer())
    soil_text_measure_id = Column(Integer())
    subsurface_depth_id = Column(Integer())
    subsurface_depth2_id = Column(Integer())
    sulfate_id = Column(Integer())
    sulfide_id = Column(Integer())
    temp_id = Column(Integer())
    texture_id = Column(Integer())
    tot_carb_id = Column(Integer())
    tot_depth_water_col_id = Column(Integer())
    tot_diss_nitro_id = Column(Integer())
    tot_nitro_content_id = Column(Integer())
    tot_org_carb_id = Column(Integer())
    water_content_id = Column(Integer())
    watering_regm_id = Column(Integer())
    zinc_id = Column(Integer())
    agrochem_addition_id = Column(Integer())
    al_sat_id = Column(Integer())
    al_sat_meth_id = Column(Integer())
    alkalinity_id = Column(Integer())
    alkalinity_method_id = Column(Integer())
    alkyl_diethers_id = Column(Integer())
    biotic_regm_id = Column(Integer())
    biotic_relationship_id = Column(Integer())
    climate_environment_id = Column(Integer())
    cur_land_us_id = Column(Integer())
    cur_vegetation_id = Column(Integer())
    cur_vegetation_meth_id = Column(Integer())
    depth_id = Column(Integer())
    depth2_id = Column(Integer())
    drainage_class_id = Column(Integer())
    env_package_id = Column(Integer())
    extreme_event_id = Column(Integer())
    experiemental_factor_id = Column(Integer())
    fao_class_id = Column(Integer())
    fire_id = Column(Integer())
    flooding_id = Column(Integer())
    gaseous_environment_id = Column(Integer())
    geo_loc_name_id = Column(Integer())
    growth_facil_id = Column(Integer())
    heavy_metals_meth_id = Column(Integer())
    heavy_metals_id = Column(Integer())
    horizon_id = Column(Integer())
    horizon_meth_id = Column(Integer())
    lat_Ion_id = Column(Integer())
    lbc_thirty_id = Column(Integer())
    lbceq_id = Column(Integer())
    light_regm_id = Column(Integer())
    link_addit_analysis_id = Column(Integer())
    link_class_info_id = Column(Integer())
    link_climate_info_id = Column(Integer())
    local_class_id = Column(Integer())
    local_class_meth_id = Column(Integer())
    rel_to_oxygen_id = Column(Integer())
    samp_size_id = Column(Integer())
    samp_collect_device_id = Column(Integer())
    samp_mat_process_id = Column(Integer())
    soil_type_id = Column(Integer())
    soil_type_meth_id = Column(Integer())
    source_mat_id = Column(Integer())
    salinity_meth_id = Column(Integer())
    samp_store_dur_id = Column(Integer())
    samp_store_loc_id = Column(Integer())
    store_cond_id = Column(Integer())
    tidal_stage_id = Column(Integer())
    perturbation_id = Column(Integer())
    chem_administration_id = Column(Integer())
    oxy_stat_samp_id = Column(Integer())
    texture_meth_id = Column(Integer())
    tot_org_c_meth_id = Column(Integer())
    tillage_id = Column(Integer())
    previous_land_use_id = Column(Integer())
    previous_land_use_meth_id = Column(Integer())
    sample_operations_id = Column(Integer())
    
    
    alternative_identifiers_rel = relationship( "BioSampleAlternativeIdentifiers" )
    alternative_identifiers = association_proxy("alternative_identifiers_rel", "alternative_identifiers",
                                  creator=lambda x_: BioSampleAlternativeIdentifiers(alternative_identifiers=x_))
    
    
    GOLD_sample_identifiers_rel = relationship( "BioSampleGOLDSampleIdentifiers" )
    GOLD_sample_identifiers = association_proxy("GOLD_sample_identifiers_rel", "GOLD_sample_identifiers",
                                  creator=lambda x_: BioSampleGOLDSampleIdentifiers(GOLD_sample_identifiers=x_))
    
    
    INSDC_biosample_identifiers_rel = relationship( "BioSampleINSDCBiosampleIdentifiers" )
    INSDC_biosample_identifiers = association_proxy("INSDC_biosample_identifiers_rel", "INSDC_biosample_identifiers",
                                  creator=lambda x_: BioSampleINSDCBiosampleIdentifiers(INSDC_biosample_identifiers=x_))
    
    
    INSDC_secondary_sample_identifiers_rel = relationship( "BioSampleINSDCSecondarySampleIdentifiers" )
    INSDC_secondary_sample_identifiers = association_proxy("INSDC_secondary_sample_identifiers_rel", "INSDC_secondary_sample_identifiers",
                                  creator=lambda x_: BioSampleINSDCSecondarySampleIdentifiers(INSDC_secondary_sample_identifiers=x_))
    
    
    part_of_rel = relationship( "BioSamplePartOf" )
    part_of = association_proxy("part_of_rel", "part_of",
                                  creator=lambda x_: BioSamplePartOf(part_of=x_))
    
    
    sample_link_rel = relationship( "BioSampleSampleLink" )
    sample_link = association_proxy("sample_link_rel", "sample_link",
                                  creator=lambda x_: BioSampleSampleLink(sample_link=x_))
    
    
    def __repr__(self):
        return f"bioSample(id={self.id},identifier={self.identifier},technical_reps={self.technical_reps},replicate_number={self.replicate_number},collection_date_inc={self.collection_date_inc},collection_time={self.collection_time},collection_tim_inc={self.collection_tim_inc},community={self.community},description={self.description},canary={self.canary},add_date={self.add_date},mod_date={self.mod_date},dna_absorb1={self.dna_absorb1},dna_absorb2={self.dna_absorb2},dna_collect_site={self.dna_collect_site},dna_cont_well={self.dna_cont_well},dna_container_id={self.dna_container_id},dna_concentration={self.dna_concentration},dna_isolate_meth={self.dna_isolate_meth},dna_organisms={self.dna_organisms},dna_project_contact={self.dna_project_contact},dna_samp_ID={self.dna_samp_ID},dna_sample_format={self.dna_sample_format},dna_sample_name={self.dna_sample_name},dna_seq_project={self.dna_seq_project},dna_seq_project_PI={self.dna_seq_project_PI},dna_seq_project_name={self.dna_seq_project_name},dnase_rna={self.dnase_rna},dna_volume={self.dna_volume},ecosystem={self.ecosystem},ecosystem_category={self.ecosystem_category},ecosystem_subtype={self.ecosystem_subtype},ecosystem_type={self.ecosystem_type},experimental_factor_other={self.experimental_factor_other},EMSL_store_temp={self.EMSL_store_temp},filter_method={self.filter_method},host_name={self.host_name},other_treatment={self.other_treatment},org_nitro_method={self.org_nitro_method},isotope_exposure={self.isotope_exposure},location={self.location},specific_ecosystem={self.specific_ecosystem},habitat={self.habitat},micro_biomass_C_meth={self.micro_biomass_C_meth},micro_biomass_N_meth={self.micro_biomass_N_meth},micro_biomass_meth={self.micro_biomass_meth},microbial_biomass_N={self.microbial_biomass_N},microbial_biomass_C={self.microbial_biomass_C},non_microb_biomass={self.non_microb_biomass},non_microb_biomass_method={self.non_microb_biomass_method},name={self.name},ncbi_taxonomy_name={self.ncbi_taxonomy_name},salinity_category={self.salinity_category},project_id={self.project_id},proport_woa_temperature={self.proport_woa_temperature},proposal_dna={self.proposal_dna},proposal_rna={self.proposal_rna},rna_absorb1={self.rna_absorb1},rna_absorb2={self.rna_absorb2},rna_collect_site={self.rna_collect_site},rna_concentration={self.rna_concentration},rna_cont_type={self.rna_cont_type},rna_cont_well={self.rna_cont_well},rna_container_ID={self.rna_container_ID},rna_isolate_meth={self.rna_isolate_meth},rna_organisms={self.rna_organisms},rna_project_contact={self.rna_project_contact},rna_samp_ID={self.rna_samp_ID},rna_sample_format={self.rna_sample_format},rna_sample_name={self.rna_sample_name},rna_seq_project={self.rna_seq_project},rna_seq_project_PI={self.rna_seq_project_PI},rna_seq_project_name={self.rna_seq_project_name},rna_volume={self.rna_volume},type={self.type},analysis_type={self.analysis_type},dna_cont_type={self.dna_cont_type},dna_dnase={self.dna_dnase},samp_collec_method={self.samp_collec_method},sample_collection_site={self.sample_collection_site},sample_shipped={self.sample_shipped},sample_type={self.sample_type},soil_texture_meth={self.soil_texture_meth},soluble_iron_micromol={self.soluble_iron_micromol},start_date_inc={self.start_date_inc},start_time_inc={self.start_time_inc},tot_nitro_cont_meth={self.tot_nitro_cont_meth},water_cont_soil_meth={self.water_cont_soil_meth},env_broad_scale_id={self.env_broad_scale_id},env_local_scale_id={self.env_local_scale_id},env_medium_id={self.env_medium_id},alt_id={self.alt_id},air_temp_regm_id={self.air_temp_regm_id},aminopept_act_id={self.aminopept_act_id},ammonium_id={self.ammonium_id},ammonium_nitrogen_id={self.ammonium_nitrogen_id},annual_precpt_id={self.annual_precpt_id},annual_temp_id={self.annual_temp_id},bacteria_carb_prod_id={self.bacteria_carb_prod_id},bishomohopanol_id={self.bishomohopanol_id},bromide_id={self.bromide_id},calcium_id={self.calcium_id},carb_nitro_ratio_id={self.carb_nitro_ratio_id},chloride_id={self.chloride_id},chlorophyll_id={self.chlorophyll_id},collection_date_id={self.collection_date_id},crop_rotation_id={self.crop_rotation_id},density_id={self.density_id},diss_carb_dioxide_id={self.diss_carb_dioxide_id},diss_hydrogen_id={self.diss_hydrogen_id},diss_inorg_carb_id={self.diss_inorg_carb_id},diss_inorg_phosp_id={self.diss_inorg_phosp_id},diss_org_carb_id={self.diss_org_carb_id},diss_org_nitro_id={self.diss_org_nitro_id},diss_oxygen_id={self.diss_oxygen_id},elev_id={self.elev_id},glucosidase_act_id={self.glucosidase_act_id},GrowthFacil_id={self.GrowthFacil_id},humidity_regm_id={self.humidity_regm_id},magnesium_id={self.magnesium_id},manganese_id={self.manganese_id},mean_frict_vel_id={self.mean_frict_vel_id},mean_peak_frict_vel_id={self.mean_peak_frict_vel_id},microbial_biomass_id={self.microbial_biomass_id},microbial_biomass_meth_id={self.microbial_biomass_meth_id},misc_param_id={self.misc_param_id},n_alkanse_id={self.n_alkanse_id},nitrate_id={self.nitrate_id},nitrate_nitrogen_id={self.nitrate_nitrogen_id},nitrite_id={self.nitrite_id},nitrite_nitrogen={self.nitrite_nitrogen},org_matter_id={self.org_matter_id},org_nitro_id={self.org_nitro_id},organism_count_id={self.organism_count_id},samp_store_temp_id={self.samp_store_temp_id},part_org_carb_id={self.part_org_carb_id},petroleum_hydrocarb_id={self.petroleum_hydrocarb_id},ph_id={self.ph_id},ph_meth_id={self.ph_meth_id},phaeopigments_id={self.phaeopigments_id},phosphate_id={self.phosphate_id},phosplipid_fatt_acid_id={self.phosplipid_fatt_acid_id},pool_dna_extracts_id={self.pool_dna_extracts_id},potassium_id={self.potassium_id},pressure_id={self.pressure_id},profile_position_id={self.profile_position_id},redox_potential_id={self.redox_potential_id},salinity_id={self.salinity_id},samp_vol_we_dna_ext_id={self.samp_vol_we_dna_ext_id},season_precpt_id={self.season_precpt_id},season_temp_id={self.season_temp_id},sieving_id={self.sieving_id},size_frac_low_id={self.size_frac_low_id},size_frac_up_id={self.size_frac_up_id},slope_aspect_id={self.slope_aspect_id},slope_gradient_id={self.slope_gradient_id},sodium_id={self.sodium_id},soil_text_measure_id={self.soil_text_measure_id},subsurface_depth_id={self.subsurface_depth_id},subsurface_depth2_id={self.subsurface_depth2_id},sulfate_id={self.sulfate_id},sulfide_id={self.sulfide_id},temp_id={self.temp_id},texture_id={self.texture_id},tot_carb_id={self.tot_carb_id},tot_depth_water_col_id={self.tot_depth_water_col_id},tot_diss_nitro_id={self.tot_diss_nitro_id},tot_nitro_content_id={self.tot_nitro_content_id},tot_org_carb_id={self.tot_org_carb_id},water_content_id={self.water_content_id},watering_regm_id={self.watering_regm_id},zinc_id={self.zinc_id},agrochem_addition_id={self.agrochem_addition_id},al_sat_id={self.al_sat_id},al_sat_meth_id={self.al_sat_meth_id},alkalinity_id={self.alkalinity_id},alkalinity_method_id={self.alkalinity_method_id},alkyl_diethers_id={self.alkyl_diethers_id},biotic_regm_id={self.biotic_regm_id},biotic_relationship_id={self.biotic_relationship_id},climate_environment_id={self.climate_environment_id},cur_land_us_id={self.cur_land_us_id},cur_vegetation_id={self.cur_vegetation_id},cur_vegetation_meth_id={self.cur_vegetation_meth_id},depth_id={self.depth_id},depth2_id={self.depth2_id},drainage_class_id={self.drainage_class_id},env_package_id={self.env_package_id},extreme_event_id={self.extreme_event_id},experiemental_factor_id={self.experiemental_factor_id},fao_class_id={self.fao_class_id},fire_id={self.fire_id},flooding_id={self.flooding_id},gaseous_environment_id={self.gaseous_environment_id},geo_loc_name_id={self.geo_loc_name_id},growth_facil_id={self.growth_facil_id},heavy_metals_meth_id={self.heavy_metals_meth_id},heavy_metals_id={self.heavy_metals_id},horizon_id={self.horizon_id},horizon_meth_id={self.horizon_meth_id},lat_Ion_id={self.lat_Ion_id},lbc_thirty_id={self.lbc_thirty_id},lbceq_id={self.lbceq_id},light_regm_id={self.light_regm_id},link_addit_analysis_id={self.link_addit_analysis_id},link_class_info_id={self.link_class_info_id},link_climate_info_id={self.link_climate_info_id},local_class_id={self.local_class_id},local_class_meth_id={self.local_class_meth_id},rel_to_oxygen_id={self.rel_to_oxygen_id},samp_size_id={self.samp_size_id},samp_collect_device_id={self.samp_collect_device_id},samp_mat_process_id={self.samp_mat_process_id},soil_type_id={self.soil_type_id},soil_type_meth_id={self.soil_type_meth_id},source_mat_id={self.source_mat_id},salinity_meth_id={self.salinity_meth_id},samp_store_dur_id={self.samp_store_dur_id},samp_store_loc_id={self.samp_store_loc_id},store_cond_id={self.store_cond_id},tidal_stage_id={self.tidal_stage_id},perturbation_id={self.perturbation_id},chem_administration_id={self.chem_administration_id},oxy_stat_samp_id={self.oxy_stat_samp_id},texture_meth_id={self.texture_meth_id},tot_org_c_meth_id={self.tot_org_c_meth_id},tillage_id={self.tillage_id},previous_land_use_id={self.previous_land_use_id},previous_land_use_meth_id={self.previous_land_use_meth_id},sample_operations_id={self.sample_operations_id},)"
        
    
        
    


class MetaProteomicsAnalysisActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'MetaProteomicsAnalysisActivity_has_input'
    
    MetaProteomicsAnalysisActivity_id = Column(Text(), ForeignKey('MetaProteomicsAnalysisActivity.id'), primary_key=True)
    has_input = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"MetaProteomicsAnalysisActivity_has_input(MetaProteomicsAnalysisActivity_id={self.MetaProteomicsAnalysisActivity_id},has_input={self.has_input},)"
        
    
        
    


class MetaProteomicsAnalysisActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'MetaProteomicsAnalysisActivity_has_output'
    
    MetaProteomicsAnalysisActivity_id = Column(Text(), ForeignKey('MetaProteomicsAnalysisActivity.id'), primary_key=True)
    has_output = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"MetaProteomicsAnalysisActivity_has_output(MetaProteomicsAnalysisActivity_id={self.MetaProteomicsAnalysisActivity_id},has_output={self.has_output},)"
        
    
        
    


class MetaProteomicsAnalysisActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'MetaProteomicsAnalysisActivity_part_of'
    
    MetaProteomicsAnalysisActivity_id = Column(Text(), ForeignKey('MetaProteomicsAnalysisActivity.id'), primary_key=True)
    part_of = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"MetaProteomicsAnalysisActivity_part_of(MetaProteomicsAnalysisActivity_id={self.MetaProteomicsAnalysisActivity_id},part_of={self.part_of},)"
        
    
        
    


class MetaboliteQuantificationAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'MetaboliteQuantification_alternative_identifiers'
    
    MetaboliteQuantification_id = Column(Text(), ForeignKey('MetaboliteQuantification.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"MetaboliteQuantification_alternative_identifiers(MetaboliteQuantification_id={self.MetaboliteQuantification_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class NomAnalysisActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'NomAnalysisActivity_has_input'
    
    NomAnalysisActivity_id = Column(Text(), ForeignKey('NomAnalysisActivity.id'), primary_key=True)
    has_input = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"NomAnalysisActivity_has_input(NomAnalysisActivity_id={self.NomAnalysisActivity_id},has_input={self.has_input},)"
        
    
        
    


class NomAnalysisActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'NomAnalysisActivity_has_output'
    
    NomAnalysisActivity_id = Column(Text(), ForeignKey('NomAnalysisActivity.id'), primary_key=True)
    has_output = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"NomAnalysisActivity_has_output(NomAnalysisActivity_id={self.NomAnalysisActivity_id},has_output={self.has_output},)"
        
    
        
    


class NomAnalysisActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'NomAnalysisActivity_part_of'
    
    NomAnalysisActivity_id = Column(Text(), ForeignKey('NomAnalysisActivity.id'), primary_key=True)
    part_of = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"NomAnalysisActivity_part_of(NomAnalysisActivity_id={self.NomAnalysisActivity_id},part_of={self.part_of},)"
        
    
        
    


class OntologyClassAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'OntologyClass_alternative_identifiers'
    
    OntologyClass_id = Column(Text(), ForeignKey('OntologyClass.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"OntologyClass_alternative_identifiers(OntologyClass_id={self.OntologyClass_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class PeptideQuantificationAllProteins(Base):
    """
    
    """
    __tablename__ = 'PeptideQuantification_all_proteins'
    
    PeptideQuantification_id = Column(Text(), ForeignKey('PeptideQuantification.id'), primary_key=True)
    all_proteins = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"PeptideQuantification_all_proteins(PeptideQuantification_id={self.PeptideQuantification_id},all_proteins={self.all_proteins},)"
        
    
        
    


class WorkFlowExecutionActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'WorkFlowExecutionActivity_has_input'
    
    WorkFlowExecutionActivity_id = Column(Text(), ForeignKey('WorkFlowExecutionActivity.id'), primary_key=True)
    has_input = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"WorkFlowExecutionActivity_has_input(WorkFlowExecutionActivity_id={self.WorkFlowExecutionActivity_id},has_input={self.has_input},)"
        
    
        
    


class WorkFlowExecutionActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'WorkFlowExecutionActivity_has_output'
    
    WorkFlowExecutionActivity_id = Column(Text(), ForeignKey('WorkFlowExecutionActivity.id'), primary_key=True)
    has_output = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"WorkFlowExecutionActivity_has_output(WorkFlowExecutionActivity_id={self.WorkFlowExecutionActivity_id},has_output={self.has_output},)"
        
    
        
    


class WorkFlowExecutionActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'WorkFlowExecutionActivity_part_of'
    
    WorkFlowExecutionActivity_id = Column(Text(), ForeignKey('WorkFlowExecutionActivity.id'), primary_key=True)
    part_of = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"WorkFlowExecutionActivity_part_of(WorkFlowExecutionActivity_id={self.WorkFlowExecutionActivity_id},part_of={self.part_of},)"
        
    
        
    


class MetabolomicsAnalysisActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'metabolomicsAnalysisActivity_has_input'
    
    metabolomicsAnalysisActivity_id = Column(Text(), ForeignKey('metabolomicsAnalysisActivity.id'), primary_key=True)
    has_input = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"metabolomicsAnalysisActivity_has_input(metabolomicsAnalysisActivity_id={self.metabolomicsAnalysisActivity_id},has_input={self.has_input},)"
        
    
        
    


class MetabolomicsAnalysisActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'metabolomicsAnalysisActivity_has_output'
    
    metabolomicsAnalysisActivity_id = Column(Text(), ForeignKey('metabolomicsAnalysisActivity.id'), primary_key=True)
    has_output = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"metabolomicsAnalysisActivity_has_output(metabolomicsAnalysisActivity_id={self.metabolomicsAnalysisActivity_id},has_output={self.has_output},)"
        
    
        
    


class MetabolomicsAnalysisActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'metabolomicsAnalysisActivity_part_of'
    
    metabolomicsAnalysisActivity_id = Column(Text(), ForeignKey('metabolomicsAnalysisActivity.id'), primary_key=True)
    part_of = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"metabolomicsAnalysisActivity_part_of(metabolomicsAnalysisActivity_id={self.metabolomicsAnalysisActivity_id},part_of={self.part_of},)"
        
    
        
    


class MagsAnalysisActivityHasInput(Base):
    """
    
    """
    __tablename__ = 'magsAnalysisActivity_has_input'
    
    magsAnalysisActivity_id = Column(Text(), ForeignKey('magsAnalysisActivity.id'), primary_key=True)
    has_input = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"magsAnalysisActivity_has_input(magsAnalysisActivity_id={self.magsAnalysisActivity_id},has_input={self.has_input},)"
        
    
        
    


class MagsAnalysisActivityHasOutput(Base):
    """
    
    """
    __tablename__ = 'magsAnalysisActivity_has_output'
    
    magsAnalysisActivity_id = Column(Text(), ForeignKey('magsAnalysisActivity.id'), primary_key=True)
    has_output = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"magsAnalysisActivity_has_output(magsAnalysisActivity_id={self.magsAnalysisActivity_id},has_output={self.has_output},)"
        
    
        
    


class MagsAnalysisActivityPartOf(Base):
    """
    
    """
    __tablename__ = 'magsAnalysisActivity_part_of'
    
    magsAnalysisActivity_id = Column(Text(), ForeignKey('magsAnalysisActivity.id'), primary_key=True)
    part_of = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"magsAnalysisActivity_part_of(magsAnalysisActivity_id={self.magsAnalysisActivity_id},part_of={self.part_of},)"
        
    
        
    


class DataObjectAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'dataObject_alternative_identifiers'
    
    dataObject_id = Column(Text(), ForeignKey('dataObject.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"dataObject_alternative_identifiers(dataObject_id={self.dataObject_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class PersonValueWebsites(Base):
    """
    
    """
    __tablename__ = 'personValue_websites'
    
    personValue_id = Column(Text(), ForeignKey('personValue.id'), primary_key=True)
    websites = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"personValue_websites(personValue_id={self.personValue_id},websites={self.websites},)"
        
    
        
    


class SampleProcessingGOLDSequencingProjectIdentifier(Base):
    """
    
    """
    __tablename__ = 'sampleProcessing_GOLD_sequencing_project_identifier'
    
    sampleProcessing_id = Column(Text(), ForeignKey('sampleProcessing.id'), primary_key=True)
    GOLD_sequencing_project_identifier = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"sampleProcessing_GOLD_sequencing_project_identifier(sampleProcessing_id={self.sampleProcessing_id},GOLD_sequencing_project_identifier={self.GOLD_sequencing_project_identifier},)"
        
    
        
    


class SampleProcessingINSDCExperimentIdentifiers(Base):
    """
    
    """
    __tablename__ = 'sampleProcessing_INSDC_experiment_identifiers'
    
    sampleProcessing_id = Column(Text(), ForeignKey('sampleProcessing.id'), primary_key=True)
    INSDC_experiment_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"sampleProcessing_INSDC_experiment_identifiers(sampleProcessing_id={self.sampleProcessing_id},INSDC_experiment_identifiers={self.INSDC_experiment_identifiers},)"
        
    
        
    


class SampleProcessingAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'sampleProcessing_alternative_identifiers'
    
    sampleProcessing_id = Column(Text(), ForeignKey('sampleProcessing.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"sampleProcessing_alternative_identifiers(sampleProcessing_id={self.sampleProcessing_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class SampleProcessingHasInput(Base):
    """
    
    """
    __tablename__ = 'sampleProcessing_has_input'
    
    sampleProcessing_id = Column(Text(), ForeignKey('sampleProcessing.id'), primary_key=True)
    has_input = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"sampleProcessing_has_input(sampleProcessing_id={self.sampleProcessing_id},has_input={self.has_input},)"
        
    
        
    


class SampleProcessingHasOutput(Base):
    """
    
    """
    __tablename__ = 'sampleProcessing_has_output'
    
    sampleProcessing_id = Column(Text(), ForeignKey('sampleProcessing.id'), primary_key=True)
    has_output = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"sampleProcessing_has_output(sampleProcessing_id={self.sampleProcessing_id},has_output={self.has_output},)"
        
    
        
    


class SampleProcessingPartOf(Base):
    """
    
    """
    __tablename__ = 'sampleProcessing_part_of'
    
    sampleProcessing_id = Column(Text(), ForeignKey('sampleProcessing.id'), primary_key=True)
    part_of = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"sampleProcessing_part_of(sampleProcessing_id={self.sampleProcessing_id},part_of={self.part_of},)"
        
    
        
    


class BioSampleAlternativeIdentifiers(Base):
    """
    
    """
    __tablename__ = 'bioSample_alternative_identifiers'
    
    bioSample_id = Column(Text(), ForeignKey('bioSample.id'), primary_key=True)
    alternative_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"bioSample_alternative_identifiers(bioSample_id={self.bioSample_id},alternative_identifiers={self.alternative_identifiers},)"
        
    
        
    


class BioSampleGOLDSampleIdentifiers(Base):
    """
    
    """
    __tablename__ = 'bioSample_GOLD_sample_identifiers'
    
    bioSample_id = Column(Text(), ForeignKey('bioSample.id'), primary_key=True)
    GOLD_sample_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"bioSample_GOLD_sample_identifiers(bioSample_id={self.bioSample_id},GOLD_sample_identifiers={self.GOLD_sample_identifiers},)"
        
    
        
    


class BioSampleINSDCBiosampleIdentifiers(Base):
    """
    
    """
    __tablename__ = 'bioSample_INSDC_biosample_identifiers'
    
    bioSample_id = Column(Text(), ForeignKey('bioSample.id'), primary_key=True)
    INSDC_biosample_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"bioSample_INSDC_biosample_identifiers(bioSample_id={self.bioSample_id},INSDC_biosample_identifiers={self.INSDC_biosample_identifiers},)"
        
    
        
    


class BioSampleINSDCSecondarySampleIdentifiers(Base):
    """
    
    """
    __tablename__ = 'bioSample_INSDC_secondary_sample_identifiers'
    
    bioSample_id = Column(Text(), ForeignKey('bioSample.id'), primary_key=True)
    INSDC_secondary_sample_identifiers = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"bioSample_INSDC_secondary_sample_identifiers(bioSample_id={self.bioSample_id},INSDC_secondary_sample_identifiers={self.INSDC_secondary_sample_identifiers},)"
        
    
        
    


class BioSamplePartOf(Base):
    """
    
    """
    __tablename__ = 'bioSample_part_of'
    
    bioSample_id = Column(Text(), ForeignKey('bioSample.id'), primary_key=True)
    part_of = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"bioSample_part_of(bioSample_id={self.bioSample_id},part_of={self.part_of},)"
        
    
        
    


class BioSampleSampleLink(Base):
    """
    
    """
    __tablename__ = 'bioSample_sample_link'
    
    bioSample_id = Column(Text(), ForeignKey('bioSample.id'), primary_key=True)
    sample_link = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"bioSample_sample_link(bioSample_id={self.bioSample_id},sample_link={self.sample_link},)"
        
    
        
    


