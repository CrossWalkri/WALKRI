---
title: WALKRI Interface Specification
version: 0.1.2
date: 2026-06-13
license: CC0
status: Working draft. Companion to WALKRI-standard-0_1_0.md.
---

# WALKRI Interface Specification

Version 0.1.2 | 2026-06-13 | CC0

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

## Part 5: Dependency Edges and Conditional Logic

### 5.1 Why Edges Need Their Own Mapping

The WALKRI standard's Part III specifies the five criterion specification elements (criterion intent, operational definition, response form, evidence form, conformance threshold) for each instrument that a form presents. Those five elements describe the instrument as a node: what it asks, what its responses mean, what evidence it requires, what conformance threshold it carries. They say nothing about the edges between instruments, that is, the conditional relationships that decide whether an instrument is presented at all, what must be answered before its conformance threshold can be assessed, and in what order instruments resolve.

Every target format in this specification carries this edge information natively. JSON Schema carries it in the `if`/`then`/`else` and `dependentRequired` keywords; REDCap carries it in branching logic expressions; XLSForm carries it in `relevant` and `constraint` expressions; the artificial-intelligence side carries it in conditional structured-output schemas and in evaluation-pipeline stage dependencies. Until this Part, the interface specification mapped only the node elements and left the edges unmapped. That omission is a soundness gap. A WALKRI-certified form could carry conditional logic, such as a field that is hidden unless an upstream response takes a particular value, that the certification never assessed, because the certification only ever looked at instruments one at a time. A reader of the conformance record would have no way to tell that the form's behavior depends on relationships the record does not describe.

This Part closes that gap by specifying how the edge information is read out of each format so that a single dependency graph can be derived from it.

### 5.2 The Derive-and-Attest Principle

The dependency graph is not authored by hand. It is derived mechanically from the form's own formal logic, the designer attests to the derived graph, and the graph travels in the conformance record. One source of truth, which is the form logic itself; one derived artifact, which is the graph; one attestation over that artifact.

The reason for deriving rather than declaring is that the conditional keywords in every target format are themselves formal and machine-readable. JSON Schema conditionals are evaluated by any conformant validator. REDCap branching logic and XLSForm `relevant` expressions are evaluated by their respective engines on every form render. Because the logic is already formal, a second, hand-written set of dependency declarations would only restate it, and a restatement drifts: the form logic and the declaration fall out of step the first time either is edited without the other, and the conformance record then attests to something the form no longer does. Deriving the graph from the form logic removes that second copy. The designer does not write the edges; the designer reviews the edges the certification read out of the form and attests that they are the intended ones. An auditor holding the same form can regenerate the identical graph and check the attestation against it.

The graph has the following shape. Nodes are instruments, each identified by the field name or identifier the format already uses. Edges are typed, and three edge types are recognized:

- **Activation edges.** An upstream response value (or set of values) causes a downstream instrument to be presented or hidden. The edge records the upstream node, the downstream node, and the activating condition read from the format.
- **Assessment-dependency edges.** A downstream instrument's conformance threshold cannot be assessed until an upstream instrument resolves, because the downstream threshold is defined in terms of the upstream response. The edge records which upstream resolution the downstream assessment waits on.
- **Ordering edges.** One instrument must resolve before another for reasons the format expresses as a sequencing constraint rather than as an activation or assessment dependency.

The certification derives the typed edge set, the designer attests to it, and the attested graph is recorded alongside the per-field conformance entries described in Part 2.2. Because the graph is derived, the conformance record states the derivation source (the form artifact and its version) so that the regeneration is reproducible.

### 5.3 Form-Side Read-Out

This section specifies how the edge information is read out of each of the three form-side formats. In each case the read-out is mechanical: a defined traversal of the format's own conditional constructs yields the typed edges.

The syntaxes named here build on prior art in form and clinical-data interchange, and the read-out borrows the structure those syntaxes already define. The Clinical Data Interchange Standards Consortium Operational Data Model (CDISC ODM) expresses conditional presentation through its `ConditionDef` element, which names the condition under which an item or item group appears. The Health Level Seven Fast Healthcare Interoperability Resources standard (HL7 FHIR) expresses the same idea in the `enableWhen` element of a Questionnaire item, which names the upstream item, the operator, and the answer that enables the downstream item. JSON Schema conditionals (`if`/`then`/`else`) express it in pure schema terms. The read-outs below map each native construct onto the same typed-edge vocabulary so that a graph derived from a JSON Schema form, a REDCap form, and an XLSForm are directly comparable.

**JSON Schema: `if`/`then`/`else` and `dependentRequired`.** A JSON Schema `if`/`then`/`else` block names a condition over one or more fields (the `if` subschema) and a consequence (the `then` subschema, applied when the condition holds; the `else` subschema, applied when it does not). The read-out traverses every `if`/`then`/`else` block and reads the fields named in the `if` subschema as upstream nodes and the fields whose presence, requiredness, or permitted values change in the `then` or `else` subschema as downstream nodes. Where the consequence is that a downstream field becomes required or permitted, the edge is an activation edge with the `if` condition as its activating condition. Where the consequence changes a downstream field's permitted values or its conformance threshold in terms of the upstream value, the edge is an assessment-dependency edge, because the downstream conformance threshold cannot be assessed until the upstream value resolves. The `dependentRequired` keyword names, for a given field, the set of other fields that become required when the given field is present; each entry yields an activation edge from the named field to each dependent field, with the activating condition being the presence of the named field. Because `if`/`then`/`else` and `dependentRequired` are evaluated by any conformant JSON Schema validator, the derivation needs no logic beyond a schema walk.

**REDCap branching logic.** REDCap attaches a branching-logic expression to a field; the field is shown only when the expression evaluates true. The expression references other fields by their REDCap variable names and combines them with comparison and boolean operators. The read-out parses each branching-logic expression, reads every field referenced in it as an upstream node and the field carrying the expression as the downstream node, and emits an activation edge whose activating condition is the parsed expression. Where REDCap calculated fields or validation ranges define a downstream field's permitted values in terms of an upstream field, the read-out emits an assessment-dependency edge instead, on the same basis as the JSON Schema case: the downstream threshold waits on the upstream resolution.

**XLSForm `relevant` and `constraint` expressions.** XLSForm carries two relevant expression columns. The `relevant` column holds an expression that decides whether a question is presented; the `constraint` column holds an expression the response must satisfy to be accepted. The read-out parses each `relevant` expression, reads the questions it references as upstream nodes and the question carrying the expression as the downstream node, and emits an activation edge whose activating condition is the parsed `relevant` expression. It parses each `constraint` expression and, where the constraint references another question (so that the acceptable response to one question depends on the response to another), emits an assessment-dependency edge from the referenced question to the constrained question. Where a `relevant` or `constraint` expression encodes only a sequencing requirement that is neither an activation nor an assessment dependency, the read-out emits an ordering edge.

In all three form-side formats the traversal is deterministic: the same form yields the same typed edge set every time, which is what makes the derived graph attestable and regenerable.

### 5.4 Artificial-Intelligence-Side Read-Out

The artificial-intelligence modality carries edge information in two places, and both are read out into the same typed-edge vocabulary as the form side.

**Structured-output schemas (conditional and required-field structure).** When an instrument is presented to a language model rather than to a human form-filler, its responses are captured against a structured-output schema, which is itself most often a JSON Schema. That schema carries the same conditional constructs as the form-side JSON Schema case: `if`/`then`/`else`, `dependentRequired`, and per-property requiredness. The read-out is the same schema walk specified in Part 5.3 for JSON Schema, producing activation edges where a response value makes a downstream field required or permitted and assessment-dependency edges where a downstream field's permitted values or conformance threshold are defined in terms of an upstream field. The structured-output case therefore needs no separate parser; it reuses the JSON Schema read-out, and the edges it yields are comparable, node for node, with edges derived from a human-facing form built on the same schema.

**Evaluation-pipeline dependency chains.** An artificial-intelligence evaluation pipeline runs instruments as stages, and one stage's output frequently gates a later stage: a later stage is run only when an earlier stage produced a particular output, or a later stage's conformance threshold is defined in terms of an earlier stage's result. The read-out traverses the pipeline definition (the declared sequence of stages and the conditions on each stage), reads each stage as a node, and emits an activation edge wherever a stage is run conditionally on an upstream stage's output, with the activating condition being the gating condition declared on the stage. Where a later stage's conformance threshold is defined in terms of an earlier stage's result rather than merely being run conditionally, the read-out emits an assessment-dependency edge, because the later threshold cannot be assessed until the earlier stage resolves. Where the pipeline declares a stage order that is neither a conditional run nor a threshold dependency, the read-out emits an ordering edge. As with the form side, the pipeline definition is the single source of truth: the graph is derived from it, the designer attests to the derived graph, and an auditor holding the same pipeline definition regenerates the identical edge set.

### 5.5 What the Conformance Record Carries

The derived dependency graph is recorded alongside the per-field conformance entries specified in Part 2.2. For each form or pipeline, the conformance record carries: the typed edge set (each edge naming its upstream node, downstream node, edge type, and the condition read from the format); the derivation source (the form artifact or pipeline definition and its version, so the derivation is reproducible); and the designer's attestation that the derived edges are the intended ones. The graph does not introduce a new authored artifact that could drift from the form logic; it is a read-out of that logic, recorded so that the conformance record covers the form's conditional behavior and not only its instruments taken one at a time. An auditor regenerates the graph from the named derivation source and checks it against the attested edge set.

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 0.1.2 | 2026-06-13 | Added Part 5 (Dependency Edges and Conditional Logic). The prior parts mapped instrument nodes only; nothing mapped the edges between instruments (which upstream response activates or hides an instrument, what must resolve before a conformance threshold is assessable, ordering constraints), so a certified form could carry conditional logic the certification never assessed. Part 5 closes that soundness gap on the derive-and-attest principle: the dependency graph is derived mechanically from the form's own formal logic, the designer attests to the derived graph, and the graph travels in the conformance record as one source of truth that an auditor can regenerate. The new Part specifies the read-out for the form side (JSON Schema `if`/`then`/`else` and `dependentRequired`; REDCap branching logic; XLSForm `relevant` and `constraint` expressions) and for the artificial-intelligence side (conditional structured-output schemas; evaluation-pipeline stage dependencies), crediting CDISC ODM `ConditionDef`, HL7 FHIR `enableWhen`, and JSON Schema conditionals as prior art for the syntaxes. Normative-content addition; no existing field, requirement, or wire format changed. Filename retained at the `0_1_0` series stem (the established convention in this file's history, where the 0.1.1 internal bump likewise did not rename the file) to preserve seven live cross-references across the corpus; see the report note. |
| 0.1.1 | 2026-06-08 | Conformance-threshold rename formalized and Frame Language own-voice pass applied. The machine annotation key `x-walkri-compliance-threshold` is now `x-walkri-conformance-threshold` and the display name is "Conformance Threshold" throughout, completing the WALKRI element rename (matching the JSON schemas at @0.2.1); this is a breaking key rename for any tool reading the old annotation. Six own-voice watchlist terms recast: "compliance" with a third-party standard to "conformance"; "governs/governing/governed" to "specifies/applies to/applied to"; the "enforcement mechanism" gloss to "implemented by". No field, requirement, or wire format changed beyond the documented annotation-key rename; naming and own-voice only. |

---

*End of WALKRI Interface Specification v0.1.2*
