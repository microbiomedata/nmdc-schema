pre_schema.yaml:
	poetry run python -c 'from linkml_runtime.utils.schemaview import SchemaView; \
	from linkml_runtime.dumpers import yaml_dumper; \
	schema_url = "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/refs/tags/v10.9.1/src/schema/nmdc.yaml"; \
	sv = SchemaView(schema_url, merge_imports=True); \
	yaml_dumper.dump(sv.schema, "pre_schema.yaml")'

berkeley_schema.yaml:
	poetry run python -c 'from linkml_runtime.utils.schemaview import SchemaView; \
	from linkml_runtime.dumpers import yaml_dumper; \
	schema_url = "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/refs/tags/v11.0.1/src/schema/nmdc.yaml"; \
	sv = SchemaView(schema_url, merge_imports=True); \
	yaml_dumper.dump(sv.schema, "berkeley_schema.yaml")'

pre_study.yaml: pre_schema.yaml
	yq '.classes.Study' $< | cat > $@

pre_biosample.yaml: pre_schema.yaml
	yq '.classes.Biosample' $< | cat > $@

pre_types.yaml: pre_schema.yaml
	yq '.types' $< | cat > $@

pre_settings.yaml: pre_schema.yaml
	yq '.settings' $< | cat > $@

pre_prefixes.yaml: pre_schema.yaml
	yq '.prefixes' $< | cat > $@

pre_enums.yaml: pre_schema.yaml
	yq '.enums' $< | cat > $@

pre_subsets.yaml: pre_schema.yaml
	yq '.subsets' $< | cat > $@

berkeley_study.yaml: berkeley_schema.yaml
	yq '.classes.Study' $< | cat > $@

berkeley_biosample.yaml: berkeley_schema.yaml
	yq '.classes.Biosample' $< | cat > $@

berkeley_types.yaml: berkeley_schema.yaml
	yq '.types' $< | cat > $@

berkeley_settings.yaml: berkeley_schema.yaml
	yq '.settings' $< | cat > $@

berkeley_prefixes.yaml: berkeley_schema.yaml
	yq '.prefixes' $< | cat > $@

berkeley_enums.yaml: berkeley_schema.yaml
	yq '.enums' $< | cat > $@

berkeley_subsets.yaml: berkeley_schema.yaml
	yq '.subsets' $< | cat > $@

pre_vs_berkeley_study.yaml: pre_study.yaml berkeley_study.yaml
	poetry run deep diff --ignore-order $^ | yq -P | cat > $@

pre_vs_berkeley_biosample.yaml: pre_biosample.yaml berkeley_biosample.yaml
	poetry run deep diff --ignore-order $^ | yq -P | cat > $@

pre_vs_berkeley_types.yaml: pre_types.yaml berkeley_types.yaml
	poetry run deep diff --ignore-order $^ | yq -P | cat > $@

pre_vs_berkeley_settings.yaml: pre_settings.yaml berkeley_settings.yaml
	poetry run deep diff --ignore-order $^ | yq -P | cat > $@

pre_vs_berkeley_prefixes.yaml: pre_prefixes.yaml berkeley_prefixes.yaml
	poetry run deep diff --ignore-order $^ | yq -P | cat > $@

pre_vs_berkeley_enums.yaml: pre_enums.yaml berkeley_enums.yaml
	poetry run deep diff --ignore-order $^ | yq -P | cat > $@

pre_vs_berkeley_subsets.yaml: pre_subsets.yaml berkeley_subsets.yaml
	poetry run deep diff --ignore-order $^ | yq -P | cat > $@


