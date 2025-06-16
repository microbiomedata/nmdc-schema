nmdc-schema.ols.owl.ttl: src/schema/nmdc.yaml
	date && time poetry run linkml generate owl \
		--add-ols-annotations \
		--default-permissible-value-type "http://www.w3.org/2002/07/owl#Class" \
		--enum-iri-separator "#" \
		--format owl \
		--log_level WARNING \
		--mergeimports \
		--metadata \
		--metadata-profile ols \
		--add-root-classes \
		--no-assert-equivalent-classes \
		--metaclasses \
		--no-mixins-as-expressions \
		--no-stacktrace \
		--no-type-objects \
		--ontology-uri-suffix .owl.ttl \
		--use-native-uris \
		--useuris $< > $@ && date

#Mon Jun  9 01:26:34 PM EDT 2025
#WARNING:linkml.generators.owlgen:ignoring equals_string=plate as unable to tell if literal
#WARNING:linkml.generators.owlgen:ignoring equals_string=plate as unable to tell if literal
#WARNING:linkml.generators.owlgen:ignoring equals_string=plate as unable to tell if literal
#WARNING:linkml.generators.owlgen:ignoring equals_string=plate as unable to tell if literal
#WARNING:linkml.generators.owlgen:ignoring equals_string=dataset_doi as unable to tell if literal
#WARNING:linkml.generators.owlgen:ignoring equals_string=award_doi as unable to tell if literal
#WARNING:linkml.generators.owlgen:ignoring equals_string=pass as unable to tell if literal
#WARNING:linkml.generators.owlgen:ignoring equals_string=gas_chromatography as unable to tell if literal
#WARNING:linkml.generators.owlgen:ignoring equals_string=liquid_chromatography as unable to tell if literal
#WARNING:linkml.generators.owlgen:ignoring equals_string=gas_chromatography as unable to tell if literal
#WARNING:linkml.generators.owlgen:ignoring equals_string=retention_index as unable to tell if literal
#8.86user 0.27system 0:07.43elapsed 122%CPU (0avgtext+0avgdata 204820maxresident)k
#46480inputs+2536outputs (5major+71342minor)pagefaults 0swaps
#Mon Jun  9 01:26:42 PM EDT 2025
