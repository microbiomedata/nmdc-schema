# NMDC Schema Expansion Examples

This document provides concrete examples of expansions occurring in the NMDC schema, mapped to the underlying LinkML mechanisms.

## Example 1: Prefixes (ExpandedDict Serialization)

### Source YAML
```yaml
# src/schema/core.yaml
prefixes:
  linkml: https://w3id.org/linkml/
  biolink: https://w3id.org/biolink/
  nmdc: https://w3id.org/nmdc/
```

### Internal Representation (After SchemaView Load)
```python
schema.prefixes = {
    'linkml': Prefix(prefix_prefix='linkml', prefix_reference='https://w3id.org/linkml/'),
    'biolink': Prefix(prefix_prefix='biolink', prefix_reference='https://w3id.org/biolink/'),
    'nmdc': Prefix(prefix_prefix='nmdc', prefix_reference='https://w3id.org/nmdc/')
}
```

**Why Dict?** For fast O(1) lookup by prefix name during URI expansion.

### Expanded Form (After gen-linkml dump)
```yaml
prefixes:
  - prefix_prefix: linkml
    prefix_reference: https://w3id.org/linkml/
  - prefix_prefix: biolink
    prefix_reference: https://w3id.org/biolink/
  - prefix_prefix: nmdc
    prefix_reference: https://w3id.org/nmdc/
```

**Why List?** YAML has no dict notation with arbitrary ordering. YAMLRoot._default() converts internal dicts to lists.

**Code location:** yamlutils.py lines 69-78

### Cleaned Form (After yq pipeline)
```yaml
prefixes:
  linkml: https://w3id.org/linkml/
  biolink: https://w3id.org/biolink/
  nmdc: https://w3id.org/nmdc/
```

**Cleanup command:**
```bash
yq eval '.prefixes |= map_values(.prefix_reference)' schema.yaml
```

**Code location:** Makefile line 152

---

## Example 2: Annotations (ExpandedDict → Simplified)

### Source with Annotation
```yaml
# src/schema/some_file.yaml
classes:
  MyClass:
    description: "A class with metadata"
    annotations:
      example_tag: "some_value"
      another_tag: "another_value"
```

### Internal Representation
```python
schema.classes['MyClass'].annotations = {
    'example_tag': Annotation(tag='example_tag', value='some_value'),
    'another_tag': Annotation(tag='another_tag', value='another_value')
}
```

### Expanded Form (After dump)
```yaml
classes:
  MyClass:
    description: A class with metadata
    annotations:
      - tag: example_tag
        value: some_value
      - tag: another_tag
        value: another_value
```

**Why?** Annotation has multiple fields (tag, value), so it becomes ExpandedDict.

### Cleaned Form
```yaml
classes:
  MyClass:
    description: A class with metadata
    annotations:
      example_tag: some_value
      another_tag: another_value
```

**Cleanup command:**
```bash
yq eval '.classes[] |= select(has("annotations")).annotations |= map_values(.value)' schema.yaml
```

**Code location:** Makefile line 151

---

## Example 3: Slot Induction and Metaslot Addition

### Original Slot Definition
```yaml
# src/schema/core.yaml
slots:
  description:
    description: "A free text description of a thing"
    range: string
```

### After induced_slot(slot_name='description', class_name='Biosample')

```python
induced_slot_result = {
    'name': 'description',
    'description': 'A free text description of a thing',
    'range': 'string',
    'owner': 'Biosample',                    # ← ADDED by line 1542
    'domain_of': [                           # ← ADDED by lines 1577-1578
        'NamedThing',
        'Biosample',
        'StudySet',
        ...  # All classes using 'description'
    ],
    'alias': 'description',                 # ← ADDED by line 1574
    'from_schema': 'https://w3id.org/nmdc/' # ← ADDED by line 407
}
```

**Code locations:**
- `owner`: schemaview.py:1542
- `domain_of`: schemaview.py:1577-1578
- `alias`: schemaview.py:1574
- `from_schema`: schemaview.py:407-410

### Impact on Serialization

If you serialize an induced slot:
```yaml
slots:
  description:
    alias: description
    description: A free text description of a thing
    domain_of:
      - NamedThing
      - Biosample
      - StudySet
      - ...
    from_schema: https://w3id.org/nmdc/
    owner: Biosample
    range: string
```

These computed fields appear in the output. They should NOT be edited manually.

---

## Example 4: Permissible Values (Key Duplication + ExpandedDict)

### Source
```yaml
enums:
  BiomatTypeEnum:
    permissible_values:
      soil: "Soil material"
      water: "Water"
      plant: "Plant material"
```

### Internal Representation
```python
schema.enums['BiomatTypeEnum'].permissible_values = {
    'soil': PermissibleValue(text='soil', description='Soil material'),
    'water': PermissibleValue(text='water'),
    'plant': PermissibleValue(text='plant', description='Plant material')
}
```

**Note:** Key ('soil') is ALSO the text field value.

### Expanded Form
```yaml
enums:
  BiomatTypeEnum:
    permissible_values:
      - text: soil
        description: Soil material
      - text: water
      - text: plant
        description: Plant material
```

### Cleaned Form (removes 'text' redundancy)
```yaml
enums:
  BiomatTypeEnum:
    permissible_values:
      soil: "Soil material"
      water: null  # or just omitted
      plant: "Plant material"
```

**Cleanup command:**
```bash
yq eval 'del(.enums.[].permissible_values.[].text)' schema.yaml
```

**Code location:** Makefile line 158

---

## Example 5: Attributes with inlined_as_list

### Source Definition
```yaml
# src/schema/basic_classes.yaml
classes:
  QuantityValue:
    attributes:
      has_unit:
        description: "Unit of measurement"
        range: Unit
        inlined_as_list: true
        multivalued: true
```

### Expected Serialization
```yaml
# Always a list, never ExpandedDict
my_object:
  has_unit:
    - "unit:meter"
    - "unit:second"
```

NOT:
```yaml
# This would be wrong:
my_object:
  has_unit:
    - unit: "unit:meter"
    - unit: "unit:second"
```

**Rule:** `inlined_as_list: true` forces List form, never ExpandedDict.

**Code location:** referencevalidator.py:490

---

## Example 6: from_schema Tracking

### During Schema Load

When SchemaView loads imports:

```yaml
# schema_a.yaml
id: https://example.org/schema_a
types:
  MyType:
    description: "Custom type from schema A"

---

# schema_b.yaml (imports schema_a)
id: https://example.org/schema_b
imports:
  - schema_a
types:
  MyOtherType:
    description: "Type from schema B"
```

### After SchemaView Load
```python
sv = SchemaView('schema_b.yaml')
sv.get_type('MyType').from_schema
# → 'https://example.org/schema_a'

sv.get_type('MyOtherType').from_schema
# → 'https://example.org/schema_b'
```

### In Materialized Output
```yaml
types:
  MyType:
    description: Custom type from schema A
    from_schema: https://example.org/schema_a
  MyOtherType:
    description: Type from schema B
    from_schema: https://example.org/schema_b
```

### After Cleanup
```yaml
types:
  MyType:
    description: Custom type from schema A
  MyOtherType:
    description: Type from schema B
```

**Cleanup removes from_schema because it's metadata, not semantic content.**

**Code locations:**
- Addition: schemaview.py:407-410
- Removal: Makefile line 150

---

## Example 7: Settings Simplification

### Internal Form
```python
schema.settings = {
    'property_1': Setting(setting_key='property_1', setting_value='value_1'),
    'property_2': Setting(setting_key='property_2', setting_value='value_2')
}
```

### Expanded Form
```yaml
settings:
  - setting_key: property_1
    setting_value: value_1
  - setting_key: property_2
    setting_value: value_2
```

### Cleaned Form
```yaml
settings:
  property_1: value_1
  property_2: value_2
```

**Cleanup command:**
```bash
yq eval '.settings |= map_values(.setting_value)' schema.yaml
```

**Code location:** Makefile line 153

---

## Example 8: Class Induction with Multiple Field Propagation

### Original Classes
```yaml
classes:
  NamedThing:
    description: "A named thing"
    attributes:
      name:
        description: "Name of the thing"
        identifier: true

  Biosample:
    is_a: NamedThing
    description: "A biological sample"
    attributes:
      sample_type:
        range: string
```

### After induced_class('Biosample')
```python
induced = sv.induced_class('Biosample')
# Result has attributes dict with:
induced.attributes = {
    'name': SlotDefinition(
        name='name',
        description='Name of the thing',
        identifier=True,
        owner='Biosample',  # ← From induction
        domain_of=['NamedThing', 'Biosample'],  # ← From induction
        alias='name',  # ← From induction
    ),
    'sample_type': SlotDefinition(
        name='sample_type',
        range='string',
        owner='Biosample',  # ← From induction
        alias='sample_type',  # ← From induction
    )
}
```

**Note:** The 'name' slot gets properties from NamedThing propagated down to Biosample context.

**Code location:** schemaview.py:1587-1613

---

## Example 9: SimpleDict vs ExpandedDict

### Custom Class - SimpleDict Case
```yaml
classes:
  ColorValue:
    attributes:
      color_code:
        identifier: true
      hex_value:
        range: string

  attributes_with_colors:
    range: ColorValue
    inlined: true
    multivalued: true
    inlined_as_list: false
```

**Result: SimpleDict**
```yaml
# Serialized form
my_object:
  attributes_with_colors:
    red: "#FF0000"
    green: "#00FF00"
    blue: "#0000FF"
```

**Why?** ColorValue has exactly 1 non-identifier field (hex_value), making it a SimpleDict candidate.

**Code location:** referencevalidator.py:1000-1013

### Compare to ExpandedDict Case
```yaml
classes:
  ColorValue:
    attributes:
      color_code:
        identifier: true
      hex_value:
        range: string
      description:  # ← Additional field!
        range: string
```

**Result: ExpandedDict**
```yaml
# Serialized form
my_object:
  attributes_with_colors:
    - color_code: red
      hex_value: "#FF0000"
      description: "Red color"
    - color_code: green
      hex_value: "#00FF00"
      description: "Green color"
```

**Why?** ColorValue now has 2 non-identifier fields, so it becomes ExpandedDict.

---

## Example 10: Read-Only Computed Fields Issue

### The Problem
```yaml
# This should ideally be marked read-only:
slots:
  owner:
    description: "The class that owns this slot"
    range: string
    read_only: true  # ← Because it's computed by induced_slot()
```

### Current Issue
The branch `2663-dont-assert-read-only-slots` suggests read_only assertions are causing problems:
- Some induction methods don't properly initialize computed fields if marked read_only
- Better approach: Don't mark computed fields as read_only, just document they're generated
- Users should understand `owner`, `domain_of`, `from_schema` come from processing, not editable source

**Code location:** Current work in branch 2663-dont-assert-read-only-slots

---

## How to Detect Expansions in NMDC

```bash
# Find all slots that will cause ExpandedDict expansion
grep -r "inlined: true" src/schema/*.yaml | grep -v "inlined_as_list: true"

# Find all classes that are range of multi-valued, inlined slots
# These need to be checked for ExpandedDict/SimpleDict status

# View the materialized version with expansions
cat contrib/nmdc_materialized.yaml | grep -A 10 "prefixes:"

# View the cleaned version
cat contrib/nmdc.yaml | grep -A 5 "prefixes:"
```

---

## Summary: Expansion Patterns in NMDC

| Element | Type | Mechanism | Cleanup |
|---------|------|-----------|---------|
| Prefixes | ExpandedDict | Dict→List in YAML | map_values(.prefix_reference) |
| Settings | ExpandedDict | Dict→List in YAML | map_values(.setting_value) |
| Annotations | ExpandedDict | Dict→List in YAML | map_values(.value) |
| Extensions | ExpandedDict | Dict→List in YAML | (not cleaned in NMDC) |
| Permissible Values | ExpandedDict + Key | Dict→List in YAML | del([].text) |
| Slot.owner | Metaslot | Computed by induced_slot() | (custom cleanup) |
| Slot.domain_of | Metaslot | Computed by induced_slot() | (custom cleanup) |
| from_schema | Metaslot | Set by load_import() | del(.. select has) |
| Domain specs | Metaslot | Computed/propagated | del(slots select != MixsCompliantData) |
