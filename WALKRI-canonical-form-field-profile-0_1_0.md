---
title: WALKRI Canonical Form Field Profile for CROSS Round Configuration
version: 0.1.1
date: 2026-06-09
license: CC0
status: Working draft. Companion to WALKRI-interface-specification-0_1_0.md.
related_documents:
  - WALKRI-interface-specification-0_1_0.md
  - WALKRI-CROSS-boundary-0_1_0.md
  - CROSS/CROSS-canonical-round-configuration-schema-0_1_0.md
---

# WALKRI Canonical Form Field Profile for CROSS Round Configuration

Version 0.1.1 | 2026-06-09 | CC0

---

## Part I: Purpose

This document is the WALKRI companion to the CROSS Canonical Round Configuration Schema (CROSS-canonical-round-configuration-schema-0_1_0.md). It documents how the WALKRI x-walkri- field specification properties are instantiated in the CROSS canonical round configuration format. It is the reference for implementers building WALKRI-conformant fields within CROSS round configurations.

WALKRI-interface-specification-0_1_0.md defines the generic x-walkri- JSON Schema profile. This document applies that profile to the CROSS canonical round configuration context. This document does not supersede or modify the interface specification; it extends it with CROSS-specific notes.

The authority boundary between CROSS and WALKRI at the field level is specified in WALKRI-CROSS-boundary-0_1_0.md. CROSS covers the obligation architecture at the round level (obligation_mode, change_specification, components, gate_type). WALKRI covers the criterion specification quality at the field level (the x-walkri- properties on each field within sections).

---

## Part II: Field-Level Property Reference

Every field in a CROSS canonical round configuration carries the following x-walkri- properties. All are required for WALKRI conformance.

### Summary Table

| Property | Type | Required | WALKRI Requirement |
|---|---|---|---|
| `x-walkri-criterion-intent` | string | always | Criterion Intent (WALKRI Part III, 3.1) |
| `x-walkri-operational-definition` | object | always | Operational Definition (WALKRI Part III, 3.2) |
| `x-walkri-response-form-justification` | string | always | Response Form (WALKRI Part III, 3.3) |
| `x-walkri-evidence-form` | string | always | Evidence Form (WALKRI Part III, 3.4) |
| `x-walkri-conformance-threshold` | object | always | Conformance Threshold (WALKRI Part III, 3.5) |
| `x-walkri-verdict` | enum | always | Audit outcome: `instrument` or `label` |
| `x-walkri-specification-version` | string (semver) | always | Field specification versioning |
| `x-walkri-specification-date` | string (ISO 8601 date) | always | Field specification timestamp |

---

## Part III: The Operational Definition Object

`x-walkri-operational-definition` is an object with four required sub-fields. This structure is consistent with WALKRI-interface-specification-0_1_0.md Part 3.1.

```json
{
  "x-walkri-operational-definition": {
    "inclusion": "What a qualifying response looks like. For enum fields: one definition per option. For text fields: the scope and minimum content of a complete response.",
    "exclusion": "What a non-qualifying response looks like. The string 'none' is a valid documented assertion that no exclusion conditions exist. A blank field is an incomplete specification, not an implicit assertion of no exclusions.",
    "unit-of-analysis": "The unit being measured or described. For numeric fields: the counting unit and aggregation rule. For text fields: the level of description required.",
    "edge-case": "At least one edge case and its determination. Names a boundary condition and states which side of the boundary it falls on."
  }
}
```

---

## Part IV: The Conformance Threshold Object

`x-walkri-conformance-threshold` is required for all fields, including fields that reference no external standard. When no external standard is referenced, the field must carry:

```json
{
  "x-walkri-conformance-threshold": {
    "minimum-threshold": "none"
  }
}
```

The `"none"` value is a positive assertion that the field designer has considered whether an external standard reference applies and determined that none does. A missing `x-walkri-conformance-threshold` property is an incomplete specification.

When an external standard is referenced:

```json
{
  "x-walkri-conformance-threshold": {
    "standard-url": "https://example.org/standard",
    "version-anchor": "v2.1, 2024-03-15",
    "required-components": ["indicator-1", "indicator-3"],
    "evidence-per-component": {
      "indicator-1": "A signed attestation from the relevant certification body.",
      "indicator-3": "A publicly accessible repository meeting the named criteria."
    },
    "minimum-threshold": "all"
  }
}
```

`minimum-threshold` accepts: `all`, `minimum-N-of-M` (where N and M are specified in the value string, e.g., `"minimum-2-of-4"`), `custom` (where the threshold is described inline), or `none`.

---

## Part V: The WALKRI Verdict in CROSS Context

`x-walkri-verdict` carries `instrument` or `label`.

**instrument**: The field satisfies all five WALKRI criterion specification requirements at conformant quality. It may be published to applicants.

**label**: The field fails one or more requirements. It may not be published in a CROSS+WALKRI conformant round without a documented override and revision timeline. CROSS's field clarity gate (CROSS-grant-configurator-0_2_0.md Part IV) applies this before round publication.

A field may carry a `label` verdict during the design phase. The verdict must be resolved before the round configuration is published as the authoritative Commit stage output. A published round configuration with any `x-walkri-verdict: "label"` field lacking a documented override is a CROSS+WALKRI conformance failure.

---

## Part VI: Scope of the x-walkri- Profile in CROSS Fields

The x-walkri- properties cover only the fields within the `sections` array (and within component `sections` for compound rounds). They do not apply to round-level CROSS obligation architecture fields (obligation_mode, change_specification, components, gate_type, evidence_standard). Those fields are covered by CROSS. The applicable authority for each part of the schema is specified in WALKRI-CROSS-boundary-0_1_0.md.

The `id`, `label`, `description`, and `conditional_on` properties on a field are CROSS administrative fields. Their presence does not affect WALKRI conformance assessment.

---

## Part VII: Relationship to WALKRI-interface-specification-0_1_0.md

This profile is a direct application of the WALKRI JSON Schema profile defined in WALKRI-interface-specification-0_1_0.md Part 3.1. The following notes clarify the CROSS-specific application.

The operational definition uses the four sub-field structure (inclusion, exclusion, unit-of-analysis, edge-case) as specified in the interface specification.

Both `x-walkri-specification-version` and `x-walkri-specification-date` are required in the CROSS canonical format, consistent with the interface specification.

The CROSS canonical format adds a `label` field as the human-facing field name. This is distinct from the WALKRI criterion intent, which states what the field measures rather than what it is called.

Implementers building translators from the canonical CROSS format to specific form platforms should consult WALKRI-interface-specification-0_1_0.md for the XLSForm and REDCap compatibility mappings.

---

## Changelog

| Version | Date | Changes |
|---|---|---|
| 0.1.1 | 2026-06-09 | Conformance-threshold rename and Frame Language own-voice pass. The field property `x-walkri-compliance-threshold` is renamed `x-walkri-conformance-threshold` and the display name is now "Conformance Threshold" (a breaking annotation-key rename, aligning with the JSON schemas at @0.2.1 and the interface specification). Own-voice watchlist terms recast (govern to cover/apply, enforce to apply). No requirement changed; naming and vocabulary only. |
| 0.1.0 | 2026-05-22 | Initial specification. |
