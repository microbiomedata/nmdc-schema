## Invalid Schemas Description


The below table summarizes why each of the test JSON files in this folder are invalid.


| Filename                      | Invalidity Reason      |
| ----------------------------- | ---------------------- |
| [biosample_invalid_range.json](biosample_invalid_range.json)                       | Invalid types of values passed to `has_raw_value`, `latitude` and `longitude` |
| [biosample_mismatch_regex.json](biosample_mismatch_regex.json)                     | Array of values passed to `GOLD_sample_identifiers` do not fit regex |
| [biosample_missing_required_field.json](biosample_missing_required_field.json)     | Missing `id` field |
| [biosample_single_multi_value_mixup.json](biosample_single_multi_value_mixup.json) | Passing multiple values to `type` field |
| [biosample_undeclared_slot.json](biosample_undeclared_slot.json)                   | Added out of schema `foo` field |
| [study_credit_enum_mangle.json](study_credit_enum_mangle.json)                     | Passing values outside of enum to `applied_role` |
