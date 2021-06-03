# SSSOM Mappings
This directory holds [SSSOM](https://github.com/mapping-commons/SSSOM) files used to define mappings.

Some recently added files are per-sample mappings and not actually in the SSSOM format. Might require moving to a better location.
- per_biosample_scoped_ebs_mapping_results.tsv
    - This file accounts for the fact that biosamples can be annotated with a pipe-delimited list of terms in MIxS triad columns like `env_broad_scale`. See https://www.ncbi.nlm.nih.gov/biosample/?term=SAMN13905271
    - Based on recent discussions with Chris M, the mapped IDs and labels have not been re-assembled into the `label [ID]` format yet
    - Therefore `BIOSAMPLE:SAMN13905271`, which officially has an `env_broad_scale` annotation of 'Marine Biome [ENVO:00000447]|Archipelago [ENVO:00000220]' is assigned the IDs `ENVO:00000447|ENVO:00000220` and the labels `marine biome|archipelago`
