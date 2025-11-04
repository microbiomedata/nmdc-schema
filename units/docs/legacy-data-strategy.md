# Legacy Data Strategy

## Purpose

This document outlines a **proposed strategy** for handling legacy data with non-standard units. It is **speculative** and based on preliminary research rather than implemented solutions.

**For current problems:** See `units-problems-definitive.md`  
**For implemented solutions:** See `README.md`

## ⚠️ **PROPOSED STRATEGY** ⚠️

**This document contains implementation proposals based on GitHub issue discussions.**

## Overview

Proposed strategy for handling legacy data with units that cannot be converted to UCUM, based on [PR #2599](https://github.com/microbiomedata/nmdc-schema/pull/2599) discussions.

## Problem Statement

From [PR #2599](https://github.com/microbiomedata/nmdc-schema/pull/2599): *"One option for dealing with legacy data using units that we just don't want to approve of: a bertron-style key/value slot"*

Legacy data often contains:
- **Non-UCUM compliant units** that can't be standardized
- **Invalid unit combinations** that don't make scientific sense
- **Domain-specific notations** not suitable for general schema inclusion
- **Measurement errors** that shouldn't be perpetuated in the schema

## Proposed Approach: Enhanced `misc_param`

**Proposal**: Enhance existing `misc_param` slot for non-compliant unit metadata using flexible key-value structure.

**Status**: [Issue #2633](https://github.com/microbiomedata/nmdc-schema/issues/2633) - "implement key:value pairing for non-compliant unit metadata"

### Proposed Structure

```yaml
# THIS IS SPECULATIVE - NOT ACTUAL SCHEMA
misc_param:
  range: MiscParam
  description: Any other measurement performed or parameter collected, that is not listed here

classes:
  MiscParam:  # PROPOSED, NOT IMPLEMENTED
    slots:
      - attribute_id      # Optional: standardized attribute identifier
      - attribute_label   # Human-readable attribute name
      - raw_value        # Original value as recorded
      - normalized_value # Optional: attempted standardization
      - unit            # Original unit (may be non-UCUM)
      - notes           # Context/caveats about the measurement
```

### Example Usage

```json
{
  "attribute_label": "pump_efficiency_old_method",
  "raw_value": "85 weird_units",
  "unit": "weird_units", 
  "notes": "Legacy measurement using deprecated method, units not convertible to UCUM"
}
```

## Implementation Status

**Status**: Proposal stage - see [Issue #2633](https://github.com/microbiomedata/nmdc-schema/issues/2633).

## References

- [PR #2599](https://github.com/microbiomedata/nmdc-schema/pull/2599) - Original storage_units implementation (mentions bertron approach)
- [Issue #2633](https://github.com/microbiomedata/nmdc-schema/issues/2633) - Key:value pairing for non-compliant units (OPEN, NO IMPLEMENTATION)
- [Issue #2549](https://github.com/microbiomedata/nmdc-schema/issues/2549) - Bertron-schema modularization (CLOSED)
- [Bertron-schema PR #34](https://github.com/ber-data/bertron-schema/pull/34/files) - Reference implementation (external project)

## Note

**This is a proposed approach** based on PR discussions and GitHub issues. Check [Issue #2633](https://github.com/microbiomedata/nmdc-schema/issues/2633) for implementation progress.