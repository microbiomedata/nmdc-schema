These mapping files are based on documentable paths from strings in NEON tables or API results and terms from the
Environment Ontology. No subject-matter knowledge was used. Refinement based on subject-matter knowledge is very
welcome, but must be expressable as a path from a NEON string, possibly through other resources (including natural
language and term embedding algorithms) to EnvO terms.

The `env_local_term` mappings in neon-nlcd-local-broad-mappings.tsv are most direct, but could be accused of making too
much use of **shadow classes**.

The `env_braod_scale` and `env_medium` mappings are specific if possible, but otherwise default to the root terms of 
"biome" or "terrestrial biome" and "soil" respectively.

See also:

- nmdc_schema/neon-nlcd-envo-mapping.py
- nmdc_schema/neon-soil-order-envo-mapping.py

**shadow classes**: Many ontologists, including this author, are concerned about the proliferation of shadow classes in
many important biomedical and environmental ontologies.
See [Shadow Concepts Considered Harmful](https://douroucouli.wordpress.com/2022/08/10/shadow-concepts-considered-harmful/).
Nonetheless, "area" and "zone" terms from the Environment Ontology have been used as the `env_local_scale`s as they came
from almost entirely deterministic mappings, with only minor programmatic string tidying and the use of
a [MRLC metadata file](https://www.mrlc.gov/data?f%5B0%5D=category%3ALand%20Cover&f%5B1%5D=region%3Aconus)
as a helper.

----

_Mark Andrew Miller_

_2023-06-11_