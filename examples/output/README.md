## Database-MetabolomicsAnalysis-1
### Input
```yaml
metabolomics_analysis_set:
- ended_at_time: '2021-09-15T10:13:20+00:00'
  execution_resource: NERSC-Cori
  git_url: https://example.org/WorkflowExecutionActivity
  has_input:
  - nmdc:i1
  - nmdc:i2
  has_output:
  - nmdc:o1
  - nmdc:o2
  id: nmdc:wfmb-99-ABCDEF
  name: Metabolomics Analysis Activity for nmdc:wfmb-99-ABCDEF
  part_of:
  - nmdc:wfch-11-ab
  started_at_time: '2021-08-05T14:48:51+00:00'
  type: nmdc:MetabolomicsAnalysis

```
## Database-biosamples-dna-in-tube
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  dna_cont_type: tube
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-dtTMNb
  type: nmdc:Biosample

```
## NucleotideSequencing-2
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- gold:Gp0108335
analyte_category: metagenome
associated_studies:
- nmdc:sty-00-xxx
has_input:
- nmdc:bsm-00-red
has_output:
- nmdc:dobj-00-9n9n9n
id: nmdc:omprc-99-zUCd5N
mod_date: 22-MAY-20 06.13.12.927000000 PM
name: Thawing permafrost microbial communities from the Arctic, studying carbon transformations
  - Permafrost 712P3D
ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
  carbon transformations - Permafrost 712P3D
part_of:
- nmdc:omprc-00-555xxx
processing_institution: JGI
type: nmdc:NucleotideSequencing

```
## Database-extraction_set-minimal
### Input
```yaml
extraction_set:
- has_input:
  - generic:xxx
  has_output:
  - generic:yyy
  id: nmdc:extrp-99-abcdef
  name: DNA extraction of NEON sample WREF_072-O-20190618-COMP
  type: nmdc:Extraction

```
## ChromatographicSeparationProcess-compilation_example
### Input
```yaml
chromatographic_category: liquid_chromatography
has_input:
- nmdc:procsm-11-9gjxns61
has_output:
- nmdc:procsm-11-05g48p90
- nmdc:procsm-11-05g48p91
id: nmdc:cspro-99-oW43DzG0
ordered_mobile_phases:
- duration:
    has_numeric_value: 60
    has_unit: min
    type: nmdc:QuantityValue
  substances_used:
  - final_concentration:
      has_numeric_value: 10
      has_unit: '%'
      type: nmdc:QuantityValue
    known_as: nmdc:chem-99-000003
    type: nmdc:PortionOfSubstance
  type: nmdc:MobilePhaseSegment
- substances_used:
  - final_concentration:
      has_numeric_value: 15
      has_unit: mM
      type: nmdc:QuantityValue
    known_as: nmdc:chem-99-000015
    type: nmdc:PortionOfSubstance
  type: nmdc:MobilePhaseSegment
stationary_phase: CN
temperature:
  has_numeric_value: 25
  has_unit: Cel
  type: nmdc:QuantityValue
type: nmdc:ChromatographicSeparationProcess

```
## Database-metagenome-assembly
### Input
```yaml
metagenome_assembly_set:
- asm_score: 3.29
  contig_bp: 192123121
  contigs: 429340
  ctg_l50: 433
  ctg_l90: 288
  ctg_logsum: 303893
  ctg_max: 17245
  ctg_n50: 132307
  ctg_n90: 357156
  ctg_powsum: 32467
  ended_at_time: '2020-03-25T00:00:00+00:00'
  execution_resource: LANL-B-div
  gap_pct: 0
  gc_avg: 0.55402
  gc_std: 0.09822
  git_url: https://github.com/microbiomedata/metaAssembly/releases/tag/1.0.0
  has_input:
  - nmdc:bd723452a107e973fcc6734ff7894bb9
  has_output:
  - nmdc:8ecc9e4fe4c74d7a58b02fd8954555b9
  - nmdc:3f85e34d2c32b65e33e4abd2431dfbe8
  - nmdc:3c892f96e847b0b524d5d4e50611b5fd
  - nmdc:8e504039a96e9ab885eef69155127754
  - nmdc:cf15f0ee330bfda8f666a43222b23f8a
  id: nmdc:wfmgas-99-B7Vogx
  name: Metagenome assembly 1472_51277
  num_aligned_reads: 63046103
  num_input_reads: 87803950
  part_of:
  - nmdc:wfch-11-ab
  scaf_bp: 192123121
  scaf_l50: 433
  scaf_l90: 288
  scaf_l_gt50k: 0
  scaf_logsum: 303893
  scaf_max: 17245
  scaf_n50: 132307
  scaf_n90: 357156
  scaf_n_gt50k: 0
  scaf_pct_gt50k: 0
  scaf_powsum: 32467
  scaffolds: 429340
  started_at_time: '2020-03-24T00:00:00+00:00'
  type: nmdc:MetagenomeAssembly
- asm_score: 3.196
  contig_bp: 333164102
  contigs: 747801
  ctg_l50: 432
  ctg_l90: 289
  ctg_logsum: 483596
  ctg_max: 15780
  ctg_n50: 235059
  ctg_n90: 623912
  ctg_powsum: 51427
  ended_at_time: '2020-03-25T00:00:00+00:00'
  execution_resource: LANL-B-div
  gap_pct: 0
  gc_avg: 0.57087
  gc_std: 0.09613
  git_url: https://github.com/microbiomedata/metaAssembly/releases/tag/1.0.0
  has_input:
  - nmdc:b7e3ca7843cc0cf9a4944a9a9d3e2a66
  has_output:
  - nmdc:df1fa16afe70385923b5d36cfe9513f4
  - nmdc:c4358d917f029c6fd0f8a81f4e0f1119
  - nmdc:d3bfc0e4a96431a4c07f46ad150b6edd
  - nmdc:76655ec7b8a1e70a3cdf05bcd91ed9ed
  - nmdc:8cebf127e41e82bd908676051acf154b
  id: nmdc:wfmgas-99-CvgXTq
  name: Metagenome assembly 1472_51278
  num_aligned_reads: 95369019
  num_input_reads: 141175680
  part_of:
  - nmdc:wfch-11-ab
  scaf_bp: 333164102
  scaf_l50: 432
  scaf_l90: 289
  scaf_l_gt50k: 0
  scaf_logsum: 483596
  scaf_max: 15780
  scaf_n50: 235059
  scaf_n90: 623912
  scaf_n_gt50k: 0
  scaf_pct_gt50k: 0
  scaf_powsum: 51427
  scaffolds: 747801
  started_at_time: '2020-03-25T00:00:00+00:00'
  type: nmdc:MetagenomeAssembly
- asm_score: 3.527
  contig_bp: 279001661
  contigs: 607951
  ctg_l50: 449
  ctg_l90: 290
  ctg_logsum: 475574
  ctg_max: 26906
  ctg_n50: 183452
  ctg_n90: 505179
  ctg_powsum: 50819
  ended_at_time: '2020-03-25T00:00:00+00:00'
  execution_resource: LANL-B-div
  gap_pct: 0
  gc_avg: 0.55832
  gc_std: 0.09898
  git_url: https://github.com/microbiomedata/metaAssembly/releases/tag/1.0.0
  has_input:
  - nmdc:918109eabfaabfa7b7e948154c013e8a
  has_output:
  - nmdc:72f3b35ad52c9f2f17c39054ae05d8c7
  - nmdc:97deb14198281d7ff3e1a6d4ff7ab223
  - nmdc:2f4e213f4334bc304ff9d2f02c60e4a8
  - nmdc:66ac3134506a741f4e05b85a8b62e330
  - nmdc:1a84af1136a19bdd716320bdd0e47c67
  id: nmdc:wfmgas-99-L9Z34K
  name: Metagenome assembly 1472_51279
  num_aligned_reads: 79146088
  num_input_reads: 116129794
  part_of:
  - nmdc:wfch-11-ab
  scaf_bp: 279001661
  scaf_l50: 449
  scaf_l90: 290
  scaf_l_gt50k: 0
  scaf_logsum: 475574
  scaf_max: 26906
  scaf_n50: 183452
  scaf_n90: 505179
  scaf_n_gt50k: 0
  scaf_pct_gt50k: 0
  scaf_powsum: 50819
  scaffolds: 607951
  started_at_time: '2020-03-25T00:00:00+00:00'
  type: nmdc:MetagenomeAssembly

```
## Database-nmdc-example
### Input
```yaml
biosample_set:
- add_date: 17-MAR-17 04.55.54.717000000 PM
  associated_studies:
  - nmdc:sty-00-8675309
  community: microbial communities
  description: Permafrost microbial communities from Stordalen Mire, Sweden
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Wetlands
  ecosystem_type: Soil
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: 'Sweden: Stordalen'
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0150408
  habitat: Fen
  id: nmdc:bsm-99-isqhuW
  lat_lon:
    has_raw_value: 68.35 19.05
    latitude: 68.35
    longitude: 19.05
    type: nmdc:GeolocationValue
  location: Stordalen Mire, Sweden
  mod_date: 08-JAN-20 02.49.23.000000000 PM
  name: Permafrost microbial communities from Stordalen Mire, Sweden - 611E1M metaG
  ncbi_taxonomy_name: permafrost metagenome
  samp_name: 11E1M metaG
  sample_collection_site: Mire fen
  specific_ecosystem: Permafrost
  type: nmdc:Biosample
- add_date: 17-AUG-17 05.38.34.719000000 PM
  associated_studies:
  - nmdc:sty-00-8675309
  community: microbial communities
  description: Forest soil from Barre Woods Harvard Forest LTER site was incubated
    at 10C with heavy water. Sample is from a control plot at ambient soil temperature,
    organic horizon - top 4cm of soil
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: 'USA: Massachusetts'
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0157174
  habitat: soil
  id: nmdc:bsm-99-dge3H9
  lat_lon:
    has_raw_value: 42.481016 -72.178343
    latitude: 42.481016
    longitude: -72.178343
    type: nmdc:GeolocationValue
  location: Barre Woods Harvard Forest LTER site, Petersham, Massachusetts, United
    States
  mod_date: 08-JAN-20 02.49.23.000000000 PM
  name: Forest soil microbial communities from Barre Woods Harvard Forest LTER site,
    Petersham, Massachusetts, United States - Inc-BW-C-14-O
  ncbi_taxonomy_name: soil metagenome
  samp_name: Inc-BW-C-14-O
  sample_collection_site: forest soil
  specific_ecosystem: Forest Soil
  type: nmdc:Biosample
- add_date: 29-MAR-18 01.27.40.709000000 PM
  associated_studies:
  - nmdc:sty-00-8675309
  community: microbial communities
  description: Rhizosphere microbial communities from Carex aquatilis grown in submerged
    peat from a thermokarst bog, University of Washington, Seatle, WA, United States
  ecosystem: Host-associated
  ecosystem_category: Plants
  ecosystem_subtype: Soil
  ecosystem_type: Rhizosphere
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: 'USA: Seattle, Washington'
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0188037
  habitat: rhizosphere
  host_name: Carex aquatilis
  id: nmdc:bsm-99-dc6tg6
  lat_lon:
    has_raw_value: 47.6516 -122.3045
    latitude: 47.6516
    longitude: -122.3045
    type: nmdc:GeolocationValue
  location: University of Washington, Seatle, WA, United States
  mod_date: 08-JAN-20 02.49.25.000000000 PM
  name: Rhizosphere microbial communities from Carex aquatilis grown in University
    of Washington, Seatle, WA, United States - 4-1-23 metaG
  ncbi_taxonomy_name: rhizosphere metagenome
  samp_name: 4-1-23 metaG
  sample_collection_site: Peat Soil
  specific_ecosystem: Unclassified
  type: nmdc:Biosample
data_generation_set:
- add_date: 17-AUG-17 05.08.38.451000000 PM
  alternative_identifiers:
  - gold:Gp0225767
  analyte_category: metagenome
  associated_studies:
  - nmdc:sty-00-31415
  description: Forest soil from Barre Woods Harvard Forest LTER site was incubated
    at 10C with heavy water. Sample is from a control plot at ambient soil temperature,
    organic horizon - top 4cm of soil
  has_input:
  - nmdc:bsm-00-yellow
  has_output:
  - nmdc:dobj-00-90125
  id: nmdc:dgns-99-9XUVVF
  mod_date: 16-OCT-20 02.04.01.374000000 AM
  name: Forest soil microbial communities from Barre Woods Harvard Forest LTER site,
    Petersham, Massachusetts, United States - Inc-BW-C-14-O
  ncbi_project_name: Forest soil microbial communities from Barre Woods Harvard Forest
    LTER site, Petersham, Massachusetts, United States - Inc-BW-C-14-O
  part_of:
  - nmdc:dgms-00-31415
  processing_institution: JGI
  type: nmdc:NucleotideSequencing
- add_date: 17-MAR-17 04.55.44.822000000 PM
  alternative_identifiers:
  - gold:Gp0208560
  analyte_category: metagenome
  associated_studies:
  - nmdc:sty-00-8675309
  description: Permafrost microbial communities from Stordalen Mire, Sweden
  has_input:
  - nmdc:bsm-00-green
  has_output:
  - nmdc:dobj-00-pizza
  id: nmdc:dgns-99-dk9vgI
  mod_date: 22-MAY-20 06.38.19.576000000 PM
  name: Permafrost microbial communities from Stordalen Mire, Sweden - 611E1M metaG
  ncbi_project_name: Permafrost microbial communities from Stordalen Mire, Sweden
    - 611E1M metaG
  processing_institution: JGI
  type: nmdc:NucleotideSequencing
- add_date: 29-MAR-18 01.27.30.036000000 PM
  alternative_identifiers:
  - gold:Gp0306221
  analyte_category: metagenome
  associated_studies:
  - nmdc:sty-00-avacado
  description: Rhizosphere microbial communities from Carex aquatilis grown in submerged
    peat from a thermokarst bog, University of Washington, Seatle, WA, United States
  has_input:
  - nmdc:bsm-00-blue
  has_output:
  - nmdc:dobj-00-mobydick
  id: nmdc:dgns-99-MVW1FV
  mod_date: 04-APR-20 08.26.35.067000000 AM
  name: Rhizosphere microbial communities from Carex aquatilis grown in University
    of Washington, Seatle, WA, United States - 4-1-23 metaG
  ncbi_project_name: Rhizosphere microbial communities from Carex aquatilis grown
    in University of Washington, Seatle, WA, United States - 4-1-23 metaG
  processing_institution: JGI
  type: nmdc:NucleotideSequencing
data_object_set:
- description: Raw sequencer read data
  file_size_bytes: 9208349052
  id: nmdc:dobj-99-dkJ8xX
  name: 11340.8.202049.GTCTCCT-AAGGAGA.fastq.gz
  type: nmdc:DataObject
- description: Raw sequencer read data
  file_size_bytes: 34243309819
  id: nmdc:dobj-99-7zrm55
  name: 11839.4.222578.GAGCTCA-TTGAGCT.fastq.gz
  type: nmdc:DataObject
- description: Raw sequencer read data
  file_size_bytes: 7580035314
  id: nmdc:dobj-99-sQQw0I
  name: 12660.4.274923.GATCGTAC-GTACGATC.fastq.gz
  type: nmdc:DataObject
study_set:
- associated_dois:
  - doi_category: dataset_doi
    doi_provider: osti
    doi_value: doi:10.25585/1488217
    type: nmdc:Doi
  description: Thawing permafrost is one of the largest soil carbon pools on the planet.
    The goal of this project is to study microbial communities that participate in
    the soil carbon cycle.
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Wetlands
  ecosystem_type: Soil
  gold_study_identifiers:
  - gold:Gs123456789
  id: nmdc:sty-99-FkQIsc
  name: Permafrost microbial communities from Stordalen Mire, Sweden
  principal_investigator:
    has_raw_value: Virginia Rich
    type: nmdc:PersonValue
  specific_ecosystem: Permafrost
  study_category: research_study
  type: nmdc:Study
- associated_dois:
  - doi_category: dataset_doi
    doi_provider: osti
    doi_value: doi:10.25585/1488215
    type: nmdc:Doi
  description: The goal of this study is to learn the molecular mechanisms underlying
    changes in the temperature sensitive respiration response of forest soils to long-term
    experimental warming
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  gold_study_identifiers:
  - gold:Gs121212
  id: nmdc:sty-99-oJmAOs
  name: Forest soil microbial communities from Barre Woods Harvard Forest LTER site,
    Petersham, Massachusetts, United States
  principal_investigator:
    has_raw_value: Jeffrey Blanchard
    type: nmdc:PersonValue
  specific_ecosystem: Forest Soil
  study_category: consortium
  type: nmdc:Study
- associated_dois:
  - doi_category: dataset_doi
    doi_provider: osti
    doi_value: doi:10.25585/1488209
    type: nmdc:Doi
  description: The goal of this study is to advance understanding of the response
    of methane production and methane oxidation to changes in plant productivity so
    that modeled representations of these processes and interactions can be improved.
  ecosystem: Host-associated
  ecosystem_category: Plants
  ecosystem_subtype: Rhizosphere
  ecosystem_type: Roots
  gold_study_identifiers:
  - gold:Gs0134277
  id: nmdc:sty-99-3bQQ4j
  name: Rhizosphere microbial communities from Carex aquatilis grown in University
    of Washington, Seatle, WA, United States
  principal_investigator:
    has_raw_value: Rebecca Neumann
    type: nmdc:PersonValue
  specific_ecosystem: Soil
  study_category: research_study
  type: nmdc:Study

```
## Database-study-set-with-consortia-and-parents
### Input
```yaml
study_set:
- description: The parent consortium of all the NEON consortia
  id: nmdc:sty-11-34xj1152
  name: NEON Parent Consortium
  study_category: consortium
  type: nmdc:Study
- description: The National Science Foundation's National Ecological Observatory Network
    (NEON) is a continental-scale observation facility operated by Battelle and designed
    to collect long-term open access ecological data to better understand how U.S.
    ecosystems are changing.
  funding_sources:
  - 'NSF#1724433 National Ecological Observatory Network: Operations Activities'
  gold_study_identifiers:
  - gold:Gs0144570
  - gold:Gs0161344
  id: nmdc:sty-11-34xj1150
  name: 'National Ecological Observatory Network: soil metagenomes (DP1.10107.001)'
  part_of:
  - nmdc:sty-11-34xj1152
  principal_investigator:
    email: kthibault@battelleecology.org
    has_raw_value: Kate Thibault
    name: Kate Thibault
    orcid: orcid:0000-0003-3477-6424
    profile_image_url: https://portal.nersc.gov/project/m3408/profile_images/thibault_katy.jpg
    type: nmdc:PersonValue
  study_category: consortium
  study_image:
  - type: nmdc:ImageValue
    url: https://portal.nersc.gov/project/m3408/profile_images/nmdc_sty-11-34xj1150.jpg
  title: 'National Ecological Observatory Network: soil metagenomes (DP1.10107.001)'
  type: nmdc:Study
  websites:
  - https://www.neonscience.org/
  - https://data.neonscience.org/data-products/DP1.10107.001
  - https://data.neonscience.org/api/v0/documents/NEON.DOC.014048vO
  - https://data.neonscience.org/api/v0/documents/NEON_metagenomes_userGuide_vE.pdf
- description: The National Science Foundation's National Ecological Observatory Network
    (NEON) is a continental-scale observation facility operated by Battelle and designed
    to collect long-term open access ecological data to better understand how U.S.
    ecosystems are changing.
  funding_sources:
  - 'NSF#1724433 National Ecological Observatory Network: Operations Activities'
  id: nmdc:sty-11-hht5sb92
  name: 'National Ecological Observatory Network: surface water metagenomes (DP1.20281.001)'
  part_of:
  - nmdc:sty-11-34xj1152
  principal_investigator:
    email: kthibault@battelleecology.org
    has_raw_value: Kate Thibault
    name: Kate Thibault
    orcid: orcid:0000-0003-3477-6424
    type: nmdc:PersonValue
  study_category: consortium
  study_image:
  - type: nmdc:ImageValue
    url: https://portal.nersc.gov/project/m3408/profile_images/nmdc_sty-11-34xj1150.jpg
  title: 'National Ecological Observatory Network: surface water metagenomes (DP1.20281.001)'
  type: nmdc:Study
  websites:
  - https://www.neonscience.org/
  - https://data.neonscience.org/data-products/DP1.20281.001
  - https://data.neonscience.org/api/v0/documents/NEON_metagenomes_userGuide_vE.pdf
- description: The National Science Foundation's National Ecological Observatory Network
    (NEON) is a continental-scale observation facility operated by Battelle and designed
    to collect long-term open access ecological data to better understand how U.S.
    ecosystems are changing.
  funding_sources:
  - 'NSF#1724433 National Ecological Observatory Network: Operations Activities'
  id: nmdc:sty-11-pzmd0x14
  name: 'National Ecological Observatory Network: benthic metagenomes (DP1.20279.001)'
  part_of:
  - nmdc:sty-11-34xj1152
  principal_investigator:
    email: kthibault@battelleecology.org
    name: Kate Thibault
    orcid: orcid:0000-0003-3477-6424
    type: nmdc:PersonValue
  study_category: consortium
  study_image:
  - type: nmdc:ImageValue
    url: https://portal.nersc.gov/project/m3408/profile_images/nmdc_sty-11-34xj1150.jpg
  title: 'National Ecological Observatory Network: benthic metagenomes (DP1.20279.001)'
  type: nmdc:Study
  websites:
  - https://www.neonscience.org/
  - https://data.neonscience.org/data-products/DP1.20279.001
  - https://data.neonscience.org/api/v0/documents/NEON_metagenomes_userGuide_vE.pdf

```
## Biosample-embargoed
### Input
```yaml
associated_studies:
- nmdc:sty-00-abc123
embargoed: true
env_broad_scale:
  has_raw_value: ENVO:00002030
  term:
    id: ENVO:00002030
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_local_scale:
  has_raw_value: ENVO:00002169
  term:
    id: ENVO:00002169
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_medium:
  has_raw_value: ENVO:00005792
  term:
    id: ENVO:00005792
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
id: nmdc:bsm-99-dtTMNb
type: nmdc:Biosample

```
## Database-polymorphic-planned-process-set
### Input
```yaml
planned_process_set:
- id: nmdc:poolp-00-123456
  type: nmdc:Pooling
- has_input:
  - nmdc:bsm-00-435737
  has_output:
  - nmdc:procsm-00-0938548
  id: nmdc:extrp-00-999999
  type: nmdc:Extraction
- has_input:
  - nmdc:procsm-00-0938548
  has_output:
  - nmdc:procsm-00-sdsdll
  id: nmdc:libprp-00-999999
  type: nmdc:LibraryPreparation

```
## Database-mags
### Input
```yaml
mags_set:
- binned_contig_num: 489
  ended_at_time: '2021-01-10T00:00:00+00:00'
  execution_resource: NERSC-Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:0a3d00715d01ad7b8f3aee59b674dfe9
  - nmdc:668d207be5ea844f988fbfb2813564cc
  - nmdc:b7e9c8d0bffdd13ace6f862a61fa87d2
  has_output:
  - nmdc:818f5a47d1371295f9313909ea12eb50
  - nmdc:e0b7421514f976cb7ad8c343cf3077a9
  - nmdc:a755bb87aded36aefbd8022506a793c7
  - nmdc:1346fe25b6ff22180eb3a51204e0b1fc
  id: nmdc:wfmag-99-5MiDJM
  img_identifiers:
  - img.taxon:3300062116
  input_contig_num: 169782
  low_depth_contig_num: 0
  mags_list:
  - bin_name: bins.1
    bin_quality: LQ
    completeness: 11.42
    contamination: 0.21
    gene_count: 250
    num_16s: 0
    num_23s: 0
    num_5s: 1
    num_t_rna: 1
    number_of_contig: 52
    type: nmdc:MagBin
  - bin_name: bins.2
    bin_quality: LQ
    completeness: 51.25
    contamination: 10.34
    gene_count: 2548
    num_16s: 0
    num_23s: 0
    num_5s: 1
    num_t_rna: 26
    number_of_contig: 426
    type: nmdc:MagBin
  - bin_name: bins.3
    bin_quality: LQ
    completeness: 2
    contamination: 0
    gene_count: 294
    num_16s: 0
    num_23s: 0
    num_5s: 0
    num_t_rna: 1
    number_of_contig: 11
    type: nmdc:MagBin
  name: MAGs activiity 1781_86101
  part_of:
  - nmdc:wfch-11-ab
  started_at_time: '2021-01-10T00:00:00+00:00'
  too_short_contig_num: 159810
  type: nmdc:MagsAnalysis
  unbinned_contig_num: 9483
- binned_contig_num: 206
  ended_at_time: '2021-01-10T00:00:00+00:00'
  execution_resource: NERSC-Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:b78f599c21fb31b00d3f8a3c56daeb88
  - nmdc:662dc676b0b5a486248357f5b887c18b
  - nmdc:bc034c7024043ea88b44d0897bb5bece
  has_output:
  - nmdc:c24915651cfdfc91f3e6b5bac679c3af
  - nmdc:e8ec230bfe68a272b34540e7f5ab5b2b
  - nmdc:474fa29bd39452fa80f5a32e9e6be6f4
  - nmdc:9800add41d26829494265ba81a100c53
  id: nmdc:wfmag-99-VOgM5i
  input_contig_num: 78376
  low_depth_contig_num: 0
  mags_list:
  - bin_name: bins.1
    bin_quality: LQ
    completeness: 25.86
    contamination: 0
    gene_count: 401
    num_16s: 0
    num_23s: 0
    num_5s: 0
    num_t_rna: 4
    number_of_contig: 74
    type: nmdc:MagBin
  - bin_name: bins.2
    bin_quality: LQ
    completeness: 0
    contamination: 0
    gene_count: 383
    num_16s: 0
    num_23s: 0
    num_5s: 0
    num_t_rna: 5
    number_of_contig: 74
    type: nmdc:MagBin
  - bin_name: bins.3
    bin_quality: LQ
    completeness: 17.61
    contamination: 0
    gene_count: 313
    num_16s: 0
    num_23s: 0
    num_5s: 0
    num_t_rna: 7
    number_of_contig: 58
    type: nmdc:MagBin
  name: MAGs activiity 1781_86089
  part_of:
  - nmdc:wfch-12-ab
  started_at_time: '2021-01-10T00:00:00+00:00'
  too_short_contig_num: 75364
  type: nmdc:MagsAnalysis
  unbinned_contig_num: 2806

```
## Database-biosamples-infiltrations
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-dtTMNb
  infiltrations:
  - 00:01:32
  - 00:00:53
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-abcdef
  infiltrations:
  - 00:02:54
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-qwerty
  infiltrations:
  - 01:24:03
  - 00:02:33
  - 00:02:02
  type: nmdc:Biosample

```
## ChemicalConversionProcess-minimal
### Input
```yaml
chemical_conversion_category: acid_base
duration:
  has_numeric_value: 1
  has_unit: h
  type: nmdc:QuantityValue
has_input:
- nmdc:fasp-37
has_output:
- nmdc:ome-39
id: nmdc:chcpr-19-789
substances_used:
- final_concentration:
    has_numeric_value: 10
    has_unit: mM
    type: nmdc:QuantityValue
  known_as: nmdc:chem-99-000003
  sample_state_information: liquid
  type: nmdc:PortionOfSubstance
  volume:
    has_numeric_value: 120
    has_unit: mL
    type: nmdc:QuantityValue
temperature:
  has_numeric_value: 25
  has_unit: Cel
  type: nmdc:QuantityValue
type: nmdc:ChemicalConversionProcess

```
## Database-processed_sample-extract-exhaustive
### Input
```yaml
processed_sample_set:
- biomaterial_purity:
    has_numeric_value: 2
    type: nmdc:QuantityValue
  description: Extracted DNA from WOOD_024-M-20190715-COMP
  external_database_identifiers:
  - neon.identifier:19S_31_2826
  id: nmdc:procsm-99-dtTMNb
  name: WOOD_024-M-20190715-COMP-DNA1
  type: nmdc:ProcessedSample

```
## Extraction-NEON
### Input
```yaml
end_date: '2021-08-19'
extraction_target: DNA
has_input:
- nmdc:procsm-11-9gjxns61
has_output:
- nmdc:procsm-11-0wxpzf07
id: nmdc:extrp-11-00r2pk65
input_mass:
  has_numeric_value: 0.25
  has_unit: g
  type: nmdc:QuantityValue
name: extraction of sample 123
processing_institution: Battelle
qc_status: pass
start_date: 2020-06-24T22:06Z
type: nmdc:Extraction

```
## DataObject-mass_spec
### Input
```yaml
data_object_type: LC-DDA-MS/MS Raw Data
description: raw instrument file for nmdc:dgms-11-bn8jcq58
file_size_bytes: 1150434379
id: nmdc:dobj-12-bxzqgh77
md5_checksum: 3EFB4966125DFA9329ADE5B18EADDA8E
name: SpruceW_P19_15_22Jun17_Pippin_17-04-06
type: nmdc:DataObject
url: https://nmdcdemo.emsl.pnnl.gov/proteomics/raw/SpruceW_P19_15_22Jun17_Pippin_17-04-06.raw

```
## Database-nom_analysis_set
### Input
```yaml
nom_analysis_set:
- ended_at_time: '2018-11-13T20:20:39+00:00'
  execution_resource: EMSL-RZR
  git_url: xxx
  has_input:
  - nmdc:1
  - nmdc:2
  has_output:
  - nmdc:3
  - nmdc:4
  id: nmdc:wfnom-99-abcdefg
  part_of:
  - nmdc:wfch-99-abcdefg
  started_at_time: '2018-11-13T20:20:39+00:00'
  type: nmdc:NomAnalysis

```
## Biosample-soil_horizon
### Input
```yaml
associated_studies:
- nmdc:sty-00-abc123
env_broad_scale:
  has_raw_value: ENVO:00002030
  term:
    id: ENVO:00002030
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_local_scale:
  has_raw_value: ENVO:00002169
  term:
    id: ENVO:00002169
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_medium:
  has_raw_value: ENVO:00005792
  term:
    id: ENVO:00005792
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
id: nmdc:bsm-99-dtTMNb
soil_horizon: M horizon
type: nmdc:Biosample

```
## MetabolomicsAnalysis-1
### Input
```yaml
ended_at_time: '2021-09-15T10:13:20+00:00'
execution_resource: NERSC-Cori
git_url: https://example.org/WorkflowExecutionActivity
has_input:
- nmdc:i1
- nmdc:i2
has_output:
- nmdc:o1
- nmdc:o2
id: nmdc:wfmb-99-ABCDEF
part_of:
- nmdc:wfch-11-ab
started_at_time: '2021-08-05T14:48:51+00:00'
type: nmdc:MetabolomicsAnalysis

```
## SubSamplingProcess-minimal
### Input
```yaml
contained_in: v-bottom_conical_tube
container_size:
  has_numeric_value: 50
  has_unit: mL
  type: nmdc:QuantityValue
has_input:
- nmdc:bsm-99-oW43DzG1
has_output:
- nmdc:procsm-11-05g48p90
id: nmdc:subspr-99-oW43DzG0
mass:
  has_numeric_value: 30
  has_unit: g
  type: nmdc:QuantityValue
temperature:
  has_numeric_value: 25
  has_unit: C
  type: nmdc:QuantityValue
type: nmdc:SubSamplingProcess
volume:
  has_numeric_value: 20
  has_unit: mL
  type: nmdc:QuantityValue

```
## Database-neon-story
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-abcdef1
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-abcdef2
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-abcdef3
  type: nmdc:Biosample
extraction_set:
- end_date: '2021-01-15'
  extraction_target: DNA
  has_input:
  - nmdc:procsm-99-pooled
  has_output:
  - nmdc:procsm-99-extract
  id: nmdc:extrp-99-abcdef
  name: first dna extraction set
  start_date: '2021-01-15'
  type: nmdc:Extraction
library_preparation_set:
- end_date: '2021-01-15'
  has_input:
  - nmdc:procsm-99-extract
  has_output:
  - nmdc:procsm-99-library
  id: nmdc:libprp-99-abcdef
  library_type: DNA
  name: DNA library preparation of NEON sample TREE_001-O-20170707-COMP-DNA1
  start_date: '2021-01-15'
  type: nmdc:LibraryPreparation
pooling_set:
- alternative_identifiers:
  - generic:ps1_alt_id
  description: This is the first pooling process that has ever occurred on earth
  end_date: '2021-01-14'
  has_input:
  - nmdc:bsm-99-abcdef1
  - nmdc:bsm-99-abcdef2
  - nmdc:bsm-99-abcdef3
  has_output:
  - nmdc:procsm-99-pooled
  id: nmdc:poolp-99-abcdef
  name: first pooling process
  start_date: '2021-01-14'
  type: nmdc:Pooling
processed_sample_set:
- id: nmdc:procsm-99-xyz1
  name: first processed sample set
  type: nmdc:ProcessedSample
- id: nmdc:procsm-99-xyz2
  name: first DNA extract
  type: nmdc:ProcessedSample
- id: nmdc:procsm-99-xyz3
  name: first library
  type: nmdc:ProcessedSample

```
## Study-minimal
### Input
```yaml
id: nmdc:sty-11-ab
study_category: research_study
type: nmdc:Study

```
## Database-biosamples-dna-in-plate-valid-well-val
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  dna_cont_type: plate
  dna_cont_well: B2
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-dtTMNb
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  dna_cont_type: plate
  dna_cont_well: A10
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-000001
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  dna_cont_type: plate
  dna_cont_well: A11
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-000002
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  dna_cont_type: plate
  dna_cont_well: H10
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-000003
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  dna_cont_type: plate
  dna_cont_well: H11
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-000004
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  dna_cont_type: plate
  dna_cont_well: C1
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-000005
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  dna_cont_type: plate
  dna_cont_well: C12
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-000006
  type: nmdc:Biosample

```
## Study-exhaustive
### Input
```yaml
alternative_descriptions:
- any string 1
- any string 2
alternative_identifiers:
- generic:abc1
alternative_names:
- any string 1
- any string 2
alternative_titles:
- any string 1
- any string 2
associated_dois:
- doi_category: publication_doi
  doi_value: doi:10.1126/science.1058040
  type: nmdc:Doi
- doi_category: dataset_doi
  doi_provider: kbase
  doi_value: doi:10.1126/science.1456956
  type: nmdc:Doi
- doi_category: award_doi
  doi_provider: jgi
  doi_value: doi:10.1126/science.1234545
  type: nmdc:Doi
- doi_category: data_management_plan_doi
  doi_provider: gsc
  doi_value: doi:10.48321/D1Z60Q
  type: nmdc:Doi
description: see also name, title, objective, various alternatives
ecosystem: unconstrained text. should be validated against the controlled vocabulary,
  by the sample's environmental package. would also be nice to align the CV with MIxS
  environmental triads
ecosystem_category: unconstrained text
ecosystem_subtype: unconstrained text
ecosystem_type: unconstrained text
funding_sources:
- any string 1
- any string 2
gold_study_identifiers:
- gold:Gs12345
- gold:Gs90909
has_credit_associations:
- applied_roles:
  - Supervision
  - Conceptualization
  - Funding acquisition
  applies_to_person:
    email: jcventer@jcvi.org
    has_raw_value: Craig Venter
    name: J. Craig Venter
    orcid: ORCID:0000-0002-7086-765X
    profile_image_url: https://en.wikipedia.org/wiki/Craig_Venter#/media/File:Craigventer2.jpg
    type: nmdc:PersonValue
    was_generated_by: nmdc:any_string_1
    websites:
    - https://www.jcvi.org/
    - https://www.jcvi.org/about/j-craig-venter
  type: prov:Association
- applied_roles:
  - Investigation
  - Supervision
  applies_to_person:
    name: Tanja Davidsen
    type: nmdc:PersonValue
  type: prov:Association
homepage_website:
- https://www.neonscience.org/
id: nmdc:sty-11-ab
mgnify_project_identifiers:
- mgnify.proj:ABC123
name: see also description, title, objective, various alternatives
objective: This record, an instance of class Study from the nmdc-schema was had authored,
  so that the NMDC team would have at least one instance, using all slots, with a
  mixture of reasonable values and minimally compliant values.
part_of:
- nmdc:sty-11-34xj1157
principal_investigator:
  email: jcventer@jcvi.org
  has_raw_value: Craig Venter
  name: J. Craig Venter
  orcid: ORCID:0000-0002-7086-765X
  profile_image_url: https://en.wikipedia.org/wiki/Craig_Venter#/media/File:Craigventer2.jpg
  type: nmdc:PersonValue
  was_generated_by: nmdc:any_string_1
  websites:
  - https://www.jcvi.org/
  - https://www.jcvi.org/about/j-craig-venter
related_identifiers: any string R1
specific_ecosystem: unconstrained text
study_category: research_study
title: Sample Exhaustive Biosample instance. Although all of these values should pass
  validation, that does not mean that any Biosample of any type would necessarily
  have this particular combination of values.
type: nmdc:Study
websites:
- https://w3id.org/nmdc
- https://w3id.org/linkml

```
## DataObject-1
### Input
```yaml
description: Metagenome Contig Coverage Stats for gold:Gp0061273
file_size_bytes: 32787380
id: nmdc:dobj-99-izwYW6
name: mapping_stats.txt
type: nmdc:DataObject

```
## Extraction-proteomics
### Input
```yaml
has_input:
- nmdc:procsm-37
has_output:
- nmdc:procsm-39
id: nmdc:extrp-38-r2pk
substances_used:
- known_as: nmdc:chem-99-000005
  type: nmdc:PortionOfSubstance
- known_as: nmdc:chem-99-000002
  type: nmdc:PortionOfSubstance
- final_concentration:
    has_numeric_value: 0.05
    has_unit: "\u03BCg/\u03BCL"
    type: nmdc:QuantityValue
  known_as: nmdc:chem-99-000014
  type: nmdc:PortionOfSubstance
type: nmdc:Extraction

```
## Extraction-metabolomics
### Input
```yaml
has_input:
- nmdc:bsm-6
has_output:
- nmdc:psm-8
id: nmdc:extrp-71-r2pk
substances_used:
- known_as: nmdc:chem-99-000005
  type: nmdc:PortionOfSubstance
- final_concentration:
    has_numeric_value: 5
    has_unit: '%'
    type: nmdc:QuantityValue
  known_as: nmdc:chem-99-000003
  type: nmdc:PortionOfSubstance
type: nmdc:Extraction

```
## Database-biosamples-rna-in-plate-valid-well-val
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-dtTMNb
  rna_cont_type: plate
  rna_cont_well: B2
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-000001
  rna_cont_type: plate
  rna_cont_well: A10
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-000002
  rna_cont_type: plate
  rna_cont_well: A11
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-000003
  rna_cont_type: plate
  rna_cont_well: H10
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-000004
  rna_cont_type: plate
  rna_cont_well: H11
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-000005
  rna_cont_type: plate
  rna_cont_well: C1
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-000006
  rna_cont_type: plate
  rna_cont_well: C12
  type: nmdc:Biosample

```
## ChemicalEntity-1
### Input
```yaml
alternative_identifiers:
- wd:Q37525
chemical_formula: C6H12O6
description: generally considered the most abundant monosaccharide in nature
id: nmdc:chem-99-000001
inchi: 1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5-,6?/m1/s1
inchi_key: WQZGKKKJIJFFOK-GASJEMHNSA-N
name: glucose
smiles:
- OC[C@H]1OC(O)[C@H](O)[C@@H](O)[C@@H]1O
- C([C@@H]1[C@H]([C@@H]([C@H]([C@H](O1)O)O)O)O)O
type: nmdc:ChemicalEntity

```
## DissolvingProcess-minimal
### Input
```yaml
duration:
  has_numeric_value: 2
  has_unit: hours
  type: nmdc:QuantityValue
has_input:
- nmdc:bsm-12-A67
has_output:
- nmdc:procsm-13-S67F
id: nmdc:dispro-11-A74
instrument_used:
- nmdc:inst-12-124
substances_used:
- final_concentration:
    has_numeric_value: 15
    has_unit: mM
    type: nmdc:QuantityValue
  known_as: nmdc:chem-99-000015
  type: nmdc:PortionOfSubstance
  volume:
    has_numeric_value: 500
    has_unit: mL
    type: nmdc:QuantityValue
- known_as: nmdc:chem-99-000006
  substance_role: solubilizing_agent
  type: nmdc:PortionOfSubstance
type: nmdc:DissolvingProcess

```
## Database-biosamples-sites
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-99-U21mUX
  collected_from: nmdc:frsite-99-SPreao
  description: Root microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  gold_biosample_identifiers:
  - gold:Gb0305833
  id: nmdc:bsm-99-J9FcnC
  name: Root microbial communities from poplar common garden site in Clatskanie, Oregon,
    USA - BESC-13-CL1_35_33 endosphere
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-99-U21mUX
  collected_from: nmdc:frsite-99-SPreao
  description: Rhizosphere soil microbial communities from poplar common garden site
    in Clatskanie, Oregon, USA
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  gold_biosample_identifiers:
  - gold:Gb0291692
  id: nmdc:bsm-99-BdlWdQ
  name: Rhizosphere soil microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA - BESC-13-CL1_35_33
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-99-U21mUX
  collected_from: nmdc:frsite-99-SPreao
  description: Bulk soil microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  gold_biosample_identifiers:
  - gold:Gb0291582
  id: nmdc:bsm-99-vn74Wq
  name: Bulk soil microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA - BESC-13-CL1_35_33
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-99-U21mUX
  collected_from: nmdc:frsite-99-h2mYFG
  description: Root microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  gold_biosample_identifiers:
  - gold:Gb0305834
  id: nmdc:bsm-99-P8FdpS
  name: Root microbial communities from poplar common garden site in Clatskanie, Oregon,
    USA - BESC-13-CL2_39_29 endosphere
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-99-U21mUX
  collected_from: nmdc:frsite-99-h2mYFG
  description: Rhizosphere soil microbial communities from poplar common garden site
    in Clatskanie, Oregon, USA
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  gold_biosample_identifiers:
  - gold:Gb0291693
  id: nmdc:bsm-99-ugBwz3
  name: Rhizosphere soil microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA - BESC-13-CL2_39_29
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-99-U21mUX
  collected_from: nmdc:frsite-99-h2mYFG
  description: Bulk soil microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  gold_biosample_identifiers:
  - gold:Gb0291583
  id: nmdc:bsm-99-tN5lxM
  name: Bulk soil microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA - BESC-13-CL2_39_29
  type: nmdc:Biosample
collecting_biosamples_from_site_set:
- has_input:
  - nmdc:frsite-99-SPreao
  has_output:
  - nmdc:bsm-99-J9FcnC
  - nmdc:bsm-99-BdlWdQ
  - nmdc:bsm-99-vn74Wq
  id: nmdc:clsite-99-Cq00d1
  name: Collection of biosamples from BESC-13-CL1_35_33
  type: nmdc:CollectingBiosamplesFromSite
- has_input:
  - nmdc:frsite-99-h2mYFG
  has_output:
  - nmdc:bsm-99-P8FdpS
  - nmdc:bsm-99-ugBwz3
  - nmdc:bsm-99-tN5lxM
  id: nmdc:clsite-99-yzmLBN
  name: Collection of biosamples from BESC-13-CL2_39_29
  type: nmdc:CollectingBiosamplesFromSite
field_research_site_set:
- description: Bioscales tree BESC-13-CL1_35_33
  id: nmdc:frsite-99-SPreao
  name: BESC-13-CL1_35_33
  type: nmdc:FieldResearchSite
- description: Bioscales tree BESC-13-CL2_39_29
  id: nmdc:frsite-99-h2mYFG
  name: BESC-13-CL2_39_29
  type: nmdc:FieldResearchSite

```
## Database-instrument_set
### Input
```yaml
instrument_set:
- id: nmdc:inst-12-dtTMNb
  model: novaseq_6000
  name: Illumina NovaSeq
  type: nmdc:Instrument
  vendor: illumina
- id: nmdc:inst-12-dtTMN3
  model: exploris_480
  name: my favorite Orbitrap
  type: nmdc:Instrument

```
## FunctionalAnnotation-minimal
### Input
```yaml
has_function: KEGG_PATHWAY:abc12345
type: nmdc:FunctionalAnnotation

```
## DataObject-exhaustive
### Input
```yaml
alternative_identifiers:
- prefix:value1
- prefix:value2
compression_type: any string
data_object_type: Crispr Terms
description: Crispr Terms for nmdc:ann0vx38
file_size_bytes: 1234
id: nmdc:dobj-11-dtTMNb
insdc_experiment_identifiers:
- insdc.sra:SRX0123456
- insdc.sra:ERX0123456
md5_checksum: 22afa3d49b73eaec2e9787a6b88fbdc3
name: Crispr Terms
type: nmdc:DataObject
url: http://example.com
was_generated_by: nmdc:invalid_id

```
## Biosample-minimal
### Input
```yaml
associated_studies:
- nmdc:sty-00-abc123
env_broad_scale:
  has_raw_value: ENVO:00002030
  term:
    id: ENVO:00002030
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_local_scale:
  has_raw_value: ENVO:00002169
  term:
    id: ENVO:00002169
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_medium:
  has_raw_value: ENVO:00005792
  term:
    id: ENVO:00005792
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
id: nmdc:bsm-99-dtTMNb
type: nmdc:Biosample

```
## Database-biosample-exhasutive
### Input
```yaml
biosample_set:
- abs_air_humidity:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  add_date: '2021-03-31'
  add_recov_method:
    has_raw_value: xxx
    type: nmdc:TextValue
  additional_info:
    has_raw_value: xxx
    type: nmdc:TextValue
  address:
    has_raw_value: xxx
    type: nmdc:TextValue
  adj_room:
    has_raw_value: xxx
    type: nmdc:TextValue
  aero_struc:
    has_raw_value: xxx
    type: nmdc:TextValue
  agrochem_addition:
  - has_raw_value: lime;1 kg/acre;2022-11-16T16:05:42+0000
    type: nmdc:TextValue
  air_PM_concen:
  - has_raw_value: xxx
    type: nmdc:TextValue
  air_temp:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  air_temp_regm:
  - has_raw_value: 25 degree Celsius;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    type: nmdc:TextValue
  al_sat:
    has_raw_value: 0.1 mg/kg
    type: nmdc:QuantityValue
  al_sat_meth:
    has_raw_value: https://journaljeai.com/index.php/JEAI/article/view/583
    type: nmdc:TextValue
  alkalinity:
    has_raw_value: 50 milligram per liter
    type: nmdc:QuantityValue
  alkalinity_method:
    has_raw_value: https://wrrc.umass.edu/research/projects/acid-rain-monitoring-project/analysis-method-ph-and-alkalinity
    type: nmdc:TextValue
  alkyl_diethers:
    has_raw_value: 0.005 mole per liter
    type: nmdc:QuantityValue
  alt:
    has_raw_value: 100 meter
    type: nmdc:QuantityValue
  alternative_identifiers:
  - generic:abc123
  aminopept_act:
    has_raw_value: 0.269 mole per liter per hour
    type: nmdc:QuantityValue
  ammonium:
    has_raw_value: 1.5 milligram per liter
    type: nmdc:QuantityValue
  ammonium_nitrogen:
    has_raw_value: 0.5 milligram per liter
    type: nmdc:QuantityValue
  amount_light:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  analysis_type:
  - metabolomics
  - metagenomics
  ances_data:
    has_raw_value: xxx
    type: nmdc:TextValue
  annual_precpt:
    has_raw_value: 0.5 milligram per liter
    type: nmdc:QuantityValue
  annual_temp:
    has_raw_value: 12.5 degree Celsius
    type: nmdc:QuantityValue
  antibiotic_regm:
  - has_raw_value: xxx
    type: nmdc:TextValue
  api:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  arch_struc: building
  aromatics_pc:
    has_raw_value: xxx
    type: nmdc:TextValue
  asphaltenes_pc:
    has_raw_value: xxx
    type: nmdc:TextValue
  associated_studies:
  - nmdc:sty-00-987654
  - nmdc:sty-00-qwerty
  atmospheric_data:
  - has_raw_value: xxx
    type: nmdc:TextValue
  avg_dew_point:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  avg_occup:
    has_raw_value: xxx
    type: nmdc:TextValue
  avg_temp:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  bac_prod:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  bac_resp:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  bacteria_carb_prod:
    has_raw_value: 2.53 microgram per liter per hour
    type: nmdc:QuantityValue
  barometric_press:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  basin:
    has_raw_value: xxx
    type: nmdc:TextValue
  bathroom_count:
    has_raw_value: xxx
    type: nmdc:TextValue
  bedroom_count:
    has_raw_value: xxx
    type: nmdc:TextValue
  benzene:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  biochem_oxygen_dem:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  biocide:
    has_raw_value: xxx
    type: nmdc:TextValue
  biocide_admin_method:
    has_raw_value: xxx
    type: nmdc:TextValue
  biol_stat: wild
  biomass:
  - has_raw_value: xxx
    type: nmdc:TextValue
  biosample_categories:
  - LTER
  - FICUS
  biotic_regm:
    has_raw_value: sample inoculated with Rhizobium spp. Culture
    type: nmdc:TextValue
  biotic_relationship: parasite
  bishomohopanol:
    has_raw_value: 14 microgram per liter
    type: nmdc:QuantityValue
  blood_press_diast:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  blood_press_syst:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  bromide:
    has_raw_value: 0.05 parts per million
    type: nmdc:QuantityValue
  build_docs: building information model
  build_occup_type:
  - office
  building_setting: urban
  built_struc_age:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  built_struc_set:
    has_raw_value: xxx
    type: nmdc:TextValue
  built_struc_type:
    has_raw_value: xxx
    type: nmdc:TextValue
  calcium:
    has_raw_value: 0.2 micromole per liter
    type: nmdc:QuantityValue
  carb_dioxide:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  carb_monoxide:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  carb_nitro_ratio:
    has_raw_value: '0.417361111'
    type: nmdc:QuantityValue
  ceil_area:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  ceil_cond: new
  ceil_finish_mat: drywall
  ceil_struc:
    has_raw_value: xxx
    type: nmdc:TextValue
  ceil_texture: crows feet
  ceil_thermal_mass:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  ceil_type: cathedral
  ceil_water_mold:
    has_raw_value: xxx
    type: nmdc:TextValue
  chem_administration:
  - has_raw_value: agar [CHEBI:2509];2018-05-11T20:00Z
    type: nmdc:ControlledTermValue
  chem_mutagen:
  - has_raw_value: xxx
    type: nmdc:TextValue
  chem_oxygen_dem:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  chem_treat_method: xxx
  chem_treatment:
    has_raw_value: xxx
    type: nmdc:TextValue
  chloride:
    has_raw_value: 5000 milligram per liter
    type: nmdc:QuantityValue
  chlorophyll:
    has_raw_value: 5 milligram per cubic meter
    type: nmdc:QuantityValue
  climate_environment:
  - has_raw_value: tropical climate;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    type: nmdc:TextValue
  collected_from: nmdc:unconstrained_site_identifier_string
  collection_date:
    has_raw_value: xxx
    type: nmdc:TimestampValue
  collection_date_inc: '2023-01-29'
  collection_time: 05:42+0000
  collection_time_inc: 13:42+0000
  community: no_example_from_mixs
  conduc:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  cool_syst_id:
    has_raw_value: xxx
    type: nmdc:TextValue
  crop_rotation:
    has_raw_value: yes;R2/2017-01-01/2018-12-31/P6M
    type: nmdc:TextValue
  cult_root_med:
    has_raw_value: xxx
    type: nmdc:TextValue
  cur_land_use: farmstead
  cur_vegetation:
    has_raw_value: MIxS doesn't provide any guidance more specific than "text"
    type: nmdc:TextValue
  cur_vegetation_meth:
    has_raw_value: https://link.springer.com/article/10.1023/A:1011975321668
    type: nmdc:TextValue
  date_last_rain:
    has_raw_value: xxx
    type: nmdc:TimestampValue
  density:
    has_raw_value: 1000 kilogram per cubic meter
    type: nmdc:QuantityValue
  depos_env: other
  depth:
    has_maximum_numeric_value: 2.5
    has_minimum_numeric_value: 1.5
    has_numeric_value: 2.0
    has_raw_value: 1.5 to 2.5 meters (that may not be the pattern the submission schema
      expects). Extractions below require external migration logic.
    has_unit: meter
    type: nmdc:QuantityValue
  description: unconstrained text
  dew_point:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  diether_lipids:
  - has_raw_value: xxx
    type: nmdc:TextValue
  diss_carb_dioxide:
    has_raw_value: 5 milligram per liter
    type: nmdc:QuantityValue
  diss_hydrogen:
    has_raw_value: 0.3 micromole per liter
    type: nmdc:QuantityValue
  diss_inorg_carb:
    has_raw_value: 2059 micromole per kilogram
    type: nmdc:QuantityValue
  diss_inorg_nitro:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  diss_inorg_phosp:
    has_raw_value: 56.5 micromole per liter
    type: nmdc:QuantityValue
  diss_iron:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  diss_org_carb:
    has_raw_value: 197 micromole per liter
    type: nmdc:QuantityValue
  diss_org_nitro:
    has_raw_value: 0.05 micromole per liter
    type: nmdc:QuantityValue
  diss_oxygen:
    has_raw_value: 175 micromole per kilogram
    type: nmdc:QuantityValue
  diss_oxygen_fluid:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  dna_absorb1: 2.02
  dna_absorb2: 2.02
  dna_collect_site: untreated pond water
  dna_concentration: 100.0
  dna_cont_type: plate
  dna_cont_well: C2
  dna_container_id: Pond_MT_041618
  dna_dnase: 'yes'
  dna_isolate_meth: DNA
  dna_organisms: expected to contain microbes (59%) fungi (30%), viruses (10%), tadpoles
    (1%)
  dna_project_contact: John Jones
  dna_samp_id: '187654'
  dna_sample_format: 10 mM Tris-HCl
  dna_sample_name: JGI_pond_041618
  dna_seq_project: '1191234'
  dna_seq_project_name: JGI Pond metagenomics
  dna_seq_project_pi: Jane Johnson
  dna_volume: 25.0
  dnase_rna: 'yes'
  door_comp_type: revolving
  door_cond: damaged
  door_direct: inward
  door_loc: north
  door_mat: aluminum
  door_move: collapsible
  door_size:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  door_type: composite
  door_type_metal: collapsible
  door_type_wood: battened
  door_water_mold:
    has_raw_value: xxx
    type: nmdc:TextValue
  down_par:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  drainage_class: well
  drawings: operation
  ecosystem: unconstrained text. should be validated against the controlled vocabulary,
    by the sample's environmental package. would also be nice to align the CV with
    MIxS environmental triads
  ecosystem_category: unconstrained text
  ecosystem_subtype: unconstrained text
  ecosystem_type: unconstrained text
  efficiency_percent:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  elev: 100.0
  elevator:
    has_raw_value: xxx
    type: nmdc:TextValue
  embargoed: true
  emsl_biosample_identifiers:
  - generic:abc123
  emulsions:
  - has_raw_value: xxx
    type: nmdc:TextValue
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_package:
    has_raw_value: unconstrained text. should require the name of a MIxS EnvironmentalPackage
      class. have asked MIxS to return this term to their model. UPDATE VALIDATION
      RULES/PATTERN/ENUM!
    type: nmdc:TextValue
  escalator:
    has_raw_value: xxx
    type: nmdc:TextValue
  ethylbenzene:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  exp_duct:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  exp_pipe:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  experimental_factor:
    has_raw_value: unconstrained text, unlike the MIxS environmental triad
    type: nmdc:ControlledTermValue
  experimental_factor_other: unconstrained text, but presumably expects 'term label
    [term id]'
  ext_door:
    has_raw_value: xxx
    type: nmdc:TextValue
  ext_wall_orient: north
  ext_window_orient: north
  extreme_event: '2023-01-15'
  fao_class: Fluvisols
  fertilizer_regm:
  - has_raw_value: xxx
    type: nmdc:TextValue
  field:
    has_raw_value: xxx
    type: nmdc:TextValue
  filter_method: Basix PES, 13-100-106 FisherSci is an example value, but unconstrained
    text is accepted at this point
  filter_type:
  - HEPA
  fire: 2000-11 to 2000-12
  fireplace_type:
    has_raw_value: xxx
    type: nmdc:TextValue
  flooding: '2000-01-15'
  floor_age:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  floor_area:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  floor_cond: new
  floor_count:
    has_raw_value: xxx
    type: nmdc:TextValue
  floor_finish_mat: tile
  floor_struc: balcony
  floor_thermal_mass:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  floor_water_mold: condensation
  fluor:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  freq_clean:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  freq_cook:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  fungicide_regm:
  - has_raw_value: xxx
    type: nmdc:TextValue
  furniture: cabinet
  gaseous_environment:
  - has_raw_value: nitric oxide;0.5 micromole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    type: nmdc:TextValue
  gaseous_substances:
  - has_raw_value: xxx
    type: nmdc:TextValue
  gender_restroom: female
  genetic_mod:
    has_raw_value: xxx
    type: nmdc:TextValue
  geo_loc_name:
    has_raw_value: 'USA: Maryland, Bethesda'
    type: nmdc:TextValue
  glucosidase_act:
    has_raw_value: 5 mol per liter per hour
    type: nmdc:QuantityValue
  gold_biosample_identifiers:
  - gold:Gb123456789
  - gold:Gb90909090
  gravidity:
    has_raw_value: xxx
    type: nmdc:TextValue
  gravity:
  - has_raw_value: xxx
    type: nmdc:TextValue
  growth_facil:
    has_raw_value: Growth chamber [CO_715:0000189]
    type: nmdc:ControlledTermValue
  growth_habit: erect
  growth_hormone_regm:
  - has_raw_value: xxx
    type: nmdc:TextValue
  habitat: unconstrained text
  hall_count:
    has_raw_value: xxx
    type: nmdc:TextValue
  handidness: ambidexterity
  hc_produced: Oil
  hcr: Shale
  hcr_fw_salinity:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  hcr_geol_age: Archean
  hcr_pressure:
    has_raw_value: xxx
    type: nmdc:TextValue
  hcr_temp:
    has_raw_value: xxx
    type: nmdc:TextValue
  heat_cool_type:
  - radiant system
  heat_deliv_loc: north
  heat_sys_deliv_meth: xxx
  heat_system_id:
    has_raw_value: xxx
    type: nmdc:TextValue
  heavy_metals:
  - has_raw_value: mercury;0.09 micrograms per gram
    type: nmdc:TextValue
  - has_raw_value: arsenic;0.09 micrograms per gram
    type: nmdc:TextValue
  heavy_metals_meth:
  - has_raw_value: https://link.springer.com/article/10.1007/s42452-019-1578-x
    type: nmdc:TextValue
  height_carper_fiber:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  herbicide_regm:
  - has_raw_value: xxx
    type: nmdc:TextValue
  horizon_meth:
    has_raw_value: xxx
    type: nmdc:TextValue
  host_age:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  host_body_habitat:
    has_raw_value: xxx
    type: nmdc:TextValue
  host_body_product:
    has_raw_value: xxx
    type: nmdc:ControlledTermValue
  host_body_site:
    has_raw_value: xxx
    type: nmdc:ControlledTermValue
  host_body_temp:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  host_color:
    has_raw_value: xxx
    type: nmdc:TextValue
  host_common_name:
    has_raw_value: xxx
    type: nmdc:TextValue
  host_diet:
  - has_raw_value: xxx
    type: nmdc:TextValue
  host_dry_mass:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  host_family_relation:
  - xxx
  host_genotype:
    has_raw_value: xxx
    type: nmdc:TextValue
  host_growth_cond:
    has_raw_value: xxx
    type: nmdc:TextValue
  host_height:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  host_last_meal:
  - has_raw_value: xxx
    type: nmdc:TextValue
  host_length:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  host_life_stage:
    has_raw_value: xxx
    type: nmdc:TextValue
  host_name: snail is an example value, but unconstrained text is accepted at this
    point
  host_phenotype:
    has_raw_value: xxx
    type: nmdc:ControlledTermValue
  host_sex: female
  host_shape:
    has_raw_value: xxx
    type: nmdc:TextValue
  host_subject_id:
    has_raw_value: xxx
    type: nmdc:TextValue
  host_subspecf_genlin:
  - xxx
  host_substrate:
    has_raw_value: xxx
    type: nmdc:TextValue
  host_symbiont:
  - xxx
  host_taxid:
    has_raw_value: NCBITaxon:9606
    term:
      id: NCBITaxon:9606
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  host_tot_mass:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  host_wet_mass:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  humidity:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  humidity_regm:
  - has_raw_value: 25 gram per cubic meter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    type: nmdc:TextValue
  id: nmdc:bsm-99-dtTMNb
  igsn_biosample_identifiers:
  - any:curie_1
  - any:curie_2
  img_identifiers:
  - img.taxon:abc123
  indoor_space: bedroom
  indoor_surf: cabinet
  indust_eff_percent:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  inorg_particles:
  - has_raw_value: xxx
    type: nmdc:TextValue
  insdc_biosample_identifiers:
  - biosample:SAMN123456789
  - biosample:SAMN000
  inside_lux:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  int_wall_cond: new
  isotope_exposure: 13C glucose
  iw_bt_date_well:
    has_raw_value: xxx
    type: nmdc:TimestampValue
  iwf:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  last_clean:
    has_raw_value: xxx
    type: nmdc:TimestampValue
  lat_lon:
    has_raw_value: 50.586825 6.408977
    latitude: 50.586825
    longitude: 6.408977
    type: nmdc:GeolocationValue
  lbc_thirty:
    has_raw_value: 543 mg/kg
    type: nmdc:QuantityValue
  lbceq:
    has_raw_value: 1575 mg/kg
    type: nmdc:QuantityValue
  light_intensity:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  light_regm:
    has_raw_value: incandescent light;10 lux;450 nanometer
    type: nmdc:TextValue
  light_type:
  - none
  link_addit_analys:
    has_raw_value: https://pubmed.ncbi.nlm.nih.gov/2315679/
    type: nmdc:TextValue
  link_class_info:
    has_raw_value: https://wisconsindot.gov/Documents/doing-bus/eng-consultants/cnslt-rsrces/geotechmanual/gt-03-03.pdf
    type: nmdc:TextValue
  link_climate_info:
    has_raw_value: https://www.int-res.com/abstracts/cr/v14/n3/p161-173/
    type: nmdc:TextValue
  lithology: Basement
  local_class:
    has_raw_value: jicama soil
    type: nmdc:TextValue
  local_class_meth:
    has_raw_value: https://www.sciencedirect.com/science/article/abs/pii/S0016706105003083
    type: nmdc:TextValue
  location: unconstrained text. should we even keep this slot? check if it has been
    used in MongoDB.
  magnesium:
    has_raw_value: 52.8 micromole per kilogram
    type: nmdc:QuantityValue
  manganese:
    has_raw_value: 24.7 mg/kg
    type: nmdc:QuantityValue
  max_occup:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  mean_frict_vel:
    has_raw_value: 0.5 meter per second
    type: nmdc:QuantityValue
  mean_peak_frict_vel:
    has_raw_value: 1 meter per second
    type: nmdc:QuantityValue
  mech_struc: subway
  mechanical_damage:
  - has_raw_value: xxx
    type: nmdc:TextValue
  methane:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  micro_biomass_c_meth: https://acsess.onlinelibrary.wiley.com/doi/abs/10.2136/sssaspecpub49.c12
  micro_biomass_meth: xxx
  micro_biomass_n_meth: https://acsess.onlinelibrary.wiley.com/doi/abs/10.2136/sssaspecpub49.c12
  microbial_biomass:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  microbial_biomass_c: 0.05 ug C/g dry soil
  microbial_biomass_n: 0.05 ug N/g dry soil
  mineral_nutr_regm:
  - has_raw_value: xxx
    type: nmdc:TextValue
  misc_param:
  - has_raw_value: Bicarbonate ion concentration;2075 micromole per kilogram
    type: nmdc:TextValue
  mod_date: '2023-01-25'
  n_alkanes:
  - has_raw_value: n-hexadecane;100 milligram per liter
    type: nmdc:TextValue
  name: Sample Exhaustive Biosample instance. Although all of these values should
    pass validation, that does not mean that any Biosample of any type would necessarily
    have this particular combination of values.
  ncbi_taxonomy_name: soil metagenome
  nitrate:
    has_raw_value: 65 micromole per liter
    type: nmdc:QuantityValue
  nitrite:
    has_raw_value: 0.5 micromole per liter
    type: nmdc:QuantityValue
  nitrite_nitrogen:
    has_raw_value: 1.2 mg/kg
    type: nmdc:QuantityValue
  nitro:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  non_microb_biomass: insect 0.23 ug; plant 1g
  non_microb_biomass_method: https://doi.org/10.1038/s41467-021-26181-3
  non_min_nutr_regm:
  - xxx
  number_pets:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  number_plants:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  number_resident:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  occup_density_samp:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  occup_document: estimate
  occup_samp:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  org_carb:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  org_count_qpcr_info: xxx
  org_matter:
    has_raw_value: 1.75 milligram per cubic meter
    type: nmdc:QuantityValue
  org_nitro:
    has_raw_value: 4 micromole per liter
    type: nmdc:QuantityValue
  org_nitro_method: https://doi.org/10.1016/0038-0717(85)90144-0
  org_particles:
  - has_raw_value: xxx
    type: nmdc:TextValue
  organism_count:
  - has_raw_value: ATP
    type: nmdc:QuantityValue
  other_treatment: unconstrained text
  owc_tvdss:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  oxy_stat_samp: aerobic
  oxygen:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  part_org_carb:
    has_raw_value: 1.92 micromole per liter
    type: nmdc:QuantityValue
  part_org_nitro:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  particle_class:
  - has_raw_value: xxx
    type: nmdc:TextValue
  permeability:
    has_raw_value: xxx
    type: nmdc:TextValue
  perturbation:
  - has_raw_value: antibiotic addition;R2/2018-05-11T14:30Z/2018-05-11T19:30Z/P1H30M
    type: nmdc:TextValue
  pesticide_regm:
  - has_raw_value: xxx
    type: nmdc:TextValue
  petroleum_hydrocarb:
    has_raw_value: 0.05 micromole per liter
    type: nmdc:QuantityValue
  ph: 99.99
  ph_meth:
    has_raw_value: https://www.epa.gov/sites/production/files/2015-12/documents/9040c.pdf
    type: nmdc:TextValue
  ph_regm:
  - has_raw_value: xxx
    type: nmdc:TextValue
  phaeopigments:
  - has_raw_value: 2.5 milligram per cubic meter
    type: nmdc:TextValue
  phosphate:
    has_raw_value: 0.7 micromole per liter
    type: nmdc:QuantityValue
  phosplipid_fatt_acid:
  - has_raw_value: 2.98 milligram per liter
    type: nmdc:TextValue
  photon_flux:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  plant_growth_med:
    has_raw_value: xxx
    type: nmdc:ControlledTermValue
  plant_product:
    has_raw_value: xxx
    type: nmdc:TextValue
  plant_sex: Androdioecious
  plant_struc:
    has_raw_value: xxx
    type: nmdc:ControlledTermValue
  pollutants:
  - has_raw_value: xxx
    type: nmdc:TextValue
  porosity:
    has_raw_value: xxx
    type: nmdc:TextValue
  potassium:
    has_raw_value: 463 milligram per liter
    type: nmdc:QuantityValue
  pour_point:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  pre_treatment:
    has_raw_value: xxx
    type: nmdc:TextValue
  pres_animal_insect: cat;3
  pressure:
    has_raw_value: 50 atmosphere
    type: nmdc:QuantityValue
  prev_land_use_meth: xxx
  previous_land_use:
    has_raw_value: xxx
    type: nmdc:TextValue
  primary_prod:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  primary_treatment:
    has_raw_value: xxx
    type: nmdc:TextValue
  prod_rate:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  prod_start_date:
    has_raw_value: xxx
    type: nmdc:TimestampValue
  profile_position: summit
  project_id: no example from MIxS
  proport_woa_temperature: no example from MIxS
  proposal_dna: '504000'
  proposal_rna: '504000'
  quad_pos: North side
  radiation_regm:
  - has_raw_value: xxx
    type: nmdc:TextValue
  rainfall_regm:
  - has_raw_value: xxx
    type: nmdc:TextValue
  reactor_type:
    has_raw_value: xxx
    type: nmdc:TextValue
  redox_potential:
    has_raw_value: 300 millivolt
    type: nmdc:QuantityValue
  rel_air_humidity:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  rel_humidity_out:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  rel_samp_loc: edge of car
  replicate_number: '1'
  reservoir:
    has_raw_value: xxx
    type: nmdc:TextValue
  resins_pc:
    has_raw_value: xxx
    type: nmdc:TextValue
  rna_absorb1: 2.02
  rna_absorb2: 2.02
  rna_collect_site: untreated pond water
  rna_concentration: 100.0
  rna_cont_type: plate
  rna_cont_well: C2
  rna_container_id: Pond_MT_041618
  rna_isolate_meth: RNA
  rna_organisms: expected to contain microbes (59%) fungi (30%), viruses (10%), tadpoles
    (1%)
  rna_project_contact: John Jones
  rna_samp_id: '187654'
  rna_sample_format: 10 mM Tris-HCl
  rna_sample_name: JGI_pond_041618
  rna_seq_project: '1191234'
  rna_seq_project_name: JGI Pond metagenomics
  rna_seq_project_pi: Jane Johnson
  rna_volume: 25.0
  room_air_exch_rate:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  room_architec_elem: xxx
  room_condt: new
  room_connected: attic
  room_count:
    has_raw_value: xxx
    type: nmdc:TextValue
  room_dim:
    has_raw_value: xxx
    type: nmdc:TextValue
  room_door_dist:
    has_raw_value: xxx
    type: nmdc:TextValue
  room_door_share:
    has_raw_value: xxx
    type: nmdc:TextValue
  room_hallway:
    has_raw_value: xxx
    type: nmdc:TextValue
  room_loc: corner room
  room_moist_dam_hist: 123
  room_net_area:
    has_raw_value: xxx
    type: nmdc:TextValue
  room_occup:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  room_samp_pos: north corner
  room_type: attic
  room_vol:
    has_raw_value: xxx
    type: nmdc:TextValue
  room_wall_share:
    has_raw_value: xxx
    type: nmdc:TextValue
  room_window_count: 123
  root_cond:
    has_raw_value: xxx
    type: nmdc:TextValue
  root_med_carbon:
    has_raw_value: xxx
    type: nmdc:TextValue
  root_med_macronutr:
    has_raw_value: xxx
    type: nmdc:TextValue
  root_med_micronutr:
    has_raw_value: xxx
    type: nmdc:TextValue
  root_med_ph:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  root_med_regl:
    has_raw_value: xxx
    type: nmdc:TextValue
  root_med_solid:
    has_raw_value: xxx
    type: nmdc:TextValue
  root_med_suppl:
    has_raw_value: xxx
    type: nmdc:TextValue
  salinity:
    has_raw_value: 25 practical salinity unit
    type: nmdc:QuantityValue
  salinity_category: halotolerant is an example from the schema, but MIxS doesn't
    provide this slot any more
  salinity_meth:
    has_raw_value: PMID:22895776
    type: nmdc:TextValue
  salt_regm:
  - has_raw_value: xxx
    type: nmdc:TextValue
  samp_capt_status: other
  samp_collec_device: xxx
  samp_collec_method: swabbing
  samp_collect_point: well
  samp_dis_stage: dissemination
  samp_floor: basement
  samp_loc_corr_rate:
    has_raw_value: xxx
    type: nmdc:TextValue
  samp_mat_process:
    has_raw_value: filtering of seawater
    type: nmdc:ControlledTermValue
  samp_md:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  samp_name: see also name
  samp_preserv:
    has_raw_value: xxx
    type: nmdc:TextValue
  samp_room_id:
    has_raw_value: xxx
    type: nmdc:TextValue
  samp_size:
    has_raw_value: 5 liters
    type: nmdc:QuantityValue
  samp_sort_meth:
  - has_raw_value: xxx
    type: nmdc:TextValue
  samp_store_dur:
    has_raw_value: P1Y6M
    type: nmdc:TextValue
  samp_store_loc:
    has_raw_value: Freezer no:5
    type: nmdc:TextValue
  samp_store_temp:
    has_raw_value: -80 degree Celsius
    type: nmdc:QuantityValue
  samp_subtype: biofilm
  samp_taxon_id:
    has_raw_value: soil metagenome [NCBItaxon:410658]
    term:
      id: NCBItaxon:410658
      name: soil metagenome
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  samp_time_out:
    has_raw_value: xxx
    type: nmdc:TextValue
  samp_transport_cond:
    has_raw_value: xxx
    type: nmdc:TextValue
  samp_tvdss:
    has_raw_value: xxx
    type: nmdc:TextValue
  samp_type:
    has_raw_value: xxx
    type: nmdc:TextValue
  samp_weather: cloudy
  samp_well_name:
    has_raw_value: xxx
    type: nmdc:TextValue
  sample_collection_site: unconstrained text
  sample_link:
  - IGSN:DSJ0284
  - any:curie
  sample_shipped: 15 g
  sample_type: soil - water extract
  saturates_pc:
    has_raw_value: xxx
    type: nmdc:TextValue
  season:
    has_raw_value: xxx
    type: nmdc:TextValue
  season_environment:
  - has_raw_value: xxx
    type: nmdc:TextValue
  season_precpt:
    has_raw_value: 75 millimeters
    type: nmdc:QuantityValue
  season_temp:
    has_raw_value: 18 degree Celsius
    type: nmdc:QuantityValue
  season_use: Spring
  secondary_treatment:
    has_raw_value: xxx
    type: nmdc:TextValue
  sediment_type: biogenous
  sewage_type:
    has_raw_value: xxx
    type: nmdc:TextValue
  shad_dev_water_mold: xxx
  shading_device_cond: damaged
  shading_device_loc:
    has_raw_value: xxx
    type: nmdc:TextValue
  shading_device_mat:
    has_raw_value: xxx
    type: nmdc:TextValue
  shading_device_type: tree
  sieving:
    has_raw_value: MIxS does not provide an example
    type: nmdc:TextValue
  silicate:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  size_frac:
    has_raw_value: xxx
    type: nmdc:TextValue
  size_frac_low:
    has_raw_value: 0.2 micrometer
    type: nmdc:QuantityValue
  size_frac_up:
    has_raw_value: 20 micrometer
    type: nmdc:QuantityValue
  slope_aspect:
    has_raw_value: MIxS does not provide an example
    type: nmdc:QuantityValue
  slope_gradient:
    has_raw_value: MIxS does not provide an example
    type: nmdc:QuantityValue
  sludge_retent_time:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  sodium:
    has_raw_value: 10.5 milligram per liter
    type: nmdc:QuantityValue
  soil_horizon: O horizon
  soil_text_measure:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  soil_texture_meth: xxx
  soil_type:
    has_raw_value: plinthosol [ENVO:00002250]
    type: nmdc:TextValue
  soil_type_meth:
    has_raw_value: Frederick series
    type: nmdc:TextValue
  solar_irradiance:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  soluble_inorg_mat:
  - has_raw_value: xxx
    type: nmdc:TextValue
  soluble_iron_micromol: MIxS doesn't provide an example
  soluble_org_mat:
  - has_raw_value: xxx
    type: nmdc:TextValue
  soluble_react_phosp:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  source_mat_id:
    has_raw_value: MPI012345
    type: nmdc:TextValue
  space_typ_state:
    has_raw_value: xxx
    type: nmdc:TextValue
  specific: operation
  specific_ecosystem: unconstrained text
  specific_humidity:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  sr_dep_env: Lacustine
  sr_geol_age: Archean
  sr_kerog_type: other
  sr_lithology: Clastic
  standing_water_regm:
  - has_raw_value: xxx
    type: nmdc:TextValue
  start_date_inc: '2023-01-27'
  start_time_inc: 13:42+0000
  store_cond:
    has_raw_value: -20 degree Celsius freezer;P2Y10D
    type: nmdc:TextValue
  substructure_type:
  - basement
  subsurface_depth:
    has_raw_value: MIxS does not provide an example
    type: nmdc:QuantityValue
  sulfate:
    has_raw_value: 5 micromole per liter
    type: nmdc:QuantityValue
  sulfate_fw:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  sulfide:
    has_raw_value: 2 micromole per liter
    type: nmdc:QuantityValue
  surf_air_cont:
  - dust
  surf_humidity:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  surf_material: adobe
  surf_moisture:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  surf_moisture_ph: 123
  surf_temp:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  suspend_part_matter:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  suspend_solids:
  - has_raw_value: xxx
    type: nmdc:TextValue
  tan:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  technical_reps: '2'
  temp:
    has_raw_value: 25 degree Celsius
    type: nmdc:QuantityValue
  temp_out:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  tertiary_treatment:
    has_raw_value: xxx
    type: nmdc:TextValue
  tidal_stage: high tide
  tillage:
  - chisel
  tiss_cult_growth_med:
    has_raw_value: xxx
    type: nmdc:TextValue
  toluene:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  tot_carb:
    has_raw_value: MIxS does not provide an example
    type: nmdc:QuantityValue
  tot_depth_water_col:
    has_raw_value: 500 meter
    type: nmdc:QuantityValue
  tot_diss_nitro:
    has_raw_value: 40 microgram per liter
    type: nmdc:QuantityValue
  tot_inorg_nitro:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  tot_iron:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  tot_nitro:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  tot_nitro_cont_meth: https://currentprotocols.onlinelibrary.wiley.com/doi/abs/10.1002/0471142913.fab0102s00
  tot_nitro_content:
    has_raw_value: 35 milligrams Nitrogen per kilogram of soil
    type: nmdc:QuantityValue
  tot_org_c_meth:
    has_raw_value: https://www.epa.gov/sites/production/files/2015-12/documents/9060a.pdf
    type: nmdc:TextValue
  tot_org_carb:
    has_raw_value: 2%
    type: nmdc:QuantityValue
  tot_part_carb:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  tot_phosp:
    has_raw_value: 0.03 milligram per liter
    type: nmdc:QuantityValue
  tot_phosphate:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  tot_sulfur:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  train_line: red
  train_stat_loc: south station above ground
  train_stop_loc: end
  turbidity:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  tvdss_of_hcr_press:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  tvdss_of_hcr_temp:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  typ_occup_density: 123
  type: nmdc:Biosample
  ventilation_rate:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  ventilation_type:
    has_raw_value: xxx
    type: nmdc:TextValue
  vfa:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  vfa_fw:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  vis_media: photos
  viscosity:
    has_raw_value: xxx
    type: nmdc:TextValue
  volatile_org_comp:
  - has_raw_value: xxx
    type: nmdc:TextValue
  wall_area:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  wall_const_type: frame construction
  wall_finish_mat: plaster
  wall_height:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  wall_loc: north
  wall_surf_treatment: painted
  wall_texture: knockdown
  wall_thermal_mass:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  wall_water_mold:
    has_raw_value: xxx
    type: nmdc:TextValue
  wastewater_type:
    has_raw_value: xxx
    type: nmdc:TextValue
  water_cont_soil_meth: MIxS doesn't provide an example
  water_content:
  - MIxS doesn't provide an example 1
  - MIxS doesn't provide an example 2
  water_current:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  water_cut:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  water_feat_size:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  water_feat_type: fountain
  water_prod_rate:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  water_temp_regm:
  - has_raw_value: xxx
    type: nmdc:TextValue
  watering_regm:
  - has_raw_value: 1 liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    type: nmdc:TextValue
  weekday: Monday
  win:
    has_raw_value: xxx
    type: nmdc:TextValue
  wind_direction:
    has_raw_value: xxx
    type: nmdc:TextValue
  wind_speed:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  window_cond: damaged
  window_cover: blinds
  window_horiz_pos: left
  window_loc: north
  window_mat: fiberglass
  window_open_freq:
    has_raw_value: xxx
    type: nmdc:TextValue
  window_size:
    has_raw_value: xxx
    type: nmdc:TextValue
  window_status:
    has_raw_value: xxx
    type: nmdc:TextValue
  window_type: single-hung sash window
  window_vert_pos: bottom
  window_water_mold:
    has_raw_value: xxx
    type: nmdc:TextValue
  xylene:
    has_raw_value: xxx
    type: nmdc:QuantityValue
  zinc:
    has_raw_value: 2.5 mg/kg
    type: nmdc:QuantityValue

```
## ProtocolExecution-single_step
### Input
```yaml
has_input:
- nmdc:bsm-6
has_process_parts:
- nmdc:extrp-71-r2pk
id: nmdc:pex-99-18sD2
protocol_execution_category: organic_matter_extraction
protocol_link:
  name: Water Extractable Organic Matter (WEOM)
  type: nmdc:Protocol
  url: https://www.protocols.io/view/water-extractable-organic-matter-weom-ewov1o4oylr2/v1
type: nmdc:ProtocolExecution

```
## ChemicalConversionProcess-digest
### Input
```yaml
duration:
  has_numeric_value: 3
  has_unit: h
  type: nmdc:QuantityValue
has_input:
- nmdc:procsm-37
has_output:
- nmdc:procsm-39
id: nmdc:chcpr-19-7890
substances_used:
- known_as: nmdc:chem-99-000005
  sample_state_information: liquid
  substance_role: solvent
  type: nmdc:PortionOfSubstance
- known_as: nmdc:chem-99-000002
  source_concentration:
    has_numeric_value: 50
    has_unit: mM
    type: nmdc:QuantityValue
  substance_role: buffer
  type: nmdc:PortionOfSubstance
- final_concentration:
    has_numeric_value: 0.05
    has_unit: "\u03BCg/\u03BCL"
    type: nmdc:QuantityValue
  known_as: nmdc:chem-99-000014
  substance_role: ms_proteolytic_enzyme
  type: nmdc:PortionOfSubstance
substances_volume:
  has_numeric_value: 75
  has_unit: "\u03BCL"
  type: nmdc:QuantityValue
temperature:
  has_numeric_value: 37
  has_unit: Cel
  type: nmdc:QuantityValue
type: nmdc:ChemicalConversionProcess

```
## NucleotideSequencing-processing-institution
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- gold:Gp0108335
analyte_category: metagenome
associated_studies:
- nmdc:sty-00-555xxx
has_input:
- nmdc:bsm-00-red
has_output:
- nmdc:dobj-00-9n9n9n
id: nmdc:dgns-99-zUCd5N
mod_date: 22-MAY-20 06.13.12.927000000 PM
name: Thawing permafrost microbial communities from the Arctic, studying carbon transformations
  - Permafrost 712P3D
ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
  carbon transformations - Permafrost 712P3D
part_of:
- nmdc:dgns-21-999xxx
processing_institution: UCD_Genome_Center
type: nmdc:NucleotideSequencing

```
## Database-biosamples-rna-in-tube
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-dtTMNb
  rna_cont_type: tube
  type: nmdc:Biosample

```
## ProtocolExecution-minimal
### Input
```yaml
has_input:
- nmdc:bsm-6
has_process_parts:
- nmdc:extrp-71-r2pk
- nmdc:filtpr-22-32G2BS
id: nmdc:pex-99-18sD2
protocol_execution_category: organic_matter_extraction
protocol_link:
  name: Water Extractable Organic Matter (WEOM)
  type: nmdc:Protocol
  url: https://www.protocols.io/view/water-extractable-organic-matter-weom-ewov1o4oylr2/v1
type: nmdc:ProtocolExecution

```
## Database-pooling_set-minimal
### Input
```yaml
pooling_set:
- id: nmdc:poolp-9x9-1x
  name: first pooling process
  type: nmdc:Pooling

```
## ReadQcAnalysis-1
### Input
```yaml
ended_at_time: '2021-09-15T10:13:20+00:00'
execution_resource: NERSC-Perlmutter
git_url: git_url1
has_input:
- jgi:534819030d87850d7aea2a16
has_output:
- nmdc:ae40d7ae535c92b6d347915d8b1ac125
- nmdc:bd723452a107e973fcc6734ff7894bb9
id: nmdc:wfrqc-99-ABCDEF
input_base_count: 300.0
input_read_bases: 300.0
input_read_count: 10.0
name: name1
output_base_count: 100.0
output_read_bases: 100.0
output_read_count: 3.0
part_of:
- nmdc:wfch-11-ab
started_at_time: '2021-08-05T14:48:51+00:00'
type: nmdc:ReadQcAnalysis

```
## Database-biosamples-1
### Input
```yaml
biosample_set:
- add_date: 28-JUL-14 12.00.00.000000000 AM
  associated_studies:
  - nmdc:sty-00-abc123
  community: microbial communities
  description: Bulk Aqueous phase filtered water
  ecosystem: Environmental
  ecosystem_category: Aquatic
  ecosystem_subtype: Groundwater
  ecosystem_type: Freshwater
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0101224
  habitat: Coalbed water
  id: nmdc:bsm-99-dtTMNb
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients (early)
  ncbi_taxonomy_name: coal metagenome
  samp_taxon_id:
    has_raw_value: coal metagenome [NCBITaxon:1260732]
    term:
      id: NCBITaxon:1260732
      name: coal metagenome
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
  associated_studies:
  - nmdc:sty-00-abc123
  biosample_categories:
  - LTER
  - SIP
  community: microbial communities
  description: Bulk Aqueous phase filtered water
  ecosystem: Environmental
  ecosystem_category: Aquatic
  ecosystem_subtype: Groundwater
  ecosystem_type: Freshwater
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0101224
  habitat: Coalbed water
  id: nmdc:bsm-99-AtTUOs
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients (early)
  ncbi_taxonomy_name: coal metagenome
  samp_taxon_id:
    has_raw_value: coal metagenome [NCBITaxon:1260732]
    term:
      id: NCBITaxon:1260732
      name: coal metagenome
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
  associated_studies:
  - nmdc:sty-00-abc123
  community: microbial communities
  description: Bulk Aqueous phase filtered water
  ecosystem: Environmental
  ecosystem_category: Aquatic
  ecosystem_subtype: Groundwater
  ecosystem_type: Freshwater
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0101225
  habitat: Coalbed water
  id: nmdc:bsm-99-eBVHjN
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients Extra
  ncbi_taxonomy_name: coal metagenome
  samp_taxon_id:
    has_raw_value: coal metagenome [NCBITaxon:1260732]
    term:
      id: NCBITaxon:1260732
      name: coal metagenome
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
  associated_studies:
  - nmdc:sty-00-abc123
  community: microbial communities
  description: Bulk Aqueous phase filtered water
  ecosystem: Environmental
  ecosystem_category: Aquatic
  ecosystem_subtype: Groundwater
  ecosystem_type: Freshwater
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0101226
  habitat: Coalbed water
  id: nmdc:bsm-99-TDPHTh
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients
  ncbi_taxonomy_name: coal metagenome
  samp_taxon_id:
    has_raw_value: coal metagenome [NCBITaxon:1260732]
    term:
      id: NCBITaxon:1260732
      name: coal metagenome
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample

```
## DataObject-minimal
### Input
```yaml
description: Crispr Terms for nmdc:ann0vx38
id: nmdc:dobj-11-dtTMNb
name: Crispr Terms
type: nmdc:DataObject

```
## Database-study_test
### Input
```yaml
study_set:
- description: Using analytical expertise at both the JGI and EMSL, we plan to follow
    successional patterns of protein expression by root-associated microorganisms.
    This work builds on foundational research we are conducting with the common California
    grassland plant, Avena fatua, grown in Hopland, CA soil (FOA DE-PS02-09ER09-25).
    Using our 16-chamber 13C labeling facility at UC Berkeley, we have shown that
    elevated CO2 increased the amount of C allocated belowground, and increased the
    yield of root biomass. The rhizosphere microbial community undergoes a succession
    as the root grows, senesces, and dies. In elevated CO2 treatments, we also detect
    a greater amount of root-derived 13C in the mineral-associated heavy fraction
    of the soil, which is commonly assumed to reflect longer term stabilization. \n
    \nIn our JGI-EMSL project, we will follow over time how roots impact the functional
    capacity of the rhizosphere microbiome to enzymatically mediate decomposition
    processes. We hypothesize that root-exudate stimulation of soil microbial populations
    results in elevated expression of biomolecules (transcripts, enzymes, metabolites)
    for the decomposition of macromolecular C compounds.
  ecosystem: Host-associated
  ecosystem_category: Plants
  ecosystem_subtype: Soil
  ecosystem_type: Rhizosphere
  gold_study_identifiers:
  - gold:Gs999999
  id: nmdc:sty-99-boww8R
  name: Avena fatua rhizosphere microbial communities from Hopland, California, USA,
    for root-enhanced decomposition of organic matter studies
  principal_investigator:
    has_raw_value: Mary Firestone
    type: nmdc:PersonValue
  specific_ecosystem: Unclassified
  study_category: research_study
  type: nmdc:Study
- description: "We propose to utilize the unique resources at EMSL and the JGI to\
    \ obtain a better understanding of the phylogenetic and functional diversity of\
    \ cyanobacteria that have been collected from DOE mission relevant environments\
    \ (e.g. alkaline and acidic hot springs, and hypersaline terrestrial and water\
    \ habitats) and deposited in a culture collection that contains &gt;1,200 strains.\
    \ The Cyanobacteria are one of the most metabolically and morphologically diverse\
    \ bacterial phyla and it has been hypothesized that they are the origin of oxygenic\
    \ photosynthesis. The project proposed here would complement and utilize the genomic\
    \ information that was generated during JGI\u2019s GEBA Cyano project to add valuable\
    \ insights about the metabolic processes that are active in members of this phylum\
    \ and that have been - and still are - key factors in shaping our planet. In contrast\
    \ to the GEBA Cyano project, the project proposed here include mixed cultures\
    \ of organisms that are recalcitrant to separation. A comprehensive omics approach\
    \ of these simple consortia will allow us to develop tools for Systems Microbiology\
    \ and for analyzing microbe-microbe and microbe-climate interactions and the single-cell\
    \ and whole system level. Phylogenomics: We will request 16S rRNA data from our\
    \ culture collections to classify phenotypes that are most promising for addressing\
    \ questions related to carbon and nitrogen cycling and developing new chassis\
    \ for biofuel production strains. To obtain a complete 16S rRNA-based inventory\
    \ of the Cyanobacteria collection we would request ~40 Gb of iTag data from the\
    \ JGI. In addition, we would request Fluorescence in situ hybridization (FISH)\
    \ microscopy from EMSL for selected samples that contain more than one phylotype,\
    \ to obtain a better understanding of the special organization within mixed populations.\
    \ We will request an additional ~10 Gb of iTag data to monitor phylogenetic changes\
    \ in mixed cultures with phenotypes that are in particular relevant to carbon\
    \ and nitrogen cycling.   Single Cell Genomics and Metagenomics: We will request\
    \ sorting of mixed cultures targeting ~100 single cells and genomic sequencing\
    \ of the obtained isolates using JGI's PacBio pipeline (total of ~50 Gb genomic\
    \ data). For mixed cultured from which no ? or only a fraction of the community\
    \ - can be isolated as single cell, we will request a total of ~50 Gb of metagenomics\
    \ data. This will provide us with the genomic data that will be necessary to reconstruct\
    \ metabolic pathways of hitherto uncultured cyanobacteria and to identify the\
    \ key factors that make the individual members of these mixed cultures recalcitrant\
    \ to cultivation under axenic conditions. Physiology and chemistry: To determine\
    \ the physical and chemical changes that occur during Cyanobacteria mediated carbon\
    \ and nitrogen cycling, we will request access to cryo-transmission electron microscopy,\
    \ scanning electron microscopy coupled with focused ion beam, X ray spectroscopy\
    \ and electron diffraction analyses, confocal microscopy, Raman spectroscopy,\
    \ synchrotron-based computed x-ray microtomography, nano secondary ion mass spectrometry,\
    \ and high field Fourier transform ion cyclotron resonance mass spectrometry at\
    \ EMSL.   Functional dynamics: To determine the dynamics of the genetic modules\
    \ that are being transcribed into mRNA during Cyanobacteria mediated carbon and\
    \ nitrogen cycling, we propose to generate expression profiles from 10 selected\
    \ axenic and 10 mixed cultures. We will request a total of ~10 Gb and ~50 Gb of\
    \ transcriptome and metatranscriptomic data from the JGI, respectively. To determine\
    \ the dynamics of genetic modules being translated and converted into proteins\
    \ and metabolites during Cyanobacteria mediated carbon and nitrogen cycling, we\
    \ will generate metaproteomic and metametabolomic data from 10 selected axenic\
    \ and 10 mixed cultures. We will request access and support to and with mass spectrometry,\
    \ NMR spectrometry, and computation time on Chinook from EMSL."
  ecosystem: Host-associated
  ecosystem_category: Microbial
  ecosystem_subtype: Unclassified
  ecosystem_type: Bacteria
  gold_study_identifiers:
  - gold:Gs999999
  id: nmdc:sty-99-hfaLvo
  name: Cyanobacterial communities from the Joint Genome Institute, California, USA
  principal_investigator:
    has_raw_value: Matthias Hess
    type: nmdc:PersonValue
  specific_ecosystem: Unclassified
  study_category: research_study
  type: nmdc:Study
- description: 'A fundamental challenge of microbial environmental science is to understand
    how earth systems will respond to climate change. A parallel challenge in biology
    is to unverstand how information encoded in organismal genes manifests as biogeochemical
    processes at ecosystem-to-global scales. These grand challenges intersect in the
    need to understand the glocal carbon (C) cycle, which is both mediated by biological
    processes and a key driver of climate through the greenhouse gases carbon dioxide
    (CO2) and methane (CH4). A key aspect of these challenges is the C cycle implications
    of the predicted dramatic shrinkage in northern permafrost in the coming century.  '
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Wetlands
  ecosystem_type: Soil
  gold_study_identifiers:
  - gold:Gs999999
  id: nmdc:sty-99-dkDZYe
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations
  principal_investigator:
    has_raw_value: Virginia Rich
    type: nmdc:PersonValue
  specific_ecosystem: Permafrost
  study_category: research_study
  type: nmdc:Study

```
## Database-library-prep-exhausive
### Input
```yaml
library_preparation_set:
- description: DNA extraction of NEON sample TREE_001-O-20170707-COMP-DNA1 using SOP
    BMI_metagenomicsSequencingSOP_v2
  end_date: '2018-09-26'
  has_input:
  - generic:xxx
  has_output:
  - generic:xxx
  id: nmdc:libprp-99-xxx2
  library_preparation_kit: KAPA HyperPrep Kit
  library_type: DNA
  name: DNA library creation of NEON sample TREE_001-O-20170707-COMP-DNA1
  pcr_cycles: 0
  processing_institution: Battelle
  start_date: '2018-09-26'
  type: nmdc:LibraryPreparation
- description: RNA extraction of NEON sample TREE_001-O-20170707-COMP-DNA1 using SOP
    XX
  end_date: '2018-09-26'
  has_input:
  - generic:xxy
  has_output:
  - generic:xxz
  id: nmdc:libprp-99-xxx1
  library_preparation_kit: TruSeq RNA Library Prep Kit v2
  library_type: RNA
  name: RNA library creation of NEON sample TREE_001-O-20170707-COMP-DNA1
  pcr_cycles: 12
  processing_institution: Battelle
  start_date: '2018-09-26'
  type: nmdc:LibraryPreparation

```
## NucleotideSequencing-ndsdc-bioproject
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
analyte_category: metagenome
associated_studies:
- nmdc:sty-00-555xxx
gold_sequencing_project_identifiers:
- gold:Gp0704888
has_input:
- nmdc:bsm-00-red
has_output:
- nmdc:dobj-00-9n9n9n
id: nmdc:dgns-11-pf500b03
insdc_bioproject_identifiers:
- bioproject:PRJNA1029144
mod_date: 22-MAY-20 06.13.12.927000000 PM
name: Thawing permafrost microbial communities from the Arctic, studying carbon transformations
  - Permafrost 712P3D
ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
  carbon transformations - Permafrost 712P3D
part_of:
- nmdc:dgns-99-777xxx
processing_institution: JGI
type: nmdc:NucleotideSequencing

```
## DataObject-my_emsl_prefix
### Input
```yaml
alternative_identifiers:
- my_emsl:1016236
data_object_type: LC-DDA-MS/MS Raw Data
description: raw instrument file for nmdc:dgms-11-7nfk8n58
file_size_bytes: 448727423
id: nmdc:dobj-11-mzxj8743
md5_checksum: ED2BA6CD95CE5D86D8D29A8DD548F48F
name: Froze_Core_2015_S1_30_40_3_QE_26May16_Pippin_16-03-39.raw
type: nmdc:DataObject
url: https://nmdcdemo.emsl.pnnl.gov/proteomics/raw/Froze_Core_2015_S1_30_40_3_QE_26May16_Pippin_16-03-39.raw

```
## Database-multiple-paths
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-dtTMNb
  name: real biosample from the field
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-XYZ
  name: one DNA library, like an analytical sample
  type: nmdc:Biosample
data_generation_set:
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108335
  analyte_category: metagenome
  associated_studies:
  - nmdc:sty-00-555xxx
  has_input:
  - nmdc:bsm-00-red
  has_output:
  - nmdc:dobj-00-9n9n9n
  id: nmdc:dgns-99-zUCd5N
  mod_date: 22-MAY-20 06.13.12.927000000 PM
  name: a process in which a biosample was sequenced?
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712P3D
  processing_institution: JGI
  type: nmdc:NucleotideSequencing

```
## DataObject-3
### Input
```yaml
description: Metagenome Contig Coverage Stats for gold:Gp0061273
file_size_bytes: 32787380
id: nmdc:dobj-99-izwYW6
name: mapping_stats.txt
type: nmdc:DataObject

```
## Database-multi-id-study
### Input
```yaml
study_set:
- gnps_task_identifiers:
  - gnps.task:4b848c342a4f4abc871bdf8a09a60807
  - gnps.task:51cc733a80ed41139ecdd1bedf3c01af
  - gnps.task:8062948726c543dba53ec58c0f1ebb25
  - gnps.task:f8efbde4cc154db6a4cf269072d42d40
  id: nmdc:sty-11-r2h77870
  jgi_portal_study_identifiers:
  - jgi.proposal:507130
  study_category: research_study
  type: nmdc:Study

```
## PortionOfSubstance-1
### Input
```yaml
type: nmdc:PortionOfSubstance

```
## DataObject-2
### Input
```yaml
description: Assembled scaffold fasta for gold:Gp0061273
file_size_bytes: 205297945
id: nmdc:dobj-99-PqBJvW
name: assembly_scaffolds.fna
type: nmdc:DataObject

```
## Database-data-generations
### Input
```yaml
data_generation_set:
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108335
  analyte_category: metagenome
  associated_studies:
  - nmdc:sty-00-555xxx
  has_input:
  - nmdc:bsm-00-red
  has_output:
  - nmdc:dobj-00-9n9n9n
  id: nmdc:dgns-99-zUCd5N
  mod_date: 22-MAY-20 06.13.12.927000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 712P3D
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712P3D
  part_of:
  - nmdc:dgns-00-555xxx
  processing_institution: JGI
  type: nmdc:NucleotideSequencing
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108340
  analyte_category: metagenome
  associated_studies:
  - nmdc:sty-00-555xxx
  has_input:
  - nmdc:bsm-00-orange0
  has_output:
  - nmdc:dobj-00-zzzbrxzzz
  id: nmdc:dgns-99-gKlQlF
  mod_date: 22-MAY-20 06.10.59.590000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 612S3M
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 612S3M
  processing_institution: JGI
  type: nmdc:NucleotideSequencing
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108341
  analyte_category: metagenome
  associated_studies:
  - nmdc:sty-00-555xxx
  has_input:
  - nmdc:bsm-00-orange1
  has_output:
  - nmdc:dobj-00-thx1198
  id: nmdc:dgns-99-5kgIJR
  mod_date: 22-MAY-20 06.09.46.171000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 712S3S
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712S3S
  processing_institution: JGI
  type: nmdc:NucleotideSequencing

```
## MetagenomeSequencing-from-metagenome_seequencing_json
### Input
```yaml
ended_at_time: '2021-09-15T10:13:20+00:00'
execution_resource: JGI
git_url: https://github.com/microbiomedata/RawSequencingData
has_input:
- nmdc:unvalidated_placeholder
has_output:
- nmdc:22afa3d49b73eaec2e9787a6b88fbdc3
id: nmdc:wfmsa-99-qwertyuiop
name: Sequencing Activity for nmdc:mga0vx38
part_of:
- nmdc:wfch-11-ab
started_at_time: '2021-08-05T14:48:51+00:00'
type: nmdc:MetagenomeSequencing
version: v1.0.0

```
## MixingProcess-minimal
### Input
```yaml
duration:
  has_numeric_value: 2
  has_unit: hours
  type: nmdc:QuantityValue
has_input:
- nmdc:biosample-1
- nmdc:processed-sample-2
has_output:
- nmdc:4
id: nmdc:mixpro-11-A74
instrument_used:
- nmdc:inst-12-124
type: nmdc:MixingProcess

```
## Study-credit-1
### Input
```yaml
has_credit_associations:
- applied_roles:
  - Data curation
  applies_to_person:
    orcid: orcid:0000-0002-1825-00
    type: nmdc:PersonValue
  type: prov:Association
- applied_roles:
  - Software
  applies_to_person:
    orcid: orcid:0000-0001-9076-6066
    type: nmdc:PersonValue
  type: prov:Association
id: nmdc:sty-99-WoeqAi
study_category: research_study
type: nmdc:Study

```
## Database-ReadQcAnalysisActivity-quality_fail
### Input
```yaml
read_qc_analysis_set:
- ended_at_time: '2023-08-30T13:26:02.892410+00:00'
  execution_resource: NERSC-Perlmutter
  git_url: https://github.com/microbiomedata/ReadsQC
  has_failure_categorization:
  - qc_failure_what: malformed_data
    qc_failure_where: ReadQcAnalysisActivity
    type: nmdc:FailureCategorization
  has_input:
  - nmdc:dobj-11-1k62bt83
  - nmdc:dobj-11-e8hs8y25
  id: nmdc:wfrqc-11-hemh0a87.1
  name: Read QC Activity for nmdc:wfrqc-11-hemh0a87.1
  part_of:
  - nmdc:wfch-11-ab
  qc_comment: Failure during call-stage to interleave fastq files
  qc_status: fail
  started_at_time: '2023-08-29T19:41:47.365957+00:00'
  type: nmdc:ReadQcAnalysis
  version: v1.0.8
- ended_at_time: '2023-08-30T13:26:02.892410+00:00'
  execution_resource: NERSC-Perlmutter
  git_url: https://github.com/microbiomedata/ReadsQC
  has_input:
  - nmdc:dobj-11-1k62bt83
  - nmdc:dobj-11-e8hs8y25
  has_output:
  - nmdc:dobj-11-e8hs8y26
  - nmdc:dobj-11-e8hs8y27
  - nmdc:dobj-11-e8hs8y28
  id: nmdc:wfrqc-11-hemh0a88.1
  name: Read QC Activity for nmdc:wfrqc-11-hemh0a88.1
  part_of:
  - nmdc:wfch-11-ab
  qc_comment: Number of output reads from readqc is above threshold (6000000 > 1000000)
  qc_status: pass
  started_at_time: '2023-08-29T19:41:47.365957+00:00'
  type: nmdc:ReadQcAnalysis
  version: v1.0.8
- ended_at_time: '2023-08-30T13:26:02.892410+00:00'
  execution_resource: NERSC-Perlmutter
  git_url: https://github.com/microbiomedata/ReadsQC
  has_failure_categorization:
  - qc_failure_what: low_read_count
    qc_failure_where: ReadQcAnalysisActivity
    type: nmdc:FailureCategorization
  has_input:
  - nmdc:dobj-11-1k62bt83
  - nmdc:dobj-11-e8hs8y25
  has_output:
  - nmdc:dobj-11-e8hs8y26
  - nmdc:dobj-11-e8hs8y27
  - nmdc:dobj-11-e8hs8y28
  id: nmdc:wfrqc-11-hemh0a90.1
  name: Read QC Activity for nmdc:wfrqc-11-hemh0a87.1
  part_of:
  - nmdc:wfch-11-ab
  qc_comment: Most data removed for artifacts
  qc_status: fail
  started_at_time: '2023-08-29T19:41:47.365957+00:00'
  type: nmdc:ReadQcAnalysis
  version: v1.0.8

```
## Database-pooling_set-exhaustive
### Input
```yaml
pooling_set:
- alternative_identifiers:
  - generic:xxx
  description: xxx
  has_input:
  - generic:xxx
  - generic:yyy
  has_output:
  - generic:xxx
  id: nmdc:poolp-9x9-1x
  name: first pooling process
  type: nmdc:Pooling

```
## Database-mass-spectrometry
### Input
```yaml
data_generation_set:
- acquisition_category: tandem_mass_spectrum
  acquisition_strategy: data_independent_acquisition
  add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - emsl:123423
  analyte_category: metabolome
  associated_studies:
  - nmdc:sty-00-555xxx
  has_input:
  - nmdc:bsm-00-red
  has_output:
  - nmdc:dobj-00-9n9n9n
  id: nmdc:dgms-99-zUCd5N
  ionization_source: electron_ionization
  mass_analyzer: Orbitrap
  mass_spectrum_collection_mode: full_profile
  mod_date: 22-MAY-20 06.13.12.927000000 PM
  polarity_mode: negative
  resolution_category: high
  type: nmdc:MassSpectrometry

```
## Pooling-minimal
### Input
```yaml
id: nmdc:poolp-9x9-1x
name: first pooling process
type: nmdc:Pooling

```
## Database-processed_sample-minimal
### Input
```yaml
processed_sample_set:
- id: nmdc:procsm-99-dtTMNb
  type: nmdc:ProcessedSample

```
## FiltrationProcess-minimal_pressurized
### Input
```yaml
conditionings:
- Methanol
- Sterile water
filtration_category: pressure
has_input:
- nmdc:processed-sample-3
has_output:
- nmdc:7
id: nmdc:filtpr-22-32G2BS
instrument_used:
- nmdc:inst-12-125
is_pressurized: true
type: nmdc:FiltrationProcess

```
## Database-with-MetagenomeSequencing
### Input
```yaml
metagenome_sequencing_set:
- ended_at_time: '2021-09-15T10:13:20+00:00'
  execution_resource: JGI
  git_url: https://github.com/microbiomedata/RawSequencingData
  has_input:
  - nmdc:unvalidated_placeholder
  has_output:
  - nmdc:22afa3d49b73eaec2e9787a6b88fbdc3
  id: nmdc:wfmsa-99-qwertyuiop
  name: Sequencing Activity for nmdc:mga0vx38
  part_of:
  - nmdc:wfch-11-ab
  started_at_time: '2021-08-05T14:48:51+00:00'
  type: nmdc:MetagenomeSequencing
  version: v1.0.0

```
## Instrument-basic
### Input
```yaml
id: nmdc:inst-12-dtTMNb
model: novaseq_6000
name: Illumina NovaSeq
type: nmdc:Instrument
vendor: illumina

```
## Study-tidy
### Input
```yaml
alternative_descriptions:
- any string 1
- any string 2
alternative_identifiers:
- generic:abc1
alternative_names:
- any string 1
- any string 2
alternative_titles:
- any string 1
- any string 2
associated_dois:
- doi_category: publication_doi
  doi_value: doi:10.1126/science.1058040
  type: nmdc:Doi
- doi_category: dataset_doi
  doi_provider: kbase
  doi_value: doi:10.1126/science.1456956
  type: nmdc:Doi
- doi_category: award_doi
  doi_provider: jgi
  doi_value: doi:10.1126/science.1234545
  type: nmdc:Doi
- doi_category: data_management_plan_doi
  doi_provider: gsc
  doi_value: doi:10.48321/D1Z60Q
  type: nmdc:Doi
description: see also name, title, objective, various alternatives
ecosystem: unconstrained text. should be validated against the controlled vocabulary,
  by the sample's environmental package. would also be nice to align the CV with MIxS
  environmental triads
ecosystem_category: unconstrained text
ecosystem_subtype: unconstrained text
ecosystem_type: unconstrained text
funding_sources:
- any string 1
- any string 2
gold_study_identifiers:
- gold:Gs12345
- gold:Gs90909
has_credit_associations:
- applied_roles:
  - Supervision
  - Conceptualization
  - Funding acquisition
  applies_to_person:
    email: jcventer@jcvi.org
    has_raw_value: Craig Venter
    name: J. Craig Venter
    orcid: ORCID:0000-0002-7086-765X
    profile_image_url: https://en.wikipedia.org/wiki/Craig_Venter#/media/File:Craigventer2.jpg
    type: nmdc:PersonValue
    was_generated_by: nmdc:any_string_1
    websites:
    - https://www.jcvi.org/
    - https://www.jcvi.org/about/j-craig-venter
  type: prov:Association
- applied_roles:
  - Investigation
  - Supervision
  applies_to_person:
    name: Tanja Davidsen
    type: nmdc:PersonValue
  type: prov:Association
homepage_website:
- https://www.neonscience.org/
id: nmdc:sty-11-ab
mgnify_project_identifiers:
- mgnify.proj:ABC123
name: see also description, title, objective, various alternatives
objective: This record, an instance of class Study from the nmdc-schema was had authored,
  so that the NMDC team would have at least one instance, using all slots, with a
  mixture of reasonable values and minimally compliant values.
part_of:
- nmdc:sty-11-34xj1157
principal_investigator:
  email: jcventer@jcvi.org
  has_raw_value: Craig Venter
  name: J. Craig Venter
  orcid: ORCID:0000-0002-7086-765X
  profile_image_url: https://en.wikipedia.org/wiki/Craig_Venter#/media/File:Craigventer2.jpg
  type: nmdc:PersonValue
  was_generated_by: nmdc:any_string_1
  websites:
  - https://www.jcvi.org/
  - https://www.jcvi.org/about/j-craig-venter
protocol_link:
- name: any string 1
  type: nmdc:Protocol
- name: any string 2
  type: nmdc:Protocol
related_identifiers: any string R1
specific_ecosystem: unconstrained text
study_category: research_study
study_image:
- description: Photo of Craig Venter Institute, Rockville, Maryland
  display_order: 1
  has_raw_value: https://upload.wikimedia.org/wikipedia/commons/8/86/J._Craig_Vernter_Institute_Rockville_Maryland.jpg
  type: nmdc:ImageValue
  url: https://upload.wikimedia.org/wikipedia/commons/8/86/J._Craig_Vernter_Institute_Rockville_Maryland.jpg
  was_generated_by: nmdc:any_string_1
- description: Photo of Craig Venter Institute, La Jolla, California
  display_order: 2
  has_raw_value: https://today.ucsd.edu/news_uploads/140213ventor2.jpg
  type: nmdc:ImageValue
  url: https://today.ucsd.edu/news_uploads/140213ventor2.jpg
  was_generated_by: nmdc:any_string_1
title: Sample Exhaustive Biosample instance. Although all of these values should pass
  validation, that does not mean that any Biosample of any type would necessarily
  have this particular combination of values.
type: nmdc:Study
websites:
- https://w3id.org/nmdc
- https://w3id.org/linkml

```
## Database-biosample_set_low-but-acceptable-rna_volume
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-dtTMNb
  rna_volume: 12
  type: nmdc:Biosample

```
## QuantityValue-1
### Input
```yaml
has_maximum_numeric_value: 100
has_minimum_numeric_value: 200
has_raw_value: 100-200 ml
has_unit: ml
type: nmdc:QuantityValue

```
## Pooling-exhaustive
### Input
```yaml
alternative_identifiers:
- generic:xxx
description: xxx
has_input:
- generic:xxx
- generic:yyy
has_output:
- generic:xxx
id: nmdc:poolp-9x9-1x
name: first pooling process
type: nmdc:Pooling

```
## Database-biosamples-minimal
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-dtTMNb
  type: nmdc:Biosample

```
## Database-neon_Biosample_to_DataObject_NEON
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-11-34xj1150
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-abcdef1
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-11-34xj1150
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-abcdef2
  type: nmdc:Biosample
- associated_studies:
  - nmdc:sty-11-34xj1150
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:bsm-99-abcdef3
  type: nmdc:Biosample
data_generation_set:
- analyte_category: metagenome
  associated_studies:
  - nmdc:sty-11-34xj1150
  has_input:
  - nmdc:procsm-99-xyz3
  has_output:
  - nmdc:dobj-12-jdhk9537
  - nmdc:dobj-12-yx0tfp52
  id: nmdc:dgns-11-s9xj2r24
  instrument_used:
  - nmdc:inst-12-yx0tfp52
  name: Test NEON data
  part_of:
  - nmdc:dgns-11-34xj1150
  processing_institution: Battelle
  type: nmdc:NucleotideSequencing
data_object_set:
- data_object_type: Metagenome Raw Read 1
  description: Test R1 data
  id: nmdc:dobj-12-jdhk9537
  name: BMI_HY7W2BGXG_Plate19S_13WellG10_R1.fastq.gz
  type: nmdc:DataObject
  url: https://storage.neonscience.org/neon-microbial-raw-seq-files/2020/BMI_HY7W2BGXG_mms_R1/BMI_HY7W2BGXG_Plate19S_13WellG10_R1.fastq.gz
- data_object_type: Metagenome Raw Read 2
  description: Test R2 data
  id: nmdc:dobj-12-yx0tfp52
  name: W2BGXG_Plate19S_13WellG10_R2.fastq.gz
  type: nmdc:DataObject
  url: https://storage.neonscience.org/neon-microbial-raw-seq-files/2020/BMI_HY7W2BGXG_mms_R2/BMI_HY7W2BGXG_Plate19S_13WellG10_R2.fastq.gz
- data_object_type: Filtered Sequencing Reads
  description: Test filtered data for NEON
  id: nmdc:dobj-12-71q7wv80
  name: 1472_51293.filtered.fastq.gz
  type: nmdc:DataObject
  url: https://data.microbiomedata.org/data/1472_51293/qa/1472_51293.filtered.fastq.gz
extraction_set:
- end_date: '2021-01-15'
  extraction_target: DNA
  has_input:
  - nmdc:procsm-99-xyz1
  has_output:
  - nmdc:procsm-99-xyz2
  id: nmdc:extrp-99-abcdef
  name: first dna extraction set
  start_date: '2021-01-15'
  type: nmdc:Extraction
library_preparation_set:
- end_date: '2021-01-15'
  has_input:
  - nmdc:procsm-99-xyz2
  has_output:
  - nmdc:procsm-99-xyz3
  id: nmdc:libprp-99-abcdef
  library_type: DNA
  name: DNA library preparation of NEON sample TREE_001-O-20170707-COMP-DNA1
  start_date: '2021-01-15'
  type: nmdc:LibraryPreparation
pooling_set:
- description: This is the first pooling process that has ever occurred on earth
  end_date: '2021-01-14'
  has_input:
  - nmdc:bsm-99-abcdef1
  - nmdc:bsm-99-abcdef2
  - nmdc:bsm-99-abcdef3
  has_output:
  - nmdc:procsm-99-xyz1
  id: nmdc:poolp-99-abcdef
  name: first pooling process
  start_date: '2021-01-14'
  type: nmdc:Pooling
processed_sample_set:
- id: nmdc:procsm-99-xyz1
  name: first processed sample set
  type: nmdc:ProcessedSample
- id: nmdc:procsm-99-xyz2
  name: first DNA extract
  type: nmdc:ProcessedSample
- id: nmdc:procsm-99-xyz3
  name: first library
  type: nmdc:ProcessedSample
read_qc_analysis_set:
- ended_at_time: '2023-03-23T17:17:05.111725+00:00'
  execution_resource: NERSC-Cori
  git_url: https://github.com/microbiomedata/ReadsQC
  has_input:
  - nmdc:dobj-12-jdhk9537
  - nmdc:dobj-12-yx0tfp52
  has_output:
  - nmdc:dobj-12-71q7wv80
  - nmdc:dobj-12-y236qp68
  id: nmdc:wfrqc-12-63da5n74
  name: 'TEST Read QC Activity for nmdc:wfrqc-12-63da5n74 '
  part_of:
  - nmdc:wfch-11-ab
  started_at_time: '2023-03-23T17:17:05.111689+00:00'
  type: nmdc:ReadQcAnalysis
  version: b1.0.7
workflow_chain_set:
- analyte_category: metagenome
  id: nmdc:wfch-11-ab
  type: nmdc:WorkflowChain
  was_informed_by: nmdc:dgns-11-s9xj2r24

```
## MobilePhaseSegment-1
### Input
```yaml
duration:
  has_numeric_value: 2
  has_unit: hours
  type: nmdc:QuantityValue
substances_used:
- final_concentration:
    has_numeric_value: 10
    has_unit: '%'
    type: nmdc:QuantityValue
  known_as: nmdc:chem-99-000003
  type: nmdc:PortionOfSubstance
type: nmdc:MobilePhaseSegment

```
## DataObject-MB-unknown-enum-pv
### Input
```yaml
data_object_type: Crispr Terms
description: Crispr Terms for nmdc:ann0vx38
file_size_bytes: 1234
id: nmdc:dobj-11-dtTMNb
md5_checksum: 22afa3d49b73eaec2e9787a6b88fbdc3
name: Crispr Terms
type: nmdc:DataObject
url: http://example.com

```
## Biosample-with-fire
### Input
```yaml
associated_studies:
- nmdc:sty-00-abc123
env_broad_scale:
  has_raw_value: ENVO:00002030
  term:
    id: ENVO:00002030
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_local_scale:
  has_raw_value: ENVO:00002169
  term:
    id: ENVO:00002169
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_medium:
  has_raw_value: ENVO:00005792
  term:
    id: ENVO:00005792
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
fire: 1871-10-01 to 1871-10-31
id: nmdc:bsm-99-dtTMNb
type: nmdc:Biosample

```
## Database-functional-annotations
### Input
```yaml
functional_annotation_set:
- has_function: KEGG_PATHWAY:rsk00410
  type: nmdc:FunctionalAnnotation
- has_function: KEGG.REACTION:R00100
  type: nmdc:FunctionalAnnotation
- has_function: RHEA:12345
  type: nmdc:FunctionalAnnotation
- has_function: MetaCyc:RXN-14904
  type: nmdc:FunctionalAnnotation
- has_function: EC:1.1.1.1
  type: nmdc:FunctionalAnnotation
- has_function: GO:0032571
  type: nmdc:FunctionalAnnotation
- has_function: MetaNetX:MNXR101574
  type: nmdc:FunctionalAnnotation
- has_function: SEED:Biotin_biosynthesis
  type: nmdc:FunctionalAnnotation
- has_function: KEGG.ORTHOLOGY:K00001
  type: nmdc:FunctionalAnnotation
- has_function: EGGNOG:veNOG12876
  type: nmdc:FunctionalAnnotation
- has_function: PFAM:PF11779
  type: nmdc:FunctionalAnnotation
- has_function: TIGRFAM:TIGR00010
  type: nmdc:FunctionalAnnotation
- has_function: SUPFAM:SSF57615
  type: nmdc:FunctionalAnnotation
- has_function: CATH:1.10.10.200
  type: nmdc:FunctionalAnnotation
- has_function: PANTHER.FAMILY:PTHR12345
  type: nmdc:FunctionalAnnotation

```
## Protocol-minimal
### Input
```yaml
name: any string 1
type: nmdc:Protocol

```
## ImageValue-1
### Input
```yaml
description: Photo of Craig Venter Institute, La Jolla, California
display_order: 2
has_raw_value: https://today.ucsd.edu/news_uploads/140213ventor2.jpg
type: nmdc:ImageValue
url: https://today.ucsd.edu/news_uploads/140213ventor2.jpg
was_generated_by: nmdc:any_string_1

```
## CreditAssociation-1
### Input
```yaml
applied_roles:
- Supervision
- Conceptualization
- Funding acquisition
applies_to_person:
  email: jcventer@jcvi.org
  has_raw_value: Craig Venter
  name: J. Craig Venter
  orcid: ORCID:0000-0002-7086-765X
  profile_image_url: https://en.wikipedia.org/wiki/Craig_Venter#/media/File:Craigventer2.jpg
  type: nmdc:PersonValue
  was_generated_by: nmdc:any_string_1
  websites:
  - https://www.jcvi.org/
  - https://www.jcvi.org/about/j-craig-venter
type: prov:Association

```
## Database-WorkflowChain-WorkflowExecution
### Input
```yaml
read_qc_analysis_set:
- ended_at_time: '2023-03-23T17:17:05.111725+00:00'
  execution_resource: NERSC-Cori
  git_url: https://github.com/microbiomedata/ReadsQC
  has_input:
  - nmdc:dobj-12-jdhk9537
  - nmdc:dobj-12-yx0tfp52
  has_output:
  - nmdc:dobj-12-71q7wv80
  - nmdc:dobj-12-y236qp68
  id: nmdc:wfrqc-12-63da5n74
  name: 'TEST Read QC Activity for nmdc:wfrqc-12-63da5n74 '
  part_of:
  - nmdc:wfch-11-ab
  - nmdc:wfch-12-cd
  started_at_time: '2023-03-23T17:17:05.111689+00:00'
  type: nmdc:ReadQcAnalysis
  version: b1.0.7
workflow_chain_set:
- analyte_category: metagenome
  id: nmdc:wfch-11-ab
  type: nmdc:WorkflowChain
  was_informed_by: nmdc:dgns-11-s9xj2r24
- analyte_category: metagenome
  id: nmdc:wfch-12-cd
  type: nmdc:WorkflowChain
  was_informed_by: nmdc:dgns-11-s9xj2r24

```
## ChromatographicSeparationProcess-SPE
### Input
```yaml
has_input:
- nmdc:procsm-11-9gjxns61
has_output:
- nmdc:procsm-11-05g48p90
- nmdc:procsm-11-05g48p91
id: nmdc:cspro-99-oW43DzG0
ordered_mobile_phases:
- substances_used:
  - final_concentration:
      has_numeric_value: 10
      has_unit: '%'
      type: nmdc:QuantityValue
    known_as: nmdc:chem-99-000003
    type: nmdc:PortionOfSubstance
  type: nmdc:MobilePhaseSegment
  volume:
    has_numeric_value: 700
    has_unit: mL
    type: nmdc:QuantityValue
- substances_used:
  - final_concentration:
      has_numeric_value: 15
      has_unit: mM
      type: nmdc:QuantityValue
    known_as: nmdc:chem-99-000015
    type: nmdc:PortionOfSubstance
  type: nmdc:MobilePhaseSegment
  volume:
    has_numeric_value: 700
    has_unit: mL
    type: nmdc:QuantityValue
stationary_phase: CN
type: nmdc:ChromatographicSeparationProcess

```
## Database-nucleic-extraction
### Input
```yaml
extraction_set:
- description: DNA extraction of NEON sample WREF_072-O-20190618-COMP using SOP BMI_dnaExtractionSOP_v7
  end_date: '2019-11-08'
  extraction_target: DNA
  has_input:
  - generic:xxx
  has_output:
  - generic:xxx
  id: nmdc:extrp-99-abcdef
  input_mass:
    has_numeric_value: 0.25
    has_unit: gram
    type: nmdc:QuantityValue
  name: DNA extraction of NEON sample WREF_072-O-20190618-COMP
  qc_status: pass
  start_date: '2019-11-08'
  type: nmdc:Extraction

```
## FunctionalAnnotationAggMember-minimal
### Input
```yaml
count: 120
gene_function_id: KEGG.ORTHOLOGY:K00627
metagenome_annotation_id: nmdc:8253bcdcd0387177ff895c38a047c719
type: nmdc:FunctionalAnnotationAggMember

```
## GeneProduct-minimal
### Input
```yaml
id: nmdc:123
type: nmdc:GeneProduct

```
## WorkflowChain
### Input
```yaml
analyte_category: metagenome
gold_analysis_project_identifiers:
- gold:Ga0083920
id: nmdc:wfch-11-ab
jgi_portal_analysis_project_identifiers:
- jgi.analysis:1023687
name: Workflow Chain for Metagenomics analysis of NEON Biosample
type: nmdc:WorkflowChain
was_informed_by: nmdc:dgns-11-ab

```
## Database-functional_annotation_agg
### Input
```yaml
functional_annotation_agg:
- count: 120
  gene_function_id: KEGG.ORTHOLOGY:K00627
  metagenome_annotation_id: nmdc:8253bcdcd0387177ff895c38a047c719
  type: nmdc:FunctionalAnnotationAggMember

```
## Database-AssemblyAnalysis-1
### Input
```yaml
metagenome_assembly_set:
- ended_at_time: '2020-03-25T00:00:00+00:00'
  execution_resource: LANL-B-div
  git_url: https://github.com/microbiomedata/metaAssembly/releases/tag/1.0.0
  has_failure_categorization:
  - qc_failure_what: assembly_size_too_small
    qc_failure_where: MetagenomeAssembly
    type: nmdc:FailureCategorization
  - qc_failure_what: other
    qc_failure_where: MetagenomeAssembly
    type: nmdc:FailureCategorization
  has_input:
  - nmdc:dobj-12-1243
  has_output:
  - nmdc:dobj-12-1247
  id: nmdc:wfmgas-99-B7Vogx
  name: Metagenome assembly 1472_51277
  part_of:
  - nmdc:wfch-11-ab
  qc_comment: 15% human contamination and assembly size is below 5 MB
  qc_status: fail
  started_at_time: '2020-03-24T00:00:00+00:00'
  type: nmdc:MetagenomeAssembly

```
## Database-analytical_sample-extract-EDITED-TO_PASS
### Input
```yaml
processed_sample_set:
- description: Extracted DNA from WOOD_024-M-20190715-COMP
  id: nmdc:procsm-99-dtTMNb
  name: WOOD_024-M-20190715-COMP-DNA1
  type: nmdc:ProcessedSample

```
## Database-extraction_set-exhaustive
### Input
```yaml
extraction_set:
- description: DNA extraction of NEON sample WREF_072-O-20190618-COMP using SOP BMI_dnaExtractionSOP_v7
  end_date: '2019-11-08'
  extraction_target: DNA
  has_input:
  - generic:xxx
  has_output:
  - generic:xxx
  id: nmdc:extrp-99-abcdef
  input_mass:
    has_numeric_value: 0.25
    has_unit: gram
    type: nmdc:QuantityValue
  name: DNA extraction of NEON sample WREF_072-O-20190618-COMP
  qc_status: pass
  start_date: '2019-11-08'
  type: nmdc:Extraction

```
## Study-emsl
### Input
```yaml
emsl_project_identifiers:
- emsl.project:60141
id: nmdc:sty-11-ab
study_category: research_study
type: nmdc:Study

```
## Database-chemical_entity_set-1
### Input
```yaml
chemical_entity_set:
- alternative_identifiers:
  - wd:Q37525
  chemical_formula: C6H12O6
  description: generally considered the most abundant monosaccharide in nature
  id: nmdc:chem-99-000001
  inchi: 1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5-,6?/m1/s1
  inchi_key: WQZGKKKJIJFFOK-GASJEMHNSA-N
  name: glucose
  smiles:
  - OC[C@H]1OC(O)[C@H](O)[C@@H](O)[C@@H]1O
  - C([C@@H]1[C@H]([C@@H]([C@H]([C@H](O1)O)O)O)O)O
  type: nmdc:ChemicalEntity
- alternative_identifiers:
  - CHEBI:184335
  id: nmdc:chem-99-000002
  name: ammonium bicarbonate
  type: nmdc:ChemicalEntity
- alternative_identifiers:
  - MS:1001251
  description: A serine protease that hydrolyzes peptide bonds at the C-terminus of
    arginine and lysine.
  id: nmdc:chem-99-000014
  name: trypsin
  type: nmdc:ChemicalEntity
- alternative_identifiers:
  - CHEBI:17790
  chemical_formula: CH3OH
  id: nmdc:chem-99-000003
  inchi_key: OKKJLVBELUTLKV-UHFFFAOYSA-N
  name: methanol
  type: nmdc:ChemicalEntity
- alternative_identifiers:
  - CHEBI:15377
  chemical_formula: H2O
  id: nmdc:chem-99-000004
  name: water
  type: nmdc:ChemicalEntity
- id: nmdc:chem-99-000005
  name: deionized water
  type: nmdc:ChemicalEntity
- alternative_identifiers:
  - CHEBI:7696
  chemical_formula: HCl
  id: nmdc:chem-99-000015
  name: hydrochloric acid
  type: nmdc:ChemicalEntity
- id: nmdc:chem-99-000006
  name: triton-x 100
  type: nmdc:ChemicalEntity
- alternative_identifiers:
  - MS:1001306
  description: A serine protease that hydrolyzes peptide bonds at the C-terminus of
    tryptophan, leucine, tyrosine, and phenylalanine.
  id: nmdc:chem-99-000007
  name: chymotrypsin
  type: nmdc:ChemicalEntity
- alternative_identifiers:
  - MS:1001309
  description: A serine protease that hydrolyzes peptide, ester, and amide bonds at
    the C-terminus of lysine.
  id: nmdc:chem-99-000008
  name: Lys-C
  type: nmdc:ChemicalEntity
- alternative_identifiers:
  - MS:1003093
  description: A metalloendopeptidase that hydrolyzes peptide bonds at the C-terminus
    of lysine.
  id: nmdc:chem-99-000009
  name: Lys-N
  type: nmdc:ChemicalEntity
- alternative_identifiers:
  - MS:1001917
  description: A serine protease that hydrolyzes peptide and ester bonds at the C-terminus
    of aspartic acid or glutamic acid
  id: nmdc:chem-99-000010
  name: Glu-C
  type: nmdc:ChemicalEntity
- alternative_identifiers:
  - MS:1001303
  description: A cysteine protease that hydrolyzes peptide, ester, and amide bonds
    at the C-terminus of arginine and with lower efficiency, lysine.
  id: nmdc:chem-99-000011
  name: Arg-C
  type: nmdc:ChemicalEntity
- alternative_identifiers:
  - MS:1001304
  description: A zinc metalloendopeptidase that hydrolyzes peptide bonds at the N-terminus
    of aspartic acid.
  id: nmdc:chem-99-000012
  name: Asp-N
  type: nmdc:ChemicalEntity
- description: A serine protease that hydrolyzes peptide bonds at the C-terminus of
    threonine, alanine, serine, and valine.
  id: nmdc:chem-99-000013
  name: alphaLP
  type: nmdc:ChemicalEntity

```
## Database-study-set-with-gnps-id
### Input
```yaml
study_set:
- associated_dois:
  - doi_category: award_doi
    doi_provider: emsl
    doi_value: doi:10.25585/1488217
    type: nmdc:Doi
  description: Thawing permafrost is one of the largest soil carbon pools on the planet.
    The goal of this project is to study microbial communities that participate in
    the soil carbon cycle.
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Wetlands
  ecosystem_type: Soil
  gnps_task_identifiers:
  - gnps.task:4b848c342a4f4abc871bdf8a09a60807
  gold_study_identifiers:
  - gold:Gs123456789
  id: nmdc:sty-99-FkQIsc
  name: Permafrost microbial communities from Stordalen Mire, Sweden
  principal_investigator:
    has_raw_value: Virginia Rich
    type: nmdc:PersonValue
  specific_ecosystem: Permafrost
  study_category: research_study
  type: nmdc:Study

```
## FunctionalAnnotation-exhaustive
### Input
```yaml
has_function: KEGG_PATHWAY:abc12345
subject: nmdc:gene_product_1
type: nmdc:FunctionalAnnotation
was_generated_by: nmdc:activity_1

```
## ChromatographicSeparationProcess-GC-has_calibration
### Input
```yaml
chromatographic_category: gas_chromatography
has_calibration: any text
has_input:
- nmdc:procsm-11-9gjxns61
has_output:
- nmdc:procsm-11-05g48p90
- nmdc:procsm-11-05g48p91
id: nmdc:cspro-99-oW43DzG0
stationary_phase: Silica
type: nmdc:ChromatographicSeparationProcess

```
## NucleotideSequencing-1
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- gold:Gp0108335
analyte_category: metagenome
associated_studies:
- nmdc:sty-00-555xxx
has_input:
- nmdc:bsm-00-red
has_output:
- nmdc:dobj-00-9n9n9n
id: nmdc:dgns-99-zUCd5N
mod_date: 22-MAY-20 06.13.12.927000000 PM
name: Thawing permafrost microbial communities from the Arctic, studying carbon transformations
  - Permafrost 712P3D
ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
  carbon transformations - Permafrost 712P3D
part_of:
- nmdc:dgns-22-444xxx
processing_institution: JGI
type: nmdc:NucleotideSequencing

```
## Database-study-set-with-dois
### Input
```yaml
study_set:
- associated_dois:
  - doi_category: award_doi
    doi_provider: jgi
    doi_value: doi:10.25585/1487763
    type: nmdc:Doi
  - doi_category: award_doi
    doi_provider: emsl
    doi_value: doi:10.25585/1487765
    type: nmdc:Doi
  - doi_category: publication_doi
    doi_provider: jgi
    doi_value: doi:10.21/FQSQT4T3
    type: nmdc:Doi
  - doi_category: publication_doi
    doi_value: doi:10.1016/j.foodchem.2008.11.065
    type: nmdc:Doi
  - doi_category: dataset_doi
    doi_provider: ess_dive
    doi_value: doi:10.1333/s00897980202a
    type: nmdc:Doi
  - doi_category: dataset_doi
    doi_provider: massive
    doi_value: doi:10.1093/acprof:oso/9780195159561.001.1
    type: nmdc:Doi
  description: Thawing permafrost is one of the largest soil carbon pools on the planet.
    The goal of this project is to study microbial communities that participate in
    the soil carbon cycle.
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Wetlands
  ecosystem_type: Soil
  gnps_task_identifiers:
  - gnps.task:4b848c342a4f4abc871bdf8a09a60807
  gold_study_identifiers:
  - gold:Gs123456789
  id: nmdc:sty-99-FkQIsc
  name: Permafrost microbial communities from Stordalen Mire, Sweden
  principal_investigator:
    has_raw_value: Virginia Rich
    type: nmdc:PersonValue
  specific_ecosystem: Permafrost
  study_category: research_study
  type: nmdc:Study

```
## DataGeneration-invalid-class_is_abstract
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- gold:Gp0108335
analyte_category: metagenome
associated_studies:
- nmdc:sty-00-555xxx
has_input:
- nmdc:bsm-00-red
has_output:
- nmdc:dobj-00-9n9n9n
id: nmdc:dgns-99-zUCd5N
mod_date: 22-MAY-20 06.13.12.927000000 PM
name: Thawing permafrost microbial communities from the Arctic, studying carbon transformations
  - Permafrost 712P3D
ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
  carbon transformations - Permafrost 712P3D
processing_institution: JGI
type: nmdc:DataGeneration

```
## Database-biosamples-high-rna_volume
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  id: nmdc:bsm-99-dtTMNb
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  rna_volume: 1200
  type: nmdc:Biosample

```
## ChemicalConversionProcess-invalid_compound_entry
### Input
```yaml
catalyzed_by:
- has_solution_components:
  - compound: trypsin
    concentration:
      has_numeric_value: 0.05
      has_unit: "\u03BCg/\u03BCL"
duration:
  has_numeric_value: 3
  has_unit: h
has_input:
- nmdc:procsm-37
has_output:
- nmdc:procsm-39
has_reagents:
  solutions_used:
  - has_solution_components:
    - compound: Hot Chocolate, yummy yummy
    - compound: ammonium_bicarbonate
      concentration:
        has_numeric_value: 50
        has_unit: mM
    volume:
      has_numeric_value: 75
      has_unit: "\u03BCL"
id: nmdc:chcpr-19-7890
temperature:
  has_numeric_value: 37
  has_unit: Cel

```
## Database-biosamples-dna-in-plate-invalid-well-val
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  dna_cont_type: plate
  dna_cont_well: A1
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  id: nmdc:bsm-99-dtTMNb
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  type: nmdc:Biosample

```
## Database-WorkflowChain_WorkflowExecution_no_part_of
### Input
```yaml
read_qc_analysis_set:
- ended_at_time: '2023-03-23T17:17:05.111725+00:00'
  execution_resource: NERSC-Cori
  git_url: https://github.com/microbiomedata/ReadsQC
  has_input:
  - nmdc:dobj-12-jdhk9537
  - nmdc:dobj-12-yx0tfp52
  has_output:
  - nmdc:dobj-12-71q7wv80
  - nmdc:dobj-12-y236qp68
  id: nmdc:wfrqc-12-63da5n74
  name: 'TEST Read QC Activity for nmdc:wfrqc-12-63da5n74 '
  started_at_time: '2023-03-23T17:17:05.111689+00:00'
  type: nmdc:ReadQcAnalysis
  version: b1.0.7
workflow_chain_set:
- analyte_category: metagenome
  id: nmdc:wfch-11-ab
  type: nmdc:WorkflowChain
  was_informed_by: nmdc:dgns-11-s9xj2r24
- analyte_category: metagenome
  id: nmdc:wfch-12-cd
  type: nmdc:WorkflowChain
  was_informed_by: nmdc:dgns-11-s9xj2r24

```
## DataObject-no-name
### Input
```yaml
description: Crispr Terms for nmdc:ann0vx38
id: nmdc:dobj-99-abc123
type: nmdc:DataObject

```
## Database-plannedprocess-non-string-end_datet
### Input
```yaml
extraction_set:
- end_date: 2021-01-15
  extraction_target: DNA
  has_input:
  - bare:pool_out_1
  has_output:
  - bare:dna_extract_1
  id: nmdc:extrp-99-abcdefg
  name: first dna extraction set
  type: nmdc:Extraction
library_preparation_set:
- has_input:
  - bare:dna_extract_1
  has_output:
  - bare:library_1
  id: nmdc:libprp-99-abcdefg
  library_type: DNA
  name: DNA library preparation of NEON sample TREE_001-O-20170707-COMP-DNA1
  type: nmdc:LibraryPreparation

```
## Biosample-invalid_fire
### Input
```yaml
associated_studies:
- nmdc:sty-00-abc123
env_broad_scale:
  has_raw_value: ENVO:00002030
  term:
    id: ENVO:00002030
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_local_scale:
  has_raw_value: ENVO:00002169
  term:
    id: ENVO:00002169
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_medium:
  has_raw_value: ENVO:00005792
  term:
    id: ENVO:00005792
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
fire: like a volcano
id: nmdc:bsm-99-dtTMNb
type: nmdc:Biosample

```
## WorkflowChain-missing_analyte_category
### Input
```yaml
id: nmdc:wfch-11-ab
name: Workflow Chain for Metagenomics analysis of NEON Biosample
type: nmdc:WorkflowChain
was_informed_by: nmdc:dgns-11-ab

```
## Database-biosamples-rna-in-bucket
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  id: nmdc:bsm-99-dtTMNb
  rna_cont_type: bucket
  type: nmdc:Biosample

```
## ChromatographicSeparationProcess-undefined-compund
### Input
```yaml
has_input:
- nmdc:procsm-11-9gjxns61
has_output:
- nmdc:procsm-11-05g48p90
- nmdc:procsm-11-05g48p91
id: nmdc:cspro-99-oW43DzG0
ordered_mobile_phases:
- has_solution_components:
  - compound: MeOH
    type: nmdc:SolutionComponent
  type: nmdc:Solution
  volume:
    has_numeric_value: 700
    has_unit: mL
    type: nmdc:QuantityValue
- has_solution_components:
  - compound: hydrochloric_acid
    concentration:
      has_numeric_value: 10
      has_unit: mM
      type: nmdc:QuantityValue
    type: nmdc:SolutionComponent
  type: nmdc:Solution
  volume:
    has_numeric_value: 700
    has_unit: mL
    type: nmdc:QuantityValue
- has_solution_components:
  - compound: water
    type: nmdc:SolutionComponent
  type: nmdc:Solution
  volume:
    has_numeric_value: 1000
    has_unit: mL
    type: nmdc:QuantityValue
stationary_phase: CN
type: nmdc:ChromatographicSeparationProcess

```
## MetabolomicsAnalysis-invalid_execution_resource_not_in_enum
### Input
```yaml
ended_at_time: '2021-09-15T10:13:20+00:00'
execution_resource: NERSC - Cori
git_url: https://example.org/WorkflowExecutionActivity
has_input:
- nmdc:i1
- nmdc:i2
has_output:
- nmdc:o1
- nmdc:o2
id: nmdc:wfmb-99-ABCDEF
part_of: nmdc:xxx-00-ABCDEF
started_at_time: '2021-08-05T14:48:51+00:00'
type: nmdc:MetabolomicsAnalysis

```
## Biosample-minimal-no-type
### Input
```yaml
associated_studies:
- nmdc:sty-00-abc123
env_broad_scale:
  has_raw_value: ENVO:00002030
  term:
    id: ENVO:00002030
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_local_scale:
  has_raw_value: ENVO:00002169
  term:
    id: ENVO:00002169
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_medium:
  has_raw_value: ENVO:00005792
  term:
    id: ENVO:00005792
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
id: nmdc:bsm-99-dtTMNb

```
## Biosample-non_boolean_embargo
### Input
```yaml
associated_studies:
- nmdc:sty-00-abc123
embargoed: 999
env_broad_scale:
  has_raw_value: ENVO:00002030
  term:
    id: ENVO:00002030
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_local_scale:
  has_raw_value: ENVO:00002169
  term:
    id: ENVO:00002169
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_medium:
  has_raw_value: ENVO:00005792
  term:
    id: ENVO:00005792
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
id: nmdc:bsm-99-dtTMNb
type: nmdc:Biosample

```
## MassSpectrometry-no-analyte_category
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- gold:Gp0108335
has_input:
- nmdc:bsm-00-red
has_output:
- nmdc:dobj-00-9n9n9n
id: nmdc:dgms-99-9n9n9n
mod_date: 22-MAY-20 06.13.12.927000000 PM
name: Thawing permafrost microbial communities from the Arctic, studying carbon transformations
  - Permafrost 712P3D
ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
  carbon transformations - Permafrost 712P3D
part_of:
- nmdc:sty-00-555xxx
processing_institution: JGI
type: nmdc:MassSpectrometry

```
## FunctionalAnnotation-invalid-function
### Input
```yaml
has_function: KEGG_PATHWAY:XOXOXOXO
type: nmdc:FunctionalAnnotation

```
## Solution-multiple_components
### Input
```yaml
substances_used:
- final_concentration:
    has_numeric_value: 10
    has_unit: mM
    type: nmdc:QuantityValue
  known_as: nmdc:chem-99-000003
  type: nmdc:PortionOfSubstance
- final_concentration:
    has_numeric_value: 15
    has_unit: mM
    type: nmdc:QuantityValue
  known_as: nmdc:chem-99-000015
  type: nmdc:PortionOfSubstance
- known_as: nmdc:chem-99-000004
  type: nmdc:PortionOfSubstance
type: nmdc:Solution
volume:
  has_numeric_value: 500
  has_unit: mL
  type: nmdc:QuantityValue

```
## MetagenomeSequencing-no_parthood
### Input
```yaml
ended_at_time: '2021-09-15T10:13:20+00:00'
execution_resource: JGI
git_url: https://github.com/microbiomedata/RawSequencingData
has_input:
- nmdc:unvalidated_placeholder
has_output:
- nmdc:22afa3d49b73eaec2e9787a6b88fbdc3
id: nmdc:wfmsa-99-qwertyuiop
name: Sequencing Activity for nmdc:mga0vx38
started_at_time: '2021-08-05T14:48:51+00:00'
type: nmdc:MetagenomeSequencing
version: v1.0.0

```
## Database-studies-missing-study_category
### Input
```yaml
study_set:
- description: A fundamental challenge of microbial environmental science is to understand
    how earth systems will respond to climate change
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Wetlands
  ecosystem_type: Soil
  id: nmdc:sty-00-555xxx
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations
  specific_ecosystem: Permafrost
  type: nmdc:Study

```
## Database-Extraction-sample_mass-now_input_mass
### Input
```yaml
extraction_set:
- description: DNA extraction of NEON sample WREF_072-O-20190618-COMP using SOP BMI_dnaExtractionSOP_v7
  end_date: '2019-11-08'
  extraction_target: DNA
  has_input:
  - nmdc:xxx
  has_output:
  - nmdc:xxx
  id: nmdc:extrp-99-abcdef
  name: DNA extraction of NEON sample WREF_072-O-20190618-COMP
  processing_institution: Battelle
  protocol_link:
    name: BMI_dnaExtractionSOP_v7
    type: nmdc:Protocol
    url: https://data.neonscience.org/documents/10179/2431540/BMI_dnaExtractionSOP_v7/61204962-bb01-a0b9-3354-ccdaab5132c3
  qc_status: pass
  sample_mass:
    has_numeric_value: 0.25
    has_unit: gram
    type: nmdc:QuantityValue
  start_date: '2019-11-08'
  type: nmdc:Extraction

```
## Database-data-generation-instrument_name-retired
### Input
```yaml
data_generation_set:
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108335
  analyte_category: metagenome
  associated_studies:
  - nmdc:sty-00-555xxx
  has_input:
  - nmdc:bsm-00-red
  has_output:
  - nmdc:dobj-00-9n9n9n
  id: nmdc:dgns-99-zUCd5N
  instrument_name: THIS SLOT SHOULD NOT BE ALLOWED FOR THIS CLASS ANYMORE
  mod_date: 22-MAY-20 06.13.12.927000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 712P3D
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712P3D
  processing_institution: JGI
  type: nmdc:NucleotideSequencing

```
## Extraction-metabolomics-concentration-without-compound
### Input
```yaml
extractant:
  has_solution_components:
  - concentration:
      has_numeric_value: 5
      has_unit: '%'
      type: nmdc:QuantityValue
    type: nmdc:SolutionComponent
  type: nmdc:Solution
has_input:
- nmdc:ome-6
has_output:
- nmdc:ome-8
id: nmdc:extrp-71-r2pk
type: nmdc:Extraction

```
## Extraction-metabolomics-string-extractant
### Input
```yaml
extractant: 10 methanol in deionized water
has_input:
- nmdc:ome-6
has_output:
- nmdc:ome-8
id: nmdc:extrp-71-r2pk
type: nmdc:Extraction

```
## Study-has-abstract
### Input
```yaml
abstract: Nothing was studied.
alternative_descriptions:
- any string 1
- any string 2
alternative_names:
- any string 1
- any string 2
alternative_titles:
- any string 1
- any string 2
associated_dois:
- doi_category: dataset_doi
  doi_provider: osti
  doi_value: doi:10.25585/1488209
  type: nmdc:Doi
description: see also name, title, objective, various alternatives
ecosystem: unconstrained text. should be validated against the controlled vocabulary,
  by the sample's environmental package. would also be nice to align the CV with MIxS
  environmental triads
ecosystem_category: unconstrained text
ecosystem_subtype: unconstrained text
ecosystem_type: unconstrained text
funding_sources:
- 'This is an example of a funding source with too long of a description. Funding
  sources should be no more than 250 characters.  Any longer is unnecessary and excessive.
  It''s very very very very very very very very very very very very very very very
  very  very very very very very very very long"

  '
- any string 2
gold_study_identifiers:
- gold:Gs12345
- gold:Gs90909
id: nmdc:sty-11-ab
mgnify_project_identifiers:
- mgnify.proj:ABC123
name: see also description, title, objective, various alternatives
objective: This record, an instance of class Study from the nmdc-schema was had authored,
  so that the NMDC team would have at least one instance, using all slots, with a
  mixture of reasonable values and minimally compliant values.
principal_investigator:
  email: jcventer@jcvi.org
  has_raw_value: Craig Venter
  name: J. Craig Venter
  orcid: ORCID:0000-0002-7086-765X
  profile_image_url: https://en.wikipedia.org/wiki/Craig_Venter#/media/File:Craigventer2.jpg
  type: nmdc:PersonValue
  was_generated_by: nmdc:any_string_1
  websites:
  - https://www.jcvi.org/
  - https://www.jcvi.org/about/j-craig-venter
protocol_link:
- name: any string 1
  type: nmdc:Protocol
- name: any string 2
  type: nmdc:Protocol
related_identifiers: any string R1
specific_ecosystem: unconstrained text
study_category: research_study
title: Sample Exhaustive Biosample instance. Although all of these values should pass
  validation, that does not mean that any Biosample of any type would necessarily
  have this particular combination of values.
type: nmdc:Study
websites:
- https://w3id.org/nmdc
- https://w3id.org/linkml

```
## Filtration-invalid_non-numeric-pore-size-num-val
### Input
```yaml
conditionings:
- Methanol
- Kerosene
filter_material: PTFE
filter_pore_size:
  has_numeric_value: '0.02'
  has_unit: "\xB5m"
  type: nmdc:QuantityValue
filtration_category: pre-condition
has_input:
- nmdc:biosample-1
has_output:
- nmdc:5
id: nmdc:filtpr-99-123
type: nmdc:FiltrationProcess

```
## WorkflowChain-invalid_gold_ext_ids_not_array
### Input
```yaml
analyte_category: metagenome
gold_analysis_project_identifiers: gold:Ga0083920
id: nmdc:wfch-11-ab
jgi_portal_analysis_project_identifiers:
- jgi.analysis:1023687
name: Workflow Chain for Metagenomics analysis of NEON Biosample
type: nmdc:WorkflowChain
was_informed_by: nmdc:dgns-11-ab

```
## Database-studies-legacy-gold-study-id
### Input
```yaml
study_set:
- description: We propose to utilize the unique resources at EMSL and the JGI to obtain
    a better understanding of the phylogenetic and functional diversity of cyanobacteria
  ecosystem: Host-associated
  ecosystem_category: Microbial
  ecosystem_subtype: Unclassified
  ecosystem_type: Bacteria
  id: gold:Gs0110132
  name: Cyanobacterial communities from the Joint Genome Institute, California, USA
  specific_ecosystem: Unclassified
  study_category: research_study
  type: nmdc:Study

```
## Database-Biosample-invalid_lat_lon_ranges
### Input
```yaml
biosample_set:
- add_date: 28-JUL-14 12.00.00.000000000 AM
  associated_studies:
  - nmdc:sty-00-8675309
  community: microbial communities
  description: Bulk Aqueous phase filtered water
  ecosystem: Environmental
  ecosystem_category: Aquatic
  ecosystem_subtype: Groundwater
  ecosystem_type: Freshwater
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0101224
  habitat: Coalbed water
  id: nmdc:bsm-99-dtTMNb
  lat_lon:
    has_raw_value: 100
    latitude: '-33.460524'
    longitude: '150.168149'
    type: nmdc:GeolocationValue
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients (early)
  ncbi_taxonomy_name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
  associated_studies:
  - nmdc:sty-00-8675309
  community: microbial communities
  description: Bulk Aqueous phase filtered water
  ecosystem: Environmental
  ecosystem_category: Aquatic
  ecosystem_subtype: Groundwater
  ecosystem_type: Freshwater
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0101225
  habitat: Coalbed water
  id: nmdc:bsm-99-dtTMNb2
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients Extra
  ncbi_taxonomy_name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
  associated_studies:
  - nmdc:sty-00-8675309
  community: microbial communities
  description: Bulk Aqueous phase filtered water
  ecosystem: Environmental
  ecosystem_category: Aquatic
  ecosystem_subtype: Groundwater
  ecosystem_type: Freshwater
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0101226
  habitat: Coalbed water
  id: nmdc:bsm-99-dtTMNb3
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients
  ncbi_taxonomy_name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample

```
## Study-include-emsl_project_dois
### Input
```yaml
alternative_descriptions:
- any string 1
- any string 2
alternative_identifiers:
- generic:abc1
alternative_names:
- any string 1
- any string 2
alternative_titles:
- any string 1
- any string 2
associated_dois:
- doi_category: dataset_doi
  doi_provider: osti
  doi_value: doi:10.25585/1488209
  type: nmdc:Doi
description: see also name, title, objective, various alternatives
ecosystem: unconstrained text. should be validated against the controlled vocabulary,
  by the sample's environmental package. would also be nice to align the CV with MIxS
  environmental triads
ecosystem_category: unconstrained text
ecosystem_subtype: unconstrained text
ecosystem_type: unconstrained text
emsl_project_dois:
- doi:10.25585/1487763
funding_sources:
- any string 1
- any string 2
gold_study_identifiers:
- gold:Gs12345
- gold:Gs90909
has_credit_associations:
- applied_roles:
  - Supervision
  - Conceptualization
  - Funding acquisition
  applies_to_person:
    email: jcventer@jcvi.org
    has_raw_value: Craig Venter
    name: J. Craig Venter
    orcid: ORCID:0000-0002-7086-765X
    profile_image_url: https://en.wikipedia.org/wiki/Craig_Venter#/media/File:Craigventer2.jpg
    type: nmdc:PersonValue
    was_generated_by: nmdc:any_string_1
    websites:
    - https://www.jcvi.org/
    - https://www.jcvi.org/about/j-craig-venter
  type: prov:Association
- applied_roles:
  - Investigation
  - Supervision
  applies_to_person:
    name: Tanja Davidsen
    type: nmdc:PersonValue
  type: prov:Association
id: nmdc:sty-11-ab
mgnify_project_identifiers:
- mgnify.proj:ABC123
name: see also description, title, objective, various alternatives
objective: This record, an instance of class Study from the nmdc-schema was had authored,
  so that the NMDC team would have at least one instance, using all slots, with a
  mixture of reasonable values and minimally compliant values.
principal_investigator:
  email: jcventer@jcvi.org
  has_raw_value: Craig Venter
  name: J. Craig Venter
  orcid: ORCID:0000-0002-7086-765X
  profile_image_url: https://en.wikipedia.org/wiki/Craig_Venter#/media/File:Craigventer2.jpg
  type: nmdc:PersonValue
  was_generated_by: nmdc:any_string_1
  websites:
  - https://www.jcvi.org/
  - https://www.jcvi.org/about/j-craig-venter
protocol_link:
- name: any string 1
  type: nmdc:Protocol
- name: any string 2
  type: nmdc:Protocol
related_identifiers: any string R1
specific_ecosystem: unconstrained text
study_category: research_study
title: Sample Exhaustive Biosample instance. Although all of these values should pass
  validation, that does not mean that any Biosample of any have this particular combination
  of values.
type: nmdc:Study
websites:
- https://w3id.org/nmdc
- https://w3id.org/linkml

```
## Database-nom_analysis_set-non-string-ended_at_time
### Input
```yaml
nom_analysis_set:
- ended_at_time: 2018-11-13 20:20:39+00:00
  execution_resource: EMSL-RZR
  git_url: xxx
  has_input:
  - nmdc:1
  - nmdc:2
  has_output:
  - nmdc:3
  - nmdc:4
  id: nmdc:wfnom-99-abcdefg
  part_of: nmdc:sty-11-34xj1150
  started_at_time: '2018-11-13T20:20:39+00:00'
  type: nmdc:NomAnalysis

```
## Study-has-missing_doi_provider
### Input
```yaml
alternative_descriptions:
- any string 1
- any string 2
alternative_names:
- any string 1
- any string 2
alternative_titles:
- any string 1
- any string 2
associated_dois:
- doi_category: dataset_doi
  doi_value: doi:10.25585/1488209
  type: nmdc:Doi
description: see also name, title, objective, various alternatives
ecosystem: unconstrained text. should be validated against the controlled vocabulary,
  by the sample's environmental package. would also be nice to align the CV with MIxS
  environmental triads
ecosystem_category: unconstrained text
ecosystem_subtype: unconstrained text
ecosystem_type: unconstrained text
funding_sources:
- any string 1
- any string 2
gold_study_identifiers:
- gold:Gs12345
- gold:Gs90909
id: nmdc:sty-11-ab
mgnify_project_identifiers:
- mgnify.proj:ABC123
name: see also description, title, objective, various alternatives
objective: This record, an instance of class Study from the nmdc-schema was had authored,
  so that the NMDC team would have at least one instance, using all slots, with a
  mixture of reasonable values and minimally compliant values.
principal_investigator:
  email: jcventer@jcvi.org
  has_raw_value: Craig Venter
  name: J. Craig Venter
  orcid: ORCID:0000-0002-7086-765X
  profile_image_url: https://en.wikipedia.org/wiki/Craig_Venter#/media/File:Craigventer2.jpg
  type: nmdc:PersonValue
  was_generated_by: nmdc:any_string_1
  websites:
  - https://www.jcvi.org/
  - https://www.jcvi.org/about/j-craig-venter
protocol_link:
- name: any string 1
  type: nmdc:Protocol
- name: any string 2
  type: nmdc:Protocol
related_identifiers: any string R1
specific_ecosystem: unconstrained text
study_category: research_study
title: Sample Exhaustive Biosample instance. Although all of these values should pass
  validation, that does not mean that any Biosample of any
type: nmdc:Study
websites:
- https://w3id.org/nmdc
- https://w3id.org/linkml

```
## Database-biosample_gold_id_list_as_primary_key
### Input
```yaml
biosample_set:
- add_date: 28-JUL-14 12.00.00.000000000 AM
  associated_studies:
  - nmdc:sty-00-8675309
  community: microbial communities
  description: Bulk Aqueous phase filtered water
  ecosystem: Environmental
  ecosystem_category: Aquatic
  ecosystem_subtype: Groundwater
  ecosystem_type: Freshwater
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  habitat: Coalbed water
  id:
  - gold:Gb0101224
  - gold:Gb0101225
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients (early)
  ncbi_taxonomy_name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
  associated_studies:
  - nmdc:sty-00-8675309
  community: microbial communities
  description: Bulk Aqueous phase filtered water
  ecosystem: Environmental
  ecosystem_category: Aquatic
  ecosystem_subtype: Groundwater
  ecosystem_type: Freshwater
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0101225
  habitat: Coalbed water
  id: nmdc:bsm-99-dtTMNb
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients Extra
  ncbi_taxonomy_name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
  associated_studies:
  - nmdc:sty-00-8675309
  community: microbial communities
  description: Bulk Aqueous phase filtered water
  ecosystem: Environmental
  ecosystem_category: Aquatic
  ecosystem_subtype: Groundwater
  ecosystem_type: Freshwater
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0101226
  habitat: Coalbed water
  id: nmdc:bsm-99-dtTMNb2
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients
  ncbi_taxonomy_name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample

```
## Biosample-invalid-infiltrations
### Input
```yaml
env_broad_scale:
  has_raw_value: ENVO:00002030
  term:
    id: ENVO:00002030
env_local_scale:
  has_raw_value: ENVO:00002169
  term:
    id: ENVO:00002169
env_medium:
  has_raw_value: ENVO:00005792
  term:
    id: ENVO:00005792
id: nmdc:bsm-99-dtTMNb
infiltrations:
- 2 minutes
part_of:
- nmdc:sty-00-abc123

```
## NucleotideSequencing-invalid-prefix
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- gold:Gp0108335
analyte_category: metagenome
has_input:
- nmdc:bsm-00-red
has_output:
- nmdc:dobj-00-9n9n9n
id: nmdc:omicsprc-99-zUCd5N
mod_date: 22-MAY-20 06.13.12.927000000 PM
name: Thawing permafrost microbial communities from the Arctic, studying carbon transformations
  - Permafrost 712P3D
ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
  carbon transformations - Permafrost 712P3D
part_of:
- nmdc:sty-00-555xxx
processing_institution: JGI
type: nmdc:NucleotideSequencing

```
## Database-biosamples-lat_lon-with-GLV-missing-latitude
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  id: nmdc:bsm-99-dtTMNb
  lat_lon:
    has_raw_value: -33.460524 150.168149
    longitude: 150.168149
    type: nmdc:GeolocationValue
  type: nmdc:Biosample

```
## Database-polymorphic-invalid-type
### Input
```yaml
planned_process_set:
- id: nmdc:poolp-00-123456
  type: nmdc:Pooling
- has_input:
  - nmdc:bsm-00-435737
  has_output:
  - nmdc:procsm-00-0938548
  id: nmdc:extrp-00-999999
  type: nmdc:Extraction
- has_input:
  - nmdc:procsm-00-0938548
  has_output:
  - nmdc:procsm-00-sdsdll
  id: nmdc:libprp-00-999999
  type: nmdc:UndefinedClass

```
## Database-NomAnalysisActivity-remove_used
### Input
```yaml
nom_analysis_set:
- ended_at_time: '2018-11-13T20:20:39+00:00'
  execution_resource: NERSC-Cori
  git_url: xxx
  has_input:
  - nmdc:1
  - nmdc:2
  has_output:
  - nmdc:3
  - nmdc:4
  id: nmdc:wfnom-99-abcdefg
  part_of: nmdc:sty-00-abc123
  started_at_time: '2018-11-13T20:20:39+00:00'
  type: nmdc:NomAnalysis
  used: 12T_FTICR_B

```
## ChemicalConversionProcess-tries-to-menton-reagent-by-id
### Input
```yaml
duration:
  has_numeric_value: 1
  has_unit: h
  type: nmdc:QuantityValue
has_input:
- nmdc:fasp-37
has_output:
- nmdc:ome-39
has_reagents:
  lab_reagents_used:
  - chemical_formula: CH3OH
    concentration:
      has_numeric_value: 10
      has_unit: mM
      type: nmdc:QuantityValue
    inchi_key: OKKJLVBELUTLKV-UHFFFAOYSA-N
    sample_state_information: liquid
    type: nmdc:LaboratoryReagent
    volume:
      has_numeric_value: 120
      has_unit: mL
      type: nmdc:QuantityValue
  - nmdc:rgnt-37
  type: nmdc:ReagentsCollection
id: nmdc:chcpr-19-789
temperature:
  has_numeric_value: 25
  has_unit: Cel
  type: nmdc:QuantityValue
type: nmdc:ChemicalConversionProcess

```
## MetabolomicsAnalysis-invalid-has-slot-used
### Input
```yaml
ended_at_time: '2021-09-15T10:13:20+00:00'
execution_resource: NERSC-Cori
git_url: https://example.org/WorkflowExecutionActivity
has_input:
- nmdc:i1
- nmdc:i2
has_output:
- nmdc:o1
- nmdc:o2
id: nmdc:wfmb-99-ABCDEF
part_of: nmdc:wfch-11-ab
started_at_time: '2021-08-05T14:48:51+00:00'
type: nmdc:MetabolomicsAnalysis
used: used1

```
## Database-studies-undefined-doi-slot
### Input
```yaml
study_set:
- description: We propose to utilize the unique resources at EMSL and the JGI to obtain
    a better understanding of the phylogenetic and functional diversity of cyanobacteria
  doi:
    has_raw_value: 10.25585/1487758
  ecosystem: Host-associated
  ecosystem_category: Microbial
  ecosystem_subtype: Unclassified
  ecosystem_type: Bacteria
  id: nmdc:sty-99-abcdefg
  name: Cyanobacterial communities from the Joint Genome Institute, California, USA
  specific_ecosystem: Unclassified
  study_category: research_study
  type: nmdc:Study

```
## Database-mags-img_identifiers-exceeds-cardinality
### Input
```yaml
mags_set:
- binned_contig_num: 489
  ended_at_time: '2021-01-10T00:00:00+00:00'
  execution_resource: NERSC-Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:0a3d00715d01ad7b8f3aee59b674dfe9
  - nmdc:668d207be5ea844f988fbfb2813564cc
  - nmdc:b7e9c8d0bffdd13ace6f862a61fa87d2
  has_output:
  - nmdc:818f5a47d1371295f9313909ea12eb50
  - nmdc:e0b7421514f976cb7ad8c343cf3077a9
  - nmdc:a755bb87aded36aefbd8022506a793c7
  - nmdc:1346fe25b6ff22180eb3a51204e0b1fc
  id: nmdc:wfmag-99-5MiDJM
  img_identifiers:
  - img.taxon:3300062116
  - img.taxon:3300062117
  input_contig_num: 169782
  low_depth_contig_num: 0
  mags_list:
  - bin_name: bins.1
    bin_quality: LQ
    completeness: 11.42
    contamination: 0.21
    gene_count: 250
    num_16s: 0
    num_23s: 0
    num_5s: 1
    num_t_rna: 1
    number_of_contig: 52
    type: nmdc:MagBin
  - bin_name: bins.2
    bin_quality: LQ
    completeness: 51.25
    contamination: 10.34
    gene_count: 2548
    num_16s: 0
    num_23s: 0
    num_5s: 1
    num_t_rna: 26
    number_of_contig: 426
    type: nmdc:MagBin
  - bin_name: bins.3
    bin_quality: LQ
    completeness: 2
    contamination: 0
    gene_count: 294
    num_16s: 0
    num_23s: 0
    num_5s: 0
    num_t_rna: 1
    number_of_contig: 11
    type: nmdc:MagBin
  name: MAGs activiity 1781_86101
  part_of:
  - nmdc:wfch-11-ab
  started_at_time: '2021-01-10T00:00:00+00:00'
  too_short_contig_num: 159810
  type: nmdc:MagsAnalysis
  unbinned_contig_num: 9483
- binned_contig_num: 206
  ended_at_time: '2021-01-10T00:00:00+00:00'
  execution_resource: NERSC-Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:b78f599c21fb31b00d3f8a3c56daeb88
  - nmdc:662dc676b0b5a486248357f5b887c18b
  - nmdc:bc034c7024043ea88b44d0897bb5bece
  has_output:
  - nmdc:c24915651cfdfc91f3e6b5bac679c3af
  - nmdc:e8ec230bfe68a272b34540e7f5ab5b2b
  - nmdc:474fa29bd39452fa80f5a32e9e6be6f4
  - nmdc:9800add41d26829494265ba81a100c53
  id: nmdc:wfmag-99-VOgM5i
  input_contig_num: 78376
  low_depth_contig_num: 0
  mags_list:
  - bin_name: bins.1
    bin_quality: LQ
    completeness: 25.86
    contamination: 0
    gene_count: 401
    num_16s: 0
    num_23s: 0
    num_5s: 0
    num_t_rna: 4
    number_of_contig: 74
    type: nmdc:MagBin
  - bin_name: bins.2
    bin_quality: LQ
    completeness: 0
    contamination: 0
    gene_count: 383
    num_16s: 0
    num_23s: 0
    num_5s: 0
    num_t_rna: 5
    number_of_contig: 74
    type: nmdc:MagBin
  - bin_name: bins.3
    bin_quality: LQ
    completeness: 17.61
    contamination: 0
    gene_count: 313
    num_16s: 0
    num_23s: 0
    num_5s: 0
    num_t_rna: 7
    number_of_contig: 58
    type: nmdc:MagBin
  name: MAGs activiity 1781_86089
  part_of:
  - nmdc:wfch-12-ab
  started_at_time: '2021-01-10T00:00:00+00:00'
  too_short_contig_num: 75364
  type: nmdc:MagsAnalysis
  unbinned_contig_num: 2806

```
## Biosample-incomplete_napa_id
### Input
```yaml
add_date: 28-JUL-14 12.00.00.000000000 AM
associated_studies:
- nmdc:sty-00-abc123
community: microbial communities
description: Bulk Aqueous phase filtered water
ecosystem: Environmental
ecosystem_category: Aquatic
ecosystem_subtype: Groundwater
ecosystem_type: Freshwater
env_broad_scale:
  has_raw_value: ENVO:00002030
  term:
    id: ENVO:00002030
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_local_scale:
  has_raw_value: ENVO:00002169
  term:
    id: ENVO:00002169
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_medium:
  has_raw_value: ENVO:00005792
  term:
    id: ENVO:00005792
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
geo_loc_name:
  has_raw_value: Lithgow
  type: nmdc:TextValue
gold_biosample_identifiers:
- gold:Gb0101224
habitat: Coalbed water
id: nmdc:bsm-
lat_lon:
  has_raw_value: -33.460524 150.168149
  latitude: -33.460524
  longitude: 150.168149
  type: nmdc:GeolocationValue
location: from the Lithgow State Coal Mine, New South Wales, Australia
mod_date: 26-AUG-16 01.50.27.000000000 PM
name: Lithgow State Coal Mine Calcium nutrients (early)
ncbi_taxonomy_name: coal metagenome
sample_collection_site: Lithgow State Coal Mine
specific_ecosystem: Coalbed water
type: nmdc:Biosample

```
## Database-study-include-abstract
### Input
```yaml
study_set:
- abstract: Nothing was studied.
  alternative_descriptions:
  - any string 1
  - any string 2
  alternative_names:
  - any string 1
  - any string 2
  alternative_titles:
  - any string 1
  - any string 2
  associated_dois:
  - doi_category: dataset_doi
    doi_provider: osti
    doi_value: doi:10.25585/1488209
    type: nmdc:Doi
  description: see also name, title, objective, various alternatives
  ecosystem: unconstrained text. should be validated against the controlled vocabulary,
    by the sample's environmental package. would also be nice to align the CV with
    MIxS environmental triads
  ecosystem_category: unconstrained text
  ecosystem_subtype: unconstrained text
  ecosystem_type: unconstrained text
  funding_sources:
  - This is an example of a funding source with too long of a description. Funding
    sources should be no more than 150 characters. Any longer is unnecessary and excessive.
    Its very very very very very very very very very long.
  - any string 2
  gold_study_identifiers:
  - gold:Gs12345
  - gold:Gs90909
  id: nmdc:sty-11-ab
  mgnify_project_identifiers:
  - mgnify.proj:ABC123
  name: see also description, title, objective, various alternatives
  objective: This record, an instance of class Study from the nmdc-schema was had
    authored, so that the NMDC team would have at least one instance, using all slots,
    with a mixture of reasonable values and minimally compliant values.
  principal_investigator:
    email: jcventer@jcvi.org
    has_raw_value: Craig Venter
    name: J. Craig Venter
    orcid: ORCID:0000-0002-7086-765X
    profile_image_url: https://en.wikipedia.org/wiki/Craig_Venter#/media/File:Craigventer2.jpg
    type: nmdc:PersonValue
    was_generated_by: nmdc:any_string_1
    websites:
    - https://www.jcvi.org/
    - https://www.jcvi.org/about/j-craig-venter
  protocol_link:
  - name: any string 1
    type: nmdc:Protocol
  - name: any string 2
    type: nmdc:Protocol
  related_identifiers: any string R1
  specific_ecosystem: unconstrained text
  study_category: research_study
  title: Sample Exhaustive Biosample instance. Although all of these values should
    pass validation, that does not mean that any Biosample of any type would necessarily
    have this particular combination of values.
  type: nmdc:Study
  websites:
  - https://w3id.org/nmdc
  - https://w3id.org/linkml

```
## Study-invalid-homepage-website
### Input
```yaml
homepage_website:
- https://www.neonscience.org/
- https://consortium.org/
id: nmdc:sty-11-ab
study_category: consortium

```
## DataObject-no-type
### Input
```yaml
description: Crispr Terms for nmdc:ann0vx38
id: nmdc:dobj-99-abc123
name: Crispr Terms for nmdc:ann0vx38

```
## DissolvingProcess-minimal-no-solvent
### Input
```yaml
duration:
  has_numeric_value: 2
  has_unit: hours
  type: nmdc:QuantityValue
has_input:
- nmdc:bsm-12-A67
has_output:
- nmdc:procsm-13-S67F
id: nmdc:dispro-11-A74
instrument_used:
- nmdc:inst-12-124
solubilizing_agent: triton_X-100
type: nmdc:DissolvingProcess

```
## Database-studies-undefined-principal_investigator_name-slot
### Input
```yaml
study_set:
- description: A fundamental challenge of microbial environmental science is to understand
    how earth systems will respond to climate change
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Wetlands
  ecosystem_type: Soil
  id: nmdc:sty-00-555xxx
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations
  principal_investigator_name:
    has_raw_value: Virginia Rich
  specific_ecosystem: Permafrost
  study_category: research_study
  type: nmdc:Study

```
## Database-MetabolomicAnalysis_part_of_not_array
### Input
```yaml
metabolomics_analysis_set:
- ended_at_time: '2021-09-15T10:13:20+00:00'
  execution_resource: NERSC-Cori
  git_url: https://example.org/WorkflowExecutionActivity
  has_input:
  - nmdc:i1
  - nmdc:i2
  has_output:
  - nmdc:o1
  - nmdc:o2
  id: nmdc:wfmb-99-ABCDEF
  name: Metabolomics Analysis Activity for nmdc:wfmb-99-ABCDEF
  part_of: nmdc:wfch-11-ab
  started_at_time: '2021-08-05T14:48:51+00:00'
  type: nmdc:MetabolomicsAnalysis

```
## Study-using-undefined-genome_portal_identifiers-slot
### Input
```yaml
id: nmdc:sty-11-ab
jgi_genome_portal_identifiers:
- https://genome.jgi.doe.gov/portal/BioDefcarcycling/BioDefcarcycling.info.html
study_category: research_study
type: nmdc:Study

```
## Study-has-publications
### Input
```yaml
alternative_descriptions:
- any string 1
- any string 2
alternative_names:
- any string 1
- any string 2
alternative_titles:
- any string 1
- any string 2
description: see also name, title, objective, various alternatives
ecosystem: unconstrained text. should be validated against the controlled vocabulary,
  by the sample's environmental package. would also be nice to align the CV with MIxS
  environmental triads
ecosystem_category: unconstrained text
ecosystem_subtype: unconstrained text
ecosystem_type: unconstrained text
funding_sources:
- any string 1
- any string 2
gold_study_identifiers:
- gold:Gs12345
- gold:Gs90909
id: nmdc:sty-11-ab
mgnify_project_identifiers:
- mgnify.proj:ABC123
name: see also description, title, objective, various alternatives
objective: This record, an instance of class Study from the nmdc-schema was had authored,
  so that the NMDC team would have at least one instance, using all slots, with a
  mixture of reasonable values and minimally compliant values.
principal_investigator:
  email: jcventer@jcvi.org
  has_raw_value: Craig Venter
  name: J. Craig Venter
  orcid: ORCID:0000-0002-7086-765X
  profile_image_url: https://en.wikipedia.org/wiki/Craig_Venter#/media/File:Craigventer2.jpg
  type: nmdc:PersonValue
  was_generated_by: nmdc:any_string_1
  websites:
  - https://www.jcvi.org/
  - https://www.jcvi.org/about/j-craig-venter
protocol_link:
- name: any string 1
  type: nmdc:Protocol
- name: any string 2
  type: nmdc:Protocol
publications:
- any string 1
- any string 2
related_identifiers: any string R1
specific_ecosystem: unconstrained text
title: Sample Exhaustive Biosample instance. Although all of these values should pass
  validation, that does not mean that any Biosample of any type would necessarily
  have this particular combination of values.
type: nmdc:Study
websites:
- https://w3id.org/nmdc
- https://w3id.org/linkml

```
## Database-Biosample-invalid_id
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-8675309
  env_broad_scale:
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  id: nmdc:local
  type: nmdc:Biosample

```
## NucleotideSequencing-no-id
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- gold:Gp0108335
analyte_category: metagenome
has_input:
- nmdc:bsm-00-red
has_output:
- nmdc:dobj-00-9n9n9n
mod_date: 22-MAY-20 06.13.12.927000000 PM
name: Thawing permafrost microbial communities from the Arctic, studying carbon transformations
  - Permafrost 712P3D
ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
  carbon transformations - Permafrost 712P3D
part_of:
- nmdc:sty-00-555xxx
processing_institution: JGI
type: nmdc:NucleotideSequencing

```
## Database-studies-undefined-foo-slot
### Input
```yaml
study_set:
- description: Using analytical expertise at both the JGI and EMSL, we plan to follow
    successional patterns of protein expression
  ecosystem: Host-associated
  ecosystem_category: Plants
  ecosystem_subtype: Soil
  ecosystem_type: Rhizosphere
  foo: bar
  id: nmdc:sty-00-abc123
  name: Avena fatua rhizosphere microbial communities from Hopland, California, USA,
    for root-enhanced decomposition of organic matter studies
  specific_ecosystem: Unclassified
  study_category: research_study
  type: nmdc:Study

```
## ChromatographicSeparationProcess-no_has_calibration_with_GC
### Input
```yaml
chromatographic_category: gas_chromatography
has_input:
- nmdc:procsm-11-9gjxns61
has_output:
- nmdc:procsm-11-05g48p90
- nmdc:procsm-11-05g48p91
id: nmdc:cspro-99-oW43DzG0
ordered_mobile_phases:
- has_solution_components:
  - compound: methanol
    type: nmdc:SolutionComponent
  type: nmdc:Solution
  volume:
    has_numeric_value: 700
    has_unit: mL
    type: nmdc:QuantityValue
- has_solution_components:
  - compound: hydrochloric_acid
    concentration:
      has_numeric_value: 10
      has_unit: mM
      type: nmdc:QuantityValue
    type: nmdc:SolutionComponent
  type: nmdc:Solution
  volume:
    has_numeric_value: 700
    has_unit: mL
    type: nmdc:QuantityValue
- has_solution_components:
  - compound: water
    type: nmdc:SolutionComponent
  type: nmdc:Solution
  volume:
    has_numeric_value: 1000
    has_unit: mL
    type: nmdc:QuantityValue
stationary_phase: CN
type: nmdc:ChromatographicSeparationProcess

```
## Database-nom_analysis_set-incomplete-string-ended_at_time
### Input
```yaml
nom_analysis_set:
- ended_at_time: '2018-11-13T20:20:39+00:00'
  execution_resource: EMSL-RZR
  git_url: xxx
  has_input:
  - nmdc:1
  - nmdc:2
  has_output:
  - nmdc:3
  - nmdc:4
  id: nmdc:wfnom-99-abcdefg
  part_of: nmdc:sty-11-34xj1150
  started_at_time: 2018-11-111
  type: nmdc:NomAnalysis

```
## Database-ReadQcAnalysisActivity-invalid
### Input
```yaml
read_qc_analysis_activity_set:
- ended_at_time: '2023-08-30T13:26:02.892410+00:00'
  execution_resource: NERSC-Perlmutter
  git_url: https://github.com/microbiomedata/ReadsQC
  has_failure_categorization:
  - qc_failure_what: malformed_data
    qc_failure_where: ReadQcAnalysisActivity
  has_input:
  - nmdc:dobj-11-1k62bt83
  - nmdc:dobj-11-e8hs8y25
  id: nmdc:wfrqc-11-hemh0a87.1
  name: Read QC Activity for nmdc:wfrqc-11-hemh0a87.1
  qc_comment: Failure during call-stage to interleave fastq files
  qc_status: pass
  started_at_time: '2023-08-29T19:41:47.365957+00:00'
  type: nmdc:ReadQcAnalysisActivity
  version: v1.0.8
  was_informed_by: nmdc:omprc-11-r0pjgp16

```
## SolutionComponent-minimal
### Input
```yaml
compound: methanol
concentration:
  has_numeric_value: 10
  has_unit: mM
  type: nmdc:QuantityValue
type: nmdc:SolutionComponent

```
## NucleotideSequencing-omics-type-slot-retired
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- gold:Gp0108335
analyte_category: metagenome
has_input:
- nmdc:bsm-00-red
has_output:
- nmdc:dobj-00-9n9n9n
id: nmdc:dgns-99-zUCd5N
mod_date: 22-MAY-20 06.13.12.927000000 PM
name: Thawing permafrost microbial communities from the Arctic, studying carbon transformations
  - Permafrost 712P3D
ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
  carbon transformations - Permafrost 712P3D
omics_type: all_values_illegal
part_of:
- nmdc:sty-00-555xxx
processing_institution: JGI
type: nmdc:NucleotideSequencing

```
## Solution-minimal
### Input
```yaml
substances_used:
- final_concentration:
    has_numeric_value: 10
    has_unit: mM
    type: nmdc:QuantityValue
  known_as: nmdc:chem-99-000003
  type: nmdc:PortionOfSubstance
  volume:
    has_numeric_value: 120
    has_unit: mL
    type: nmdc:QuantityValue
type: nmdc:Solution

```
## Database-biosample_undeclared_slot
### Input
```yaml
biosample_set:
- add_date: 28-JUL-14 12.00.00.000000000 AM
  associated_studies:
  - nmdc:sty-00-8675309
  community: microbial communities
  description: Bulk Aqueous phase filtered water
  ecosystem: Environmental
  ecosystem_category: Aquatic
  ecosystem_subtype: Groundwater
  ecosystem_type: Freshwater
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  foo: bar
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0101224
  habitat: Coalbed water
  id: nmdc:bsm-99-dtTMNb
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients (early)
  ncbi_taxonomy_name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
  associated_studies:
  - nmdc:sty-00-8675309
  community: microbial communities
  description: Bulk Aqueous phase filtered water
  ecosystem: Environmental
  ecosystem_category: Aquatic
  ecosystem_subtype: Groundwater
  ecosystem_type: Freshwater
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0101225
  habitat: Coalbed water
  id: nmdc:bsm-99-dtTMNb2
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients Extra
  ncbi_taxonomy_name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
  associated_studies:
  - nmdc:sty-00-8675309
  community: microbial communities
  description: Bulk Aqueous phase filtered water
  ecosystem: Environmental
  ecosystem_category: Aquatic
  ecosystem_subtype: Groundwater
  ecosystem_type: Freshwater
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  gold_biosample_identifiers:
  - gold:Gb0101226
  habitat: Coalbed water
  id: nmdc:bsm-99-dtTMNb3
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients
  ncbi_taxonomy_name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample

```
## Filtration-invalid_non-string-conditioning
### Input
```yaml
conditionings:
- Methanol
- 123
filter_material: PTFE
filter_pore_size:
  has_numeric_value: 0.02
  has_unit: "\xB5m"
  type: nmdc:QuantityValue
filtration_category: pre-condition
has_input:
- nmdc:biosample-1
has_output:
- nmdc:5
id: nmdc:filtpr-99-123
type: nmdc:FiltrationProcess

```
## ProtocolExecution-inlined_not_valid
### Input
```yaml
has_input:
- nmdc:bsm-6
has_process_parts:
- extractant:
    has_solution_components:
    - compound: deionized_water
    - compound: methanol
      concentration:
        has_numeric_value: 5
        has_unit: '%'
  has_input:
  - nmdc:ome-6
  has_output:
  - nmdc:ome-8
  id: nmdc:extrp-71-r2pk
id: nmdc:pex-99-18sD2
protocol_execution_category: organic_matter_extraction
protocol_link:
  name: Water Extractable Organic Matter (WEOM)
  type: nmdc:Protocol
  url: https://www.protocols.io/view/water-extractable-organic-matter-weom-ewov1o4oylr2/v1
type: nmdc:ProtocolExecution

```
## Database-study_set-bad-emsl-doi-slot-name
### Input
```yaml
study_set:
- emsl_proposal_dois:
  - doi:10.46936/intm.proj.2021.60141/60000423
  id: nmdc:sty-11-ab
  study_category: research_study
  type: nmdc:Study

```
## Database-biosamples-lat_lon-with-GLV-missing-longitude
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  id: nmdc:bsm-99-dtTMNb
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    type: nmdc:GeolocationValue
  type: nmdc:Biosample

```
## DataGeneration-invalid-mass-spec-collection-mode
### Input
```yaml
acquisition_category: tandem_mass_spectrum
acquisition_strategy: data_independent_acquisition
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- emsl:123423
analyte_category: metabolome
associated_studies:
- nmdc:sty-00-555xxx
has_input:
- nmdc:bsm-00-red
has_output:
- nmdc:dobj-00-9n9n9n
id: nmdc:dgms-99-zUCd5N
ionization_source: electrospray_ionization
mass_analyzer: Orbitrap
mass_spectrum_collection_mode: profile
mod_date: 22-MAY-20 06.13.12.927000000 PM
polarity_mode: negative
resolution_category: high
type: nmdc:MassSpectrometry

```
## MetabolomicsAnalysis-invalid-missing_execution_resource
### Input
```yaml
ended_at_time: '2021-09-15T10:13:20+00:00'
git_url: https://example.org/WorkflowExecutionActivity
has_input:
- nmdc:i1
- nmdc:i2
has_output:
- nmdc:o1
- nmdc:o2
id: nmdc:wfmb-99-ABCDEF
part_of: nmdc:xxx-00-123456
started_at_time: '2021-08-05T14:48:51+00:00'
type: nmdc:MetabolomicsAnalysis

```
## Database-biosamples-rna-in-plate-invalid-well-val
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  id: nmdc:bsm-99-dtTMNb
  rna_cont_type: plate
  rna_cont_well: A1
  type: nmdc:Biosample

```
## Database-using-undefined-analytical_sample_set-slot
### Input
```yaml
analytical_sample_set:
- id: nmdc:ansm-99-dtTMNb
  name: WOOD_024-M-20190715-COMP-DNA1

```
## DataObject-no-id
### Input
```yaml
description: Crispr Terms for nmdc:ann0vx38
name: Crispr Terms for nmdc:ann0vx38
type: nmdc:DataObject

```
## Database-biosamples-dna-in-bucket
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  dna_cont_type: bucket
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  id: nmdc:bsm-99-dtTMNb
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  type: nmdc:Biosample

```
## Database-biosamples-rna-in-plate-no-well-val
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  id: nmdc:bsm-99-dtTMNb
  rna_cont_type: plate
  type: nmdc:Biosample

```
## Database-invalid-functional-annotations
### Input
```yaml
functional_annotation_set:
- has_function: KEGG_PATHWAY:XOXOXOXO
  type: nmdc:FunctionalAnnotation
- has_function: KEGG_PATHWAY:iIiIiIiI
  type: nmdc:FunctionalAnnotation

```
## Database-data-generation-undefined-omics-processing
### Input
```yaml
data_generation_set:
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108335
  analyte_category: metagenome
  has_input:
  - nmdc:bsm-00-red
  has_output:
  - nmdc:dobj-00-9n9n9n
  id: nmdc:dgms-99-zUCd5N
  mod_date: 22-MAY-20 06.13.12.927000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 712P3D
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712P3D
  part_of:
  - nmdc:dgns-00-555xxx
  processing_institution: JGI
  type: nmdc:NucleotideSequencing
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108340
  analyte_category: metagenome
  has_input:
  - nmdc:bsm-00-orange0
  has_output:
  - nmdc:dobj-00-zzzbrxzzz
  id: nmdc:dgns-99-gKlQlF
  mod_date: 22-MAY-20 06.10.59.590000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 612S3M
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 612S3M
  part_of:
  - nmdc:dgns-00-555xxx
  processing_institution: JGI
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108341
  analyte_category: metagenome
  associated_studies:
  - nmdc:dgns-00-555xxx
  has_input:
  - nmdc:bsm-00-orange1
  has_output:
  - nmdc:dobj-00-thx1198
  id: nmdc:dgns-99-5kgIJR
  mod_date: 22-MAY-20 06.09.46.171000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 712S3S
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712S3S
  omics_type: THIS SLOT IS NOT AVAILABLE FOR THIS CLAS ANYMORE
  processing_institution: JGI
  type: nmdc:NucleotideSequencing

```
## DataObject-invalid-data_object_type
### Input
```yaml
alternative_identifiers:
- prefix:value1
- prefix:value2
compression_type: any string
data_object_type: undefined permissible value for `file type enum`
description: Crispr Terms for nmdc:ann0vx38
file_size_bytes: 1234
id: nmdc:dobj-11-dtTMNb
md5_checksum: 22afa3d49b73eaec2e9787a6b88fbdc3
name: Crispr Terms
type: nmdc:DataObject
url: http://example.com
was_generated_by: nmdc:invalid_id

```
## Database-MetagenomeAssembly_invalid_qc_status_rules
### Input
```yaml
metagenome_assembly_set:
- ended_at_time: '2020-03-25T00:00:00+00:00'
  execution_resource: LANL B-div
  git_url: https://github.com/microbiomedata/metaAssembly/releases/tag/1.0.0
  has_input:
  - nmdc:dobj-12-1243
  id: nmdc:wfmgas-99-B7Vogx
  name: Metagenome assembly 1472_51277
  started_at_time: '2020-03-24T00:00:00+00:00'
  type: nmdc:MetagenomeAssembly
  was_informed_by: nmdc:omprc-12-124

```
## ChromatographicSeparationProcess_wrong_associated_study_class_value
### Input
```yaml
associated_studies:
- nmdc:dgms-666-333xxx
chromatographic_category: gas_chromatography
has_calibration: nmdc:obj-asdfasd-asdfasdf
has_input:
- nmdc:procsm-11-9gjxns61
has_output:
- nmdc:procsm-11-05g48p90
- nmdc:procsm-11-05g48p91
id: nmdc:cspro-99-oW43DzG0
ordered_mobile_phases:
- has_solution_components:
  - compound: methanol
    type: nmdc:SolutionComponent
  type: nmdc:Solution
  volume:
    has_numeric_value: 700
    has_unit: mL
    type: nmdc:QuantityValue
- has_solution_components:
  - compound: hydrochloric_acid
    concentration:
      has_numeric_value: 10
      has_unit: mM
      type: nmdc:QuantityValue
    type: nmdc:SolutionComponent
  type: nmdc:Solution
  volume:
    has_numeric_value: 700
    has_unit: mL
    type: nmdc:QuantityValue
- has_solution_components:
  - compound: water
    type: nmdc:SolutionComponent
  type: nmdc:Solution
  volume:
    has_numeric_value: 1000
    has_unit: mL
    type: nmdc:QuantityValue
part_of:
- nmdc-dgms-88-555xxx
stationary_phase: CN
type: nmdc:ChromatographicSeparationProcess

```
## Biosample-minimal-invalid-type
### Input
```yaml
associated_studies:
- nmdc:sty-00-abc123
env_broad_scale:
  has_raw_value: ENVO:00002030
  term:
    id: ENVO:00002030
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_local_scale:
  has_raw_value: ENVO:00002169
  term:
    id: ENVO:00002169
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_medium:
  has_raw_value: ENVO:00005792
  term:
    id: ENVO:00005792
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
id: nmdc:bsm-99-dtTMNb
type: nmdc:UndefinedClass

```
## PlaceholderClass-1
### Input
```yaml
description: A minimal instance for the core module
id: nmdc:123
name: Placeholder 1
type: nmdc:PlaceholderClass

```
## Instrument-invalid_model
### Input
```yaml
id: nmdc:inst-12-dtTMNb
model: anytimeseq
name: Illumina AnyTimeSeq
type: nmdc:Instrument
vendor: illumina

```
## Database-Extraction-extraction_method-slot-retired
### Input
```yaml
extraction_set:
- description: DNA extraction of NEON sample WREF_072-O-20190618-COMP using SOP BMI_dnaExtractionSOP_v7
  end_date: '2019-11-08'
  extraction_method: phenol/chloroform extraction
  extraction_target: DNA
  has_input:
  - nmdc:xxx
  has_output:
  - nmdc:xxx
  id: nmdc:extrp-99-abcdef
  name: DNA extraction of NEON sample WREF_072-O-20190618-COMP
  processing_institution: Battelle
  protocol_link:
    name: BMI_dnaExtractionSOP_v7
    type: nmdc:Protocol
    url: https://data.neonscience.org/documents/10179/2431540/BMI_dnaExtractionSOP_v7/61204962-bb01-a0b9-3354-ccdaab5132c3
  qc_status: pass
  start_date: '2019-11-08'
  type: nmdc:Extraction

```
## Database-biosamples-rna-in-tube-with-well-value
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  id: nmdc:bsm-99-dtTMNb
  rna_cont_type: tube
  rna_cont_well: B2
  type: nmdc:Biosample

```
## Database-functional_annotation_agg
### Input
```yaml
functional_annotation_agg:
- count: 120
  metagenome_annotation_id: nmdc:8253bcdcd0387177ff895c38a047c719

```
## WorkflowChain-missing-was_informed_by
### Input
```yaml
analyte_category: metagenome
id: nmdc:wfch-11-ab
name: Workflow Chain for Metagenomics analysis of NEON Biosample
type: nmdc:WorkflowChain

```
## Study-emsl-bad-local
### Input
```yaml
emsl_project_identifiers:
- emsl.project:abc
id: nmdc:sty-11-ab
study_category: research_study
type: nmdc:Study

```
## ReadQcAnalysis-invalid-has-was_informed_by
### Input
```yaml
ended_at_time: '2021-09-15T10:13:20+00:00'
execution_resource: NERSC-Perlmutter
git_url: git_url1
has_input:
- jgi:534819030d87850d7aea2a16
has_output:
- nmdc:ae40d7ae535c92b6d347915d8b1ac125
- nmdc:bd723452a107e973fcc6734ff7894bb9
id: nmdc:wfrqc-99-ABCDEF
input_base_count: 300.0
input_read_bases: 300.0
input_read_count: 10.0
name: name1
output_base_count: 100.0
output_read_bases: 100.0
output_read_count: 3.0
part_of: nmdc:wfch-11-ab
started_at_time: '2021-08-05T14:48:51+00:00'
type: nmdc:ReadQcAnalysis
was_informed_by: nmdc:wfch-99-qwertyuiop

```
## MetagenomeSequencing-bad_id
### Input
```yaml
ended_at_time: '2021-09-15T10:13:20+00:00'
execution_resource: JGI
git_url: https://github.com/microbiomedata/RawSequencingData
has_input:
- nmdc:unvalidated_placeholder
has_output:
- nmdc:22afa3d49b73eaec2e9787a6b88fbdc3
id: nmdc:bad_id
name: Sequencing Activity for nmdc:mga0vx38
part_of: nmdc:mga0vx38
started_at_time: '2021-08-05T14:48:51+00:00'
type: nmdc:MetagenomeSequencing
version: v1.0.0

```
## Database-biosamples-dna-in-tube-with-well-value
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  dna_cont_type: tube
  dna_cont_well: B2
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  id: nmdc:bsm-99-dtTMNb
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  type: nmdc:Biosample

```
## Biosample-minimal-no-id-but-with-type
### Input
```yaml
associated_studies:
- nmdc:sty-00-abc123
env_broad_scale:
  has_raw_value: ENVO:00002030
  term:
    id: ENVO:00002030
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_local_scale:
  has_raw_value: ENVO:00002169
  term:
    id: ENVO:00002169
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
env_medium:
  has_raw_value: ENVO:00005792
  term:
    id: ENVO:00005792
    type: nmdc:OntologyClass
  type: nmdc:ControlledIdentifiedTermValue
type: nmdc:Biosample

```
## Database-biosamples-dna-in-plate-no-well-val
### Input
```yaml
biosample_set:
- associated_studies:
  - nmdc:sty-00-abc123
  dna_cont_type: plate
  env_broad_scale:
    has_raw_value: ENVO:00002030
    term:
      id: ENVO:00002030
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
      type: nmdc:OntologyClass
    type: nmdc:ControlledIdentifiedTermValue
  geo_loc_name:
    has_raw_value: Lithgow
    type: nmdc:TextValue
  id: nmdc:bsm-99-dtTMNb
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
    type: nmdc:GeolocationValue
  type: nmdc:Biosample

```
