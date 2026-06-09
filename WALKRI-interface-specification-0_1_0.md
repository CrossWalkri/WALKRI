---
title: WALKRI Interface Specification
version: 0.1.1
date: 2026-06-08
license: CC0
status: Working draft. Companion to WALKRI-standard-0_1_0.md.
---

# WALKRI Interface Specification

Version 0.1.1 | 2026-06-08 | CC0

---

## Part 1: Purpose

This document is for implementers building tools that connect to WALKRI: form builders, data collection platforms, obligation standard toolchains, and downstream data consumers. It provides the technical contracts for each of WALKRI's three interfaces.

The WALKRI standard defines *what* is required: the five criterion specification elements, the three-stage process, the data quality standards, and the certification model. This document defines *how* those requirements are communicated across system boundaries. Where the standard says "fields must carry provenance information," this document specifies the exact JSON structure that carries it. Where the standard says "secondary compatible formats are recognized," this document specifies the field-by-field mappings.

Three separate interfaces are needed because WALKRI sits at a junction between three fundamentally different kinds of systems, each with its own data model and conformance expectations.

WALKRI connects to obligation standards, which are normative frameworks specifying what must be collected. These systems care about declared requirements, gate criteria, and certification tiers. They do not care about JSON Schema internals or webhook delivery.

WALKRI connects to form rendering tools, which encode questions as fields and collect responses. These systems care about field types, validation rules, and export formats. They have their own data models (XLSForm, REDCap data dictionaries, JSON Schema) that must be reconciled with WALKRI's field specification requirements.

WALKRI connects to data consumers: ML pipelines, researchers, evaluators, and automated analysis systems. These systems care about schema consistency, provenance metadata, and alignment with open data standards such as Croissant, FAIR, and W3C PROV.

Each interface requires a distinct technical contract. A single unified specification would obscure the distinctions and make implementation harder.

---

## Part 2: Obligation Standards

This section specifies how any obligation standard connects to WALKRI. The interface is generic; any conformant obligation standard may use it.

### 2.1 What an Obligation Standard Provides to WALKRI

An obligation standard that formally references WALKRI must provide the following for each collection requirement it imposes:

**A declared list of fields or criteria the standard requires to be collected.** This list must be machine-readable and versioned. Each field or criterion must carry a stable identifier within the obligation standard's namespace (e.g., `cross:gate-criterion:open-licensing` or `dpgs:indicator:2`).

**For each field: the obligation mode it serves.** WALKRI recognizes four obligation modes. Build obligations apply to fields required during an initial design or setup phase. Change obligations apply to fields required when an existing entity modifies its configuration or status. Retroactive obligations apply to fields that must be completed for prior periods when a new obligation comes into effect. Other obligations cover any field that does not fit the three primary modes; the obligation standard must document the mode in this case.

**Whether the field is required or optional at each gate.** For multi-gate processes (like the CROSS two-level gate), the obligation standard specifies which fields are required at the first gate (typically a lighter specification requirement) and which are required at the second gate (typically the full specification requirement). Fields that are optional at one gate may be required at another.

**Any external standards the field must reference.** If the obligation standard requires applicants to demonstrate conformance with a third-party standard (e.g., the Digital Public Goods Standard, SPDX license identifiers, WCAG accessibility standards), the obligation standard must name those external standards and their version anchors. WALKRI's External Standard Reference Protocol (Part VI of the WALKRI standard) then specifies how those references are encoded in field specifications.

### 2.2 What WALKRI Provides Back to the Obligation Standard

For each field in a WALKRI-certified form, WALKRI produces:

**A conformance record entry for each field.** The entry states the pass, fail, or override status for each of the five criterion specification requirements (criterion intent, operational definition, response form, evidence form, conformance threshold). It also records any override justifications for fields that were flagged but passed via documented override.

**The certification tier achieved.** WALKRI recognizes two certification tiers: Standard and Enhanced. Standard certification requires all five criterion specification requirements to be satisfied for all fields, with overrides permitted where documented. Enhanced certification additionally requires Croissant metadata generation, W3C PROV provenance graph output per response, and a publicly published conformance record with a stable URI. The obligation standard specifies which tier it requires; WALKRI reports the tier achieved.

**The field specification version that applies to each gate assessment.** Because field specifications evolve independently of the standard, the conformance record binds the assessment to a specific field specification version. This version anchor is the mechanism that ensures a downstream consumer can determine which definition applied to the data collected in any given reporting period.

### 2.3 CROSS Connection

CROSS references WALKRI for Gate Criterion Specification and Data Quality Standards. A CROSS-conformant program satisfies both references by running all gate criterion fields through WALKRI audit before the round opens. This is implemented by the Grant Configurator's field clarity gate: no field that fails WALKRI audit (with unresolved, undocumented flags) may be published to applicants.

Implementers deploying CROSS and WALKRI together should consult WALKRI-CROSS-boundary-0_1_0.md, which specifies, for each CROSS requirement, whether CROSS or WALKRI is the applicable authority.

### 2.4 Generic Connection for Non-CROSS Obligation Standards

Any standard that requires fields to be collected can reference WALKRI without implementing CROSS. The generic reference form is:

> "Fields collecting [named requirement] must meet WALKRI criterion specification requirements at [Standard / Enhanced] certification level, as specified in WALKRI-standard-0_1_0.md."

No other WALKRI-specific implementation is required beyond this declaration and the field audit process it entails. The obligation standard does not need to reproduce WALKRI's five criterion specification elements; it references them by standard citation. The obligation standard is responsible for declaring which fields require WALKRI certification; WALKRI is responsible for defining what certification means.

An obligation standard that takes this approach must include a version anchor for WALKRI in its citation (e.g., "WALKRI v0.1.0") so that the requirements binding on implementers at any given time are unambiguous.

---

## Part 3: Form Rendering Tools

WALKRI's native format is JSON Schema (draft-07 or later). This section specifies the WALKRI JSON Schema profile: the specific fields, extensions, and constraints that WALKRI adds to base JSON Schema to carry criterion specification information.

### 3.1 The WALKRI JSON Schema Profile

The WALKRI JSON Schema profile adds custom properties to each field definition using the `x-walkri-` prefix convention. These properties are vendor extensions in JSON Schema terms; conformant JSON Schema validators ignore properties they do not recognize, so WALKRI-extended schemas remain valid JSON Schema.

The following custom properties are required for a WALKRI-conformant field definition:

```json
{
  "x-walkri-criterion-intent": "string (required)",
  "x-walkri-operational-definition": {
    "inclusion": "string (required)",
    "exclusion": "string (required; 'none' is a valid documented value)",
    "unit-of-analysis": "string (required)",
    "edge-case": "string (required)"
  },
  "x-walkri-response-form-justification": "string (required)",
  "x-walkri-evidence-form": "string (required)",
  "x-walkri-conformance-threshold": {
    "standard-url": "string (URI, required when an external standard is referenced)",
    "version-anchor": "string (required when an external standard is referenced)",
    "required-components": ["array of strings"],
    "evidence-per-component": {"component-name": "evidence description"},
    "minimum-threshold": "string: 'all' | 'minimum-N-of-M' | 'custom'"
  },
  "x-walkri-specification-version": "string (semver, required)",
  "x-walkri-specification-date": "string (ISO 8601, required)"
}
```

Each property maps directly to a WALKRI criterion specification requirement:

| Custom Property | WALKRI Requirement |
|---|---|
| `x-walkri-criterion-intent` | Criterion Intent (Part III, 3.1) |
| `x-walkri-operational-definition` | Operational Definition (Part III, 3.2) |
| `x-walkri-response-form-justification` | Response Form (Part III, 3.3) |
| `x-walkri-evidence-form` | Evidence Form (Part III, 3.4) |
| `x-walkri-conformance-threshold` | Conformance Threshold (Part III, 3.5) |
| `x-walkri-specification-version` | Field Specification Version (Part VII, 7.1) |
| `x-walkri-specification-date` | Specification Timestamp (Part VII, 7.1) |

The `x-walkri-conformance-threshold` object is required whenever the field references an external standard. When no external standard is referenced, the property must still be present but may carry `{"minimum-threshold": "none"}` to make the absence of a referenced standard explicit rather than leaving the property absent (which would be ambiguous between "no standard referenced" and "this property was not yet specified").

The `x-walkri-operational-definition.exclusion` field accepts the string `"none"` as a valid documented value when there are genuinely no exclusion conditions. A blank field is an incomplete specification; `"none"` is a positive assertion that the field designer has considered exclusions and found none applicable.

### 3.2 Base JSON Schema Properties for Validation

The following base JSON Schema properties carry WALKRI-relevant validation constraints without requiring extension:

`type` specifies the response type (string, number, boolean, array). For WALKRI purposes, the type must be consistent with the response form justification in `x-walkri-response-form-justification`.

`enum` encodes the defined options for single-select and multi-select fields. Each option in `enum` must have a corresponding entry in `x-walkri-operational-definition.inclusion` that defines what the option means. An `enum` value without a definition in the operational definition is a WALKRI conformance failure.

`format` encodes semantic types for text fields: `email`, `uri`, `date` (ISO 8601). For ETH wallet address fields, `format` does not have a standard value; use `pattern` instead.

`pattern` encodes regular expression validation. For ETH wallet addresses, the conformant pattern is `^0x[a-fA-F0-9]{40}$`. For other pattern-validated fields, the pattern must be documented in the operational definition with an explanation of what it matches and why.

`minimum` and `maximum` encode the valid range for numeric fields. These must be consistent with the unit of analysis and counting rule specified in `x-walkri-operational-definition`.

`minLength` and `maxLength` encode character limits for text fields. Minimum length requirements must be consistent with the minimum content requirement stated in `x-walkri-operational-definition`.

### 3.3 XLSForm Compatibility

XLSForm is a widely used open standard for defining surveys, used by KoBoToolbox, ODK, and related platforms. WALKRI criterion specification elements map to XLSForm columns as follows:

| WALKRI Property | XLSForm Column |
|---|---|
| `x-walkri-criterion-intent` | `hint` column |
| `x-walkri-evidence-form` | `bind::walkri:evidence` (custom bind column) |
| `x-walkri-operational-definition` | `constraint_message` (for validation failure text) + `x-walkri-operational-definition` (metadata column) |
| `x-walkri-response-form-justification` | `x-walkri-response-form-justification` (metadata column) |
| `x-walkri-conformance-threshold` | `x-walkri-conformance-threshold` (metadata column as JSON string) |
| `x-walkri-specification-version` | `x-walkri-specification-version` (metadata column) |
| `x-walkri-specification-date` | `x-walkri-specification-date` (metadata column) |

The `bind::walkri:evidence` column follows XLSForm's bind namespace convention. XLSForm tools that do not recognize this column will ignore it without error; the column exists to preserve WALKRI evidence form metadata through XLSForm import and export cycles.

XLSForm import into a WALKRI tool produces a WALKRI field specification draft, not a complete specification. The draft populates available fields from the XLSForm columns above but leaves `x-walkri-operational-definition.unit-of-analysis` and `x-walkri-operational-definition.edge-case` for Stage 2 completion. Importing an XLSForm does not produce a WALKRI-conformant specification automatically; it produces the starting material for Stage 2 work.

XLSForm export from a WALKRI tool must preserve all `x-walkri-` metadata columns. A WALKRI tool that strips these columns on export is not compatible at this interface.

### 3.4 REDCap Data Dictionary Compatibility

REDCap data dictionaries export field definitions with the following columns: Field Name, Form Name, Field Type, Field Label, Choices/Calculations (for categorical fields), Field Note, Text Validation Type, Text Validation Min, and Text Validation Max.

WALKRI maps REDCap export columns to draft field specification content as follows:

| REDCap Column | WALKRI Mapping |
|---|---|
| `Field Label` | Draft `x-walkri-criterion-intent` |
| `Field Note` | Draft `x-walkri-criterion-intent` (supplement, if more detailed than Field Label) |
| `Choices/Calculations` | Draft `x-walkri-operational-definition.inclusion` per option |
| `Text Validation Type` | Informs `x-walkri-response-form-justification` |
| `Text Validation Min` / `Max` | Maps to JSON Schema `minimum`/`maximum` or `minLength`/`maxLength` |
| `Field Type` | Maps to JSON Schema `type` and informs response form |

REDCap import produces a WALKRI field specification draft requiring Stage 2 completion. The draft populates criterion intent from the Field Label and option definitions from Choices, but `x-walkri-operational-definition.exclusion`, `x-walkri-operational-definition.unit-of-analysis`, `x-walkri-operational-definition.edge-case`, `x-walkri-response-form-justification`, `x-walkri-evidence-form`, and `x-walkri-conformance-threshold` all require Stage 2 authorship before the specification is conformant.

### 3.5 Form Tool Compatibility Checklist

A form tool must satisfy the following requirements to be WALKRI-compatible:

- Export form definitions as JSON Schema or XLSForm, with all `x-walkri-` properties preserved in the export.
- Accept JSON Schema import with custom `x-walkri-` properties intact; a tool that strips unknown properties on import is not compatible.
- Support webhook delivery of form responses to the WALKRI Enrichment Layer. The webhook payload must include the field name, the response value, the form version, and a submission timestamp.
- Support field-level metadata, not only form-level metadata. WALKRI's provenance and specification properties are per-field; a tool that only permits metadata at the form level cannot carry WALKRI field specifications correctly.

A tool that meets all four requirements is WALKRI-compatible. A tool that meets the first two but not the third is compatible for specification storage but not for downstream enrichment; the operator must implement an alternative mechanism for passing responses to the enrichment layer.

---

## Part 4: Data Consumers

This section specifies what WALKRI-enriched output must contain for each form response, and how that output aligns with the Croissant, FAIR, and W3C PROV standards.

### 4.1 The Provenance Envelope

The WALKRI Enrichment Layer adds a provenance envelope to each submitted response. The envelope is a JSON object appended to the response record. It does not modify any response value; it adds metadata.

```json
{
  "walkri:provenance": {
    "form-id": "string (stable identifier for this form, not instance-specific)",
    "form-version": "string (semver)",
    "field-specification-version": "string (semver per field; use object map for per-field versions)",
    "walkri-version": "0.1.0",
    "form-tool": "string (tool class identifier, e.g. 'KoBoToolbox'; not instance URL)",
    "collection-timestamp": "string (ISO 8601)",
    "certification-level": "standard | enhanced | uncertified",
    "conformance-record-ref": "string (URI to published conformance record; null if not published)"
  }
}
```

The `field-specification-version` may be either a single semver string (if all fields in the form share a single specification version) or a JSON object mapping field names to individual semver strings (for forms where different fields were certified at different versions). The per-field map form is required whenever any field has been revised independently of others:

```json
{
  "field-specification-version": {
    "organization-name": "1.0.0",
    "wallet-address": "1.0.0",
    "open-license-indicator": "1.2.0",
    "impact-narrative": "2.0.0"
  }
}
```

The `form-tool` value is the tool class identifier (the tool's product name or platform name), not the specific deployment URL. The downstream consumer needs to know the class of tool to assess any known constraints it imposes on response capture; they do not need the instance URL, which changes across deployments and may expose internal infrastructure.

The `certification-level` field reports the certification tier achieved by the form. A form that has never been audited by the WALKRI Audit Tool carries `"uncertified"`. A form that was audited but did not achieve the minimum conformance threshold also carries `"uncertified"`. Only forms that have passed audit carry `"standard"` or `"enhanced"`.

### 4.2 Croissant Alignment

Croissant is an ML-ready dataset metadata standard. WALKRI-enriched datasets can produce Croissant metadata by mapping the provenance envelope and field specifications to Croissant's RecordSet and Field structures.

The following mappings apply:

| WALKRI Property | Croissant Mapping |
|---|---|
| `x-walkri-criterion-intent` | `ml:Field/description` |
| `x-walkri-operational-definition` | `ml:Field/semantics` |
| `x-walkri-response-form-justification` | `ml:Field/annotation` (custom annotation) |
| `x-walkri-evidence-form` | `ml:Field/annotation` (custom annotation, separate from response form justification) |
| `walkri:provenance.certification-level` | `ml:RecordSet/annotation` (custom Croissant annotation: `walkri:certificationLevel`) |
| `walkri:provenance.conformance-record-ref` | `ml:RecordSet/annotation` (custom Croissant annotation: `walkri:conformanceRecord`) |
| `walkri:provenance.form-version` | `ml:RecordSet/version` |
| `walkri:provenance.collection-timestamp` | `ml:RecordSet/datePublished` |

Croissant metadata generation is an Enhanced certification feature. A Standard-certified WALKRI form may produce Croissant metadata as an optional output; an Enhanced-certified form must produce it as a required output.

The Croissant metadata for a WALKRI-enriched dataset is a separate artifact from the dataset itself. It is generated by the WALKRI Enrichment Layer on request and is not embedded in the response records. Its URI is recorded in `walkri:provenance.conformance-record-ref` alongside the conformance record URI, or in a separate `walkri:provenance.croissant-metadata-ref` field if both are published.

### 4.3 FAIR Alignment

WALKRI satisfies the four FAIR principles as follows.

**Findable.** WALKRI certification produces a conformance record with a stable URI. At Enhanced certification level, the conformance record is published at that URI. The `walkri:provenance.conformance-record-ref` field in every response envelope carries this URI, making the dataset's quality documentation discoverable from any individual response.

**Accessible.** Form specifications and conformance records are published in JSON Schema format, which is an open, machine-readable format with no license restrictions. No authentication is required to read WALKRI field specifications; they are designed to be open reference documents.

**Interoperable.** JSON Schema with `x-walkri-` extensions is parseable by any JSON Schema tool; the extensions are ignored by validators that do not know about them, and consumed by validators that do. The `x-walkri-` namespace is reserved for WALKRI use. No conflicts with other JSON Schema extension namespaces have been identified as of v0.1.1.

**Reusable.** The provenance envelope provides the version, specification metadata, license, and form tool class required for a downstream consumer to assess whether a dataset is reusable for their purpose. A consumer who receives a WALKRI-enriched dataset can determine: which version of each field definition applied to the data; which version of the WALKRI standard applied to the audit; and whether the form was certified. This is the minimum information required for a reusability assessment.

### 4.4 W3C PROV Alignment

The W3C PROV data model expresses provenance using three core concepts: Entity (a thing whose provenance is tracked), Activity (something that happened), and Agent (a party bearing responsibility for an activity).

The provenance envelope maps to W3C PROV-O as follows:

| Provenance Envelope Field | PROV-O Mapping |
|---|---|
| Form at a specific version (`form-id` + `form-version`) | `prov:Entity` |
| Collection event (`collection-timestamp`) | `prov:Activity` |
| Form tool (`form-tool`) | `prov:Agent` (software agent) |
| Field specifying organization (from conformance record) | `prov:Agent` (organizational agent) |
| Individual response record | `prov:Entity` (was generated by the collection activity) |
| Conformance record | `prov:Entity` (was generated by the audit activity) |

The WALKRI Enrichment Layer produces a PROV-compatible provenance graph for each response on request. This is an Enhanced certification feature. The provenance graph is expressed in PROV-JSON format (the JSON serialization of W3C PROV-O) and is generated per response, not per dataset. A downstream consumer who needs to trace the provenance of a specific response can request its PROV graph from the enrichment layer using the response's stable identifier.

The provenance graph for a single response contains at minimum: the response entity, the collection activity, the form tool agent, and the `prov:wasGeneratedBy` and `prov:wasAssociatedWith` relations connecting them. It does not contain provenance for prior reporting periods or for other responses; those graphs are separate artifacts.

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 0.1.1 | 2026-06-08 | Conformance-threshold rename formalized and Frame Language own-voice pass applied. The machine annotation key `x-walkri-compliance-threshold` is now `x-walkri-conformance-threshold` and the display name is "Conformance Threshold" throughout, completing the WALKRI element rename (matching the JSON schemas at @0.2.1); this is a breaking key rename for any tool reading the old annotation. Six own-voice watchlist terms recast: "compliance" with a third-party standard to "conformance"; "governs/governing/governed" to "specifies/applies to/applied to"; the "enforcement mechanism" gloss to "implemented by". No field, requirement, or wire format changed beyond the documented annotation-key rename; naming and own-voice only. |

---

*End of WALKRI Interface Specification v0.1.1*
