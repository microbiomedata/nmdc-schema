RUN=poetry run

# local/.env.decoy contents:
#SOURCE_MONGO_USER=
#SOURCE_MONGO_PASS=

local/mongo_as_unvalidated_nmdc_database.yaml:
	date  # 276.50 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) dump-single-modality \
		--max-docs-per-coll 200000 \
		--schema-source src/schema/nmdc.yaml \
		--selected-collections study_set \
		--output-yaml $@ \
		pymongo-access  \
		--admin-db "" \
		--auth-mechanism "" \
		--env-file local/.env.decoy \
		--mongo-db-name for-local-pure-export \
		--mongo-host localhost \
		--mongo-port 27017 \
		--no-direct-connection

local/mongo_as_unvalidated_nmdc_database_from_api.yaml:
	date  # 276.50 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) dump-single-modality \
		--max-docs-per-coll 200000 \
		--schema-source src/schema/nmdc.yaml \
		--selected-collections study_set \
		--output-yaml $@ \
		api-access