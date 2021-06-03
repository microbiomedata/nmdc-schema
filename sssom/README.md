# SSSOM Mappings

This directory holds [SSSOM](https://github.com/mapping-commons/SSSOM) files used to define mappings.

### Some recently added files are per-sample mappings and not actually in the SSSOM format.

_Might require moving to a better location._

- `biosample_env_package_normalizastion.tsv`
  - Counts all of the `env_package` values submitted to NCBI Biosample Metadata and provides mappings to `EnvPackage` from https://www.ncbi.nlm.nih.gov/biosample/docs/packages/?format=xml where possible. Lot of overlap with `env_package.pattern` from `mixs.yaml`, but not identical. `EnvPackageDisplay` may actually provide better overlap.
  - 14,083,847 out of 14,300,584 biosamples have no `env_package` annotation.
  - Roughly 50k biosamples each are annotated with `host-associated` and `human-gut`. Are those of interest to NMDC?
  - 16,367 samples are annotated with `water`
  - _TODO: what's the correlation of `water` annotated biosamples with biosamples whose `taxonomy_id` indicates an unidentified/environmental/metagenome sample?_
- `per_biosample_scoped_ebs_mapping_results.tsv`
  - This file accounts for the fact that biosamples can be annotated with a pipe-delimited list of terms in MIxS triad columns like `env_broad_scale`. See https://www.ncbi.nlm.nih.gov/biosample/?term=SAMN13905271
  - Otherwise, it is just a merger of `biosample_ebs_water_packages_unclassified_taxa_sssom.tsv` with the NCBI Biosample metadata
  - Based on recent discussions with Chris M, the mapped IDs and labels have not been re-assembled into the `label [ID]` format yet
  - Therefore `BIOSAMPLE:SAMN13905271`, which officially has an `env_broad_scale` annotation of 'Marine Biome [ENVO:00000447]|Archipelago [ENVO:00000220]' is assigned the IDs `ENVO:00000447|ENVO:00000220` and the labels `marine biome|archipelago`

