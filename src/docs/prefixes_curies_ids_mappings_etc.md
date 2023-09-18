# Notes about prefixes, CURIEs, identifiers and mappings: 
## An NMDC and LinkML perspective

# First Draft: 2023-09-18

## The nmdc-schema is a framework for describing multi-omics microbiome experiments.

- What samples were included?
- Where were they gathered?
- What qualities do they have?
- How were they prepared, so that they would be suitable for sequencing, LC-MS proteomics, metabolomics, etc?
- How were the results of those analyses interpreted?

All metadata gathered and stored by the NMDC community must validate against the nmdc-schema.

## The nmdc-schema is expressed in the [LinkML](https://linkml.github.io/linkml/) schema language.

LinkML uses structures like classes, slots (for relationships and properties), types and enumerations.
People with object-oriented programming experience might find this familiar.

## The name "LinkML" indicates that it's' a modeling language for linked data.

LinkML schemas generally make good use of terminology from external resources, especially ontologies,
especially those from the OBO Foundry. In return, LinkML schema elements and the corresponding data should be
interoperable with other ontologies and semantic databases.

## Asserting element identifiers in the schema with URIs and CURIEs

One consequence of this semantic/linked data orientation is that all schema elements are identified by a URI,
most often in the compact CURIe form: a prefix and a local identifier.
Even if a class isn't decorated with a `class_uri` annotation, it will always have a key (in a JSON, YAML or Python Obj sense), 
which is sometimes reiterated as the `name`. In that case, the class' URI will be `<prefix>:<key>`. 
LinkML schemas should have default prefix assertions, but any element can use a different prefix, as long as an expansion is provided.

## Prefixes in LinkML **schemas**

Prefixes used in a LinkML must be associated with an expansion in the schema (which may include imported modules).
Ideally, the expanded URI should be web resolvable, but that is not required.
The prefixes can be expanded to base URIs owned by a particular resource, or they can be
expanded to base URIs owned by some resolving service, like the bioregistry.


## Asserting mappings in the nmdc-schema

As mentioned above, URIs are assigned to most elements of a LinkML schema, either explicitly by the schema authors,
or implicitly through the default prefix and the element's key. If an external prefix is used, that means the semantics 
of the element are identical to the external term, unless otherwise refined. Sometimes it is desirable to associate a 
LinkML schema element with a term from an external resource, without asserting that the semantics are identical. 
In this case, a variety of [mapping terms](https://linkml.io/linkml-model/latest/docs/mappings/) can be used.

Adding mappings to a schema element is one of the best and most compact ways to clarify the meaning of that element. 

Schema contributors are strongly encouraged to use mappings whose prefixes are already defined in the schema.
Schema contributors are always responsible for having a holistic understanding of an external term to be mapped
into the schema. This means gaining familiarity with the parent and child terms, as well as any other axioms 
applied to the term. The EBI Ontology Lookup Service is a good place to look for these details.

When it appears necessary to use a mapping whose prefix isn't already defined in the schema, the contributor
is responsible for having a holistic understanding of the external namespace (not just the term to be mapped).
There are several ways to start assessing an ontology that is being considered as a source of mappings.
If the ontology is in the OBO Foundry, one can look at the 
[OBO Foundry Dashboard](http://dashboard.obofoundry.org/dashboard/index.html).

## Asserting identifiers in LinkML data

Generally speaking, the smallest atom of LinkML data is an instance of one class. LinkML slots take values, 
but always in the context of some class (on the right hand side). LinkML data files are frequently collections 
of instances of one or more classes. The is no requirement that these classes provide a slot whose value
uniquely identifies the instances, but LinkML provides a mechanism that is broadly followed:
one slot available in each class is annotated with `identifier: true`. (Or at least, that's what it would look like
in a YAML serialization.) That means that the slot is required in all instances of the class, 
and that any collection of instances from that class must have unique values in that slot. 
It is also typical to say that the range of the is type `uriorcurie`.

## Mentioning identifiers in LinkML data

A common pattern in the nmdc-schema is asserting that some identifiable process has inputs and outputs. 

```yaml
pooling_set:
  - id: pooling:1
    inputs:
      - biosample:1
      - biosample:2
      - biosample:3
  - id: pooling:2
    inputs:
      - biosample:4
      - biosample:5
      - biosample:6
```

Here we have declared the existence of two pooling processes. A CURIe identifier is asserted for both of them,
and three inputs are mentioned for each. The example CURIes above don't necessarily follow any nmdc-schema
identifier pattern rules. If these were real CURIes, then the pooling and biosample prefixes would have to be
defined in the schema files.

In this case, let's assume definitions for the biosample inputs should be defined elsewhere in an NMDC data set.
Cases in which biosamples are mentioned without being defined would be considered violations of the referential integrity.
The development of referential integrity validators for LinkML has begun in Autumn, 2023.

Another pattern is saying that something defined within a NMDC data set is equivalent to something defined elsewhere.

## Using URIs supports scoping and self-documentation; using CURIes makes things more compact and readable



```yaml
biosample_set:
    - id: biosample:1
      gold_biosample_identifiers:
        - gold:1
        - gold:2
```

In this case, the gold prefix must be defined in the schema. When expanded to URIs via the prefix definitions,
these gold_biosample_identifiers would all be web-resolvable.

## Where to find a report of NMDC prefixes
* project/jsonld/nmdc.context.jsonld (autogenerated by m)
* assets/misc/data_prefix_expansions.context.jsonld (curated based on prefixed observed in MongoDB)



----

# include a pattern or make better use of id prefixes?

# may need to reassert identifier and or unique for subclasses

bioregistry not identifiers.org

Using URI or CURIe sematic identifiers means that the...

* multiple modules
* main exported jsonld context
* extra jsonld contest for data prefixes, especially using case-variant prefixes.
* bioregistry, not identifiers.org

----

# PREFIX, id and CURIe notes
* prefix definitions have to account for prefixes and base URIs used in the schema and in the data
* look out for http://example.org/UNKNOWN/ and "example." in the schema and in the data
* bioregistry is preferred over identifiers.org?
* should prefixes be uppercase or lowercase?
  * WARNING:root:Prefix case mismatch - supplied: cas expected: CAS
  * WARNING:root:Prefix case mismatch - supplied: massive expected: MASSIVE
  * WARNING:root:Prefix case mismatch - supplied: gold expected: GOLD
* see also project/jsonld/nmdc.context.jsonld
* see also project/prefixmap/nmdc.json

* gen-prefix-map doesn't merge
* emits JSON content into a file with teh .yaml extension by default
* so regenerating it from the merged schema as part of `project/nmdc_schema_merged.yaml` in `Makefile`
* why do project/jsonld/nmdc.context.jsonld and project/prefixmap/nmdc.json look so different?
* see also nmdc_schema/class_sparql.py
* see also nmdc_schema/anyuri_strings_to_iris.py (which applies but doesn't assert prefix expansions)
* see also nmdc_schema/migration_recursion.py which
* adds the nmdc prefix to totally bare CURIes
* converts CURIes with the UUID prefix into true <urn:uuid:...> IRIs
* also check validation `pattern`s and id_prefixes
* eliminate use of default_curi_maps
* MetaCyc expansion assumes we're talking about metacyc reactions and not genes, compounds etc.
* doesn't look like all the emit_prefixes are making it into the OWL output

# see also local/lint.log
## bioregistry not identifiers.org, BUT

warning Schema maps prefix 'CAS' to namespace 'https://bioregistry.io/cas:' instead of
namespace 'http://identifiers.org/cas/'  (canonical_prefixes)
warning Schema maps prefix 'CATH' to namespace 'https://bioregistry.io/cath:' instead of
namespace 'http://identifiers.org/cath/'  (canonical_prefixes)
warning Schema maps prefix 'CHEMBL.COMPOUND' to namespace 'https://bioregistry.io/chembl.compound:' instead of
namespace 'http://identifiers.org/chembl.compound/'  (canonical_prefixes)
warning Schema maps prefix 'DRUGBANK' to namespace 'https://bioregistry.io/drugbank:' instead of
namespace 'http://identifiers.org/drugbank/'  (canonical_prefixes)
warning Schema maps prefix 'EFO' to namespace 'http://www.ebi.ac.uk/efo/' instead of
namespace 'http://identifiers.org/efo/'  (canonical_prefixes)
warning Schema maps prefix 'EGGNOG' to namespace 'https://bioregistry.io/eggnog:' instead of
namespace 'http://identifiers.org/eggnog/'  (canonical_prefixes)
warning Schema maps prefix 'HMDB' to namespace 'https://bioregistry.io/hmdb:' instead of
namespace 'http://identifiers.org/hmdb/'  (canonical_prefixes)
warning Schema maps prefix 'MASSIVE' to namespace 'https://bioregistry.io/reference/massive:' instead of
namespace 'http://identifiers.org/massive/'  (canonical_prefixes)
warning Schema maps prefix 'MESH' to namespace 'https://bioregistry.io/mesh:' instead of
namespace 'http://identifiers.org/mesh/'  (canonical_prefixes)
warning Schema maps prefix 'PANTHER.FAMILY' to namespace 'https://bioregistry.io/panther.family:' instead of
namespace 'http://identifiers.org/panther.family/'  (canonical_prefixes)
warning Schema maps prefix 'PFAM' to namespace 'https://bioregistry.io/pfam:' instead of
namespace 'http://identifiers.org/pfam/'  (canonical_prefixes)
warning Schema maps prefix 'PUBCHEM.COMPOUND' to namespace 'https://bioregistry.io/pubchem.compound:' instead of
namespace 'http://identifiers.org/pubchem.compound/'  (canonical_prefixes)
warning Schema maps prefix 'SUPFAM' to namespace 'https://bioregistry.io/supfam:' instead of
namespace 'http://identifiers.org/supfam/'  (canonical_prefixes)
warning Schema maps prefix 'TIGRFAM' to namespace 'https://bioregistry.io/tigrfam:' instead of
namespace 'http://identifiers.org/tigrfam/'  (canonical_prefixes)
warning Schema maps prefix 'rdf' to namespace 'http://www.w3.org/1999/02/22-rdf-syntax-ns#' instead of using prefix '
RDF'  (canonical_prefixes)
warning Schema maps prefix 'rdfs' to namespace 'http://www.w3.org/2000/01/rdf-schema#' instead of using prefix 'RDFS'  (
canonical_prefixes)


# not using default_curi_maps any more
* all prefixes must now be explicit


## unresolved

* rdflib = "^6.2.0" # some LinkML components are not compatible with rdflib 7+ yet
* still getting anyurl typed string statement objects in RDF. I added a workaround in anyuri-strings-to-iris
* make better use of id prefixes?
* todo what reference ontologies do we want to include in a graph database? 
  * kegg, but from where?
  * nmdc schema
  * envo
  * mixs
  * chebi
  * selected branches of NCBI taxonomy? protein ontology?
  * could federate uniprot
* two graphdb endpoints: http://3.236.215.220:7200/sparql (switch to port 80) and https://graphdb-dev.microbiomedata.org/
* configure graphdb visual graph for showing blank nodes ?

## unrelated

* squeaky-clean does not include mixs-yaml-clean
* audit DOIs, websites, urls, and other uriorcurie values


