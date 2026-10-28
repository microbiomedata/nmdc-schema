"""Require slot mappings to ontology classes to use close or related mappings.

CLAUDE.md ("Type compatibility") says a slot maps to a property. When the
only matching term is a class, the slot may name it in close_mappings or
related_mappings, never in exact, broad, narrow or generic mappings. This
reads the src/schema/*.yaml source files and checks every ``*_mappings``
value on a slot, a class attribute, or a slot_usage entry.

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
    "NCBI_BIOSAMPLE_ATTRIBUTE",
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
    # GENEPIO terms used on slots in https://github.com/microbiomedata/nmdc-schema/pull/3533,
    # checked 2026-10-28.
    "GENEPIO:0000035": "class",
    "GENEPIO:0001123": "class",
    "GENEPIO:0001136": "class",
    "GENEPIO:0001139": "class",
    "GENEPIO:0001153": "class",
    "GENEPIO:0001174": "class",
    "GENEPIO:0001181": "class",
    "GENEPIO:0001185": "class",
    "GENEPIO:0001189": "class",
    "GENEPIO:0001191": "class",
    "GENEPIO:0001198": "class",
    "GENEPIO:0001223": "class",
    "GENEPIO:0001232": "class",
    "GENEPIO:0001234": "class",
    "GENEPIO:0001241": "class",
    "GENEPIO:0001253": "class",
    "GENEPIO:0001452": "class",
    "GENEPIO:0001736": "class",
    "GENEPIO:0100309": "class",
    "GENEPIO:0100310": "class",
    "GENEPIO:0100428": "class",
    "GENEPIO:0100436": "class",
    "GENEPIO:0100448": "class",
    "GENEPIO:0100760": "class",
    "GENEPIO:0100766": "class",
    "GENEPIO:0100767": "class",
    "GENEPIO:0100768": "class",
    "GENEPIO:0100769": "class",
    "GENEPIO:0100771": "class",
    "GENEPIO:0100773": "class",
    "GENEPIO:0100774": "class",
    "GENEPIO:0100775": "class",
    "GENEPIO:0100779": "class",
    "GENEPIO:0100780": "class",
    "GENEPIO:0100783": "class",
    "GENEPIO:0100784": "class",
    "GENEPIO:0100788": "class",
    "GENEPIO:0100789": "class",
    "GENEPIO:0100791": "class",
    "GENEPIO:0100792": "class",
    "GENEPIO:0100794": "class",
    "GENEPIO:0100795": "class",
    "GENEPIO:0100805": "class",
    "GENEPIO:0100806": "class",
    "GENEPIO:0100808": "class",
    "GENEPIO:0100809": "class",
    "GENEPIO:0100811": "class",
    "GENEPIO:0100812": "class",
    "GENEPIO:0100814": "class",
    "GENEPIO:0100815": "class",
    "GENEPIO:0100816": "class",
    "GENEPIO:0100817": "class",
    "GENEPIO:0100821": "class",
    "GENEPIO:0100822": "class",
    "GENEPIO:0100878": "class",
    "GENEPIO:0100879": "class",
    "GENEPIO:0100905": "class",
    "GENEPIO:0100906": "class",
    "GENEPIO:0100908": "class",
    "GENEPIO:0100909": "class",
    "GENEPIO:0100914": "class",
    "GENEPIO:0100921": "class",
    "GENEPIO:0100922": "class",
    "GENEPIO:0100935": "class",
    "GENEPIO:0100936": "class",
    "GENEPIO:0101014": "class",
    "GENEPIO:0101015": "class",
    "GENEPIO:0101203": "class",
    "GENEPIO:0101205": "class",
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

# A slot may name an ontology class only under these keys (CLAUDE.md,
# "LinkML Mapping Metaslots").
CLASS_MAPPING_KEYS = {"close_mappings", "related_mappings"}


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


def test_slot_class_mappings_use_close_or_related() -> None:
    repository_root = Path(__file__).resolve().parents[1]
    problems = []
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
            mapping_key = location.rsplit("/", 1)[1]
            if kind == "class" and mapping_key not in CLASS_MAPPING_KEYS:
                problems.append(
                    f"{where} is an ontology class; use close_mappings or related_mappings"
                )

    assert not problems, (
        "A slot maps to a class only with close_mappings or related_mappings"
        " (CLAUDE.md, 'LinkML Mapping Metaslots').\n" + "\n".join(problems)
    )
