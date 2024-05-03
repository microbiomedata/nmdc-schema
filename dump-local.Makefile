RUN=poetry run

local/mongo_as_unvalidated_nmdc_database.yaml:
	date  # 276.50 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) pure-export \
		--admin-db "" \
		--auth-mechanism "" \
		--env-file local/.env.decoy \
		--max-docs-per-coll 200000 \
		--mongo-db-name for-local-pure-export \
		--mongo-host localhost \
		--mongo-port 27017 \
		--no-direct-connection \
		--output-yaml $@ \
		--page-size 200000 \
		--schema-file src/schema/nmdc.yaml \
		--selected-collections study_set \
