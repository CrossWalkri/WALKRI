---
title: WALKRI Assessment Rubric
version: 0.1.4
date: 2026-06-08
license: CC0
status: Working draft. Companion to WALKRI-standard-0_1_0.md.
---

# WALKRI Assessment Rubric

Version 0.1.4 | 2026-06-08 | CC0

---

## Part 1: How to Use This Rubric

This rubric translates the standard's requirements into specific questions with pass/fail/override logic. Three categories of users apply it: WALKRI auditors conducting formal certification assessments, self-assessment practitioners reviewing their own forms before seeking certification, and AI-assisted audit tools implementing the WALKRI Audit Tool described in Part IX of the standard.

The rubric is organized around two assessment contexts. The distinction between them determines what an auditor does with findings, not how the findings are generated.

**Pre-publication audit** assesses fields before they are shown to applicants. This is the pre-publishing quality gate described in Part IV of the standard. Findings at this stage are actionable: a blocking failure must be resolved or overridden before the form is published. An advisory failure should be resolved but does not prevent publication if documented. Pre-publication audit is the primary use case for this rubric; it is when findings can still change the instrument.

**Post-publication audit** assesses fields retrospectively to produce a conformance record. This is the audit conducted when seeking WALKRI certification for a form that was already published and used. The auditor applies the same questions, but the findings inform the conformance record rather than the form design. Blocking failures in a post-publication audit are recorded as unresolved conformance gaps; they downgrade or preclude certification at the relevant tier. The findings also feed the remediation plan for the next form version.

In both contexts, the auditor works field by field. Each field receives an independent assessment.

---

## Part 2: Criterion Specification Assessment

Part 2 covers the five criterion specification requirements from Part III of the standard. These requirements apply at the field design stage and are assessed against the field specification document, not against applicant responses. The auditor is asking: is this field specification complete enough to support consistent interpretation by applicants and reviewers?

The requirements must be assessed in the order presented. Criterion intent is assessed first because its absence makes all subsequent assessments meaningless: without a criterion intent, there is no basis for evaluating whether the operational definition, response form, evidence form, or conformance threshold are appropriate.

### 2.1 Criterion Intent

**Assessment Question:** Is there a plain-language statement of what this field measures that is distinct from the field label?

| Outcome | Description |
|---|---|
| Pass | The criterion intent names the specific condition, behavior, or fact being measured. It is written in terms different from the label. A reviewer who only read the criterion intent statement could describe what would constitute a true response without referring to the label. |
| Fail | The criterion intent is absent, or it restates the label in different words without adding specificity. Example of a failing criterion intent for a field labeled "Community Engagement": "This field measures the organization's community engagement activities." This restates the label; it adds no measurement specificity. |

**Override Condition:** Not applicable. Criterion intent is always blocking. A field without a criterion intent cannot be assessed on any other dimension because there is no measurement claim against which to evaluate the remaining elements. If criterion intent is absent, the auditor stops the assessment for that field and returns it for remediation before continuing.

**Status:** Blocking. No override is available.

---

### 2.2 Operational Definition

**Assessment Question:** Does the operational definition contain inclusion criteria, exclusion criteria, a unit of analysis, and at least one edge case determination?

| Outcome | Description |
|---|---|
| Pass | All four elements are present. Inclusion criteria specify what qualifies as a valid response. Exclusion criteria specify what does not qualify, with enough specificity that a reviewer could classify an ambiguous response without seeking additional guidance. The unit of analysis is stated (e.g., "one instance equals one unique community member, not one interaction"). At least one edge case is named and resolved. |
| Fail | Any one of the four elements is absent. The most common failure: inclusion criteria are present but exclusion criteria are absent. Without exclusion criteria, the boundary of what counts is undefined; all ambiguous responses default to inclusion, which inflates the field's apparent coverage and makes responses across applicants non-comparable. |

**Override Conditions, By Element:**

Exclusion criteria may be documented as intentionally empty where the auditor and field designer agree that genuinely nothing could fail to qualify as a response. This is rare. When claimed, the auditor records the design reasoning (not merely the assertion) in the conformance record. The absence of exclusion criteria is not self-evidently an intentional design choice; it must be argued and documented.

Edge case determination is advisory when the field has low ambiguity by design, meaning the inclusion and exclusion criteria together leave no plausible response in an undecided state. The auditor assesses whether this condition is met; they do not accept the designer's characterization without applying their own judgment.

**Status:** Blocking for criterion intent and inclusion criteria. Advisory for edge case determination where low-ambiguity conditions are documented.

---

### 2.3 Response Form

**Assessment Question:** Is the response form specified, and is the justification for that form documented?

| Outcome | Description |
|---|---|
| Pass | The response form is named using one of the recognized response types: single-select, multi-select, binary, numeric, text, URL, or composite. A written justification is given explaining why this form was chosen over the natural alternatives. The justification addresses whether the response type can capture the variance in the underlying construct that the criterion intent requires. |
| Fail | The response form is not specified, or it is specified without justification. Justification that only restates the form type ("we used single-select because respondents select one option") does not count; justification must address the measurement rationale. |

**A Failure The Auditor Must Specifically Flag:** Single-select response form applied to a criterion where the operational definition's inclusion criteria naturally admit more than one simultaneously true answer. This is a design error that produces artificially imprecise data by forcing respondents to compress multi-valued reality into a single option. It must be flagged with a description of which inclusion criteria produce the multi-value problem.

**Override Condition:** A mismatch between the preferred response form and the implemented form may be overridden where technical constraints of the form rendering platform prevent implementation of the preferred form. The constraint must be documented specifically: which platform, which constraint, which preferred form could not be used. A general claim that "the platform does not support it" without specificity is not sufficient for override.

**Status:** Response form name is blocking. Justification is advisory but should be flagged as a deficiency if absent, because an unjustified form choice cannot be audited for correctness.

---

### 2.4 Evidence Form

**Assessment Question:** Does the evidence form name a specific artifact or data point that satisfies the criterion?

| Outcome | Description |
|---|---|
| Pass | The evidence form names a concrete artifact that an independent reviewer could locate and assess without additional guidance from the respondent. Examples of passing evidence form specifications: "A LICENSE file at the root of the project repository containing an OSI-approved SPDX license identifier"; "An on-chain transaction hash resolving to a completed transfer on a named public ledger"; "A signed attestation document from a named third-party auditor conforming to the attestation template at [URL]." |
| Fail | The evidence form delegates verification to reviewer judgment without naming the artifact. Examples: "proof of open source license" without naming where the proof must appear or what form it must take; "documentation of impact" without specifying the document type, required content, or submission format; absent evidence form entirely. |

**Override Condition:** For qualitative or narrative fields where no artifact-based evidence is structurally possible, the auditor documents the verification method in lieu of an evidence form. The documentation must name the assessment criteria reviewers apply, the minimum threshold for a passing reviewer assessment, and whether the assessment is conducted by one or multiple reviewers. This override converts a nominally absent evidence form into a documented verification methodology. It is not a waiver of the verification requirement; it is a documented alternative implementation.

**Status:** Blocking for fields configured at third-party verifiable strength or above, as classified in the field specification. Advisory for fields configured at self-report level, where the absence of an independent artifact is an acknowledged design condition rather than an oversight.

---

### 2.5 Conformance Threshold (for fields referencing external standards)

**Assessment Question:** For each external standard referenced, does the field specification enumerate which components are required, what evidence satisfies each, and the minimum threshold for passage?

| Outcome | Description |
|---|---|
| Pass | All three elements are present for each external standard referenced: component enumeration, evidence specification per component, and minimum threshold for passage. The threshold is stated explicitly enough that two reviewers who had never discussed it would apply it consistently. |
| Fail | An external standard is named without component enumeration, or components are enumerated without evidence specification per component, or the minimum threshold is not stated. The most common failure: citing a multi-indicator external standard by name and treating the citation as a sufficient specification. Example: "Must qualify as a Digital Public Good" with no enumeration of which of the nine DPG Standard indicators apply, no evidence specification per indicator, and no minimum passage threshold. This is a label, not a criterion specification. |

**Override Condition:** Where an external standard has no published component structure (it is a genuinely binary pass/fail determination with no sub-indicators), the conformance threshold requirement is satisfied by specifying the evidence form for the binary determination. The auditor must verify that the standard is in fact binary with no sub-indicators, not merely that the field designer has treated it as binary for convenience.

**Status:** Blocking when any external standard is referenced in the field specification. Not applicable when no external standard is referenced, because this requirement does not apply to self-standing field specifications.

---

### Part 2 Summary Table

| Requirement | Assessment Question | Fail Threshold | Override Available | Status |
|---|---|---|---|---|
| Criterion intent | Is there a plain-language statement distinct from the label? | Absent or restates label | No | Blocking |
| Operational definition | Are all four elements present? | Any element absent | Yes, for exclusion criteria where intentionally empty; advisory waiver for edge case in low-ambiguity fields | Blocking (inclusion criteria); Advisory (edge case) |
| Response form | Is the form named and justified? | Form absent or unjustified | Yes, for platform constraint on preferred form | Blocking (form name); Advisory (justification) |
| Evidence form | Does it name a specific verifiable artifact? | Absent or delegates to reviewer judgment | Yes, for qualitative fields; documented verification method required | Blocking (third-party verifiable fields); Advisory (self-report fields) |
| Conformance threshold | Are components, evidence, and threshold specified per external standard? | Any element absent when external standard referenced | Yes, for binary-only standards | Blocking (when external standard referenced) |

---

## Part 3: Data Quality Standards Assessment

Part 3 covers the five data quality standards from Part V of the standard. These standards apply at two moments: as design requirements (the field specification should satisfy them before publication) and as reviewer-facing assessment questions (applied during gate review of submitted data). Pre-publication auditors apply the same questions prospectively, asking whether the field specification as designed would produce data that could pass these assessments.

A finding in Part 3 does not by itself fail a field at the specification stage, but recurring patterns across findings diagnose systematic gaps in the field specification. The connection between each data quality standard and the criterion specification requirement it most directly enforces is noted for each.

### 3.1 Validity

**Assessment Question:** Could an independent reviewer, given the stated source and construction methodology, confirm that this field measures what it claims to measure?

**Validity Finding:** The reported data is downstream of unmeasured confounders that were not disclosed in the evidence form or methodology. Alternatively, the completion criteria are insufficient to determine whether the stated obligation was met. Alternatively, the measurement instrument does not reach the granularity required by the claimed result (e.g., a field claiming to measure "depth of community co-design" via a single binary yes/no response).

**Connection To Specification:** A validity finding traces back to criterion intent (2.1). The logical chain from the evidence form to the result claimed in the criterion intent is missing or broken.

---

### 3.2 Integrity

**Assessment Question:** Does any evidence for this field's data originate from a source independent of the respondent?

**Integrity Finding:** All evidence originates from respondent-controlled systems with no independent corroboration. For fields specified at self-report level, this is an expected and documented design condition; the finding is informational, not disqualifying. For fields specified at third-party verifiable level or above, this is a gate failure: the evidence form required independent verification, and the submitted evidence does not provide it.

**Connection To Specification:** An integrity finding traces back to evidence form (2.4). The evidence form is where the source and verification pathway are specified; if the form specified independent verification and the submitted evidence bypasses it, the submitted evidence does not satisfy the field's requirements.

---

### 3.3 Precision

**Assessment Question:** Is the measurement or verification instrument precise enough to support the claimed result?

**Precision Finding:** Completion criteria are so vague that any response satisfies them, making it impossible to distinguish between respondents with meaningfully different characteristics. Alternatively, a quantitative claim is smaller than the variance of the measurement instrument (the claimed difference cannot be attributed to real differences given the instrument's resolution). Alternatively, a single-select categorical response is used to report a phenomenon the operational definition suggests is multi-valued, compressing real differences into artificial uniformity.

**Connection To Specification:** A precision finding traces back to response form (2.3). The response form determines the resolution of the measurement instrument; a precision failure is most often a response form mismatch that was not caught at the specification stage.

---

### 3.4 Reliability

**Assessment Question:** If this respondent submitted prior data for the same field using a different operational definition, measurement form, or completion criteria, is the change documented and the comparability of prior periods determined?

**Reliability Finding:** Different criteria or response forms were used in different reporting periods without documentation. The change may be visible (a new option was added to a dropdown) or invisible (the operational definition was updated without changing the field label). In either case, if the change is not documented with an assessment of its comparability implications, longitudinal comparison of the data is unreliable: apparent changes over time may reflect definition changes rather than real changes in the underlying population.

**Connection To Specification:** A reliability finding traces back to operational definition (2.2) and to the schema requirements in Part VII of the standard, specifically the comparability documentation obligation.

---

### 3.5 Timeliness

**Assessment Question:** Is the evidence current to the period being assessed?

**Timeliness Finding:** Evidence from a prior period is presented as current without a documented rationale for why prior-period evidence is representative of the current period. The field's evidence form specified a recency requirement and the submitted evidence does not meet it. Alternatively, the evidence form did not specify a recency requirement, and the submitted evidence is dated far enough before the assessment period that its currency is in reasonable doubt.

**Connection To Specification:** A timeliness finding traces back to evidence form (2.4). A timeliness failure at the data assessment stage is typically a design gap in the evidence form rather than a data submission error.

---

## Part 4: Certification Thresholds

### WALKRI Certification (Standard)

A form achieves Standard certification when all of the following conditions are met:

All blocking criterion specification requirements in Part 2 pass or have documented overrides for every field in the form. No field has an unresolved, undocumented blocking failure. Override documentation meets the requirements specified in Part 5 of this rubric.

No Integrity findings at third-party verifiable strength or above. A field configured at third-party verifiable level whose submitted evidence is entirely respondent-controlled, with no independent corroboration, is a gate failure for Standard certification.

Conformance threshold is specified for every external standard referenced across all fields in the form. A referenced external standard without a conformance threshold is a blocking failure under 2.5.

A form certified at Standard level is suitable for human-reviewed evaluation. Reviewers can apply the field specifications consistently, and the resulting data is attributable to real differences in the applicant population rather than to definitional ambiguity.

### WALKRI Certification (Enhanced)

A form achieves Enhanced certification when all Standard conditions are met, plus the following:

All five data quality standards from Part 3 are documented in the field specification itself, not only assessed at gate review time. The field specification for each field includes a prospective validity chain, an integrity disclosure (naming the evidence source and its relationship to the respondent), a precision assessment (justifying the response form's resolution against the decision the field is designed to inform), a reliability protocol (stating how changes to the field will be documented across reporting periods), and a timeliness specification (naming the recency requirement for evidence).

Provenance fields are complete per Part VII of the standard for every field in the form. This includes field creator identity, specification timestamps, WALKRI version, form tool identifier, and field specification version.

Downstream interface requirements are met: the field specifications produce output aligned with Croissant, FAIR, and W3C PROV as specified in Part VII of the standard and detailed in WALKRI-interface-specification-0_1_0.md.

A form certified at Enhanced level is suitable for AI-assisted evaluation and for ingestion by machine learning pipelines. Downstream data consumers can process the data without manual metadata reconstruction.

---

## Part 5: Override Documentation Requirements

An override converts a blocking failure into a documented conformance choice. An override is not a waiver: it does not eliminate the requirement or excuse the gap. It is a recorded decision that the certifying organization accepts responsibility for, with the reasoning and compensating approach visible in the conformance record.

Overrides are not available for all blocking failures. Part 2 of this rubric specifies which requirements admit overrides and under what conditions. An auditor may not authorize an override for a requirement marked as having no override available.

Override documentation must contain four elements. If any element is absent, the override is not valid and the underlying failure remains unresolved.

**The requirement that was not met.** State the specific requirement from Part 2 (e.g., "Operational definition: exclusion criteria absent") and the field to which it applies. A general statement that "the field does not fully meet the operational definition requirement" is insufficient; the specific missing element must be named.

**The reason it was not met.** State the category of reason: technical constraint, intentional design choice, or genuine impossibility. Then describe the specific circumstance. "Technical constraint" requires naming the constraint and the platform or system that imposes it. "Intentional design choice" requires stating the design reasoning, not merely asserting that a choice was made. "Genuine impossibility" requires a brief argument for why the requirement is structurally impossible for this field type.

**The compensating control or alternative approach taken.** State what has been done in lieu of meeting the requirement. The compensating control must address the same risk that the requirement was designed to address. An override with no compensating control is a documented gap, not a documented conformance choice; it may be recorded as such but does not achieve the same conformance status.

**The name or role of the person or organization making the override decision.** The override is a decision, and decisions have authors. An override without an identified decision-maker cannot be held accountable and is treated as unsigned.

Overrides are part of the conformance record and are visible to every party that receives the conformance record. A certifying organization that grants overrides liberally will produce a conformance record that reflects that pattern. Downstream data consumers and external auditors can assess the quality of a form's certification by reviewing the override record alongside the pass/fail record.

---

## Part 5: Identity Instrument Assessment (Section 3.7)

Part 5 covers the three identity instrument types from WALKRI Section 3.7 and the self-reference consistency requirement. These are assessed separately from the general criterion specification requirements in Part 2 because they operate at two levels: field-level (the identity declaration fields themselves) and application-level (the self-reference consistency check across all fields).

Identity instrument assessment applies only to programs using CROSS entry gates or any obligation standard that activates the organizational identity declaration requirement. Programs that do not activate this requirement do not need Part 5.

---

### 5.1 Legal Entity Instrument

**Assessment Question:** Does the legal entity field's specification require the legal name as registered, the jurisdiction, and a registration number or equivalent identifier, and does the operational definition explicitly exclude non-legal names?

| Outcome | Description |
|---|---|
| Pass | The criterion intent specifies that the field identifies the legal person or registered organization accountable for grant obligations. The operational definition includes: inclusion criteria requiring the name as it appears in the jurisdiction of registration, the jurisdiction itself, and a registration number or equivalent identifier where applicable. Exclusion criteria explicitly name the following as non-qualifying: project names, display names, brand names, GitHub organization names, and pseudonyms, unless any of these are also the applicant's legal name of record. |
| Fail | The criterion intent does not distinguish legal name from display name. The operational definition lacks explicit exclusion of non-legal identifiers. The field can be satisfied by a project name or brand name without requiring evidence that the name corresponds to a registered entity. |

**Override Condition:** Where no legal entity exists (individual applicants with no legal registration), the operational definition may be modified to require the individual's full legal name and a statement that no legal entity exists. The override must document what accountability mechanism substitutes for entity registration.

**Status:** Blocking. A legal entity field that does not distinguish legal identity from display identity is structurally unable to establish the accountability chain that continuation and redress provisions require.

---

### 5.2 Display Name Instrument

**Assessment Question:** Does the display name field require evidence of prior public use, and does the operational definition exclude names created specifically for the current application?

| Outcome | Description |
|---|---|
| Pass | The criterion intent specifies that the field identifies the publicly known name used consistently in prior communications. The operational definition requires at least one URL demonstrating prior public use of the display name (a prior grant application, a public repository, a published communication, or a program record). The exclusion criteria explicitly state that a name chosen specifically for this application with no prior public appearances does not satisfy the display name instrument. |
| Fail | The display name field accepts any self-assigned name without requiring evidence of prior use. No distinction is made between established public identities and names created for the current application. |

**Override Condition:** For new projects at the inception round, a display name with no prior use is structurally possible: the organization is genuinely new. The override documents the first-round status and notes that continuity of the declared display name will be assessed at continuation. The override is not available for applicants who claim prior work under a different identity; that situation activates the prior entity relationship instrument.

**Status:** Blocking when the program uses continuation gates or cross-round track record assessments. Advisory for inception-only rounds.

---

### 5.3 Prior Entity Relationship Instrument

**Assessment Question:** Where the application cites prior work as evidence, does the field specification require the entity under which that work was performed, the applicant's relationship at the time, and the current status of that relationship?

| Outcome | Description |
|---|---|
| Pass | The trigger condition is correctly specified: the instrument activates whenever prior work is cited, not only when an applicant voluntarily discloses a prior entity. The operational definition requires three elements for each cited prior work: the name of the entity under whose resources, governance, or employment the work was performed; the applicant's role in that entity at the time; and the current status of the relationship (active, departed, restructured). |
| Fail | The instrument is absent from the form entirely, or is present but lacks a trigger condition linked to prior work citation. The most common failure: the instrument is listed as an optional field that activates only when the applicant self-identifies a prior entity, rather than being required whenever the applicant cites prior work in any field. This allows applicants to cite organizational prior work while implicitly presenting it as their own independent contribution. |

**Override Condition:** Not available for blocking elements. The trigger condition (activates on citation of prior work) must be present.

**Status:** Blocking for the trigger condition. The prior entity relationship instrument's fundamental purpose is to surface the organizational context of cited prior work; a field that can be skipped despite the presence of cited prior work does not satisfy this purpose.

---

### 5.4 Self-Reference Consistency Check

The self-reference consistency check is an application-level audit step, not a field-level one. It is conducted after all field-level assessments are complete. The auditor scans the full application for every self-reference (every instance where the applicant names themselves, their organization, their project, or their prior work) and checks whether each self-reference resolves to one of the two declared identities: the legal entity or the display name.

**Assessment Question:** Does every self-reference across all fields in the application resolve to the declared legal entity name or declared display name?

| Outcome | Description |
|---|---|
| Pass | All self-references in the application resolve to one of the two declared identities. Variant forms (abbreviations, URL slugs, Twitter handles) that are clearly associated with the declared identities by cross-reference are acceptable. |
| Fail | One or more self-references name an entity, project name, or identity that does not correspond to either declared identity and has not been explained in the prior entity relationship instrument. Common failure pattern: an applicant's progress section refers to work performed under "Project X" while the legal entity field names a different organization and the display name field names a third identity, with no prior entity relationship instrument filed. |

**This check is always advisory at the field-specification stage** because inconsistency is an application-level pattern that cannot be detected from the field specification alone. It becomes blocking at the application review stage: a reviewer who finds unresolved self-reference inconsistencies must flag them before the gate assessment proceeds.

**Connection to WALKRI Data Quality Standards:** Self-reference inconsistency is an integrity failure (data quality standard 3.2 in WALKRI Part V): evidence collection is not separated from the entity that benefits, because the applicant's identity itself is unclear. An application with unresolved self-reference inconsistencies cannot satisfy the integrity standard at any gate.

---

### Part 5 Summary Table

| Instrument | Trigger | Key Specification Requirement | Status |
|---|---|---|---|
| Legal entity | Always required at entry gate | Explicit exclusion of non-legal identifiers; jurisdiction and registration ID required | Blocking |
| Display name | Always required at entry gate | Evidence of prior public use required; exclusion of application-created names | Blocking (continuation programs); Advisory (inception-only) |
| Prior entity relationship | Activated by citation of prior work in any field | Trigger condition linked to prior work citation, not self-disclosure; three elements per cited work | Blocking (trigger condition) |
| Self-reference consistency | Application-level, post-field-audit | All self-references resolve to one of the two declared identities | Advisory at specification; Blocking at application review |

---

## Part 6: Gate Declaration Instrument Assessment Questions (Section 3.8)

These assessment questions apply when evaluating field specifications that implement the five CROSS entry gate declaration instruments defined in WALKRI Section 3.8.

### Revenue Architecture Instrument Assessment

1. Does the field specification require the applicant to select from the four canonical types (grant-only, fee-for-service, commercial, hybrid) or does it accept free-text responses that cannot be consistently classified?

2. For programs that configure the revenue architecture instrument: does the specification activate the additionality boundary sub-field for commercial and hybrid types, or does it allow commercial and hybrid applicants to omit the additionality boundary statement?

3. Does the operational definition specify what evidence is required for commercial and hybrid declarations (named revenue sources, contracts, token contracts), or does it accept self-report without a verification path?

4. Does the evidence form specify where a reviewer can independently check the declared architecture (on-chain contract explorers, public pricing pages, disclosed investor relations), or does the field rely solely on applicant attestation?

5. Does the specification state what happens when a commercial or hybrid declaration is inconsistent with the applicant's concurrent funding disclosure, or does it leave that reconciliation undefined?

### Disbursement Authority Instrument Assessment

1. Does the field specification require one of the three canonical states (Individual, Collective, Delegated) or does it accept generic descriptions that cannot be consistently assessed?

2. For Collective state: does the specification require the multisig or governance contract address to be named so it can be resolved on-chain, or does it accept a description of the governance mechanism without a verifiable address?

3. For Delegated state: does the specification require both the receiving entity and the deploying entity to be named, or does it allow a single entity declaration that conceals the delegation?

4. Does the evidence form specify where a reviewer can verify the declared authority (legal registration records, on-chain multisig resolution, organizational bylaws), or does the field rely solely on self-declaration?

5. Does the specification state what is required when the disbursement authority address differs from the on-chain identity anchor declared in Field 6, or does it leave that reconciliation undefined?

### Continuity Capacity Instrument Assessment

1. Does the field specification require the named primary contributor to be identified explicitly, or does it accept organizational descriptions that do not name an individual?

2. Does the specification require an explanation for Single and Partial states (how would the project continue if the primary contributor were unavailable), or does it accept the state declaration without a continuity explanation?

3. Is the evidence form specific enough that a reviewer can independently verify whether the named primary contributor is the sole author of the primary deliverable (GitHub contribution history, commit authorship), or does the specification rely on self-report?

4. Does the specification note that Single continuity capacity is a risk factor affecting the sustainability stance assessment, or does it present all three states as equivalent for evaluation purposes?

### Obligation Fulfillment Record Instrument Assessment

1. Does the field specification clearly state the activation conditions (returning applicants, prior-work-citing applicants), or does it leave activation ambiguous?

2. Does the specification require a structured repeating unit per prior grant (granting program, grant period, committed deliverable, produced artifact with link, fulfillment state), or does it accept narrative that cannot be consistently assessed across the cohort?

3. Does the evidence form require publicly accessible links from sources outside the applicant's control, or does it accept applicant-generated documentation as sufficient?

4. Does the specification state what the evaluator does when the obligation fulfillment record does not mention a grant that the Attestation Corpus query reveals, or does it leave non-disclosure undiscussed?

5. Does the specification cover the three fulfillment states (fulfilled, partially fulfilled, unfulfilled) and state that non-disclosure of an unfulfilled prior obligation is treated more seriously than disclosure of the same, or does it treat all non-disclosures as equivalent?

### Development Stage Instrument Assessment

1. Does the field specification use the five-stage classification (proof of concept through retroactive recognition) or does it allow free-text descriptions that cannot be consistently compared across the cohort?

2. Does the specification require an explanation of why the declared stage is accurate, or does it accept the stage selection without justification?

3. Does the specification require at least one piece of independently verifiable evidence consistent with the declared stage (GitHub activity for Stage 1-2, usage data for Stage 2-3, dependency records for Stage 4), or does it accept self-attestation?

4. Does the specification include a consistency check between the declared stage and the obligation mode committed to (Stage 1-2 in a build-obligation round is consistent; Stage 4 in a build-obligation round requires explanation), or does it evaluate the stage declaration in isolation?

5. Where the program configures a target stage range: does the specification state what happens when an applicant's declared stage falls outside the range (configuration mismatch requiring funder review, not automatic gate failure), or does it treat out-of-range declarations as automatic failures?

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 0.1.4 | 2026-06-08 | Disbursement-authority Governed state renamed Collective (the "For Collective state" assessment guidance), completing the Governed-to-Collective rename. The version stamps in the frontmatter and heading, which had lagged at 0.1.2 behind the 0.1.3 changelog entry, are corrected. No assessment content changed; naming only. |
| 0.1.3 | 2026-05-23 | Primitive rename cascade applied. The "Governance Resilience Instrument Assessment" section is now the "Continuity Capacity Instrument Assessment". Question 4 updated to reference "Single continuity capacity" as a risk factor. The three-state vocabulary (Single, Partial, Resilient) is preserved. Historical changelog entry below retains the prior primitive name as it stood at the time of release. |
| 0.1.2 | 2026-05-18 | Section 3.8 assessment questions added: five instrument rubrics covering revenue architecture, disbursement authority, governance resilience, obligation fulfillment record, and development stage. Five questions per instrument following the criterion specification element assessment structure. |
| 0.1.1 | 2026-05-17 | Part 5 added: Identity Instrument Assessment. Assessment questions, pass/fail/override logic, and status for the legal entity instrument (5.1), display name instrument (5.2), prior entity relationship instrument (5.3), and self-reference consistency check (5.4). Summary table added. |
| 0.1.0 | 2026-05-15 | Initial draft. Five criterion specification assessment questions with pass/fail/override logic. Five data quality standards assessment questions. Certification thresholds for Standard and Enhanced. Override documentation requirements. |
