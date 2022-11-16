# Identifiers in NMDC

Identifiers are crucial for the NMDC, both for any data objects *created* (aka minted) and for any external objects *referenced*

Examples of entities that require identifiers:

 * Samples
 * Data objects (e.g. sequence files)
 * Taxa (e.g. NCBITaxon or GTDB)
 * Genes, Proteins
 * Sequences (e.g. genome/transcriptome)
 * Ontology terms and other descriptors
     * functional orthologs, e.g. KEGG.orthology (KO) terms
     * pathways, e.g. KEGG.pathway, MetaCyc, GO
     * reactions/activities: KEGG, MetaCyc
     * chemical entities: CHEBI, CHEMBL, INCHI, ...
     * sequence feature types: SO, Rfam

Identifiers should be:

 * Permanent
 * Unique
 * Resolvable
 * Opaque

See [McMurry et al, PMID:28662064](https://www.ncbi.nlm.nih.gov/pubmed/28662064) for more desiderata.

## CURIEs - prefixed IDs

Following McMurry et al we adopt the use of *prefixed identifiers*

The syntax is:

    Prefix:LocalId

Examples:

 - GO:0008152
 - BIOSAMPLE:SAMEA2397676
 - DOI:10.1038/nbt1156

These prefixed identifiers are also known as CURIEs (Compact URIs). There is a [W3C specification](https://www.w3.org/TR/curie) for these

All prefixes should be registered with a standard identifier prefix system. These include:

 * http://n2t.net
 * http://identifiers.org
 * http://obofoundry.org

## Examples

### INSDC BioSamples

Registry entry: https://registry.identifiers.org/registry/biosample

Example ID/CURIE: BIOSAMPLE:SAMEA2397676

Resolving via identifiers.org: [https://identifiers.org/BIOSAMPLE:SAMEA2397676](https://identifiers.org/BIOSAMPLE:SAMEA2397676)

Resolving via nt2.net: [http://n2t.net/BIOSAMPLE:SAMEA2397676](http://n2t.net/BIOSAMPLE:SAMEA2397676)

### GOLD identifiers

https://registry.identifiers.org/registry/gold

Example ID: `GOLD:Gp0119849`

Resolving via identifiers.org: https://identifiers.org/GOLD:Gp0119849

### identifiers for ontology terms and function descriptors

Most of the ontologies we use are in OBO. All OBO IDs are prefixed
using the ontology ID space. The list of ID spaces can be found on
http://obofoundry.org

For example the ID/CURIE `ENVO:00002007` represents the class `sediment` and is expanded to a URI of http://purl.obolibrary.org/obo/ENVO_00002007

#### KEGG

KEGG is actually a set of databases, each with its own prefix, usually of form `KEGG.$database`, e.g.

 * [KEGG.ORTHOLOGY](https://registry.identifiers.org/registry/kegg.orthology) (aka KO), e.g. KEGG.ORTHOLOGY:K00001
 * [KEGG.COMPOUND](https://registry.identifiers.org/registry/kegg.compound), e.g. KEGG.COMPOUND:C12345

## Recommended IDs for use within NMDC

The NMDC schema is annotated with the set of IDs that are allowed to act as primary keys for instances of each class.

For example the class [OrthologyGroup](https://microbiomedata.github.io/nmdc-metadata/docs/OrthologyGroup) has a description of the IDs allowed on the class web page, the first listed is [KEGG.ORTHOLOGY](https://registry.identifiers.org/registry/kegg.orthology)

The underlying yaml looks like this:


```
  orthology group:
    is_a: functional annotation term
    description: >-
      A set of genes or gene products in which all members are orthologous
    id_prefixes:
      - KEGG.ORTHOLOGY  ## KO number
      - EGGNOG
      - PFAM
      - TIGRFAM
      - SUPFAM
      - PANTHER.FAMILY
    exact_mappings:
      - biolink:GeneFamily
```

The full URLs for each is in the jsonld context file

## IDs minted for use within NMDC

The NMDC schema specifies legal identifiers for all of its classes. All data instances/records that are intended for upload into the NMDC metadata store must have an `id` field that follows this specification, which is discussed below. NMDC offers a central identifier minting [endpoint](https://api.dev.microbiomedata.org/docs#/identifiers/mint_ids_ids_mint_post) in order to save data contributors the trouble of hand-crafting `id`s, but it will require an update before it generates `id`s following the pattern specified below.

The possibility of decentralized (or offline) minting of `id`s  by trusted organizations has also been anticipated. `id` component 3 below (the shoulder) is used to indicate the organizastion that minted an `id`. LBL, which hosts the `id` minting endpoint will use one shoulder value. If another organization, like JGI or EMSL, needs to bulk-create `id`s outside of the  central identifier minting endpoint, they would use different shoulders, to be determined by the NMDC schema and metadata team.

No matter where they are minted, all NMDC `id` values must match this abstract pattern:

```
nmdc:<type-code>-<shoulder>-<blade><.version><_locus>
```


The abstract pattern has six parts, delimited by hyphens (unless otherwise specified):

1. `nmdc`: All NMDC identifiers will begin with this static prefix.

2. `<type-code>`: An alphabetical code with a 1:1 correspondence to a class from the NMDC schema. Answers the question "of what class is the data record that bears this `id`"? Must consist of 1 to 6 lower case letters, although a minimum of 3 letters is suggested. The *type code* portion of an NMDC `id` must match the regular expression `[a-z]{1,6}`.

3. `<shoulder>`: A code that indicates what organization minted the identifier. Shoulder values must be zero to six lower case letters, flanked by one digit on either side. Answers the question "what organization minted this `id`"? The central identifier endpoint, hosted at LBL, uses the shoulder 00. Should organizations like JGI or EMSL need to mint identifiers in bulk, they would be assigned other shoulders, so that `id` values aren't reused. The *shoulder* portion of an NMDC `id` must match the regular expression `[0-9][a-z]{0,6}[0-9]`.

4. `<blade>`: The fully unique part of the identifier under a given type code and shoulder namespace. The _shoulder_ and _blade_ together make up the _key_ of the identifier. The blade is an alphanumeric string of open-ended length with at least one character, following the regular expression: `[A-Za-z0-9]{1,}`.

5. `<.version>`: Differentiates multiple iterations of a workflow. The delimiter used to separate the *version* from the *blade* and everything before it is a dot (`.`). The *version* is a potentially repeating alphanumeric pattern with a minimum length of 1 character. The *version* portion of an NMDC `id` must match the regular expression `(\.[A-Za-z0-9]{1,})*`.

6. `<_locus>`: Indicates the contig on which a genomic feature is found, along with its start and end coordinates. Delimited from the rest of the `id` by an underscore (`_`). The *locus* part, if present, must have at least one character from the set off uppercase letters, lower case letters, digits, underscores (`_`), dots (`.`) and hyphens (`-`). The regular expression that the locus will follow is: `_[A-Za-z0-9_\.-]+`.

Therefore, the regular expression pattern for the overall `id` is:

```
^(?<prefix>nmdc):(?<typecode>[a-z]{1,6})-(?<shoulder>[0-9][a-z]{0,6}[0-9])-(?<blade>[A-Za-z0-9]{1,})(?<version>(\.[A-Za-z0-9]{1,})*)(?<locus>_[A-Za-z0-9_\.-]+)?$
```

## Reuse vs minting new IDs

We try to reuse IDs as far as possible. For example, for any sample already in GOLD, we use the GOLD sample identifier, e.g. GOLD:Gb.....

## IDs generated during workflows

This section is in  progress. See https://github.com/microbiomedata/nmdc-metadata/issues/195

All instances of [OmicsProcessing](https://microbiomedata.github.io/nmdc-metadata/docs/OmicsProcessing) have IDs. The policy for ID depends on the provider.

Currently metagenomics omics objects look like this:

```yaml
      id: "gold:Gp0108335"
      name: "Thawing permafrost microbial communities from the Arctic, studying carbon transformations - Permafrost 712P3D"
      has_input: 
        - "gold:Gb0108335"
      part_of: 
        - "gold:Gs0112340"
      has_output: 
        - "jgi:551a20d30d878525404e90d5"
      omics_type: Metagenome
      type: "nmdc:OmicsProcessing"
      add_date: "30-OCT-14 12.00.00.000000000 AM"
      mod_date: "22-MAY-20 06.13.12.927000000 PM"
      ncbi_project_name: "Thawing permafrost microbial communities from the Arctic, studying carbon transformations - Permafrost 712P3D"
      processing_institution: "Joint Genome Institute"
      principal_investigator_name: "Virginia Rich"
```

note that we use re-using the GOLD ID rather than minting a new one

the linked data object uses a jgi prefix and an md5 hash

```yaml
      id: "jgi:551a20d30d878525404e90d5"
      name: "8871.1.114459.GCCAAT.fastq.gz"
      description: "Raw sequencer read data"
      file_size_bytes: 17586370657
      type: "nmdc:DataObject"
```

note that currently jgi is not registered and thus the ID is not resolvable

Currently metaproteomics omics objects look like this:

```yaml
      id: "emsl:404590"
      name: "FECB_21_5093B_01_23Dec14_Tiger_14-11-12"
      description: "High res MS with low res CID MSn"
      part_of: 
        - "gold:Gs0110132"
      has_output: 
        - "emsl:output_404590"
      omics_type: Proteomics
      type: "nmdc:OmicsProcessing"
      instrument_name: "VOrbiETD03"
      processing_institution: "Environmental Molecular Sciences Lab"
```

this is suboptimal; `emsl` is not yet registered, and it's not clear that the integer is unique within emsl, let alone the nmdc subset

the output data objects are formed from these:

```yaml
      id: "emsl:output_404590"
      name: "output: FECB_21_5093B_01_23Dec14_Tiger_14-11-12"
      description: "High res MS with low res CID MSn"
      file_size_bytes: 503296678
      type: "nmdc:DataObject"
```

the data objects use hashes (md5) prefixed with nmdc:

```yaml
      name: "404590_resultant.tsv"
      description: "Aggregation of analysis tools{MSGFplus, MASIC} results"
      file_size_bytes: 10948480
      type: "nmdc:DataObject"
      id: "nmdc:e0c70280a7a23c7c5cc1e589f72e896e"
```

note nmdc is not yet registered

Both metaG and metaT analyses produce GFF3 files. See [issue 184](https://github.com/microbiomedata/nmdc-metadata/issues/184) for more on how the GFF is modeled.

The main entity we care about in these is the [gene product] https://microbiomedata.github.io/nmdc-metadata/docs/GeneProduct) ID (usually a protein), this is what functional annotation hangs off. 

This is typically a protein encoded by a CDS, e.g.

```
Ga0185794_41    GeneMark.hmm-2 v1.05    CDS     48      1037    56.13   +       0       ID=Ga0185794_41_48_1037;translation_table=11;start_type=ATG;product=5-methylthioadenosine/S-adenosylhomocysteine deaminase;product_source=KO:K12960;cath_funfam=3.20.20.140;cog=COG0402;ko=KO:K12960;ec_number=EC:3.5.4.28,EC:3.5.4.31;pfam=PF01979;superfamily=51338,51556
```

Currently we are prefixing the ID field in GFF with `nmdc`, e.g. `nmdc:Ga0185794_41_48_1037` as the protein ID

When converting col9 we ensure that each ID is correctly prefixed. So for example, we use `KEGG.OTHOLOGY:K12960` not `KO:K12960` as the former is the official prefix according to KEGG and identifiers.org

We will also later need a policy for IDs for the sequences in col1 (ie genome or transcript), please return later for more details...


## MIxS term identifiers

We are working with the GSC to provide permanent IDs for MIxS terms. Note these terms are schema-level rather than data-level.

Please check this section later

For now we place these in the nmdc namespaces, e.g

`nmdc:alt`

## Identifier mapping

Please check this section later

## Identifiers and semantic web URIs

We produce a JSON-LD context with the schema:

 * [jsonschema/nmdc.context.jsonld](jsonschema/nmdc.context.jsonld)

When this is combined with schema-conformant JSON, RDF can be automatically created using the intended URIs
