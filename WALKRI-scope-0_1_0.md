---
title: WALKRI - Working Architecture for Legible Knowledge Intake
version: 0.1.1
date: 2026-06-13
status: Scope document. Pre-draft. Not yet a specification.
companion_standard: CROSS v0.3.7 (github.com/durgadasji/CROSS)
brand: CROSS+WALKRI
license: CC0 (intended)
---

# WALKRI - Working Architecture for Legible Knowledge Intake

Scope Document, version 0.1.1 | 2026-06-13

---

## 1. Purpose

WALKRI (Working Architecture for Legible Knowledge Intake) is a standard for designing and auditing structured intake forms so that the data collected at the point of capture is operationally precise, comparable across programs, and fit for downstream analysis. The core problem it addresses is not form design aesthetics or user experience: it is epistemic quality at the point of capture. A form that collects answers to imprecisely defined questions produces data that cannot be trusted, compared, or used as evidence for anything. This failure happens upstream of any analysis; no pipeline, dashboard, or artificial intelligence layer can correct it after the fact.

The typical failure mode is familiar to anyone who has administered a grants round. A funder publishes fields with labels and no definitions. "Contributions" appears as a dropdown with options that are never explained. "Qualifies as Digital Public Good" appears as a checkbox with no specification of which of the nine Digital Public Good indicators apply, what evidence satisfies each, or how a reviewer should interpret an affirmative response. Applicants fill these fields based on their own interpretation. Reviewers score them based on their own interpretation. The resulting dataset is a collection of answers to different questions labeled identically. WALKRI treats this as a preventable defect, not an acceptable default.

What WALKRI adds is a quality gate applied before a form is published, and an enrichment layer applied after responses are submitted. The pre-publishing gate asks whether each field has been defined precisely enough to produce reliable, comparable data. The post-submission enrichment layer adds provenance metadata and schema consistency records before data reaches downstream systems. Together these two interventions protect epistemic quality at the only moment it can be protected: the moment of capture.

---

## 2. Relationship to CROSS

CROSS (Common Reporting Outcome Standards Schema) and WALKRI operate at different layers of the same infrastructure stack, and each layer has a distinct function.

CROSS operates at the conceptual and protocol layer. It specifies what funded interventions must demonstrate, how funders configure gate criteria for their programs, and how grantees report results against those criteria. CROSS defines the world model: what counts as a valid entry specification, what obligation mode a round is configured for, what constitutes a change indicator versus a deliverable specification, and what evidence is required at each gate. CROSS says what the categories are and what the rules of evidence are.

WALKRI operates at the instrumentation and collection layer. It specifies how to collect evidence about that world model without corrupting it on intake. When CROSS requires a funder to define a gate criterion, WALKRI specifies how that criterion must be encoded in a form field to be answerable at all. When CROSS requires an applicant to report against an indicator, WALKRI specifies what form that indicator's evidence field must take so that responses are interpretable and comparable. WALKRI does not change what CROSS requires; it operationalizes the collection of it.

Below both standards sits a third layer: interoperability and provenance. WALKRI aligns its output formats with Croissant (the machine learning-ready dataset metadata standard from Google, Hugging Face, and Meta, published 2024), the FAIR principles (Findable, Accessible, Interoperable, Reusable), and the W3C Provenance Data Model. These are not dependencies: WALKRI produces data and metadata that conform to these standards, so that data collected through WALKRI-certified forms can enter any pipeline that consumes them.

WALKRI is portable. It was designed in the context of CROSS+WALKRI as a compound standard for grants programs, but WALKRI itself applies to any structured intake context: decentralized autonomous organization voting forms, evaluation workflows, public application intake, research survey instruments, or any setting where the quality of collected data determines the quality of downstream decisions. The precision obligations WALKRI enforces are not grants-specific. They are a general requirement for any form whose outputs will be used as evidence.

---

## 3. The Three-Stage Process

WALKRI structures its process in three stages: ideation, specification, and applicant guidance. Each stage produces a distinct artifact, and each artifact is a prerequisite for the next.

The ideation stage addresses what a funder actually needs to know before any field is created. This sounds obvious and is routinely skipped. Funders typically begin by designing fields, which forces them to make definitional decisions implicitly and inconsistently. Ideation makes those decisions explicit first. What question is this field trying to answer? What would a good answer look like? What would a bad answer look like? What is the minimum evidence that would let a reviewer distinguish between them? What are the failure modes of this field: what can applicants answer that looks correct but is actually uninformative? The ideation stage produces a criterion intent document: a plain-language record of what each field is for, what it is not for, and what the funder commits to knowing before encoding the field.

The specification stage encodes that intent as a precisely defined, validated field that meets WALKRI criterion specification requirements. A WALKRI-conformant field has five required elements: a criterion intent statement derived from the ideation stage, an operational definition with positive and negative examples, a justification for the response form chosen (why a dropdown versus a free-text field versus a number, and what that form can and cannot capture), an evidence form specification (what kind of evidence a valid response would contain), and a conformance threshold for any field that references an external standard. The specification stage produces a WALKRI schema: a set of field definitions in JSON Schema format that encodes all five elements as machine-readable metadata alongside the field validation rules.

The applicant guidance stage translates the specification into language that helps applicants understand what good data looks like for each field. This is not marketing copy or instructions on how to fill out the form. It is a precision document: for each field, it states what the funder is trying to learn, gives a worked example of a response that would satisfy the criterion, gives a worked example of a response that would fail the criterion and why, and names the evidence the applicant should be drawing on. The applicant guidance stage produces a field-level guidance document that is published alongside the form.

---

## 4. Technical Architecture

WALKRI's native format is JSON Schema. JSON Schema is the open standard that underlies all major form tools (Fillout, Jotform, Typeform, Airtable, Google Forms, and others). Every major form platform either exports to JSON Schema, consumes JSON Schema for field validation, or operates an internal representation that is isomorphic with it. By operating at the JSON Schema layer, WALKRI remains platform-independent: its output is a portable, version-controlled, human-readable schema that any form tool can ingest as a rendering instruction.

WALKRI's two operational moments in a form's lifecycle are pre-publishing and post-submission. The pre-publishing quality gate takes a draft JSON Schema and audits each field against WALKRI criterion specification requirements. It checks whether each field has a criterion intent statement, an operational definition, a response form justification, an evidence form specification, and a conformance threshold where applicable. Fields that fail the audit are flagged with the specific requirement they are missing. The output of the quality gate is either a WALKRI-certified schema (with the certification recorded as metadata in the schema file) or a failure report. A form is not WALKRI-certified until every field passes.

Post-submission enrichment is delivered via webhook. All major form tools support outbound webhooks on submission: when a response is submitted, the tool sends the response payload to a specified endpoint. WALKRI's webhook processor receives the response, adds provenance metadata (submission timestamp, schema version at time of submission, field-level certification status, hash of the schema the response was validated against), and writes a schema-consistent record to the configured downstream system. This means that the downstream data store receives not just the applicant's answers but a provenance record that ties each answer to the exact field definition it was answering at the time. Schema changes after submission do not corrupt earlier records.

Form tools are interchangeable rendering layers in this architecture. WALKRI does not care which form tool a program uses. It speaks the open formats all tools share, and it does its work at the layers (pre-publishing schema, post-submission webhook) that all tools expose. Migrating from one form tool to another does not invalidate a WALKRI-certified schema; it only requires re-rendering the schema in the new tool's interface.

Downstream alignment with Croissant means that WALKRI-certified datasets can be registered in the Hugging Face datasets ecosystem and consumed by machine learning pipelines without additional curation. Alignment with FAIR principles means that every dataset produced through a WALKRI-certified form is Findable (the schema includes metadata sufficient for indexing), Accessible (data can be retrieved through open protocols), Interoperable (data uses standard vocabularies and formats), and Reusable (the provenance record documents conditions for reuse). Alignment with the W3C Provenance Data Model means that the chain from field definition to applicant response to downstream record is formally documented and auditable.

---

## 5. The Bidirectional Precision Principle

CROSS version 0.2.4 encodes the Bidirectional Precision Principle: the precision obligations a funder imposes on applicants run in both directions. A funder that requires applicants to specify operational definitions, measurement forms, evidence forms, data sources, and construction methodologies for their outcome indicators is making an implicit claim: that these elements of precision are what make data trustworthy. The Bidirectional Precision Principle holds that the funder's own fields and criteria must meet the same standard.

WALKRI operationalizes this principle at the field level. Every field in a WALKRI-certified form must carry five elements, corresponding exactly to the precision requirements CROSS places on applicant indicators.

The first element is criterion intent: a statement of what the field is designed to learn and what it is not designed to learn, in terms a reviewer could apply consistently.

The second element is an operational definition with examples. The definition must be specific enough that two independent reviewers applying it to the same response would reach the same conclusion. A definition that would allow reviewers to disagree is not operational. Positive examples (responses that satisfy the criterion) and negative examples (responses that appear to satisfy the criterion but do not) are required components.

The third element is response form justification: an explicit statement of why the chosen response form (dropdown, number, date, free text, multi-select, file upload) is the appropriate form for this criterion, what it can capture, and what it cannot capture. This prevents the common failure of encoding a continuous variable as a dropdown with four categories, losing the variance that makes the data useful.

The fourth element is evidence form specification: a description of what kind of evidence a valid response would draw on. For a field asking about prior grant funding, valid evidence might be a list with funder names, amounts, and dates. For a field asking about codebase activity, valid evidence might be a repository link with a specified lookback period. Naming the evidence form makes reviewer judgment consistent and tells applicants what to prepare.

The fifth element is conformance threshold, required for any field that references an external standard or certification. If a field asks whether a project qualifies under an external framework, the field must specify which criteria of that framework apply, what evidence satisfies each, and what minimum threshold constitutes conformance. A checkbox labeled with the name of a standard, with no specification of what the checkbox means, fails this requirement.

---

## 6. What WALKRI Does Not Do

WALKRI is a standard for field specification and a quality gate for form schemas. It is not a form builder, and it does not occupy any part of the form builder's role.

WALKRI does not render forms to users. The applicant-facing form is always produced by a form tool. WALKRI defines what the schema underlying that form must contain; the form tool decides how to present it.

WALKRI does not collect responses. Response collection is a form tool function. WALKRI's post-submission webhook receives a copy of each response to add provenance metadata, but the authoritative response record lives in the form tool's database.

WALKRI does not replace form tools. Programs using WALKRI still choose and operate their own form tool. WALKRI adds a layer before the form is published and a layer after responses are submitted; it does not substitute for anything in between.

WALKRI does not require any specific form platform. The JSON Schema and webhook architecture are supported by all major form tools. A program using Fillout can be WALKRI-certified. So can a program using Airtable, Typeform, Jotform, or a custom form built on a JSON Schema validator. The certification lives in the schema and the provenance record, not in the platform.

WALKRI also does not substitute for CROSS where CROSS applies. WALKRI handles the instrumentation of data collection. The question of what answerability a funded intervention must demonstrate, what gate criteria apply, and how results are reported is CROSS's domain. When used together, CROSS configures the obligation structure and WALKRI specifies the data quality of the forms that collect evidence for it.

---

## 7. Scope of Version 0.1.0

Version 0.1.0 of the WALKRI standard covers the specification layer: what a WALKRI-conformant field is, what a WALKRI-certified form is, how the three-stage process works, and what the technical architecture requires.

Specifically, version 0.1.0 defines the criterion specification requirements (the five required elements for every field), the three-stage process and the artifacts each stage produces, the JSON Schema output format and the metadata fields that carry criterion specification data, the webhook enrichment protocol and the provenance metadata fields it writes, and the certification record format that a WALKRI-certified schema must contain.

Version 0.1.0 does not cover the reference implementation product. The standard specifies what the quality gate must check and what the webhook processor must produce; it does not prescribe the software architecture of the tools that perform these operations. The reference implementation is a separate deliverable, to be scoped after the standard itself is stable.

Version 0.1.0 also defers pricing and commercial model, specific integrations with named form platforms (though it defines the interface requirements those integrations must meet), and the applicant guidance format beyond its required content (presentation decisions are implementation choices). Registry infrastructure for tracking which forms and datasets are WALKRI-certified is noted as a future requirement but not specified in this version.

---

## 8. Open Questions

Four design questions remain open at this stage of the standard.

The first concerns scope of the criterion specification requirement. The five required elements are clear for fields that collect substantive data about an applicant's work. They are less obviously applicable to administrative fields: contact information, wallet address, agreement to terms. The question is whether administrative fields require a reduced specification (perhaps only response form and evidence form), a full specification, or are simply out of scope for WALKRI certification requirements. The answer affects how certification is defined and how burdensome the standard is to apply.

The second concerns versioning of certified schemas across a program's history. When a funder revises a field definition between rounds, responses from the prior round were collected against a different definition. The provenance record handles this for individual responses, but the question of how to represent cross-round comparability in the dataset metadata has not been resolved. Croissant's dataset card format offers one approach; a WALKRI-specific versioning convention is another. The implications for multi-round analysis are significant enough that the standard should address this explicitly.

The third concerns the verification of ideation stage outputs before proceeding to specification. The ideation stage produces a criterion intent document that is a prerequisite for specification. At present, the standard does not specify a review mechanism: who decides whether a criterion intent document is sufficient to proceed? Options include self-certification by the funder, peer review by another certified practitioner, or a structured checklist that the standard itself provides. The choice determines how much institutional overhead the process requires and how well it scales to smaller programs.

The fourth concerns the relationship between WALKRI certification and the Croissant and FAIR downstream standards. WALKRI aligns with these standards but does not currently specify what minimum WALKRI conformance is required for a dataset to make a credible Croissant or FAIR claim. Drawing that line clearly would make the certification more legible to the research and machine learning communities WALKRI intends to serve, but it requires taking positions on those standards' interpretation that have not yet been worked through.

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 0.1.1 | 2026-06-13 | Frame Language own-voice vocabulary pass. Recasts: "accountability mode" recast to "obligation mode" and "the accountability structure" to "the obligation structure", using CROSS's own canonical Part III vocabulary; own-voice "WALKRI-compliant field" recast to "WALKRI-conformant field" (both occurrences), aligning with the corpus's established "conformant" usage; "what minimum threshold constitutes compliance" recast to "constitutes conformance"; "what accountability a funded intervention must demonstrate" recast to "what answerability ... must demonstrate"; the verb "enforces" recast to "specifies" in "WALKRI specifies the data quality of the forms". No field, conformance threshold, or mapping changed; vocabulary only. |
