# Parent Classes of Non-Element Classes

## Summary

Of the 32 metamodel classes that are NOT in the element closure:

| Parent Class | Count | Type | Purpose |
|-------------|-------|------|---------|
| **ROOT** (no parent) | 26 | Standalone | Helper/structural classes |
| **expression** | 3 | abstract, mixin | Expression types |
| **anonymous_expression** | 2 | abstract | Anonymous nested structures |
| **class_level_rule** | 1 | abstract | Rule base class |

## Detailed Breakdown

### 1. ROOT Classes (26 classes - no inheritance)

These classes have no parent (`is_a: null`):

#### Mixins (3)
- **common_metadata** (mixin) - Shared metadata slots
- **class_expression** (mixin) - Boolean expressions for class membership
- **expression** (abstract, mixin) - Base for all expression types

#### Abstract Base Classes (2)
- **anonymous_expression** (abstract) - Base for nested anonymous structures
- **class_level_rule** (abstract) - Base for rule types

#### Helper/Structural Classes (21)
1. **Anything** - Unconstrained type
2. **alt_description** - Attributed descriptions
3. **anonymous_enum_expression** - Anonymous enum constraints
4. **anonymous_type_expression** - Anonymous type constraints
5. **array_expression** - Array dimension specifications
6. **dimension_expression** - Individual array dimension
7. **enum_binding** - Enum binding to slots/classes
8. **example** - Usage examples
9. **extra_slots_expression** - Extra slots handling
10. **import_expression** - Import specifications
11. **local_name** - Localized names
12. **match_query** - Pattern matching for enums
13. **path_expression** - Path through slot sequences
14. **pattern_expression** - Regular expression patterns
15. **permissible_value** - Enumeration values
16. **prefix** - Namespace prefixes
17. **reachability_query** - Graph reachability for enums
18. **setting** - Global settings/constants
19. **structured_alias** - Structured synonyms
20. **type_mapping** - Framework-specific type mappings
21. **unique_key** - Composite key definitions

### 2. expression Children (3 classes)

**Parent:** `expression` (abstract, mixin)

1. **enum_expression** - Enum range constraints
2. **slot_expression** (mixin) - Slot value constraints
3. **type_expression** (mixin) - Type constraints

### 3. anonymous_expression Children (2 classes)

**Parent:** `anonymous_expression` (abstract)

1. **anonymous_class_expression** - Inline class expressions
2. **anonymous_slot_expression** - Inline slot expressions

### 4. class_level_rule Children (1 class)

**Parent:** `class_level_rule` (abstract)

1. **class_rule** - If-then rules for classes

## Inheritance Trees

```
expression (abstract, mixin) [ROOT]
├── enum_expression
├── slot_expression (mixin)
└── type_expression (mixin)

anonymous_expression (abstract) [ROOT]
├── anonymous_class_expression
└── anonymous_slot_expression

class_level_rule (abstract) [ROOT]
└── class_rule

[26 standalone ROOT classes with no parents]
```

## Comparison: Element vs Non-Element Hierarchies

### Element Hierarchy (8 classes)
```
element (abstract)
├── schema_definition
├── type_definition
├── subset_definition
└── definition (abstract)
    ├── enum_definition
    ├── slot_definition
    └── class_definition
```

**Characteristics:**
- Deep hierarchy (3 levels)
- All have `name` as identifier
- Represent named schema elements
- Total: 8 classes

### Non-Element Hierarchies (32 classes)

**Characteristics:**
- Shallow hierarchies (max 2 levels)
- 26/32 are ROOT level (no parent)
- No standardized identifier (each uses different key)
- Represent:
  - Constraints/expressions
  - Metadata/helpers
  - Structural elements
- Total: 32 classes

## Why So Many ROOT Classes?

Most non-element classes are ROOT because they serve **specialized, independent purposes**:

1. **Configuration** (prefix, setting, import_expression)
2. **Metadata** (example, alt_description, local_name)
3. **Constraints** (array_expression, pattern_expression, unique_key)
4. **Enum mechanics** (permissible_value, match_query, reachability_query, enum_binding)
5. **Type mappings** (type_mapping, extra_slots_expression)
6. **Aliasing** (structured_alias)
7. **Helpers** (Anything, path_expression, dimension_expression)

These don't need inheritance because they're **context-specific helpers** rather than core schema elements.

## Mixins (Abstract Classes Available for Mixing)

Several non-element classes are mixins that can be mixed into other classes:

| Mixin | Type | Used By |
|-------|------|---------|
| **expression** | abstract, mixin | Base for all expression types |
| **common_metadata** | mixin | Mixed into many classes for standard metadata |
| **class_expression** | mixin | Boolean expressions for classes |
| **slot_expression** | mixin | Constraint expressions for slots |
| **type_expression** | mixin | Type constraint expressions |

## Key Insight: Two Parallel Hierarchies

LinkML's metamodel has **two distinct class hierarchies**:

### 1. Element Hierarchy (Named Schema Elements)
- **Purpose**: Define the named components of a schema
- **Identifier**: `name` slot
- **Hierarchy**: Deep (3 levels)
- **Examples**: Classes, slots, enums, types

### 2. Non-Element Classes (Helpers & Constraints)
- **Purpose**: Support schema definition with metadata, constraints, expressions
- **Identifiers**: Varied (text, key slots, or none)
- **Hierarchy**: Shallow (mostly flat)
- **Examples**: Expressions, settings, examples, patterns

This design keeps **core schema elements separate from helper/constraint mechanisms**.
