---
title: WALKRI Worked Examples
version: 0.1.5
date: 2026-06-13
license: CC0
status: Working draft. Companion to WALKRI-standard-0_1_0.md.
source: Octant Epoch 12 grant evaluation cycle, 2026.
---

# WALKRI Worked Examples

Version 0.1.5 | 2026-06-13 | CC0

---

## Introduction

These examples demonstrate what WALKRI failures look like in practice and what conformant specifications would have looked like in their place. They are drawn from the Octant Epoch 12 grant evaluation cycle. Octant is a web3 public goods funding program; in Epoch 12, 52 grant applications were submitted using a form built in Fillout. Several fields in that form produced inconsistent applicant responses that complicated evaluation because those fields lacked precise operational definitions, conformance thresholds, or evidence forms. The cases documented here are real specification failures from that cycle, reconstructed in WALKRI's five-element format to show what the fields should have contained before any application was accepted.

Each example follows the same structure: the field as published, a description of what happened in evaluation, and a WALKRI-conformant specification showing all five elements. The final example is a positive case, showing a field that would pass WALKRI audit without modification. The last two sections draw quantitative observations from the Epoch 12 experience and close with a summary for practitioners who run grant evaluations.

The before/after blocks use structured comparison formatting throughout. Prose sections use prose. The goal is not to criticize the Octant team's execution; the goal is to make the failure modes concrete enough that they are recognizable and fixable in future cycles.

---

## Example 1: The DPG Eligibility Field

### The field as published

```
Label:              "Building on Ethereum or qualifying as DPG per DPGAlliance"
Response form:      Not specified (applicants answered in free text)
Evidence form:      Not specified
Conformance threshold: Not specified
```

### What happened

Evaluators could not consistently assess DPG eligibility because the field did not specify which of the nine DPG Standard indicators applied, what evidence form satisfied each, or whether all nine or a subset were required. Registry membership was used as a proxy for the nine-indicator assessment, which is incorrect: registry membership confirms past assessment, not current qualification. Projects that had been assessed for the registry years earlier were treated as currently qualifying even where the project had changed substantially since assessment. Evaluations across 29 applications produced inconsistent DPG determinations because each evaluator applied a personal interpretation of what "qualifying as DPG" meant.

### WALKRI-conformant specification

**Criterion Intent:** Whether the project satisfies the Digital Public Goods Standard as an alternative to the Ethereum pathway, assessed against the nine DPG Standard indicators, for purposes of determining pathway eligibility at time of application.

**Operational Definition:**
- Inclusion: a project qualifies if it satisfies the required DPG Standard indicators as specified in the conformance threshold below.
- Exclusion: registry membership alone does not qualify a project; the current state of the project must satisfy the indicators at the time of evaluation.
- Unit of analysis: the applying project, not the organization.
- Edge case: a project in the DPG registry that has changed substantially since registry assessment is evaluated against current indicators, not registry status. Substantial change is defined as a change in license, a change in core functionality, or a change in technical dependencies that affects platform independence.

**Response Form:** Multi-select. Applicants select the pathway that applies: Ethereum mainnet, Ethereum Layer 2, or DPG Standard. Multi-select because some projects may qualify under both pathways.

**Response Form Justification:** The original single free-text framing required applicants to argue for whichever pathway they believed applied, without a structured mechanism to indicate that both pathways applied. Projects that qualified on both grounds were recorded inconsistently, producing artificial distinctions in pathway distribution across the cohort. A multi-select resolves this and produces a cleaner dataset for cross-project analysis.

**Evidence Form:** For the DPG pathway, a completed DPG self-assessment form or a link to the project's evidence for each required indicator. Evidence must be accessible from public sources without authentication.

**Conformance threshold** (DPG Standard, https://digitalpublicgoods.net/standard/, accessed 2026-05-15):

Required indicators (all four must pass):
- Indicator 1, SDG relevance: named SDG with explanation of relevance.
- Indicator 2, open license: LICENSE file URL in a public repository with an OSI-approved license identifier for software, or a Creative Commons license for content; SPDX identifier required.
- Indicator 4, platform independence: list of dependencies with confirmation that none are mandatory proprietary platforms.
- Indicator 5, documentation: public documentation URL accessible without authentication.

Advisory indicators (3, 6, 7, 8, 9): reviewers note presence or absence but advisory indicators do not determine passage.

Minimum threshold: all four required indicators must pass. Failure on any required indicator is a gate fail on the DPG pathway.

### WALKRI audit result

| Element | Original field | WALKRI-conformant specification |
|---|---|---|
| Criterion intent | Absent | Pass |
| Operational definition | Absent | Pass |
| Response form | Not specified | Pass |
| Evidence form | Absent | Pass |
| Conformance threshold | Absent | Pass |

**Original Field:** Not certifiable. Five unresolved flags.
**Conformant Specification:** Certified at Standard level.

---

## Example 2: The "Contributions" Single-Select Field

### The field as published

```
Label:              "Contributions"
Response form:      Single-select dropdown
Options:            Code | Community | Research | Governance | Other
Option definitions: Not specified
Evidence form:      Not specified
```

### What happened

Projects whose work spanned multiple contribution types were forced to select one. A project that maintained production infrastructure while running educational workshops selected either "Code" or "Community" and lost the other dimension in the dataset. The problem compounded at the analysis layer: projects with primarily "Community" contributions were evaluated differently from projects with primarily "Code" contributions even where the public goods impact was comparable. The single-select structure introduced a categorical distortion that was invisible in the collected data because the data looked clean. The distortion was only visible when evaluators tried to compare projects across categories and found that the categories did not represent stable natural kinds in the applicant population.

A second failure compounded the first: none of the five options carried a definition. "Community" could mean in-person events, online forum moderation, translation, or governance facilitation. "Governance" could mean voting in a DAO, writing governance proposals, or building tooling for governance processes. Two applicants with substantively similar work selected different options based on how they described themselves, not on any common definition.

### WALKRI-conformant specification

**Criterion Intent:** The primary types of contribution the project makes to the ecosystem, for purposes of understanding the project's public goods pathway and enabling cross-project comparison by contribution type.

**Operational Definition:**
- Inclusion: any contribution type that the project has demonstrably produced in the prior 12 months with evidence accessible from public sources.
- Exclusion: aspirational contributions not yet produced; contributions produced by other projects that the applying project only coordinates or funds.
- Unit of analysis: the applying project's outputs.
- Edge case: a project that began operations within the prior 12 months is assessed on the period of operation; the 12-month window does not disqualify newer projects.

**Option definitions** (each option is defined; applicants may select all that apply):
- Code: software artifacts released under an open license in a public repository, including applications, libraries, tooling, and protocol implementations.
- Community: documented facilitation, education, or coordination activities with named participants or events, including workshops, curricula, translations, and moderated forums.
- Research: published findings under an open license accessible without authentication, including reports, papers, and documented investigations.
- Infrastructure: operational systems with verifiable uptime records, including nodes, relays, bridges, oracles, and indexers.
- Governance: participation in on-chain or structured off-chain governance with verifiable records, including proposal authorship, protocol design contributions, and governance tooling development.

**Response Form:** Multi-select. Applicants may select all contribution types that apply.

**Response Form Justification:** Most projects contribute across multiple types. A single-select forces artificial categorization that distorts evaluation and reduces data quality for cross-project analysis. The original single-select also had no option definitions, meaning the categorical distortion was compounded by interpretation variance within each category.

**Evidence Form:** For each selected contribution type, a URL to a public artifact demonstrating that contribution type within the prior 12 months. A project selecting three contribution types must submit at least one URL per type.

### WALKRI audit result

| Element | Original field | WALKRI-conformant specification |
|---|---|---|
| Criterion intent | Absent | Pass |
| Operational definition | Absent (options undefined) | Pass |
| Response form | Single-select on multi-value construct (design error) | Pass |
| Evidence form | Absent | Pass |
| Conformance threshold | N/A (no external standard) | N/A |

**Original Field:** Not certifiable. Four flags, including a response form design error.
**Conformant Specification:** Certified at Standard level.

Note on response form design errors: a design error differs from a missing element. A missing element is an absence; a design error is an active structural choice that produces systematic measurement error. The single-select on a multi-value construct is a design error because it cannot be fixed by adding a definition. The response type itself must change.

---

## Example 3: A Well-Specified Field (Positive Case)

This example shows a field that passes WALKRI audit without modification. It is drawn from a hypothetical but realistic version of a "Prior grant funding" field from a rigorous grant program. The purpose is to demonstrate that WALKRI conformance does not require heroic effort when specification discipline is applied from the start.

### The field as specified

**Label:** Prior grant funding received in the past 24 months

**Criterion Intent:** The total amount of grant funding received by the applying project from external funders in the 24-month period ending on the application deadline, for purposes of assessing funding concentration and evaluating the marginal impact of the requested grant.

**Operational Definition:**
- Inclusion: any grant, award, or non-dilutive funding received by the project or its operating entity from an external funder, including retroactive public goods funding rounds, foundation grants, and program awards.
- Exclusion: investment (equity, token, or convertible note); revenue from products or services; funding received by a parent organization that was not specifically designated for this project; in-kind contributions.
- Unit of measurement: USD equivalent at the time of receipt, using the exchange rate on the date of receipt for non-USD denominations.
- Counting rule: each distinct grant award is counted separately. A multi-tranche grant is counted as one award; the total committed amount is reported, not the amount disbursed to date.
- Boundary condition: funding received on the application deadline date is included; funding received after the deadline is excluded regardless of when it was announced.
- Edge case: if the project is incorporated in multiple legal entities and the grant was received by a sister entity that shares operational infrastructure, include it and note the entity relationship.

**Response Form:** Numeric (USD equivalent, integer, no decimals), followed by a multi-field structured input listing each grant by funder name, amount, date, and grant program name.

**Response Form Justification:** A numeric field captures the aggregate for analysis; the structured list captures the provenance of each component for reviewer verification. A single text field would produce responses in inconsistent formats that are not machine-readable.

**Evidence Form:** For each grant listed, a publicly accessible announcement URL or award letter. Self-reported totals without supporting URLs are not accepted. If no public announcement exists, a redacted award letter or a letter of attestation from the funder is acceptable.

**Conformance Threshold:** Not applicable. This field does not reference an external standard. The operational definition above is the conformance specification.

**Timeliness Note:** Evidence must reflect the 24-month window ending on the application deadline. Evidence from outside this window should not be submitted and will not be considered.

### WALKRI audit result

| Element | Assessment |
|---|---|
| Criterion intent | Pass: measurement claim is clear and distinct from the label |
| Operational definition | Pass: inclusion, exclusion, unit, counting rule, boundary condition, and one edge case all present |
| Response form | Pass: response type is appropriate for the construct; justification addresses why numeric plus structured list is correct |
| Evidence form | Pass: artifact type, required content, and acceptable alternatives are specified; recency requirement is stated |
| Conformance threshold | Pass: no external standard referenced; operational definition is self-sufficient |

**Field certified at Standard level without modification.**

This field took more time to specify than typical form design. That time investment is recovered in evaluation: reviewers applying this field to 29 applications make no discretionary judgments about what counts as prior funding. The operational definition makes those judgments once, in advance, for the entire cohort.

---

## Example 4: The Upstream Value - Before and After Analysis

The cost of underspecified fields is not primarily a data quality cost. It is an evaluator time cost that accrues during review and a reliability cost that accrues when results are contested or when the dataset is reused.

The Epoch 12 evaluation record supports the following observations.

**Eligibility Judgment Calls:** The DPG eligibility field, as published, required at least one substantive judgment call per application that cited DPG status as a basis for eligibility. Across 29 applications, at least 8 required extended researcher investigation to determine whether the project's claimed DPG status was current and applicable. A WALKRI-conformant DPG field, with its four required indicators and specified evidence form, would have resolved those 8 cases at application time by requiring applicants to submit indicator-level evidence with their application. The evaluator time cost of post-submission investigation is conservatively estimated at 30 to 45 minutes per case, totaling 4 to 6 hours of evaluation time that a conformant field would have eliminated.

**Unverifiable Public Claims:** Across the 29 applications, at least 12 produced findings of "cannot be confirmed from any public source" on claims that were material to eligibility or impact assessment. A properly specified evidence form requirement, applied at the point of submission, would have surfaced these gaps before any evaluation began. Applicants who cannot satisfy an evidence form requirement at submission time either strengthen their submission or are flagged immediately, rather than passing initial review and requiring intensive investigative work later.

**Contribution Type Distortion:** The single-select Contributions field produced at least 6 cases where the selected category visibly understated the project's actual contribution profile, based on reviewer notes cross-referenced against the applicant's supporting materials. These 6 cases required qualitative adjustment during evaluation. A multi-select field with defined options would have captured the full profile at the application stage.

**Specification Cost Vs. Evaluation Cost:** Specifying the DPG eligibility field and the Contributions field to WALKRI conformance would have required approximately 2 to 4 hours of design time before the round opened. The evaluation time cost attributable to those two underspecified fields alone is estimated at 8 to 12 hours across the full Epoch 12 cohort. The ratio is not favorable to the "we'll figure it out in evaluation" approach. That ratio holds across every round the form is reused in its current state.

These numbers are drawn from the Epoch 12 evaluation record and are reported using "at least" framing where exact counts are uncertain. They are not projections or models; they reflect documented judgment calls and researcher findings from the evaluation cycle.

---

## Closing: The Case Study Summary

Epoch 12 demonstrated a pattern that is common in grant evaluation and predictable in its consequences. A form is built quickly, fields are labeled rather than defined, and eligibility criteria reference external standards without specifying what those standards require in practice. The form looks complete because it has all the right labels. The problems emerge in evaluation, when reviewers discover that the labels do not resolve the questions they need to answer. Evaluators spend time they should not have to spend reconstructing definitions that should have been in the form. Results are harder to defend because the standard was never written down. The dataset is harder to reuse because the fields cannot be trusted to mean the same thing across applications.

WALKRI addresses this at the source: the point where a question becomes a field before any applicant sees it. Applying WALKRI to the two most consequential underspecified fields in Epoch 12 (the DPG eligibility field and the Contributions field) would have taken a few hours before the round opened and would have eliminated an estimated 8 to 12 hours of evaluation judgment work, produced a cleaner and more auditable dataset, and reduced the number of eligibility determinations that depended on individual evaluator interpretation. The investment is in specification. The return is in reliability.

---

## Example 5: The Organizational Identity Declaration

### The field as published (Epoch 12)

```
Label:              "Are you:"
Response form:      Single-select
Options:            Solo contributor/applying as an individual
                    A working group
                    A registered organization/incorporated organization
Evidence form:      Not specified
No legal entity field: absent
No display name field: absent
No prior entity relationship instrument: absent
```

The form collected an organizational status classification but not an organizational identity. There was no field asking for the legal entity name, jurisdiction, or registration number. There was no field asking for the display name under which the project was publicly known. There was no field asking whether cited prior work was performed under a different organizational context.

### What happened

Three patterns from the Epoch 12 cohort illustrate what the absence of identity instruments produced.

**Pattern 1: Unverifiable attribution.** Several applications cited prior technical work as evidence of capability without naming the organization under which that work was performed. Evaluators could not determine whether the cited work belonged to the applying entity, to a prior employer, or to a collaborative organization the applicant had since left. Attribution claims could not be assessed as accurate or inaccurate because the attribution was never made specific. The evaluator had to conduct organizational research to reconstruct the entity history that an identity declaration would have surfaced directly.

**Pattern 2: Self-reference inconsistency.** Applications used three or four different names interchangeably: a GitHub organization name in one field, a project name in another, a legal entity name in a third, and a display name in a fourth, with no declared relationship between them. Evaluators could not determine whether these were the same entity viewed from different angles or distinct entities with different answerability structures. In one case, the "solo contributor" category was selected while the evidence field cited repositories owned by a different organization entirely.

**Pattern 3: Prior work presented as current ownership.** Applications described technical work performed during employment at a previous organization as if it were the applicant's independent prior work. The cited codebase was owned and maintained by the prior employer; the applicant had departed. No disclosure was made. The evaluator could not assess whether the applicant had legal authority to represent the cited work as their own track record. The application passed initial review and the misrepresentation was discovered only during deep-dive verification of the GitHub repository history.

### WALKRI-conformant specification

**Legal entity instrument**

Criterion intent: Identifies the legal person or registered organization legally answerable for delivering grant obligations and receiving disbursement.

Operational definition:
- Inclusion: the name exactly as it appears in the jurisdiction of registration. For a corporation: the registered corporate name. For a natural person with no entity: full legal name.
- Exclusion: project names, brand names, GitHub organization names, pseudonyms, and display names that are not also the applicant's legal name of record.
- Unit of analysis: the legal entity making the application.
- Edge case: if the applying entity is a chapter or working group of a larger organization, the legal name of the parent organization must also be stated, with the relationship between the two described.

Response form: Text (legal name) + text (jurisdiction) + text (registration number or "not applicable" with explanation).

Evidence form: The legal entity name must be independently verifiable from a public registry within 60 days of submission. Acceptable sources: national business registries, state incorporation records, charity commission databases, or equivalent official registries. The applicant provides the registry name and URL in the evidence form response.

**Display name instrument**

Criterion intent: Identifies the publicly known name under which this project presents itself in grant histories, repositories, and public communications, enabling cross-program track record queries.

Operational definition:
- Inclusion: a name used in at least one publicly accessible communication, grant record, or repository prior to this application.
- Exclusion: names created specifically for this application with no prior public use.
- Unit of analysis: the project or organizational unit applying.
- Edge case: if the project has changed its display name since a prior round, both the prior name and the current name must be stated with the date of transition.

Response form: Text (display name) + URL (evidence of prior public use).

Evidence form: One URL to a publicly accessible page where the display name appears in a context predating this application. A GitHub organization page, a prior grant application record, or a published article are all acceptable.

**Prior entity relationship instrument** (conditional: activates when prior work is cited)

Criterion intent: Identifies the organizational context under which cited prior work was performed, so that evaluators can assess whether the attribution claim is accurate and the applying entity has appropriate standing to represent the cited work.

Trigger condition: this instrument is required in the entry specification for any application that cites prior work in any field. Activation is not at the applicant's discretion. An applicant who cites prior work and does not complete this instrument has submitted an incomplete entry.

Operational definition: for each piece of cited prior work, three elements are required: the name of the entity under whose resources, governance, or employment the work was performed; the applicant's role in that entity at the time; and the current ownership and access status (who holds IP rights, controls the deployment, and has the user relationship with cited users).
- Exclusion: "I did this work independently" without further specification is not a complete response if the work was funded by, performed within, or hosted by any organization. If the work was truly independent, that must be stated explicitly with evidence of independent funding and hosting.
- Edge case: if the prior work was a collaborative project with no clear single owner, the applicant states the collaborative context, their specific contribution within it, and what rights the collaborative arrangement grants them to represent the work in this application.

Response form: Structured text (three elements per cited work, each labeled).

Evidence form: For the entity of performance: a public record confirming the applicant's association with that entity (LinkedIn profile, organizational team page, GitHub organization membership, or equivalent). For current ownership: a URL to the relevant repository, license file, or contract establishing the current ownership and access arrangement.

### WALKRI audit result

| Instrument | Published field | WALKRI-conformant specification |
|---|---|---|
| Legal entity | Absent | Pass |
| Display name | Absent | Pass |
| Prior entity relationship | Absent | Pass |
| Self-reference consistency | Not checkable (no declared identities to check against) | Pass |

**Published form:** Not certifiable for identity. No identity instruments present. Self-reference consistency check structurally impossible without declared identities.

**Conformant specification:** Certified at Standard level for all four identity elements.

### What the conformant specification would have changed

The three patterns described above would have been surfaced at application time rather than during evaluator deep-dives.

Pattern 1 (unverifiable attribution): the prior entity relationship instrument would have required applicants to name the organization under which cited work was performed, their role, and the current ownership. Evaluators would have received the attribution context with the application rather than having to reconstruct it during review.

Pattern 2 (self-reference inconsistency): the self-reference consistency certification would have required applicants to certify that all names used throughout the application resolve to either the legal entity or the display name. Applications with inconsistent names would have self-identified the inconsistency rather than presenting it as an unmarked pattern for evaluators to discover.

Pattern 3 (prior employer work presented as independent): the current ownership and access element of the prior entity relationship instrument would have required disclosure of who holds the IP and controls the deployment. An applicant who had departed their employer would have had to state that the prior employer maintains the codebase, surfacing the misrepresentation at application time.

---

## Example 6: Gate Declaration Fields (Section 3.8) - Three Epoch 12 Patterns

### Pattern A: Grant-Only Revenue with Single Continuity (Clean declaration)

**Application context:** A two-person developer tooling project with no token, no fees, and no commercial revenue. First external grant application.

**Revenue architecture instrument:**
Revenue architecture type: Grant-only
Named revenue sources: No revenue sources. This is the project's first external funding application.
Additionality boundary: Not applicable (grant-only).

**Assessment:** Conformant. Grant-only with no prior funding is a valid and complete declaration. The evaluator notes Stage 1 declaration and Single continuity capacity as expected co-occurring states.

**Disbursement authority instrument:**
Authority state: Individual
Full legal name: [Named developer, jurisdiction stated]

**Assessment:** Conformant. Individual disbursement authority for a sole contributor is consistent with the Continuity Capacity declaration.

**Continuity Capacity instrument:**
Resilience state: Single
Named primary contributor: [Named developer]
Continuity explanation: The project is sole-authored. If unavailable, development would pause until a new contributor is onboarded. No succession mechanism exists at this stage.

**Assessment:** Conformant and honest. Single state is a risk factor recorded in the evaluation, not a gate failure.

---

### Pattern B: Undisclosed Commercial Revenue (Non-conformant declaration)

**Application context:** A project with a deployed governance token and active staking rewards. The revenue architecture declaration reads "Grant-only."

**Revenue architecture instrument:**
Revenue architecture type: Grant-only
Named revenue sources: Community grants only.

**Assessment:** Non-conformant. The evaluator discovers an active governance token contract with staking rewards. Staking rewards constitute commercial revenue under the revenue architecture primitive. The grant-only declaration is a material misclassification. This triggers a concurrent funding disclosure review and an additionality declaration requirement.

**What a conformant declaration would have read:**
Revenue architecture type: Commercial (staking rewards constitute commercial revenue)
Named revenue sources: Staking rewards from governance token. Grant funding supplements staking revenue for development work outside the commercial scope.
Additionality boundary: This grant funds [specific development scope] that staking revenue does not cover.

---

### Pattern C: Returning Applicant with Partially Fulfilled Prior Obligation (Conformant disclosure)

**Application context:** A returning applicant with one prior grant from this program. Two of three milestones were completed. The third milestone was scoped down due to a market change documented in the continuation gate submission.

**Obligation fulfillment record:**
Granting program: [Program name]
Grant period: [Prior epoch]
Committed deliverable: [Three milestones as specified at entry gate]
Produced artifact: [Links to two completed milestones. Third milestone: scope reduction documented at continuation gate submission, archived at [link].]
Fulfillment state: Partially fulfilled
Explanation: The third milestone was reduced in scope at the continuation gate due to [named market change]. The reduction was disclosed and accepted by the program committee. The reduced deliverable is published at [link].

**Assessment:** Conformant and exemplary. Partially fulfilled with proactive disclosure and documented committee acceptance is treated as a positive track record signal. The evaluator confirms the continuation gate record exists and the reduced deliverable is accessible.

---

## Example 7: Instrument Dependency Declaration (Section 3.9)

The first six examples assess instruments as nodes: each field measured something, defined its responses, named its evidence. This example assesses an edge between instruments. The Epoch 12 form, like most intake forms, carried conditional logic: some fields appeared only when an upstream answer took a given value. A node-by-node audit can pass every field in such a form and still never examine the conditional logic that decides which fields a given applicant actually sees and is assessed on. Section 3.9 closes that gap by requiring the form's dependency graph to be derived from the form's own formal logic, attested, and recorded alongside the instruments.

A note on framing: a form field is the form-modality instantiation of an instrument, so the edges below are equally edges between instruments in any modality. This example uses the form-field rendering because that is the one Epoch 12 used.

### The instrument set with a conditional edge

The revenue architecture instrument (Section 3.8) is single-select across four types: grant-only, fee-for-service, commercial, hybrid. A second instrument, the additionality boundary, asks what the grant funds that commercial revenue does not. That second instrument is meaningful only for an applicant who has commercial revenue. The form expresses this as a conditional: the additionality boundary field appears only when the revenue architecture answer is Commercial or Hybrid. That conditional is an edge, and the additionality boundary instrument also carries a second edge, a cross-instrument consistency constraint: the revenue it implies must agree with the applicant's concurrent funding disclosure.

```
Instruments in the set:
  Revenue architecture   (single-select: grant-only | fee-for-service | commercial | hybrid)
  Additionality boundary (text; appears conditionally)
  Concurrent funding disclosure (structured list)

The edge, as the form's formal logic carries it:
  Additionality boundary activates only when Revenue architecture is commercial or hybrid.
  Additionality boundary value must be consistent with Concurrent funding disclosure.
```

### The derived dependency graph

The graph is not author-written prose about how the form behaves. It is read off the form's own JSON Schema, where the conditional is a formal keyword. The activation edge is the `if/then` block; the consistency edge is recorded as a cross-instrument constraint the auditor confirms against the named instrument.

```
Human-readable edge list:
  Revenue architecture:           independent
  Concurrent funding disclosure:  independent
  Additionality boundary:         activation (appears only when Revenue architecture
                                    is commercial or hybrid);
                                  cross-instrument consistency (must agree with
                                    Concurrent funding disclosure)

JSON Schema native read-out (the activation edge the list above was derived from):
  "if":   { "properties": { "revenue_architecture": { "enum": ["commercial", "hybrid"] } } },
  "then": { "required": ["additionality_boundary"] }
```

The two independent instruments declare the Declared-Absent value (independent) in one word each; only the additionality boundary instrument carries edges, so only it carries a graph entry beyond the one-word value. This is the design intent of Section 3.9: a shallow form pays almost nothing, and only the instruments that actually branch carry their full edge structure.

### The attested record

The dependency graph travels in the conformance record. The designer attests that the edge list and the JSON Schema native read-out are the form's derived graph and that no instrument carries an edge the graph omits. The attestation is over an artifact an auditor can regenerate from the form schema, so there is one source of truth rather than a hand-written description that can drift from the live form.

```
Designer attestation: Attested by [Name/Role], 2026-05-15. The graph above was
  derived from the form schema at [reference] and is regenerable from it. No
  instrument carries an edge the graph omits.
Manually attested edges (platform-limitation overrides only): None.
```

### WALKRI audit result

| Instrument | Dependency declaration | Outcome |
|---|---|---|
| Revenue architecture | independent | Pass |
| Concurrent funding disclosure | independent | Pass |
| Additionality boundary | activation + cross-instrument consistency, derived and attested | Pass |
| Form-level dependency graph | derived from the form schema, attested, recorded | Pass |

**Conformant instrument set:** Certified. The graph is derived from the form's own formal logic, attested by the designer, and recorded; the two edgeless instruments are correctly marked independent.

### The non-conformant version (same form, edge present but uncertified)

This is the same form with the same conditional logic, audited node by node only. Every field passes its five criterion elements. The additionality boundary field still appears only for commercial and hybrid applicants, but the form's dependency graph was never derived, attested, or recorded.

```
Label set as published:   Revenue architecture; Additionality boundary; Concurrent funding disclosure
Per-field (node) audit:   all five criterion elements Pass on each field
Dependency graph:         absent (the activation and consistency edges were never derived,
                            attested, or recorded)
```

**What happened.** Two applicants traverse the form differently. A grant-only applicant never sees the additionality boundary field; a commercial applicant does. The certification examined each field in isolation and never examined the conditional that produces these two different paths. When the data is pooled, the additionality boundary column is populated for some applicants and empty for others, and the empty cells are ambiguous between "instrument did not apply" and "applicant skipped it." Worse, the cross-instrument consistency edge was never recorded, so a commercial applicant whose additionality boundary contradicts their concurrent funding disclosure passes a node-only audit, because no instrument, taken alone, is wrong. The edge that would have caught the contradiction was the part the audit never looked at.

**WALKRI audit result for the non-conformant version:**

| Instrument | Dependency declaration | Outcome |
|---|---|---|
| Revenue architecture | not recorded | Fail (2.6) |
| Concurrent funding disclosure | not recorded | Fail (2.6) |
| Additionality boundary | carries activation and consistency edges; not derived, attested, or recorded | Fail (2.6) |
| Form-level dependency graph | absent while the form carries conditional logic | Fail (2.6) |

**Non-conformant instrument set:** Not certifiable. The form carries conditional and cross-instrument logic with no derived, attested, and recorded dependency graph; this is a blocking failure under rubric 2.6 regardless of every node passing its five criterion elements.

### What the conformant version changes

The difference between the two versions is not new fields and not stricter node requirements; it is whether the edges the form already carries are certified. Deriving the graph from the form schema costs little when the edges are few, and the one-word independent value keeps edgeless instruments cheap. What the certification buys is that the path through the form, the thing that decides what each applicant actually encounters and is assessed on, is part of what was assessed rather than a soundness hole the node-level audit structurally cannot reach.

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 0.1.5 | 2026-06-13 | Section 3.9 reflection. Example 7 added (Instrument Dependency Declaration): an instrument set with a conditional edge (the additionality boundary instrument activates only when the revenue architecture answer is commercial or hybrid, and carries a cross-instrument consistency edge to the concurrent funding disclosure), its dependency graph derived from the form's own JSON Schema and shown in two agreeing forms (human-readable edge list and JSON Schema native read-out), the designer attestation, and the WALKRI audit result, with the two edgeless instruments marked Declared-Absent (independent). The contrasting non-conformant version is the same form with the same conditional logic audited node by node only: every field passes its five criterion elements while the dependency graph is absent, a blocking failure under rubric 2.6. Light instrument-framing note that a form field is the form-modality instantiation of an instrument; no existing example field, outcome, conformance threshold, or mapping changed. |
| 0.1.4 | 2026-06-13 | Frame Language own-voice vocabulary pass. Recasts: own-voice "compliance" recast to "conformance" (Example 3 "the conformance specification"); "accountability/accountable (of the legal party)" recast to "answerability/answerable" (distinct entities with different answerability structures; the Example 5 legal entity instrument criterion intent). Residual prior-primitive wording finished: "Single Governance"/"Single governance" recast to "Single Continuity"/"Single continuity capacity" in Example 6 Pattern A heading and assessment, matching the Continuity Capacity rename already propagated at v0.1.3. Kept as admissible: the quoted published form option list "Code | Community | Research | Governance | Other" and the prose critiquing the ambiguity of its "Governance" option (Example 2); the authored "Governance" contribution-category option definition (named domain concept, on-chain/off-chain governance); the named technical concept "governance token / governance token contract" (Example 6 Pattern B); the historical changelog record naming the prior Governance Resilience primitive. No example field, outcome, conformance threshold, or mapping changed; vocabulary only. |
| 0.1.3 | 2026-06-08 | Primitive rename cascade propagated: the Governance Resilience instrument is now the Continuity Capacity instrument in Example 6, completing the Foundation v0.1.7 rename in this companion. No example content or outcome changed; naming only. |
| 0.1.2 | 2026-05-18 | Example 6 added: Gate Declaration Fields (Section 3.8). Three patterns: grant-only with single governance (clean), undisclosed commercial revenue (non-conformant with corrected version), returning applicant with partially fulfilled prior obligation (conformant disclosure). |
| 0.1.1 | 2026-05-17 | Example 5 added: The Organizational Identity Declaration. Before/after from the Epoch 12 evaluation cycle. Three patterns from evaluation (unverifiable attribution, self-reference inconsistency, prior employer work as independent) with WALKRI-conformant specifications for all three identity instruments and a WALKRI audit result table. |
| 0.1.0 | 2026-05-15 | Initial draft. Four examples from the Epoch 12 evaluation cycle: DPG eligibility field (Example 1), Contributions single-select field (Example 2), well-specified prior grant funding field as positive case (Example 3), and upstream value analysis (Example 4). |
