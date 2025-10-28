# Readonly Slots Analysis

## Summary

Only **meta.yaml** has readonly assertions. No other LinkML schema files in this directory use readonly.

## Readonly Slots in meta.yaml

### Schema-level Metadata (supplied by loader/schema view)

These slots are automatically populated when a schema is loaded:

1. **definition_uri** (line 227)
   
   - Description: filled in by the schema loader or schema view
   - The native URI of the element

2. **from_schema** (line 355)
   
   - Description: supplied by the schema loader or schema view
   - ID of the schema that defined the element

3. **imported_from** (line 366)
   
   - Description: supplied by the schema loader or schema view
   - The imports entry that this element was derived from

4. **metamodel_version** (line 970)
   
   - Description: supplied by the schema loader or schema view
   - Version of the metamodel used to load the schema

5. **source_file** (line 977)
   
   - Description: supplied by the schema loader
   - Name, URI or description of the source of the schema

6. **source_file_date** (line 985)
   
   - Description: supplied by the loader
   - Modification date of the source of the schema

7. **source_file_size** (line 993)
   
   - Description: supplied by the schema loader or schema view
   - Size in bytes of the source of the schema

8. **generation_date** (line 1001)
   
   - Description: supplied by the schema loader or schema view
   - Date and time that the schema was loaded/generated

### Slot-level Metadata (filled in by loader)

These slots are computed for slot definitions:

9. **owner** (line 1934)
   
   - Description: filled in by loader -- either class domain or slot domain
   - The "owner" of the slot (deprecated, will be replaced by domain_of)

10. **domain_of** (line 1941)
    
    - Description: filled in by the loader
    - The class(es) that reference the slot in a "slots" or "slot_usage" context

11. **is_usage_slot** (line 1952)
    
    - Description: filled in by the loader
    - True means that this slot was defined in a slot_usage situation
    - Status: deprecated, replaced by usage_slot_name

12. **usage_slot_name** (line 1958)
    
    - Description: filled in by the loader
    - The name of the slot referenced in the slot_usage

### Definition of readonly Itself

13. **readonly** (line 1561)
    - The slot definition that defines what "readonly" means
    - Range: string
    - Inherited: true
    - Description: If present, slot is read only. Text explains why

## Key Insights

- **All readonly slots are system-generated**: None are meant to be set by schema authors
- **Two categories**:
  1. Schema-level metadata (8 slots) - about the schema itself
  2. Slot-level metadata (4 slots) - about how slots are used in classes
- **Purpose**: Prevent manual editing of values that should only be set by the LinkML framework
- **Used only in metamodel**: The concept of readonly is only needed in meta.yaml, which defines the metamodel itself

## Files Without Readonly

The following files have **no readonly assertions**:

- types.yaml
- extensions.yaml
- mappings.yaml
- annotations.yaml
- units.yaml
- validation.yaml
- datasets.yaml
- array.yaml
- extended_types.yaml
