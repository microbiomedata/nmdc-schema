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

In order to run the following command, contact Mark, Eric or Sujay to get the password, 
specifically the for the `biosample_guest` user on database `ncbi_biosamples_feb26`  at `biosample-postgres-loadbalancer.mam.production.svc.spin.nersc.org`

Then you will need add the password into `src/scripts/ncbi_nmdc_exact_term_matching.py`. 
Please don't commit that file once you have edited the password! We are working parametrizing the password out, 
either though a command line option  or a .env file.

To execute the above strategy, run the following command:

```bash
poetry run python src/scripts/ncbi_nmdc_exact_term_matching.py
```

See the output at: *assets/ncbi_mappings/ncbi_pg_db_field_mappings_filled.tsv*