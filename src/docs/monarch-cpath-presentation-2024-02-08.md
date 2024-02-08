# Samples in the `nmdc-schema`

## NMDC Background
- The [National Microbiome Data Collaborative](https://microbiomedata.org/) is (in this author's words) a environmentally-focused, schema-driven multi-omics project. 
- We are primarily funded by the United States Department of Energy 
- We provide tools for 
    - entering metadata about samples, following the constraints of a LinkML schema
    - interactively with [DataHarmonizer](https://github.com/cidgoh/DataHarmonizer)
    - in bulk through APIs
    - running standardized workflows for metagenomics, metatranscriptomics, metaproteomics, meta-metabolimics,etc.  
    - visually exploring the metadata in the NMDC Data Portal and downloading the outputs form the computational workflows
    - accessing the metadata through [APIs like this](https://api.microbiomedata.org/docs)
- NMDC actually has a few different schemas right now
    - The reference/production [nmdc-schema](https://github.com/microbiomedata/nmdc-schema)
        - documenation site
    - A flattened [submission-schema](https://github.com/microbiomedata/submission-schema) for DataHarmonizer, automatically derived from the `nmdc-schema`
        - we aspire to provide support for DataHarmonizer directly in the `nmdc-schema` eventually
    - A bleeding-edge [berkeley-schema-fy24](https://github.com/microbiomedata/berkeley-schema-fy24) fork that came out of a hackathon
        - To be merged into the production schema ASAP
    - A derriviative of the `nmdc-schema`, in the nmdc-schema repo, with weakened regular expression patterns that are tolerant of legacy identifiers.
        - Will be retried when we fininish converting the identifiers to follow the current standard.
        - *Elaborate?*

## Noteworthy Class Hierarchies in `nmdc-schema`
- Structure [AttributeValue](https://microbiomedata.github.io/berkeley-schema-fy24/AttributeValue/)s, like a quantity with a unit
- [PlannedProcess](https://microbiomedata.github.io/berkeley-schema-fy24/PlannedProcess/)es
- [OntologyClass](https://microbiomedata.github.io/berkeley-schema-fy24/OntologyClass/)es, for binding together a user-proved annotation and the corresponding ontology class identifier and label
- [**Biosample**](https://microbiomedata.github.io/berkeley-schema-fy24/Biosample/)s!
    - a subclass of [MaterialEntity](https://microbiomedata.github.io/berkeley-schema-fy24/MaterialEntity/)
    - [ProcessedSample](https://microbiomedata.github.io/berkeley-schema-fy24/ProcessedSample/) is a sibling of Biosample, and isn't differentiated very well yet, although we specify that most [sample-modifying processes](https://microbiomedata.github.io/berkeley-schema-fy24/MaterialProcessing/) only have `ProcessedSample`s as their output

## [Biosample](https://microbiomedata.github.io/berkeley-schema-fy24/Biosample/)s

> Biological source material which can be characterized by an experiment

- Biosample data instances can be retrieved from an API endpoint
    - for example: [https://api.microbiomedata.org/nmdcschema/biosample_set?max_page_size=20](https://api.microbiomedata.org/nmdcschema/biosample_set?max_page_size=20)
    - [additional retrieval options](https://api.microbiomedata.org/docs#/metadata/list_from_collection_nmdcschema__collection_name__get) can be viewed at the API's Swagger page
    - a [list of other instance collections with statistics](https://api.microbiomedata.org/nmdcschema/collection_stats) is available from another endpoint
- Currently these are **mostly** from natural or built environments, as opposed to host-associated environments like a mouse's cecum.
- Here's an API request for [and un-aggregated report of Biosample environmental contexts](https://api.microbiomedata.org/nmdcschema/biosample_set?max_page_size=20&projection=ecosystem%2Cecosystem_category%2Cecosystem_type%2Cecosystem_subtype%2Cspecific_ecosystem), according to the GOLD Ecosystem Classification 
- We extensively use the MIxS standard to annotate Biosamples. MIxS also provides three terms for describing a the context of a samples source. For example, [env_broad_scale](https://genomicsstandardsconsortium.github.io/mixs/0000012/)


## [MIxS](https://genomicsstandardsconsortium.github.io/mixs/) Annotations of NMDC Biosamples

## NMDC Biosamples are Overloaded





