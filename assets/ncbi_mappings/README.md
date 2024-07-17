# NMDC schema slots/NCBI Postgres database field mapping strategy

### Pre-requisites

SSH tunnel to loadbalancer on SPIN where the PostgresQL dump of the NCBI BioSample database has been deployed. To build this PostgresQL version locally follow the setup instructions in: https://github.com/turbomam/biosample-xmldb-sqldb/tree/main

```bash
ssh -i ~/.ssh/nersc -L 15432:biosample-postgres-loadbalancer.mam.production.svc.spin.nersc.org:5432 <nersc-username>@dtn01.nersc.gov
```

The strategy used to fill in the mappings is exact term matching.

Exact term matching
* Matching between the NMDC slot name and the field/column name from the NCBI Postgre view called "attributes_plus"
* Matching between the NMDC slot name and the display name (text between <Name></Name> within each <Attribute></Attribute>) and synonyms (text between <Synonym></Synonym> within each <Attribute></Attribute>)

To execute the above strategy, run the following command:

```bash
poetry run python src/scripts/ncbi_postgres_nmdc_exact_term_matching.py
```

See the output at: *assets/ncbi_mappings/ncbi_pg_db_field_mappings_filled.tsv*

# NMDC schema slots/NCBI Attributes mapping strategy

The strategy used to fill in the mappings is exact term matching.

Exact term matching
* Matching between the NMDC slot name and one of the names associated with a BioSample Attribute
  * harmonized name: text between <HarmonizedName></HarmonizedName> within each <Attribute></Attribute>
  * display name/attribute name: text between <Name></Name> within each <Attribute></Attribute>
  * synonym: text between <Synonym></Synonym> within each <Attribute></Attribute>
* Ignore mapping for certain slots coming from irrelevant imported schemas 
by marking them as `IGNORE`
* Programatically identify the slots that need manual curation in a package-specific manner, 
and either find the appropriate NCBI Attribute it can be marked to, or simply mark it as `IGNORE`

To execute the above strategy, run the following command:

```bash
make assets/ncbi_mappings/ncbi_attribute_mappings_filled.tsv
```

See the output at: *ncbi_attribute_mappings_filled.tsv*