"""Require slot mappings to point at properties, not ontology classes.

CLAUDE.md ("Type compatibility") says a slot maps to a property, not a
class. This reads the src/schema/*.yaml source files and checks every
``*_mappings`` value on a slot, a class attribute, or a slot_usage entry.

The test doesn't use the network. ONTOLOGY_TERM_KINDS records what OLS4
returned for each ontology term used in a slot mapping. When a new term
is added, look it up and add it, for example:

    curl -s "https://www.ebi.ac.uk/ols4/api/properties?iri=<IRI>" | jq .page.totalElements
    curl -s "https://www.ebi.ac.uk/ols4/api/terms?iri=<IRI>" | jq .page.totalElements

A term found under properties is "property"; one found under terms is
"class". See https://github.com/microbiomedata/nmdc-schema/issues/3522
"""

from collections.abc import Iterator
from pathlib import Path

import yaml

MAPPING_KEYS = (
    "mappings",
    "exact_mappings",
    "close_mappings",
    "broad_mappings",
    "narrow_mappings",
    "related_mappings",
)

# Prefixes that aren't ontologies in OLS4, so this test doesn't check them.
# A prefix missing from here is treated as an ontology and checked.
NOT_CHECKED_PREFIXES = {
    "biolink",
    "dcm",
    "dcterms",
    "MIXS",
    "nmdc",
    "prov",
    "qudt",
    "schema",
    "skos",
}

# What OLS4 returned for each term, checked 2026-10-16 with the
# /api/terms and /api/properties endpoints.
ONTOLOGY_TERM_KINDS = {
    "edam.data:1188": "class",
    "GENEPIO:0000093": "class",
    "GENEPIO:0001450": "class",
    "GENEPIO:0100596": "class",
    "MS:1000004": "class",
    "MS:1000008": "class",
    "MS:1000443": "class",
    "MS:1003213": "class",
    "NCIT:C165211": "class",
    "NCIT:C177560": "class",
    "NCIT:C39409": "class",
    "NCIT:C74932": "class",
    "OBI:0002110": "class",
    "OBI:0002475": "class",
    "OMIT:0013243": "class",
    "OMIT:0013245": "class",
    "OMIT:0013248": "class",
    "OMIT:0013250": "class",
    "PATO:0000125": "class",
    "SIO:000337": "class",
    "TAXRANK:0000001": "class",
    "TAXRANK:0000002": "class",
    "TAXRANK:0000003": "class",
    "TAXRANK:0000004": "class",
    "TAXRANK:0000005": "class",
    "TAXRANK:0000006": "class",
    "TAXRANK:0000022": "class",
}

# (slot, term) pairs that map a slot to a class today. Don't add to this set.
# https://github.com/microbiomedata/nmdc-schema/issues/3250 fixes them.
GRANDFATHERED = {
    ("doi_provider", "NCIT:C74932"),
    ("doi_value", "edam.data:1188"),
    ("doi_value", "OBI:0002110"),
    ("extraction_targets", "NCIT:C177560"),
    ("funding_sources", "NCIT:C39409"),
    ("gtdbtk_class", "TAXRANK:0000002"),
    ("gtdbtk_domain", "TAXRANK:0000022"),
    ("gtdbtk_family", "TAXRANK:0000004"),
    ("gtdbtk_genus", "TAXRANK:0000005"),
    ("gtdbtk_order", "TAXRANK:0000003"),
    ("gtdbtk_phylum", "TAXRANK:0000001"),
    ("gtdbtk_species", "TAXRANK:0000006"),
    ("input_mass", "MS:1000004"),
    ("ionization_source", "MS:1000008"),
    ("library_preparation_kit", "GENEPIO:0001450"),
    ("mass", "PATO:0000125"),
    ("mass_analyzers", "MS:1000443"),
    ("mass_spectrometry_acquisition_strategy", "MS:1003213"),
    ("members_id", "GENEPIO:0100596"),
    ("num_16s", "OMIT:0013243"),
    ("num_23s", "OMIT:0013245"),
    ("num_5s", "OMIT:0013248"),
    ("num_t_rna", "OMIT:0013250"),
    ("number_of_contig", "GENEPIO:0000093"),
    ("objective", "SIO:000337"),
    ("pcr_cycles", "OBI:0002475"),
    ("processing_institution_workflow_metadata", "NCIT:C165211"),
}


def slot_mappings(schema: dict) -> Iterator[tuple[str, str, str]]:
    """Yield (location, slot name, term) for every mapping on a slot."""
    for slot_name, slot in (schema.get("slots") or {}).items():
        for key in MAPPING_KEYS:
            for term in (slot or {}).get(key) or []:
                yield f"slots/{slot_name}/{key}", slot_name, term
    for class_name, class_definition in (schema.get("classes") or {}).items():
        for part in ("attributes", "slot_usage"):
            for slot_name, slot in ((class_definition or {}).get(part) or {}).items():
                for key in MAPPING_KEYS:
                    for term in (slot or {}).get(key) or []:
                        yield (
                            f"classes/{class_name}/{part}/{slot_name}/{key}",
                            slot_name,
                            term,
                        )


def test_slot_mappings_point_at_properties() -> None:
    repository_root = Path(__file__).resolve().parents[1]
    problems = []
    still_grandfathered = set()
    for schema_path in sorted((repository_root / "src" / "schema").glob("*.yaml")):
        with schema_path.open(encoding="utf-8") as source_file:
            schema = yaml.safe_load(source_file)
        for location, slot_name, term in slot_mappings(schema):
            if term.split(":", 1)[0] in NOT_CHECKED_PREFIXES:
                continue
            where = f"{schema_path.relative_to(repository_root)}/{location}: {term}"
            kind = ONTOLOGY_TERM_KINDS.get(term)
            if kind is None:
                problems.append(
                    f"{where} isn't in ONTOLOGY_TERM_KINDS; look it up in OLS4 and add it"
                )
            elif kind == "class":
                if (slot_name, term) in GRANDFATHERED:
                    still_grandfathered.add((slot_name, term))
                else:
                    problems.append(
                        f"{where} is an ontology class; map the slot to a property"
                    )

    assert not problems, (
        "A slot maps to a property, not a class (CLAUDE.md, 'Type compatibility').\n"
        + "\n".join(problems)
    )
    fixed = GRANDFATHERED - still_grandfathered
    assert not fixed, (
        "These slot-to-class mappings are fixed; remove them from GRANDFATHERED:\n"
        + "\n".join(f"{slot} {term}" for slot, term in sorted(fixed))
    )
