# schema_definition Aggregation Slots

## Question
What are all the classes that a `schema_definition` can aggregate?

## Answer: 9 Collection Types

A `schema_definition` aggregates instances of the following metamodel classes:

| Collection Slot | Range (Class Type) | Description | YAML Key |
|----------------|-------------------|-------------|----------|
| **classes** | class_definition | Class definitions | Top-level `classes:` |
| **slots** | slot_definition | Slot definitions | Top-level `slots:` |
| **enums** | enum_definition | Enumeration definitions | Top-level `enums:` |
| **types** | type_definition | Type definitions | Top-level `types:` |
| **subsets** | subset_definition | Subset definitions | Top-level `subsets:` |
| **prefixes** | prefix | Namespace prefix mappings | Top-level `prefixes:` |
| **settings** | setting | Schema-wide settings | Top-level `settings:` |
| **bindings** | enum_binding | Enum bindings to classes/slots | Top-level `bindings:` |
| **imports** | uriorcurie | URIs of imported schemas | Top-level `imports:` |

## Detailed Breakdown

### 1. classes → class_definition

```yaml
classes:
  Person:           # key = class name
    description: A person
    slots:
      - name
      - age
```

- **Range**: class_definition (inherits from definition → element)
- **Multivalued**: true
- **Inlined**: true
- **Key**: name (from element)

### 2. slots → slot_definition

```yaml
slots:
  name:             # key = slot name
    range: string
    required: true
```

- **Range**: slot_definition (inherits from definition → element)
- **Multivalued**: true
- **Inlined**: true
- **Key**: name (from element)

Note: `slot_definitions` is an alias for `slots`

### 3. enums → enum_definition

```yaml
enums:
  StatusEnum:       # key = enum name
    permissible_values:
      - active
      - inactive
```

- **Range**: enum_definition (inherits from definition → element)
- **Multivalued**: true
- **Inlined**: true
- **Key**: name (from element)

### 4. types → type_definition

```yaml
types:
  email:            # key = type name
    uri: xsd:string
    base: str
    pattern: "^\\S+@\\S+$"
```

- **Range**: type_definition (inherits from element)
- **Multivalued**: true
- **Inlined**: true
- **Key**: name (from element)

### 5. subsets → subset_definition

```yaml
subsets:
  basic_subset:     # key = subset name
    description: Core elements
```

- **Range**: subset_definition (inherits from element)
- **Multivalued**: true
- **Inlined**: true
- **Key**: name (from element)

### 6. prefixes → prefix

```yaml
prefixes:
  schema:           # key = prefix name
    prefix_prefix: schema
    prefix_reference: http://schema.org/
```

- **Range**: prefix (ROOT class, not element descendant)
- **Multivalued**: true
- **Inlined**: true
- **Key**: prefix_prefix

### 7. settings → setting

```yaml
settings:
  my_setting:       # key = setting name
    setting_key: my_setting
    setting_value: "some value"
```

- **Range**: setting (ROOT class, not element descendant)
- **Multivalued**: true
- **Inlined**: true (assumed)
- **Key**: setting_key

### 8. bindings → enum_binding

```yaml
bindings:
  MyBinding:        # key context-dependent
    range: StatusEnum
    binds_value_of: status_slot
```

- **Range**: enum_binding (ROOT class, not element descendant)
- **Multivalued**: true
- **Inlined**: true (assumed)
- **Key**: No explicit identifier

### 9. imports → uriorcurie (special case)

```yaml
imports:
  - linkml:types
  - https://example.org/other-schema
```

- **Range**: uriorcurie (primitive type, not a class!)
- **Multivalued**: true
- **Not inlined**: This is a simple list of URIs, not objects
- **Note**: This is the ONLY collection slot that doesn't aggregate class instances

## Element vs Non-Element Aggregations

### Element Descendants (5 collections)

These aggregate **named schema elements** (all inherit from `element`):

1. **classes** → class_definition
2. **slots** → slot_definition
3. **enums** → enum_definition
4. **types** → type_definition
5. **subsets** → subset_definition

All use `name` as their identifier and appear as keyed collections in YAML.

### Non-Element Classes (3 collections)

These aggregate **helper/configuration objects**:

6. **prefixes** → prefix
7. **settings** → setting
8. **bindings** → enum_binding

Each has its own identifier mechanism (prefix_prefix, setting_key, etc.)

### Primitive Type (1 collection)

9. **imports** → uriorcurie (just a list of strings/URIs)

## Full schema_definition Slot List

From the metamodel, schema_definition has these slots (26 total):

### Aggregation Slots (9)
- classes, slots, enums, types, subsets, prefixes, settings, bindings, imports

### Metadata Slots (17)
- **Identifiers**: id, name
- **Versioning**: version, metamodel_version
- **Source info**: source_file, source_file_date, source_file_size, generation_date
- **Configuration**: default_prefix, default_range, default_curi_maps
- **Emit control**: emit_prefixes
- **License**: license
- **Constraints**: slot_names_unique

All of these are inherited from `element` or specific to `schema_definition`.

## Collection Pattern

All aggregation slots follow this pattern:

```yaml
slot_name:
  domain: schema_definition
  range: <definition_class>
  multivalued: true
  inlined: true
  inlined_as_list: false  # Creates keyed map, not list
```

This creates the YAML pattern:

```yaml
<collection_name>:
  <key1>:
    <properties>
  <key2>:
    <properties>
```

Rather than:

```yaml
<collection_name>:
  - name: <key1>
    <properties>
  - name: <key2>
    <properties>
```

## Inheritance of Aggregations

Note that `schema_definition` inherits from `element`, so it also has all element slots like:
- name, description, title
- aliases, mappings, annotations
- etc.

But the 9 aggregation slots listed above are the ones that hold **collections of other metamodel instances**.

## Summary

A `schema_definition` aggregates **9 types** of objects:

### Named Definitions (5) - All inherit from element
1. class_definition
2. slot_definition
3. enum_definition
4. type_definition
5. subset_definition

### Configuration Objects (3) - ROOT classes
6. prefix
7. setting
8. enum_binding

### External References (1) - Primitive type
9. uriorcurie (imports)

The first 5 are what users think of as "schema content" (classes, slots, enums, types, subsets).
The remaining 4 are supporting configuration and metadata.
