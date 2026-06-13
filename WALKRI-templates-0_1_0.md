---
title: WALKRI Templates
version: 0.1.6
date: 2026-06-13
license: CC0
status: Working draft. Companion to WALKRI-standard-0_1_0.md.
---

# WALKRI Templates

Version 0.1.6 | 2026-06-13 | CC0

These templates correspond to the four artifacts produced by the WALKRI three-stage process: the Ideation Record (Stage 1), the WALKRI Field Specification (Stage 2), the Applicant Guidance Document (Stage 3), and the WALKRI Audit Report (conformance record). Each template includes a brief description and field-by-field instructions. Placeholder text appears in [brackets].

Read the standard before using the templates; the templates do not repeat the rationale for each requirement.

---

## Template 1: Ideation Record

### What it is and when it is used

The Ideation Record is the Stage 1 output. It is an internal document, not shared with applicants, that captures the question-holder's information needs before any field is designed. Each entry names one information need, traces it to a specific decision, and states the failure mode if the data turns out to be missing or imprecise.

Each entry in the Ideation Record becomes the source for one field specification in Stage 2. A Stage 2 field that cannot be traced to an Ideation Record entry lacks a documented rationale and cannot be certified.

Produce one Ideation Record per program or form version. Add entries until every decision the form is meant to support has at least one corresponding information need.

---

```
IDEATION RECORD

Program or round name: [Full name of the program, grant round, or intake process]

Ideation date: [YYYY-MM-DD]

Completed by: [Name or role of the question-holder]

---

INFORMATION NEED [Repeat this block for each information need]

Information need:
  We need to know: [Plain language statement of what the program needs to know.
  Example: "We need to know whether the applicant's project repository is publicly
  accessible under an approved open license at the time of application."]

Decision this data will inform:
  This tells us whether to: [Plain language statement of the decision.
  Example: "This tells us whether to advance the applicant past the open licensing
  gate criterion or to flag the application for remediation."]

Failure mode if data is missing or imprecise:
  Without this, we will: [Plain language statement of the consequence.
  Example: "Without this, we will have no consistent basis for distinguishing
  applicants who hold qualifying licenses from those who do not, and reviewers
  will make the determination based on personal familiarity with license names
  rather than on verified evidence."]

Draft field label: [A working title for the field this information need will become.
  This is not the final label; it is a handle for use during Stage 2 specification.
  Example: "Open License Status"]

Notes on known complexity or edge cases: [Optional. Record anything that may
  complicate the field design: ambiguous cases, populations that don't fit the
  expected pattern, prior versions of this field that caused problems, or
  dependencies on other fields in the form.
  Example: "Projects that are transitioning from a proprietary license may have
  mixed licensing across repositories. We need to decide in Stage 2 whether the
  gate criterion applies to the primary repository only or to all repositories
  listed in the application."]

---

[Repeat INFORMATION NEED block as needed]
```

---

## Template 2: WALKRI Field Specification

### What it is and when it is used

The WALKRI Field Specification is the Stage 2 output and the central artifact of the entire process. One specification is produced per field. The specification contains all five criterion specification requirements from Part III of the WALKRI standard: criterion intent, operational definition, response form, evidence form, and conformance threshold.

The field specification structures everything downstream: it is the source for the Stage 3 applicant guidance, the artifact the WALKRI Audit Tool assesses, and the machine-readable definition that travels with the collected data. A field cannot be certified without a complete specification.

Produce one Field Specification for each information need in the Ideation Record. The criterion intent in Section B should be traceable directly to the corresponding Ideation Record entry.

---

```
WALKRI FIELD SPECIFICATION

=== SECTION A: IDENTITY ===

Field label: [The label applicants will see. Should be plain, direct, and consistent
  with the draft label from the Ideation Record unless the Stage 2 process produced
  a clearer formulation. Example: "Open License"]

Field version: [Increment each time this specification changes. Start at 1.0.
  Example: "1.0"]

Specification date: [YYYY-MM-DD]

Derived from ideation record: [Reference to the information need this field addresses.
  Include the program name, ideation date, and the plain language statement of the
  information need. Example: "Ideation Record, [Program Name], [YYYY-MM-DD]:
  'We need to know whether the applicant's project repository is publicly accessible
  under an approved open license at the time of application.'"]

Dependency declaration: [The edges this instrument carries to other instruments in
  the set, per Section 3.9 of the standard. Do not author these edges by hand from
  scratch; read them off the instrument set's own formal logic (in JSON Schema, the
  conditional keywords; in the form-rendering formats, the equivalent skip, branch,
  and ordering logic) and record what that logic actually carries for this instrument.
  If this instrument has no edges, the value is the single word: independent. This is
  the Declared-Absent convention and is the default for any instrument with no
  conditional, ordering, or cross-instrument logic. If this instrument has edges,
  record each of the following that applies:
    Activation conditions: [What upstream response makes this instrument appear or
      apply. Example: "Activates only when 'Revenue architecture type' is Commercial
      or Hybrid."]
    Assessment dependencies: [What must resolve before this instrument's conformance
      threshold can be assessed. Example: "Cannot be assessed until 'Development stage'
      resolves, because the stage determines the evidence threshold applied here."]
    Ordering constraints: [Any required order relative to other instruments.
      Example: "Must be presented after the legal entity instrument."]
    Cross-instrument consistency constraints: [Any value that must agree with another
      instrument's value. Example: "Declared revenue here must be consistent with the
      concurrent funding disclosure instrument."]
  Example for an independent instrument: "independent".]

=== SECTION B: CRITERION SPECIFICATION ===

--- B1: Criterion Intent ---

Criterion intent: [A written statement of what this field measures, distinct from
  its label. Answers the question: what does a true response to this field tell us
  about the applicant or subject? This is a measurement claim, not a label.
  Example: "This field measures whether the applicant's primary project repository
  carries a valid open license from the approved list at the time of submission.
  A passing response indicates that the code base is legally available for use,
  modification, and distribution by third parties under terms consistent with the
  program's open-source requirements."]

--- B2: Operational Definition ---

Inclusion criteria: [What counts as a valid response. Be specific enough that two
  independent reviewers would reach the same conclusion given the same evidence.
  Example: "A valid response is an SPDX license identifier (e.g., MIT, Apache-2.0,
  GPL-3.0-only) present in either a root-level LICENSE file or a clearly labeled
  license section of the README in the primary repository. The license must be
  listed on the approved license list at [URL], accessed [YYYY-MM-DD]."]

Exclusion criteria: [What explicitly does not count. List the most common
  near-misses and incorrect interpretations.
  Example: "The following do not satisfy this criterion: a license mentioned only
  in prose without an SPDX identifier; a license present only in a sub-directory
  or secondary repository; a license that is on the approved list but is applied
  to documentation only and not to the source code; a pending license application
  or statement of intent to apply a license."]

Unit of analysis: [What entity the response describes. Select: person / organization
  / repository / project / event / other. Example: "Repository (primary repository
  as identified in the application's project URL field)."]

Edge case determination: [At least one example of how an ambiguous case is handled.
  The resolution must be specified here, not left to reviewer discretion.
  Example: "If the applicant lists multiple repositories and only one carries a
  qualifying license, the response is 'No' unless the program has designated a
  single primary repository and that repository carries a qualifying license.
  Reviewers must not average or weight across repositories."]

--- B3: Response Form ---

Response form: [Select: single-select / multi-select / binary / numeric / text /
  URL / composite. Example: "binary"]

Response form justification: [Why this response type is appropriate for the
  criterion intent. The justification must address whether the response type
  can capture the variance in the underlying construct that the criterion intent
  requires. Example: "Binary is appropriate because the criterion intent is a
  gate criterion with two outcomes: the license criterion is satisfied or it is
  not. The decision the data informs (gate passage) requires only this distinction.
  A single-select with more options would imply gradations that this criterion
  does not actually assess."]

Options: [For single-select or multi-select fields only. List each option with its
  definition. Do not list options without definitions; undefined options are the
  primary source of operational definition failures in categorical fields.
  For binary fields, define the conditions for Yes and No instead.

  Yes: [Condition for Yes. Example: "The primary repository carries a valid
  SPDX-identified license from the approved list, present in a root-level LICENSE
  file or README license section, at the time of submission."]

  No: [Condition for No. Example: "The primary repository does not carry a
  qualifying license, or carries a license that is not on the approved list, or
  the license cannot be independently verified from the provided URL."]]

--- B4: Evidence Form ---

Evidence form: [The specific artifact that satisfies this criterion. For
  document-based evidence: document type, required content, and whether a link
  or upload is required. For quantitative evidence: data source, methodology,
  and time period. For external verification: verifying party, scope, and form
  of verification. Example: "A direct URL to the root-level LICENSE file or the
  README section containing the license text in the primary project repository.
  The URL must resolve to a publicly accessible page at the time of review.
  A screenshot or copy-paste of license text is not acceptable in place of a
  live URL."]

--- B5: Conformance Threshold (complete this section only if this field references
  an external standard) ---

External standard: [Name of the standard and its canonical URL.
  Example: "Digital Public Goods Standard, https://digitalpublicgoods.net/standard/"]

Version anchor: [Dated access record, version number, or content hash identifying
  the exact version consulted. Example: "DPG Standard v1.1.9, accessed 2025-11-01"]

Required components: [List each required sub-indicator or component of the external
  standard that applies to this field. Do not summarize; list each component
  separately so that the conformance threshold can be audited component by component.
  Example:
    Component 1: Indicator 2 - Use of Approved Open License
    Component 2: Indicator 3 - Clear Ownership (if applicable to this criterion)]

Evidence per component: [For each component listed above, state what specific
  evidence satisfies it.
  Example:
    Component 1 evidence: A clearly stated SPDX license identifier in the project
    repository's root-level LICENSE file or README. A reference to a license in
    prose text without an SPDX identifier does not satisfy this component.
    Component 2 evidence: A named entity (individual or organization) identified
    as the copyright holder in the LICENSE file or repository documentation.]

Minimum threshold: [State which components must be satisfied for passage, and
  whether any components may be satisfied via documented mitigation plans.
  Example: "Both components must be satisfied for gate passage. Neither is
  waivable. No mitigation pathway applies to this criterion."]

=== SECTION C: DATA QUALITY ASSESSMENT ===

Validity note: [How a reviewer confirms this field measures what the criterion
  intent claims it measures. Identify the logical chain from the evidence form
  to the result claimed in the criterion intent, and note any points where the
  chain could break.
  Example: "A URL pointing to a root-level LICENSE file with a valid SPDX
  identifier confirms that the license is applied to the repository's source code
  and is publicly visible. The chain breaks if the URL resolves but the file
  content has changed since submission; reviewers should check the URL at review
  time, not rely on the applicant's characterization of its contents."]

Integrity note: [The independent verification mechanism for this field. State
  whether this field relies on self-report, third-party verification, or an
  automatically verifiable artifact, and what the verification pathway is.
  Example: "This field is independently verifiable: the provided URL either
  resolves to a qualifying license or it does not. Reviewers do not depend on
  the applicant's characterization of the license. The only integrity risk is
  an applicant who applies a license after submission; timestamp comparison
  with the application date can mitigate this if repository commit history is
  available."]

Precision note: [The level of specificity required in a valid response, and
  whether the response form is fine-grained enough to support the decision
  this data informs.
  Example: "Binary precision is sufficient for a gate criterion. The decision
  (advance or flag) requires only a pass/fail determination. If the program were
  to introduce tiered licensing requirements in a future version (e.g., preferred
  licenses vs. acceptable licenses), the response form would need to be upgraded
  to single-select with defined tiers."]

=== SECTION D: APPLICANT GUIDANCE SUMMARY ===

[This section is the source material for the Stage 3 Applicant Guidance Document.
Derive the Stage 3 document from this section; do not introduce new definitional
content in Stage 3.]

Plain language explanation: [One sentence explaining what the field asks, written
  for an applicant who has not read the criterion specification.
  Example: "This field asks you to confirm that your primary project repository
  uses an approved open license and to provide a direct link to that license."]

Complete response example: [One example of a complete answer that satisfies the
  criterion. Make the example specific enough to be instructive, not just
  illustrative.
  Example: "Yes. Primary repository: https://github.com/example-org/example-project.
  License URL: https://github.com/example-org/example-project/blob/main/LICENSE.
  License: Apache-2.0."]

Incomplete response example: [One example of a common incomplete answer, with a
  brief note on why it fails.
  Example: "Yes, we use an open source license. [Fails because no SPDX identifier
  is given, no URL is provided, and 'open source' is not a license specification.
  A reviewer cannot independently verify this response.]"]
```

---

## Template 3: Applicant Guidance Document

### What it is and when it is used

The Applicant Guidance Document is the Stage 3 output. It is the applicant-facing document that accompanies the form. It is derived entirely from Section D of the WALKRI Field Specifications; no new definitional content is introduced here.

The Applicant Guidance Document does not expose the Ideation Record, the criterion specification language, or the internal data quality notes from the Field Specification. Its purpose is to help applicants produce complete, verifiable responses.

Produce one Applicant Guidance Document per form version. Update it whenever a Field Specification changes and the change affects what applicants need to know.

---

```
APPLICANT GUIDANCE DOCUMENT

Program name: [Full program name]
Round: [Round identifier or reporting period]
Form version: [Version number this guidance corresponds to]
Guidance date: [YYYY-MM-DD]

---

INTRODUCTION

[Briefly explain why this form exists and how responses will be used, written for
applicants. Do not expose evaluation criteria, scoring weights, or the decisions
the data informs. Focus on what the applicant needs to understand to complete the
form accurately. Keep this section to two to four sentences.

Example: "This form collects structured information about your project to support
[Program Name]'s review process. Each field has a specific definition; please read
the guidance for each field before responding. Incomplete or unverifiable responses
may delay review or result in a request for clarification. If you are unsure how
to respond to any field, contact [contact information] before the submission
deadline."]

---

FIELD GUIDANCE

[Repeat this block for each field in the form, in the order the fields appear.
Derive all content directly from Section D of the corresponding WALKRI Field
Specification. Do not introduce new definitions or requirements here.]

---

Field: [Field label as it appears in the form]

What this field is asking:
  [Plain language criterion intent from Field Specification Section D.
  One to three sentences. Example: "This field asks whether your primary project
  repository carries an approved open license. We are looking for a specific,
  verifiable license, not a general statement of your project's values around
  openness."]

What a complete response looks like:
  [Complete response example from Field Specification Section D, presented as a
  model for the applicant.
  Example: "A complete response includes three things: a 'Yes' or 'No' answer,
  the URL of your primary repository, and the direct URL of your LICENSE file or
  README section where the license text appears. For example:
  Yes. Repository: https://github.com/example-org/example-project.
  License: https://github.com/example-org/example-project/blob/main/LICENSE (Apache-2.0)."]

Common errors to avoid:
  [Incomplete response example from Field Specification Section D, reframed as
  guidance rather than as a failure description.
  Example: "Do not respond with a general statement such as 'Yes, we use an open
  source license' without providing a URL. Reviewers cannot verify a license
  without a direct link, and responses without URLs are considered incomplete.
  Also, make sure the URL you provide is publicly accessible; links that require
  login or organizational membership cannot be reviewed."]

Why this matters (optional):
  [A brief, plain language statement of why this field is in the form, written
  without exposing the internal decision logic from the Ideation Record. Include
  only if it will genuinely help applicants complete the field more accurately.
  Omit if it would expose evaluation criteria or create strategic incentives to
  tailor responses.
  Example: "Open licensing is a core requirement of this program. This field
  confirms that reviewers can verify your project's licensing status independently
  before the review begins."]

---

[Repeat FIELD GUIDANCE block for each field]
```

---

## Template 4: WALKRI Audit Report

### What it is and when it is used

The WALKRI Audit Report is the conformance record produced by a WALKRI audit. It documents, for each field in the form, whether the five criterion specification requirements are satisfied (Pass), not satisfied (Fail), or satisfied by a documented override (Override-documented). It is the artifact a certified program presents to downstream data consumers, funders, or research partners as evidence that the form was designed to a known standard.

Produce one Audit Report per form version audited. A change to any field definition triggers re-audit for that field; unchanged fields retain their prior certification status. The Audit Report documents which fields were audited in which cycle.

The Audit Report may be produced by the WALKRI Audit Tool, by a manual audit, or by a combination. The format is the same in all cases; the auditor field identifies whether a tool or a person performed the assessment.

---

```
WALKRI AUDIT REPORT

=== HEADER ===

Program or form name: [Full name of the program or form audited]

Form version audited: [Version number of the form. Must correspond to a specific,
  dated release of the form, not a draft or working copy.]

WALKRI version applied: [Internal version of the WALKRI standard the audit applied,
  e.g. 0.2.0. The filename stem WALKRI-standard-0_1_0.md is the stable series
  identifier; the internal version is authoritative.]

Audit date: [YYYY-MM-DD]

Auditor: [Organization name, practitioner name, or tool identifier.
  Example: "WALKRI Audit Tool v0.1.0" or "Independent Review, [Org Name]"]

---

=== FORM-LEVEL DEPENDENCY GRAPH (Section 3.9) ===

[This is the instrument set's dependency graph: the edges between instruments, as
distinct from the per-instrument nodes assessed below. It is derived from the
instrument set's own formal logic and is the one source of truth for the edges; the
per-instrument dependency declarations in each field assessment are read off this
same graph. The designer attests to the derived graph here, and an auditor can
regenerate it from the specification. A form whose instruments are all independent
records "independent" for every instrument and carries no edges.

Provide the graph in two forms: the human-readable edge list and the JSON Schema
native read-out it was derived from. The two must agree.]

Human-readable edge list: [One line per instrument. For an instrument with no edges,
  write "independent". For an instrument with edges, name each edge type that applies
  (activation, assessment dependency, ordering, cross-instrument consistency) and the
  instrument it links to.
  Example:
    Legal entity: independent
    Display name: independent
    Revenue architecture: independent
    Additionality boundary: activation (appears only when Revenue architecture is
      Commercial or Hybrid); cross-instrument consistency (must agree with concurrent
      funding disclosure)
    Development stage: independent
    Stage evidence threshold: assessment dependency (cannot be assessed until
      Development stage resolves)]

JSON Schema native read-out: [The conditional keywords in the instrument set's JSON
  Schema from which the edge list above was derived. For form-rendering formats other
  than JSON Schema, record the equivalent skip, branch, and ordering logic read out
  per WALKRI-interface-specification-0_1_0.md. For an all-independent set, this is the
  schema with no if/then/dependentSchemas/dependentRequired keywords, which is itself
  the evidence that every instrument is independent.
  Example (the activation edge above, in JSON Schema):
    "if":   { "properties": { "revenue_architecture": { "enum": ["commercial", "hybrid"] } } },
    "then": { "required": ["additionality_boundary"] }
  ]

Designer attestation: [Name or role of the designer attesting that the edge list and
  the JSON Schema native read-out above are the derived dependency graph of this
  instrument set, and that no instrument carries an edge the graph omits. Example:
  "Attested by [Name/Role], [YYYY-MM-DD]. The graph above was derived from the form
  schema at [reference] and is regenerable from it."]

Manually attested edges (platform-limitation overrides only): [If a required edge
  cannot be expressed in the form-rendering format, record it here with the platform
  named, the specific limitation, and the compensating control that holds the edge in
  practice. Per the rubric 2.6 override. If none, write "None."]

---

=== FIELD-BY-FIELD ASSESSMENT ===

[Repeat this block for each field audited. Fields not audited in this cycle
(because they were unchanged from a prior certified version) are noted in
the summary but do not require a full block entry.]

---

Field label: [As it appears in the form]

Field version: [Version number of the Field Specification assessed]

Criterion intent: [Pass / Fail / Override-documented]

Operational definition: [Pass / Fail / Override-documented]

Response form: [Pass / Fail / Override-documented]

Evidence form: [Pass / Fail / Override-documented]

Conformance threshold: [Pass / Fail / Override-documented / N/A]
  [Mark N/A if this field does not reference an external standard.]

Instrument dependency declaration: [Pass / Fail / Override-documented]
  [Records this instrument's edges as carried in the form-level dependency graph
  below, or the Declared-Absent value (independent). Pass when the instrument's
  edges are derived from the set's formal logic and match the form-level graph, or
  when the instrument is correctly marked independent. Fail when the instrument
  carries conditional, ordering, or cross-instrument logic that the graph does not
  account for, or is marked independent while carrying edges. Per Section 3.9.]

Data quality notes: [Record any Validity, Integrity, or Precision flags raised
  during the audit. If none, write "None." Reliability and Timeliness flags may
  also be recorded here.
  Example: "Integrity: This field relies entirely on self-report. No independent
  verification pathway is specified in the evidence form. This is flagged but
  not overridden; the question-holder has acknowledged the limitation and will
  add a third-party verification option in the next form version."]

Override justification: [If any requirement above is marked Override-documented,
  state the justification here. The justification must explain why the flag does
  not apply to this field's context, or why the field meets the requirement's
  intent even if it does not meet its standard form. Overrides are conformance
  choices, not failures, but they are disclosed in this record.
  Example: "Response form override: This qualitative narrative field does not have
  a formal response form justification as required by 3.3 because the field is
  intentionally open-ended and the value of the field depends on not constraining
  the response type. The question-holder has documented this as an inherently
  qualitative field per WALKRI Appendix A, Question 2. The override is authorized
  by [Name/Role], [YYYY-MM-DD]."]

---

[Repeat FIELD ASSESSMENT block for each field audited]

---

=== SUMMARY ===

Fields audited this cycle: [N]

Fields carrying forward certification from prior cycle (unchanged): [N]

Total fields in form: [N]

Fields passing all requirements: [N]

Fields with documented overrides: [N]

Fields failing without override: [N]

Overall status: [Select one:
  Certified - All fields pass all requirements with no overrides.
  Certified with overrides - All fields pass or have documented overrides.
    No unresolved failures.
  Not certified - One or more fields have unresolved failures without documented
    overrides. List the affected fields below.]

Unresolved failures (if Not certified): [List each field with an unresolved
  failure and the specific requirement that failed. Example:
  - Field "Community Reach": Operational definition - Fail. No option definitions
    provided for single-select field.
  - Field "Open License": Conformance threshold - Fail. References DPG Standard
    without enumerating applicable indicators or minimum threshold.]

Certification expiry: [Date of next required re-audit. Re-audit is required at
  the next form version change. If no version change is anticipated within
  12 months, record the date 12 months from the audit date as a recommended
  review date. Example: "Re-audit required at next form version change.
  Recommended review date if no change occurs: [YYYY-MM-DD]."]
```

---

## Notes on Using These Templates

These templates are designed to be used in sequence. The Ideation Record produces the inputs for the Field Specification. Field Specification Section D produces the inputs for the Applicant Guidance Document. Field Specification Sections A through C produce the inputs for the Audit Report.

Information flows in one direction through the process: from ideation to specification to applicant guidance. No new definitional content is introduced in Stage 3. If the Applicant Guidance Document needs to say something that is not in the Field Specification, the specification is incomplete and should be revised before Stage 3 begins.

The Audit Report is a conformance record, not a quality judgment. A field with a documented override is not a worse field than one without; the override system exists precisely to allow context-specific decisions to be made legibly rather than forcing false conformance or leaving decisions undocumented. The distinction that matters for certification is between overrides (documented and authorized) and failures (unresolved and undisclosed).

For worked examples of these templates applied to specific field types, see WALKRI-worked-examples-0_1_0.md.

---

## Template 5: Organizational Identity Declaration

### What it is and when it is used

The Organizational Identity Declaration is the Section 3.7 instrument package. It is required at all entry specification gates in CROSS-conformant programs regardless of obligation mode. It contains three instruments: the legal entity instrument, the display name instrument, and the prior entity relationship instrument. The third instrument is conditional: it activates only when prior work is cited in the application.

This template is the applicant-facing form for the declaration. It is distinct from the WALKRI Field Specification for each instrument (which follows Template 2). The declaration is what the applicant completes; the field specification is the design document that specifies how the declaration is assessed.

Programs using this template should pair it with a WALKRI Field Specification (Template 2) for each instrument. The two documents together constitute a complete identity declaration implementation.

---

```
ORGANIZATIONAL IDENTITY DECLARATION

Program name: [Full program name]
Round: [Round identifier or reporting period]
Submission date: [YYYY-MM-DD]

---

INSTRUMENT 1: LEGAL ENTITY

Legal entity name: [The name exactly as it appears in the jurisdiction of
  registration. If a corporation: the registered corporate name. If a legal
  partnership: the partnership name on the registration document. If applying
  as a natural person with no legal entity: your full legal name and a statement
  that no legal entity exists.

  Do not enter: project names, brand names, GitHub organization names, pseudonyms,
  or display names unless those names are also your legal name of record in the
  stated jurisdiction.]

Jurisdiction of registration: [Country and, where applicable, state/province.
  Example: "United States - Delaware" or "Switzerland - Zug" or "United Kingdom -
  England and Wales".]

Registration number or equivalent identifier: [The number assigned by the
  registering authority. For corporations: incorporation number. For nonprofits:
  EIN or equivalent. For unregistered individuals: leave blank and explain why
  no registration applies. Example: "Delaware entity number: 7023941"]

If no legal entity exists, state the answerability mechanism: [If you are
  applying as an individual with no legal entity, state your full legal name
  and identify who is personally answerable for obligations under this grant.
  Example: "Applying as Jane Smith, natural person. Jane Smith is personally
  answerable for all obligations under this grant. No legal entity exists."]

---

INSTRUMENT 2: DISPLAY NAME

Display name: [The name under which this project or organization is publicly
  known, used consistently in prior communications, repositories, grant histories,
  and publications. If the display name is identical to the legal entity name,
  state that explicitly rather than repeating the name.

  A name used only on this application with no prior public appearances is not a
  display name. A display name requires prior public use.]

Evidence of prior public use: [One or more URLs demonstrating that this display
  name was in use before this application. Acceptable sources: a prior grant
  application, a public GitHub organization or repository, a published
  communication, or a program record. Example: "github.com/example-project
  (established January 2024). Previous Octant application under this name:
  [URL]."]

Relationship between display name and legal entity: [Describe how the display
  name relates to the legal entity name above. Examples: "The display name is
  the project name maintained by the legal entity." / "The display name is an
  informal abbreviation of the legal entity name." / "They are the same."]

---

INSTRUMENT 3: PRIOR ENTITY RELATIONSHIP
(Complete this section only if you cite prior work anywhere in this application.
If no prior work is cited, state "Not applicable" and stop.)

Prior work citation: [Copy or summarize the prior work cited in this application
  that activates this instrument. Example: "Application cites development of
  [Protocol X] as evidence of technical capability."]

Entity of performance: [Name the legal entity or organizational context under
  which the cited prior work was performed. If the work was performed under an
  employer: name the employer. If under a DAO: name the DAO and your role within
  it. If under a prior legal entity that has since been restructured: name the
  prior entity. Example: "Prior work was performed while employed at [Org Name]
  from 2021 to 2023."]

Applicant's relationship at the time of the work: [Your role in the entity at
  the time. Example: "Lead engineer, employed full-time. Departed the organization
  in November 2023."]

Current status of the relationship: [Whether the relationship to the prior entity
  is active, inactive, or restructured, and what that means for the cited work.
  Example: "Departed in November 2023. The organization continues to operate
  separately from the applying entity."]

Current ownership and access: [Who currently holds intellectual property rights
  to the cited work; who controls the deployment or codebase; who maintains the
  user relationship with any users cited as evidence of the prior work's impact.
  Be specific about what the applying entity controls and what it does not.
  Example: "The codebase is open source under MIT license. The prior employer
  holds no exclusive rights. The applying entity has forked the repository and
  is the active maintainer of the fork. The original deployment is maintained
  by the prior employer."]

[Repeat this section for each distinct piece of prior work cited.]

---

SELF-REFERENCE CONSISTENCY CERTIFICATION

By submitting this declaration, the applicant certifies that every reference to
the applying entity, its team, and its work throughout this application resolves
to either the legal entity name stated in Instrument 1 or the display name stated
in Instrument 2. Any reference to a third name or organizational context that is
not covered by Instrument 3 is a consistency flag and must be resolved before the
gate assessment proceeds.
```

---

## Template 6: Gate Declaration Fields (Section 3.8)

**Revenue Architecture Declaration**
Revenue architecture type (select one): [ ] Grant-only [ ] Fee-for-service [ ] Commercial [ ] Hybrid
Named revenue sources: [list all active revenue sources, including grants, service contracts, product revenue, token appreciation, staking rewards]
[If Commercial or Hybrid]: Additionality boundary: [specify what this grant funds that commercial revenue does not]

**Disbursement Authority Declaration**
Authority state (select one): [ ] Individual [ ] Collective [ ] Delegated
[If Individual]: Full legal name of authority holder: ___
[If Collective]: Mechanism name: ___ | Multisig or governance contract address: ___ | Current key holders: ___ | Quorum threshold: ___
[If Delegated]: Receiving entity: ___ | Deploying entity: ___ | Delegation terms: ___ | Documentation: ___

**Continuity Capacity Declaration**
Continuity state (select one): [ ] Single [ ] Partial [ ] Resilient
Named primary contributor: ___
[If Single or Partial]: Continuity explanation: [how would the project continue if the primary contributor were unavailable?]

**Obligation Fulfillment Record** (activates for returning applicants and prior-work-citing applicants)
[Repeat for each prior grant in scope]:
- Granting program: ___
- Grant period: ___
- Committed deliverable or FROM-TO state: ___
- Produced artifact or measured change: ___ [with publicly accessible link]
- Fulfillment state (select one): [ ] Fulfilled [ ] Partially fulfilled [ ] Unfulfilled
- Explanation [required if not Fulfilled]: ___

**Development Stage Declaration**
Stage (select one): [ ] Stage 1: Proof of concept [ ] Stage 2: Early adoption [ ] Stage 3: Growth [ ] Stage 4: Established infrastructure [ ] Stage 5: Retroactive recognition
Explanation: [describe why this stage accurately characterizes the project]
Independent evidence: [name a verifiable external source that corroborates the declared stage]

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 0.1.6 | 2026-06-13 | Section 3.9 reflection. Template 2 (Field Specification) Section A gains a Dependency declaration slot: a per-instrument field read off the instrument set's own formal logic, defaulting to the Declared-Absent value (independent) for an instrument with no edges, and recording activation conditions, assessment dependencies, ordering constraints, and cross-instrument consistency constraints where edges exist. Template 4 (Audit Report) gains a form-level Dependency Graph artifact between the header and the field-by-field assessment, given in two agreeing forms (human-readable edge list and JSON Schema native read-out) with a designer attestation and a slot for platform-limitation manual edges; the per-field assessment block gains an Instrument dependency declaration Pass/Fail/Override line. The "WALKRI version applied" placeholder now points to the standard's authoritative internal version rather than a fixed 0.1.0, since the filename stem is the stable series identifier. Light instrument-framing note that a form field is the form-modality instantiation of an instrument; no existing template field, conformance threshold, or mapping changed. |
| 0.1.5 | 2026-06-13 | Frame Language own-voice vocabulary pass. Recasts: the verb "governs" recast to "structures"/"specifies" in own-voice prose (the field specification structures everything downstream; the design document specifies how the declaration is assessed); own-voice "transparently" recast to "legibly" (the override-system note); "accountability/accountable (of the legal party)" recast to "answerability/answerable" in the Template 5 legal entity instrument no-entity branch, including its worked example. Kept as admissible: the named technical concept "governance contract address" (on-chain, Template 6); the historical changelog records naming the prior Governance Resilience primitive. No template field, conformance threshold, or mapping changed; vocabulary only. |
| 0.1.4 | 2026-06-08 | Disbursement-authority Governed state renamed Collective in Template 6 (the "[If Collective]" sub-field branch), completing the Governed-to-Collective rename. The version stamps in the frontmatter and heading, which had lagged at 0.1.2 behind the 0.1.3 changelog entry, are corrected. No template content changed; naming only. |
| 0.1.3 | 2026-05-23 | Primitive rename cascade applied. Template 6: the "Governance Resilience Declaration" sub-template is now the "Continuity Capacity Declaration"; the three-state vocabulary (Single, Partial, Resilient) and the named primary contributor and continuity explanation sub-fields are preserved. Historical changelog entry below retains the prior primitive name as it stood at the time of release. |
| 0.1.2 | 2026-05-18 | Template 6 added: Gate Declaration Fields (Section 3.8). Covers revenue architecture, disbursement authority, governance resilience, obligation fulfillment record, and development stage declarations with structured sub-fields for each state. |
| 0.1.1 | 2026-05-17 | Template 5 added: Organizational Identity Declaration. Three-instrument template covering the legal entity instrument, display name instrument, and conditional prior entity relationship instrument, plus a self-reference consistency certification. Annotated field instructions for each element. |
| 0.1.0 | 2026-05-15 | Initial draft. Four templates: Ideation Record (Stage 1), WALKRI Field Specification (Stage 2), Applicant Guidance Document (Stage 3), and WALKRI Audit Report. |
