"""Keep related chemical names in ChemicalEntityEnum from being recorded as synonyms.

Some ``ChemicalEntityEnum`` values name an acid or a salt that the literature
usually calls by its ion, for example ``acetic_acid`` for "acetate". The ion is
a different ChEBI entry, so it is recorded twice: as a ``related_mappings``
CURIE, and as a ``structured_aliases`` entry with predicate
``RELATED_SYNONYM`` whose ``source`` is that ChEBI entry's page. A plain
``aliases`` entry would not do, because CONTRIBUTING.md reserves ``aliases``
for equivalent values.
"""

from linkml_runtime import SchemaView

from tests import ROOT

CORE_SCHEMA = ROOT / "src" / "schema" / "core.yaml"
CHEBI_PAGE = "https://www.ebi.ac.uk/chebi/"


def test_related_chebi_mappings_have_related_structured_aliases():
    """Each related ChEBI mapping has a RELATED_SYNONYM alias sourced to it, and no plain alias repeats that name."""
    enum = SchemaView(str(CORE_SCHEMA)).get_enum("ChemicalEntityEnum", strict=True)
    failures = []
    for name, pv in enum.permissible_values.items():
        related = [str(curie) for curie in pv.related_mappings or [] if str(curie).startswith("CHEBI:")]
        if not related:
            continue
        structured = [a for a in pv.structured_aliases or [] if str(a.predicate) == "RELATED_SYNONYM"]
        sources = {str(a.source) for a in structured}
        for curie in related:
            if CHEBI_PAGE + curie not in sources:
                failures.append(f"{name}: no RELATED_SYNONYM structured alias with source {CHEBI_PAGE + curie}")
        related_names = {a.literal_form for a in structured}
        for alias in pv.aliases or []:
            if alias in related_names or not structured:
                failures.append(f"{name}: plain alias {alias!r} names a related, non-equivalent chemical")
    assert not failures, "\n".join(failures)
