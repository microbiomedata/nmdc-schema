RUN=poetry run

# local/.env.decoy contents:
#SOURCE_MONGO_USER=
#SOURCE_MONGO_PASS=

local/pymongo_as_unvalidated_nmdc_database.yaml:
	date
	time $(RUN) pure-export \
		--max-docs-per-coll 200000 \
		--schema-source src/schema/nmdc.yaml \
		--selected-collections fake_set \
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

local/api_as_unvalidated_nmdc_database.yaml:
	date
	time $(RUN) pure-export \
		--max-docs-per-coll 200000 \
		--schema-source src/schema/nmdc.yaml \
		--selected-collections fake_set \
		--selected-collections study_set \
		--output-yaml $@ \
		api-access \
		--page-size 20
