---
title: WALKRI Runbooks
version: 0.1.2
date: 2026-05-18
license: CC0
status: Working draft. Companion to WALKRI-standard-0_1_0.md (v0.1.4).
parent_standard: WALKRI v0.1.4 (github.com/CrossWalkri/WALKRI)
companion_cross_document: CROSS-runbooks-0_1_0.md
---

## Purpose

WALKRI runbooks are pre-audited field specification packages for common program contexts. Each runbook provides a complete set of WALKRI-conformant field definitions that a program can adopt as a starting configuration and modify. They lower the barrier to WALKRI conformance by providing deployable field sets rather than requiring programs to build specifications from scratch against the full standard.

The pairing with CROSS runbooks works as follows. CROSS runbooks specify the obligation architecture: what type of obligation is being funded, which gates apply, and what evidence strength is required at each gate. WALKRI runbooks specify the field set that collects the data to satisfy that obligation architecture. Selecting the matching CROSS and WALKRI runbooks gives a program a complete, ready-to-publish round configuration without needing to build either side from scratch.

The intended workflow is: a program selects the runbook that best matches their context, reviews each field specification, modifies what needs to change for their specific round, and adds any program-specific fields not covered by the runbook. Fields can be changed, removed, or added. The audit record documents which runbook was the starting point and what modifications were made. The runbook is a starting configuration, not a locked template.

Each field in a runbook carries one of three customization status values. Core fields carry the obligation architecture's minimum requirements and should not be removed without documented justification. Suggested fields are common for this context but may not apply to every program using this runbook. Optional fields are included as examples of additional precision a program may want and carry no conformance obligation.

---

## Part I: CROSS-Paired Runbooks

These six runbooks correspond directly to the six CROSS runbooks. A program selecting a CROSS runbook should use the matching WALKRI runbook as the starting field set.

---

### 1. Discovery Sprint

Matching CROSS runbook: Discovery Sprint (build obligation, small grant, self-report evidence).

Context: A program funding an early-stage build with a specific deliverable. The primary obligation is producing a specified artifact. Entry evidence is a falsifiable deliverable specification. Completion evidence is the artifact's existence and public accessibility.

---

**Legal entity or individual name** [Core]

Criterion intent: Identify the natural person or registered organization accountable for delivering the grant obligations and receiving disbursement.

Operational definition: The name as it appears in the jurisdiction of registration for organizations, or the full legal name for individuals. A project name, display name, or GitHub organization name does not satisfy this field unless it is the legal name. Where no legal entity exists, the individual who assumes personal accountability for the obligation must be named explicitly.

Response form: Short text. Justification: the legal name is a single, unambiguous string. Free prose is not appropriate because it permits aliases, display names, and partial names.

Evidence form: Public organizational registration database query returning the named entity and jurisdiction, or government-issued ID for individuals. Registration number or equivalent public identifier must accompany the name for organizations.

Status: Core

---

**Revenue architecture declaration** [Core]

Use the full specification from WALKRI Section 3.8: Revenue architecture instrument. Status: Core. The grant-only type requires only the single-select; fee-for-service, commercial, and hybrid types require the additional sub-fields. For a Discovery Sprint round, most applicants will be grant-only; the field provides baseline documentation and catches exceptions.

---

**Development stage declaration** [Core]

Use the full specification from WALKRI Section 3.8: Development stage instrument. Status: Core. For Discovery Sprint, the expected stage is Stage 1 (proof of concept) or Stage 2 (early adoption); a Stage 3 or higher applicant in a Discovery Sprint round should be flagged for stage-round alignment review, as the Discovery Sprint runbook is calibrated for early-stage work.

---

**Deliverable specification** [Core]

Criterion intent: Identify the artifact the grant will produce, with completion criteria specific enough that a reviewer who did not commission the work could independently verify whether they were met.

Operational definition: A description of the artifact type (library, tool, contract, dataset, documentation set, or other named type), the completion criteria stated as verifiable conditions rather than aspirational descriptions, and the public location where the completed artifact will be accessible. Completion criteria must be falsifiable: a criterion that cannot be answered yes or no by an independent reviewer is not a completion criterion.

Response form: Long text. Justification: the deliverable and its completion criteria require narrative to specify adequately; structured fields cannot capture the range of valid deliverable types.

Evidence form: At completion gate, the artifact exists at the declared public location, is accessible without authentication, and meets each named completion criterion verifiable by an independent reviewer.

Status: Core

---

**Public repository or artifact location** [Core]

Criterion intent: Named public URL where the funded work will be hosted and where progress and completion can be independently verified.

Operational definition: A URL resolving to a public repository, published package, deployed application, or equivalent public location controlled by the applicant. The URL must be accessible without authentication. A private repository link does not satisfy this field.

Response form: URL. Justification: the response is a single, machine-verifiable string. A text field would permit partial URLs, narrative descriptions of location, or inaccessible private links.

Evidence form: URL resolves at time of entry and at time of completion; content is publicly accessible; the artifact named in the deliverable specification is present.

Status: Core

---

**Open license declaration** [Core]

Criterion intent: Confirm that the funded work will be released under a named open license permitting use, modification, and distribution without restriction, consistent with the public goods claim.

Operational definition: A named SPDX license identifier (e.g. MIT, Apache-2.0, GPL-3.0-only) applied to the artifact at or before completion. A reference to "open source" or "open license" without a named SPDX identifier does not satisfy this field. A license restricting commercial use, requiring special permission for redistribution, or expiring after a period does not satisfy this field.

Response form: Single-select from a list of accepted SPDX identifiers, plus a text field for the location of the license file in the repository. Justification: constraining to a named SPDX list prevents applicants from self-certifying licenses that do not meet the open license standard.

Evidence form: The named SPDX license identifier appears in a LICENSE file at the root of the repository or in the package manifest at time of completion.

Conformance threshold: Accepted identifiers are any OSI-approved SPDX identifiers. The conformance threshold is: the SPDX identifier is named explicitly, the license file exists in the repository root or package manifest, and the license is in the OSI-approved list. A license that restricts commercial use (e.g. CC-BY-NC) does not satisfy this threshold regardless of how it is labeled.

Status: Core

---

**Concurrent funding disclosure** [Core]

Criterion intent: Identify all active grants, investments, and revenue sources from the prior 24 months related to the scope of this application, so the committee can assess additionality and avoid double-funding the same work.

Operational definition: For each source: the name of the funder, investor, or revenue origin; the approximate amount; the relationship to the scope of this application (same deliverable, adjacent scope, or different scope); and whether ongoing reporting or milestone obligations to that source exist. "None" is a valid response only if no grants, investments, or material revenue related to this scope exist in the prior 24 months. A response of "none" when prior funding exists is a disqualifying misrepresentation.

Response form: Long text with structured sub-fields: source name, amount, relationship to this application's scope, ongoing obligations (yes/no). Justification: the field must capture multiple sources with different relationships to the scope; a single text field risks omission; structured sub-fields make completeness verifiable.

Evidence form: Disclosed sources are cross-referenceable against public grant records (KarmaGAP, Gitcoin Explorer, RPGF recipient lists) and chain explorer data. Non-disclosed sources identified through independent research constitute a material discrepancy.

Status: Core

---

**Additionality statement** [Core, required when concurrent funding is disclosed]

Criterion intent: Identify specifically what this grant funds that concurrent sources do not, so the committee can confirm that the public goods ask represents marginal contribution rather than subsidy of work already funded.

Operational definition: A narrative specifying: (1) which part of the deliverable or which development stages this grant covers relative to other funders; (2) where overlap exists between this grant and concurrent sources, if any, and how double-funding of the same input is avoided; (3) an attestation that the applicant will not charge the same cost to multiple funders. If no concurrent funding exists, this field is not required.

Response form: Long text. Justification: the additionality argument requires narrative to articulate scope boundaries and overlap handling.

Evidence form: At entry gate, the additionality statement is internally consistent with the concurrent funding disclosure. At completion gate, outcome credit attribution is consistent with the additionality declared at entry.

Status: Core

---

**KarmaGAP profile** [Suggested]

Criterion intent: Named public profile on KarmaGAP documenting the applicant's prior grant history, milestone completion record, and funder relationships.

Operational definition: A URL resolving to an active KarmaGAP profile for the applying entity or its key personnel. A profile created at application time with no prior history satisfies the format requirement but not the track record requirement. The profile URL must resolve without authentication.

Response form: URL. Justification: the profile is a single public record accessible by URL.

Evidence form: URL resolves to a KarmaGAP profile. Milestone completion rate and history are assessed by the reviewer independently from the application.

Status: Suggested

---

### 2. Staged Development

Matching CROSS runbook: Staged Development (build obligation at Stage 1, change obligation at Stage 2, continuation gate active).

Context: A multi-stage program where Stage 1 funds the build of an artifact and Stage 2 funds the demonstration of measurable uptake or impact. The WALKRI runbook for Staged Development includes all Discovery Sprint Core fields plus Stage 2 fields for the change obligation phase. The Stage 2 fields below apply at Stage 2 entry and are not required at Stage 1 entry.

All Discovery Sprint Core fields apply at Stage 1 entry. The following fields are added for Stage 2.

---

**Revenue architecture declaration** [Core]

Use the full specification from WALKRI Section 3.8: Revenue architecture instrument. Status: Core. The grant-only type requires only the single-select; fee-for-service, commercial, and hybrid types require the additional sub-fields.

---

**Development stage declaration** [Core]

Use the full specification from WALKRI Section 3.8: Development stage instrument. Status: Core. For Staged Development, Stage 1 is the expected declaration for Stage 1 applications; Stage 2 is expected for Stage 2 applications. The stage declaration must be consistent with which stage the application covers. An applicant declaring Stage 3 while applying to Stage 1 should be questioned about why they are in a Staged Development round rather than a Growth-stage round.

---

**FROM state (baseline condition)** [Core, Stage 2]

Criterion intent: Named, measurable condition that exists before the Stage 2 intervention, established from an independent data source, documenting the gap that Stage 1's artifact is positioned to address.

Operational definition: A sentence or paragraph identifying: the specific condition or absence (e.g. "No library exists for X, as of [date], which produces problem Y in Z ecosystem"), a quantified baseline where applicable, the population or system affected, and the named independent data source. "We will improve X" is not a FROM state. A FROM state must be a specific, sourced observation of a current condition, not a statement of intent.

Response form: Long text. Justification: the FROM state requires narrative specification of multiple elements that cannot be captured by structured fields without losing the causal reasoning.

Evidence form: Named data source resolves and is publicly accessible; the quoted condition or statistic is present in or derivable from the source; date of access is specified.

Status: Core

---

**TO state (target condition)** [Core, Stage 2]

Criterion intent: Named, measurable end-state the Stage 2 grant is intended to produce, expressed in the same units and for the same population or system as the FROM state.

Operational definition: A sentence identifying: the specific measurable condition at grant end, the population or system, the unit and direction of change, and the measurement date. The TO state must use the same unit as the FROM state. A TO state that cannot be compared to the FROM state using the same measurement instrument is not a valid TO state.

Response form: Long text. Justification: articulating outcome targets requires narrative that structured fields cannot capture without losing necessary qualifications.

Evidence form: Units match the FROM state; the target is directionally consistent with the stated intervention logic; the measurement method for the TO state is named.

Status: Core

---

**Continuation intent declaration** [Suggested]

Criterion intent: Confirm that the applicant understands the Stage 2 entry requirements and intends to apply for Stage 2 continuation, so the committee can assess whether the Stage 1 deliverable is designed for measurable Stage 2 uptake.

Operational definition: A brief statement confirming: (1) the applicant understands that Stage 2 entry requires demonstration of measurable uptake or impact of the Stage 1 artifact; (2) the Stage 1 deliverable is designed with Stage 2 measurement in mind; (3) the applicant intends to apply for Stage 2 if Stage 1 completion criteria are met. A declaration of intent to not apply for Stage 2 is a valid response and does not affect Stage 1 eligibility.

Response form: Binary (yes/no for intent to apply for Stage 2), plus a short text field for the measurement approach the applicant anticipates using at Stage 2. Justification: the binary captures the intent; the text field captures whether the applicant has thought concretely about Stage 2 measurement.

Evidence form: Internal consistency check only at entry; no external evidence required. At Stage 2 entry gate, the Stage 1 artifact must meet the completion criteria declared at Stage 1 entry.

Status: Suggested

---

### 3. Community Allocation

Matching CROSS runbook: Community Allocation (retroactive obligation, conviction-weighted community review).

Context: A program rewarding demonstrated prior contribution to the community. The obligation object is the prior contribution itself. The field set focuses on evidence of prior work, usage by non-team members, and community validation.

---

**Revenue architecture declaration** [Core]

Required at all entry gates. Applicant classifies revenue architecture as grant-only, fee-for-service, commercial, or hybrid. Commercial and hybrid types require an additionality boundary statement specifying what this grant funds that commercial revenue does not. Activates concurrent funding disclosure review for commercial and hybrid types. [CROSS v0.3.6, Part II, Revenue Architecture; WALKRI Section 3.8]

Status: Core

---

**Development stage declaration** [Core]

Required at all entry gates. Applicant classifies development stage as Stage 1 (proof of concept) through Stage 5 (retroactive recognition). Declaration must include an explanation and at least one piece of independently verifiable evidence consistent with the declared stage. Stage declarations inconsistent with the obligation mode committed to require explanation. [CROSS v0.3.6, Part IV; WALKRI Section 3.8]

Status: Core

---

**Prior contribution description** [Core]

Criterion intent: Identify the specific prior work being submitted for community recognition, with enough specificity that a reviewer who did not commission the work could independently verify its existence and scope.

Operational definition: A narrative describing: the artifact, protocol, project, or body of work; the dates of active contribution; the applicant's role in producing it; and where it is publicly accessible. Generic descriptions of a category of work ("we have been building in web3 for X years") do not satisfy this field. The description must be specific enough that an independent reviewer could locate the work without further contact with the applicant.

Response form: Long text. Justification: the nature of prior contributions varies too widely for structured fields to capture without losing specificity.

Evidence form: Artifacts named in the description are publicly accessible. Named repositories, deployed contracts, or published materials exist at the stated locations.

Status: Core

---

**Usage evidence** [Core]

Criterion intent: Demonstrate that the prior contribution has been used or built upon by parties outside the applicant's organization, at a scale and in a manner verifiable from public sources.

Operational definition: Evidence of use by non-team members, from sources the applicant does not control. Qualifying evidence includes: download counts from package registries (npm, PyPI, crates.io); dependent repositories in production codebases from non-team organizations; on-chain transaction counts initiated by non-team addresses; named third-party integrations confirmed by those organizations' own communications; independent press coverage or citations. The applicant's own reports of use, without corroboration from a source outside their control, do not satisfy this field.

Response form: Long text with named evidence items, each with a source URL. Justification: usage evidence types are heterogeneous and must be specified with independent source references to be verifiable.

Evidence form: Each named evidence item resolves to an independently accessible source. The source is not controlled by the applicant. The evidence is current to within 12 months of the application date.

Status: Core

---

**Prior funding disclosure** [Core]

Criterion intent: Identify all prior grants, retroactive awards, and investment received for the work being submitted, so the committee can assess additionality and community validation independent of funded promotion.

Operational definition: For retroactive applications, the disclosure covers all prior grants, retroactive awards, and investment received for the work being submitted, not only sources active in the prior 24 months. For each source: the name of the funder, investor, or revenue origin; the approximate amount; the relationship to the work being submitted (same work, adjacent scope, or different scope); and whether ongoing reporting or milestone obligations to that source exist. "None" is a valid response only if no grants, investments, or material revenue related to the submitted work exist. A response of "none" when prior funding exists is a disqualifying misrepresentation.

Response form: Long text with structured sub-fields: source name, amount, relationship to this submission's scope, ongoing obligations (yes/no). Justification: the field must capture multiple sources with different relationships to the scope; structured sub-fields make completeness verifiable.

Evidence form: Disclosed sources are cross-referenceable against public grant records and chain explorer data. Non-disclosed sources identified through independent research constitute a material discrepancy.

Status: Core

---

**Community validation** [Suggested]

Criterion intent: Identify named members of the community who can attest independently that the prior contribution has been valuable to their work, without being solicited or coached by the applicant.

Operational definition: Named individuals (not anonymous) who have publicly stated that the contribution has been useful, in a context the applicant did not create or control (forum posts, GitHub comments, social media posts, published documentation that cites the work). The applicant may provide links to public statements; they may not solicit statements for the purpose of this application.

Response form: Long text with named individuals and links to their public statements. Justification: community validation is inherently narrative and relational; structured fields cannot capture the nature of the relationship.

Evidence form: Named individuals are independently findable. Links resolve to public statements that are attributable to the named individual and made in a context the applicant did not create.

Status: Suggested

---

### 4. Retroactive Impact

Matching CROSS runbook: Retroactive Impact (retroactive obligation, usage and outcome evidence scope at continuation).

Context: Stronger evidentiary requirements than Community Allocation. Evidence must demonstrate not just usage but measurable change attributable to the contribution.

All Community Allocation Core fields apply. The following field is added.

---

**Revenue architecture declaration** [Core]

Required at all entry gates. Applicant classifies revenue architecture as grant-only, fee-for-service, commercial, or hybrid. Commercial and hybrid types require an additionality boundary statement specifying what this grant funds that commercial revenue does not. Activates concurrent funding disclosure review for commercial and hybrid types. [CROSS v0.3.6, Part II, Revenue Architecture; WALKRI Section 3.8]

Status: Core

---

**Development stage declaration** [Core]

Required at all entry gates. Applicant classifies development stage as Stage 1 (proof of concept) through Stage 5 (retroactive recognition). Declaration must include an explanation and at least one piece of independently verifiable evidence consistent with the declared stage. Stage declarations inconsistent with the obligation mode committed to require explanation. [CROSS v0.3.6, Part IV; WALKRI Section 3.8]

Status: Core

---

**Outcome evidence** [Core]

Criterion intent: Demonstrate that the prior contribution produced a measurable change in the ecosystem, protocol, or community it was designed to serve, independently of the applicant's own report.

Operational definition: A named measurable change with: the condition before the contribution existed (baseline), the condition after (post-intervention), the unit of measurement, and the independent data source for each. The measuring party must be named and must be outside the applicant's organization. Social media posts, testimonials, and institutional endorsements do not constitute outcome evidence. On-chain data, published analytics, independent audits, and third-party research papers do.

Response form: Long text with structured sub-fields: the baseline condition with source, the post-intervention condition with source, the independent measuring party. Justification: outcome evidence requires specification of baseline, post-intervention, and measurement method; these cannot be captured in an unstructured text field.

Evidence form: Baseline and post-intervention data are publicly accessible from named sources outside the applicant's control. The measuring party is independently identifiable. The change is directionally consistent with the contribution's stated function.

Status: Core

---

### 5. Graduated Evidence

Matching CROSS runbook: Graduated Evidence (change obligation, multi-stage, escalating evidence, sustainability plan required).

Context: A multi-stage program with escalating evidence requirements at each stage. Stage 1 requires activity evidence. Stage 2 requires outcome evidence. The continuation gate requires a sustainability assessment. The field set covers the full change-obligation indicator specification.

All Staged Development Core fields apply. The following fields are added.

---

**Revenue architecture declaration** [Core]

Required at all entry gates. Applicant classifies revenue architecture as grant-only, fee-for-service, commercial, or hybrid. Commercial and hybrid types require an additionality boundary statement specifying what this grant funds that commercial revenue does not. Activates concurrent funding disclosure review for commercial and hybrid types. [CROSS v0.3.6, Part II, Revenue Architecture; WALKRI Section 3.8]

Status: Core

---

**Development stage declaration** [Core]

Required at all entry gates. Applicant classifies development stage as Stage 1 (proof of concept) through Stage 5 (retroactive recognition). Declaration must include an explanation and at least one piece of independently verifiable evidence consistent with the declared stage. Stage declarations inconsistent with the obligation mode committed to require explanation. [CROSS v0.3.6, Part IV; WALKRI Section 3.8]

Status: Core

---

**Indicator specification** [Core]

Criterion intent: Identify the specific measurement instrument that will document progress from the FROM state toward the TO state, with enough precision that the same instrument can be applied consistently across reporting periods.

Operational definition: The indicator name (a short label), the unit of measurement, the direction of desirable change (increase or decrease), the counting rule (how one unit is counted, what is included and excluded), the data source, the collection method (how the data will be gathered), and the collection frequency. An indicator that cannot be consistently applied by two independent data collectors using the stated counting rule is not sufficiently specified.

Response form: Structured sub-fields: indicator name (short text), unit (short text), direction (single-select: increase/decrease), counting rule (long text), data source (short text), collection method (short text), collection frequency (single-select or short text). Justification: each sub-field captures a distinct specification element; combining them in a single text field produces incomparable responses.

Evidence form: The counting rule is applied consistently in progress reporting. The data source resolves and is accessible. The collection method is replicable by an independent party.

Status: Core

---

**Sustainability plan** [Core]

Criterion intent: Identify how the work and its outcomes will continue after the grant period ends, so the committee can assess whether the public benefit claimed will persist beyond the funded period.

Operational definition: A statement covering: what happens to the funded work at the end of the grant period (who maintains it, under what conditions it remains accessible, what operational costs are required to sustain it); how those costs will be covered after the grant ends (self-funding, successor grant, revenue, community contribution, or protocol treasury), with enough specificity for a reviewer to assess plausibility; and where the work reaches a defined end state after which maintenance is not required, a specification of that end state and the conditions under which it will be declared reached.

Response form: Long text. Justification: sustainability arrangements are too varied to capture in structured fields without losing the specificity needed to assess plausibility.

Evidence form: The stated continuation mechanism is internally consistent with the applicant's current resource position (as declared in the sufficiency architecture declaration). Named successor organizations or community contributors are independently identifiable.

Status: Core

---

**Data cost estimation** [Suggested]

Criterion intent: Confirm that data collection for the specified indicator is operationally feasible within the project budget, so the committee can assess whether the indicator will actually be measured or will be abandoned when collection costs are encountered.

Operational definition: An estimate of the cost of collecting indicator data for one reporting period (in time, money, or both), and a statement of which line item in the project budget covers that cost. "Low cost" or "minimal effort" without a specific estimate does not satisfy this field.

Response form: Short text for the cost estimate, short text for the budget line item covering it. Justification: the two elements are distinct and should be captured separately to allow independent assessment of each.

Evidence form: The budget line item is present in the submitted project budget. The cost estimate is plausible relative to the collection method described in the indicator specification.

Status: Suggested

---

### 6. Institutional Conformance

Matching CROSS runbook: Institutional Conformance (change obligation, all gates at independent review, counterfactual reference required, IP ownership required).

Context: Programs seeking institutional co-funding or satisfying USAID, OECD DAC, or comparable compliance requirements. Full PIRS-compatible field set. All fields audited to the highest evidence strength.

All Graduated Evidence Core fields apply. The following fields are added.

---

**Revenue architecture declaration** [Core]

Required at all entry gates. Applicant classifies revenue architecture as grant-only, fee-for-service, commercial, or hybrid. Commercial and hybrid types require an additionality boundary statement specifying what this grant funds that commercial revenue does not. Activates concurrent funding disclosure review for commercial and hybrid types. [CROSS v0.3.6, Part II, Revenue Architecture; WALKRI Section 3.8]

Status: Core

---

**Development stage declaration** [Core]

Required at all entry gates. Applicant classifies development stage as Stage 1 (proof of concept) through Stage 5 (retroactive recognition). Declaration must include an explanation and at least one piece of independently verifiable evidence consistent with the declared stage. Stage declarations inconsistent with the obligation mode committed to require explanation. [CROSS v0.3.6, Part IV; WALKRI Section 3.8]

Status: Core

---

**Counterfactual reference** [Core]

Criterion intent: Document what would have occurred without the intervention, as the attribution baseline required for causal claims about the grant's contribution to the observed outcome.

Operational definition: A named comparison condition or comparison group against which the grant outcome is attributed. The counterfactual must name: the specific counterfactual scenario (what would have happened without the intervention), the rationale for why this scenario is a plausible counterfactual (not just "nothing would have happened"), and either a comparison group (a population not receiving the intervention) or a historical trend extrapolation with stated assumptions. A counterfactual that rests solely on the applicant's assertion that no other factors contributed to the outcome does not satisfy this field.

Response form: Long text. Justification: counterfactual arguments are inherently narrative and contextual; structured fields cannot capture the range of valid counterfactual types or the necessary reasoning.

Evidence form: The counterfactual scenario is internally consistent with the FROM state evidence. The comparison group or historical trend is independently accessible from a named public source. The rationale addresses the main alternative explanations for the observed change.

Status: Core

---

**IP ownership declaration** [Core]

Criterion intent: Identify who holds rights in the outputs of the funded work, under what terms those rights are held, and what the public's rights of access and use are, so the committee can verify that the public goods claim is consistent with the intellectual property position.

Operational definition: A statement specifying: the name of the party or parties who will hold intellectual property rights in the outputs at the time of completion; the terms under which those rights are held (exclusive, licensed, open, or other); and whether a third party could use, fork, or build upon the outputs without seeking permission from any rights holder. An output claimed as a public good over which the applicant holds exclusive rights without an open license does not satisfy the public goods claim without explanation of how the exclusive rights are compatible with the public benefit.

Response form: Long text. Justification: IP arrangements are legally complex and vary widely; structured fields would either oversimplify or produce incomparable responses.

Evidence form: The declared license is present in the repository or attached to the artifact at completion. The named rights holder is independently identifiable. If a patent is claimed or pending, the patent application or grant number is provided.

Status: Core

---

**Independent attestation declaration** [Core]

Criterion intent: Identify a named party outside the applicant's organization who will confirm that the evidence submitted at the completion gate meets the stated completion criteria, providing the independent review evidence strength required at this gate level.

Operational definition: The name and institutional affiliation of the independent reviewer, their qualification to assess the specific evidence type required (domain expertise relevant to the indicator), and their relationship to the applicant (confirming no Tier 1 or unwaived Tier 2 conflict of interest). A reviewer employed by the applicant's organization, holding equity in the applicant's project, or named as a team member or advisor on the applicant's public materials does not satisfy this field.

Response form: Structured sub-fields: reviewer name, institutional affiliation, qualification statement, relationship to applicant. Justification: each element is distinct and must be separately assessable.

Evidence form: The reviewer's institutional affiliation is publicly verifiable. Their domain qualification is consistent with the evidence type. No Tier 1 conflict of interest is present.

Status: Core

---

## Part II: Institutional Framework Runbooks

These three runbooks are not paired with a specific CROSS runbook. They are field sets designed to satisfy the intake requirements of specific institutional accountability frameworks. Programs selecting one of these runbooks produce data that satisfies the named framework's reporting requirements as a structural consequence of the field design.

---

### 7. USAID PIRS

Context: Programs required to produce USAID Performance Indicator Reference Sheet (PIRS) documentation for each indicator. USAID ADS 201 requires nine elements per indicator. The fields in this runbook correspond to those nine elements. A program using this runbook as their intake field set produces PIRS-compliant indicator documentation without additional work.

---

**Revenue architecture declaration** [Core]

Required at all entry gates. Applicant classifies revenue architecture as grant-only, fee-for-service, commercial, or hybrid. Commercial and hybrid types require an additionality boundary statement specifying what this grant funds that commercial revenue does not. Activates concurrent funding disclosure review for commercial and hybrid types. [CROSS v0.3.6, Part II, Revenue Architecture; WALKRI Section 3.8]

Note for USAID PIRS context: Development stage declarations in USAID-aligned programs should map to the USAID program cycle stages where applicable. Revenue architecture of commercial or hybrid type may affect USAID co-financing rules and should be flagged for compliance review.

Status: Core

---

**Development stage declaration** [Core]

Required at all entry gates. Applicant classifies development stage as Stage 1 (proof of concept) through Stage 5 (retroactive recognition). Declaration must include an explanation and at least one piece of independently verifiable evidence consistent with the declared stage. Stage declarations inconsistent with the obligation mode committed to require explanation. [CROSS v0.3.6, Part IV; WALKRI Section 3.8]

Note for USAID PIRS context: Development stage declarations in USAID-aligned programs should map to the USAID program cycle stages where applicable. Revenue architecture of commercial or hybrid type may affect USAID co-financing rules and should be flagged for compliance review.

Status: Core

---

**Indicator name** [Core] - maps to PIRS Element 1

Criterion intent: A short descriptive label for the indicator that is stable across reporting periods and consistent with how the indicator is referenced in the program's Performance Management Plan.

Operational definition: A noun phrase of ten words or fewer identifying what is being measured. The label must not change between reporting periods unless the indicator itself is formally revised. A label that describes a process rather than a measured condition is not a valid indicator name.

Response form: Short text. Justification: the indicator name is a single, stable label; longer text is not appropriate.

Evidence form: The indicator name is consistent with the label used in the program's Performance Management Plan and in all gate submissions.

Status: Core

---

**Indicator definition and unit** [Core] - maps to PIRS Element 2

Criterion intent: Specify what is being measured, how one unit is counted, and what the boundary of inclusion is, with enough precision that the indicator can be applied consistently by any data collector.

Operational definition: The unit of measurement (the thing being counted or measured, stated as a noun), the counting rule (what qualifies as one unit, what is excluded, and how partial cases are handled), and the scope of inclusion (the population or system to which the indicator applies). A definition that omits any of these three elements is incomplete. An indicator definition must be operationally identical to the field specification in the WALKRI indicator specification field: these two fields must be consistent.

Response form: Long text. Justification: the definition, unit, and counting rule require narrative to specify adequately without losing necessary precision.

Evidence form: The counting rule is applied consistently across all reporting periods. Any deviation from the stated counting rule is documented and disclosed in the gate submission.

Status: Core

---

**Disaggregation** [Core] - maps to PIRS Element 3

Criterion intent: Identify the categories by which indicator values will be reported separately, enabling analysis of differential outcomes across population segments.

Operational definition: Named disaggregation categories that the applicant commits to reporting for every data collection period. Categories committed to in the application may be added in subsequent periods but may not be removed without committee approval and documented rationale. "By geography and gender" without specifying the geographic units or the gender categories used does not satisfy this field. For each named category, the category definition must be stated (e.g. "sex: male, female, non-binary as self-reported" not simply "sex").

Response form: Multi-select from a list of standard disaggregation categories (geography, sex, age cohort, organization type, chain/network) plus a free-text field for custom categories. Justification: standardized categories enable cross-program comparison; the free-text field accommodates program-specific categories not on the standard list.

Evidence form: Reported indicator values in gate submissions are disaggregated by every category declared at application. Missing disaggregation without documented justification is a gate failure at the progress or completion gate.

Status: Core

---

**Rationale and relationship** [Core] - maps to PIRS Element 4

Criterion intent: Explain why this indicator was selected to measure the outcome, how it relates to the program's stated goal, and why alternative indicators were not selected, so the committee can assess indicator validity.

Operational definition: A statement covering: (1) why this specific measurement is the appropriate proxy for the program outcome; (2) how the indicator relates to the program's logic model or theory of change; (3) what the primary alternative indicators considered were, and why they were not selected. An indicator rationale that simply restates what the indicator measures without addressing validity is not a complete rationale.

Response form: Long text. Justification: the rationale requires narrative reasoning about indicator selection that cannot be captured in structured fields.

Evidence form: The stated rationale is internally consistent with the FROM state, TO state, and indicator specification. The relationship to the program logic is traceable.

Status: Core

---

**Data acquisition** [Core] - maps to PIRS Element 5

Criterion intent: Specify the named data source, how data will be collected, at what frequency, and what the cost of one collection cycle is, so the committee can assess operational feasibility and independent verifiability.

Operational definition: The field combines the WALKRI data source, collection method, and data cost estimation fields. Required elements: the named data source (specific enough that an independent party could locate it), the collection method (how data is gathered from that source), the collection frequency (how often data is gathered, tied to gate schedule), and the cost estimate for one collection period (in time and money, with the budget line item that covers it). "We will track this internally" without specifying the source or method does not satisfy this field.

Response form: Long text with structured sub-fields: data source (short text), collection method (short text), collection frequency (short text), cost estimate for one period (short text), budget line item (short text). Justification: each element is distinct; combining them in a single text field produces responses where individual elements cannot be independently assessed.

Evidence form: The named data source resolves and is publicly accessible (or the access mechanism is stated for non-public sources). The collection method is replicable. The cost estimate is plausible relative to the collection method. The budget line item is present in the submitted project budget.

Status: Core

---

**Data quality assessment procedure** [Core] - maps to PIRS Element 6

Criterion intent: Document the process by which the applicant will verify that collected data meets the five WALKRI data quality standards (validity, integrity, precision, reliability, timeliness) before submission.

Operational definition: A brief description of the quality check process for each collection period: who performs the check, what they check, and what a quality failure would produce (revision, disclosure, or gate flag). A statement that "data will be verified internally" without specifying the process does not satisfy this field. Where independent verification is required at the gate level, the quality check procedure must name the independent party and confirm their independence from the applicant's organization.

Response form: Long text. Justification: quality check procedures vary by indicator type and collection context.

Evidence form: The described procedure is consistent with the indicator's data source and collection method. Where independent verification is required at the gate level, the quality check procedure names the independent party.

Status: Core

---

**Baseline** [Core] - maps to PIRS Element 7

Criterion intent: Document the condition that exists before the intervention, from an independent data source, against which progress toward the TO state will be measured.

Operational definition: This field uses the WALKRI FROM state specification. The baseline must include: a specific, quantified condition (not a qualitative description), the population or system to which it applies, the date of measurement, and the named independent data source. A baseline of "zero" or "none" is acceptable only when the intervention is introducing something that does not currently exist, and the source documenting that absence must still be named.

Response form: Long text. Justification: the baseline requires narrative specification of multiple elements that structured fields cannot capture without losing necessary precision.

Evidence form: Named data source resolves and is publicly accessible. The quoted condition or statistic is present in or derivable from the source. Date of access is specified.

Status: Core

---

**Targets** [Core] - maps to PIRS Element 8

Criterion intent: State the specific, measurable end-state the program is intended to produce, in the same units as the baseline, with a target date.

Operational definition: This field uses the WALKRI TO state specification. The target must be expressed in the same unit as the baseline, apply to the same population or system, and name the date by which the target is expected to be reached. A target that is expressed in different units from the baseline, or that applies to a different population, is not comparable and does not satisfy this field.

Response form: Long text. Justification: articulating outcome targets requires narrative that structured fields cannot capture without losing necessary qualifications.

Evidence form: Units match the baseline. The target date is consistent with the grant period. The measurement method for the target is the same as for the baseline.

Status: Core

---

**Indicator limitations** [Core] - maps to PIRS Element 9

Criterion intent: Document known limitations of the indicator that a reviewer or downstream analyst should understand when interpreting reported values.

Operational definition: A brief statement of: what the indicator does not measure that a naive reader might assume it measures; any counting rule limitations that affect comparability across periods or contexts; and any conditions under which the indicator would produce misleading results. A statement that there are "no significant limitations" requires justification for why the indicator is free from the standard limitations affecting its type.

Response form: Long text. Justification: limitations are contextual and cannot be captured by structured fields without losing the specificity needed to understand their significance.

Evidence form: No external evidence required. Consistency check only: the stated limitations are consistent with the counting rule and data source declared elsewhere in the indicator specification.

Status: Core

---

### 8. OECD DAC

Context: Programs aligning to the six OECD DAC evaluation criteria (Relevance, Coherence, Effectiveness, Efficiency, Impact, Sustainability). The fields in this runbook are designed to ensure that the intake data supports evaluation against all six criteria. Programs using this runbook collect, at intake, the information needed to conduct a DAC-aligned evaluation at completion without requiring supplementary data gathering.

---

**Revenue architecture declaration** [Core]

Required at all entry gates. Applicant classifies revenue architecture as grant-only, fee-for-service, commercial, or hybrid. Commercial and hybrid types require an additionality boundary statement specifying what this grant funds that commercial revenue does not. Activates concurrent funding disclosure review for commercial and hybrid types. [CROSS v0.3.6, Part II, Revenue Architecture; WALKRI Section 3.8]

Note for OECD DAC context: Revenue architecture declarations affect DAC co-financing attribution. Hybrid and commercial revenue types require additionality arguments consistent with DAC blended finance principles.

Status: Core

---

**Development stage declaration** [Core]

Required at all entry gates. Applicant classifies development stage as Stage 1 (proof of concept) through Stage 5 (retroactive recognition). Declaration must include an explanation and at least one piece of independently verifiable evidence consistent with the declared stage. Stage declarations inconsistent with the obligation mode committed to require explanation. [CROSS v0.3.6, Part IV; WALKRI Section 3.8]

Note for OECD DAC context: Revenue architecture declarations affect DAC co-financing attribution. Hybrid and commercial revenue types require additionality arguments consistent with DAC blended finance principles.

Status: Core

---

**Relevance statement** [Core] - addresses DAC criterion: Relevance

Criterion intent: Identify the specific need or problem this program addresses, for whom, and why the intervention is an appropriate response to that need.

Operational definition: A statement covering: the population or system experiencing the need, the specific nature of the need as documented from an independent source, and the mechanism by which this program addresses it. Generic claims that a program addresses "public goods funding gaps" or "ecosystem development" without specifying the population and need do not satisfy this field. The named independent source must be accessible and must document the stated need.

Response form: Long text. Justification: relevance requires narrative specification of population, need, and intervention logic; structured fields cannot capture this without losing necessary specificity.

Evidence form: The named independent source resolves and documents the stated need. The connection between the stated need and the program's design is traceable.

Status: Core

---

**Coherence statement** [Core] - addresses DAC criterion: Coherence

Criterion intent: Identify other known interventions in the same problem area, assess whether this program is additive or duplicative relative to them, and explain how the program's approach is coordinated with or differentiated from those interventions.

Operational definition: A statement covering: the two or three most prominent comparable programs or interventions in the same problem area; for each, how the scope of this program relates (complementary, different population, different approach, or potential overlap); and whether any coordination exists or is planned with those programs. A coherence statement that does not name any comparable programs, or that asserts no comparable programs exist, requires justification for why the problem area is uncontested.

Response form: Long text. Justification: coherence requires relational reasoning about multiple external programs; structured fields would require listing comparable programs individually, which loses the reasoning about their relationship.

Evidence form: Named comparable programs are independently findable. The characterization of their scope and the stated relationship to this program are internally consistent with the program's own scope description.

Status: Core

---

**Effectiveness specification** [Core] - addresses DAC criterion: Effectiveness

Criterion intent: State the specific outcome the program will achieve, the baseline condition it is changing, and the indicator by which progress will be measured, so the committee can assess at completion whether the program was effective.

Operational definition: This field combines the WALKRI FROM state, TO state, and indicator specification fields. All three must be present and internally consistent. The FROM state must be quantified and sourced. The TO state must be in the same units as the FROM state. The indicator must be specified with counting rule, data source, and collection method. A narrative about intended effectiveness without a quantified baseline and target does not satisfy this field.

Response form: Long text structured as: FROM state (with source), TO state (with target date), indicator specification (with counting rule, source, and method). Justification: the three elements are distinct and must be separately assessable; they require narrative to specify adequately.

Evidence form: FROM state data source resolves. Units are consistent between FROM and TO state. Indicator counting rule is specific enough to be applied by an independent party.

Status: Core

---

**Efficiency assessment** [Core] - addresses DAC criterion: Efficiency

Criterion intent: Document the resources required to achieve the stated outcome and assess whether the input-to-outcome ratio is reasonable relative to comparable interventions.

Operational definition: A statement covering: the total resources required (grant amount plus in-kind or matched resources), broken down by major input category (personnel, infrastructure, data collection, overhead); the expected output and outcome per unit of resource; and one or more comparable interventions with a stated cost-effectiveness comparison. "Cost-effective" without a comparator does not satisfy this field. The comparator must be named and independently accessible.

Response form: Long text with structured sub-fields: total resource input (short text), resource breakdown (long text), output and outcome per unit of resource (short text), named comparator with source (long text). Justification: efficiency assessment requires both structured cost data and narrative reasoning about the comparator; these cannot be collapsed into a single field.

Evidence form: The resource breakdown is internally consistent with the submitted budget. The named comparator resolves and supports the stated comparison.

Status: Core

---

**Impact theory** [Core] - addresses DAC criterion: Impact

Criterion intent: Describe the long-term change this program is intended to contribute to, beyond the immediate outcome, and the logic by which the program's outputs and outcomes lead to that longer-term change.

Operational definition: A statement covering: the long-term change the program is intended to contribute to (the impact level, distinct from the immediate outcome), the causal pathway from the program's outputs and outcomes to that impact, and the assumptions that must hold for that causal pathway to function. An impact claim that cannot be distinguished from the immediate outcome is not an impact statement. An impact statement without named causal pathway assumptions does not satisfy this field.

Response form: Long text. Justification: impact theory requires narrative specification of causal chains and assumptions; structured fields cannot capture this without losing the reasoning.

Evidence form: The causal pathway is internally consistent with the program's design. The assumptions are stated explicitly and are testable in principle.

Status: Core

---

**Sustainability plan** [Core] - addresses DAC criterion: Sustainability

Criterion intent: Identify how the work and its outcomes will continue after the grant period ends. This field uses the same specification as the WALKRI sustainability plan field defined in the Graduated Evidence runbook.

Operational definition: Applies the Graduated Evidence sustainability plan operational definition without modification. Required elements: what happens to the funded work at grant end, how operational costs will be covered after the grant ends, and (where applicable) the conditions under which the work reaches a defined end state requiring no further maintenance.

Response form: Long text. Justification: sustainability arrangements are too varied for structured fields without losing the specificity needed to assess plausibility.

Evidence form: The stated continuation mechanism is internally consistent with the applicant's current resource position. Named successor organizations or community contributors are independently identifiable.

Status: Core

---

### 9. DPG Standard

Context: Programs requiring Digital Public Good qualification as a gate criterion. This runbook provides pre-audited field specifications for assessing all nine DPG Standard indicators (github.com/DPGAlliance/DPG-Standard, tag v1.1.7) with explicit conformance thresholds for each.

Registry note: the DPGA registry records past assessments at the time of registration, not current qualification status. Registry membership accepted as evidence at the time of registration does not constitute evidence of current compliance with each indicator. The conformance threshold for each indicator below specifies whether registry membership is accepted as sufficient evidence or whether independent indicator assessment is required regardless of registry status. Programs should assume independent indicator assessment is required unless the threshold note explicitly accepts registry membership.

---

**Revenue architecture declaration** [Core]

Required at all entry gates. Applicant classifies revenue architecture as grant-only, fee-for-service, commercial, or hybrid. Commercial and hybrid types require an additionality boundary statement specifying what this grant funds that commercial revenue does not. Activates concurrent funding disclosure review for commercial and hybrid types. [CROSS v0.3.6, Part II, Revenue Architecture; WALKRI Section 3.8]

Note for DPG Standard context: Development stage Stage 1-2 declarations must be consistent with the DPG registry's "nominee" vs "confirmed" status requirements. A Stage 3-4 project applying for DPG confirmation should have more comprehensive evidence than a Stage 1 nominee.

Status: Core

---

**Development stage declaration** [Core]

Required at all entry gates. Applicant classifies development stage as Stage 1 (proof of concept) through Stage 5 (retroactive recognition). Declaration must include an explanation and at least one piece of independently verifiable evidence consistent with the declared stage. Stage declarations inconsistent with the obligation mode committed to require explanation. [CROSS v0.3.6, Part IV; WALKRI Section 3.8]

Note for DPG Standard context: Development stage Stage 1-2 declarations must be consistent with the DPG registry's "nominee" vs "confirmed" status requirements. A Stage 3-4 project applying for DPG confirmation should have more comprehensive evidence than a Stage 1 nominee.

Status: Core

---

**Relevance to sustainable development goals** [Core] - DPG Indicator 1

Criterion intent: Confirm that the digital public good directly advances one or more Sustainable Development Goals, with a named SDG and a traceable description of how the tool or content contributes to that goal.

Operational definition: A statement naming: the specific SDG or SDGs, the target or targets within each SDG, and the mechanism by which the digital good contributes to those targets. "Supports sustainable development" without naming a specific SDG and target does not satisfy this field.

Response form: Long text. Justification: the SDG relationship requires narrative specification of mechanism; structured fields cannot capture the reasoning.

Evidence form: Named SDG and target are from the official SDG list. The stated contribution mechanism is internally consistent with the digital good's function.

Conformance threshold: Registry membership is not accepted as evidence of current SDG relevance. Independent indicator assessment is required: the named SDG and target must be present in the submission, and the contribution mechanism must be traceable from the submission without reference to the registry entry.

Status: Core

---

**Open license** [Core] - DPG Indicator 2

Criterion intent: Confirm that the digital public good is released under a named open license permitting use, modification, and distribution, consistent with the DPG Standard's open access requirement.

Operational definition: A named SPDX license identifier (any OSI-approved open source license for software; any Creative Commons license except NC or ND variants for content; ODbL or equivalent for data) applied to the digital good and present in the repository or published artifact. The license must be in the LICENSE file or package manifest, not only in project documentation. A reference to being "open source" without a named SPDX identifier does not satisfy this field.

Response form: Single-select SPDX identifier plus the URL of the LICENSE file. Justification: the license is a named standard; free text permits non-compliant licenses to be represented as compliant.

Evidence form: The SPDX identifier resolves to an OSI-approved license (for software) or a Creative Commons license without NC or ND restrictions (for content). The LICENSE file exists at the named URL.

Conformance threshold: Registry membership is not accepted as a substitute for current license verification. The license file must exist and be accessible at the time of submission. A change of license since registry registration requires new independent verification.

Status: Core

---

**Clear ownership** [Core] - DPG Indicator 3

Criterion intent: Identify the entity that owns or is responsible for the digital public good, and confirm that this ownership is clearly documented in a publicly accessible location.

Operational definition: The name of the entity (organization or individual) that holds legal ownership of or primary responsibility for the digital public good, the location of the ownership documentation (e.g. the repository's ownership statement, the organization's public registration, or the project's governance documentation), and confirmation that there are no unresolved ownership disputes. A project that lists multiple co-owners must specify how ownership and stewardship responsibilities are allocated.

Response form: Short text for the owner name; URL for the ownership documentation location; long text for ownership allocation if multiple parties are involved. Justification: the owner name and documentation location are single values; the allocation statement requires narrative.

Evidence form: The owner name is independently verifiable from the documentation URL. The documentation URL is publicly accessible without authentication.

Conformance threshold: Registry membership is accepted as evidence of ownership documentation only if the registry entry contains the ownership statement and is current. If the registry entry is more than 12 months old or the ownership has changed since registration, independent verification is required.

Status: Core

---

**Platform independence** [Core] - DPG Indicator 4

Criterion intent: Confirm that the digital public good does not require use of any specific proprietary platform, infrastructure provider, or technology stack to be deployed and used.

Operational definition: A statement confirming: the digital good can be installed and operated on infrastructure the user controls, without requiring a proprietary runtime, proprietary data store, or proprietary API that the user cannot replicate. Where the digital good has been tested on specific platforms, those platforms must be named; the statement must confirm that the good is not exclusively dependent on any of them. A digital good that requires a specific proprietary cloud provider's APIs to function does not satisfy this field.

Response form: Long text. Justification: platform independence depends on the specific architecture and dependencies, which require narrative to specify adequately.

Evidence form: The stated dependencies are cross-referenceable against the repository's dependency manifest. The named dependencies are open source or otherwise freely available without proprietary restriction.

Conformance threshold: Registry membership is not accepted as evidence of current platform independence. The dependency manifest must be assessed at the time of submission.

Status: Core

---

**Documentation** [Core] - DPG Indicator 5

Criterion intent: Confirm that the digital public good includes comprehensive documentation that enables a new user or developer to install, configure, and use it without assistance from the original developers.

Operational definition: Documentation must cover: installation (how to install the good on a new system), configuration (how to configure it for a specific deployment context), and usage (how end users interact with it). Documentation must be in the repository or linked from the repository README. Documentation that is incomplete, outdated (more than one major version behind), or requires account creation to access does not satisfy this field.

Response form: URL pointing to the documentation root. Short text confirming the three documentation types (installation, configuration, usage) are present. Justification: the documentation URL is a single value; the confirmation of coverage types requires a brief structured check.

Evidence form: The documentation URL resolves and is publicly accessible. The three documentation types are present and apply to the current version of the good.

Conformance threshold: Registry membership is not accepted as evidence of current documentation completeness. Documentation must be assessed against the current version of the good at the time of submission.

Status: Core

---

**Non-extraction of data** [Core] - DPG Indicator 6

Criterion intent: Confirm that the digital public good does not collect, transmit, or aggregate data about users or their usage in a manner that benefits the developer at the expense of users, and that users retain control of their own data.

Operational definition: A statement covering: what data the digital good collects from users or about their usage; who that data is transmitted to; whether users can inspect, export, and delete their data; and whether the developer or any third party receives data about users without their explicit informed consent. A digital good that collects usage analytics and transmits them to a third-party service without disclosure does not satisfy this field. A statement that "no data is collected" must be consistent with the technical architecture.

Response form: Long text. Justification: data collection and transmission practices are technically complex and vary by deployment context; structured fields cannot capture this without losing necessary specificity.

Evidence form: The stated data practices are consistent with the technical architecture as documented in the repository. Any third-party data recipients are named.

Conformance threshold: Registry membership is not accepted as evidence of current data practice. The technical architecture and any data transmission must be assessed from the current codebase at the time of submission.

Status: Core

---

**Adherence to privacy and applicable laws** [Core] - DPG Indicator 7

Criterion intent: Confirm that the digital public good's design and operation are consistent with applicable privacy laws in the jurisdictions where it is deployed, and that the project has assessed and addressed the relevant legal requirements.

Operational definition: A statement covering: the jurisdictions in which the digital good is designed to be deployed; the privacy laws applicable in those jurisdictions that the project has assessed (e.g. GDPR, COPPA, LGPD, PDPA); the mechanism by which the digital good satisfies those requirements; and whether a privacy impact assessment has been conducted. A claim of legal compliance without naming the applicable laws and the mechanism of compliance does not satisfy this field.

Response form: Long text. Justification: legal compliance requirements vary by jurisdiction and application type; structured fields cannot capture this without losing necessary specificity.

Evidence form: Named laws are verifiable legal standards in the stated jurisdictions. The compliance mechanism is internally consistent with the digital good's architecture. A privacy impact assessment, if cited, is accessible.

Conformance threshold: Registry membership is not accepted as evidence of current legal compliance. Applicable law changes after registration require independent reassessment.

Status: Core

---

**Adherence to standards and best practices** [Core] - DPG Indicator 8

Criterion intent: Confirm that the digital public good adheres to applicable technical standards and sector-specific best practices relevant to its domain.

Operational definition: A statement naming: the technical standards and sector-specific best practices the project claims adherence to; the mechanism of adherence for each (e.g. automated testing, third-party audit, specification review); and any standards the project has considered but has not yet satisfied, with the reason and a timeline for resolution. "We follow industry best practices" without naming specific standards does not satisfy this field.

Response form: Long text. Justification: applicable standards vary by domain and technical architecture; structured fields cannot enumerate all relevant standards.

Evidence form: Named standards are independently verifiable specifications. The stated adherence mechanism is consistent with the project's technical practices.

Conformance threshold: Registry membership is not accepted as evidence of current standards adherence. Standards evolve, and adherence must be assessed against the current version of each named standard at the time of submission.

Status: Core

---

**Responsible data use policies** [Core] - DPG Indicator 9

Criterion intent: Confirm that the digital public good has documented, public policies governing how data it handles is collected, processed, stored, and shared, and that those policies are consistent with the non-extraction and privacy requirements of the DPG Standard.

Operational definition: A statement providing: the URL of the project's published data use policy (e.g. privacy policy, data governance policy, or equivalent); a brief description of the key provisions (data retention, sharing, user rights); and confirmation that the policy is accessible to users of the digital good without requiring account creation. A policy that exists only as an internal document not accessible to users does not satisfy this field.

Response form: URL of the data use policy. Long text summary of key provisions. Justification: the policy URL is a single value; the summary of provisions requires narrative to be assessable without requiring the reviewer to parse the full policy.

Evidence form: The policy URL resolves and is publicly accessible. The key provisions stated in the summary are present in the policy. The policy applies to the current version of the digital good.

Conformance threshold: Registry membership is not accepted as evidence of a current and accessible data use policy. The policy must be assessed at the time of submission.

Status: Core

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 0.1.2 | 2026-05-18 | Revenue architecture declaration and development stage declaration added as Core fields to all remaining runbooks: Community Allocation, Retroactive Impact, Graduated Evidence, Institutional Conformance, USAID PIRS, OECD DAC, and DPG Standard. Context notes added for each institutional framework runbook. |
| 0.1.1 | 2026-05-18 | Discovery Sprint and Staged Development runbooks updated. Revenue architecture declaration and development stage declaration added as Core fields to both runbooks, derived from WALKRI Section 3.8 instruments. Both fields are now universal requirements in CROSS-conformant programs. Stage notes for each runbook specify the expected stage declarations and flag stage-round misalignment cases. |
| 0.1.0 | 2026-05-18 | Initial release. Six CROSS-paired runbooks (Discovery Sprint, Staged Development, Community Allocation, Retroactive Impact, Graduated Evidence, Institutional Conformance). Three institutional framework runbooks (USAID PIRS, OECD DAC, DPG Standard). Core/Suggested/Optional field status taxonomy. |
