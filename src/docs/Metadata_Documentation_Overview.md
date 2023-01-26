# The NMDC Metadata Standards Documentation
# Introduction

This documentation provides details on the National Microbiome Data
Collaborative’s ([<u>NMDC</u>](http://microbiomedata.org)) approach to
sample and data processing metadata. These are key features that drive
the data search and discovery aspect of the NMDC data portal
([<u>https://microbiomedata.org/data/</u>](https://microbiomedata.org/data/)).
If you are unfamiliar with these types of metadata (Figure 1), we
recommend you begin with an *Introduction to Metadata and Ontologies:
Everything You Always Wanted to Know About Metadata and Ontologies (But
Were Afraid to Ask)*
([<u>https://doi.org/10.25979/1607365</u>](https://doi.org/10.25979/1607365)).

<div align="center">
	<img src="../images/NMDC_metadata_img1.png" style="width:80%"/>
</div>

Figure 1: Microbiome metadata types: Information that contextualizes
sample including its geographic location and collection date, sample
preparation, data processing methods, and data products produced from a
biological sample (Luke et al., 2020. Introduction to Metadata and
Ontologies: Everything You Always Wanted to Know About Metadata and
Ontologies (But Were Afraid to Ask). DOI: 10.25979/1607365).

All data integrated into the NMDC data portal must adhere to existing
metadata standards for proper indexing and display, and to ensure
accurate search results are returned. This documentation outlines the
standards and ontologies that were included in the NMDC data schema, a
framework that defines how data were defined and linked. For the
2019-2022 pilot initiative, the NMDC Metadata Standards Team (see the
[<u>NMDC Team page</u>](https://microbiomedata.org/team/)) leveraged
existing community-driven standards developed by the [<u>Genomics
Standards Consortium</u>](https://gensc.org/) (GSC), the Joint Genome
Institute (JGI) [<u>Genomes Online
Database</u>](https://gold.jgi.doe.gov/) (GOLD), and OBO Foundry’s
[<u>Environmental
Ontology</u>](http://www.obofoundry.org/ontology/envo.html) (EnvO). In
collaboration with these organizations, the NMDC has created a framework
for mapping these standards into an interoperable framework that can be
expanded to include additional standards and ontologies in the future.

Additional information on the activities by the NMDC Metadata Standards
team can be found on the NMDC website at:
[<u>https://microbiomedata.org/metadata/</u>](https://microbiomedata.org/metadata/)

# Standards and Ontologies used by the NMDC

## Sample Metadata

### GSC Minimum Information about any (x) Sequence (MIxS)

The GSC has developed standards for describing genomic and metagenomic
sequences, including the “minimum information about a genome sequence”
([<u>MIGS</u>](https://pubmed.ncbi.nlm.nih.gov/18464787/)), the “minimum
information about a metagenome sequence”
([<u>MIMS</u>](https://pubmed.ncbi.nlm.nih.gov/18464787/)), and the
“minimum information about a marker gene sequence”
([<u>MIMARKS</u>](https://pubmed.ncbi.nlm.nih.gov/21552244/)). To
complement this community-driven standard effort, the GSC has also
developed a system for describing the environment from which a
biological sample originates, as “environmental packages” and
established a unified standard set of checklists through the minimum
information about any (x) sequence (<u>MIxS</u>). MIxS provides a
standardized data dictionary of sample descriptors (e.g., location,
environment, elevation, altitude, depth, etc.) organized into different
packages for 17 different sample environments.

To standardize how physical samples are described (i.e., sample
metadata, Figure 1), the NMDC schema includes environmental descriptors
from the GSC MIxS standards.

*Explore how to create a MIxS-compliant sample metadata spreadsheet*

-   Review our example spreadsheet with sample metadata that has been
    converted to be compliant with the MIxS Soil environment package.
    Note that not all non-mandatory terms from the MIxs Soil package
    were relevant for these example samples, and hence were omitted for
    clarity.

    -   [<u>Basic sample
        spreadsheet</u>](https://docs.google.com/spreadsheets/d/1i2w2CEEHiMJZesi984LyU-ayaHKNFOCCN0TcPmKFda0/edit?usp=sharing)
        (Tab 1 - before conversion to MIxS)

    -   [<u>MIxS-compliant soil
        spreadsheet</u>](https://docs.google.com/spreadsheets/d/1i2w2CEEHiMJZesi984LyU-ayaHKNFOCCN0TcPmKFda0/edit?usp=sharing)
        (Tab 2 - converted to MIxS Soil)

-   Explore the mandatory, unique, and shared descriptors from the
    [<u>MIxS Soil
    package</u>](https://docs.google.com/document/d/1oNlMNQySuCoEeqhf1Qou8D-BV5bE76TkjrJLya8Ehw4/edit)

-   Searchable descriptors from ***all*** MIxS environmental packages *-
    coming soon!*

-   Learn more about all of the [<u>17 MIxS environmental
    packages</u>](https://gensc.org/mixs)

### Genomes Online Database (GOLD)

The JGI [<u>Genomes OnLine Database</u>](https://gold.jgi.doe.gov/)
(GOLD, [<u>Mukherjee
2021</u>](https://pubmed.ncbi.nlm.nih.gov/33152092/)) is an open-access
repository of genome, metagenome, and metatranscriptome sequencing
projects with their associated metadata. GOLD data are organized based
on Study, Biosample/Organism, Sequencing Project and Analysis Project
([<u>Mukherjee 2017</u>](https://pubmed.ncbi.nlm.nih.gov/30357420/)).
Biosamples (defined as the physical material collected from an
environment) are described using a five-level ecosystem classification
[path (Figure 2)](https://pubmed.ncbi.nlm.nih.gov/20653767/); the NMDC
schema also uses this ecosystem classification to describe sample
environments.

<div align="center">
<img src="../images/NMDC_metadata_img2.png" style="width:100%"/>
</div>

Figure 2. The GOLD five-level ecosystem classification paths
([<u>Mukherjee 2019</u>](https://pubmed.ncbi.nlm.nih.gov/33152092/)).

*Overview of the GOLD ecosystem paths*

-   ***Ecosystem*** describes biosamples using three different broadest
    contexts, namely environmental, engineered, and host-associated.

-   ***Ecosystem category*** subdivides the ecosystem into categories,
    such as aquatic or terrestrial.

-   ***Ecosystem type*** classifies those categories into types, such as
    freshwater or marine, cave, desert, soil, etc.

-   ***Ecosystem subtype*** allows for additional environmental context
    or boundaries.

-   ***Specific ecosystem*** that describes the environment that
    directly influences the sample or the environmental material itself.

*Explore how to map sample environments using the GOLD ecosystem
classification*

-   Learn more about the GOLD ecosystem paths using an [<u>interactive
    visualization tool</u>](https://gold.jgi.doe.gov/ecosystemtree).

-   Review a
    [<u>step-by-step</u>](https://drive.google.com/file/d/1h-FVY26G_Q_OazkZrYmlTg4QhQUZTRFY/view?usp=sharing)
    example of how to assign the GOLD ecosystem classification to a lake
    sediment sample.

### Environmental Ontology (EnvO)

The Environment Ontology (<u>EnvO</u>, [<u>Buttigieg
2016</u>](https://pubmed.ncbi.nlm.nih.gov/27664130/)) is a community-led
ontology that represents environmental entities such as biomes,
environmental features, and environmental materials. Each EnvO term is
identified using a unique *resource identifier* (e.g.,
[<u>CURIE</u>](https://en.wikipedia.org/wiki/CURIE) or
[<u>IRI</u>](https://en.wikipedia.org/wiki/Internationalized_Resource_Identifier))
that resolves in a web browser. This ensures that EnvO’s terms (and
their definitions) are easy to find, reference, and share amongst
collaborators. It also ensures that datasets described using EnvO terms
can be more easily integrated and analyzed in a reproducible manner. And
since the meanings of the terms are precisely defined and accessible,
humans and computers can easily connect EnvO terms across datasets.

EnvO terms are the recommended values for several of the mandatory terms
in the MIxS packages, often referred to as the "MIxS triad”.

-   **MIxS: env\_broad\_scale** (a.k.a. Biome): The major environmental
    system that the sample or specimen came from. Often, the value for
    this term comes from EnvO’s
    [<u>biome</u>](http://www.ontobee.org/ontology/ENVO?iri=http://purl.obolibrary.org/obo/ENVO_00000428)
    hierarchy, and is similar to GOLD’s *Ecosystem category.*

    -   <u>Examples:</u> forest biome, tropical biome, and oceanic
        pelagic zone biome

-   **MIxS: env\_local\_scale** (a.k.a. Feature): A more direct
    expression of the sample or specimen’s local vicinity, which likely
    has a significant influence on the sample or specimen. Possible
    values are listed in EnvO’s [<u>astronomical body
    part</u>](http://www.ontobee.org/ontology/ENVO?iri=http://purl.obolibrary.org/obo/ENVO_01000813)
    hierarchy, which is similar to GOLD’s *Ecosystem type/subtype.*

    -   <u>Examples</u>: mountain, pond, whale fall, and karst

-   **MIxS: env\_medium** (a.k.a. material): The environmental
    material(s) immediately surrounding your sample or specimen prior to
    sampling. Examples of this are found in EnvO’s [<u>environmental
    material</u>](http://www.ontobee.org/ontology/ENVO?iri=http://purl.obolibrary.org/obo/ENVO_00010483)
    hierarchy, and is similar to GOLD’s *Specific ecosystem.*

    -   <u>Examples:</u> sediment, soil, water, and air

*Explore how to map sample environments using the EnvO ecosystem
classification*

Review a step-by-step example of how to assign EnvO terms to an
oligotrophic lake sediment sample below.


<table>
 <tbody>
	<tr class="odd">
	 <td width="35%"  valign="top">
		<p><strong>env_broad_scale (Biome)</strong></p>
		<p>Using <a href="http://www.ontobee.org/ontology/ENVO?iri=http://purl.obolibrary.org/obo/ENVO_00000428"><u>EnvO biome</u></a> categories, <em>aquatic</em> is appropriate. However, since the EnvO is a hierarchical system, the aquatic biome has two sub-categories: freshwater and marine biomes. The freshwater biome is further divided into freshwater lake biome and freshwater river biome. Therefore, for a lake sediment sample, <em>freshwater lake biome</em> is the appropriate EnvO biome category.</p>
	 </td>
	 <td>
		<img src="../images/NMDC_metadata_img3.png" style="width:100%" />
	 </td>
	</tr>
	<tr class="even">
	<td valign="top">
	 <p><strong>env_local_scale (Feature)</strong></p>
	 <p>Next, we describe the local environmental feature in the vicinity of and likely having a strong causal influence on the sample. Using the <a href="http://www.ontobee.org/ontology/ENVO?iri=http://purl.obolibrary.org/obo/ENVO_01000813"><u>EnvO astronomical body part</u></a> categories, we step through the relevant categories (see figure on the right) until we reach the EnvO term <em>oligotrophic lake</em>.</p></td>
	<td>
		<img src="../images/NMDC_metadata_img4.png" style="width:100%" />
	</td>
	</tr>
	<tr class="odd">
	<td valign="top">
	 <p><strong>env_medium (Material)</strong></p>
	 <p>Finally, since the sample is <em>oligotrophic lake sediment</em>, the <a href="http://www.ontobee.org/ontology/ENVO?iri=http://purl.obolibrary.org/obo/ENVO_00002007"><u>EnvO environmental material</u></a> could be assigned <em>sediment</em>. But because the EnvO hierarchy provides sub-categories within <em>sediment</em>, the environmenta material will be assigned <em>lake sediment</em>.</p></td>
	 <td>
		 <img src="../images/NMDC_metadata_img5.png" style="width:100%" />
	 </td>
	</tr>
 </tbody>
</table>


Therefore, the EnvO triad for *oligotrophic lake sediment* is:

> **Env\_broad\_scale**: freshwater lake biome \[ENVO\_01000252\]
>
> **Env\_local\_scale**: oligotrophic lake \[ENVO\_01000774\]
>
> **Env\_medium**: lake sediment \[ENVO\_00000546\]

### Classifying samples with GOLD and MIxS/EnvO

The five-level GOLD ecosystem classification path and EnvO triad each
have unique advantages in describing the environmental context of a
biosample. The NMDC leverages the strengths of both the GOLD ecosystem
classification path and MIxS/EnvO triad. The assignment of MIxS/EnvO
triad for the biosamples currently in the NMDC data portal was achieved
through a manual curation process using various metadata fields of GOLD
biosamples fields, such as name, description, habitat, sample collection
site, identifier, ecosystem classification path, and study description.
The NMDC team is currently working on exploring solutions for automated
mapping between GOLD and MIxS/EnvO.

<div align="center">
	<img src="../images/NMDC_metadata_img6.png" style="width:80%" />
</div>

Figure 3: Mapping between the MIxS/EnvO triad and the GOLD ecosystem
classification enables integration of sample environments defined with
GOLD and MIxS/EnvO.

## Data Processing Metadata

In addition, the NMDC is adopting the MIxS standards for sequence data
types (e.g., sequencing method, pcr primers and conditions, etc.), and
are building on previous efforts by the [<u>Proteomics Standards
Initiative</u>](http://www.psidev.info/groups/mass-spectrometry) and
[<u>Metabolomics Standards
Initiative</u>](https://github.com/MSI-Metabolomics-Standards-Initiative/CIMR)
to develop standards and controlled vocabularies for mass spectrometry
data types (e.g., ionization mode, mass resolution, scan rate, etc.).
*Additional details on the processing metadata are coming soon.*

# Overview of the NMDC Data Schema

The NMDC has developed a normalized metadata
[<u>schema</u>](https://github.com/microbiomedata/nmdc-metadata)
(available in the NMDC GitHub) for representing studies, samples,
relationships between samples, and associated data objects. The schema
is organized into object classes, which act as nodes. Each class has
associated slots, which are fields that contain metadata that describe
the object. For more in-depth information, full documentation of the
NMDC schema can be found
[<u>here</u>](https://microbiomedata.github.io/nmdc-metadata/#classes).

For the NMDC pilot, a python
[<u>toolkit</u>](https://github.com/microbiomedata/nmdc-metadata) for
generating NMDC-compliant JavaScript Object Notation (JSON) objects was
developed to create ETL (Extract-Transform-Load) software to ingest
metadata from the DOE User Facilities. Read more about the data in the
NMDC pilot [<u>here</u>](https://microbiomedata.org/data/).
