# LinkML Schema Expansion Mechanisms: Complete Technical Analysis

## Executive Summary

This document provides a comprehensive technical analysis of the fundamental mechanisms in LinkML that cause schema expansions during loading, induction, and dumping. The analysis reveals that expansions follow predictable patterns based on the LinkML metamodel design and can be categorized into three main mechanisms:

1. **ExpandedDict Serialization** - Collections of objects with multiple fields are serialized as lists instead of dictionaries
2. **Metaslot Injection** - Schema processing adds computed metadata fields to slots and classes
3. **Alias/Name Injection** - Key fields are duplicated as separate fields for storage optimization

## Part 1: The ExpandedDict/SimpleDict Serialization Mechanism

### 1.1 Fundamental Design Pattern

The core issue is in **yamlutils.py lines 69-78**, which shows the serialization logic in YAMLRoot._default():

```python
if isinstance(v, dict):
    itemslist = []
    for vk, vv in v.items():
        itemslist.append(vv)
    rval[k] = itemslist
```

When a slot is stored internally as a Python dict (for efficient lookup by key), the serializer converts it to a list when dumping to YAML. This is because:

1. **Internal storage is always dict** - Classes use `_normalize_inlined_as_dict()` to store collections as dictionaries for O(1) lookup
2. **YAML serialization expands to list** - The _default() method converts dicts to lists when serializing
3. **On reload** - The `_normalize_inlined()` method reconstructs the dict from the list form

### 1.2 Which Classes Get ExpandedDict Serialization?

Any class stored in a slot with these characteristics gets ExpandedDict serialization:

1. **Must be inlined**: `inlined: true`
2. **Must be multi-valued**: `multivalued: true`
3. **NOT inlined_as_list**: `inlined_as_list` is NOT true
4. **Does NOT have single non-PK attribute**: The range class cannot have exactly one non-identifier/non-key attribute (which would make it SimpleDict eligible)
5. **No "expanded" annotation**: Unless explicitly annotated with `expanded: false`

### 1.3 Classes with Multiple Fields (Candidates for ExpandedDict)

These LinkML metamodel classes are serialized as ExpandedDict because they have multiple semantic fields:

| Class | Key Field | Other Fields | Internal Storage |
|-------|-----------|-------------|-------------------|
| **Prefix** | `prefix_prefix` | `prefix_reference` | `{prefix_name: Prefix(...)}` |
| **LocalName** | `local_name_source` | `local_name_value` | `{source: LocalName(...)}` |
| **Setting** | `setting_key` | `setting_value` | `{key: Setting(...)}` |
| **Annotation** | `tag` | `value` + metadata | `{tag_name: Annotation(...)}` |
| **Extension** | `tag` | `value` + metadata | `{tag_name: Extension(...)}` |
| **PermissibleValue** | `text` | `description`, `meaning`, etc. | `{value: PermissibleValue(...)}` |
| **AltDescription** | `source` | `description` | `{source: AltDescription(...)}` |
| **StructuredAlias** | `literal_form` | `categories`, `distinguishing_text`, etc. | `{form: StructuredAlias(...)}` |
| **Example** | (id) | `value`, `description` | List or embedded |

### 1.4 Serialization Examples

**Internal representation (Python):**
```python
schema.prefixes = {
    'schema': Prefix(prefix_prefix='schema', prefix_reference='http://schema.org/'),
    'biolink': Prefix(prefix_prefix='biolink', prefix_reference='https://w3id.org/biolink/')
}
```

**After YAMLRoot._default() processing (expanded dict form):**
```yaml
prefixes:
  - prefix_prefix: schema
    prefix_reference: http://schema.org/
  - prefix_prefix: biolink
    prefix_reference: https://w3id.org/biolink/
```

**After yq cleanup (simplified):**
```yaml
prefixes:
  schema: http://schema.org/
  biolink: https://w3id.org/biolink/
```

### 1.5 SimpleDict Serialization Cases

A slot gets SimpleDict serialization when:
- `inlined: true`
- `multivalued: true`
- `inlined_as_list: false` (not explicitly a list)
- The range class has exactly ONE non-identifier/non-key attribute

This appears in schemaview.py:1000-1013:
```python
def _slot_as_simple_dict_value_slot(self, slot: SlotDefinition) -> Optional[SlotDefinition]:
    if not slot.inlined or slot.inlined_as_list:
        return False
    range_element = self._slot_range_element(slot)
    if isinstance(range_element, ClassDefinition):
        non_pk_atts = [s for s in range_element.attributes.values()
                       if not s.identifier and not s.key]
        if len(non_pk_atts) == 1:
            return non_pk_atts[0]
```

**Examples:** Any custom classes with exactly one meaningful field beyond the key would serialize as SimpleDict.

## Part 2: Metaslot Injection During Schema Processing

### 2.1 What Are Metaslots?

Metaslots are the fields/attributes of LinkML metamodel classes (SlotDefinition, ClassDefinition, etc.). They define the structure of schema elements. These are computed/added during:

1. **Schema loading** - When SchemaView initializes
2. **Slot induction** - When `induced_slot()` is called
3. **Class induction** - When `induced_class()` is called

### 2.2 Complete List of Metaslots That Get Added or Modified

During `induced_slot()` call (schemaview.py:1471-1579):

#### Always Modified:
1. **`owner`** - Set to the class name that "owns" this slot (line 1542)
   - Added by: `induced_slot.owner = an` in the loop through ancestor classes

2. **`domain_of`** - Populated with all classes that use this slot (lines 1575-1578)
   - Added by: Iterating through all classes and finding which ones reference the slot
   - Example: If slot "description" is used in 10 classes, `domain_of` will have 10 entries

3. **`alias`** - Set to the underscore version of slot name if not present (line 1574)
   - Added by: `induced_slot.alias = underscore(slot_name)` if not already set

#### Conditionally Modified (via metaslot propagation loop):
4. **`range`** - Gets default range from schema if not set (lines 1561-1563)

5. **`maximum_value`** / **`minimum_value`** - Combined from ancestor slots with special logic (lines 1528-1550)

6. **All inheritable slots** - Propagated from ancestor slots (lines 1521-1527):
   - These include: `title`, `description`, `deprecated`, `examples`, `in_subset`, `see_also`, `exact_mappings`, `close_mappings`, `related_mappings`, `narrow_mappings`, `broad_mappings`, `comments`, `notes`, `todos`, `annotations`, `extensions`, etc.

### 2.3 Additional Processing

Lines 1566-1574 also set:
- **`inlined`** - Set to true if `inlined_as_list` is true
- **`required`** - Set to true if `identifier` or `key` is true
- **`name`** (if mangle_name) - Mangled to `ClassName__slot_name` form

### 2.4 Where from_schema Is Added

**During schema loading (schemaview.py:407-410):**
```python
for s in self.schema_map.values():
    for e in s.all_elements().values():
        if e.from_schema is None:
            e.from_schema = s.id
        for a in e.aliases:
            a.from_schema = s.id
```

**During get_slot() for attributes (schemaview.py:723-724):**
```python
if slot is None and attributes:
    for c in self.all_classes(imports=imports).values():
        if slot_name in c.attributes:
            slot = copy(c.attributes[slot_name])
            slot.from_schema = c.from_schema
            slot.owner = c.name
```

### 2.5 Metaslot Summary Table

| Metaslot | Added By | When | Purpose |
|----------|----------|------|---------|
| `owner` | induced_slot() | Slot induction | Identifies which class owns this slot |
| `domain_of` | induced_slot() | Slot induction | Lists all classes using this slot |
| `alias` | induced_slot() | Slot induction | Alternative name for the slot |
| `from_schema` | load_import() / get_slot() | Schema loading | Track which schema element came from |
| `required` | induced_slot() | Slot induction | Inferred from identifier/key flags |
| `range` | induced_slot() | Slot induction | Default range from schema if not set |
| `inlined` | induced_slot() | Slot induction | Inferred from inlined_as_list |
| All inherited slots | induced_slot() | Slot induction | Propagated from ancestors |

## Part 3: Keyed Dictionary Fields That Expand

### 3.1 The Key Pattern in Metamodel Classes

The critical pattern from meta.py is that certain classes are defined to be stored as keyed dictionaries using `_normalize_inlined_as_dict()`:

Lines in meta.py `__post_init__` methods using keyed=True:
- Line 194: `alt_descriptions` (key: `source`)
- Line 379: `local_names` (key: `local_name_source`)
- Line 392: `extensions` (key: `tag`)
- Line 394: `annotations` (key: `tag`)
- Line 571: `prefixes` (key: `prefix_prefix`)
- Line 587: `subsets` (key: `name`)
- Line 589: `types` (key: `name`)
- Line 591: `enums` (key: `name`)
- Line 593: `slots` (key: `name`)
- Line 595: `classes` (key: `name`)
- Line 615: `settings` (key: `setting_key`)
- Line 896: `permissible_values` (key: `text`)

### 3.2 The Expansion Process

For each keyed dictionary slot:

1. **YAML Load** (list form):
   ```yaml
   prefixes:
     - prefix_prefix: schema
       prefix_reference: http://schema.org/
   ```

2. **__post_init__ normalization** (converts to dict):
   ```python
   self.prefixes = {
       'schema': Prefix(prefix_prefix='schema', prefix_reference='http://schema.org/')
   }
   ```

3. **YAML Dump** (converts back to list via _default()):
   ```yaml
   prefixes:
     - prefix_prefix: schema
       prefix_reference: http://schema.org/
   ```

4. **yq cleanup** (simplifies to value-only form):
   ```yaml
   prefixes:
     schema: http://schema.org/
   ```

## Part 4: Configuration Flags and Annotations

### 4.1 Inlined Configuration

The `inlined` slot property controls how multivalued fields are serialized:

```
inlined: false  → List of CURIEs/URIs (not expanded)
inlined: true + inlined_as_list: true  → List of full objects
inlined: true + inlined_as_list: false → Dict of full objects (ExpandedDict)
```

### 4.2 The "expanded" Annotation

In referencevalidator.py:498-502:
```python
if ("expanded" in parent_slot.annotations
    and parent_slot.annotations["expanded"].value):
    return CollectionForm.ExpandedDict
```

This annotation explicitly forces ExpandedDict serialization even when SimpleDict would normally apply.

### 4.3 CollectionForm Decision Tree

```
multivalued: false
  → NonCollection

multivalued: true + inlined: false
  → List

multivalued: true + inlined: true + inlined_as_list: true
  → List

multivalued: true + inlined: true + inlined_as_list: false
  + "expanded" annotation with value = true
  → ExpandedDict

multivalued: true + inlined: true + inlined_as_list: false
  + expand_all flag = true
  → ExpandedDict

multivalued: true + inlined: true + inlined_as_list: false
  + range class has exactly 1 non-PK attribute
  → SimpleDict

multivalued: true + inlined: true + inlined_as_list: false
  + other cases
  → CompactDict
```

## Part 5: Complete Expansion Patterns Beyond Patterns/Structured Patterns

### 5.1 Pattern Materialization (Already Documented)

- `structured_pattern` → `pattern` (regex compilation)

### 5.2 Attribute Materialization (NOT Default Behavior)

When using `gen-linkml --materialize-attributes`:
- Slot definitions in classes get expanded to their full induced form
- This adds all inherited and propagated metaslots
- Example: A slot in a subclass gets all metaslots from parent class merged in

### 5.3 Collection Form Materialization (Automatic)

When dumping and reloading:
- Internal dict representations become list representations
- These persist if not cleaned with yq pipeline
- The cleanup pipeline normalizes these back to simplified forms

### 5.4 Key Field Duplication (Always Present)

For classes with keyed storage, the key field appears twice:
- As the dictionary key: `{prefix_name: {...}}`
- As a field in the object: `{prefix_prefix: 'prefix_name'}`

This duplication is semantic - it allows round-tripping and ensures the object is self-contained.

### 5.5 Metadata Field Addition (During Induction)

When inducing slots, these fields are automatically populated:
- `owner` - Which class owns the slot
- `domain_of` - All classes using the slot
- `alias` - Normalized form of slot name
- `from_schema` - Which imported schema the element came from

### 5.6 Read-Only Slot Assertions

The current branch (2663-dont-assert-read-only-slots) indicates there were read_only assertions that are being removed. These would mark slots like `owner`, `domain_of`, and other computed fields as read-only.

## Part 6: The yq Cleanup Pipeline and Its Role

The cleanup pipeline (in SCHEMA_MATERIALIZATION_GUIDE.md) removes expansions:

1. **Annotations expansion removal** (Step 2, 5):
   ```bash
   yq eval '.classes[] |= select(has("annotations")).annotations |= map_values(.value)'
   ```
   Converts: `annotations: {tag: {tag: tag, value: actual_value}}` → `annotations: {tag: actual_value}`

2. **Prefix/Setting/LocalName simplification** (Steps 3, 4):
   ```bash
   yq eval '.prefixes |= map_values(.prefix_reference)'
   ```
   Converts: `{prefix_prefix: schema, prefix_reference: http://...}` → `http://...`

3. **Name field removal** (Steps 6-8, 11, 13):
   Removes redundant name fields that duplicate dictionary keys

4. **Domain/from_schema cleanup** (Steps 1, 10):
   Removes tracking metadata not needed in output

## Part 7: Prediction Matrix - When Expansions Occur

| Element Type | Serializes As | Expands To | Reverts To |
|--------------|--------------|-----------|-----------|
| **Prefix** | ExpandedDict | List of dicts | Simple key-value via yq |
| **LocalName** | ExpandedDict | List of dicts | List (keyed=False) |
| **Settings** | ExpandedDict | List of dicts | Simple key-value via yq |
| **Annotations** | ExpandedDict | List of dicts | Simple key-value via yq |
| **Slot in Class** | (depends on slot) | List if inlined_as_list | Unchanged |
| **owner metaslot** | String | Always persists | Removed by yq step 10 |
| **domain_of metaslot** | List | Appended during induction | Removed by yq step 10 |
| **from_schema metaslot** | URI | Added during load | Removed by yq step 1 |

## Part 8: Code Locations Reference

| Mechanism | File | Lines | Description |
|-----------|------|-------|-------------|
| **Dict→List conversion** | yamlutils.py | 69-78 | YAMLRoot._default() converts dicts to lists |
| **Dict normalization** | yamlutils.py | 98-209 | _normalize_inlined_as_dict() normalizes loaded lists back to dicts |
| **Metaslot injection** | schemaview.py | 1471-1579 | induced_slot() adds owner, domain_of, alias |
| **from_schema addition** | schemaview.py | 407-410, 723-724 | Set during loading and attribute retrieval |
| **SimpleDict detection** | referencevalidator.py | 1000-1013 | _slot_as_simple_dict_value_slot() checks for single attr |
| **CollectionForm decision** | referencevalidator.py | 481-503 | infer_slot_collection_form() decides serialization |
| **Keyed dict definitions** | meta.py | 194, 379, 392, 394, 571, 587-615, 896 | __post_init__ methods define keyed collections |
| **yq cleanup** | Makefile | 143-182 | Complete cleanup pipeline definition |

## Part 9: Key Insights for Predicting Expansions

1. **The Core Rule**: Any multi-valued, inlined slot that doesn't have `inlined_as_list: true` will serialize as a list (ExpandedDict) if its range class has more than one non-identifier field.

2. **The Key Field Double**: Classes like Prefix, LocalName, Setting have the key field defined twice (as dict key and as object field) to enable self-contained object storage.

3. **The Metadata Cascade**: Inducing a slot doesn't just materialize its own properties - it triggers computation of `owner`, `domain_of`, and propagation of all inheritable metaslots from ancestors.

4. **The Cleanup Philosophy**: The yq pipeline assumes that expanded forms are generated intermediates. The "true" schema is the compact form. Materialized forms are for tools that can't handle the compact form.

5. **The from_schema Tracking**: This metaslot is added by SchemaView to track which imported file each element came from. It's considered non-essential and removed in cleanup.

6. **No Magic Flags**: There's no hidden configuration that controls all expansions. They follow from:
   - The `inlined` and `inlined_as_list` slot properties
   - The structure of the range class (how many fields it has)
   - The "expanded" annotation on slots
   - The `expand_all` flag in ReferenceValidator

7. **Read-Only Fields**: Fields like `owner`, `domain_of`, and `from_schema` should ideally be marked read-only since they're computed, not user-set. The current branch appears to be removing incorrect read-only assertions.

## Conclusion

LinkML expansions are not arbitrary - they follow from the fundamental design choice to use Python dicts internally for efficient lookup, combined with YAML's lack of built-in dict notation. The yq cleanup pipeline is the final normalization step that removes these implementation details from the output schema artifact. Understanding these mechanisms allows precise prediction of which elements will expand and when, without needing empirical observation.
