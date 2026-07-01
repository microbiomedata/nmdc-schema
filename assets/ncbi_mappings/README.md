# NMDC schema slots/NCBI Attributes mapping strategy

To generate the filled mapping TSV, run:

```bash
make assets/ncbi_mappings/ncbi_attribute_mappings_filled.tsv
```

The strategy used to fill in the mappings is exact term matching.

Exact term matching
* Matching between the NMDC slot name and one of the names associated with a BioSample Attribute
  * harmonized name: text between <HarmonizedName></HarmonizedName> within each <Attribute></Attribute>
  * display name/attribute name: text between <Name></Name> within each <Attribute></Attribute>
  * synonym: text between <Synonym></Synonym> within each <Attribute></Attribute>
* Ignore mapping for certain slots coming from irrelevant imported schemas 
by marking them as `IGNORE`
* Programatically identify the slots that need manual curation in a package-specific manner, 
and either find the appropriate NCBI Attribute it can be marked to, or simply mark it as `IGNORE`

To execute the above strategy, run the following command:

```bash
make assets/ncbi_mappings/ncbi_attribute_mappings_filled.tsv
```

See the output at: *ncbi_attribute_mappings_filled.tsv*