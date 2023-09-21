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

```yaml
biosample_set:
    - id: biosample:1
      gold_biosample_identifiers:
        - gold:1
        - gold:2
```

In this case, the gold prefix must be defined in the schema. When expanded to URIs via the prefix definitions,
these gold_biosample_identifiers would all be web-resolvable.

## Constraining mentioned identifiers

We can limit the values that go into any slot by using a `pattern` constraint. We can also use the `id_prefixes` constraint
to limit the prefixes that are used in whatever slot has been declared to be the identifier of a class.
(Attributes of a class are supposed to be cascaded to subclasses, via the `is_a` attribute.
This may not always be the case though. In the nmdc-schema we have been using a belt-and-suspenders approach of 
re-declaring the `uriorcurie` range )

All prefixes used in the `id_prefixes` constraint must be defined in the schema. 
We should have a standing practice of reflecting on the declared `id_prefixes`, and removing prefixes that haven't been used yet
and are not likely to eer be used.

Maintenance of the prefix portions of a `pattern` will generally require more manual checking. We shouldn't be constraining
the values of slots to use a prefix that isn't declared, but no checks are automatically applied.

## Using URIs supports scoping and self-documentation

Any class could use any slot with any range to "link to" something external. A `Person` could have a `place_of_birth` slot,
and that could take unconstrained string or enumerated values like "Switzerland". But that doesn't provide much support for
people looking up more information about the place_of_birth. You could create `wikidata_place_of_birth` and 
`dbpedia_place_of_birth` slots and add annotations to the slot to aid in external lookups, but that isn't a good practice if
supporting several external targets. A better practice is to have one `place_of_birth` slot, with the `uriorcuire` range.
Then users can provide values like `<http://www.wikidata.org/entity/Q39>` or `<http://dbpedia.org/resource/Switzerland>`.
Then there is no ambiguity about the target of the link. 

## Using CURIes makes things more compact and readable

If the schema contains prefix definitions like 
`wd: <http://www.wikidata.org/entity/>` and `dbpedia: <http://dbpedia.org/resource/>`, then the values can be written as 
`wd:Q39` and `dbpedia:Switzerland`. This is more compact and readable, but it requires that the prefixes be defined in the schema.
Then, more constraint can be imposed with a pattern on the `place_of_birth` slot like '^(wd|dbpedia):.+$'

## Where to find a report of NMDC prefixes
* project/jsonld/nmdc.context.jsonld (autogenerated as the jsonldcontext output from `make gen-project`)
* assets/misc/data_prefix_expansions.context.jsonld (curated based on prefixed observed in MongoDB)

----

# PREFIX, id and CURIe notes

* not using `default_curi_maps` any more
  * all prefixes must now be explicit
* prefix definitions have to account for prefixes and base URIs used in the schema and in the data
* look out forthe presence of http://example.org/UNKNOWN/ and "example." in the schema, the data and any SPARQL results
* should prefixes be uppercase or lowercase?
  * it must be consistent. look for precedent
* bogus emsl UUID prefixes handled with `--emsl-biosample-uuid-replacement` in `anyuri-strings-to-iris`
* values that are supposed to be curies but don't have a prefix get the prefix `--salvage-prefix` added by `migration-recursion`
* keep an eye on validation `pattern`s and id_prefixes
* MetaCyc expansion assumes we're talking about metacyc reactions and not genes, compounds etc. The same may hold for other under-qualified prefixes

## see local/lint.log
### use bioregistry, not identifiers.org, BUT

> warning Schema maps prefix 'CHEMBL.COMPOUND' to namespace 'https://bioregistry.io/chembl.compound:' instead of
namespace 'http://identifiers.org/chembl.compound/'  (canonical_prefixes)

>warning Schema maps prefix 'rdf' to namespace 'http://www.w3.org/1999/02/22-rdf-syntax-ns#' instead of using prefix '
RDF'  (canonical_prefixes)
warning Schema maps prefix 'rdfs' to namespace 'http://www.w3.org/2000/01/rdf-schema#' instead of using prefix 'RDFS'  (
canonical_prefixes)

----

## unresolved

* may need to reassert identifier, range and or unique for subclasses
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

* gen-prefix-map 
  * doesn't merge
  * emits JSON content into a file with teh .yaml extension by default

* doesn't look like all the emit_prefixes are making it into the OWL output

* two graphdb endpoints: http://3.236.215.220:7200/sparql (switch to port 80) and https://graphdb-dev.microbiomedata.org/
* configure graphdb visual graph for showing blank nodes ?

## unrelated

* `make squeaky-clean` does not include `mixs-yaml-clean`, so that `mixs.yaml` isn't unnecessarily regenerated
* MAM audit DOIs, websites, urls, and other uriorcurie values


