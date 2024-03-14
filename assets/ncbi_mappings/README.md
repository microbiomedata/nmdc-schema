# NMDC schema slots/NCBI Postgres database field mapping strategy

### Pre-requisites

SSH tunnel to loadbalancer on SPIN where the PostgresQL dump of the NCBI BioSample database has been deployed. To build this PostgresQL version locally follow the setup instructions in: https://github.com/turbomam/biosample-xmldb-sqldb/tree/main

```bash
ssh -i ~/.ssh/nersc -L 15432:biosample-postgres-loadbalancer.mam.production.svc.spin.nersc.org:5432 spatil@dtn01.nersc.gov
```

The first strategy used to fill in the mappings is exact term matching.

1. Exact term matching
 * Matching between the NMDC slot name and the field/column name from the NCBI Postgre view called "attributes_plus"
 * Matching between the NMDC slot name and the display name (text between <Name></Name> within each <Attribute></Attribute>) and synonyms (text between <Synonym></Synonym> within each <Attribute></Attribute>)

To execute the above strategy, run the following command:

```bash
poetry run python assets/ncbi_mappings/exact_term_matching.py
```

See the output at: *assets/ncbi_mappings/exact_term_matching.py*