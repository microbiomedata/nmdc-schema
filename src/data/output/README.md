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
  - GOLD:Gb0150408
  habitat: Fen
  id: nmdc:bsm-99-isqhuW
  lat_lon:
    has_raw_value: 68.35 19.05
  location: Stordalen Mire, Sweden
  mod_date: 08-JAN-20 02.49.23.000000000 PM
  name: Permafrost microbial communities from Stordalen Mire, Sweden - 611E1M metaG
  ncbi_taxonomy_name: permafrost metagenome
  part_of:
  - GOLD:Gs0128849
  samp_name:
    has_raw_value: 611E1M metaG
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
  - GOLD:Gb0157174
  habitat: soil
  id: nmdc:bsm-99-dge3H9
  lat_lon:
    has_raw_value: 42.481016 -72.178343
  location: Barre Woods Harvard Forest LTER site, Petersham, Massachusetts, United
    States
  mod_date: 08-JAN-20 02.49.23.000000000 PM
  name: Forest soil microbial communities from Barre Woods Harvard Forest LTER site,
    Petersham, Massachusetts, United States - Inc-BW-C-14-O
  ncbi_taxonomy_name: soil metagenome
  part_of:
  - GOLD:Gs0128849
  samp_name:
    has_raw_value: Inc-BW-C-14-O
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
  - GOLD:Gb0188037
  habitat: rhizosphere
  host_name: Carex aquatilis
  id: nmdc:bsm-99-dc6tg6
  lat_lon:
    has_raw_value: 47.6516 -122.3045
  location: University of Washington, Seatle, WA, United States
  mod_date: 08-JAN-20 02.49.25.000000000 PM
  name: Rhizosphere microbial communities from Carex aquatilis grown in University
    of Washington, Seatle, WA, United States - 4-1-23 metaG
  ncbi_taxonomy_name: rhizosphere metagenome
  part_of:
  - GOLD:Gs0128849
  samp_name:
    has_raw_value: 4-1-23 metaG
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
  - GOLD:Gp0225767
  description: Forest soil from Barre Woods Harvard Forest LTER site was incubated
    at 10C with heavy water. Sample is from a control plot at ambient soil temperature,
    organic horizon - top 4cm of soil
  has_input:
  - GOLD:Gb0157174
  has_output:
  - jgi:599c3a117ded5e41edd7da77
  id: nmdc:omprc-99-9XUVVF
  mod_date: 16-OCT-20 02.04.01.374000000 AM
  name: Forest soil microbial communities from Barre Woods Harvard Forest LTER site,
    Petersham, Massachusetts, United States - Inc-BW-C-14-O
  ncbi_project_name: Forest soil microbial communities from Barre Woods Harvard Forest
    LTER site, Petersham, Massachusetts, United States - Inc-BW-C-14-O
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - GOLD:Gs0130354
  processing_institution: JGI
  type: nmdc:OmicsProcessing
- add_date: 17-MAR-17 04.55.44.822000000 PM
  alternative_identifiers:
  - GOLD:Gp0208560
  description: Permafrost microbial communities from Stordalen Mire, Sweden
  has_input:
  - GOLD:Gb0150408
  has_output:
  - jgi:58b653757ded5e7a2af951c4
  id: nmdc:omprc-99-dk9vgI
  mod_date: 22-MAY-20 06.38.19.576000000 PM
  name: Permafrost microbial communities from Stordalen Mire, Sweden - 611E1M metaG
  ncbi_project_name: Permafrost microbial communities from Stordalen Mire, Sweden
    - 611E1M metaG
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - GOLD:Gs0128849
  processing_institution: JGI
  type: nmdc:OmicsProcessing
- add_date: 29-MAR-18 01.27.30.036000000 PM
  alternative_identifiers:
  - GOLD:Gp0306221
  description: Rhizosphere microbial communities from Carex aquatilis grown in submerged
    peat from a thermokarst bog, University of Washington, Seatle, WA, United States
  has_input:
  - GOLD:Gb0188037
  has_output:
  - jgi:5baa816646d1e63f764deb37
  id: nmdc:omprc-99-MVW1FV
  mod_date: 04-APR-20 08.26.35.067000000 AM
  name: Rhizosphere microbial communities from Carex aquatilis grown in University
    of Washington, Seatle, WA, United States - 4-1-23 metaG
  ncbi_project_name: Rhizosphere microbial communities from Carex aquatilis grown
    in University of Washington, Seatle, WA, United States - 4-1-23 metaG
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - GOLD:Gs0134277
  processing_institution: JGI
  type: nmdc:OmicsProcessing
study_set:
- description: Thawing permafrost is one of the largest soil carbon pools on the planet.
    The goal of this project is to study microbial communities that participate in
    the soil carbon cycle.
  doi:
    has_raw_value: 10.25585/1488217
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Wetlands
  ecosystem_type: Soil
  gold_study_identifiers:
  - GOLD:Gs0128849
  id: nmdc:sty-99-FkQIsc
  name: Permafrost microbial communities from Stordalen Mire, Sweden
  principal_investigator:
    has_raw_value: Virginia Rich
  specific_ecosystem: Permafrost
  type: nmdc:Study
- description: The goal of this study is to learn the molecular mechanisms underlying
    changes in the temperature sensitive respiration response of forest soils to long-term
    experimental warming
  doi:
    has_raw_value: 10.25585/1488215
  ecosystem: Environmental
  ecosystem_category: Terrestrial
  ecosystem_subtype: Unclassified
  ecosystem_type: Soil
  gold_study_identifiers:
  - GOLD:Gs0130354
  id: nmdc:sty-99-oJmAOs
  name: Forest soil microbial communities from Barre Woods Harvard Forest LTER site,
    Petersham, Massachusetts, United States
  principal_investigator:
    has_raw_value: Jeffrey Blanchard
  specific_ecosystem: Forest Soil
  type: nmdc:Study
- description: The goal of this study is to advance understanding of the response
    of methane production and methane oxidation to changes in plant productivity so
    that modeled representations of these processes and interactions can be improved.
  doi:
    has_raw_value: 10.25585/1488209
  ecosystem: Host-associated
  ecosystem_category: Plants
  ecosystem_subtype: Rhizosphere
  ecosystem_type: Roots
  gold_study_identifiers:
  - GOLD:Gs0134277
  id: nmdc:sty-99-3bQQ4j
  name: Rhizosphere microbial communities from Carex aquatilis grown in University
    of Washington, Seatle, WA, United States
  principal_investigator:
    has_raw_value: Rebecca Neumann
  specific_ecosystem: Soil
  type: nmdc:Study

```
## Database-sample-prep
### Input
```yaml
dissolving_activity_set:
- dissolution_aided_by:
    activity_speed:
      has_numeric_value: 800
      has_unit: RPM
    activity_time:
      has_numeric_value: 2
      has_unit: hours
    device_type: orbital_shaker
  dissolution_reagent: deionized_water
  dissolution_volume:
    has_numeric_value: 30
    has_unit: mL
  dissolved_in:
    container_size:
      has_numeric_value: 50
      has_unit: mL
    container_type: screw_top_conical
  material_input: nmdc:matsm-b1fb4ff1-e59b-4e2b-a8f9-b95ea6ba4135
  material_output: nmdc:matsm-181a7a0a-4b04-4a22-9b89-db53e2ccdc99
material_sample_set:
- description: a soil biosample
  id: nmdc:matsm-99-PVhTGD
  name: monet_data:soil_1
- description: a 6 gram aliquot of monet_data:soil_1
  id: nmdc:matsm-99-m7PfV8
  name: nmdc:matsm-b1fb4ff1-e59b-4e2b-a8f9-b95ea6ba4135
- description: monet_data:somextract_6 dissolved in 30 mL of water
  id: nmdc:matsm-99-j670OL
  name: monet_data:somextract_7
- description: something at the beginning of a reaction
  id: nmdc:matsm-99-KyiIwv
  name: monet_data:derive_4
- description: something at the end of a reaction
  id: nmdc:matsm-99-KaZog6
  name: monet_data:derive_5
material_sampling_activity_set:
- amount_collected:
    has_numeric_value: 6
    has_unit: grams
  biosample_input: nmdc:matsm-bfc5b458-1c62-44e7-886a-dd3a2cc7ad67
  collected_into:
    container_size:
      has_numeric_value: 50
      has_unit: mL
    container_type: screw_top_conical
  material_output: nmdc:matsm-b1fb4ff1-e59b-4e2b-a8f9-b95ea6ba4135
  sampling_method: weighing
reaction_activity_set:
- material_input: nmdc:matsm-31380f3c-cea3-4f68-a8c6-cd84efa5e622
  material_output: nmdc:matsm-9fe9277b-454a-4257-a825-3b4725df665e
  reaction_aided_by:
    activity_temperature:
      has_numeric_value: 37
      has_unit: degrees Celsius
    activity_time:
      has_numeric_value: 1.5
      has_unit: hours
    device_type: thermomixer

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
- gold:Gs0110115

```
## OmicsProcessing-1
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- gold:Gp0108335
has_input:
- gold:Gb0108335
has_output:
- jgi:551a20d30d878525404e90d5
id: nmdc:omprc-99-zUCd5N
mod_date: 22-MAY-20 06.13.12.927000000 PM
name: Thawing permafrost microbial communities from the Arctic, studying carbon transformations
  - Permafrost 712P3D
ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
  carbon transformations - Permafrost 712P3D
omics_type:
  has_raw_value: Metagenome
part_of:
- gold:Gs0112340
processing_institution: JGI
type: nmdc:OmicsProcessing

```
## Biosample-exhasutive
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
- any_string
- seriously_anything
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
dna_absorb1: '2.02'
dna_absorb2: '2.02'
dna_collect_site: untreated pond water
dna_concentration: '100'
dna_cont_type: plate
dna_cont_well: C2
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
dna_volume: '25'
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
- any_string
- seriously_anything
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
- GOLD:Gb123456789
- GOLD:Gb90909090
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
  has_raw_value: '9606'
humidity_regm:
- has_raw_value: 25 gram per cubic meter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
id: nmdc:bsm-99-dtTMNb
igsn_biosample_identifiers:
- any:curie_1
- any:curie_2
img_identifiers:
- any string 1
- any string 2
insdc_biosample_identifiers:
- biosample:SAMN123456789
- biosample:SAMN000
isotope_exposure: 13C glucose
lat_lon:
  has_raw_value: 50.586825 6.408977
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
- ATP
other_treatment: unconstrained text
oxy_stat_samp: aerobe
part_of:
- nmdc:unconstrained_study_identifier_string1_needs_pattern_materialization_what_about_referential_integrity
- nmdc:unconstrained_study_identifier_string2
part_org_carb:
  has_raw_value: 1.92 micromole per liter
perturbation:
- has_raw_value: antibiotic addition;R2/2018-05-11T14:30Z/2018-05-11T19:30Z/P1H30M
petroleum_hydrocarb:
  has_raw_value: 0.05 micromole per liter
ph: 99.99
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
rna_absorb1: '2.02'
rna_absorb2: '2.02'
rna_collect_site: untreated pond water
rna_concentration: '100'
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
rna_volume: '25'
salinity:
  has_raw_value: 25 practical salinity unit
salinity_category: halotolerant is an example from the schema, but MIxS doesn't provide
  this slot any more
salinity_meth:
  has_raw_value: PMID:22895776
samp_collec_method:
  has_raw_value: swabbing
samp_mat_process:
  has_raw_value: filtering of seawater
samp_name:
  has_raw_value: see also name
samp_size:
  has_raw_value: 5 liters
samp_store_dur:
  has_raw_value: P1Y6M
samp_store_loc:
  has_raw_value: Freezer no:5
samp_store_temp:
  has_raw_value: -80 degree Celsius
samp_taxon_id:
  has_raw_value: soil metagenome [NCBItaxon:410658] but no validation applied yet
samp_vol_we_dna_ext:
  has_raw_value: 1500 milliliter
sample_collection_site: unconstrained text
sample_link:
- IGSN:DSJ0284
- any:curie
sample_shipped: 15 g
sample_type: water_extract_soil
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
tot_nitro_cont_meth:
  has_raw_value: https://currentprotocols.onlinelibrary.wiley.com/doi/abs/10.1002/0471142913.fab0102s00
tot_nitro_content:
  has_raw_value: 35 milligrams Nitrogen per kilogram of soil
tot_org_c_meth:
  has_raw_value: https://www.epa.gov/sites/production/files/2015-12/documents/9060a.pdf
tot_org_carb:
  has_raw_value: 2%
tot_phosp:
  has_raw_value: 0.03 milligram per liter
type: nmdc:Biosample. change this to require a class name or an enumeration
water_cont_soil_meth:
  has_raw_value: MIxS doesn't provide an example
water_content:
- MIxS doesn't provide an example 1
- MIxS doesn't provide an example 2
watering_regm:
- has_raw_value: 1 liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
zinc:
  has_raw_value: 2.5 mg/kg

```
## Study-minimal
### Input
```yaml
id: nmdc:sty-11-ab

```
## Study-exhaustive
### Input
```yaml
abstract: Nothing was studied.
alternative_descriptions:
- any string 1
- any string 2
alternative_identifiers:
- any string A1
- any string A2
alternative_names:
- any string 1
- any string 2
alternative_titles:
- any string 1
- any string 2
description: see also name, title, objective, various alternatives
doi:
  has_raw_value: https://doi.org/10.1126/science.1058040
ecosystem: unconstrained text. should be validated against the controlled vocabulary,
  by the sample's environmental package. would also be nice to align the CV with MIxS
  environmental triads
ecosystem_category: unconstrained text
ecosystem_subtype: unconstrained text
ecosystem_type: unconstrained text
emsl_proposal_doi: any string
emsl_proposal_identifier: any string EP1
ess_dive_datasets:
- any string 1
- any string 2
funding_sources:
- any string 1
- any string 2
gold_study_identifiers:
- GOLD:Gs12345
- GOLD:Gs90909
has_credit_associations:
- applied_role: Funding acquisition
  applied_roles:
  - Supervision
  - Conceptualization
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
mgnify_project_identifiers: mgnify.proj:ABC123
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
study_image:
- description: Photo of Craig Venter Institute, Rockville, Maryland
  display_order: '1'
  has_raw_value: https://upload.wikimedia.org/wikipedia/commons/8/86/J._Craig_Vernter_Institute_Rockville_Maryland.jpg
  url: https://upload.wikimedia.org/wikipedia/commons/8/86/J._Craig_Vernter_Institute_Rockville_Maryland.jpg
  was_generated_by: nmdc:any_string_1
- description: Photo of Craig Venter Institute, La Jolla, California
  display_order: '2'
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
## DataObject-1
### Input
```yaml
description: Metagenome Contig Coverage Stats for gold:Gp0061273
file_size_bytes: 32787380
id: nmdc:dobj-99-izwYW6
name: mapping_stats.txt
type: nmdc:DataObject

```
## Database-with-MetagenomeSequencingActivity
### Input
```yaml
metagenome_sequencing_activity_set:
- ended_at_time: '2021-09-15T10:13:20+00:00'
  execution_resource: JGI
  git_url: ''
  has_input:
  - nmdc:unvalidated_placeholder
  has_output:
  - nmdc:22afa3d49b73eaec2e9787a6b88fbdc3
  id: nmdc:wf-99-qwertyuiop
  name: Sequencing Activity for nmdc:mga0vx38
  part_of:
  - nmdc:mga0vx38
  started_at_time: '2021-08-05T14:48:51+00:00'
  type: nmdc:MetagenomeSequencing
  version: v1.0.0
  was_informed_by: gold:Gp0213371

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
  - GOLD:Gb0305833
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
  - GOLD:Gb0291692
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
  - GOLD:Gb0291582
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
  - GOLD:Gb0305834
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
  - GOLD:Gb0291693
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
  - GOLD:Gb0291583
  id: nmdc:bsm-99-tN5lxM
  name: Bulk soil microbial communities from poplar common garden site in Clatskanie,
    Oregon, USA - BESC-13-CL2_39_29
  part_of:
  - nmdc:sty-99-U21mUX
collecting_biosamples_from_site_set:
- has_inputs:
  - nmdc:frsite-99-SPreao
  has_outputs:
  - nmdc:bsm-99-J9FcnC
  - nmdc:bsm-99-BdlWdQ
  - nmdc:bsm-99-vn74Wq
  id: nmdc:clsite-99-Cq00d1
  name: Collection of biosamples from BESC-13-CL1_35_33
- has_inputs:
  - nmdc:frsite-99-h2mYFG
  has_outputs:
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
git_url: ''
has_input:
- nmdc:unvalidated_placeholder
has_output:
- nmdc:22afa3d49b73eaec2e9787a6b88fbdc3
id: nmdc:wf-99-qwertyuiop
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
## DataObject-exhaustive
### Input
```yaml
alternative_identifiers:
- prefix:value1
- prefix:value2
compression_type: any string
data_object_type: Crisprt Terms
description: Crisprt Terms for nmdc:ann0vx38
file_size_bytes: 1234
id: nmdc:dobj-11-dtTMNb
md5_checksum: 22afa3d49b73eaec2e9787a6b88fbdc3
name: Crisprt Terms
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
- gold:Gs0110115

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
  - GOLD:Gb0101224
  habitat: Coalbed water
  id: nmdc:bsm-99-dtTMNb
  lat_lon:
    has_raw_value: -33.460524 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients (early)
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - gold:Gs0110115
  samp_taxon_id:
    has_raw_value: coal metagenome [NCBITaxon:1260732]
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
  - GOLD:Gb0101224
  habitat: Coalbed water
  id: nmdc:bsm-99-AtTUOs
  lat_lon:
    has_raw_value: -33.460524 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients (early)
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - gold:Gs0110115
  samp_taxon_id:
    has_raw_value: coal metagenome [NCBITaxon:1260732]
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
  - GOLD:Gb0101225
  habitat: Coalbed water
  id: nmdc:bsm-99-eBVHjN
  lat_lon:
    has_raw_value: -33.460524 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients Extra
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - gold:Gs0110115
  samp_taxon_id:
    has_raw_value: coal metagenome [NCBITaxon:1260732]
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
  - GOLD:Gb0101226
  habitat: Coalbed water
  id: nmdc:bsm-99-TDPHTh
  lat_lon:
    has_raw_value: -33.460524 150.168149
  location: from the Lithgow State Coal Mine, New South Wales, Australia
  mod_date: 26-AUG-16 01.50.27.000000000 PM
  name: Lithgow State Coal Mine Calcium nutrients
  ncbi_taxonomy_name: coal metagenome
  part_of:
  - gold:Gs0110115
  samp_taxon_id:
    has_raw_value: coal metagenome [NCBITaxon:1260732]
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample

```
## DataObject-minimal
### Input
```yaml
description: Crisprt Terms for nmdc:ann0vx38
id: nmdc:dobj-11-dtTMNb
name: Crisprt Terms

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
- gold:Gs0110115

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
- gold:Gs0110115

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
## FunctionalAnnotation-exhaustive
### Input
```yaml
has_function: KEGG_PATHWAY:abc12345
subject: nmdc:gene_product_1
was_generated_by: nmdc:activity_1

```
## Database-omics-processings
### Input
```yaml
omics_processing_set:
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108335
  has_input:
  - gold:Gb0108335
  has_output:
  - jgi:551a20d30d878525404e90d5
  id: nmdc:omprc-99-zUCd5N
  mod_date: 22-MAY-20 06.13.12.927000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 712P3D
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712P3D
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - gold:Gs0112340
  processing_institution: JGI
  type: nmdc:OmicsProcessing
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108340
  has_input:
  - gold:Gb0108340
  has_output:
  - jgi:551a20d50d878525404e90d7
  id: nmdc:omprc-99-gKlQlF
  mod_date: 22-MAY-20 06.10.59.590000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 612S3M
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 612S3M
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - gold:Gs0112340
  processing_institution: JGI
  type: nmdc:OmicsProcessing
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108341
  has_input:
  - gold:Gb0108341
  has_output:
  - jgi:551a20d90d878525404e90e1
  id: nmdc:omprc-99-5kgIJR
  mod_date: 22-MAY-20 06.09.46.171000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 712S3S
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712S3S
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - gold:Gs0112340
  processing_institution: JGI
  type: nmdc:OmicsProcessing

```
## Database-invalid-omics-processing
### Input
```yaml
omics_processing_set:
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108335
  has_input:
  - gold:Gb0108335
  has_output:
  - jgi:551a20d30d878525404e90d5
  id: nmdc:omprc-99-zUCd5N
  mod_date: 22-MAY-20 06.13.12.927000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 712P3D
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712P3D
  omics_type:
    has_awesome_value: Metagenome
  part_of:
  - gold:Gs0112340
  processing_institution: JGI
  type: nmdc:OmicsProcessing
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108340
  has_input:
  - gold:Gb0108340
  has_output:
  - jgi:551a20d50d878525404e90d7
  id: nmdc:omprc-99-gKlQlF
  mod_date: 22-MAY-20 06.10.59.590000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 612S3M
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 612S3M
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - gold:Gs0112340
  processing_institution: JGI
  type: nmdc:OmicsProcessing
- add_date: 30-OCT-14 12.00.00.000000000 AM
  alternative_identifiers:
  - gold:Gp0108341
  has_input:
  - gold:Gb0108341
  has_output:
  - jgi:551a20d90d878525404e90e1
  id: nmdc:omprc-99-5kgIJR
  mod_date: 22-MAY-20 06.09.46.171000000 PM
  name: Thawing permafrost microbial communities from the Arctic, studying carbon
    transformations - Permafrost 712S3S
  ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
    carbon transformations - Permafrost 712S3S
  omics_type:
    has_raw_value: Metagenome
  part_of:
  - gold:Gs0112340
  processing_institution: JGI
  type: nmdc:OmicsProcessing

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
- gold:Gs0110115

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
  id: gold:Gs0110115
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
  id: gold:Gs0112340
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
- applied_role: Value Not In Enum 1
  applies_to_person:
    orcid: orcid:0000-0002-1825-00
  type: credit association
- applied_role: ValueNotInEnum2
  applies_to_person:
    orcid: orcid:0000-0001-9076-6066
  type: credit association
id: example:123

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
  - gold:Gs0128849
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
  - gold:Gs0128849
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
  - gold:Gs0128849
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
- gold:Gs0110115

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
- gold:Gs0110115

```
## FunctionalAnnotation-invalid-function
### Input
```yaml
has_function: KEGG_PATHWAY:XOXOXOXO

```
## OmicsProcessing-invalid-omics-type
### Input
```yaml
add_date: 30-OCT-14 12.00.00.000000000 AM
alternative_identifiers:
- gold:Gp0108335
has_input:
- gold:Gb0108335
has_output:
- jgi:551a20d30d878525404e90d5
id: nmdc:omprc-99-zUCd5N
mod_date: 22-MAY-20 06.13.12.927000000 PM
name: Thawing permafrost microbial communities from the Arctic, studying carbon transformations
  - Permafrost 712P3D
ncbi_project_name: Thawing permafrost microbial communities from the Arctic, studying
  carbon transformations - Permafrost 712P3D
omics_type:
  has_awesome_value: Metagenome
part_of:
- gold:Gs0112340
processing_institution: JGI
type: nmdc:OmicsProcessing

```
## DataObject-no-id-or-name
### Input
```yaml
description: Crisprt Terms for nmdc:ann0vx38

```
## MetagenomeSequencingActivity-no_parthood
### Input
```yaml
ended_at_time: '2021-09-15T10:13:20+00:00'
execution_resource: JGI
git_url: ''
has_input:
- nmdc:unvalidated_placeholder
has_output:
- nmdc:22afa3d49b73eaec2e9787a6b88fbdc3
id: nmdc:wf-99-qwertyuiop
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
  - gold:Gs0128849
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
  - gold:Gs0128849
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
  - gold:Gs0128849
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample

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
  - gold:Gs0128849
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
  - gold:Gs0128849
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
  - gold:Gs0128849
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample

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
- gold:Gs0110115
sample_collection_site: Lithgow State Coal Mine
specific_ecosystem: Coalbed water
type: nmdc:Biosample

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
- gold:Gs0110115

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
## MetagenomeSequencingActivity-bad_id
### Input
```yaml
ended_at_time: '2021-09-15T10:13:20+00:00'
execution_resource: JGI
git_url: ''
has_input:
- nmdc:unvalidated_placeholder
has_output:
- nmdc:22afa3d49b73eaec2e9787a6b88fbdc3
id: nmdc:107ade35423143e39dc30b12832ac759
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
  - gold:Gs0128849
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
  - gold:Gs0128849
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
  - gold:Gs0128849
  sample_collection_site: Lithgow State Coal Mine
  specific_ecosystem: Coalbed water
  type: nmdc:Biosample

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
description: Crisprt Terms for nmdc:ann0vx38
file_size_bytes: 1234
id: nmdc:dobj-11-dtTMNb
md5_checksum: 22afa3d49b73eaec2e9787a6b88fbdc3
name: Crisprt Terms
type: nmdc:DataObject
url: http://example.com
was_generated_by: nmdc:invalid_id

```
