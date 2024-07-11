## Database-biosamples-dna-in-tube
### Input
```yaml
biosample_set:
- dna_cont_type: tube
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
  part_of:
  - nmdc:sty-00-abc123

```
## Database-mags-activities
### Input
```yaml
mags_activity_set:
- binned_contig_num: 489
  ended_at_time: '2021-01-10T00:00:00+00:00'
  execution_resource: NERSC - Cori
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
  name: MAGs activiity 1781_86101
  started_at_time: '2021-01-10T00:00:00+00:00'
  too_short_contig_num: 159810
  type: nmdc:MAGsAnalysisActivity
  unbinned_contig_num: 9483
  was_informed_by: gold:Gp0115663
- binned_contig_num: 206
  ended_at_time: '2021-01-10T00:00:00+00:00'
  execution_resource: NERSC - Cori
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
  name: MAGs activiity 1781_86089
  started_at_time: '2021-01-10T00:00:00+00:00'
  too_short_contig_num: 75364
  type: nmdc:MAGsAnalysisActivity
  unbinned_contig_num: 2806
  was_informed_by: gold:Gp0115664

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

```
## ChromatographicSeparationProcess-compilation_example
### Input
```yaml
has_input:
- nmdc:procsm-11-9gjxns61
has_output:
- nmdc:procsm-11-05g48p90
- nmdc:procsm-11-05g48p91
id: nmdc:psp-99-oW43DzG0
ordered_mobile_phases:
- has_solution_components:
  - compound: methanol
    concentration:
      has_numeric_value: 10
      has_unit: mM
  - compound: chloridic acid
    concentration:
      has_numeric_value: 15
      has_unit: mM
  volume:
    has_numeric_value: 500
    has_unit: mL
stationary_phase: CN

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
  execution_resource: LANL B-div
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
  was_informed_by: gold:Gp0061273
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
  execution_resource: LANL B-div
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
  was_informed_by: gold:Gp0061274
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
  execution_resource: LANL B-div
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
  was_informed_by: gold:Gp0061275

```
## Database-nom_analysis_activity_set
### Input
```yaml
nom_analysis_activity_set:
- ended_at_time: '2018-11-13T20:20:39+00:00'
  execution_resource: xxx
  git_url: xxx
  has_input:
  - nmdc:1
  - nmdc:2
  has_output:
  - nmdc:3
  - nmdc:4
  id: nmdc:wfnom-99-abcdefg
  started_at_time: '2018-11-13T20:20:39+00:00'
  type: xxx
  was_informed_by: nmdc:act-99-abcdefg

```
## Database-nmdc-example
### Input
```yaml
biosample_set:
- add_date: 17-MAR-17 04.55.54.717000000 PM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: 'Sweden: Stordalen'
  gold_biosample_identifiers:
  - gold:Gb0150408
  habitat: Fen
  id: nmdc:bsm-99-isqhuW
  lat_lon:
    has_raw_value: 68.35 19.05
    latitude: 68.35
    longitude: 19.05
  location: Stordalen Mire, Sweden
  mod_date: 08-JAN-20 02.49.23.000000000 PM
  name: Permafrost microbial communities from Stordalen Mire, Sweden - 611E1M metaG
  ncbi_taxonomy_name: permafrost metagenome
  part_of:
  - nmdc:sty-00-8675309
  samp_name: 11E1M metaG
  sample_collection_site: Mire fen
  specific_ecosystem: Permafrost
  type: nmdc:Biosample
- add_date: 17-AUG-17 05.38.34.719000000 PM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: 'USA: Massachusetts'
  gold_biosample_identifiers:
  - gold:Gb0157174
  habitat: soil
  id: nmdc:bsm-99-dge3H9
  lat_lon:
    has_raw_value: 42.481016 -72.178343
    latitude: 42.481016
    longitude: -72.178343
  location: Barre Woods Harvard Forest LTER site, Petersham, Massachusetts, United
    States
  mod_date: 08-JAN-20 02.49.23.000000000 PM
  name: Forest soil microbial communities from Barre Woods Harvard Forest LTER site,
    Petersham, Massachusetts, United States - Inc-BW-C-14-O
  ncbi_taxonomy_name: soil metagenome
  part_of:
  - nmdc:sty-00-8675309
  samp_name: Inc-BW-C-14-O
  sample_collection_site: forest soil
  specific_ecosystem: Forest Soil
  type: nmdc:Biosample
- add_date: 29-MAR-18 01.27.40.709000000 PM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: 'USA: Seattle, Washington'
  gold_biosample_identifiers:
  - gold:Gb0188037
  habitat: rhizosphere
  host_name: Carex aquatilis
  id: nmdc:bsm-99-dc6tg6
  lat_lon:
    has_raw_value: 47.6516 -122.3045
    latitude: 47.6516
    longitude: -122.3045
  location: University of Washington, Seatle, WA, United States
  mod_date: 08-JAN-20 02.49.25.000000000 PM
  name: Rhizosphere microbial communities from Carex aquatilis grown in University
    of Washington, Seatle, WA, United States - 4-1-23 metaG
  ncbi_taxonomy_name: rhizosphere metagenome
  part_of:
  - nmdc:sty-00-8675309
  samp_name: 4-1-23 metaG
  sample_collection_site: Peat Soil
  specific_ecosystem: Unclassified
  type: nmdc:Biosample
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
omics_processing_set:
- add_date: 17-AUG-17 05.08.38.451000000 PM
  alternative_identifiers:
  - gold:Gp0225767
  description: Forest soil from Barre Woods Harvard Forest LTER site was incubated
    at 10C with heavy water. Sample is from a control plot at ambient soil temperature,
    organic horizon - top 4cm of soil
  has_input:
  - nmdc:bsm-00-yellow
  has_output:
  - nmdc:dobj-00-90125
  id: nmdc:omprc-99-9XUVVF
  mod_date: 16-OCT-20 02.04.01.374000000 AM
  name: Forest soil microbial communities from Barre Woods Harvard Forest LTER site,
    Petersham, Massachusetts, United States - Inc-BW-C-14-O
  ncbi_project_name: Forest soil microbial communities from Barre Woods Harvard Forest
    LTER site, Petersham, Massachusetts, United States - Inc-BW-C-14-O
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - nmdc:sty-00-31415
  processing_institution: JGI
  type: nmdc:OmicsProcessing
- add_date: 17-MAR-17 04.55.44.822000000 PM
  alternative_identifiers:
  - gold:Gp0208560
  description: Permafrost microbial communities from Stordalen Mire, Sweden
  has_input:
  - nmdc:bsm-00-green
  has_output:
  - nmdc:dobj-00-pizza
  id: nmdc:omprc-99-dk9vgI
  mod_date: 22-MAY-20 06.38.19.576000000 PM
  name: Permafrost microbial communities from Stordalen Mire, Sweden - 611E1M metaG
  ncbi_project_name: Permafrost microbial communities from Stordalen Mire, Sweden
    - 611E1M metaG
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - nmdc:sty-00-8675309
  processing_institution: JGI
  type: nmdc:OmicsProcessing
- add_date: 29-MAR-18 01.27.30.036000000 PM
  alternative_identifiers:
  - gold:Gp0306221
  description: Rhizosphere microbial communities from Carex aquatilis grown in submerged
    peat from a thermokarst bog, University of Washington, Seatle, WA, United States
  has_input:
  - nmdc:bsm-00-blue
  has_output:
  - nmdc:dobj-00-mobydick
  id: nmdc:omprc-99-MVW1FV
  mod_date: 04-APR-20 08.26.35.067000000 AM
  name: Rhizosphere microbial communities from Carex aquatilis grown in University
    of Washington, Seatle, WA, United States - 4-1-23 metaG
  ncbi_project_name: Rhizosphere microbial communities from Carex aquatilis grown
    in University of Washington, Seatle, WA, United States - 4-1-23 metaG
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - nmdc:sty-00-avacado
  processing_institution: JGI
  type: nmdc:OmicsProcessing
study_set:
- associated_dois:
  - doi_category: dataset_doi
    doi_provider: osti
    doi_value: doi:10.25585/1488217
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
  specific_ecosystem: Permafrost
  study_category: research_study
  type: nmdc:Study
- associated_dois:
  - doi_category: dataset_doi
    doi_provider: osti
    doi_value: doi:10.25585/1488215
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
  specific_ecosystem: Forest Soil
  study_category: consortium
  type: nmdc:Study
- associated_dois:
  - doi_category: dataset_doi
    doi_provider: osti
    doi_value: doi:10.25585/1488209
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
  study_category: consortium
  study_image:
  - url: https://portal.nersc.gov/project/m3408/profile_images/nmdc_sty-11-34xj1150.jpg
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
  study_category: consortium
  study_image:
  - url: https://portal.nersc.gov/project/m3408/profile_images/nmdc_sty-11-34xj1150.jpg
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
  study_category: consortium
  study_image:
  - url: https://portal.nersc.gov/project/m3408/profile_images/nmdc_sty-11-34xj1150.jpg
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
embargoed: true
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
part_of:
- nmdc:sty-00-abc123

```
## Database-polymorphic-planned-process-set
### Input
```yaml
planned_process_set:
- designated_class: nmdc:Pooling
  id: nmdc:poolp-00-123456
- designated_class: nmdc:Extraction
  has_input:
  - nmdc:bsm-00-435737
  has_output:
  - nmdc:procsm-00-0938548
  id: nmdc:extrp-00-999999
- designated_class: nmdc:LibraryPreparation
  has_input:
  - nmdc:procsm-00-0938548
  has_output:
  - nmdc:procsm-00-sdsdll
  id: nmdc:libprp-00-999999

```
## OmicsProcessing-1
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- gold:Gp0108335
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
omics_type:
  has_raw_value: Metagenome
part_of:
- nmdc:sty-00-555xxx
processing_institution: JGI
type: nmdc:OmicsProcessing

```
## Database-biosamples-infiltrations
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  - 00:01:32
  - 00:00:53
  part_of:
  - nmdc:sty-00-abc123
- env_broad_scale:
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
  id: nmdc:bsm-99-abcdef
  infiltrations:
  - 00:02:54
  part_of:
  - nmdc:sty-00-abc123
- env_broad_scale:
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
  id: nmdc:bsm-99-qwerty
  infiltrations:
  - 01:24:03
  - 00:02:33
  - 00:02:02
  part_of:
  - nmdc:sty-00-abc123

```
## Biosample-exhaustive-issue-796-bye-yq-for-7-4-10
### Input
```yaml
add_date: '2021-03-31'
agrochem_addition:
- has_raw_value: lime;1 kg/acre;2022-11-16T16:05:42+0000
air_temp_regm:
- has_raw_value: 25 degree Celsius;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
al_sat:
  has_raw_value: 0.1 mg/kg
al_sat_meth:
  has_raw_value: https://journaljeai.com/index.php/JEAI/article/view/583
alkalinity:
  has_raw_value: 50 milligram per liter
alkalinity_method:
  has_raw_value: https://wrrc.umass.edu/research/projects/acid-rain-monitoring-project/analysis-method-ph-and-alkalinity
alkyl_diethers:
  has_raw_value: 0.005 mole per liter
alt:
  has_raw_value: 100 meter
alternative_identifiers:
- generic:abc123
aminopept_act:
  has_raw_value: 0.269 mole per liter per hour
ammonium:
  has_raw_value: 1.5 milligram per liter
ammonium_nitrogen:
  has_raw_value: 0.5 milligram per liter
analysis_type:
- metabolomics
- metagenomics
annual_precpt:
  has_raw_value: 0.5 milligram per liter
annual_temp:
  has_raw_value: 12.5 degree Celsius
bacteria_carb_prod:
  has_raw_value: 2.53 microgram per liter per hour
biosample_categories:
- LTER
- FICUS
biotic_regm:
  has_raw_value: sample inoculated with Rhizobium spp. Culture
biotic_relationship: parasite
bishomohopanol:
  has_raw_value: 14 microgram per liter
bromide:
  has_raw_value: 0.05 parts per million
calcium:
  has_raw_value: 0.2 micromole per liter
carb_nitro_ratio:
  has_raw_value: '0.417361111'
chem_administration:
- has_raw_value: agar [CHEBI:2509];2018-05-11T20:00Z
chloride:
  has_raw_value: 5000 milligram per liter
chlorophyll:
  has_raw_value: 5 milligram per cubic meter
climate_environment:
- has_raw_value: tropical climate;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
collected_from: nmdc:unconstrained_site_identifier_string
collection_date:
  has_raw_value: '2018-05-11'
collection_date_inc: '2023-01-29'
collection_time: 05:42+0000
collection_time_inc: 13:42+0000
community: no_example_from_mixs
crop_rotation:
  has_raw_value: yes;R2/2017-01-01/2018-12-31/P6M
cur_land_use: farmstead
cur_vegetation:
  has_raw_value: MIxS doesn't provide any guidance more specific than "text"
cur_vegetation_meth:
  has_raw_value: https://link.springer.com/article/10.1023/A:1011975321668
density:
  has_raw_value: 1000 kilogram per cubic meter
depth:
  has_maximum_numeric_value: 2.5
  has_minimum_numeric_value: 1.5
  has_numeric_value: 2.0
  has_raw_value: 1.5 to 2.5 meters (that may not be the pattern the submission schema
    expects). Extractions below require external migration logic.
  has_unit: meter
description: unconstrained text
diss_carb_dioxide:
  has_raw_value: 5 milligram per liter
diss_hydrogen:
  has_raw_value: 0.3 micromole per liter
diss_inorg_carb:
  has_raw_value: 2059 micromole per kilogram
diss_inorg_phosp:
  has_raw_value: 56.5 micromole per liter
diss_org_carb:
  has_raw_value: 197 micromole per liter
diss_org_nitro:
  has_raw_value: 0.05 micromole per liter
diss_oxygen:
  has_raw_value: 175 micromole per kilogram
dna_absorb1: 2.02
dna_absorb2: 2.02
dna_collect_site: untreated pond water
dna_concentration: 100
dna_container_id: Pond_MT_041618
dna_dnase: 'yes'
dna_isolate_meth: phenol/chloroform extraction
dna_organisms: expected to contain microbes (59%) fungi (30%), viruses (10%), tadpoles
  (1%)
dna_project_contact: John Jones
dna_samp_id: '187654'
dna_sample_format: 10 mM Tris-HCl
dna_sample_name: JGI_pond_041618
dna_seq_project: '1191234'
dna_seq_project_name: JGI Pond metagenomics
dna_seq_project_pi: Jane Johnson
dna_volume: 25
dnase_rna: 'yes'
drainage_class: well
ecosystem: unconstrained text. should be validated against the controlled vocabulary,
  by the sample's environmental package. would also be nice to align the CV with MIxS
  environmental triads
ecosystem_category: unconstrained text
ecosystem_subtype: unconstrained text
ecosystem_type: unconstrained text
elev: 100
embargoed: true
emsl_biosample_identifiers:
- generic:abc123
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
env_package:
  has_raw_value: unconstrained text. should require the name of a MIxS EnvironmentalPackage
    class. have asked MIxS to return this term to their model. UPDATE VALIDATION RULES/PATTERN/ENUM!
experimental_factor:
  has_raw_value: unconstrained text, unlike the MIxS environmental triad
experimental_factor_other: unconstrained text, but presumably expects 'term label
  [term id]'
extreme_event: '2023-01-15'
fao_class: Fluvisols
filter_method: Basix PES, 13-100-106 FisherSci is an example value, but unconstrained
  text is accepted at this point
fire: 2000-11 to 2000-12
flooding: '2000-01-15'
gaseous_environment:
- has_raw_value: nitric oxide;0.5 micromole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
geo_loc_name:
  has_raw_value: 'USA: Maryland, Bethesda'
glucosidase_act:
  has_raw_value: 5 mol per liter per hour
gold_biosample_identifiers:
- gold:Gb123456789
- gold:Gb90909090
growth_facil:
  has_raw_value: Growth chamber [CO_715:0000189]
habitat: unconstrained text
heavy_metals:
- has_raw_value: mercury;0.09 micrograms per gram
- has_raw_value: arsenic;0.09 micrograms per gram
heavy_metals_meth:
- has_raw_value: https://link.springer.com/article/10.1007/s42452-019-1578-x
host_name: snail is an example value, but unconstrained text is accepted at this point
host_taxid:
  has_raw_value: NCBITaxon:9606
  term:
    id: NCBITaxon:9606
humidity_regm:
- has_raw_value: 25 gram per cubic meter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
id: nmdc:bsm-99-dtTMNb
igsn_biosample_identifiers:
- any:curie_1
- any:curie_2
img_identifiers:
- img.taxon:abc123
insdc_biosample_identifiers:
- biosample:SAMN123456789
- biosample:SAMN000
isotope_exposure: 13C glucose
lat_lon:
  has_raw_value: 50.586825 6.408977
  latitude: 50.586825
  longitude: 6.408977
lbc_thirty:
  has_raw_value: 543 mg/kg
lbceq:
  has_raw_value: 1575 mg/kg
light_regm:
  has_raw_value: incandescent light;10 lux;450 nanometer
link_addit_analys:
  has_raw_value: https://pubmed.ncbi.nlm.nih.gov/2315679/
link_class_info:
  has_raw_value: https://wisconsindot.gov/Documents/doing-bus/eng-consultants/cnslt-rsrces/geotechmanual/gt-03-03.pdf
link_climate_info:
  has_raw_value: https://www.int-res.com/abstracts/cr/v14/n3/p161-173/
local_class:
  has_raw_value: jicama soil
local_class_meth:
  has_raw_value: https://www.sciencedirect.com/science/article/abs/pii/S0016706105003083
location: unconstrained text. should we even keep this slot? check if it ahs been
  used in MongoDB.
magnesium:
  has_raw_value: 52.8 micromole per kilogram
manganese:
  has_raw_value: 24.7 mg/kg
mean_frict_vel:
  has_raw_value: 0.5 meter per second
mean_peak_frict_vel:
  has_raw_value: 1 meter per second
micro_biomass_c_meth: https://acsess.onlinelibrary.wiley.com/doi/abs/10.2136/sssaspecpub49.c12
micro_biomass_n_meth: https://acsess.onlinelibrary.wiley.com/doi/abs/10.2136/sssaspecpub49.c12
microbial_biomass_c: 0.05 ug C/g dry soil
microbial_biomass_n: 0.05 ug N/g dry soil
misc_param:
- has_raw_value: Bicarbonate ion concentration;2075 micromole per kilogram
mod_date: '2023-01-25'
n_alkanes:
- has_raw_value: n-hexadecane;100 milligram per liter
name: Sample Exhaustive Biosample instance. Although all of these values should pass
  validation, that does not mean that any Biosample of any type would necessarily
  have this particular combination of values.
ncbi_taxonomy_name: soil metagenome
nitrate:
  has_raw_value: 65 micromole per liter
nitrate_nitrogen:
  has_raw_value: 0.29 mg/kg
nitrite:
  has_raw_value: 0.5 micromole per liter
nitrite_nitrogen:
  has_raw_value: 1.2 mg/kg
non_microb_biomass: insect 0.23 ug; plant 1g
non_microb_biomass_method: https://doi.org/10.1038/s41467-021-26181-3
org_matter:
  has_raw_value: 1.75 milligram per cubic meter
org_nitro:
  has_raw_value: 4 micromole per liter
org_nitro_method: https://doi.org/10.1016/0038-0717(85)90144-0
organism_count:
- has_raw_value: ATP
other_treatment: unconstrained text
oxy_stat_samp: aerobic
part_of:
- nmdc:sty-00-987654
- nmdc:sty-00-qwerty
part_org_carb:
  has_raw_value: 1.92 micromole per liter
perturbation:
- has_raw_value: antibiotic addition;R2/2018-05-11T14:30Z/2018-05-11T19:30Z/P1H30M
petroleum_hydrocarb:
  has_raw_value: 0.05 micromole per liter
ph: 11.22
ph_meth:
  has_raw_value: https://www.epa.gov/sites/production/files/2015-12/documents/9040c.pdf
phaeopigments:
- has_raw_value: 2.5 milligram per cubic meter
phosphate:
  has_raw_value: 0.7 micromole per liter
phosplipid_fatt_acid:
- has_raw_value: 2.98 milligram per liter
pool_dna_extracts:
  has_raw_value: yes, 5
potassium:
  has_raw_value: 463 milligram per liter
pressure:
  has_raw_value: 50 atmosphere
profile_position: summit
project_id: no example from MIxS
proport_woa_temperature: no example from MIxS
proposal_dna: '504000'
proposal_rna: '504000'
redox_potential:
  has_raw_value: 300 millivolt
replicate_number: '1'
rna_absorb1: 2.02
rna_absorb2: 2.02
rna_collect_site: untreated pond water
rna_concentration: 100
rna_cont_type: plate
rna_cont_well: C2
rna_container_id: Pond_MT_041618
rna_isolate_meth: phenol/chloroform extraction
rna_organisms: expected to contain microbes (59%) fungi (30%), viruses (10%), tadpoles
  (1%)
rna_project_contact: John Jones
rna_samp_id: '187654'
rna_sample_format: 10 mM Tris-HCl
rna_sample_name: JGI_pond_041618
rna_seq_project: '1191234'
rna_seq_project_name: JGI Pond metagenomics
rna_seq_project_pi: Jane Johnson
rna_volume: 25
salinity:
  has_raw_value: 25 practical salinity unit
salinity_category: halotolerant is an example from the schema, but MIxS doesn't provide
  this slot any more
salinity_meth:
  has_raw_value: PMID:22895776
samp_collec_method: swabbing
samp_mat_process:
  has_raw_value: filtering of seawater
samp_name: see also name
samp_size:
  has_raw_value: 5 liters
samp_store_dur:
  has_raw_value: P1Y6M
samp_store_loc:
  has_raw_value: Freezer no:5
samp_store_temp:
  has_raw_value: -80 degree Celsius
samp_taxon_id:
  has_raw_value: soil metagenome [NCBItaxon:410658]
  term:
    id: NCBItaxon:410658
    name: soil metagenome
samp_vol_we_dna_ext:
  has_raw_value: 1500 milliliter
sample_collection_site: unconstrained text
sample_link:
- IGSN:DSJ0284
- any:curie
sample_shipped: 15 g
sample_type: soil - water extract
season_precpt:
  has_raw_value: 75 millimeters
season_temp:
  has_raw_value: 18 degree Celsius
sieving:
  has_raw_value: MIxS does not provide an example
size_frac_low:
  has_raw_value: 0.2 micrometer
size_frac_up:
  has_raw_value: 20 micrometer
slope_aspect:
  has_raw_value: MIxS does not provide an example
slope_gradient:
  has_raw_value: MIxS does not provide an example
sodium:
  has_raw_value: 10.5 milligram per liter
soil_type:
  has_raw_value: plinthosol [ENVO:00002250]
soil_type_meth:
  has_raw_value: Frederick series
soluble_iron_micromol: MIxS doesn't provide an example
source_mat_id:
  has_raw_value: MPI012345
specific_ecosystem: unconstrained text
start_date_inc: '2023-01-27'
start_time_inc: 13:42+0000
store_cond:
  has_raw_value: -20 degree Celsius freezer;P2Y10D
subsurface_depth:
  has_raw_value: MIxS does not provide an example
sulfate:
  has_raw_value: 5 micromole per liter
sulfide:
  has_raw_value: 2 micromole per liter
technical_reps: '2'
temp:
  has_raw_value: 25 degree Celsius
tidal_stage: high tide
tillage:
- chisel
tot_carb:
  has_raw_value: MIxS does not provide an example
tot_depth_water_col:
  has_raw_value: 500 meter
tot_diss_nitro:
  has_raw_value: 40 microgram per liter
tot_nitro_cont_meth: https://currentprotocols.onlinelibrary.wiley.com/doi/abs/10.1002/0471142913.fab0102s00
tot_nitro_content:
  has_raw_value: 35 milligrams Nitrogen per kilogram of soil
tot_org_c_meth:
  has_raw_value: https://www.epa.gov/sites/production/files/2015-12/documents/9060a.pdf
tot_org_carb:
  has_raw_value: 2%
tot_phosp:
  has_raw_value: 0.03 milligram per liter
type: nmdc:Biosample. change this to require a class name or an enumeration
water_cont_soil_meth: MIxS doesn't provide an example
water_content:
- MIxS doesn't provide an example 1
- MIxS doesn't provide an example 2
watering_regm:
- has_raw_value: 1 liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
zinc:
  has_raw_value: 2.5 mg/kg

```
## Database-processed_sample-extract-exhaustive
### Input
```yaml
processed_sample_set:
- biomaterial_purity:
    has_numeric_value: 2
  description: Extracted DNA from WOOD_024-M-20190715-COMP
  external_database_identifiers:
  - neon.identifier:19S_31_2826
  id: nmdc:procsm-99-dtTMNb
  name: WOOD_024-M-20190715-COMP-DNA1

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
qc_status: pass
start_date: 2020-06-24T22:06Z

```
## DataObject-mass_spec
### Input
```yaml
data_object_type: LC-DDA-MS/MS Raw Data
description: raw instrument file for nmdc:omprc-11-bn8jcq58
file_size_bytes: 1150434379
id: nmdc:dobj-12-bxzqgh77
md5_checksum: 3EFB4966125DFA9329ADE5B18EADDA8E
name: SpruceW_P19_15_22Jun17_Pippin_17-04-06
url: https://nmdcdemo.emsl.pnnl.gov/proteomics/raw/SpruceW_P19_15_22Jun17_Pippin_17-04-06.raw

```
## Biosample-soil_horizon
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
part_of:
- nmdc:sty-00-abc123
soil_horizon: M horizon

```
## TextValue-raw_value
### Input
```yaml
has_raw_value: 1600 Pennsylvania Ave

```
## ReadQcAnalysisActivity-1
### Input
```yaml
ended_at_time: '2021-09-15T10:13:20+00:00'
execution_resource: execution_resource1
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
started_at_time: '2021-08-05T14:48:51+00:00'
type: type1
was_informed_by: gold:Gp0061273

```
## SubSamplingProcess-minimal
### Input
```yaml
contained_in: V-bottom conical tube
container_size:
  has_numeric_value: 50
  has_unit: mL
has_input:
- nmdc:bsm-99-oW43DzG1
has_output:
- nmdc:procsm-11-05g48p90
id: nmdc:sops-99-oW43DzG0
mass:
  has_numeric_value: 30
  has_unit: g
temperature:
  has_numeric_value: 25
  has_unit: C
volume:
  has_numeric_value: 20
  has_unit: mL

```
## Solution-multiple_components
### Input
```yaml
has_solution_components:
- compound: methanol
  concentration:
    has_numeric_value: 10
    has_unit: mM
- compound: chloridic acid
  concentration:
    has_numeric_value: 15
    has_unit: mM
- compound: trypsin
  concentration:
    has_numeric_value: 20
    has_unit: mM
volume:
  has_numeric_value: 500
  has_unit: mL

```
## Database-neon-story
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  id: nmdc:bsm-99-abcdef1
  part_of:
  - nmdc:sty-00-abc123
- env_broad_scale:
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
  id: nmdc:bsm-99-abcdef2
  part_of:
  - nmdc:sty-00-abc123
- env_broad_scale:
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
  id: nmdc:bsm-99-abcdef3
  part_of:
  - nmdc:sty-00-abc123
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
processed_sample_set:
- id: nmdc:procsm-99-xyz1
  name: first processed sample set
- id: nmdc:procsm-99-xyz2
  name: first DNA extract
- id: nmdc:procsm-99-xyz3
  name: first library

```
## Biosample-exhasutive
### Input
```yaml
abs_air_humidity:
  has_raw_value: xxx
add_date: '2021-03-31'
add_recov_method:
  has_raw_value: xxx
additional_info:
  has_raw_value: xxx
address:
  has_raw_value: xxx
adj_room:
  has_raw_value: xxx
aero_struc:
  has_raw_value: xxx
agrochem_addition:
- has_raw_value: lime;1 kg/acre;2022-11-16T16:05:42+0000
air_PM_concen:
- has_raw_value: xxx
air_temp:
  has_raw_value: xxx
air_temp_regm:
- has_raw_value: 25 degree Celsius;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
al_sat:
  has_raw_value: 0.1 mg/kg
al_sat_meth:
  has_raw_value: https://journaljeai.com/index.php/JEAI/article/view/583
alkalinity:
  has_raw_value: 50 milligram per liter
alkalinity_method:
  has_raw_value: https://wrrc.umass.edu/research/projects/acid-rain-monitoring-project/analysis-method-ph-and-alkalinity
alkyl_diethers:
  has_raw_value: 0.005 mole per liter
alt:
  has_raw_value: 100 meter
alternative_identifiers:
- generic:abc123
aminopept_act:
  has_raw_value: 0.269 mole per liter per hour
ammonium:
  has_raw_value: 1.5 milligram per liter
ammonium_nitrogen:
  has_raw_value: 0.5 milligram per liter
amount_light:
  has_raw_value: xxx
analysis_type:
- metabolomics
- metagenomics
ances_data:
  has_raw_value: xxx
annual_precpt:
  has_raw_value: 0.5 milligram per liter
annual_temp:
  has_raw_value: 12.5 degree Celsius
antibiotic_regm:
- has_raw_value: xxx
api:
  has_raw_value: xxx
arch_struc: building
aromatics_pc:
  has_raw_value: xxx
asphaltenes_pc:
  has_raw_value: xxx
atmospheric_data:
- has_raw_value: xxx
avg_dew_point:
  has_raw_value: xxx
avg_occup:
  has_raw_value: xxx
avg_temp:
  has_raw_value: xxx
bac_prod:
  has_raw_value: xxx
bac_resp:
  has_raw_value: xxx
bacteria_carb_prod:
  has_raw_value: 2.53 microgram per liter per hour
barometric_press:
  has_raw_value: xxx
basin:
  has_raw_value: xxx
bathroom_count:
  has_raw_value: xxx
bedroom_count:
  has_raw_value: xxx
benzene:
  has_raw_value: xxx
biochem_oxygen_dem:
  has_raw_value: xxx
biocide:
  has_raw_value: xxx
biocide_admin_method:
  has_raw_value: xxx
biol_stat: wild
biomass:
- has_raw_value: xxx
biosample_categories:
- LTER
- FICUS
biotic_regm:
  has_raw_value: sample inoculated with Rhizobium spp. Culture
biotic_relationship: parasite
bishomohopanol:
  has_raw_value: 14 microgram per liter
blood_press_diast:
  has_raw_value: xxx
blood_press_syst:
  has_raw_value: xxx
bromide:
  has_raw_value: 0.05 parts per million
build_docs: building information model
build_occup_type:
- office
building_setting: urban
built_struc_age:
  has_raw_value: xxx
built_struc_set:
  has_raw_value: xxx
built_struc_type:
  has_raw_value: xxx
calcium:
  has_raw_value: 0.2 micromole per liter
carb_dioxide:
  has_raw_value: xxx
carb_monoxide:
  has_raw_value: xxx
carb_nitro_ratio:
  has_raw_value: '0.417361111'
ceil_area:
  has_raw_value: xxx
ceil_cond: new
ceil_finish_mat: drywall
ceil_struc:
  has_raw_value: xxx
ceil_texture: crows feet
ceil_thermal_mass:
  has_raw_value: xxx
ceil_type: cathedral
ceil_water_mold:
  has_raw_value: xxx
chem_administration:
- has_raw_value: agar [CHEBI:2509];2018-05-11T20:00Z
chem_mutagen:
- has_raw_value: xxx
chem_oxygen_dem:
  has_raw_value: xxx
chem_treat_method: xxx
chem_treatment:
  has_raw_value: xxx
chimera_check:
  has_raw_value: xxx
chloride:
  has_raw_value: 5000 milligram per liter
chlorophyll:
  has_raw_value: 5 milligram per cubic meter
climate_environment:
- has_raw_value: tropical climate;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
collected_from: nmdc:unconstrained_site_identifier_string
collection_date:
  has_raw_value: xxx
collection_date_inc: '2023-01-29'
collection_time: 05:42+0000
collection_time_inc: 13:42+0000
community: no_example_from_mixs
conduc:
  has_raw_value: xxx
cool_syst_id:
  has_raw_value: xxx
crop_rotation:
  has_raw_value: yes;R2/2017-01-01/2018-12-31/P6M
cult_root_med:
  has_raw_value: xxx
cur_land_use: farmstead
cur_vegetation:
  has_raw_value: MIxS doesn't provide any guidance more specific than "text"
cur_vegetation_meth:
  has_raw_value: https://link.springer.com/article/10.1023/A:1011975321668
date_last_rain:
  has_raw_value: xxx
density:
  has_raw_value: 1000 kilogram per cubic meter
depos_env: other
depth:
  has_maximum_numeric_value: 2.5
  has_minimum_numeric_value: 1.5
  has_numeric_value: 2.0
  has_raw_value: 1.5 to 2.5 meters (that may not be the pattern the submission schema
    expects). Extractions below require external migration logic.
  has_unit: meter
description: unconstrained text
dew_point:
  has_raw_value: xxx
diether_lipids:
- has_raw_value: xxx
diss_carb_dioxide:
  has_raw_value: 5 milligram per liter
diss_hydrogen:
  has_raw_value: 0.3 micromole per liter
diss_inorg_carb:
  has_raw_value: 2059 micromole per kilogram
diss_inorg_nitro:
  has_raw_value: xxx
diss_inorg_phosp:
  has_raw_value: 56.5 micromole per liter
diss_iron:
  has_raw_value: xxx
diss_org_carb:
  has_raw_value: 197 micromole per liter
diss_org_nitro:
  has_raw_value: 0.05 micromole per liter
diss_oxygen:
  has_raw_value: 175 micromole per kilogram
diss_oxygen_fluid:
  has_raw_value: xxx
dna_absorb1: 2.02
dna_absorb2: 2.02
dna_collect_site: untreated pond water
dna_concentration: 100
dna_container_id: Pond_MT_041618
dna_dnase: 'yes'
dna_isolate_meth: phenol/chloroform extraction
dna_organisms: expected to contain microbes (59%) fungi (30%), viruses (10%), tadpoles
  (1%)
dna_project_contact: John Jones
dna_samp_id: '187654'
dna_sample_format: 10 mM Tris-HCl
dna_sample_name: JGI_pond_041618
dna_seq_project: '1191234'
dna_seq_project_name: JGI Pond metagenomics
dna_seq_project_pi: Jane Johnson
dna_volume: 25
dnase_rna: 'yes'
door_comp_type: revolving
door_cond: damaged
door_direct: inward
door_loc: north
door_mat: aluminum
door_move: collapsible
door_size:
  has_raw_value: xxx
door_type: composite
door_type_metal: collapsible
door_type_wood: battened
door_water_mold:
  has_raw_value: xxx
down_par:
  has_raw_value: xxx
drainage_class: well
drawings: operation
ecosystem: unconstrained text. should be validated against the controlled vocabulary,
  by the sample's environmental package. would also be nice to align the CV with MIxS
  environmental triads
ecosystem_category: unconstrained text
ecosystem_subtype: unconstrained text
ecosystem_type: unconstrained text
efficiency_percent:
  has_raw_value: xxx
elev: 100
elevator:
  has_raw_value: xxx
embargoed: true
emsl_biosample_identifiers:
- generic:abc123
emulsions:
- has_raw_value: xxx
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
env_package:
  has_raw_value: unconstrained text. should require the name of a MIxS EnvironmentalPackage
    class. have asked MIxS to return this term to their model. UPDATE VALIDATION RULES/PATTERN/ENUM!
escalator:
  has_raw_value: xxx
ethylbenzene:
  has_raw_value: xxx
exp_duct:
  has_raw_value: xxx
exp_pipe:
  has_raw_value: xxx
experimental_factor:
  has_raw_value: unconstrained text, unlike the MIxS environmental triad
experimental_factor_other: unconstrained text, but presumably expects 'term label
  [term id]'
ext_door:
  has_raw_value: xxx
ext_wall_orient: north
ext_window_orient: north
extreme_event: '2023-01-15'
fao_class: Fluvisols
fertilizer_regm:
- has_raw_value: xxx
field:
  has_raw_value: xxx
filter_method: Basix PES, 13-100-106 FisherSci is an example value, but unconstrained
  text is accepted at this point
filter_type:
- HEPA
fire: 2000-11 to 2000-12
fireplace_type:
  has_raw_value: xxx
flooding: '2000-01-15'
floor_age:
  has_raw_value: xxx
floor_area:
  has_raw_value: xxx
floor_cond: new
floor_count:
  has_raw_value: xxx
floor_finish_mat: tile
floor_struc: balcony
floor_thermal_mass:
  has_raw_value: xxx
floor_water_mold: condensation
fluor:
  has_raw_value: xxx
freq_clean:
  has_raw_value: xxx
freq_cook:
  has_raw_value: xxx
fungicide_regm:
- has_raw_value: xxx
furniture: cabinet
gaseous_environment:
- has_raw_value: nitric oxide;0.5 micromole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
gaseous_substances:
- has_raw_value: xxx
gender_restroom: female
genetic_mod:
  has_raw_value: xxx
geo_loc_name:
  has_raw_value: 'USA: Maryland, Bethesda'
glucosidase_act:
  has_raw_value: 5 mol per liter per hour
gold_biosample_identifiers:
- gold:Gb123456789
- gold:Gb90909090
gravidity:
  has_raw_value: xxx
gravity:
- has_raw_value: xxx
growth_facil:
  has_raw_value: Growth chamber [CO_715:0000189]
growth_habit: erect
growth_hormone_regm:
- has_raw_value: xxx
habitat: unconstrained text
hall_count:
  has_raw_value: xxx
handidness: ambidexterity
hc_produced: Oil
hcr: Shale
hcr_fw_salinity:
  has_raw_value: xxx
hcr_geol_age: Archean
hcr_pressure:
  has_raw_value: xxx
hcr_temp:
  has_raw_value: xxx
heat_cool_type:
- radiant system
heat_deliv_loc: north
heat_sys_deliv_meth: xxx
heat_system_id:
  has_raw_value: xxx
heavy_metals:
- has_raw_value: mercury;0.09 micrograms per gram
- has_raw_value: arsenic;0.09 micrograms per gram
heavy_metals_meth:
- has_raw_value: https://link.springer.com/article/10.1007/s42452-019-1578-x
height_carper_fiber:
  has_raw_value: xxx
herbicide_regm:
- has_raw_value: xxx
horizon_meth:
  has_raw_value: xxx
host_age:
  has_raw_value: xxx
host_body_habitat:
  has_raw_value: xxx
host_body_product:
  has_raw_value: xxx
host_body_site:
  has_raw_value: xxx
host_body_temp:
  has_raw_value: xxx
host_color:
  has_raw_value: xxx
host_common_name:
  has_raw_value: xxx
host_diet:
- has_raw_value: xxx
host_dry_mass:
  has_raw_value: xxx
host_family_relation:
- xxx
host_genotype:
  has_raw_value: xxx
host_growth_cond:
  has_raw_value: xxx
host_height:
  has_raw_value: xxx
host_last_meal:
- has_raw_value: xxx
host_length:
  has_raw_value: xxx
host_life_stage:
  has_raw_value: xxx
host_name: snail is an example value, but unconstrained text is accepted at this point
host_phenotype:
  has_raw_value: xxx
host_sex: female
host_shape:
  has_raw_value: xxx
host_subject_id:
  has_raw_value: xxx
host_subspecf_genlin:
- xxx
host_substrate:
  has_raw_value: xxx
host_symbiont:
- xxx
host_taxid:
  has_raw_value: NCBITaxon:9606
  term:
    id: NCBITaxon:9606
host_tot_mass:
  has_raw_value: xxx
host_wet_mass:
  has_raw_value: xxx
humidity:
  has_raw_value: xxx
humidity_regm:
- has_raw_value: 25 gram per cubic meter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
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
inorg_particles:
- has_raw_value: xxx
insdc_biosample_identifiers:
- biosample:SAMN123456789
- biosample:SAMN000
inside_lux:
  has_raw_value: xxx
int_wall_cond: new
isotope_exposure: 13C glucose
iw_bt_date_well:
  has_raw_value: xxx
iwf:
  has_raw_value: xxx
last_clean:
  has_raw_value: xxx
lat_lon:
  has_raw_value: 50.586825 6.408977
  latitude: 50.586825
  longitude: 6.408977
lbc_thirty:
  has_raw_value: 543 mg/kg
lbceq:
  has_raw_value: 1575 mg/kg
light_intensity:
  has_raw_value: xxx
light_regm:
  has_raw_value: incandescent light;10 lux;450 nanometer
light_type:
- none
link_addit_analys:
  has_raw_value: https://pubmed.ncbi.nlm.nih.gov/2315679/
link_class_info:
  has_raw_value: https://wisconsindot.gov/Documents/doing-bus/eng-consultants/cnslt-rsrces/geotechmanual/gt-03-03.pdf
link_climate_info:
  has_raw_value: https://www.int-res.com/abstracts/cr/v14/n3/p161-173/
lithology: Basement
local_class:
  has_raw_value: jicama soil
local_class_meth:
  has_raw_value: https://www.sciencedirect.com/science/article/abs/pii/S0016706105003083
location: unconstrained text. should we even keep this slot? check if it has been
  used in MongoDB.
magnesium:
  has_raw_value: 52.8 micromole per kilogram
manganese:
  has_raw_value: 24.7 mg/kg
max_occup:
  has_raw_value: xxx
mean_frict_vel:
  has_raw_value: 0.5 meter per second
mean_peak_frict_vel:
  has_raw_value: 1 meter per second
mech_struc: subway
mechanical_damage:
- has_raw_value: xxx
methane:
  has_raw_value: xxx
micro_biomass_c_meth: https://acsess.onlinelibrary.wiley.com/doi/abs/10.2136/sssaspecpub49.c12
micro_biomass_meth: xxx
micro_biomass_n_meth: https://acsess.onlinelibrary.wiley.com/doi/abs/10.2136/sssaspecpub49.c12
microbial_biomass:
  has_raw_value: xxx
microbial_biomass_c: 0.05 ug C/g dry soil
microbial_biomass_n: 0.05 ug N/g dry soil
mineral_nutr_regm:
- has_raw_value: xxx
misc_param:
- has_raw_value: Bicarbonate ion concentration;2075 micromole per kilogram
mod_date: '2023-01-25'
n_alkanes:
- has_raw_value: n-hexadecane;100 milligram per liter
name: Sample Exhaustive Biosample instance. Although all of these values should pass
  validation, that does not mean that any Biosample of any type would necessarily
  have this particular combination of values.
ncbi_taxonomy_name: soil metagenome
nitrate:
  has_raw_value: 65 micromole per liter
nitrite:
  has_raw_value: 0.5 micromole per liter
nitrite_nitrogen:
  has_raw_value: 1.2 mg/kg
nitro:
  has_raw_value: xxx
non_microb_biomass: insect 0.23 ug; plant 1g
non_microb_biomass_method: https://doi.org/10.1038/s41467-021-26181-3
non_min_nutr_regm:
- xxx
nucl_acid_amp:
  has_raw_value: xxx
nucl_acid_ext:
  has_raw_value: xxx
number_pets:
  has_raw_value: xxx
number_plants:
  has_raw_value: xxx
number_resident:
  has_raw_value: xxx
occup_density_samp:
  has_raw_value: xxx
occup_document: estimate
occup_samp:
  has_raw_value: xxx
org_carb:
  has_raw_value: xxx
org_count_qpcr_info: xxx
org_matter:
  has_raw_value: 1.75 milligram per cubic meter
org_nitro:
  has_raw_value: 4 micromole per liter
org_nitro_method: https://doi.org/10.1016/0038-0717(85)90144-0
org_particles:
- has_raw_value: xxx
organism_count:
- has_raw_value: ATP
other_treatment: unconstrained text
owc_tvdss:
  has_raw_value: xxx
oxy_stat_samp: aerobic
oxygen:
  has_raw_value: xxx
part_of:
- nmdc:sty-00-987654
- nmdc:sty-00-qwerty
part_org_carb:
  has_raw_value: 1.92 micromole per liter
part_org_nitro:
  has_raw_value: xxx
particle_class:
- has_raw_value: xxx
pcr_cond:
  has_raw_value: xxx
pcr_primers:
  has_raw_value: xxx
permeability:
  has_raw_value: xxx
perturbation:
- has_raw_value: antibiotic addition;R2/2018-05-11T14:30Z/2018-05-11T19:30Z/P1H30M
pesticide_regm:
- has_raw_value: xxx
petroleum_hydrocarb:
  has_raw_value: 0.05 micromole per liter
ph: 99.99
ph_meth:
  has_raw_value: https://www.epa.gov/sites/production/files/2015-12/documents/9040c.pdf
ph_regm:
- has_raw_value: xxx
phaeopigments:
- has_raw_value: 2.5 milligram per cubic meter
phosphate:
  has_raw_value: 0.7 micromole per liter
phosplipid_fatt_acid:
- has_raw_value: 2.98 milligram per liter
photon_flux:
  has_raw_value: xxx
plant_growth_med:
  has_raw_value: xxx
plant_product:
  has_raw_value: xxx
plant_sex: Androdioecious
plant_struc:
  has_raw_value: xxx
pollutants:
- has_raw_value: xxx
pool_dna_extracts:
  has_raw_value: yes, 5
porosity:
  has_raw_value: xxx
potassium:
  has_raw_value: 463 milligram per liter
pour_point:
  has_raw_value: xxx
pre_treatment:
  has_raw_value: xxx
pres_animal_insect: cat;3
pressure:
  has_raw_value: 50 atmosphere
prev_land_use_meth: xxx
previous_land_use:
  has_raw_value: xxx
primary_prod:
  has_raw_value: xxx
primary_treatment:
  has_raw_value: xxx
prod_rate:
  has_raw_value: xxx
prod_start_date:
  has_raw_value: xxx
profile_position: summit
project_id: no example from MIxS
proport_woa_temperature: no example from MIxS
proposal_dna: '504000'
proposal_rna: '504000'
quad_pos: North side
radiation_regm:
- has_raw_value: xxx
rainfall_regm:
- has_raw_value: xxx
reactor_type:
  has_raw_value: xxx
redox_potential:
  has_raw_value: 300 millivolt
rel_air_humidity:
  has_raw_value: xxx
rel_humidity_out:
  has_raw_value: xxx
rel_samp_loc: edge of car
replicate_number: '1'
reservoir:
  has_raw_value: xxx
resins_pc:
  has_raw_value: xxx
rna_absorb1: 2.02
rna_absorb2: 2.02
rna_collect_site: untreated pond water
rna_concentration: 100
rna_container_id: Pond_MT_041618
rna_isolate_meth: phenol/chloroform extraction
rna_organisms: expected to contain microbes (59%) fungi (30%), viruses (10%), tadpoles
  (1%)
rna_project_contact: John Jones
rna_samp_id: '187654'
rna_sample_format: 10 mM Tris-HCl
rna_sample_name: JGI_pond_041618
rna_seq_project: '1191234'
rna_seq_project_name: JGI Pond metagenomics
rna_seq_project_pi: Jane Johnson
rna_volume: 25
room_air_exch_rate:
  has_raw_value: xxx
room_architec_elem: xxx
room_condt: new
room_connected: attic
room_count:
  has_raw_value: xxx
room_dim:
  has_raw_value: xxx
room_door_dist:
  has_raw_value: xxx
room_door_share:
  has_raw_value: xxx
room_hallway:
  has_raw_value: xxx
room_loc: corner room
room_moist_dam_hist: 123
room_net_area:
  has_raw_value: xxx
room_occup:
  has_raw_value: xxx
room_samp_pos: north corner
room_type: attic
room_vol:
  has_raw_value: xxx
room_wall_share:
  has_raw_value: xxx
room_window_count: 123
root_cond:
  has_raw_value: xxx
root_med_carbon:
  has_raw_value: xxx
root_med_macronutr:
  has_raw_value: xxx
root_med_micronutr:
  has_raw_value: xxx
root_med_ph:
  has_raw_value: xxx
root_med_regl:
  has_raw_value: xxx
root_med_solid:
  has_raw_value: xxx
root_med_suppl:
  has_raw_value: xxx
salinity:
  has_raw_value: 25 practical salinity unit
salinity_category: halotolerant is an example from the schema, but MIxS doesn't provide
  this slot any more
salinity_meth:
  has_raw_value: PMID:22895776
salt_regm:
- has_raw_value: xxx
samp_capt_status: other
samp_collec_device: xxx
samp_collec_method: swabbing
samp_collect_point: well
samp_dis_stage: dissemination
samp_floor: basement
samp_loc_corr_rate:
  has_raw_value: xxx
samp_mat_process:
  has_raw_value: filtering of seawater
samp_md:
  has_raw_value: xxx
samp_name: see also name
samp_preserv:
  has_raw_value: xxx
samp_room_id:
  has_raw_value: xxx
samp_size:
  has_raw_value: 5 liters
samp_sort_meth:
- has_raw_value: xxx
samp_store_dur:
  has_raw_value: P1Y6M
samp_store_loc:
  has_raw_value: Freezer no:5
samp_store_temp:
  has_raw_value: -80 degree Celsius
samp_subtype: biofilm
samp_taxon_id:
  has_raw_value: soil metagenome [NCBItaxon:410658]
  term:
    id: NCBItaxon:410658
    name: soil metagenome
samp_time_out:
  has_raw_value: xxx
samp_transport_cond:
  has_raw_value: xxx
samp_tvdss:
  has_raw_value: xxx
samp_type:
  has_raw_value: xxx
samp_vol_we_dna_ext:
  has_raw_value: 1500 milliliter
samp_weather: cloudy
samp_well_name:
  has_raw_value: xxx
sample_collection_site: unconstrained text
sample_link:
- IGSN:DSJ0284
- any:curie
sample_shipped: 15 g
sample_type: soil - water extract
saturates_pc:
  has_raw_value: xxx
season:
  has_raw_value: xxx
season_environment:
- has_raw_value: xxx
season_precpt:
  has_raw_value: 75 millimeters
season_temp:
  has_raw_value: 18 degree Celsius
season_use: Spring
secondary_treatment:
  has_raw_value: xxx
sediment_type: biogenous
seq_meth:
  has_raw_value: xxx
seq_quality_check:
  has_raw_value: xxx
sewage_type:
  has_raw_value: xxx
shad_dev_water_mold: xxx
shading_device_cond: damaged
shading_device_loc:
  has_raw_value: xxx
shading_device_mat:
  has_raw_value: xxx
shading_device_type: tree
sieving:
  has_raw_value: MIxS does not provide an example
silicate:
  has_raw_value: xxx
size_frac:
  has_raw_value: xxx
size_frac_low:
  has_raw_value: 0.2 micrometer
size_frac_up:
  has_raw_value: 20 micrometer
slope_aspect:
  has_raw_value: MIxS does not provide an example
slope_gradient:
  has_raw_value: MIxS does not provide an example
sludge_retent_time:
  has_raw_value: xxx
sodium:
  has_raw_value: 10.5 milligram per liter
soil_horizon: O horizon
soil_text_measure:
  has_raw_value: xxx
soil_texture_meth: xxx
soil_type:
  has_raw_value: plinthosol [ENVO:00002250]
soil_type_meth:
  has_raw_value: Frederick series
solar_irradiance:
  has_raw_value: xxx
soluble_inorg_mat:
- has_raw_value: xxx
soluble_iron_micromol: MIxS doesn't provide an example
soluble_org_mat:
- has_raw_value: xxx
soluble_react_phosp:
  has_raw_value: xxx
source_mat_id:
  has_raw_value: MPI012345
space_typ_state:
  has_raw_value: xxx
specific: operation
specific_ecosystem: unconstrained text
specific_humidity:
  has_raw_value: xxx
sr_dep_env: Lacustine
sr_geol_age: Archean
sr_kerog_type: other
sr_lithology: Clastic
standing_water_regm:
- has_raw_value: xxx
start_date_inc: '2023-01-27'
start_time_inc: 13:42+0000
store_cond:
  has_raw_value: -20 degree Celsius freezer;P2Y10D
substructure_type:
- basement
subsurface_depth:
  has_raw_value: MIxS does not provide an example
sulfate:
  has_raw_value: 5 micromole per liter
sulfate_fw:
  has_raw_value: xxx
sulfide:
  has_raw_value: 2 micromole per liter
surf_air_cont:
- dust
surf_humidity:
  has_raw_value: xxx
surf_material: adobe
surf_moisture:
  has_raw_value: xxx
surf_moisture_ph: 123
surf_temp:
  has_raw_value: xxx
suspend_part_matter:
  has_raw_value: xxx
suspend_solids:
- has_raw_value: xxx
tan:
  has_raw_value: xxx
target_gene:
  has_raw_value: xxx
target_subfragment:
  has_raw_value: xxx
technical_reps: '2'
temp:
  has_raw_value: 25 degree Celsius
temp_out:
  has_raw_value: xxx
tertiary_treatment:
  has_raw_value: xxx
tidal_stage: high tide
tillage:
- chisel
tiss_cult_growth_med:
  has_raw_value: xxx
toluene:
  has_raw_value: xxx
tot_carb:
  has_raw_value: MIxS does not provide an example
tot_depth_water_col:
  has_raw_value: 500 meter
tot_diss_nitro:
  has_raw_value: 40 microgram per liter
tot_inorg_nitro:
  has_raw_value: xxx
tot_iron:
  has_raw_value: xxx
tot_nitro:
  has_raw_value: xxx
tot_nitro_cont_meth: https://currentprotocols.onlinelibrary.wiley.com/doi/abs/10.1002/0471142913.fab0102s00
tot_nitro_content:
  has_raw_value: 35 milligrams Nitrogen per kilogram of soil
tot_org_c_meth:
  has_raw_value: https://www.epa.gov/sites/production/files/2015-12/documents/9060a.pdf
tot_org_carb:
  has_raw_value: 2%
tot_part_carb:
  has_raw_value: xxx
tot_phosp:
  has_raw_value: 0.03 milligram per liter
tot_phosphate:
  has_raw_value: xxx
tot_sulfur:
  has_raw_value: xxx
train_line: red
train_stat_loc: south station above ground
train_stop_loc: end
turbidity:
  has_raw_value: xxx
tvdss_of_hcr_press:
  has_raw_value: xxx
tvdss_of_hcr_temp:
  has_raw_value: xxx
typ_occup_density: 123
type: nmdc:Biosample. change this to require a class name or an enumeration
ventilation_rate:
  has_raw_value: xxx
ventilation_type:
  has_raw_value: xxx
vfa:
  has_raw_value: xxx
vfa_fw:
  has_raw_value: xxx
vis_media: photos
viscosity:
  has_raw_value: xxx
volatile_org_comp:
- has_raw_value: xxx
wall_area:
  has_raw_value: xxx
wall_const_type: frame construction
wall_finish_mat: plaster
wall_height:
  has_raw_value: xxx
wall_loc: north
wall_surf_treatment: painted
wall_texture: knockdown
wall_thermal_mass:
  has_raw_value: xxx
wall_water_mold:
  has_raw_value: xxx
wastewater_type:
  has_raw_value: xxx
water_cont_soil_meth: MIxS doesn't provide an example
water_content:
- MIxS doesn't provide an example 1
- MIxS doesn't provide an example 2
water_current:
  has_raw_value: xxx
water_cut:
  has_raw_value: xxx
water_feat_size:
  has_raw_value: xxx
water_feat_type: fountain
water_prod_rate:
  has_raw_value: xxx
water_temp_regm:
- has_raw_value: xxx
watering_regm:
- has_raw_value: 1 liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
weekday: Monday
win:
  has_raw_value: xxx
wind_direction:
  has_raw_value: xxx
wind_speed:
  has_raw_value: xxx
window_cond: damaged
window_cover: blinds
window_horiz_pos: left
window_loc: north
window_mat: fiberglass
window_open_freq:
  has_raw_value: xxx
window_size:
  has_raw_value: xxx
window_status:
  has_raw_value: xxx
window_type: single-hung sash window
window_vert_pos: bottom
window_water_mold:
  has_raw_value: xxx
xylene:
  has_raw_value: xxx
zinc:
  has_raw_value: 2.5 mg/kg

```
## Study-minimal
### Input
```yaml
id: nmdc:sty-11-ab
study_category: research_study

```
## Database-biosamples-dna-in-plate-valid-well-val
### Input
```yaml
biosample_set:
- dna_cont_type: plate
  dna_cont_well: B2
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
  part_of:
  - nmdc:sty-00-abc123
- dna_cont_type: plate
  dna_cont_well: A10
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
  id: nmdc:bsm-99-000001
  part_of:
  - nmdc:sty-00-abc123
- dna_cont_type: plate
  dna_cont_well: A11
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
  id: nmdc:bsm-99-000002
  part_of:
  - nmdc:sty-00-abc123
- dna_cont_type: plate
  dna_cont_well: H10
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
  id: nmdc:bsm-99-000003
  part_of:
  - nmdc:sty-00-abc123
- dna_cont_type: plate
  dna_cont_well: H11
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
  id: nmdc:bsm-99-000004
  part_of:
  - nmdc:sty-00-abc123
- dna_cont_type: plate
  dna_cont_well: C1
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
  id: nmdc:bsm-99-000005
  part_of:
  - nmdc:sty-00-abc123
- dna_cont_type: plate
  dna_cont_well: C12
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
  id: nmdc:bsm-99-000006
  part_of:
  - nmdc:sty-00-abc123

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
- doi_category: dataset_doi
  doi_provider: kbase
  doi_value: doi:10.1126/science.1456956
- doi_category: award_doi
  doi_provider: jgi
  doi_value: doi:10.1126/science.1234545
- doi_category: data_management_plan_doi
  doi_provider: gsc
  doi_value: doi:10.48321/D1Z60Q
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
    websites:
    - https://www.jcvi.org/
    - https://www.jcvi.org/about/j-craig-venter
  type: any string
- applied_roles:
  - Investigation
  - Supervision
  applies_to_person:
    name: Tanja Davidsen
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
  websites:
  - https://www.jcvi.org/
  - https://www.jcvi.org/about/j-craig-venter
related_identifiers: any string R1
relevant_protocols:
- any string 1
- any string 2
specific_ecosystem: unconstrained text
study_category: research_study
study_image:
- description: Photo of Craig Venter Institute, Rockville, Maryland
  display_order: 1
  has_raw_value: https://upload.wikimedia.org/wikipedia/commons/8/86/J._Craig_Vernter_Institute_Rockville_Maryland.jpg
  url: https://upload.wikimedia.org/wikipedia/commons/8/86/J._Craig_Vernter_Institute_Rockville_Maryland.jpg
- description: Photo of Craig Venter Institute, La Jolla, California
  display_order: 2
  has_raw_value: https://today.ucsd.edu/news_uploads/140213ventor2.jpg
  url: https://today.ucsd.edu/news_uploads/140213ventor2.jpg
title: Sample Exhaustive Biosample instance. Although all of these values should pass
  validation, that does not mean that any Biosample of any type would necessarily
  have this particular combination of values.
type: any string
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
extractant:
  has_solution_components:
  - compound: deionized water
  - compound: ammonium bicarbonate
  - compound: trypsin
    concentration:
      has_numeric_value: 0.05
      has_unit: "\u03BCg/\u03BCL"
has_input:
- nmdc:fasp-37
has_output:
- nmdc:ome-39
id: nmdc:extrp-38-r2pk

```
## Extraction-metabolomics
### Input
```yaml
extractant:
  has_solution_components:
  - compound: deionized water
  - compound: methanol
    concentration:
      has_numeric_value: 5
      has_unit: '%'
has_input:
- nmdc:ome-6
has_output:
- nmdc:ome-8
id: nmdc:extrp-71-r2pk

```
## Database-with-MetagenomeSequencingActivity
### Input
```yaml
metagenome_sequencing_activity_set:
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
  - nmdc:mga0vx38
  started_at_time: '2021-08-05T14:48:51+00:00'
  type: nmdc:MetagenomeSequencing
  version: v1.0.0
  was_informed_by: gold:Gp0213371

```
## Database-biosamples-rna-in-plate-valid-well-val
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  part_of:
  - nmdc:sty-00-abc123
  rna_cont_type: plate
  rna_cont_well: B2
- env_broad_scale:
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
  id: nmdc:bsm-99-000001
  part_of:
  - nmdc:sty-00-abc123
  rna_cont_type: plate
  rna_cont_well: A10
- env_broad_scale:
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
  id: nmdc:bsm-99-000002
  part_of:
  - nmdc:sty-00-abc123
  rna_cont_type: plate
  rna_cont_well: A11
- env_broad_scale:
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
  id: nmdc:bsm-99-000003
  part_of:
  - nmdc:sty-00-abc123
  rna_cont_type: plate
  rna_cont_well: H10
- env_broad_scale:
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
  id: nmdc:bsm-99-000004
  part_of:
  - nmdc:sty-00-abc123
  rna_cont_type: plate
  rna_cont_well: H11
- env_broad_scale:
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
  id: nmdc:bsm-99-000005
  part_of:
  - nmdc:sty-00-abc123
  rna_cont_type: plate
  rna_cont_well: C1
- env_broad_scale:
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
  id: nmdc:bsm-99-000006
  part_of:
  - nmdc:sty-00-abc123
  rna_cont_type: plate
  rna_cont_well: C12

```
## Database-biosamples-sites
### Input
```yaml
biosample_set:
- collected_from: nmdc:frsite-99-SPreao
  description: Root microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA
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
  gold_biosample_identifiers:
  - gold:Gb0305833
  id: nmdc:bsm-99-J9FcnC
  name: Root microbial communities from poplar common garden site in Clatskanie, Oregon,
    USA - BESC-13-CL1_35_33 endosphere
  part_of:
  - nmdc:sty-99-U21mUX
- collected_from: nmdc:frsite-99-SPreao
  description: Rhizosphere soil microbial communities from poplar common garden site
    in Clatskanie, Oregon, USA
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
  gold_biosample_identifiers:
  - gold:Gb0291692
  id: nmdc:bsm-99-BdlWdQ
  name: Rhizosphere soil microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA - BESC-13-CL1_35_33
  part_of:
  - nmdc:sty-99-U21mUX
- collected_from: nmdc:frsite-99-SPreao
  description: Bulk soil microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA
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
  gold_biosample_identifiers:
  - gold:Gb0291582
  id: nmdc:bsm-99-vn74Wq
  name: Bulk soil microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA - BESC-13-CL1_35_33
  part_of:
  - nmdc:sty-99-U21mUX
- collected_from: nmdc:frsite-99-h2mYFG
  description: Root microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA
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
  gold_biosample_identifiers:
  - gold:Gb0305834
  id: nmdc:bsm-99-P8FdpS
  name: Root microbial communities from poplar common garden site in Clatskanie, Oregon,
    USA - BESC-13-CL2_39_29 endosphere
  part_of:
  - nmdc:sty-99-U21mUX
- collected_from: nmdc:frsite-99-h2mYFG
  description: Rhizosphere soil microbial communities from poplar common garden site
    in Clatskanie, Oregon, USA
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
  gold_biosample_identifiers:
  - gold:Gb0291693
  id: nmdc:bsm-99-ugBwz3
  name: Rhizosphere soil microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA - BESC-13-CL2_39_29
  part_of:
  - nmdc:sty-99-U21mUX
- collected_from: nmdc:frsite-99-h2mYFG
  description: Bulk soil microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA
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
  gold_biosample_identifiers:
  - gold:Gb0291583
  id: nmdc:bsm-99-tN5lxM
  name: Bulk soil microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA - BESC-13-CL2_39_29
  part_of:
  - nmdc:sty-99-U21mUX
collecting_biosamples_from_site_set:
- has_input:
  - nmdc:frsite-99-SPreao
  has_output:
  - nmdc:bsm-99-J9FcnC
  - nmdc:bsm-99-BdlWdQ
  - nmdc:bsm-99-vn74Wq
  id: nmdc:clsite-99-Cq00d1
  name: Collection of biosamples from BESC-13-CL1_35_33
- has_input:
  - nmdc:frsite-99-h2mYFG
  has_output:
  - nmdc:bsm-99-P8FdpS
  - nmdc:bsm-99-ugBwz3
  - nmdc:bsm-99-tN5lxM
  id: nmdc:clsite-99-yzmLBN
  name: Collection of biosamples from BESC-13-CL2_39_29
field_research_site_set:
- description: Bioscales tree BESC-13-CL1_35_33
  id: nmdc:frsite-99-SPreao
  name: BESC-13-CL1_35_33
- description: Bioscales tree BESC-13-CL2_39_29
  id: nmdc:frsite-99-h2mYFG
  name: BESC-13-CL2_39_29

```
## MetagenomeSequencingActivity-from-metagenome_seequencing_activity_json
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
- nmdc:mga0vx38
started_at_time: '2021-08-05T14:48:51+00:00'
type: nmdc:MetagenomeSequencing
version: v1.0.0
was_informed_by: gold:Gp0213371

```
## FunctionalAnnotation-minimal
### Input
```yaml
has_function: KEGG_PATHWAY:abc12345

```
## Database-MetabolomicsAnalysisActivity-1
### Input
```yaml
metabolomics_analysis_activity_set:
- ended_at_time: '2021-09-15T10:13:20+00:00'
  execution_resource: NERSC cori
  git_url: https://example.org/WorkflowExecutionActivity
  has_calibration: calibration with 0.01% phosphoric acid
  has_input:
  - nmdc:i1
  - nmdc:i2
  has_output:
  - nmdc:o1
  - nmdc:o2
  id: nmdc:wfmb-99-ABCDEF
  name: Metabolomics Analysis Activity for nmdc:wfmb-99-ABCDEF
  started_at_time: '2021-08-05T14:48:51+00:00'
  type: WorkflowExecutionActivity
  was_informed_by: nmdc:a1

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
md5_checksum: 22afa3d49b73eaec2e9787a6b88fbdc3
name: Crispr Terms
type: nmdc:DataObject
url: http://example.com
was_generated_by: nmdc:invalid_id

```
## Biosample-minimal
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
part_of:
- nmdc:sty-00-abc123

```
## Database-biosample-exhasutive
### Input
```yaml
biosample_set:
- abs_air_humidity:
    has_raw_value: xxx
  add_date: '2021-03-31'
  add_recov_method:
    has_raw_value: xxx
  additional_info:
    has_raw_value: xxx
  address:
    has_raw_value: xxx
  adj_room:
    has_raw_value: xxx
  aero_struc:
    has_raw_value: xxx
  agrochem_addition:
  - has_raw_value: lime;1 kg/acre;2022-11-16T16:05:42+0000
  air_PM_concen:
  - has_raw_value: xxx
  air_temp:
    has_raw_value: xxx
  air_temp_regm:
  - has_raw_value: 25 degree Celsius;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
  al_sat:
    has_raw_value: 0.1 mg/kg
  al_sat_meth:
    has_raw_value: https://journaljeai.com/index.php/JEAI/article/view/583
  alkalinity:
    has_raw_value: 50 milligram per liter
  alkalinity_method:
    has_raw_value: https://wrrc.umass.edu/research/projects/acid-rain-monitoring-project/analysis-method-ph-and-alkalinity
  alkyl_diethers:
    has_raw_value: 0.005 mole per liter
  alt:
    has_raw_value: 100 meter
  alternative_identifiers:
  - generic:abc123
  aminopept_act:
    has_raw_value: 0.269 mole per liter per hour
  ammonium:
    has_raw_value: 1.5 milligram per liter
  ammonium_nitrogen:
    has_raw_value: 0.5 milligram per liter
  amount_light:
    has_raw_value: xxx
  analysis_type:
  - metabolomics
  - metagenomics
  ances_data:
    has_raw_value: xxx
  annual_precpt:
    has_raw_value: 0.5 milligram per liter
  annual_temp:
    has_raw_value: 12.5 degree Celsius
  antibiotic_regm:
  - has_raw_value: xxx
  api:
    has_raw_value: xxx
  arch_struc: building
  aromatics_pc:
    has_raw_value: xxx
  asphaltenes_pc:
    has_raw_value: xxx
  atmospheric_data:
  - has_raw_value: xxx
  avg_dew_point:
    has_raw_value: xxx
  avg_occup:
    has_raw_value: xxx
  avg_temp:
    has_raw_value: xxx
  bac_prod:
    has_raw_value: xxx
  bac_resp:
    has_raw_value: xxx
  bacteria_carb_prod:
    has_raw_value: 2.53 microgram per liter per hour
  barometric_press:
    has_raw_value: xxx
  basin:
    has_raw_value: xxx
  bathroom_count:
    has_raw_value: xxx
  bedroom_count:
    has_raw_value: xxx
  benzene:
    has_raw_value: xxx
  biochem_oxygen_dem:
    has_raw_value: xxx
  biocide:
    has_raw_value: xxx
  biocide_admin_method:
    has_raw_value: xxx
  biol_stat: wild
  biomass:
  - has_raw_value: xxx
  biosample_categories:
  - LTER
  - FICUS
  biotic_regm:
    has_raw_value: sample inoculated with Rhizobium spp. Culture
  biotic_relationship: parasite
  bishomohopanol:
    has_raw_value: 14 microgram per liter
  blood_press_diast:
    has_raw_value: xxx
  blood_press_syst:
    has_raw_value: xxx
  bromide:
    has_raw_value: 0.05 parts per million
  build_docs: building information model
  build_occup_type:
  - office
  building_setting: urban
  built_struc_age:
    has_raw_value: xxx
  built_struc_set:
    has_raw_value: xxx
  built_struc_type:
    has_raw_value: xxx
  calcium:
    has_raw_value: 0.2 micromole per liter
  carb_dioxide:
    has_raw_value: xxx
  carb_monoxide:
    has_raw_value: xxx
  carb_nitro_ratio:
    has_raw_value: '0.417361111'
  ceil_area:
    has_raw_value: xxx
  ceil_cond: new
  ceil_finish_mat: drywall
  ceil_struc:
    has_raw_value: xxx
  ceil_texture: crows feet
  ceil_thermal_mass:
    has_raw_value: xxx
  ceil_type: cathedral
  ceil_water_mold:
    has_raw_value: xxx
  chem_administration:
  - has_raw_value: agar [CHEBI:2509];2018-05-11T20:00Z
  chem_mutagen:
  - has_raw_value: xxx
  chem_oxygen_dem:
    has_raw_value: xxx
  chem_treat_method: xxx
  chem_treatment:
    has_raw_value: xxx
  chimera_check:
    has_raw_value: xxx
  chloride:
    has_raw_value: 5000 milligram per liter
  chlorophyll:
    has_raw_value: 5 milligram per cubic meter
  climate_environment:
  - has_raw_value: tropical climate;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
  collected_from: nmdc:unconstrained_site_identifier_string
  collection_date:
    has_raw_value: xxx
  collection_date_inc: '2023-01-29'
  collection_time: 05:42+0000
  collection_time_inc: 13:42+0000
  community: no_example_from_mixs
  conduc:
    has_raw_value: xxx
  cool_syst_id:
    has_raw_value: xxx
  crop_rotation:
    has_raw_value: yes;R2/2017-01-01/2018-12-31/P6M
  cult_root_med:
    has_raw_value: xxx
  cur_land_use: farmstead
  cur_vegetation:
    has_raw_value: MIxS doesn't provide any guidance more specific than "text"
  cur_vegetation_meth:
    has_raw_value: https://link.springer.com/article/10.1023/A:1011975321668
  date_last_rain:
    has_raw_value: xxx
  density:
    has_raw_value: 1000 kilogram per cubic meter
  depos_env: other
  depth:
    has_maximum_numeric_value: 2.5
    has_minimum_numeric_value: 1.5
    has_numeric_value: 2.0
    has_raw_value: 1.5 to 2.5 meters (that may not be the pattern the submission schema
      expects). Extractions below require external migration logic.
    has_unit: meter
  description: unconstrained text
  dew_point:
    has_raw_value: xxx
  diether_lipids:
  - has_raw_value: xxx
  diss_carb_dioxide:
    has_raw_value: 5 milligram per liter
  diss_hydrogen:
    has_raw_value: 0.3 micromole per liter
  diss_inorg_carb:
    has_raw_value: 2059 micromole per kilogram
  diss_inorg_nitro:
    has_raw_value: xxx
  diss_inorg_phosp:
    has_raw_value: 56.5 micromole per liter
  diss_iron:
    has_raw_value: xxx
  diss_org_carb:
    has_raw_value: 197 micromole per liter
  diss_org_nitro:
    has_raw_value: 0.05 micromole per liter
  diss_oxygen:
    has_raw_value: 175 micromole per kilogram
  diss_oxygen_fluid:
    has_raw_value: xxx
  dna_absorb1: 2.02
  dna_absorb2: 2.02
  dna_collect_site: untreated pond water
  dna_concentration: 100
  dna_container_id: Pond_MT_041618
  dna_dnase: 'yes'
  dna_isolate_meth: phenol/chloroform extraction
  dna_organisms: expected to contain microbes (59%) fungi (30%), viruses (10%), tadpoles
    (1%)
  dna_project_contact: John Jones
  dna_samp_id: '187654'
  dna_sample_format: 10 mM Tris-HCl
  dna_sample_name: JGI_pond_041618
  dna_seq_project: '1191234'
  dna_seq_project_name: JGI Pond metagenomics
  dna_seq_project_pi: Jane Johnson
  dna_volume: 25
  dnase_rna: 'yes'
  door_comp_type: revolving
  door_cond: damaged
  door_direct: inward
  door_loc: north
  door_mat: aluminum
  door_move: collapsible
  door_size:
    has_raw_value: xxx
  door_type: composite
  door_type_metal: collapsible
  door_type_wood: battened
  door_water_mold:
    has_raw_value: xxx
  down_par:
    has_raw_value: xxx
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
  elev: 100
  elevator:
    has_raw_value: xxx
  embargoed: true
  emsl_biosample_identifiers:
  - generic:abc123
  emulsions:
  - has_raw_value: xxx
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
  env_package:
    has_raw_value: unconstrained text. should require the name of a MIxS EnvironmentalPackage
      class. have asked MIxS to return this term to their model. UPDATE VALIDATION
      RULES/PATTERN/ENUM!
  escalator:
    has_raw_value: xxx
  ethylbenzene:
    has_raw_value: xxx
  exp_duct:
    has_raw_value: xxx
  exp_pipe:
    has_raw_value: xxx
  experimental_factor:
    has_raw_value: unconstrained text, unlike the MIxS environmental triad
  experimental_factor_other: unconstrained text, but presumably expects 'term label
    [term id]'
  ext_door:
    has_raw_value: xxx
  ext_wall_orient: north
  ext_window_orient: north
  extreme_event: '2023-01-15'
  fao_class: Fluvisols
  fertilizer_regm:
  - has_raw_value: xxx
  field:
    has_raw_value: xxx
  filter_method: Basix PES, 13-100-106 FisherSci is an example value, but unconstrained
    text is accepted at this point
  filter_type:
  - HEPA
  fire: 2000-11 to 2000-12
  fireplace_type:
    has_raw_value: xxx
  flooding: '2000-01-15'
  floor_age:
    has_raw_value: xxx
  floor_area:
    has_raw_value: xxx
  floor_cond: new
  floor_count:
    has_raw_value: xxx
  floor_finish_mat: tile
  floor_struc: balcony
  floor_thermal_mass:
    has_raw_value: xxx
  floor_water_mold: condensation
  fluor:
    has_raw_value: xxx
  freq_clean:
    has_raw_value: xxx
  freq_cook:
    has_raw_value: xxx
  fungicide_regm:
  - has_raw_value: xxx
  furniture: cabinet
  gaseous_environment:
  - has_raw_value: nitric oxide;0.5 micromole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
  gaseous_substances:
  - has_raw_value: xxx
  gender_restroom: female
  genetic_mod:
    has_raw_value: xxx
  geo_loc_name:
    has_raw_value: 'USA: Maryland, Bethesda'
  glucosidase_act:
    has_raw_value: 5 mol per liter per hour
  gold_biosample_identifiers:
  - gold:Gb123456789
  - gold:Gb90909090
  gravidity:
    has_raw_value: xxx
  gravity:
  - has_raw_value: xxx
  growth_facil:
    has_raw_value: Growth chamber [CO_715:0000189]
  growth_habit: erect
  growth_hormone_regm:
  - has_raw_value: xxx
  habitat: unconstrained text
  hall_count:
    has_raw_value: xxx
  handidness: ambidexterity
  hc_produced: Oil
  hcr: Shale
  hcr_fw_salinity:
    has_raw_value: xxx
  hcr_geol_age: Archean
  hcr_pressure:
    has_raw_value: xxx
  hcr_temp:
    has_raw_value: xxx
  heat_cool_type:
  - radiant system
  heat_deliv_loc: north
  heat_sys_deliv_meth: xxx
  heat_system_id:
    has_raw_value: xxx
  heavy_metals:
  - has_raw_value: mercury;0.09 micrograms per gram
  - has_raw_value: arsenic;0.09 micrograms per gram
  heavy_metals_meth:
  - has_raw_value: https://link.springer.com/article/10.1007/s42452-019-1578-x
  height_carper_fiber:
    has_raw_value: xxx
  herbicide_regm:
  - has_raw_value: xxx
  horizon_meth:
    has_raw_value: xxx
  host_age:
    has_raw_value: xxx
  host_body_habitat:
    has_raw_value: xxx
  host_body_product:
    has_raw_value: xxx
  host_body_site:
    has_raw_value: xxx
  host_body_temp:
    has_raw_value: xxx
  host_color:
    has_raw_value: xxx
  host_common_name:
    has_raw_value: xxx
  host_diet:
  - has_raw_value: xxx
  host_dry_mass:
    has_raw_value: xxx
  host_family_relation:
  - xxx
  host_genotype:
    has_raw_value: xxx
  host_growth_cond:
    has_raw_value: xxx
  host_height:
    has_raw_value: xxx
  host_last_meal:
  - has_raw_value: xxx
  host_length:
    has_raw_value: xxx
  host_life_stage:
    has_raw_value: xxx
  host_name: snail is an example value, but unconstrained text is accepted at this
    point
  host_phenotype:
    has_raw_value: xxx
  host_sex: female
  host_shape:
    has_raw_value: xxx
  host_subject_id:
    has_raw_value: xxx
  host_subspecf_genlin:
  - xxx
  host_substrate:
    has_raw_value: xxx
  host_symbiont:
  - xxx
  host_taxid:
    has_raw_value: NCBITaxon:9606
    term:
      id: NCBITaxon:9606
  host_tot_mass:
    has_raw_value: xxx
  host_wet_mass:
    has_raw_value: xxx
  humidity:
    has_raw_value: xxx
  humidity_regm:
  - has_raw_value: 25 gram per cubic meter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
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
  inorg_particles:
  - has_raw_value: xxx
  insdc_biosample_identifiers:
  - biosample:SAMN123456789
  - biosample:SAMN000
  inside_lux:
    has_raw_value: xxx
  int_wall_cond: new
  isotope_exposure: 13C glucose
  iw_bt_date_well:
    has_raw_value: xxx
  iwf:
    has_raw_value: xxx
  last_clean:
    has_raw_value: xxx
  lat_lon:
    has_raw_value: 50.586825 6.408977
    latitude: 50.586825
    longitude: 6.408977
  lbc_thirty:
    has_raw_value: 543 mg/kg
  lbceq:
    has_raw_value: 1575 mg/kg
  light_intensity:
    has_raw_value: xxx
  light_regm:
    has_raw_value: incandescent light;10 lux;450 nanometer
  light_type:
  - none
  link_addit_analys:
    has_raw_value: https://pubmed.ncbi.nlm.nih.gov/2315679/
  link_class_info:
    has_raw_value: https://wisconsindot.gov/Documents/doing-bus/eng-consultants/cnslt-rsrces/geotechmanual/gt-03-03.pdf
  link_climate_info:
    has_raw_value: https://www.int-res.com/abstracts/cr/v14/n3/p161-173/
  lithology: Basement
  local_class:
    has_raw_value: jicama soil
  local_class_meth:
    has_raw_value: https://www.sciencedirect.com/science/article/abs/pii/S0016706105003083
  location: unconstrained text. should we even keep this slot? check if it has been
    used in MongoDB.
  magnesium:
    has_raw_value: 52.8 micromole per kilogram
  manganese:
    has_raw_value: 24.7 mg/kg
  max_occup:
    has_raw_value: xxx
  mean_frict_vel:
    has_raw_value: 0.5 meter per second
  mean_peak_frict_vel:
    has_raw_value: 1 meter per second
  mech_struc: subway
  mechanical_damage:
  - has_raw_value: xxx
  methane:
    has_raw_value: xxx
  micro_biomass_c_meth: https://acsess.onlinelibrary.wiley.com/doi/abs/10.2136/sssaspecpub49.c12
  micro_biomass_meth: xxx
  micro_biomass_n_meth: https://acsess.onlinelibrary.wiley.com/doi/abs/10.2136/sssaspecpub49.c12
  microbial_biomass:
    has_raw_value: xxx
  microbial_biomass_c: 0.05 ug C/g dry soil
  microbial_biomass_n: 0.05 ug N/g dry soil
  mineral_nutr_regm:
  - has_raw_value: xxx
  misc_param:
  - has_raw_value: Bicarbonate ion concentration;2075 micromole per kilogram
  mod_date: '2023-01-25'
  n_alkanes:
  - has_raw_value: n-hexadecane;100 milligram per liter
  name: Sample Exhaustive Biosample instance. Although all of these values should
    pass validation, that does not mean that any Biosample of any type would necessarily
    have this particular combination of values.
  ncbi_taxonomy_name: soil metagenome
  nitrate:
    has_raw_value: 65 micromole per liter
  nitrite:
    has_raw_value: 0.5 micromole per liter
  nitrite_nitrogen:
    has_raw_value: 1.2 mg/kg
  nitro:
    has_raw_value: xxx
  non_microb_biomass: insect 0.23 ug; plant 1g
  non_microb_biomass_method: https://doi.org/10.1038/s41467-021-26181-3
  non_min_nutr_regm:
  - xxx
  nucl_acid_amp:
    has_raw_value: xxx
  nucl_acid_ext:
    has_raw_value: xxx
  number_pets:
    has_raw_value: xxx
  number_plants:
    has_raw_value: xxx
  number_resident:
    has_raw_value: xxx
  occup_density_samp:
    has_raw_value: xxx
  occup_document: estimate
  occup_samp:
    has_raw_value: xxx
  org_carb:
    has_raw_value: xxx
  org_count_qpcr_info: xxx
  org_matter:
    has_raw_value: 1.75 milligram per cubic meter
  org_nitro:
    has_raw_value: 4 micromole per liter
  org_nitro_method: https://doi.org/10.1016/0038-0717(85)90144-0
  org_particles:
  - has_raw_value: xxx
  organism_count:
  - has_raw_value: ATP
  other_treatment: unconstrained text
  owc_tvdss:
    has_raw_value: xxx
  oxy_stat_samp: aerobic
  oxygen:
    has_raw_value: xxx
  part_of:
  - nmdc:sty-00-987654
  - nmdc:sty-00-qwerty
  part_org_carb:
    has_raw_value: 1.92 micromole per liter
  part_org_nitro:
    has_raw_value: xxx
  particle_class:
  - has_raw_value: xxx
  pcr_cond:
    has_raw_value: xxx
  pcr_primers:
    has_raw_value: xxx
  permeability:
    has_raw_value: xxx
  perturbation:
  - has_raw_value: antibiotic addition;R2/2018-05-11T14:30Z/2018-05-11T19:30Z/P1H30M
  pesticide_regm:
  - has_raw_value: xxx
  petroleum_hydrocarb:
    has_raw_value: 0.05 micromole per liter
  ph: 99.99
  ph_meth:
    has_raw_value: https://www.epa.gov/sites/production/files/2015-12/documents/9040c.pdf
  ph_regm:
  - has_raw_value: xxx
  phaeopigments:
  - has_raw_value: 2.5 milligram per cubic meter
  phosphate:
    has_raw_value: 0.7 micromole per liter
  phosplipid_fatt_acid:
  - has_raw_value: 2.98 milligram per liter
  photon_flux:
    has_raw_value: xxx
  plant_growth_med:
    has_raw_value: xxx
  plant_product:
    has_raw_value: xxx
  plant_sex: Androdioecious
  plant_struc:
    has_raw_value: xxx
  pollutants:
  - has_raw_value: xxx
  pool_dna_extracts:
    has_raw_value: yes, 5
  porosity:
    has_raw_value: xxx
  potassium:
    has_raw_value: 463 milligram per liter
  pour_point:
    has_raw_value: xxx
  pre_treatment:
    has_raw_value: xxx
  pres_animal_insect: cat;3
  pressure:
    has_raw_value: 50 atmosphere
  prev_land_use_meth: xxx
  previous_land_use:
    has_raw_value: xxx
  primary_prod:
    has_raw_value: xxx
  primary_treatment:
    has_raw_value: xxx
  prod_rate:
    has_raw_value: xxx
  prod_start_date:
    has_raw_value: xxx
  profile_position: summit
  project_id: no example from MIxS
  proport_woa_temperature: no example from MIxS
  proposal_dna: '504000'
  proposal_rna: '504000'
  quad_pos: North side
  radiation_regm:
  - has_raw_value: xxx
  rainfall_regm:
  - has_raw_value: xxx
  reactor_type:
    has_raw_value: xxx
  redox_potential:
    has_raw_value: 300 millivolt
  rel_air_humidity:
    has_raw_value: xxx
  rel_humidity_out:
    has_raw_value: xxx
  rel_samp_loc: edge of car
  replicate_number: '1'
  reservoir:
    has_raw_value: xxx
  resins_pc:
    has_raw_value: xxx
  rna_absorb1: 2.02
  rna_absorb2: 2.02
  rna_collect_site: untreated pond water
  rna_concentration: 100
  rna_container_id: Pond_MT_041618
  rna_isolate_meth: phenol/chloroform extraction
  rna_organisms: expected to contain microbes (59%) fungi (30%), viruses (10%), tadpoles
    (1%)
  rna_project_contact: John Jones
  rna_samp_id: '187654'
  rna_sample_format: 10 mM Tris-HCl
  rna_sample_name: JGI_pond_041618
  rna_seq_project: '1191234'
  rna_seq_project_name: JGI Pond metagenomics
  rna_seq_project_pi: Jane Johnson
  rna_volume: 25
  room_air_exch_rate:
    has_raw_value: xxx
  room_architec_elem: xxx
  room_condt: new
  room_connected: attic
  room_count:
    has_raw_value: xxx
  room_dim:
    has_raw_value: xxx
  room_door_dist:
    has_raw_value: xxx
  room_door_share:
    has_raw_value: xxx
  room_hallway:
    has_raw_value: xxx
  room_loc: corner room
  room_moist_dam_hist: 123
  room_net_area:
    has_raw_value: xxx
  room_occup:
    has_raw_value: xxx
  room_samp_pos: north corner
  room_type: attic
  room_vol:
    has_raw_value: xxx
  room_wall_share:
    has_raw_value: xxx
  room_window_count: 123
  root_cond:
    has_raw_value: xxx
  root_med_carbon:
    has_raw_value: xxx
  root_med_macronutr:
    has_raw_value: xxx
  root_med_micronutr:
    has_raw_value: xxx
  root_med_ph:
    has_raw_value: xxx
  root_med_regl:
    has_raw_value: xxx
  root_med_solid:
    has_raw_value: xxx
  root_med_suppl:
    has_raw_value: xxx
  salinity:
    has_raw_value: 25 practical salinity unit
  salinity_category: halotolerant is an example from the schema, but MIxS doesn't
    provide this slot any more
  salinity_meth:
    has_raw_value: PMID:22895776
  salt_regm:
  - has_raw_value: xxx
  samp_capt_status: other
  samp_collec_device: xxx
  samp_collec_method: swabbing
  samp_collect_point: well
  samp_dis_stage: dissemination
  samp_floor: basement
  samp_loc_corr_rate:
    has_raw_value: xxx
  samp_mat_process:
    has_raw_value: filtering of seawater
  samp_md:
    has_raw_value: xxx
  samp_name: see also name
  samp_preserv:
    has_raw_value: xxx
  samp_room_id:
    has_raw_value: xxx
  samp_size:
    has_raw_value: 5 liters
  samp_sort_meth:
  - has_raw_value: xxx
  samp_store_dur:
    has_raw_value: P1Y6M
  samp_store_loc:
    has_raw_value: Freezer no:5
  samp_store_temp:
    has_raw_value: -80 degree Celsius
  samp_subtype: biofilm
  samp_taxon_id:
    has_raw_value: soil metagenome [NCBItaxon:410658]
    term:
      id: NCBItaxon:410658
      name: soil metagenome
  samp_time_out:
    has_raw_value: xxx
  samp_transport_cond:
    has_raw_value: xxx
  samp_tvdss:
    has_raw_value: xxx
  samp_type:
    has_raw_value: xxx
  samp_vol_we_dna_ext:
    has_raw_value: 1500 milliliter
  samp_weather: cloudy
  samp_well_name:
    has_raw_value: xxx
  sample_collection_site: unconstrained text
  sample_link:
  - IGSN:DSJ0284
  - any:curie
  sample_shipped: 15 g
  sample_type: soil - water extract
  saturates_pc:
    has_raw_value: xxx
  season:
    has_raw_value: xxx
  season_environment:
  - has_raw_value: xxx
  season_precpt:
    has_raw_value: 75 millimeters
  season_temp:
    has_raw_value: 18 degree Celsius
  season_use: Spring
  secondary_treatment:
    has_raw_value: xxx
  sediment_type: biogenous
  seq_meth:
    has_raw_value: xxx
  seq_quality_check:
    has_raw_value: xxx
  sewage_type:
    has_raw_value: xxx
  shad_dev_water_mold: xxx
  shading_device_cond: damaged
  shading_device_loc:
    has_raw_value: xxx
  shading_device_mat:
    has_raw_value: xxx
  shading_device_type: tree
  sieving:
    has_raw_value: MIxS does not provide an example
  silicate:
    has_raw_value: xxx
  size_frac:
    has_raw_value: xxx
  size_frac_low:
    has_raw_value: 0.2 micrometer
  size_frac_up:
    has_raw_value: 20 micrometer
  slope_aspect:
    has_raw_value: MIxS does not provide an example
  slope_gradient:
    has_raw_value: MIxS does not provide an example
  sludge_retent_time:
    has_raw_value: xxx
  sodium:
    has_raw_value: 10.5 milligram per liter
  soil_horizon: O horizon
  soil_text_measure:
    has_raw_value: xxx
  soil_texture_meth: xxx
  soil_type:
    has_raw_value: plinthosol [ENVO:00002250]
  soil_type_meth:
    has_raw_value: Frederick series
  solar_irradiance:
    has_raw_value: xxx
  soluble_inorg_mat:
  - has_raw_value: xxx
  soluble_iron_micromol: MIxS doesn't provide an example
  soluble_org_mat:
  - has_raw_value: xxx
  soluble_react_phosp:
    has_raw_value: xxx
  source_mat_id:
    has_raw_value: MPI012345
  space_typ_state:
    has_raw_value: xxx
  specific: operation
  specific_ecosystem: unconstrained text
  specific_humidity:
    has_raw_value: xxx
  sr_dep_env: Lacustine
  sr_geol_age: Archean
  sr_kerog_type: other
  sr_lithology: Clastic
  standing_water_regm:
  - has_raw_value: xxx
  start_date_inc: '2023-01-27'
  start_time_inc: 13:42+0000
  store_cond:
    has_raw_value: -20 degree Celsius freezer;P2Y10D
  substructure_type:
  - basement
  subsurface_depth:
    has_raw_value: MIxS does not provide an example
  sulfate:
    has_raw_value: 5 micromole per liter
  sulfate_fw:
    has_raw_value: xxx
  sulfide:
    has_raw_value: 2 micromole per liter
  surf_air_cont:
  - dust
  surf_humidity:
    has_raw_value: xxx
  surf_material: adobe
  surf_moisture:
    has_raw_value: xxx
  surf_moisture_ph: 123
  surf_temp:
    has_raw_value: xxx
  suspend_part_matter:
    has_raw_value: xxx
  suspend_solids:
  - has_raw_value: xxx
  tan:
    has_raw_value: xxx
  target_gene:
    has_raw_value: xxx
  target_subfragment:
    has_raw_value: xxx
  technical_reps: '2'
  temp:
    has_raw_value: 25 degree Celsius
  temp_out:
    has_raw_value: xxx
  tertiary_treatment:
    has_raw_value: xxx
  tidal_stage: high tide
  tillage:
  - chisel
  tiss_cult_growth_med:
    has_raw_value: xxx
  toluene:
    has_raw_value: xxx
  tot_carb:
    has_raw_value: MIxS does not provide an example
  tot_depth_water_col:
    has_raw_value: 500 meter
  tot_diss_nitro:
    has_raw_value: 40 microgram per liter
  tot_inorg_nitro:
    has_raw_value: xxx
  tot_iron:
    has_raw_value: xxx
  tot_nitro:
    has_raw_value: xxx
  tot_nitro_cont_meth: https://currentprotocols.onlinelibrary.wiley.com/doi/abs/10.1002/0471142913.fab0102s00
  tot_nitro_content:
    has_raw_value: 35 milligrams Nitrogen per kilogram of soil
  tot_org_c_meth:
    has_raw_value: https://www.epa.gov/sites/production/files/2015-12/documents/9060a.pdf
  tot_org_carb:
    has_raw_value: 2%
  tot_part_carb:
    has_raw_value: xxx
  tot_phosp:
    has_raw_value: 0.03 milligram per liter
  tot_phosphate:
    has_raw_value: xxx
  tot_sulfur:
    has_raw_value: xxx
  train_line: red
  train_stat_loc: south station above ground
  train_stop_loc: end
  turbidity:
    has_raw_value: xxx
  tvdss_of_hcr_press:
    has_raw_value: xxx
  tvdss_of_hcr_temp:
    has_raw_value: xxx
  typ_occup_density: 123
  type: nmdc:Biosample. change this to require a class name or an enumeration
  ventilation_rate:
    has_raw_value: xxx
  ventilation_type:
    has_raw_value: xxx
  vfa:
    has_raw_value: xxx
  vfa_fw:
    has_raw_value: xxx
  vis_media: photos
  viscosity:
    has_raw_value: xxx
  volatile_org_comp:
  - has_raw_value: xxx
  wall_area:
    has_raw_value: xxx
  wall_const_type: frame construction
  wall_finish_mat: plaster
  wall_height:
    has_raw_value: xxx
  wall_loc: north
  wall_surf_treatment: painted
  wall_texture: knockdown
  wall_thermal_mass:
    has_raw_value: xxx
  wall_water_mold:
    has_raw_value: xxx
  wastewater_type:
    has_raw_value: xxx
  water_cont_soil_meth: MIxS doesn't provide an example
  water_content:
  - MIxS doesn't provide an example 1
  - MIxS doesn't provide an example 2
  water_current:
    has_raw_value: xxx
  water_cut:
    has_raw_value: xxx
  water_feat_size:
    has_raw_value: xxx
  water_feat_type: fountain
  water_prod_rate:
    has_raw_value: xxx
  water_temp_regm:
  - has_raw_value: xxx
  watering_regm:
  - has_raw_value: 1 liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
  weekday: Monday
  win:
    has_raw_value: xxx
  wind_direction:
    has_raw_value: xxx
  wind_speed:
    has_raw_value: xxx
  window_cond: damaged
  window_cover: blinds
  window_horiz_pos: left
  window_loc: north
  window_mat: fiberglass
  window_open_freq:
    has_raw_value: xxx
  window_size:
    has_raw_value: xxx
  window_status:
    has_raw_value: xxx
  window_type: single-hung sash window
  window_vert_pos: bottom
  window_water_mold:
    has_raw_value: xxx
  xylene:
    has_raw_value: xxx
  zinc:
    has_raw_value: 2.5 mg/kg

```
## Database-biosamples-rna-in-tube
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  part_of:
  - nmdc:sty-00-abc123
  rna_cont_type: tube

```
## MetabolomicsAnalysisActivity-1
### Input
```yaml
ended_at_time: '2021-09-15T10:13:20+00:00'
execution_resource: NERSC cori
git_url: https://example.org/WorkflowExecutionActivity
has_calibration: calibration with 0.01% phosphoric acid
has_input:
- nmdc:i1
- nmdc:i2
has_output:
- nmdc:o1
- nmdc:o2
id: nmdc:wfmb-99-ABCDEF
started_at_time: '2021-08-05T14:48:51+00:00'
type: WorkflowExecutionActivity
was_informed_by: nmdc:a1

```
## Database-pooling_set-minimal
### Input
```yaml
pooling_set:
- id: nmdc:poolp-9x9-1x
  name: first pooling process

```
## Database-biosamples-1
### Input
```yaml
biosample_set:
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - gold:Gb0101224
  habitat: Coalbed water
  id: nmdc:bsm-99-dtTMNb
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients (early)
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-abc123
  samp_taxon_id:
    has_raw_value: coal metagenome [NCBITaxon:1260732]
    term:
      id: NCBITaxon:1260732
      name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - gold:Gb0101224
  habitat: Coalbed water
  id: nmdc:bsm-99-AtTUOs
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients (early)
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-abc123
  samp_taxon_id:
    has_raw_value: coal metagenome [NCBITaxon:1260732]
    term:
      id: NCBITaxon:1260732
      name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - gold:Gb0101225
  habitat: Coalbed water
  id: nmdc:bsm-99-eBVHjN
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients Extra
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-abc123
  samp_taxon_id:
    has_raw_value: coal metagenome [NCBITaxon:1260732]
    term:
      id: NCBITaxon:1260732
      name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - gold:Gb0101226
  habitat: Coalbed water
  id: nmdc:bsm-99-TDPHTh
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-abc123
  samp_taxon_id:
    has_raw_value: coal metagenome [NCBITaxon:1260732]
    term:
      id: NCBITaxon:1260732
      name: coal metagenome
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
  specific_ecosystem: Unclassified
  study_category: research_study
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
  specific_ecosystem: Unclassified
  study_category: research_study
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
  specific_ecosystem: Permafrost
  study_category: research_study

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

```
## SolutionComponent-minimal
### Input
```yaml
compound: methanol
concentration:
  has_numeric_value: 10
  has_unit: mM

```
## DataObject-my_emsl_prefix
### Input
```yaml
alternative_identifiers:
- my_emsl:1016236
data_object_type: LC-DDA-MS/MS Raw Data
description: raw instrument file for nmdc:omprc-11-7nfk8n58
file_size_bytes: 448727423
id: nmdc:dobj-11-mzxj8743
md5_checksum: ED2BA6CD95CE5D86D8D29A8DD548F48F
name: Froze_Core_2015_S1_30_40_3_QE_26May16_Pippin_16-03-39.raw
url: https://nmdcdemo.emsl.pnnl.gov/proteomics/raw/Froze_Core_2015_S1_30_40_3_QE_26May16_Pippin_16-03-39.raw

```
## Solution-minimal
### Input
```yaml
has_solution_components:
- compound: methanol
  concentration:
    has_numeric_value: 10
    has_unit: mM
volume:
  has_numeric_value: 120
  has_unit: mL

```
## Database-multiple-paths
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  name: real biosample from the field
  part_of:
  - nmdc:sty-00-abc123
- env_broad_scale:
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
  id: nmdc:bsm-99-XYZ
  name: one DNA library, like an analytical sample
  part_of:
  - nmdc:sty-00-abc123
omics_processing_set:
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108335
  has_input:
  - nmdc:bsm-00-red
  has_output:
  - nmdc:dobj-00-9n9n9n
  id: nmdc:omprc-99-zUCd5N
  mod_date: 22-MAY-20 06.13.12.927000000 PM
  name: a process in which a biosample was sequenced?
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712P3D
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - nmdc:sty-00-555xxx
  processing_institution: JGI
  type: nmdc:OmicsProcessing

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
## Biosample-minimal-2
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
part_of:
- nmdc:sty-00-abc123

```
## Database-img_mg_annotation_objects
### Input
```yaml
activity_set:
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:b4b798cc9e7e9253ae8256a8237fd371
  has_output:
  - nmdc:a1f2c190aa6d470f2eea681126e0470e
  - nmdc:7d69d28f4abec72a7ad66411312c37fb
  - nmdc:c3ea4b3caf0c86e27118b3ffd51014b8
  - nmdc:a79973ef9a0c96d13fa19b2725b21d17
  - nmdc:1055b8fab0f63a1e56312813f47897ec
  id: nmdc:wf-99-v7tNhU
  name: MetagenomeAnnotation activity for gold:Gp0153825
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0153825
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:70fba0e579271c70e65c7ef5909958ed
  has_output:
  - nmdc:b7abebe872fb705d2cdd5fcd36becf0e
  - nmdc:5b2e3bf2abc084710300eb4668638ed3
  - nmdc:f574e3392aa40d786a566ae4bc0a5932
  - nmdc:c09c5f5c4f776e6250cf35003e939729
  - nmdc:fd3023efdffe55105bc192f5b6cb4675
  id: nmdc:wf-99-bzS2v1
  name: MetagenomeAnnotation activity for gold:Gp0119849
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119849
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:04b7e946dd85306cc75eb3c59f26bf1d
  has_output:
  - nmdc:dd84dbd2e1b611a1cb6f855f578538d3
  - nmdc:72bc285bcb9a4e0bff1b99719cf8346b
  - nmdc:e18017e4d7721b9aa8f6fe0604d61d28
  - nmdc:c93e3ebaf3c21c50bb1071d0e07daa48
  - nmdc:6e16b6f3d73dc771eba4c729600c9551
  id: nmdc:wf-99-sXZVjh
  name: MetagenomeAnnotation activity for gold:Gp0119850
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119850
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:76a9fb6a1d29da495d246728ab7ace33
  has_output:
  - nmdc:bdfa927dbe2d5bbf27f1a1cf0265a27f
  - nmdc:0ab4c3c5fb624a9931ac977df5a4aa4f
  - nmdc:4b6e2700378acc2a9ac22195a9b4cbfb
  - nmdc:f8219a779a150e71c672dd2bfd695365
  - nmdc:adfd5d1e9ec99ea5917d8b9efdbd9130
  id: nmdc:wf-99-3fBeJp
  name: MetagenomeAnnotation activity for gold:Gp0119851
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119851
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:9f3d6c465517c7bca53391ab998dad82
  has_output:
  - nmdc:de071cd0e3010778b9f491e846b95179
  - nmdc:793aa923c27dd8cc762625f96ff52f80
  - nmdc:678d467ad6c4ad6d7ba2f259585c4acd
  - nmdc:18c7f9fe5340509f00326c70c1815e88
  - nmdc:4b43a24ab20530a72e06a8721b2c09db
  id: nmdc:wf-99-F6E55A
  name: MetagenomeAnnotation activity for gold:Gp0119852
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119852
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:50175f6f32192a797c58d2ef636efa37
  has_output:
  - nmdc:2bd72614bf1a394de064eb6148074d22
  - nmdc:af374a8de732aa3c85eba74b5d29fb66
  - nmdc:db7baf32a8a49b586b8ff70b67487863
  - nmdc:c0c580b59189351b4f4919701e4db0f2
  - nmdc:14e390786d1f1eb60835aca96081ab23
  id: nmdc:wf-99-Zrij2v
  name: MetagenomeAnnotation activity for gold:Gp0119853
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119853
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:772095f1e8e7033ff8f5e5a42308347c
  has_output:
  - nmdc:93e586051957e0f4a451b70ceeac04ab
  - nmdc:6b974729dc47b7795b17fac36d496cfa
  - nmdc:3361194f90da2d18830213cd4587aa71
  - nmdc:dba970c890226f16b008f8043ca38d9b
  - nmdc:b476e6c11fed4a3254eda4d15a4183c7
  id: nmdc:wf-99-swlzri
  name: MetagenomeAnnotation activity for gold:Gp0119854
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119854
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:fb5ab52924b554184ac31308e4126b44
  has_output:
  - nmdc:465d9547f4c5d5aa4d341555f5769d9a
  - nmdc:34a4bbe14e8867d45e95e205738b6d3f
  - nmdc:7a953d15a0f368c71cb365c2dd888a83
  - nmdc:bb8a58ce8c8850f95dc84aa49a7a96f7
  - nmdc:3a05f63e1899f82d11d931adfe69d86a
  id: nmdc:wf-99-k15Id6
  name: MetagenomeAnnotation activity for gold:Gp0119855
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119855
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:9d774aebab719174e5b3113c65fe5860
  has_output:
  - nmdc:e1c28a3028e3fb994d48c67c3cad4ab4
  - nmdc:41b3a8590d7ad384f5a92bfd74267f5f
  - nmdc:5726d2d4081cd3a257e15e98f5a45f8c
  - nmdc:42164be43a9ab6da393c7d48825e289e
  - nmdc:72aaf6784de9aa35be58e12898bff353
  id: nmdc:wf-99-phL8rY
  name: MetagenomeAnnotation activity for gold:Gp0119856
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119856
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:33fa88501b23f0498c6af05c5924704e
  has_output:
  - nmdc:ecbfb703f2b4204f9f67de20840bd355
  - nmdc:60524c5c69a1c8b4a2609f4a9cb3a490
  - nmdc:4a4032318b50bdc3bae5d290a7f0735e
  - nmdc:5a77bb24847fcbf1c3fec6c40aa2ac14
  - nmdc:89ef0619642dead830035ac9389ca802
  id: nmdc:wf-99-rIKnPj
  name: MetagenomeAnnotation activity for gold:Gp0119857
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119857
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:f5e854c22a065f2895f99a0119b1b41a
  has_output:
  - nmdc:db4fc71545bef12273f70878ad83a7fe
  - nmdc:503667333d0a31fa41da4885bea45c8c
  - nmdc:8e0746f6759e85ee867f85191d83a1e9
  - nmdc:0b7a5694aefdea2070dd1b21a21a9abb
  - nmdc:43157d8de38b673ce4a4d70ee3a1198c
  id: nmdc:wf-99-NHVre9
  name: MetagenomeAnnotation activity for gold:Gp0119858
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119858
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:b6adc0392be1b4d327e57c7630de47f5
  has_output:
  - nmdc:ed4bc44713888809173573d96114f11e
  - nmdc:18cdf12e824a7fb6255dbcac79a2a9a0
  - nmdc:1729d54d35a1445759d4a85cbd4e305c
  - nmdc:eb09f7f461ad13a47bf5609cdcfc853c
  - nmdc:10128acfa04b42839c133fe298eab941
  id: nmdc:wf-99-n84Tew
  name: MetagenomeAnnotation activity for gold:Gp0119859
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119859
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:fdc028609bab950eb4289953fbe03aa5
  has_output:
  - nmdc:cf2282967219cfc4462f91840aae4126
  - nmdc:7137d225d4e84d63175b89e1f74b7728
  - nmdc:2fa5357b6e025470478224cc8c4d8443
  - nmdc:613152955d79f4344828738fb898d679
  - nmdc:959ef4ff2d105052b094138aa09b5c94
  id: nmdc:wf-99-6IBBqL
  name: MetagenomeAnnotation activity for gold:Gp0119860
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119860
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:0cb2e3b5ce7e14d6bb08eec2a31d247a
  has_output:
  - nmdc:066d13964ce47a41a1e2ef7a5b19cb59
  - nmdc:218b0daa573a8a7f5fc31d6cfe1edad5
  - nmdc:4f13ca8028e6581e0510d8667456bf28
  - nmdc:1712f2bb1fa749515ce0bf2b34f8b559
  - nmdc:0f06cb228b08e2aee24c65444d0bfc21
  id: nmdc:wf-99-sCL9p6
  name: MetagenomeAnnotation activity for gold:Gp0119861
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119861
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:1b4116c5fa8023a05811814bde3d66f0
  has_output:
  - nmdc:ceb802e43562a90b5dc028d818a8f56d
  - nmdc:9ebfce5805ecaeb07521c28690fa810c
  - nmdc:895b148dc332f979f35fae25156762d8
  - nmdc:19e4e0238ac9c1d07646431ee62fa2d9
  - nmdc:d8e967e38a491678164ab203551aad61
  id: nmdc:wf-99-xtaqhx
  name: MetagenomeAnnotation activity for gold:Gp0119862
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119862
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:8565741217a0632488535b5b20afa036
  has_output:
  - nmdc:091275dd5ad1358b576671f22c2f8157
  - nmdc:2318ee29172751d9f66edc54c7a456fa
  - nmdc:f5a9c910bcb6cbec92291db526caa1db
  - nmdc:8be139ccce758a8845092122546ff2b3
  - nmdc:46cf62901adcbcb2ca2c890b6dc8e6bd
  id: nmdc:wf-99-cnpEPb
  name: MetagenomeAnnotation activity for gold:Gp0119863
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119863
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:279ac03ea9aa6cce7c1e23119643b70e
  has_output:
  - nmdc:cc49ea1669ce6a40e73b17880ebdf36e
  - nmdc:30dc605e7458353cd12e0700042f8b23
  - nmdc:7ae6e443b360f01d0655aa6066e06c87
  - nmdc:b803f40f00f0c9988dd5968acd4821cb
  - nmdc:3695d84852c6345c02f5f1c3e3f3a423
  id: nmdc:wf-99-bFWXyt
  name: MetagenomeAnnotation activity for gold:Gp0119864
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119864
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:cbb78531961f6eab3b0f8ef2fa488801
  has_output:
  - nmdc:e34ef5954fd12e5fdab0bae08414b001
  - nmdc:a58d0ad82bcd82747443a05133e86d4a
  - nmdc:1f5ea69be09b6f086c09af241d6b9df5
  - nmdc:73e37fa7c4626d47580d5705cb656383
  - nmdc:9f23cbec97a89ce503564d05b061f37f
  id: nmdc:wf-99-H9y4oj
  name: MetagenomeAnnotation activity for gold:Gp0119865
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119865
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:3d0615c9034cfba43866390d717f8de8
  has_output:
  - nmdc:9101306c31f4b8c544f1671e66607a87
  - nmdc:4ef712b7b38e384c25a31fc24c39aab9
  - nmdc:e4f33c52b87b07d9f50cda6bf067d710
  - nmdc:2de8312087081f9aeac56c56195a5fc2
  - nmdc:5d1bb402cf5170de632179f2515a224f
  id: nmdc:wf-99-exEkWs
  name: MetagenomeAnnotation activity for gold:Gp0119866
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119866
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:203d4e9e3d7999df5978a77217526d42
  has_output:
  - nmdc:e1b8a1bb51b7c8421ed748d3da31cab9
  - nmdc:e5a23d1c8e78d044bb907acb7490c223
  - nmdc:a4403a73bfd1f57ce219127cd1ebed51
  - nmdc:b20ef196169b86e1498e45194adeff8b
  - nmdc:fd11757a61a2400b5ed8077c62cc97b9
  id: nmdc:wf-99-GzdjHY
  name: MetagenomeAnnotation activity for gold:Gp0119867
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119867
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:e30d13f5b218da7692120ac3351f9569
  has_output:
  - nmdc:0289e4fda11b48fb48c641c8e309b3ed
  - nmdc:df46e32e073a15273bb1f709b15abcd3
  - nmdc:ff55ba482b074f7f3d56c64da1b3c9c8
  - nmdc:3c788da6e9004cd3ec276d5e44b19548
  - nmdc:804bc97cd8e16289290024ea3a7edbde
  id: nmdc:wf-99-4V6suA
  name: MetagenomeAnnotation activity for gold:Gp0119868
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119868
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:7ab8f7dcc03e512ef3ab2143b63cc8de
  has_output:
  - nmdc:aa524a698ead96378589ebfec51375f4
  - nmdc:475a785b8c7e1de1e88d36b2863ad1d8
  - nmdc:ec5a78019044659ab89e4703a2ab57ff
  - nmdc:c46f4c6ee971aff627dcbfc8f1e3a9e8
  - nmdc:431354e60f7a35b67c2f7ec52b955808
  id: nmdc:wf-99-JoTrst
  name: MetagenomeAnnotation activity for gold:Gp0119869
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119869
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:68fb8b64adf5c219f787dc8bb5d94480
  has_output:
  - nmdc:9b89126b81c06ae693353614f72344cb
  - nmdc:ba17d066f634e0bcc16fbcc7f1ff55f0
  - nmdc:56c01b4ba33b765ad4a478d662a11e75
  - nmdc:977d1fc2445d1aecd5f30e0197535af9
  - nmdc:4b204c8e49c59d862209579b79c44545
  id: nmdc:wf-99-WMxKQm
  name: MetagenomeAnnotation activity for gold:Gp0119870
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119870
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:b35b812f128516b0d12910c71df77b1c
  has_output:
  - nmdc:0c72d3d72c8f29761c48d2844cbbd858
  - nmdc:cf3c06ff9bb95e6e76b26bdd29add799
  - nmdc:c2b7fc5a3e992bb271559774a779c890
  - nmdc:8c6e1665a12e9478f7f13b9177b08083
  - nmdc:b2f6e385af8cbe49df3044d523da5c82
  id: nmdc:wf-99-KNca8B
  name: MetagenomeAnnotation activity for gold:Gp0119871
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0119871
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:9339ba4d7b731220024b995f87ddc5e1
  has_output:
  - nmdc:d6afa54f891852b3a5befc294ce84489
  - nmdc:e15c4db1e4e26208b302ecb9bc2c094c
  - nmdc:3acc269b9e2b5e97ffcc3c1a0d85381c
  - nmdc:be62e3b68916c8077955d0b3d3aaf5aa
  - nmdc:feb21db71dc44afceeb88bb725315b42
  id: nmdc:wf-99-dNish1
  name: MetagenomeAnnotation activity for gold:Gp0127623
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127623
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:70c6cfaac2821e95aad6732da590276e
  has_output:
  - nmdc:73ebb84a8744552c890ad2508e313972
  - nmdc:89a4bb36ef225146a2ba0daaaea512fd
  - nmdc:6bcdfc58ee6b4eb5ae022c71636a88b4
  - nmdc:075262a23b12fd4da073a973a5b6cf15
  - nmdc:3fb3966095303ea8aa7f27bff3e9db50
  id: nmdc:wf-99-U1umHi
  name: MetagenomeAnnotation activity for gold:Gp0127624
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127624
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:593237bf7f38f66d40eca1dbb23c7aef
  has_output:
  - nmdc:16eb9d7ffc8dbf8872cbdb9b7f0a1c82
  - nmdc:18dd16caf7af261c4d647da91a6f526a
  - nmdc:3b039b9d5a75b97a67edf5d50b34d9f0
  - nmdc:c6fb34fc2da63a5cc46522279e768db9
  - nmdc:bf23db2dda841d77cf51b7c9120ba503
  id: nmdc:wf-99-Teg8kK
  name: MetagenomeAnnotation activity for gold:Gp0127625
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127625
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:59e99f35194f3f98fa07d401dddd4959
  has_output:
  - nmdc:dde9a2b70a0552a8d6f7cda7f4862aa9
  - nmdc:1f45d481e2882a15e7d060e47cbbfda3
  - nmdc:8e19f17a8fd0747410b68d804b87139d
  - nmdc:11741b35b589852f2b652d1f73afb663
  - nmdc:f1b6a4b001b67ec72eb5b5411e1321c9
  id: nmdc:wf-99-qB4hXN
  name: MetagenomeAnnotation activity for gold:Gp0127626
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127626
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:245e4bf7ae2d630d26223054f851e31c
  has_output:
  - nmdc:4c97ec34649fc995f167408bd39c9998
  - nmdc:874ae45fc2a007a7d5f9ff964fa8117a
  - nmdc:6c96999ab72498624aae8bb9b0bfbc66
  - nmdc:fec0b3842897bbce9166a628c4c2d7a0
  - nmdc:48ab9737528d088ffde37b733e3f728f
  id: nmdc:wf-99-72JIpi
  name: MetagenomeAnnotation activity for gold:Gp0127627
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127627
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:e54d5475a6bf7148d2312d0fcc349cdb
  has_output:
  - nmdc:760a1e1bc5aac21dd0b96098c72133ff
  - nmdc:69da278e8966a688cafb7bb2c8f2e4d1
  - nmdc:b73bf45facd909d89bfab76dee85a2cc
  - nmdc:ec55b61e1204cde7fe61841179b88b53
  - nmdc:bd55dfd59ed0aa7ea685734c5b7ecbab
  id: nmdc:wf-99-mbF4y1
  name: MetagenomeAnnotation activity for gold:Gp0127628
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127628
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:9eed2da9f67c58f243329daf2289f40e
  has_output:
  - nmdc:f9211f36dc6992c2dfecd160987434c7
  - nmdc:37fb326b25c1ae3caebddf668feadd76
  - nmdc:75e43708767f06de878e1c2115714e0b
  - nmdc:9559ebd9a8921ff8ae9f89c2ffcef6f7
  - nmdc:9b3fb3e409e3d3128a8a43cc58d32a95
  id: nmdc:wf-99-ylyhlC
  name: MetagenomeAnnotation activity for gold:Gp0127629
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127629
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:c3958f0be344c850d06ee61865c95ff6
  has_output:
  - nmdc:81ab86211731bc0547d3e8f8786c3e8b
  - nmdc:c6b5f388349af0214d65d1357026c7ee
  - nmdc:070f0952308650d35ae05c4fed188677
  - nmdc:6bca5ad106b3519416205a82d3a14b16
  - nmdc:f921989651475b06052058126db54de9
  id: nmdc:wf-99-56GrFn
  name: MetagenomeAnnotation activity for gold:Gp0127630
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127630
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:ff68d07b09e5a9cdd866208394d66bd6
  has_output:
  - nmdc:ee276fe3eb490475ad3d7280a8c67464
  - nmdc:e2ef79ef2b6669d93af5e90ba2c58fcf
  - nmdc:5723e7023b0e3994e92c7c5e72aa34ec
  - nmdc:04c97ac7af06bf37da8f1ffe827e454d
  - nmdc:d57f28027b2d6f82b96f5413bf8c9a59
  id: nmdc:wf-99-i3NwIC
  name: MetagenomeAnnotation activity for gold:Gp0127631
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127631
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:8f8931e086f72961675aa936b1356f86
  has_output:
  - nmdc:b8d886e71031cbe4fb1284f479348740
  - nmdc:aeafeb18adb193b1a3c5c3c2ff9a912e
  - nmdc:2395040203b3351554a9e3ffb48b0b88
  - nmdc:a89e8af0fc6daf895e7a87f1ff7087f2
  - nmdc:89b895fbf3c13801ddba22ff59bb385a
  id: nmdc:wf-99-GjHwbW
  name: MetagenomeAnnotation activity for gold:Gp0127632
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127632
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:e04c866a9a015bec110f1235db7223dc
  has_output:
  - nmdc:31e2f5b7b055f2959d50a990ebda7ff6
  - nmdc:9ef3a52b2d97cc4afb64e37d04e59865
  - nmdc:740240c975daffee3e63251fc86cfd33
  - nmdc:79fd564d59bf9fe4cfb2c771daa84f29
  - nmdc:b18381667b4e7401e1bb58e8aede5d4a
  id: nmdc:wf-99-wx4FsZ
  name: MetagenomeAnnotation activity for gold:Gp0127633
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127633
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:b502e282cb52690232ce6ec6e1cfd4bc
  has_output:
  - nmdc:01b078b5b9dde5699e9b9ab02af272df
  - nmdc:5b2ff10d97d2b516716a67dafb137937
  - nmdc:803451414e1935d4de9f9911963efe8d
  - nmdc:3374b8708ae6b77b16cd01ce4f33ee72
  - nmdc:1e286398d6b164538bbdefb9cc8a41e9
  id: nmdc:wf-99-av43Nc
  name: MetagenomeAnnotation activity for gold:Gp0127634
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127634
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:178298f959546299f78fb2bff07cd460
  has_output:
  - nmdc:9e0a73962f7014df93613b04fae9f8be
  - nmdc:4cddc89fb8b405210d66b836825c37ee
  - nmdc:4768d5de701a1ac55ed0c2d57a270dd2
  - nmdc:b2ee2639269e6d665f772fc8c4e31d07
  - nmdc:e1cd02b3a92223d8e30e8d7c90837d9a
  id: nmdc:wf-99-UbQ1cX
  name: MetagenomeAnnotation activity for gold:Gp0127635
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127635
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:555541de209f6b5bc8b4e36f9c5a96c1
  has_output:
  - nmdc:80ec7d76d2509e6eeab61d092808908b
  - nmdc:d68e6d4245c33a73666148570aac9c10
  - nmdc:31f8346eeca4b929a6c28686bb8b2043
  - nmdc:66d9d6751efad0b8019a565488f950a5
  - nmdc:e3b57dff7ca37c0da6b7d4bfb4450d9c
  id: nmdc:wf-99-43gCPe
  name: MetagenomeAnnotation activity for gold:Gp0127636
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127636
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:d66bd2d4b3ad1abef6787addfb5aa8b6
  has_output:
  - nmdc:1549562abe1044734fab8562585ec161
  - nmdc:ce74f349e03ae28dd49fc5ea4cd1d91d
  - nmdc:74b2fc3dd196a3d615c7d0d478fa2f90
  - nmdc:c43a6b5a306a8f14aab780d8f1bf9c41
  - nmdc:5f6b287493cde8cf8cb49348a2868aa6
  id: nmdc:wf-99-226YUT
  name: MetagenomeAnnotation activity for gold:Gp0127637
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127637
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:ed782cb1e889b9965707363c1324ee22
  has_output:
  - nmdc:3bd360103e4e8fc8f89c1df345367776
  - nmdc:1aba5135d8cddc36da3cd37579be190b
  - nmdc:3da4d2f1c2db68033fa2264f4db7f459
  - nmdc:17993d4fcfa7be4fd4488804d23b67c6
  - nmdc:2ca3e1a0ba8007e86dedbec47e85adba
  id: nmdc:wf-99-QxzAEB
  name: MetagenomeAnnotation activity for gold:Gp0127638
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127638
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:1d1610f39b4543fe7a0ecde2b1d8d710
  has_output:
  - nmdc:7e710e983d3a5ffbddc618c5e252e06b
  - nmdc:ccbc768cb20e4c1b25d7627b611eb8dc
  - nmdc:ee416a49155f7c07bcb776962708fb04
  - nmdc:fccc8283a46f12babeed0b2c7cc4eebd
  - nmdc:d0452fefd4ad4f4cd10c974294bf9058
  id: nmdc:wf-99-JeORrG
  name: MetagenomeAnnotation activity for gold:Gp0127639
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127639
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:e2d5ce50f49731a49740d9f61f630550
  has_output:
  - nmdc:e90b16891cff9bd5b0034cc6c89f8080
  - nmdc:4950dc66d2b5a3c325454fb106d6b726
  - nmdc:86b6734c5eb64c0cae6e95fa7f062123
  - nmdc:1fbb7302a6ad581085d561e9fd3ed802
  - nmdc:812cf8b77747ff65cfd237158535d310
  id: nmdc:wf-99-UKUKLq
  name: MetagenomeAnnotation activity for gold:Gp0127640
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127640
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:a707d24e95ee536650d1cc70bbf997d8
  has_output:
  - nmdc:71306193abf043865cafa413b3ca9c1e
  - nmdc:4ec0cbf7d166057c3d2904b2dd2f6b15
  - nmdc:11d4524c896f4fd678ff05a0547b6b52
  - nmdc:d10b0c9b0d5e646d09c570eb2e08b793
  - nmdc:a33ac2dc640b7088767a99517f22421f
  id: nmdc:wf-99-QhDga7
  name: MetagenomeAnnotation activity for gold:Gp0127641
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127641
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:1e4e73c9d1faa4585cb3a266b5a6cd39
  has_output:
  - nmdc:4f8de602126deeb9ef60cf5f739d601a
  - nmdc:65319d4c3ffdbf5dcdb2e2837aea8cf4
  - nmdc:657b2348517d3e169df0914f5d8a2d21
  - nmdc:263acdd17bdb9ed72102610070da3d65
  - nmdc:9e55f66e86f57487e23029b90a84c4a4
  id: nmdc:wf-99-i0BJTw
  name: MetagenomeAnnotation activity for gold:Gp0127642
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127642
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:e087926bf099d6b56eaa8ed38dc9587c
  has_output:
  - nmdc:0b7fc1ad662f267eaa604075f9968b7c
  - nmdc:b7b422e726f82668cd9c2ea9f0786f41
  - nmdc:f8df0729f51da70739b75a2458e32020
  - nmdc:7434bd60874fc6d05530ee0652a9e18f
  - nmdc:d897fea88896a93843966962f6bbb7be
  id: nmdc:wf-99-CDkOOW
  name: MetagenomeAnnotation activity for gold:Gp0127643
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127643
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:f40e4315c5285ac27f850a924b9f0d19
  has_output:
  - nmdc:03c32c8ae757623520f6211ff641c40a
  - nmdc:3eced892c4712a2b13e805a978ec0819
  - nmdc:0626957517790befa95e8fefad58be0c
  - nmdc:2c7d55cbee1f35793da90275740d3651
  - nmdc:0973e6d47848f6677ced2a8d463670fa
  id: nmdc:wf-99-DNvmyp
  name: MetagenomeAnnotation activity for gold:Gp0127644
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127644
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:eb1d97165017b3e14d15f6407a181be3
  has_output:
  - nmdc:17524561a0e1f2c9d9ffdebc3b2df6a8
  - nmdc:e2b3ea50301aa3efaea18732ddba04f4
  - nmdc:c3a8cfa76e5da83b2b24bc6a52f71952
  - nmdc:2ab0820d09b9c331ec56d7d3e20552e6
  - nmdc:06280b3737fbf704d850ac68da190166
  id: nmdc:wf-99-Oxm5LI
  name: MetagenomeAnnotation activity for gold:Gp0127645
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127645
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:cfb56be5f505927c085fb3105561b578
  has_output:
  - nmdc:9d87100ad8b6278b4a442c4686d7aef7
  - nmdc:5cd2f970cbb8eb5d8e52ac7a08bfb9a3
  - nmdc:c0858f9a847f241ed28f454adb580bf4
  - nmdc:646648c11733f7ab7ea23008729360ce
  - nmdc:94574634e1ccfe241af033259e27df1a
  id: nmdc:wf-99-RiJ5rZ
  name: MetagenomeAnnotation activity for gold:Gp0127646
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127646
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:9aefb925f949c698cd2a0d71d1d2d7cc
  has_output:
  - nmdc:18d40bd5ff2707ba9a4512363d05537d
  - nmdc:d855bc2d72a6ba238acfe746299cf26a
  - nmdc:af2496c3ae96ff31e6bdaae75b507ea7
  - nmdc:ec6d01297279eee2d4c03ecfda9309c9
  - nmdc:a57c9b7f192351676e897b8187cf6641
  id: nmdc:wf-99-3Xgfcz
  name: MetagenomeAnnotation activity for gold:Gp0127647
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127647
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:621134d8dd8a6b117924f92ffed69ba7
  has_output:
  - nmdc:06042b9d083bd6b9879bc5486c0b38ba
  - nmdc:1287c2532770a0f0d6792192c7400c0c
  - nmdc:c11e44f28b422233e151d324d2accb43
  - nmdc:d27fabc532b52dec4afa4673f920633a
  - nmdc:863f93ecf208a6e19f17d460d8e1a963
  id: nmdc:wf-99-0gilcH
  name: MetagenomeAnnotation activity for gold:Gp0127648
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127648
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:6300cd8140abe6322e4a9c1921584476
  has_output:
  - nmdc:a14b836f963c0f6b02a70f0fc8cd40c0
  - nmdc:35c0fd91c2225f595df469b61ba9578b
  - nmdc:a022fd9c3254ad5dc6ae5be40cd35c0b
  - nmdc:56c3ac34fb2f1c2ba7bcd9bd56be731a
  - nmdc:cff0a71781a84c7096ee79b39c3336f8
  id: nmdc:wf-99-3TAfCa
  name: MetagenomeAnnotation activity for gold:Gp0127649
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127649
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:49c49b255b8db84f4b79e0ad5a963c82
  has_output:
  - nmdc:2a7c5ba82dff4dd5d996ad5bc824103c
  - nmdc:84dc1abc2d39254da6c3d2cd6cff6d9d
  - nmdc:e25cb289f398c007806c72c080724872
  - nmdc:67dfacdfc27cb6b0ec4787e1a40d9547
  - nmdc:714fb73a8b3011d0b2faea98eda477c3
  id: nmdc:wf-99-Uv1aai
  name: MetagenomeAnnotation activity for gold:Gp0127651
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127651
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:e8bc7228a422a7c1a2641276ee3f6e37
  has_output:
  - nmdc:06ceb99673dcb924ca223539267a962a
  - nmdc:4d16f813aefc09c7720770f065964c49
  - nmdc:80c28fa3efc78e6d23d0abcf1161c983
  - nmdc:48bb698de57cd77bf1ddda9004e89c01
  - nmdc:6b39045cb99ca6220e27c4fa960f4dd1
  id: nmdc:wf-99-XcNXLE
  name: MetagenomeAnnotation activity for gold:Gp0127652
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127652
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:c9708409d9e8f45dcc89e688b3482e5e
  has_output:
  - nmdc:05cc9ce5321d6bc909ab63b8cbc59d02
  - nmdc:44f8e708349a1effdff745880f4fdd12
  - nmdc:8d83e502a533b5db8cd3bc943ae8b18b
  - nmdc:658231efecf9d087ec2a6e9467f4e968
  - nmdc:511ae319ddff2bdcbc3296d951e42d7e
  id: nmdc:wf-99-RGaB6W
  name: MetagenomeAnnotation activity for gold:Gp0127653
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127653
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:cd12b50afea3097034758d6883864dd5
  has_output:
  - nmdc:b785c7809fa99d5beca859eded4a9b0f
  - nmdc:3b7734343770dce929591ee83d96acb6
  - nmdc:b28a675c6560b34691a960f7e873841d
  - nmdc:deda4116aac7e262c0edf3358bb8e384
  - nmdc:a9cf54b925e1c5b8c3e0299730f5a464
  id: nmdc:wf-99-z7uO9d
  name: MetagenomeAnnotation activity for gold:Gp0127654
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127654
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:2860c363baa5fd6e5bbdc96a8d54b56b
  has_output:
  - nmdc:32c6c6dbce4a1c6ab92810a86f90c574
  - nmdc:6d1185f4034e364b74109d40326a450a
  - nmdc:0b4a5dc91c42b7fea3fd514d5cb3138b
  - nmdc:a31096eb3e473fd0c68d09096bc3fd85
  - nmdc:05e2702ecae6ba0ba0b0898132850b9f
  id: nmdc:wf-99-jz3us6
  name: MetagenomeAnnotation activity for gold:Gp0127655
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127655
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:3dfd278d5e4fc3539b6dfd021acdac76
  has_output:
  - nmdc:33e0f5ff7c448ded210f04798894a031
  - nmdc:8d230dd7948d2b08c4de1adc0d0002b8
  - nmdc:00f42710ff9df37cd23e5e73d54e4dd1
  - nmdc:2819bbb349ca5bdbf311aeae6ada532b
  - nmdc:0c2ae5a86d4840a0b324d73977170f1e
  id: nmdc:wf-99-a9m4gL
  name: MetagenomeAnnotation activity for gold:Gp0127656
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0127656
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:b78f599c21fb31b00d3f8a3c56daeb88
  has_output:
  - nmdc:8a812604db9b4e2bdbad6d0b3539f6ea
  - nmdc:76537a4ab5012ba3b407471da373ef1c
  - nmdc:bc034c7024043ea88b44d0897bb5bece
  - nmdc:fc419491cce16671e828d76083252841
  - nmdc:10117f9500d0dd54655a5d70195f7df5
  id: nmdc:wf-99-yo16Ew
  name: MetagenomeAnnotation activity for gold:Gp0115664
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115664
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:333b8256818eefecf0581f31a45719f9
  has_output:
  - nmdc:b30bdfcd025588bd80ebb3bcdad2cdc8
  - nmdc:7ab72f45de20843e167ee1e595bb752d
  - nmdc:e745ff0c0a95c89393f8789cd8c409e9
  - nmdc:51f3c008db6a106ee14e160f35f7d9f3
  - nmdc:dcb8211231f718d57e22f8dea1efc6d0
  id: nmdc:wf-99-vhVDYB
  name: MetagenomeAnnotation activity for gold:Gp0115675
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115675
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:b2f2d476b77fca0725cb68b0305ea3b0
  has_output:
  - nmdc:da4d331daa6d5965be8e201c3c9ba4d4
  - nmdc:73cac6bcbfa2627ab291bf230ded9748
  - nmdc:b7264d7a1c56fc32c4a0c050fe04208e
  - nmdc:d325906b9b82b3bfc2fe8ed7321a828e
  - nmdc:2fba563f11988f4e30d2b4283c3c5487
  id: nmdc:wf-99-nlSyxA
  name: MetagenomeAnnotation activity for gold:Gp0115673
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115673
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:9ca27b985234aaed07e3f6659e0416d0
  has_output:
  - nmdc:8a39e09943350e563b00e23a146c3ec1
  - nmdc:34d53203f08e6c25c8f85f6e04d6df24
  - nmdc:e7df895e1a7776ba16b6d77fdc9b077d
  - nmdc:c0365d39cb481d6e0f729b587dac10c8
  - nmdc:bfbd1bd1ad70307dd01b699ecc4ffb2a
  id: nmdc:wf-99-eo5wHj
  name: MetagenomeAnnotation activity for gold:Gp0115677
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115677
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:d1dee40a000226d9f2c8f4f05e0f85f1
  has_output:
  - nmdc:240064338b65f944556e88ebd44fbd03
  - nmdc:cfe4a8ce52735eedacc38bacdc8785e4
  - nmdc:6d1553b3e100a61f3b2b453fb7e71094
  - nmdc:78a99f435ce2bdd6cd83ebb807dc0ef3
  - nmdc:ac989404b8a9e07880788cfb061015ba
  id: nmdc:wf-99-ecPEJ8
  name: MetagenomeAnnotation activity for gold:Gp0115678
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115678
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:2235febcd5329a40beb86d8d8411e0c1
  has_output:
  - nmdc:b4a623a8d9418c04567b5712889fcdfd
  - nmdc:e28746f79f2d58d71fd5f42dff8b6dd5
  - nmdc:dceabe03f9758a72038b9824794337e1
  - nmdc:1b5b79d300bb60afffec76da4cda7f14
  - nmdc:431860b46c896880c1d8d779fb2645ec
  id: nmdc:wf-99-PTHtcy
  name: MetagenomeAnnotation activity for gold:Gp0115665
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115665
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:cbbbd9da9ae7fc0d7cd3ad507977a0fe
  has_output:
  - nmdc:75e88ab163c9d092836f9110768c6a52
  - nmdc:9c6c644e821021661d936d374ee9fc1b
  - nmdc:8f5a7f2db6790e67282439becd4c04b2
  - nmdc:f5a4336c7ac10e908cfe90a61a991c65
  - nmdc:ad6e88d469fbad7b0684afb933403a6c
  id: nmdc:wf-99-jwN3cK
  name: MetagenomeAnnotation activity for gold:Gp0115671
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115671
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:aa60f90793266081a0ba6d125fb06e55
  has_output:
  - nmdc:4e3f389524497182aa3e8832aa7b373b
  - nmdc:ab262feeaf856be190b60ea7c0a4c030
  - nmdc:a1e8795537eca0522357d60045780ab3
  - nmdc:70c8e0fc6e64b20e99a4c0f783014142
  - nmdc:654201c4699079bdd923dcff52881c07
  id: nmdc:wf-99-Cgtoyl
  name: MetagenomeAnnotation activity for gold:Gp0115666
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115666
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:17cff5e222ad522c357863eb39418117
  has_output:
  - nmdc:e74cb5e168717574193a15d5ac04a01f
  - nmdc:0bc9b55e2d8f3c45b18725845815bfde
  - nmdc:4f7a6e682f6f13b7ea73511265fdd2a9
  - nmdc:6de20d427454895dce6caeb7b9543c11
  - nmdc:9c68523f458ee1f8ec395e1442b1f508
  id: nmdc:wf-99-EfFMDW
  name: MetagenomeAnnotation activity for gold:Gp0115669
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115669
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:28a8512eff8b81cebce0614fe5ed18a0
  has_output:
  - nmdc:babc9f95621eed35bc7975dee8b417b9
  - nmdc:bc5043b689463c3651c15ad4ba1aa9a4
  - nmdc:c47020ef7958f3a4c4458e0797fc2400
  - nmdc:acdedd1c48e28e4f4e0d0679cae417f9
  - nmdc:6f236cc8b728333fcf85e4f27873a500
  id: nmdc:wf-99-0AwQGw
  name: MetagenomeAnnotation activity for gold:Gp0115667
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115667
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:6525bd7de120f6ed4dd75069d597f261
  has_output:
  - nmdc:bc4755bf8b2c0b7c384eb4ffd8e9e017
  - nmdc:23762ea8dc5ce375c3827aded41ae2c0
  - nmdc:d429e7a9bb0344196ed7bcca6131e3c0
  - nmdc:5193d8fa7e151b96396afa8d61851af8
  - nmdc:e3b04bb85be48814ca078ee871a9296b
  id: nmdc:wf-99-CroPRX
  name: MetagenomeAnnotation activity for gold:Gp0115676
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115676
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:0ce94528dc5ad4d5b62293d4d95c1e9e
  has_output:
  - nmdc:bcbae14f9733da2b512b5f5b6c8fcb98
  - nmdc:dbd78725415f5f8e80f590c3588a1c60
  - nmdc:c57d28f7dd791aab5c4caee00b247ef9
  - nmdc:f97c44951275f8b68fa94ded40fda756
  - nmdc:b4764f173896dcb134d7c94c1ee13ca3
  id: nmdc:wf-99-HHkLNr
  name: MetagenomeAnnotation activity for gold:Gp0115668
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115668
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:0a3d00715d01ad7b8f3aee59b674dfe9
  has_output:
  - nmdc:27319f58c616a07159e1fac12635bd4b
  - nmdc:8d250650c90956edff8bafccc56fd630
  - nmdc:b7e9c8d0bffdd13ace6f862a61fa87d2
  - nmdc:754074d3bcade65aba2a6f8236619ab7
  - nmdc:a4b4c623457aa10161d88a9ac4eef522
  id: nmdc:wf-99-VCC4zi
  name: MetagenomeAnnotation activity for gold:Gp0115663
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115663
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:6c7beb91bbdcda84076fd786d59cab20
  has_output:
  - nmdc:483453952f8e4dc70687e02842b2bfc8
  - nmdc:4226d30b4f7d4018245613abbb2cc254
  - nmdc:75a1e23a29f8b793c0b0abb7778d8661
  - nmdc:7e531f55eba2bd29d5bb4b1af8417b7c
  - nmdc:f05ecf0db08d716edb7a3f499582a2b7
  id: nmdc:wf-99-w74cHl
  name: MetagenomeAnnotation activity for gold:Gp0115670
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115670
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:f74d007a0d55515291e2ab3ecd50461f
  has_output:
  - nmdc:e029f10a29dd5e9d81dce82c2211fdee
  - nmdc:f6230d3d3eadab80074ecfe59a623c10
  - nmdc:5c1afd4ffb1b1594807fbd0901da7a88
  - nmdc:b0687d58e2803a41864c9d830977402b
  - nmdc:644d67586f9337bf4d12ff5859d4cd54
  id: nmdc:wf-99-bSPq9H
  name: MetagenomeAnnotation activity for gold:Gp0115672
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115672
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:1689f2f2e14c55ab5d2af78ad3eb99bd
  has_output:
  - nmdc:72ede7603b72206d929c03364769021c
  - nmdc:9c248ab2a22c7b49060e544f37b9c798
  - nmdc:876382e7107a83b87a059e4e961bff75
  - nmdc:c70d6973abeb3ee231d3e38c3c5dced4
  - nmdc:17f2fbdeb3f5891c37f2e9e43a40c7b1
  id: nmdc:wf-99-0UgR6E
  name: MetagenomeAnnotation activity for gold:Gp0115674
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115674
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:4fb2f3e8ebd99cea1e797e248b2e5c1d
  has_output:
  - nmdc:aa5fa1b83592459bd3e742be4949d0b1
  - nmdc:ee75eaed19b9a259e0e70e20a53f7fba
  - nmdc:b8c895face8e8e77bbfc7163c7eb7850
  - nmdc:21f3d777493f87403b60a4a1b3dd2f1b
  - nmdc:b63b42c7892b4a14e5661bca5bfa2419
  id: nmdc:wf-99-fLwkIr
  name: MetagenomeAnnotation activity for gold:Gp0115679
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0115679
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:40addaf8b9d84a5d076dbd654eb840a1
  has_output:
  - nmdc:0c9d8d131453a814cc825668d7c18987
  - nmdc:cd0dca213375e3c8b0266932dfff5bb6
  - nmdc:a487ead0b28de8ac44169345638c140c
  - nmdc:1d25e5266e86688b9e65764a9f181e27
  - nmdc:3725668a447e1c7e7e639376a1017e8f
  id: nmdc:wf-99-aIy9XQ
  name: MetagenomeAnnotation activity for gold:Gp0321263
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321263
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:b7ff9345cd91d675846caf34f557f4f7
  has_output:
  - nmdc:3bbaf98e3147e0e0ef35aa56f99775b6
  - nmdc:035b62005530d9f9927da7ac7b9d4407
  - nmdc:a76306b513c2c244bf2899284eed67c4
  - nmdc:409f86c6fccbe946bc56108427b01108
  - nmdc:e4e0da015bbaafeb9199ad669ae71702
  id: nmdc:wf-99-oWCV5s
  name: MetagenomeAnnotation activity for gold:Gp0321264
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321264
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:778bdc544d09cf85360c78a1dd2e263c
  has_output:
  - nmdc:175f44d76765b2555c0e94e5f05fd3a1
  - nmdc:63a567ada447f75cfc2c7fd2d45f8a39
  - nmdc:f4aaf8a82d86aa0273b984ffb1c52dd6
  - nmdc:1de4cc65fa1e329eccf2cc9982b126aa
  - nmdc:b91dc0c20caa465338c63c01e2c1328c
  id: nmdc:wf-99-lEBJxj
  name: MetagenomeAnnotation activity for gold:Gp0321265
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321265
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:a1c12622adf52a2fd9f0fa79302a03e1
  has_output:
  - nmdc:0448dc8c7da28b362275a213adfaeaf6
  - nmdc:8314866bf8dc46a8934cf8b193e21b2e
  - nmdc:422fda8c954e7ffc99883d561fb6f75b
  - nmdc:a98cf4ad6cc56d5a1992c1c5b8027525
  - nmdc:e19fcc4f4eeb2ebaa6deec9f53e1e2d7
  id: nmdc:wf-99-qlz9HX
  name: MetagenomeAnnotation activity for gold:Gp0321266
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321266
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:5660c815bdf2b740f4d1942e8cdb5611
  has_output:
  - nmdc:8c46e28d633eb9243f9edd0368a66f44
  - nmdc:9cb8fdc5cd7bd605f3fcff2ea39cfbf5
  - nmdc:e2708c2679b2002486bb6c4cc1fcc1f1
  - nmdc:716d26a135a99c9efc8c49d4b294f8e8
  - nmdc:ff9b33e360b07cf16501e4002cceb1a3
  id: nmdc:wf-99-2Qr8Pe
  name: MetagenomeAnnotation activity for gold:Gp0321267
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321267
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:59b28e87d2e4c7c9c796cfc1d5ac93ac
  has_output:
  - nmdc:c530c02506fb7f4c0e90eaa46ef931f9
  - nmdc:9047db5ed7d535f7a8cf238feea4112e
  - nmdc:d8e3a237e08fe7b14816ed38cb15f7e5
  - nmdc:313edf6edf574cd30a06f3695c98c0fe
  - nmdc:8ebacf3cb9208f5788c4a664e2bb6155
  id: nmdc:wf-99-vlNUXC
  name: MetagenomeAnnotation activity for gold:Gp0321268
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321268
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:2b0b0ceb40543eab2045a790f18ede00
  has_output:
  - nmdc:d110ababa05ffea4c73fd7f6c2823a01
  - nmdc:0edba9c3bac0163e9ee8d3acc138f0be
  - nmdc:920ffe0caa9796066c6dc232ca29e4bf
  - nmdc:8036d9e860e7c6ac63d62389b012cc39
  - nmdc:1eebc50c86e6e560d910b68358c76117
  id: nmdc:wf-99-T4zSdA
  name: MetagenomeAnnotation activity for gold:Gp0321269
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321269
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:c3131aef261fe1ff6a16d30705a40ba8
  has_output:
  - nmdc:513baf8db74eaf64d7aa7698f1cf31b7
  - nmdc:e9a333448ef41a27086e8df2b1ba6476
  - nmdc:488174c4683c9fe45eae35664a4f7774
  - nmdc:f76b4199f7c1a19bbec3f8a3c39967c8
  - nmdc:d325fdb48d28bb5e04b261496c897a80
  id: nmdc:wf-99-fPJH8j
  name: MetagenomeAnnotation activity for gold:Gp0321270
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321270
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:c293b6b51556d2c536a4f59488498829
  has_output:
  - nmdc:55982ed44eeba03a461a3b837f8344d8
  - nmdc:ede2997cb8cb2cdd14d9aa415157ecdd
  - nmdc:1e90bfe885aac91db1abd71c03ff283c
  - nmdc:1492b148b7432379040c78f4b1d84eed
  - nmdc:d5241932493adac238e254fe0ea0b1b3
  id: nmdc:wf-99-vvPofB
  name: MetagenomeAnnotation activity for gold:Gp0321271
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321271
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:009f426c6f632a1c4c437695ab32ffc9
  has_output:
  - nmdc:18bc1ef31ea841c4eb135a4598d4643e
  - nmdc:e20aeed82d3c566fcc454be8dcb30a48
  - nmdc:f5dc696f69438dcbaa2c5c1685db322e
  - nmdc:311a2b8d368d7f20869eb709f6a2fbca
  - nmdc:456ee70f5d3428e1a1326bf3b3a3f45b
  id: nmdc:wf-99-ulEnFz
  name: MetagenomeAnnotation activity for gold:Gp0321272
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321272
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:e8b2fd75ef4ade7cb2ddcf7518b9441c
  has_output:
  - nmdc:bfa6d313b084b76f378fe23e58693729
  - nmdc:cd1b72215cb87dcc9f582a4b42ba39e2
  - nmdc:edd6a05489d203f580a0c8b4db6f239b
  - nmdc:fd5fd05a55dad39734cb7845be8f1455
  - nmdc:f6c682e41266abf2a82301cee11ecc2c
  id: nmdc:wf-99-ltxbNs
  name: MetagenomeAnnotation activity for gold:Gp0321273
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321273
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:1fa65ac6726132609611b14a32375702
  has_output:
  - nmdc:75c5338fc5735f215fbff0c0a7ea89f7
  - nmdc:451db12e17920c73990ed6019cffb75e
  - nmdc:7c860f38be54584abbf65b05d023ab9b
  - nmdc:880903dfa10de6c316ea4b5648c65022
  - nmdc:28399ee3579aabdd7a96181a85a36b08
  id: nmdc:wf-99-eWTU43
  name: MetagenomeAnnotation activity for gold:Gp0321274
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321274
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:cdcfea8549196bff3b249f57b2b10214
  has_output:
  - nmdc:b134b99e3681cb2f6882d70e0505a295
  - nmdc:a94304d7af292aefec5fbeb0bcbb7685
  - nmdc:4d8a2a87ea74daac3495c512fd96d96c
  - nmdc:ad8da930414a7a388eb050a8b6fc089f
  - nmdc:6f23809a438fa0ab8784393345dd9485
  id: nmdc:wf-99-YDynsC
  name: MetagenomeAnnotation activity for gold:Gp0321275
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321275
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:48e1a9d8fbb26b86ca7690ea86fdd226
  has_output:
  - nmdc:1195d877af5d70a04d1af414939fe76a
  - nmdc:afa84ad89ba252703ca11305b2b45915
  - nmdc:98f986365776814d44158c1ef6cfd5e0
  - nmdc:cbfb3e7e74bb881dcb516e1d0388a9f7
  - nmdc:6c84c9ba98e6d4420568ccdee2d8f0ba
  id: nmdc:wf-99-tMBif9
  name: MetagenomeAnnotation activity for gold:Gp0321276
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321276
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:95ac596eeef164fae7a2810d2719070f
  has_output:
  - nmdc:e78cc5ab16e013800bd4cca3a76ca314
  - nmdc:a654d80633b26c66d4c6dd30988e3083
  - nmdc:7a00101741bd9366a36d6e2a60cf0345
  - nmdc:835275caf77ddcc493b4354cb4d10eab
  - nmdc:7222ad2fb0e606000ea88c4d22595c1b
  id: nmdc:wf-99-XjMQse
  name: MetagenomeAnnotation activity for gold:Gp0321277
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321277
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:dad86bb85b336bcdb636b084b8e73774
  has_output:
  - nmdc:a964f01c89dd3b6575fd1214fe021c3e
  - nmdc:aff1f1e47e91e8df247fed3a28a6998e
  - nmdc:f620e02d2c26b5f2c0db7d77f2168e66
  - nmdc:2cd8a777b2b2f56a47e8f99269c2278e
  - nmdc:36c79ccbf21d3d76d92e670e24ca0321
  id: nmdc:wf-99-henu5l
  name: MetagenomeAnnotation activity for gold:Gp0321278
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321278
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:df768c9feb5f43f1c5f1d86f0b3056f8
  has_output:
  - nmdc:e93e03eb9d260a9ff4d58f10f8ce033d
  - nmdc:8756ede859a2eeb165294bc60757161a
  - nmdc:32ca08ad6221ce0282f7e560d84b6bc1
  - nmdc:1150c8570758aea8c9b32602ac9df694
  - nmdc:3be5100c3d71a32afbe19ba3bd9648d2
  id: nmdc:wf-99-uw8bXm
  name: MetagenomeAnnotation activity for gold:Gp0321279
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321279
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:567601493de0856012f9ea4e6fef9107
  has_output:
  - nmdc:287108afe4b88d94e576549e1053fd72
  - nmdc:1f5cd6b40da64aad6847e6b393764ba9
  - nmdc:4541de98c3049d59ca8aed9b5dce9096
  - nmdc:ca620fc038f51501e1dd5af9bf085231
  - nmdc:20def41369f21c85f890c13663dc7c38
  id: nmdc:wf-99-NPUIdn
  name: MetagenomeAnnotation activity for gold:Gp0321280
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321280
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:205be20f2bdbe32f19cac507c398d62a
  has_output:
  - nmdc:aaacc4e710bee5cd3dcf0373126df7df
  - nmdc:7fb1738c852a309fba1fbc2d608da042
  - nmdc:37e76dc62740e3e9cde6fd0ac56fd149
  - nmdc:27eb4ee0689bfa1ed5de639be9dfe4a4
  - nmdc:5adfd50423654d4ee2a7ea1cb047903b
  id: nmdc:wf-99-2Kolge
  name: MetagenomeAnnotation activity for gold:Gp0321281
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321281
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:868d58953f9ec7fcdfeae0ed168fa8fa
  has_output:
  - nmdc:59a2715743627c1746e93b3c4737c7a1
  - nmdc:18957818ea8c9b81ca7cc6b051109f98
  - nmdc:2fe451504079842f4aed6fc3fc4234f0
  - nmdc:b4785d3de1e96579a0139fd62b46c2b1
  - nmdc:64eb490c848063b2d2ec3a67e25e9fc0
  id: nmdc:wf-99-KIP9Ra
  name: MetagenomeAnnotation activity for gold:Gp0321282
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321282
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:fde97881f9654b875616b4d73fb5d6fd
  has_output:
  - nmdc:3a1dcb36da8d2a8e0bd75839eb87ea92
  - nmdc:b609fcbf134b41436694f56d0206e33d
  - nmdc:50bc1b45ffe95d3def7b0acc0652082f
  - nmdc:371a4bc8b331c5a58f5eae72aa7f2ef2
  - nmdc:dae48dbf003f88ae694fa4461cce315d
  id: nmdc:wf-99-v30BKk
  name: MetagenomeAnnotation activity for gold:Gp0321283
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321283
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:436c60e246576c9ea7eef80eb60d03e4
  has_output:
  - nmdc:3760f2f322ccb7bd25bd9e73529e4bc0
  - nmdc:46f93869937443dd0c5c75e22877cb49
  - nmdc:0f5d384d0a5394fec7546cd4a16dc5cb
  - nmdc:73c7f3cc99686ec1e603fa63596b904f
  - nmdc:79216bdd4f78c73571a7eba424e10b4c
  id: nmdc:wf-99-ZIuifm
  name: MetagenomeAnnotation activity for gold:Gp0321284
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321284
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:b8b7349fd2e0c665bbbdd87ca0226726
  has_output:
  - nmdc:fc6955e36b421ec712ba81c97c4c4e93
  - nmdc:8f00996444824379a6954cd0baa130b0
  - nmdc:03846205920d3904b3f43807834cb364
  - nmdc:4ce337ca93786854ba56d9869e14f591
  - nmdc:deb40e1f540d8c3d4b50d76104b1a095
  id: nmdc:wf-99-GGDI6V
  name: MetagenomeAnnotation activity for gold:Gp0321285
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321285
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:159f0ce3b00a313f8388e13a7835be4b
  has_output:
  - nmdc:b6366ea7a835691458a6872883636362
  - nmdc:d669d8eae9d8b5949796eb2f4cc393f1
  - nmdc:f3e17fae5f6e76fa3b1cfa03113dde8f
  - nmdc:1272bd3b3af9bc77f17cc05e368bc7e0
  - nmdc:5a4038e9f86c14507cb7a280cf311d84
  id: nmdc:wf-99-bKBOWR
  name: MetagenomeAnnotation activity for gold:Gp0321286
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321286
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:e444c151de53be9abd34e58acf2be075
  has_output:
  - nmdc:714f824d90dea21a06e22e5f70473aed
  - nmdc:6caf7a14da0812f5e57cb4697bed9461
  - nmdc:1db0880091c36c0977ce45f22dc58464
  - nmdc:f831f58e1761dcde174db82a8054d4a2
  - nmdc:d058d233fb8da0fa70bf9306d698c2e1
  id: nmdc:wf-99-0oSxaI
  name: MetagenomeAnnotation activity for gold:Gp0321287
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321287
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:9f51c9468e7faed170bf77a03dc30b07
  has_output:
  - nmdc:4a77efe56cb144a8836f95e9e02e5e47
  - nmdc:53ede0b8abd96497214b8d1dc57c5350
  - nmdc:5ae3df50b80d100a3af98a695180fcf8
  - nmdc:c0e0818e6236ece3756233d62402530b
  - nmdc:42abcc0295b474652f5d7e3fd981eaf5
  id: nmdc:wf-99-zwlhtX
  name: MetagenomeAnnotation activity for gold:Gp0321288
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321288
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:c9fca6c9a98430936aade8145d6bee7a
  has_output:
  - nmdc:867066acab1b65ce3f8ec3b2441c7b80
  - nmdc:f3470a6f6205c26c3099cbdd56619dcd
  - nmdc:e5b6e52e7e6da8a3699b8ede666ce1b9
  - nmdc:a1b616853e0d1dcddf8f8c17266a4dab
  - nmdc:e62a9d17906da4a73dd76b04f974d958
  id: nmdc:wf-99-xSa1ZG
  name: MetagenomeAnnotation activity for gold:Gp0321289
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321289
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:53310b5b3d553d212ef78c943eef848b
  has_output:
  - nmdc:847aee43b199ff8396db40d8c4ee3700
  - nmdc:43ba589665945da68f3006d6bfa74021
  - nmdc:0cb130d4376436220b34fa916aa9cfba
  - nmdc:3617ad6fc98edf20a3b5b9b0bc90b302
  - nmdc:848d1a34aad4d6966b3941735cf380b6
  id: nmdc:wf-99-nnWqhU
  name: MetagenomeAnnotation activity for gold:Gp0321290
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321290
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:22a876d17b12588c2a668ce1c26212b9
  has_output:
  - nmdc:2d8dd4456b4d3d1d420258ffa9ab8675
  - nmdc:65f66e255aaa56c68b15083f3c8ce482
  - nmdc:1e698ab3d5a81d4d96de4f820d859817
  - nmdc:410f625da0eaebed66a6e8c18b0e53d0
  - nmdc:bf28aaeaf947e64a6fa762f0a2146946
  id: nmdc:wf-99-nIFZZ2
  name: MetagenomeAnnotation activity for gold:Gp0321291
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321291
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:d7a5f3ca0ce01d380d166d231175d19e
  has_output:
  - nmdc:eb3c2f5a879f052544ffc00f167c3f0a
  - nmdc:513ebcdefc17d2a0419e0d786d8d9c9b
  - nmdc:a301bf732634dc0b2da38821da73bb1d
  - nmdc:23725b4b671305a23b2f9bea1931dd68
  - nmdc:b66392e039cbedc07b2674aa1dba6dac
  id: nmdc:wf-99-yOE0jd
  name: MetagenomeAnnotation activity for gold:Gp0321292
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321292
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:ec774f4a8a52a34daa68ab345856cfd6
  has_output:
  - nmdc:2a021467c5feb3023bac55f1389b7b87
  - nmdc:ab9099fc7d1a32f23fff9091bafb5b30
  - nmdc:329bd25a272982d4116287b8b744e4f6
  - nmdc:92eec5b401629df8c01678ce2717c87b
  - nmdc:7eeac4fe7fa630ac5b85e864f3236f2c
  id: nmdc:wf-99-8LpUgc
  name: MetagenomeAnnotation activity for gold:Gp0321293
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321293
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:3aeced2c6f61639135e21faab643646f
  has_output:
  - nmdc:1bde731a9e60a62eb99f2a5f2055f675
  - nmdc:ef1d19f662d4301ec3a11cfec9d4b652
  - nmdc:de0eb7c5f9e4eb24ae8766920fc7a79c
  - nmdc:a77caadf1701b22232ab50ffddce7d26
  - nmdc:6b79f8e01cfeb858655b267f097ffb9c
  id: nmdc:wf-99-vJ2Mxf
  name: MetagenomeAnnotation activity for gold:Gp0321294
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321294
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:baae9294f2e086c4f4d54522c68a3547
  has_output:
  - nmdc:c4187538344a3306f84ab32a28fdf2e2
  - nmdc:934b09de148e766213549b5e6c684763
  - nmdc:5efc6f0b3731baf5bb49d7e7ff27e7a6
  - nmdc:0aabdc855939a32aa78d16892fb74a31
  - nmdc:8105fb07db3565279cb50332e5fa69e2
  id: nmdc:wf-99-IIrhrj
  name: MetagenomeAnnotation activity for gold:Gp0321295
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321295
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:dcd51279c075c4511406e36450ca6787
  has_output:
  - nmdc:b0a641550c86ac7d2a957e5af1be77a0
  - nmdc:7e9badf5c89fb1a9c593a14566fe5e3b
  - nmdc:97fe89388259cb5c3934bdbdfbe96e0e
  - nmdc:6e7afaa7acf706291e43b65f87c94030
  - nmdc:3ffa7a4a98b5106934e304d22cc2bd65
  id: nmdc:wf-99-eZmaaQ
  name: MetagenomeAnnotation activity for gold:Gp0321296
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321296
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:080bfdc30a14a0ebe427055b82609a59
  has_output:
  - nmdc:0696a840f8ce464eba62eb4341c055a4
  - nmdc:149e480eb0e2ca5bc6204f665b9a2615
  - nmdc:7eeebc5b1c413d9e8dbc15e4af1a695d
  - nmdc:41f5b96405652c89c13226494fc3d472
  - nmdc:69aedbed08dde951f5b5660697731685
  id: nmdc:wf-99-ASXJEJ
  name: MetagenomeAnnotation activity for gold:Gp0321297
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321297
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:c017cf104bfd57c9cb2723ff6ce41304
  has_output:
  - nmdc:35d3ddbc192ecab3a5631db0f76fdf6a
  - nmdc:61c6b1164b53526fb0f00f4c24392330
  - nmdc:84f74f304578f7e593e08e4121839bc2
  - nmdc:cef441d37e63c1221a31e8fad178df3e
  - nmdc:cae5e9077fc171a1e33329bab7526ddc
  id: nmdc:wf-99-J1EP4o
  name: MetagenomeAnnotation activity for gold:Gp0321298
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321298
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:daeccf51c3e846abcd03a4faa65fd237
  has_output:
  - nmdc:4731d121169b2695666f6356610718cd
  - nmdc:901c07c73907fbf0e48b41f8dd51d6e0
  - nmdc:3d7b91fa19ddd4b6ffbb395716fa0298
  - nmdc:fdd916457ddcf1bf5daf58de328918c7
  - nmdc:54cc460952c8094aaace3e475ad49170
  id: nmdc:wf-99-fkLvFW
  name: MetagenomeAnnotation activity for gold:Gp0321299
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321299
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:59e0d4534fe87c754c5818022b38f03e
  has_output:
  - nmdc:6dd3f862aff867342b1a7c84e5c69adf
  - nmdc:43bfe528d2535d158e14fa5644304173
  - nmdc:fe964169df2eccb05f25491090748cc5
  - nmdc:60c0ee336af5cc2039c3f7273e00975a
  - nmdc:ed394322e9312dba63b271c7484797a9
  id: nmdc:wf-99-N8UcIX
  name: MetagenomeAnnotation activity for gold:Gp0321300
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321300
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:80f3a59b2e11321064f589ec0dd1ceea
  has_output:
  - nmdc:23f685792e01b19b7d4c7c9a592e3fc9
  - nmdc:088296d001a191fdba4af60837e4918b
  - nmdc:fd1989f8cf71ca897641a46524242bd0
  - nmdc:fecf564c2c3f7150ad596624178c8c10
  - nmdc:9cfd08fa7dac9d59c866d32fbcd79e8f
  id: nmdc:wf-99-vqx3jd
  name: MetagenomeAnnotation activity for gold:Gp0321301
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321301
- ended_at_time: '2021-01-12T00:00:00+00:00'
  execution_resource: NERSC - Cori
  git_url: https://img.jgi.doe.gov
  has_input:
  - nmdc:4ce9a799923b238585fc952135e5a0f5
  has_output:
  - nmdc:033adebfc63b7f5cd1a0a590c8018281
  - nmdc:6388680dcab4a88c07f21c91777b782d
  - nmdc:5307f9b714e36dee8bf55e3e197ec9b9
  - nmdc:934ee6e733522628856c63b94e5527a3
  - nmdc:9a583be5f87563056c19eb94042bf19d
  id: nmdc:wf-99-HV79Ao
  name: MetagenomeAnnotation activity for gold:Gp0321302
  started_at_time: '2021-01-12T00:00:00+00:00'
  type: nmdc:MetagenomeAnnotation
  was_informed_by: gold:Gp0321302

```
## MixingProcess-minimal
### Input
```yaml
duration:
  has_numeric_value: 2
  has_unit: hours
has_input:
- nmdc:biosample-1
- nmdc:processed-sample-2
has_output:
- nmdc:4
id: nmdc:mp-1
instrument_name: Orbital Shaker

```
## Study-credit-1
### Input
```yaml
has_credit_associations:
- applied_roles:
  - Data curation
  applies_to_person:
    orcid: orcid:0000-0002-1825-00
- applied_roles:
  - Software
  applies_to_person:
    orcid: orcid:0000-0001-9076-6066
id: nmdc:sty-99-WoeqAi
study_category: research_study

```
## Database-ReadQcAnalysisActivity-quality_fail
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
  qc_status: fail
  started_at_time: '2023-08-29T19:41:47.365957+00:00'
  type: nmdc:ReadQcAnalysisActivity
  version: v1.0.8
  was_informed_by: nmdc:omprc-11-r0pjgp16
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
  qc_comment: Number of output reads from readqc is above threshold (6000000 > 1000000)
  qc_status: pass
  started_at_time: '2023-08-29T19:41:47.365957+00:00'
  type: nmdc:ReadQcAnalysisActivity
  version: v1.0.8
  was_informed_by: nmdc:omprc-11-r0pjgp16
- ended_at_time: '2023-08-30T13:26:02.892410+00:00'
  execution_resource: NERSC-Perlmutter
  git_url: https://github.com/microbiomedata/ReadsQC
  has_failure_categorization:
  - qc_failure_what: low_read_count
    qc_failure_where: ReadQcAnalysisActivity
  has_input:
  - nmdc:dobj-11-1k62bt83
  - nmdc:dobj-11-e8hs8y25
  has_output:
  - nmdc:dobj-11-e8hs8y26
  - nmdc:dobj-11-e8hs8y27
  - nmdc:dobj-11-e8hs8y28
  id: nmdc:wfrqc-11-hemh0a90.1
  name: Read QC Activity for nmdc:wfrqc-11-hemh0a87.1
  qc_comment: Most data removed for artifacts
  qc_status: fail
  started_at_time: '2023-08-29T19:41:47.365957+00:00'
  type: nmdc:ReadQcAnalysisActivity
  version: v1.0.8
  was_informed_by: nmdc:omprc-11-r0pjgp16

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

```
## Pooling-minimal
### Input
```yaml
id: nmdc:poolp-9x9-1x
name: first pooling process

```
## Database-processed_sample-minimal
### Input
```yaml
processed_sample_set:
- id: nmdc:procsm-99-dtTMNb

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
id: nmdc:fp-2
instrument_name: CEREX System 96 processor
is_pressurized: true

```
## OmicsProcessing-processing-institution
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- gold:Gp0108335
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
omics_type:
  has_raw_value: Metagenome
part_of:
- nmdc:sty-00-555xxx
processing_institution: UCD_Genome_Center
type: nmdc:OmicsProcessing

```
## Database-biosample_set_low-but-acceptable-rna_volume
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  part_of:
  - nmdc:sty-00-abc123
  rna_volume: 12

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

```
## Database-biosamples-minimal
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  part_of:
  - nmdc:sty-00-abc123

```
## Database-neon_Biosample_to_DataObject_NEON
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  id: nmdc:bsm-99-abcdef1
  part_of:
  - nmdc:sty-11-34xj1150
- env_broad_scale:
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
  id: nmdc:bsm-99-abcdef2
  part_of:
  - nmdc:sty-11-34xj1150
- env_broad_scale:
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
  id: nmdc:bsm-99-abcdef3
  part_of:
  - nmdc:sty-11-34xj1150
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
omics_processing_set:
- has_input:
  - nmdc:procsm-99-xyz3
  has_output:
  - nmdc:dobj-12-jdhk9537
  - nmdc:dobj-12-yx0tfp52
  id: nmdc:omprc-11-s9xj2r24
  instrument_name: Illumina NovaSeq S4
  name: Test NEON data
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - nmdc:sty-11-34xj1150
  processing_institution: Battelle
  type: nmdc:OmicsProcessing
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
processed_sample_set:
- id: nmdc:procsm-99-xyz1
  name: first processed sample set
- id: nmdc:procsm-99-xyz2
  name: first DNA extract
- id: nmdc:procsm-99-xyz3
  name: first library
read_qc_analysis_activity_set:
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
  - nmdc:wfrqc-11-hcr2by04.1
  started_at_time: '2023-03-23T17:17:05.111689+00:00'
  type: nmdc:ReadQCAnalysisActivity
  version: b1.0.7
  was_informed_by: nmdc:omprc-11-s9xj2r24

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
fire: 1871-10-01 to 1871-10-31
id: nmdc:bsm-99-dtTMNb
part_of:
- nmdc:sty-00-abc123

```
## Database-functional-annotations
### Input
```yaml
functional_annotation_set:
- has_function: KEGG_PATHWAY:rsk00410
- has_function: KEGG.REACTION:R00100
- has_function: RHEA:12345
- has_function: MetaCyc:RXN-14904
- has_function: EC:1.1.1.1
- has_function: GO:0032571
- has_function: MetaNetX:MNXR101574
- has_function: SEED:Biotin_biosynthesis
- has_function: KEGG.ORTHOLOGY:K00001
- has_function: EGGNOG:veNOG12876
- has_function: PFAM:PF11779
- has_function: TIGRFAM:TIGR00010
- has_function: SUPFAM:SSF57615
- has_function: CATH:1.10.10.200
- has_function: PANTHER.FAMILY:PTHR12345

```
## ChromatographicSeparationProcess-SPE
### Input
```yaml
has_input:
- nmdc:procsm-11-9gjxns61
has_output:
- nmdc:procsm-11-05g48p90
- nmdc:procsm-11-05g48p91
id: nmdc:psp-99-oW43DzG0
ordered_mobile_phases:
- has_solution_components:
  - compound: methanol
  volume:
    has_numeric_value: 700
    has_unit: mL
- has_solution_components:
  - compound: chloridic acid
    concentration:
      has_numeric_value: 10
      has_unit: mM
  volume:
    has_numeric_value: 700
    has_unit: mL
- has_solution_components:
  - compound: water
  volume:
    has_numeric_value: 1000
    has_unit: mL
stationary_phase: CN

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
  name: DNA extraction of NEON sample WREF_072-O-20190618-COMP
  qc_status: pass
  start_date: '2019-11-08'

```
## FunctionalAnnotationAggMember-minimal
### Input
```yaml
count: 120
gene_function_id: KEGG.ORTHOLOGY:K00627
metagenome_annotation_id: nmdc:8253bcdcd0387177ff895c38a047c719

```
## Database-functional_annotation_agg
### Input
```yaml
functional_annotation_agg:
- count: 120
  gene_function_id: KEGG.ORTHOLOGY:K00627
  metagenome_annotation_id: nmdc:8253bcdcd0387177ff895c38a047c719

```
## Database-analytical_sample-extract-EDITED-TO_PASS
### Input
```yaml
processed_sample_set:
- description: Extracted DNA from WOOD_024-M-20190715-COMP
  id: nmdc:procsm-99-dtTMNb
  name: WOOD_024-M-20190715-COMP-DNA1

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
  name: DNA extraction of NEON sample WREF_072-O-20190618-COMP
  protocol_link:
    name: BMI_dnaExtractionSOP_v7
    url: https://data.neonscience.org/documents/10179/2431540/BMI_dnaExtractionSOP_v7/61204962-bb01-a0b9-3354-ccdaab5132c3
  qc_status: pass
  start_date: '2019-11-08'

```
## Study-emsl
### Input
```yaml
emsl_project_identifiers:
- emsl.project:60141
id: nmdc:sty-11-ab
study_category: research_study

```
## Database-AsemblyAnalysisActivity-1
### Input
```yaml
metagenome_assembly_set:
- ended_at_time: '2020-03-25T00:00:00+00:00'
  execution_resource: LANL B-div
  git_url: https://github.com/microbiomedata/metaAssembly/releases/tag/1.0.0
  has_failure_categorization:
  - qc_failure_what: assembly_size_too_small
    qc_failure_where: MetagenomeAssembly
  - qc_failure_what: other
    qc_failure_where: MetagenomeAssembly
  has_input:
  - nmdc:dobj-12-1243
  has_output:
  - nmdc:dobj-12-1247
  id: nmdc:wfmgas-99-B7Vogx
  name: Metagenome assembly 1472_51277
  qc_comment: 15% human contamination and assembly size is below 5 MB
  qc_status: fail
  started_at_time: '2020-03-24T00:00:00+00:00'
  type: nmdc:MetagenomeAssembly
  was_informed_by: nmdc:omprc-12-124

```
## Database-study-set-with-gnps-id
### Input
```yaml
study_set:
- associated_dois:
  - doi_category: award_doi
    doi_provider: emsl
    doi_value: doi:10.25585/1488217
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
  specific_ecosystem: Permafrost
  study_category: research_study
  type: nmdc:Study

```
## FunctionalAnnotation-exhaustive
### Input
```yaml
has_function: KEGG_PATHWAY:abc12345
subject: nmdc:gene_product_1
was_generated_by: nmdc:activity_1

```
## Database-study-set-with-dois
### Input
```yaml
study_set:
- associated_dois:
  - doi_category: award_doi
    doi_provider: jgi
    doi_value: doi:10.25585/1487763
  - doi_category: award_doi
    doi_provider: emsl
    doi_value: doi:10.25585/1487765
  - doi_category: publication_doi
    doi_value: doi:10.1016/j.foodchem.2008.11.065
  - doi_category: dataset_doi
    doi_provider: ess_dive
    doi_value: doi:10.1333/s00897980202a
  - doi_category: dataset_doi
    doi_provider: massive
    doi_value: doi:10.1093/acprof:oso/9780195159561.001.1
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
  specific_ecosystem: Permafrost
  study_category: research_study
  type: nmdc:Study

```
## Database-omics-processings
### Input
```yaml
omics_processing_set:
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108335
  has_input:
  - nmdc:bsm-00-red
  has_output:
  - nmdc:dobj-00-9n9n9n
  id: nmdc:omprc-99-zUCd5N
  mod_date: 22-MAY-20 06.13.12.927000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 712P3D
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712P3D
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - nmdc:sty-00-555xxx
  processing_institution: JGI
  type: nmdc:OmicsProcessing
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108340
  has_input:
  - nmdc:bsm-00-orange0
  has_output:
  - nmdc:dobj-00-zzzbrxzzz
  id: nmdc:omprc-99-gKlQlF
  mod_date: 22-MAY-20 06.10.59.590000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 612S3M
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 612S3M
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - nmdc:sty-00-555xxx
  processing_institution: JGI
  type: nmdc:OmicsProcessing
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108341
  has_input:
  - nmdc:bsm-00-orange1
  has_output:
  - nmdc:dobj-00-thx1198
  id: nmdc:omprc-99-5kgIJR
  mod_date: 22-MAY-20 06.09.46.171000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 712S3S
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712S3S
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - nmdc:sty-00-555xxx
  processing_institution: JGI
  type: nmdc:OmicsProcessing

```
## Database-nom_analysis_activity_set-incomplete-string-ended_at_time
### Input
```yaml
nom_analysis_activity_set:
- ended_at_time: '2018-11-13T20:20:39+00:00'
  execution_resource: xxx
  git_url: xxx
  has_input:
  - nmdc:1
  - nmdc:2
  has_output:
  - nmdc:3
  - nmdc:4
  id: nmdc:wfnom-99-abcdefg
  started_at_time: 2018-11-111
  type: xxx
  was_informed_by: nmdc:act-99-abcdefg

```
## Database-biosamples-high-rna_volume
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  part_of:
  - nmdc:sty-00-abc123
  rna_volume: 1200

```
## Database-biosamples-dna-in-plate-invalid-well-val
### Input
```yaml
biosample_set:
- dna_cont_type: plate
  dna_cont_well: A1
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
  part_of:
  - nmdc:sty-00-abc123

```
## Database-invalid-omics-processing
### Input
```yaml
omics_processing_set:
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108335
  has_input:
  - nmdc:bsm-00-red
  has_output:
  - nmdc:dobj-00-9n9n9n
  id: nmdc:omprc-99-zUCd5N
  mod_date: 22-MAY-20 06.13.12.927000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 712P3D
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712P3D
  omics_type:
    has_awesome_value: Metagenome
  part_of:
  - nmdc:sty-00-555xxx
  processing_institution: JGI
  type: nmdc:OmicsProcessing
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108340
  has_input:
  - nmdc:bsm-00-orange0
  has_output:
  - nmdc:dobj-00-zzzbrxzzz
  id: nmdc:omprc-99-gKlQlF
  mod_date: 22-MAY-20 06.10.59.590000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 612S3M
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 612S3M
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - nmdc:sty-00-555xxx
  processing_institution: JGI
  type: nmdc:OmicsProcessing
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108341
  has_input:
  - nmdc:bsm-00-orange1
  has_output:
  - nmdc:dobj-00-thx1198
  id: nmdc:omprc-99-5kgIJR
  mod_date: 22-MAY-20 06.09.46.171000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 712S3S
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712S3S
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - nmdc:sty-00-555xxx
  processing_institution: JGI
  type: nmdc:OmicsProcessing

```
## Extraction-invalid_enum
### Input
```yaml
end_date: '2021-08-19'
extraction_target: phenol/chloroform extraction
has_input:
- nmdc:procsm-11-9gjxns61
has_output:
- nmdc:procsm-11-0wxpzf07
id: nmdc:extrp-11-00r2pk65
input_mass:
  has_numeric_value: 0.25
  has_unit: g
qc_status: pass
start_date: 2020-06-24T22:06Z

```
## Biosample-invalid_fire
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
fire: like a volcano
id: nmdc:bsm-99-dtTMNb
part_of:
- nmdc:sty-00-abc123

```
## Database-invalid-studies
### Input
```yaml
study_set:
- baz: blah
  description: Using analytical expertise at both the JGI and EMSL, we plan to follow
    successional patterns of protein expression
  doi:
    has_raw_value: 10.25585/1487760
  ecosystem: Host-associated
  ecosystem_category: Plants
  ecosystem_subtype: Soil
  ecosystem_type: Rhizosphere
  foo: bar
  id: nmdc:sty-00-abc123
  name: Avena fatua rhizosphere microbial communities from Hopland, California, USA,
    for root-enhanced decomposition of organic matter studies
  principal_investigator_name:
    has_raw_value: Mary Firestone
  specific_ecosystem: Unclassified
  type: nmdc:Study
- description: We propose to utilize the unique resources at EMSL and the JGI to obtain
    a better understanding of the phylogenetic and functional diversity of cyanobacteria
  doi:
    has_raw_value: 10.25585/1487758
  ecosystem: Host-associated
  ecosystem_category: Microbial
  ecosystem_subtype: Unclassified
  ecosystem_type: Bacteria
  id: gold:Gs0110132
  name: Cyanobacterial communities from the Joint Genome Institute, California, USA
  principal_investigator_name:
    has_raw_value: Matthias Hess
  specific_ecosystem: Unclassified
  type: nmdc:Study
- description: A fundamental challenge of microbial environmental science is to understand
    how earth systems will respond to climate change
  doi:
    has_raw_value: 10.25585/1487764
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
  type: nmdc:Study

```
## Study-invalid-1
### Input
```yaml
has_credit_associations:
- applied_roles:
  - Value Not In Enum 1
  applies_to_person:
    orcid: orcid:0000-0002-1825-00
  type: credit association
- applied_roles:
  - ValueNotInEnum2
  applies_to_person:
    orcid: orcid:0000-0001-9076-6066
  type: credit association
id: example:123

```
## Database-biosamples-rna-in-bucket
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  part_of:
  - nmdc:sty-00-abc123
  rna_cont_type: bucket

```
## Database-biosample_mismatch_regex
### Input
```yaml
biosample_set:
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - ABCD:Ab@#
  habitat: Coalbed water
  id: XXXX:6057d02c-664c-41c9-8486-3624ca845747
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients (early)
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-8675309
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - gold:Gb0101225
  habitat: Coalbed water
  id: nmdc:e924072f-98b5-4f88-a796-a7ba1d8ddd92
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients Extra
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-8675309
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - ABCD:Ab@#@
  - WXYZ:Wx()
  habitat: Coalbed water
  id: nmdc:61c3332d-f654-4db8-8d2f-59475894daa5
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-8675309
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample

```
## Biosample-non_boolean_embargo
### Input
```yaml
embargoed: 999
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
part_of:
- nmdc:sty-00-abc123

```
## Study-illegal-funding_sources
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
  was_generated_by: nmdc:any_string_1
  websites:
  - https://www.jcvi.org/
  - https://www.jcvi.org/about/j-craig-venter
related_identifiers: any string R1
relevant_protocols:
- any string 1
- any string 2
specific_ecosystem: unconstrained text
title: Sample Exhaustive Biosample instance. Although all of these values should pass
  validation, that does not mean that any Biosample of any type would necessarily
  have this particular combination of values.
type: any string
websites:
- https://w3id.org/nmdc
- https://w3id.org/linkml

```
## Biosample-invalid-embargoed
### Input
```yaml
embargoed: 999
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
part_of:
- nmdc:sty-00-abc123

```
## FunctionalAnnotation-invalid-function
### Input
```yaml
has_function: KEGG_PATHWAY:XOXOXOXO

```
## Database-Extraction-invalid-sample_mass
### Input
```yaml
extraction_set:
- description: DNA extraction of NEON sample WREF_072-O-20190618-COMP using SOP BMI_dnaExtractionSOP_v7
  end_date: '2019-11-08'
  extraction_method: phenol/chloroform extraction
  extraction_target: DNA
  has_input:
  - generic:xxx
  has_output:
  - generic:xxx
  id: nmdc:extrp-99-abcdef
  name: DNA extraction of NEON sample WREF_072-O-20190618-COMP
  processing_institution: Battelle
  protocol_link:
    name: BMI_dnaExtractionSOP_v7
    url: https://data.neonscience.org/documents/10179/2431540/BMI_dnaExtractionSOP_v7/61204962-bb01-a0b9-3354-ccdaab5132c3
  qc_status: pass
  sample_mass:
    has_numeric_value: 0.25
    has_unit: gram
  start_date: '2019-11-08'

```
## OmicsProcessing-no-id
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- gold:Gp0108335
has_input:
- nmdc:bsm-00-red
has_output:
- nmdc:dobj-00-9n9n9n
mod_date: 22-MAY-20 06.13.12.927000000 PM
name: Thawing permafrost microbial communities from the Arctic, studying carbon transformations
  - Permafrost 712P3D
ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
  carbon transformations - Permafrost 712P3D
omics_type:
  has_raw_value: Metagenome
part_of:
- nmdc:sty-00-555xxx
processing_institution: JGI
type: nmdc:OmicsProcessing

```
## Extraction-metabolomics-concentration-without-compound
### Input
```yaml
extractant:
  has_solution_components:
  - concentration:
      has_numeric_value: 5
      has_unit: '%'
has_input:
- nmdc:ome-6
has_output:
- nmdc:ome-8
id: nmdc:extrp-71-r2pk

```
## OmicsProcessing-invalid-omics-type
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- gold:Gp0108335
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
omics_type:
  has_awesome_value: Metagenome
part_of:
- nmdc:sty-00-555xxx
processing_institution: JGI
type: nmdc:OmicsProcessing

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

```
## DataObject-no-id-or-name
### Input
```yaml
description: Crispr Terms for nmdc:ann0vx38

```
## MetagenomeSequencingActivity-no_parthood
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
part_of: null
started_at_time: '2021-08-05T14:48:51+00:00'
type: nmdc:MetagenomeSequencing
version: v1.0.0
was_informed_by: gold:Gp0213371

```
## Database-Biosample-invalid_range
### Input
```yaml
biosample_set:
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - gold:Gb0101224
  habitat: Coalbed water
  id: nmdc:bsm-6057d02c-664c-41c9-8486-3624ca845747
  lat_lon:
    has_raw_value: 100
    latitude: '-33.460524'
    longitude: '150.168149'
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients (early)
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-8675309
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - gold:Gb0101225
  habitat: Coalbed water
  id: nmdc:bsm-e924072f-98b5-4f88-a796-a7ba1d8ddd92
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients Extra
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-8675309
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - gold:Gb0101226
  habitat: Coalbed water
  id: nmdc:bsm-61c3332d-f654-4db8-8d2f-59475894daa5
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-8675309
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample

```
## Database-nom_analysis_activity_set-non-string-ended_at_time
### Input
```yaml
nom_analysis_activity_set:
- ended_at_time: 2018-11-13 20:20:39+00:00
  execution_resource: xxx
  git_url: xxx
  has_input:
  - nmdc:1
  - nmdc:2
  has_output:
  - nmdc:3
  - nmdc:4
  id: nmdc:wfnom-99-abcdefg
  started_at_time: '2018-11-13T20:20:39+00:00'
  type: xxx
  was_informed_by: nmdc:act-99-abcdefg

```
## Database-plannedprocess-incorrect _date_slot
### Input
```yaml
extraction_set:
- extraction_date: 2021-01-15
  extraction_target: DNA
  has_inputs:
  - bare:pool_out_1
  has_outputs:
  - bare:dna_extract_1
  id: bare:des1
  name: first dna extraction set
library_preparation_set:
- has_inputs:
  - bare:dna_extract_1
  has_outputs:
  - bare:library_1
  id: bare:lcs1
  library_type: DNA
  name: DNA library preparation of NEON sample TREE_001-O-20170707-COMP-DNA1
  processed_date: 2021-01-15

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
    was_generated_by: nmdc:any_string_1
    websites:
    - https://www.jcvi.org/
    - https://www.jcvi.org/about/j-craig-venter
  type: any string
- applied_roles:
  - Investigation
  - Supervision
  applies_to_person:
    name: Tanja Davidsen
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
  was_generated_by: nmdc:any_string_1
  websites:
  - https://www.jcvi.org/
  - https://www.jcvi.org/about/j-craig-venter
related_identifiers: any string R1
relevant_protocols:
- any string 1
- any string 2
specific_ecosystem: unconstrained text
title: Sample Exhaustive Biosample instance. Although all of these values should pass
  validation, that does not mean that any Biosample of any type would necessarily
  have this particular combination of values.
type: any string
websites:
- https://w3id.org/nmdc
- https://w3id.org/linkml

```
## Study-has-missing_doi_provider
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
  doi_value: doi:10.25585/1488209
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
  was_generated_by: nmdc:any_string_1
  websites:
  - https://www.jcvi.org/
  - https://www.jcvi.org/about/j-craig-venter
related_identifiers: any string R1
relevant_protocols:
- any string 1
- any string 2
specific_ecosystem: unconstrained text
title: Sample Exhaustive Biosample instance. Although all of these values should pass
  validation, that does not mean that any Biosample of any type would necessarily
  have this particular combination of values.
type: any string
websites:
- https://w3id.org/nmdc
- https://w3id.org/linkml

```
## Database-biosample_single_multi_value_mixup
### Input
```yaml
biosample_set:
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  habitat: Coalbed water
  id:
  - gold:Gb0101224
  - gold:Gb0101225
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients (early)
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-8675309
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type:
  - nmdc:Biosample
  - nmdc:FunctionalAnnotation
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - gold:Gb0101225
  habitat: Coalbed water
  id: nmdc:e924072f-98b5-4f88-a796-a7ba1d8ddd92
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients Extra
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-8675309
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - gold:Gb0101226
  habitat: Coalbed water
  id: nmdc:61c3332d-f654-4db8-8d2f-59475894daa5
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-8675309
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
## Database-biosamples-lat_lon-with-GLV-missing-latitude
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  lat_lon:
    has_raw_value: -33.460524 150.168149
    longitude: 150.168149
  part_of:
  - nmdc:sty-00-abc123

```
## ChromatographySeparationProcess-undefined-solution-component
### Input
```yaml
has_input:
- nmdc:procsm-11-9gjxns61
has_output:
- nmdc:procsm-11-05g48p90
- nmdc:procsm-11-05g48p91
id: nmdc:psp-99-oW43DzG0
ordered_mobile_phases:
- has_solution_components:
  - compound: MeOH
  volume:
    has_numeric_value: 700
    has_unit: mL
- has_solution_components:
  - compound: chloridic acid
    concentration:
      has_numeric_value: 10
      has_unit: mM
  volume:
    has_numeric_value: 700
    has_unit: mL
- has_solution_components:
  - compound: water
  volume:
    has_numeric_value: 1000
    has_unit: mL
stationary_phase: CN

```
## TextValue-was_generated_by
### Input
```yaml
has_raw_value: 1600 Pennsylvania Ave
was_generated_by: generic:xxx

```
## Biosample-incomplete_napa_id
### Input
```yaml
add_date: 28-JUL-14 12.00.00.000000000 AM
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
env_local_scale:
  has_raw_value: ENVO:00002169
  term:
    id: ENVO:00002169
env_medium:
  has_raw_value: ENVO:00005792
  term:
    id: ENVO:00005792
geo_loc_name:
  has_raw_value: Lithgow
gold_biosample_identifiers:
- gold:Gb0101224
habitat: Coalbed water
id: nmdc:bsm-
lat_lon:
  has_raw_value: -33.460524 150.168149
  latitude: -33.460524
  longitude: 150.168149
location: from the Lithgow State Coal Mine, New South Wales, Australia
mod_date: 26-AUG-16 01.50.27.000000000 PM
name: Lithgow State Coal Mine Calcium nutrients (early)
ncbi_taxonomy_name: coal metagenome
part_of:
- nmdc:sty-00-abc123
sample_collection_site: Lithgow State Coal Mine
specific_ecosystem: Coalbed water
type: nmdc:Biosample

```
## Database-study-include-abstract
### Input
```yaml
study_set:
- abstract: This study is about a thing.
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
    doi_value: doi:10.25585/1488209
  description: see also name, title, objective, various alternatives
  ecosystem: unconstrained text. should be validated against the controlled vocabulary,
    by the sample's environmental package. would also be nice to align the CV with
    MIxS environmental triads
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
      was_generated_by: nmdc:any_string_1
      websites:
      - https://www.jcvi.org/
      - https://www.jcvi.org/about/j-craig-venter
    type: any string
  - applied_roles:
    - Investigation
    - Supervision
    applies_to_person:
      name: Tanja Davidsen
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
    was_generated_by: nmdc:any_string_1
    websites:
    - https://www.jcvi.org/
    - https://www.jcvi.org/about/j-craig-venter
  related_identifiers: any string R1
  relevant_protocols:
  - any string 1
  - any string 2
  specific_ecosystem: unconstrained text
  title: Sample Exhaustive Biosample instance. Although all of these values should
    pass validation, that does not mean that any Biosample of any type would necessarily
    have this particular combination of values.
  type: any string
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
## TextValue-forbidden-processed-value
### Input
```yaml
has_processed_value: white house
has_raw_value: 1600 Pennsylvania Ave

```
## Study-using-undefined-genome_portal_identifiers-slot
### Input
```yaml
id: nmdc:sty-11-ab
jgi_genome_portal_identifiers:
- https://genome.jgi.doe.gov/portal/BioDefcarcycling/BioDefcarcycling.info.html

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
  was_generated_by: nmdc:any_string_1
  websites:
  - https://www.jcvi.org/
  - https://www.jcvi.org/about/j-craig-venter
publications:
- any string 1
- any string 2
related_identifiers: any string R1
relevant_protocols:
- any string 1
- any string 2
specific_ecosystem: unconstrained text
title: Sample Exhaustive Biosample instance. Although all of these values should pass
  validation, that does not mean that any Biosample of any type would necessarily
  have this particular combination of values.
type: any string
websites:
- https://w3id.org/nmdc
- https://w3id.org/linkml

```
## Biosample-missing-id
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
part_of:
- nmdc:sty-00-abc123

```
## Database-Biosample-invalid_id
### Input
```yaml
biosample_set:
- env_broad_scale:
    term:
      id: ENVO:00002030
  env_local_scale:
    term:
      id: ENVO:00002169
  env_medium:
    term:
      id: ENVO:00005792
  id: local
  part_of:
  - nmdc:sty-00-8675309

```
## Database-biosample_missing_required_field
### Input
```yaml
biosample_set:
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  habitat: Coalbed water
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients (early)
  ncbi_taxonomy_name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  habitat: Coalbed water
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients Extra
  ncbi_taxonomy_name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  habitat: Coalbed water
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients
  ncbi_taxonomy_name: coal metagenome
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample

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
## Filtration-invalid_bad_data_types
### Input
```yaml
conditionings:
- Methanol
- 123
contained_in: plastic bag
filter_material: PTFE
filter_pore_size:
  has_numeric_value: '0.02'
  has_unit: "\xB5m"
filtration_category: pre-condition
has_input:
- nmdc:biosample-1
- previous step in process
has_output:
- nmdc:5
id: nmdc:fp-1

```
## MetagenomeSequencingActivity-bad_id
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
part_of:
- nmdc:mga0vx38
started_at_time: '2021-08-05T14:48:51+00:00'
type: nmdc:MetagenomeSequencing
version: v1.0.0
was_informed_by: gold:Gp0213371

```
## Database-biosample_undeclared_slot
### Input
```yaml
biosample_set:
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  foo: bar
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - gold:Gb0101224
  habitat: Coalbed water
  id: nmdc:bsm-6057d02c-664c-41c9-8486-3624ca845747
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients (early)
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-8675309
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - gold:Gb0101225
  habitat: Coalbed water
  id: nmdc:bsm-e924072f-98b5-4f88-a796-a7ba1d8ddd92
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients Extra
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-8675309
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample
- add_date: 28-JUL-14 12.00.00.000000000 AM
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
  env_local_scale:
    has_raw_value: ENVO:00002169
    term:
      id: ENVO:00002169
  env_medium:
    has_raw_value: ENVO:00005792
    term:
      id: ENVO:00005792
  geo_loc_name:
    has_raw_value: Lithgow
  gold_biosample_identifiers:
  - gold:Gb0101226
  habitat: Coalbed water
  id: nmdc:bsm-61c3332d-f654-4db8-8d2f-59475894daa5
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
    longitude: 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - nmdc:sty-00-8675309
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample

```
## Database-study_set-bad-emsl-doi-slot-name
### Input
```yaml
study_set:
- emsl_proposal_dois:
  - doi:10.46936/intm.proj.2021.60141/60000423
  id: nmdc:sty-11-ab

```
## Database-biosamples-lat_lon-with-GLV-missing-longitude
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  lat_lon:
    has_raw_value: -33.460524 150.168149
    latitude: -33.460524
  part_of:
  - nmdc:sty-00-abc123

```
## Database-biosamples-rna-in-plate-invalid-well-val
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  part_of:
  - nmdc:sty-00-abc123
  rna_cont_type: plate
  rna_cont_well: A1

```
## Database-using-undefined-analytical_sample_set-slot
### Input
```yaml
analytical_sample_set:
- id: nmdc:ansm-99-dtTMNb
  name: WOOD_024-M-20190715-COMP-DNA1
  was_informed_by: nmdc:extr-1235

```
## Database-biosamples-dna-in-bucket
### Input
```yaml
biosample_set:
- dna_cont_type: bucket
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
  part_of:
  - nmdc:sty-00-abc123

```
## Database-biosamples-rna-in-plate-no-well-val
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  part_of:
  - nmdc:sty-00-abc123
  rna_cont_type: plate

```
## Database-invalid-functional-annotations
### Input
```yaml
functional_annotation_set:
- has_function: KEGG_PATHWAY:XOXOXOXO
- has_function: KEGG_PATHWAY:iIiIiIiI

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
## Database-biosamples-rna-in-tube-with-well-value
### Input
```yaml
biosample_set:
- env_broad_scale:
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
  part_of:
  - nmdc:sty-00-abc123
  rna_cont_type: tube
  rna_cont_well: B2

```
## Study-valueswith-generators
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
- doi_category: dataset_doi
  doi_provider: kbase
  doi_value: doi:10.1126/science.1456956
- doi_category: award_doi
  doi_provider: jgi
  doi_value: doi:10.1126/science.1234545
- doi_category: data_management_plan_doi
  doi_provider: gsc
  doi_value: doi:10.48321/D1Z60Q
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
    was_generated_by: nmdc:any_string_1
    websites:
    - https://www.jcvi.org/
    - https://www.jcvi.org/about/j-craig-venter
  type: any string
- applied_roles:
  - Investigation
  - Supervision
  applies_to_person:
    name: Tanja Davidsen
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
  was_generated_by: nmdc:any_string_1
  websites:
  - https://www.jcvi.org/
  - https://www.jcvi.org/about/j-craig-venter
related_identifiers: any string R1
relevant_protocols:
- any string 1
- any string 2
specific_ecosystem: unconstrained text
study_category: research_study
study_image:
- description: Photo of Craig Venter Institute, Rockville, Maryland
  display_order: 1
  has_raw_value: https://upload.wikimedia.org/wikipedia/commons/8/86/J._Craig_Vernter_Institute_Rockville_Maryland.jpg
  url: https://upload.wikimedia.org/wikipedia/commons/8/86/J._Craig_Vernter_Institute_Rockville_Maryland.jpg
  was_generated_by: nmdc:any_string_1
- description: Photo of Craig Venter Institute, La Jolla, California
  display_order: 2
  has_raw_value: https://today.ucsd.edu/news_uploads/140213ventor2.jpg
  url: https://today.ucsd.edu/news_uploads/140213ventor2.jpg
  was_generated_by: nmdc:any_string_1
title: Sample Exhaustive Biosample instance. Although all of these values should pass
  validation, that does not mean that any Biosample of any type would necessarily
  have this particular combination of values.
type: any string
websites:
- https://w3id.org/nmdc
- https://w3id.org/linkml

```
## Database-functional_annotation_agg
### Input
```yaml
functional_annotation_agg:
- count: 120
  metagenome_annotation_id: nmdc:8253bcdcd0387177ff895c38a047c719

```
## Study-emsl-bad-local
### Input
```yaml
emsl_project_identifiers:
- emsl.project:abc
id: nmdc:sty-11-ab
study_category: research_study

```
## Database-biosamples-dna-in-tube-with-well-value
### Input
```yaml
biosample_set:
- dna_cont_type: tube
  dna_cont_well: B2
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
  part_of:
  - nmdc:sty-00-abc123

```
## Database-biosamples-dna-in-plate-no-well-val
### Input
```yaml
biosample_set:
- dna_cont_type: plate
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
  part_of:
  - nmdc:sty-00-abc123

```
