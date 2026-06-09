---
title: WALKRI-CROSS Boundary Specification
version: 0.1.2
date: 2026-05-18
license: CC0
status: Working draft. Governs the division of authority between WALKRI v0.1.4 and CROSS v0.3.7.
---

# WALKRI-CROSS Boundary Specification

Version 0.1.1 | 2026-05-17 | CC0

---

## Part 1: The Dividing Principle

CROSS owns the obligation architecture: it specifies what must be demonstrated, by whom, at which gate, and in which obligation mode. WALKRI owns the specification quality layer: it specifies how the fields and criteria collecting that demonstration must be defined so that the resulting data is valid, consistent, and auditable.

A CROSS gate says "provide an operational definition." WALKRI says what an operational definition must contain. CROSS says "reference an external standard." WALKRI says what a conformant external standard reference must include. CROSS says "the indicator must meet the data quality standards." WALKRI names those standards, defines their assessment questions, and states their failure modes.

WALKRI operates independently of CROSS. Any program that collects structured data can adopt WALKRI without CROSS. CROSS-conformant programs that have not achieved WALKRI certification for their fields meet CROSS's obligation architecture requirements but fail WALKRI's specification quality requirements. Both standards are required for a CROSS+WALKRI conformant program.

---

## Part 2: Section-by-Section Mapping

The table below maps every current CROSS v0.3.7 Part and subsection to one of four statuses.

**Status Definitions:**

- **Cross:** CROSS is the governing authority; WALKRI has no role in this requirement.
- **Walkri:** WALKRI is the governing authority; CROSS references WALKRI for this requirement.
- **Cross, References Walkri:** CROSS sets the obligation; WALKRI governs how it is implemented at the field level.
- **Split:** The obligation (what must be demonstrated) is governed by CROSS; the specification quality requirements (how fields and criteria must be defined to meet that obligation) are governed by WALKRI.

| Part / Subsection | Status | Notes |
|---|---|---|
| Part I: Independence and Suite References | CROSS | Pure CROSS obligation architecture; no specification quality content |
| Part II: Independent Obligation Dimensions (all dimensions except IP) | CROSS | Triggering logic and tier structure are obligation architecture |
| Part II: IP Ownership Declaration field quality | CROSS, REFERENCES WALKRI | The obligation to submit an IP ownership declaration stays in CROSS; field quality of that declaration is governed by WALKRI |
| Part III: Obligation Modes | CROSS | Mode declaration logic and diagnostic rules are pure obligation architecture |
| Part IV: Four gate types | CROSS | Gate existence, activation logic, and mode-specific entry requirements |
| Part IV: Pre-Award Indicator Confirmation | CROSS | Gate lifecycle management; the confirmation window and silence-as-confirmation rule are process obligations |
| Part IV: Evidence scope (four levels) | CROSS | What evidence is required at each scope level |
| Part IV: Outcome Verification with Counterfactual Reference | CROSS | The four required contract elements at counterfactual reference level are evidence obligations |
| Part IV: Evidence strength (four levels) | CROSS | How evidence is verified; the verification mechanism taxonomy |
| Part IV: Infrastructure declaration | CROSS | Funder-side process obligation; published before the round opens |
| Part IV: Proportionality | CROSS | Scaling logic calibrated by the Coordination Scaling Standard |
| Part IV: Cost-effectiveness for continuation | CROSS | Continuation criterion; obligation architecture |
| Part IV: External Standard References | WALKRI | URL, version anchor, scope, and conformance threshold protocol governed by WALKRI Part VI |
| Part IV: Gate Criterion Specification | WALKRI | The five criterion specification requirements (criterion intent, operational definition, response form, evidence form, conformance threshold) governed by WALKRI Part III |
| Part V: Indicator Specification - field list (what fields are required) | CROSS | The obligation to provide each named field is governed by CROSS |
| Part V: Indicator Specification - operational definition content requirements | WALKRI | Inclusion criteria, exclusion criteria, unit of analysis, and edge case determination governed by WALKRI Part III, Criterion 2 |
| Part V: Indicator Specification - construction methodology quality | WALKRI | Quality standards for construction and aggregation methodology governed by WALKRI |
| Part V: Indicator Specification - data source quality | WALKRI | Independence and corroboration requirements governed by WALKRI Integrity standard (WALKRI Part V) |
| Part V: Measurement form and evidence classification (three-axis) | CROSS, REFERENCES WALKRI | CROSS governs the three-axis classification (source type, measurement form, aggregation type); WALKRI's evidence form requirement (Part III, Criterion 4) governs how each axis is specified |
| Part V: On-chain execution and verification instruments | CROSS, REFERENCES WALKRI | The obligation to specify invariant, verification method, verification artifact, and failure surface is governed by CROSS; evidence form specification quality is governed by WALKRI |
| Part V: Sustainability and transition plan | CROSS | Obligation architecture; funder-activated optional field |
| Part VI: Concurrent Funding Disclosure | CROSS | Pure obligation; no specification quality content |
| Part VI-A: Scope Attribution and Outcome Credit | CROSS | Pure obligation; additionality declaration and outcome credit attribution are obligation requirements |
| Part IV: Organizational Identity Declaration (four required fields) | CROSS, REFERENCES WALKRI | CROSS governs the obligation to collect the organizational identity declaration at all entry gates; the field quality of the four declaration fields is governed by WALKRI Section 3.7 (applicant identity instruments). The entity boundary primitive (Primitives Foundation Layer 2) is the structural basis for this requirement. |
| Part IV: Prior Work Attribution Statement | CROSS, REFERENCES WALKRI | CROSS governs the obligation to file a prior work attribution statement when prior work is cited; field quality of the three required elements (entity of performance, relationship at time, current ownership) is governed by WALKRI Section 3.7 prior entity relationship instrument. |
| Part IV: Gate Record Legibility and Cross-Program Track Record | CROSS | Funder-side obligation to express gate determinations as publicly verifiable records; format is governed by Part I format agnosticism principle |
| Part IV: Round Specification Pre-commitment | CROSS | Funder-side option to publish a content-addressed commitment before the application window opens; format governed by Part I format agnosticism principle |
| Part IV: Sustainability Assessment at Continuation | CROSS | Three-position stance (sustained, conditional, dependent) required at continuation gate; pure obligation architecture |
| Part IV: Gate function (developmental vs. summative) | CROSS | Classification of gate character and resulting grantee rights; pure obligation architecture |
| Part IV: Reviewer Calibration | CROSS | Funder-side process obligation requiring calibration exercise with worked examples before any reviewer accesses live applications at independent review level or above |
| Part VII: Conflict of Interest Framework (three-tier structure) | CROSS | Pure obligation architecture; tier structure, web3-specific categories, and process requirements |
| Part VII: Organizational role conflict (Tier 2 addition) | CROSS | Disclosure requirement for reviewers holding roles in other organizations applying to the same round or recently funded; pure obligation architecture |
| Part VII: Funder-side consulting conflicts | CROSS | Disclosure and categorical bar for reviewers under paid consulting arrangements with the funder; pure obligation architecture |
| Part VII: Attestation integrity | CROSS | Prohibition on Tier 1-conflicted parties serving as attestors for gate evidence regardless of attestation format; pure obligation architecture. The format constraint (all formats equally affected) is governed by Part I format agnosticism. |
| Part VIII: Data Quality Standards | WALKRI | Validity, Integrity, Precision, Reliability, and Timeliness governed by WALKRI Part V; CROSS references WALKRI for assessment questions and failure mode definitions |
| Part IX: Grant Configurator | CROSS, REFERENCES WALKRI | CROSS governs the Grant Configurator as the funder onboarding instrument; WALKRI Standard certification is required for all fields it publishes |
| Part IX: Field clarity gate | WALKRI | The pre-publishing quality gate for underspecified fields is governed by WALKRI Part IV; CROSS references it |
| Part IX: Grantee Dashboard | CROSS | Implementation architecture |
| Part IX: Reviewers Dashboard | CROSS | Implementation architecture |
| Part IX: CROSS skill | CROSS | Implementation architecture |
| Part IX: Runbooks | CROSS | Implementation architecture |
| Part X: Companion Documents | CROSS | CROSS companion documents |
| Part IX-B: Program-Level Theory of Change Architecture | CROSS | ToC hierarchy, pathway registry, round linkage, field-level tagging, and portfolio analysis enablement are all obligation architecture. The underlying primitives (ToC hierarchy, pathway, theory layer, specification directionality, sustainability stance, portfolio analysis outputs) are defined in the Primitives Foundation Layers 6 and 7. |
| Part IX-B: Field-Level ToC Tagging (WALKRI Extension) | CROSS, REFERENCES WALKRI | CROSS defines the obligation and the tag structure; WALKRI governs the field specification quality for tagged fields through its criterion specification requirements |
| Part XI: Funder Obligations and Redress | CROSS | Pure obligation architecture; internal clarification, structured appeals, independent redress |
| Part XI: Structured Dataset Publication | CROSS, REFERENCES WALKRI | CROSS governs the obligation to publish a machine-readable structured dataset at round close; programs with WALKRI certification automatically satisfy the field-level metadata requirement because WALKRI-conformant fields carry the required schema documentation |
| Part XII: Institutional Framework Alignment | CROSS | Alignment documentation for OECD DAC, IRIS+, Logic Model, pluralistic framework, and DAOIP-5; pure cross-referencing content, no specification quality requirements |

---

## Part 3: CROSS Reference Points to WALKRI

CROSS references WALKRI at four locations. The following specifies what a conformant CROSS reference to WALKRI says at each location. Implementers consulting CROSS for the governed requirement should follow these references to the WALKRI standard.

**Reference Point 1: Gate Criterion Specification (CROSS Part IV)**

"Gate criteria in a CROSS-conformant round must meet WALKRI criterion specification requirements at Standard certification level or above (WALKRI-standard-0_1_0.md, Part III). A gate criterion that does not pass WALKRI audit before the round opens is a funder-side conformance failure."

**Reference Point 2: External Standard References (CROSS Part IV)**

"External standard references in a CROSS-conformant gate must follow the WALKRI External Standard Reference Protocol (WALKRI-standard-0_1_0.md, Part VI), including URL, version anchor, and conformance threshold specification."

**Reference Point 3: Operational Definition Requirements (CROSS Part V)**

"The operational definition must meet WALKRI requirements for inclusion criteria, exclusion criteria, unit of analysis, and edge case determination (WALKRI-standard-0_1_0.md, Part III, Criterion 2: Operational Definition)."

**Reference Point 4: Data Quality Standards (CROSS Part VIII)**

"CROSS-conformant indicators are assessed against the five WALKRI Data Quality Standards: Validity, Integrity, Precision, Reliability, and Timeliness (WALKRI-standard-0_1_0.md, Part V). Reviewers apply WALKRI assessment questions and failure mode definitions during gate assessment."

**Reference Point 5: Organizational Identity Declaration (CROSS Part IV)**

"The organizational identity declaration's four fields are applicant identity instruments under WALKRI Section 3.7 (WALKRI-standard-0_1_0.md, Section 3.7). WALKRI Section 3.7 specifies the criterion intent and operational definition for the legal entity instrument, the display name instrument, and the prior entity relationship instrument, and establishes the self-reference consistency requirement that applies across all fields in the application."

---

## Part 4: Dependency Direction

WALKRI does not reference CROSS. CROSS references WALKRI. This direction is intentional: WALKRI's specification quality layer must be portable to programs that operate under no external obligation standard at all. A program adopting WALKRI without CROSS uses WALKRI Part III directly as its specification authority, with no gate architecture, obligation mode, or evidence scope requirements implied.

A CROSS-conformant program that has not achieved WALKRI certification for its fields meets CROSS's obligation architecture requirements but fails WALKRI's specification quality requirements. Both standards are required for a CROSS+WALKRI conformant program.

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 0.1.2 | 2026-05-18 | Updated to CROSS v0.3.7 and WALKRI v0.1.4. New primitives coverage includes revenue architecture, disbursement authority, governance resilience, obligation fulfillment record, development stage, public benefit mechanism, and access condition. |
| 0.1.1 | 2026-05-17 | Updated to CROSS v0.3.3 and WALKRI v0.1.1. Twelve new rows added to the Part 2 mapping table covering additions since CROSS v0.2.4: organizational identity declaration and prior work attribution statement (both CROSS, REFERENCES WALKRI via Section 3.7); gate record legibility, round pre-commitment, sustainability assessment, gate function, and reviewer calibration (all CROSS); organizational role conflict, funder-side consulting conflicts, and attestation integrity from CROSS v0.3.3 Part VII (all CROSS); Part IX-B program-level ToC architecture (CROSS); Part IX-B field-level ToC tagging (CROSS, REFERENCES WALKRI); structured dataset publication (CROSS, REFERENCES WALKRI); institutional framework alignment (CROSS). Reference Point 5 added for Section 3.7 organizational identity declaration. |
| 0.1.0 | 2026-05-15 | Initial draft. Dividing principle: CROSS governs obligation architecture, WALKRI governs specification quality. Part 2 mapping table through CROSS v0.2.4. Four CROSS reference points to WALKRI (gate criterion specification, external standard references, operational definition requirements, data quality standards). Dependency direction: WALKRI does not reference CROSS; CROSS references WALKRI. |
