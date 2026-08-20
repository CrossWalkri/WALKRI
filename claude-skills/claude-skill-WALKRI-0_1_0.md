---
title: WALKRI Skill
version: 0.1.0
date: 2026-08-20
status: Procedural encoding of WALKRI v0.2.1 for AI-assisted specification and audit of measurement instruments at the point of data capture. Structured so a partial task can be received and completed correctly.
related_documents:
  - WALKRI-standard-0_1_0.md (internal v0.2.1)
  - machine-readable/ (the generated schema, Zod, and conformance shapes)
  - CRAFT v0.4.6 (github.com/CrossWalkri/craft), the chain standard WALKRI's instrument-facing conditions satisfy
  - ORE v0.1.2 (github.com/CrossWalkri/ORE), the paired standard grading the source that feeds the field
license: CC0 1.0
---

# WALKRI Skill

Invoke this skill before publishing any field, prompt constraint, rubric item, or extraction rule that will collect data a decision rests on, and when auditing an existing instrument for whether it is a measurement instrument or only a label. This is a procedural encoding of WALKRI (Working Architecture for Legible, Knowable, Reliable Instrumentation) v0.2.1, the field-level instrument-quality standard.

WALKRI covers the point of data capture: whether a single captured datum is legible, knowable, and reliable. Its unit is the instrument, and a form field is its most familiar instantiation; a prompt constraint, a structured-output schema element, a rubric item, and an extraction specification are the same unit in other modalities, and the five requirements attach to all of them.

## The commitment that holds through every operation below

A field that satisfies all five requirements is a measurement instrument. A field that fails any one is a label, and a label collects variation in how respondents read it rather than variation in the population. Every procedure here is run before any respondent sees the instrument, because the specification is the data contract, and data collected under it is comparable across the cohort by construction rather than by cleanup afterward.

Three consequences hold throughout and are not negotiable per task:

- **Never treat a label as a specification.** A name is not a measurement claim. Until an instrument states what a true response tells you, distinct from its label, it has not begun to specify anything.
- **Never collapse the five statuses into one pass mark.** Conformance is the five per-requirement statuses; the minimum threshold (all five pass, overrides permitted where documented) is computed over them, and the conformance record carries the resolution each criterion element specifies, never a bare mark.
- **Never let an evidence form accept interchangeable types.** Standing, activity, outcome, planning, and financial-accountability evidence each prove a different thing. A criterion that accepts any of them for the same claim has specified nothing.

## Runtime Sequence

Identify which operation is requested and run the corresponding procedure in full.

1. **Instrument specification.** Run when designing a new instrument, before publication. Produce all five requirements. See Part I.
2. **Evidence form specification.** Run as part of instrument specification, or independently when a criterion needs its evidence named. See Part II.
3. **Conformance threshold specification.** Run when the instrument references an external standard. See Part III.
4. **Data-quality assessment.** Run when auditing whether a specified instrument will actually yield sound data. See Part IV.
5. **Dependency declaration.** Run once per instrument set, deriving the dependency graph and attesting it. See Part V.
6. **Conformance record production.** Run at the close of an audit, per form version. See Part VI.

---

## Part I: Instrument specification

An instrument is a measurement instrument only if it carries all five criterion specification requirements. Produce each explicitly; a missing one is not a soft gap, it is the difference between an instrument and a label.

**Criterion intent.** State in writing what the instrument measures, distinct from its label: what a true response tells you about the subject. The label "community engagement" can mean members reached, depth of co-design, geographic spread, or frequency of contact, and each is a different instrument. Without the written intent, reviewers cannot assess responses against a consistent standard.

**Operational definition.** Define each response category completely, with qualifying and non-qualifying examples for each. For a binary field, state what produces a yes and a no with at least one edge case. For a numeric field, the unit, the counting rule, and the boundary conditions. For a text field, the scope of acceptable content and the minimum content of a complete response. An option without a definition delegates interpretation to the respondent.

**Response form.** State the response type (single-select, multi-select, binary, numeric, text, url, or composite) with a written justification that it can capture the variance the criterion intent requires. Response type is a measurement decision, not a formatting one; the wrong type produces systematic error that cannot be corrected in analysis.

**Evidence form.** See Part II.

**Conformance threshold.** For any instrument referencing an external standard, see Part III. Where none is referenced, declare that explicitly with a reason rather than leaving the requirement silent.

---

## Part II: Evidence form specification

Name the evidence type required, its required content, and the independent access path. A criterion without a specified evidence form is an assertion without a verification path.

The five evidence types, each proving a different thing:

- **Standing evidence** attests to organizational standing, recognition, membership, or formal programme participation. Required elements: the attesting body with its domain standing, the scope specifically attested, the currency window, and a verification path a reviewer can confirm without contacting the applicant. Appropriate at entry gates; not sufficient at completion gates unless the criterion is about standing itself.
- **Activity evidence** attests that named activities occurred at a stated date, location, and scale. Required elements: date, location, activity type, a quantity metric, and the counting methodology for that metric. Two organizations counting by different methods produce non-comparable numbers under the same label.
- **Outcome evidence** attests that a named condition changed or a performance claim is verified, independently of the applicant's own report. Required elements: the measurement methodology at replication-sufficient detail, the baseline and post-intervention values, the measuring party (independent verification preferred), and the testing conditions for a technical claim. The only type that satisfies a completion gate for results.
- **Planning evidence** attests to future intent, procurement, or structural agreements. Required elements: the document type, date, parties, scope, and an explicit label that this is planning, not outcome, evidence.
- **Financial-accountability evidence** attests to how funding was deployed, by expenditure category. Required elements: the period, total deployed, expenditure by named category, the document type, and the verification path.

The criterion intent determines the type. A single criterion may require more than one type; name each separately with its required elements. Every access path must resolve without the reviewer logging in, requesting access, or contacting the applicant; evidence behind an authentication wall does not satisfy the requirement regardless of the document's strength.

---

## Part III: Conformance threshold specification

External standards are rarely binary. For any instrument that references one, specify three things: which components of the external standard apply to this criterion, what evidence satisfies each component, and the minimum threshold for passage, including which components are non-waivable.

Where the external standard maintains a registry, state whether registry membership is accepted as sufficient evidence of current qualification or independent assessment is required regardless of registry status. Registry membership records a past assessment, not current qualification; leaving this unstated produces the most common failure, reviewers checking the registry as a proxy for the assessment the funder never specified. A reference that names an external standard without this threshold is a label, not a criterion specification.

---

## Part IV: Data-quality assessment

Five data-quality standards apply to every instrument across all obligation modes. Each is an assessment question an auditor asks; each is a reader's judgment, not a schema check, and each connects to the criterion requirement it most directly enforces.

- **Validity.** Does the instrument have a documented logical chain from the evidence specified in the evidence form to the result claimed in the criterion intent? (Bears on criterion intent.)
- **Integrity.** Is evidence collection separated from the actor who benefits from a favorable outcome? (Bears on evidence form.)
- **Precision.** Can the instrument detect differences at the magnitude relevant to the decisions the data will inform? (Bears on response form.)
- **Reliability.** Is the methodology consistent across periods and reviewers? Where a conformance threshold exists, a calibration record with at least two clearly-passing, two clearly-failing, and one borderline worked example is part of the specification. (Bears on operational definition.)
- **Timeliness.** Is the evidence current to the decision cycle for which the data is collected? (Bears on evidence form.)

---

## Part V: Dependency declaration

A form's instruments may carry conditional logic: one instrument's relevance depends on another's response. Derive the dependency graph mechanically from the instrument set's own formal logic, attest it, and carry it in the conformance record. An instrument with no dependency edges declares its independence explicitly (the Declared-Absent value); it does not fall silent. A certified form that contained conditional logic the certification never assessed has a soundness hole, and this declaration closes it.

---

## Part VI: Conformance record production

Certification is per form version, not per organization. A change to any field definition triggers re-audit for that field; unchanged fields retain their status. Produce a conformance record carrying:

- The audit date (ISO 8601), the WALKRI version applied, and the form version audited.
- For each instrument: the field name, the field specification version, and the pass, fail, or override status of each of the five requirements.
- For each override: the flag text, the justification, and the name or identifier of the person who authorized it. An override without all three is an unresolved flag.
- For each instrument: the dependency declaration, or the Declared-Absent value where independent.
- For each instrument, when WALKRI operates inside an evaluation chain: the chain condition it serves (its layer attribution), or the Declared-Absent value where WALKRI is used standalone. Carried this way, the record recomposes upward into condition-satisfaction evidence, with the resolution each criterion element specifies rather than a bare pass mark.

A field passes only if all five requirements pass; four of five produces a flag that must be resolved or overridden with documentation. A form with unresolved, undocumented flags cannot be certified.

---

## Relations to the rest of the corpus

**CRAFT** is the meta-standard for evaluation chain legibility. WALKRI's content descends from the Precision-First Design Standard, not from CRAFT; its relation to CRAFT's instrument-facing conditions (Condition 2 on the operational-definition side, Condition 3 valid measurement instruments, Condition 4 pre-specified criteria) is conformance: WALKRI satisfies them rather than inheriting them, which is why it states each requirement with no CRAFT present and is portable across domains. WALKRI is CRAFT's sister at the field level, not a domain application of it. The canonical statement of the relationship is the interaction-architecture document; route relationship questions there rather than re-deriving them.

**Composition with a domain standard.** A domain application (CROSS for grants) sets the gates a submission must pass; WALKRI sets what each instrument inside those gates must satisfy. The dependency runs one way: a domain application references WALKRI, and WALKRI never references a domain application.

**ORE** is the paired standard at the same boundary. WALKRI grades the field, asking whether two independent readers would collect the same thing from the definition. ORE grades the source that feeds the field, asking how much of its reliability can be seen. A record can fail at either, and neither substitutes for the other.

**Precision-First Design Standard.** Every criterion requirement is held to operational definability. A requirement two independent auditors cannot reproduce from the specification is a precision deficit, not a matter of judgment.

## The machine-readable layer

`machine-readable/dist/walkri.schema.json` (JSON Schema 2020-12) and `machine-readable/dist/walkri.zod.ts` (Zod) validate a specified instrument's structure. The schema enforces the shape (all five requirements present, an evidence form naming a taxonomy type with an access path, a conformance threshold that names its components where an external standard is referenced, a dependency declaration, and no overall pass mark). It does not decide the judgment obligations (whether the criterion intent is a genuine measurement claim, whether the operational definition constrains interpretation, and the five data-quality assessments). `machine-readable/src/walkri-register.yaml` marks each obligation as shape, judgment, or mixed; do not report a schema pass as full WALKRI conformance.
