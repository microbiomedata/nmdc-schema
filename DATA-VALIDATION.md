# Advanced Data Validation with RDF and SPARQL

> **Note**: This documentation is for maintainers who need to validate production MongoDB data against the schema. Most contributors working on schema definitions do not need these tools.

## Overview

The nmdc-schema repository includes advanced validation tools that convert MongoDB production data to RDF (Resource Description Framework) format for semantic web analysis. This workflow is resource-intensive and primarily used by maintainers for:

- Validating production MongoDB dumps against the schema
- Testing data migrations before deployment
- Running SPARQL queries against production data using GraphDB
- Identifying data quality issues at scale
- Exploring data relationships through graph queries

## Two-Level Validation

### Level 1: Basic Schema Validation (Automated)
```
MongoDB → YAML → linkml validate
```
This catches structural issues, type errors, and constraint violations.

### Level 2: Semantic Web Validation (Manual Setup)
```
MongoDB → YAML → RDF/Turtle → Ontotext GraphDB → SPARQL queries
```
This enables graph-based exploration and complex relationship queries.

## Requirements

### System Requirements
- **RAM**: 32GB minimum (MongoDB dumps are large)
- **Disk Space**: 50GB+ recommended for intermediate files
- **OS**: Linux or macOS (tested on Ubuntu)

### Software Requirements
1. **Python Environment**: Poetry-managed environment with all dependencies installed
2. **Java Runtime**: JRE 17 or higher (for Ontotext GraphDB)
3. **Docker**: For running GraphDB container
4. **Ontotext GraphDB**: Free version (see setup notes below)
5. **ROBOT tool** (optional): For additional OWL processing
6. **SSH Access**: NERSC account with access to production MongoDB

### Network Requirements
- SSH tunnel to NERSC MongoDB instance
- Ability to connect to `mongo-loadbalancer.nmdc.production.svc.spin.nersc.org:27017`

## Setup Instructions

### 1. Set Up Ontotext GraphDB (Docker)

> **Note**: GraphDB free version licensing has changed a few times. The setup below reflects current understanding but may require adjustments.

```bash
# Pull the GraphDB free edition Docker image
docker pull ontotext/graphdb:10.6.3-free

# Run GraphDB container
docker run -d \
  -p 7200:7200 \
  --name graphdb \
  -v $(pwd)/graphdb-data:/opt/graphdb/home \
  ontotext/graphdb:10.6.3-free

# GraphDB UI will be available at http://localhost:7200
```

**First-time setup:**
1. Access GraphDB at http://localhost:7200
2. Create a new repository (e.g., "nmdc-metadata")
3. Note: Free version licensing may require accepting terms through the UI

**Known issues:**
- License/registration flow changes periodically
- May require manual workarounds each time
- Current approach: "hack it out" until a stable automation path exists

### 2. Set Up SSH Tunnel to NERSC

```bash
# Initialize SSH proxy (if using sshproxy)
. ~/sshproxy.sh -u YOUR_NERSC_USERNAME

# Create SSH tunnel to MongoDB
ssh -i ~/.ssh/nersc \
    -L27777:mongo-loadbalancer.nmdc.production.svc.spin.nersc.org:27017 \
    -o ServerAliveInterval=60 \
    YOUR_NERSC_USERNAME@dtn01.nersc.gov
```

Keep this terminal open while running validation tasks.

### 3. Configure Environment

Create a `local/.env` file (if it doesn't exist):

```bash
mkdir -p local
touch local/.env
```

## Usage

### Automated Workflow (Level 1 + RDF Generation)

#### `make make-rdf`

Generates validated RDF files ready for loading into GraphDB:

```bash
make make-rdf
```

**What it does:**
1. Cleans previous RDF artifacts (`rdf-clean`)
2. Exports MongoDB data to YAML
3. Validates YAML against schema
4. Converts to RDF/Turtle format
5. Repairs and stamps RDF with metadata

**Output files** (in `local/`):
- `mongo_as_nmdc_database_validation.log` - Validation results
- `mongo_as_nmdc_database_cuire_repaired.ttl` - Repaired RDF in Turtle format
- `mongo_as_nmdc_database_cuire_repaired_stamped.ttl` - Timestamped RDF (ready for GraphDB)

#### `make pure-export-and-validate`

Export and validate MongoDB data without RDF conversion:

```bash
make pure-export-and-validate
```

This is faster and useful for checking validation errors without the full RDF pipeline.

### Manual Step: Loading into GraphDB

After running `make make-rdf`, load the RDF into GraphDB:

1. Access GraphDB UI at http://localhost:7200
2. Select your repository (e.g., "nmdc-metadata")
3. Go to "Import" → "Upload RDF files"
4. Upload `local/mongo_as_nmdc_database_cuire_repaired_stamped.ttl`
5. Also upload the OWL schema: `project/owl/nmdc.owl.ttl`

**Note**: This step is not automated due to GraphDB licensing/setup variability.

### Running SPARQL Queries

Once data is loaded into GraphDB, you can:

**Option 1: Use GraphDB UI**
- Go to "SPARQL" tab in GraphDB
- Paste query from `assets/sparql/` directory
- Execute and view results

**Option 2: Use the class_sparql.py script**
```bash
poetry run python src/scripts/experimental/class_sparql.py \
  --sparql-endpoint http://localhost:7200/repositories/nmdc-metadata \
  --target-class-name Study \
  --schema-file nmdc_schema/nmdc_materialized_patterns.yaml \
  -p project/jsonld/nmdc.context.jsonld
```

**Example queries** available in `assets/sparql/`:
- `Study.rq` - Extract all Study instances
- `OmicsProcessing.rq` - Extract OmicsProcessing data
- `subjects-lacking-rdf-types.rq` - Quality check for typing
- `mongodb-slots-to-units.rq` - Unit analysis

## Understanding the Workflow

### Data Flow

```
MongoDB (Production at NERSC)
    ↓ (SSH tunnel + pure-export)
YAML dump (local/mongo_as_nmdc_database.yaml)
    ↓ (linkml validate)
Validation log (local/mongo_as_nmdc_database_validation.log)
    ↓ (linkml convert --target-class Database --output-format ttl)
RDF/Turtle (local/mongo_as_nmdc_database.ttl)
    ↓ (repair + stamp)
Final RDF (local/mongo_as_nmdc_database_cuire_repaired_stamped.ttl)
    ↓ (MANUAL: GraphDB UI import)
Ontotext GraphDB (http://localhost:7200)
    ↓
SPARQL queries (via UI or class_sparql.py)
```

### Why RDF/GraphDB?

The RDF workflow provides capabilities beyond standard LinkML validation:

- **Graph queries**: Navigate complex relationships across the entire database
- **Exploratory analysis**: Discover patterns and connections via SPARQL
- **Standards compliance**: Validate against W3C semantic web standards (OWL)
- **Integration**: Combine with external ontologies and knowledge graphs
- **Quality checks**: Find orphaned entities, missing types, invalid references

## Known Limitations

**This workflow is not production-ready automation.** It's a maintainer tool that requires manual intervention and troubleshooting.

### OWL/RDF Conversion Issues
- **OWL schema generation doesn't always build cleanly** - may require workarounds
- **RDF data conversion may fail** on certain MongoDB structures
- **Standard OWL/RDF validators often report issues** - requires case-by-case fixes
- **Expect to hack/debug** the conversion process each time

### Why Not Query MongoDB Directly?

You might wonder: "Why convert to RDF? Why not query MongoDB directly?"

**MongoDB limitations for graph queries:**
- No native "find all subjects/objects using predicate P" query
- Aggregation pipelines can do some graph-style analysis but are verbose
- No built-in reasoning or inference
- Difficult to traverse arbitrary relationship depths

**GraphDB advantages:**
- SPARQL makes relationship queries elegant: `SELECT ?s ?o WHERE { ?s ?p ?o }`
- Can traverse graphs to arbitrary depth
- Reasoning/inference capabilities
- Standards-based (reusable queries across tools)

**Trade-off:**
- MongoDB: Fast, reliable, but limited graph capabilities
- GraphDB: Powerful graph queries, but fragile conversion pipeline

### When to Use This Workflow

✅ **Good for:**
- Exploratory data analysis
- Finding complex relationship patterns
- One-off investigations
- Learning about data structure

❌ **Not good for:**
- Automated CI/CD validation (too fragile)
- Routine testing (use `linkml validate` instead)
- Production monitoring (conversion too unreliable)

## Troubleshooting

### Out of Memory Errors

**During `make make-rdf`:**
```bash
# Increase Python memory limits if needed
export PYTHONMALLOC=malloc
make make-rdf
```

**During GraphDB import:**
- GraphDB free version has performance limitations with large files
- Consider importing in chunks or filtering data before conversion
- Allocate more memory to Docker container if needed

### SSH Tunnel Disconnects

The tunnel may timeout. Reconnect and resume:

```bash
# The -o ServerAliveInterval=60 flag helps prevent disconnects
# If disconnected, simply re-establish the tunnel and re-run make
```

### Validation Errors

Check the validation log for details:

```bash
cat local/mongo_as_nmdc_database_validation.log
```

Common issues:
- Missing required fields
- Type mismatches
- Invalid identifiers
- Broken references between entities

### GraphDB Setup Issues

**License/registration changes:**
- Free version licensing has changed multiple times
- May require creating an Ontotext account
- May require accepting license through UI on first run
- Solution: Follow current GraphDB documentation, expect manual steps

**Docker connectivity:**
```bash
# Check if GraphDB is running
docker ps | grep graphdb

# View GraphDB logs
docker logs graphdb

# Restart if needed
docker restart graphdb
```

## Alternative Approaches

### Patrick's Streaming Validation

An alternative streaming validation approach is under development that:
- Processes data in chunks (lower memory requirements)
- Provides faster feedback
- Doesn't require RDF conversion or GraphDB

*Documentation coming soon as this approach matures.*

## Performance Notes

Typical execution times on a machine with 64GB RAM:

- `pure-export-and-validate`: 10-30 minutes (depending on data size)
- `make make-rdf`: 1-3 hours (full pipeline to generate RDF)
- GraphDB import: 10-60 minutes (manual, UI-based)
- SPARQL queries in GraphDB: Seconds to minutes (depending on query complexity)

## Getting Help

If you encounter issues with this workflow:

1. **For LinkML/validation issues:**
   - Review validation logs in `local/` directory
   - Check schema documentation at https://microbiomedata.github.io/nmdc-schema/
   - Open an issue on GitHub

2. **For GraphDB issues:**
   - Check GraphDB logs: `docker logs graphdb`
   - Verify SSH tunnel: `netstat -an | grep 27777`
   - Consult Ontotext GraphDB documentation

3. **For SPARQL queries:**
   - Test queries in GraphDB UI first
   - Review example queries in `assets/sparql/`
   - Check `class_sparql.py` script documentation

## See Also

- [LinkML Documentation](https://linkml.io/)
- [Ontotext GraphDB Documentation](https://graphdb.ontotext.com/documentation/)
- [SPARQL Tutorial](https://www.w3.org/TR/sparql11-query/)
- [Migrators README](../nmdc_schema/migrators/README.md)
- [Units Documentation](../units/docs/README.md) - Example SPARQL-based analysis
