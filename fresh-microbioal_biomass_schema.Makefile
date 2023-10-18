RUN=poetry run

.PHONY: check_fresh_microbioal_biomass_schema-microbioal_biomass_schema \
validate_fresh_microbioal_biomass_data

#check_fresh_microbioal_biomass_schema: src/schema/fresh_microbioal_biomass_schema.yaml
#	$(RUN) gen-linkml --format yaml $<

validate_fresh_microbioal_biomass_data: src/schema/nmdc.yaml
	$(RUN) linkml-validate \
		--target-class WeighingProcess \
		--schema $< src/data/valid/WeighingProcess-valid.yaml
	$(RUN) linkml-validate \
		--target-class DissolutionProcess \
		--schema $< src/data/valid/DissolutionProcess-valid.yaml
#	$(RUN) linkml-validate \
#		--target-class Database \
#		--schema $< src/data/valid/Database-sample-prep-protocol-execution.yaml
	$(RUN) linkml-validate \
		--target-class ProtocolExecution \
		--schema $< src/data/valid/Database-sample-prep-protocol-execution.yaml
