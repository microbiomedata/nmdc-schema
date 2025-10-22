# Import Closure for meta.yaml

## Direct Imports

From `meta.yaml` lines 70-76:

1. `linkml:types`
2. `linkml:mappings`
3. `linkml:extensions`
4. `linkml:annotations`
5. `linkml:units`
6. ~~`linkml:validation`~~ (commented out)

## Transitive Imports

### From annotations.yaml

- `linkml:types` (already included)
- `linkml:extensions` (already included)

### From units.yaml

- `linkml:types` (already included)
- `linkml:extensions` (already included)
- `linkml:annotations` (already included)
- `linkml:mappings` (already included)

### From mappings.yaml

- `linkml:types` (already included)

### From extensions.yaml

- `linkml:types` (already included)

### From types.yaml

- (no imports - base schema)

## Complete Import Closure

Total of **5 schemas** are included in the closure:

```
meta.yaml
├── types.yaml
├── extensions.yaml
│   └── types.yaml
├── mappings.yaml
│   └── types.yaml
├── annotations.yaml
│   ├── types.yaml
│   └── extensions.yaml
│       └── types.yaml
└── units.yaml
    ├── types.yaml
    ├── extensions.yaml
    │   └── types.yaml
    ├── annotations.yaml
    │   ├── types.yaml
    │   └── extensions.yaml
    └── mappings.yaml
        └── types.yaml
```

## Schemas NOT in the Closure

The following schemas are **not** included in meta.yaml's import closure:

- `validation.yaml` (also known as `reporting.yaml`)
- `datasets.yaml`
- `array.yaml`
- `extended_types.yaml`

These are standalone schemas that import only `types.yaml` and are not pulled into `meta.yaml`.

## Summary

| Category           | Schemas                                         |
| ------------------ | ----------------------------------------------- |
| **In Closure**     | types, extensions, mappings, annotations, units |
| **Not in Closure** | validation, datasets, array, extended_types     |
| **Total Schemas**  | 10 files total, 5 in meta.yaml closure          |
