# Database examples -> validated Mermaid -> SVG. Hand-authored schema diagrams
# share the same renderer but are not generated from Database instances.
DATABASE_DIAGRAM_SCRIPT := src/scripts/database_to_diagram.py
PUPPETEER_CFG := src/docs/images/puppeteer-config.json
MERMAID_CONFIG := src/docs/images/mermaid-config.json
# Pin the renderer so a routine regeneration does not silently switch versions.
MERMAID_CLI ?= npx --yes @mermaid-js/mermaid-cli@11.17.0

DIAGRAM_MMD := $(wildcard src/docs/images/*.mmd)
DIAGRAM_SVG := $(DIAGRAM_MMD:.mmd=.svg)
EXAMPLE_DIAGRAM_NAMES := sip-lifecycle use-case-1-environmental-isolation \
    use-case-2-culture-collection use-case-3-leaf-clip use-case-4-mushroom-cap \
    use-case-5-viral-isolate-with-host
EXAMPLE_DIAGRAM_MMD := $(addprefix src/docs/images/,$(addsuffix .mmd,$(EXAMPLE_DIAGRAM_NAMES)))

.PHONY: diagrams example-diagrams sip-diagram database-diagram FORCE_DATABASE_DIAGRAM
diagrams: $(DIAGRAM_SVG)
example-diagrams: $(EXAMPLE_DIAGRAM_MMD:.mmd=.svg)
sip-diagram: src/docs/images/sip-lifecycle.svg

src/docs/images/sip-lifecycle.mmd: src/data/valid/Database-sip-lifecycle.yaml
	$(RUN) python $(DATABASE_DIAGRAM_SCRIPT) $< $@ --view workflow \
	    --label-slot gradient_position --label-slot gradient_pos_density \
	    --label-slot gradient_pos_rel_am --label-slot manifest_category \
	    --label-slot isotopolog_additions.isotope \
	    --label-slot isotopolog_additions.isotopolog_label

src/docs/images/use-case-1-environmental-isolation.mmd: src/data/valid/Database-isolate-from-soil-workflow.yaml
	$(RUN) python $(DATABASE_DIAGRAM_SCRIPT) $< $@ --view workflow --direction LR --allow-external

src/docs/images/use-case-2-culture-collection.mmd: src/data/valid/Database-isolate-from-culture-collection.yaml
	$(RUN) python $(DATABASE_DIAGRAM_SCRIPT) $< $@ --view workflow --direction LR --allow-external

src/docs/images/use-case-3-leaf-clip.mmd: src/data/valid/Database-leaf-clip.yaml
	$(RUN) python $(DATABASE_DIAGRAM_SCRIPT) $< $@ --view workflow --direction LR --allow-external

src/docs/images/use-case-4-mushroom-cap.mmd: src/data/valid/Database-mushroom-cap.yaml
	$(RUN) python $(DATABASE_DIAGRAM_SCRIPT) $< $@ --view workflow --direction LR --allow-external

src/docs/images/use-case-5-viral-isolate-with-host.mmd: src/data/valid/Database-viral-isolate-with-host.yaml
	$(RUN) python $(DATABASE_DIAGRAM_SCRIPT) $< $@ --view workflow --direction LR --allow-external \
	    --label-slot host_genus --label-slot host_species --label-slot host_strain

# Recheck the source schema on each invocation, without making mixs.yaml a Make
# dependency (that would invoke its network-dependent regeneration pipeline).
# The generator preserves mtime when the Mermaid content is unchanged.
FORCE_DATABASE_DIAGRAM:
$(EXAMPLE_DIAGRAM_MMD): $(DATABASE_DIAGRAM_SCRIPT) makefiles/diagrams.Makefile FORCE_DATABASE_DIAGRAM

src/docs/images/%.svg: src/docs/images/%.mmd $(PUPPETEER_CFG) $(MERMAID_CONFIG) makefiles/diagrams.Makefile
	$(MERMAID_CLI) -i $< -o $@ -b transparent -p $(PUPPETEER_CFG) -c $(MERMAID_CONFIG)

# One-off examples use the same validator, generator and renderer.
DATABASE ?= src/data/valid/Database-sip-lifecycle.yaml
DIAGRAM_OUTPUT ?= local/$(basename $(notdir $(DATABASE)))
DIAGRAM_OPTIONS ?=
database-diagram:
	$(RUN) python $(DATABASE_DIAGRAM_SCRIPT) "$(DATABASE)" "$(DIAGRAM_OUTPUT).mmd" $(DIAGRAM_OPTIONS)
	$(MERMAID_CLI) -i "$(DIAGRAM_OUTPUT).mmd" -o "$(DIAGRAM_OUTPUT).svg" -b transparent -p $(PUPPETEER_CFG) -c $(MERMAID_CONFIG)
