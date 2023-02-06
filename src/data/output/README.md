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
