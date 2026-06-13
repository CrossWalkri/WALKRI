---
title: WALKRI Guidance
version: 0.1.4
date: 2026-06-13
license: CC0
status: Working draft. Companion to WALKRI-standard-0_1_0.md.
---

# WALKRI Guidance

Version 0.1.4 | 2026-06-13 | CC0

---

## Part 1: How to Use This Document

Four roles will find this guidance directly useful.

Funders designing intake forms will use Parts 2, 3, and 4 most heavily. Stage 1 (ideation) and Stage 2 (specification) are where the design work happens, and Stage 3 (applicant guidance) is where the quality of that work becomes visible to applicants.

Auditors assessing conformance will use Parts 3, 6, and 7. The field specification requirements in Part 3 operationalize the five criterion specification elements from the standard. Part 6 catalogs the failure patterns that appear most often in practice. Part 7 explains how to interpret and communicate the conformance record that an audit produces.

Researchers building surveys will use Parts 2, 3, and 5. The three-stage process and five criterion specification requirements apply to survey instruments regardless of the form platform used or whether any obligation standard specifies the collection.

Developers integrating WALKRI into tools or pipelines will use Part 3 for the specification requirements and the Appendix for a compact reference format.

The WALKRI standard states requirements: what a field must contain, what process must be followed, what quality standards the data must meet. This document explains how to meet those requirements in practice. The standard is authoritative; this document is operational. Where there is any conflict, the standard prevails.

If you are starting a new form or survey from scratch, begin with Part 2 and work through the document in order. If you are assessing an existing form, begin with Part 6 to identify common failures, then use Part 3 to evaluate specific fields. If you are reading an audit report for the first time, go directly to Part 7.

---

## Part 2: Running Stage 1 (Ideation) in Practice

Stage 1 produces an ideation record: a structured document that names each information need the form is intended to satisfy, the decision that need informs, and the failure mode if the information is missing or imprecise. The ideation record is not published to applicants. It is a design document that specifies what fields get built in Stage 2 and why.

**How to conduct an ideation session.** An ideation session is a working conversation between the people who will use the collected data to make decisions. It is not a brainstorming session about what questions might be interesting to ask. Stay anchored to decisions and failure modes, not to the surface appearance of the form.

Begin by naming the decisions the form is meant to inform. Not "we want to know about team composition" but "we need to decide whether this applicant has the organizational capacity to execute a grant of this size within the grant period." Each decision becomes the organizing principle for one or more information needs.

For each information need, ask one diagnostic question: what decision will this data inform, and what is the failure mode if the data is missing or imprecise? That question does two things at once. It tests whether the information need is genuine (if you cannot name the decision, the need may be speculative rather than operational) and it surfaces the precision requirement (the failure mode tells you how fine-grained the measurement needs to be to support the decision).

A well-run ideation session for a ten-field form typically takes between 60 and 90 minutes. The output is not a draft of the form; it is a list of information needs, each with a named decision and a named failure mode.

**Common ideation failures.** Three patterns recur often enough to name explicitly.

Starting with fields instead of needs. The most common failure is arriving at the ideation session with a draft form already constructed. When practitioners start from fields, they tend to work backward from what the fields ask to what decisions they might inform, rather than working forward from decisions to what information is actually needed. The result is a form that reflects what the designers assumed they needed rather than what they actually need. If a draft form already exists when the ideation session begins, set it aside for the duration of the session.

Treating ideation as a box to check. Stage 1 is the most important stage in the process and the one most often compressed or skipped. An ideation record that lists information needs without decision names or failure modes is not a conformant ideation record; it is a list of topics. The session is complete only when each information need has both a named decision and a named failure mode.

Confusing what would be interesting to know with what is needed to decide. Intake forms routinely include fields that capture information the designers found interesting but that do not map to any specific decision. These fields impose a burden on applicants, generate data that is never used, and crowd out the fields that actually matter. If you cannot name the decision the data will inform, the field does not belong in the form.

**How to know when Stage 1 is complete.** The ideation record is complete when every information need listed in it has a named decision it informs and a named failure mode. If any entry has a blank in either column, the session is not done. "We need it to make good decisions" is not a named decision. "We might not know enough about the applicant" is not a named failure mode.

---

## Part 3: Specifying Fields in Stage 2

Stage 2 takes each information need from the ideation record and produces a WALKRI field specification: a structured document containing all five criterion specification requirements. This section explains what each requirement asks for, what a complete answer looks like, and what the most common failure mode is.

### 3.1 Criterion Intent

**What it asks for.** A written statement of what the field actually measures, distinct from its label. The criterion intent answers: what does a true response to this field tell us about the applicant or subject?

Labels are names. Intents are measurement claims. The gap between the two is where most field design fails.

**What a complete answer looks like.** Consider a field labeled "Team size." An incomplete criterion intent is "the number of people on the team," which merely restates the label with slightly more words. A complete criterion intent is "the number of people with at least 20% of their working time committed to this project for the duration of the grant period, as of the application date." That statement is specific about who counts (those with 20% or more time committed), about the time scope (the grant period), and about the reference point (the application date). A reviewer applying that intent consistently will produce consistent assessments; a reviewer applying the label alone will not.

**Most common failure mode.** The criterion intent restates or paraphrases the label without adding measurement specificity. The test for a complete criterion intent is whether it constrains interpretation in a way the label does not. If a reviewer reading only the criterion intent and a reviewer reading only the label would make identical assessment decisions, the criterion intent is not doing any work.

### 3.2 Operational Definition

**What it asks for.** A complete definition of each option or response category, with examples of what qualifies and what does not. For binary fields: what conditions produce a "yes" and what conditions produce a "no," with at least one edge case determination. For numeric fields: the unit of measurement, the counting rule, and the boundary conditions. For text fields: the scope of acceptable content and the minimum content that constitutes a complete response.

**What a complete answer looks like.** Consider a field asking about open source contributions. An incomplete operational definition is "work the applicant has contributed to open source projects." A complete operational definition specifies the unit of analysis (a discrete, merged, and publicly visible commit, pull request, or issue response to a repository with an OSI-approved license), the inclusion criteria (the contribution must be to a repository the applicant does not own or control, and must have been merged or accepted by the repository maintainer), the exclusion criteria (contributions to forks the applicant controls, closed pull requests that were not merged, and contributions to private repositories do not qualify, even if the applicant later made the repository public), and an edge case determination (contributions to repositories where the applicant is a listed maintainer but not the sole owner count if the contribution was reviewed and accepted by at least one other maintainer).

**Most common failure mode.** The operational definition specifies what qualifies but does not specify what does not qualify. An operational definition without explicit exclusion criteria leaves applicants and reviewers to apply their own judgment about edge cases. Every operational definition must have both inclusion and exclusion criteria.

### 3.3 Response Form

**What it asks for.** The response type for the field (single-select, multi-select, binary, numeric, text, URL, or composite) with a written justification for why that response type fits the criterion intent. The justification must address whether the response type can capture the variance in the underlying construct that the criterion intent requires.

**What a complete answer looks like.** Consider a field asking what type of organization the applicant is. A single-select response form with options such as "non-profit," "for-profit," "government," and "research institution" is appropriate only if the criterion intent requires a single primary classification. If the criterion intent is to understand the legal and operational structure of the organization, single-select may be correct because an organization typically has one primary legal classification. The justification would read: "Single-select is appropriate because legal incorporation status is a categorical construct with mutually exclusive categories; an applicant cannot simultaneously be a non-profit and a for-profit under the same legal entity."

**Most common failure mode.** Single-select is used for questions that naturally produce multiple valid answers. "Project type" with a single-select response form forces applicants to choose one category from a list when many projects span categories legitimately. The applicants do not share a single most-relevant category; they select different ones based on their individual interpretation of relevance, and the resulting data reflects those interpretation choices rather than the actual distribution of project types. The diagnostic question for any single-select field is: "Is it possible for an applicant with a genuine, legitimate answer to this question to have more than one accurate response from the option list?" If yes, single-select produces distorted data and multi-select or a composite response form is required.

### 3.4 Evidence Form

**What it asks for.** A specification of the specific artifact that satisfies the criterion. For document-based evidence: the document type, the required content, and whether a link or upload is required. For quantitative evidence: the data source, the collection methodology, and the time period the evidence must cover. For external verification evidence: the verifying party, the scope of their verification, and the form their verification must take.

**What a complete answer looks like.** Consider a field asking about open source licensing. An incomplete evidence form is "proof of open source license." A complete evidence form is "a LICENSE file present in the root directory of the public repository at the submitted URL, containing an OSI-approved license text or an SPDX license identifier that maps to an OSI-approved license." The complete version specifies the artifact type (a LICENSE file), its location (root directory of the repository), the access path (the public repository at the submitted URL), and the qualifying content (OSI-approved license text or a valid SPDX identifier). A reviewer applying the complete evidence form makes a binary determination with no judgment required; a reviewer given "proof of open source license" makes a series of implicit judgment calls about what kinds of proof satisfy the criterion.

**Most common failure mode.** The evidence form is delegated to reviewer judgment by leaving the artifact type and location unspecified. Phrases such as "documentation of," "evidence of," or "proof of" without a named artifact type always indicate an incomplete evidence form. The evidence form must name a specific artifact. If the criterion intent genuinely admits multiple artifact types that are equally probative, the evidence form must list each acceptable artifact type with the conditions under which it satisfies the criterion.

### 3.5 Conformance Threshold

**What it asks for.** When a field or criterion references an external standard, the conformance threshold specifies which components of that external standard apply, what evidence satisfies each component, and what the minimum threshold for passage is.

**What a complete answer looks like.** A program requiring DPG (Digital Public Good) qualification as a gate criterion must produce a conformance threshold that enumerates all nine indicators of the DPG Standard, states what evidence satisfies each indicator, and names the minimum threshold for passage.

For example, a conformance threshold for DPG Indicator 2 (use of an approved open license) might read: "The applicant must provide a clearly stated SPDX license identifier in the project repository's root-level LICENSE file or README. A reference to a license in prose text without an SPDX identifier does not satisfy this indicator. A link to a third-party license text without reproduction or reference in the repository does not satisfy this indicator." The threshold statement for the full set of indicators might read: "All nine indicators must be satisfied for gate passage. Indicators 1, 2, and 3 are non-waivable. For indicators 4 through 9, an applicant who cannot satisfy an indicator may submit a documented mitigation plan; a maximum of two indicators may be satisfied via mitigation plan."

**When the requirement applies.** The conformance threshold requirement applies whenever a field references an external standard. A field that uses its own operational definition without reference to an outside framework does not need a conformance threshold; the operational definition itself specifies interpretation. The conformance threshold is required only when the field says, in effect, "the applicant must satisfy some external authority's standard," because that construction delegates interpretation to the external standard without specifying how that standard applies in this context.

---

## Part 4: Writing Applicant Guidance (Stage 3)

Stage 3 produces the applicant-facing documentation that accompanies each field. Its source material is the Stage 2 field specification. Stage 3 does not add new definitional content; it translates specification language, which is designed for precision, into applicant language, which is designed for comprehension.

**What the applicant-facing document contains.** Four elements are required for each field.

The first element is what the field is asking, stated in plain language. This is a plain-language version of the criterion intent. It should tell the applicant what the field is measuring without exposing the full technical precision of the criterion intent statement. The applicant does not need to know that the criterion intent specifies "at least 20% of working time"; they need to understand that the field is asking about people who are genuinely working on the project, not advisors or board members who have occasional involvement.

The second element is what a complete answer looks like. This draws on the examples from the operational definition. One or two concrete examples are more useful than a general description. "A complete answer names two full-time engineers and one part-time designer and states their time commitments explicitly" is more useful than "describe your team."

The third element is what a common incomplete answer looks like, derived from the failure modes identified during the operational definition process. "A common incomplete answer lists all people who have ever contributed to the project, including advisors, occasional volunteers, and people who left before the grant period began. The field is asking only about people actively working on the project during the grant period."

The fourth element is why the field exists, stated briefly and without exposing the ideation record. "This field helps us assess whether the team has the capacity to execute the proposed work within the timeline" gives applicants enough context to calibrate their answers without disclosing the full decision framework.

**How to derive Stage 3 from Stage 2.** The translation is mechanical once the Stage 2 specification is complete. The criterion intent becomes the plain-language explanation. The qualifying examples from the operational definition become the positive example. The non-qualifying examples and edge case determinations become the negative example. The decision the field informs, drawn from the ideation record through the criterion intent, becomes the "why this field exists" statement.

When the Stage 2 specification is complete, Stage 3 should take significantly less time than Stage 2. If writing Stage 3 guidance requires making new decisions about what counts or what does not count, that is a signal that Stage 2 is not complete. Stage 3 guidance should never be the place where definitional decisions are made.

---

## Part 5: Using WALKRI Without an Obligation Standard

Organizations that want to improve data collection quality without adopting any external obligation framework use WALKRI's three-stage process and five criterion specification requirements as their complete specification authority. Part III of the standard is the direct specification authority in this case. Nothing in the three-stage process or the five criterion specification requirements assumes that any external obligation standard specifies what is being collected.

**The conformance threshold requirement without an external obligation standard.** When no external obligation standard is referenced, the conformance threshold requirement applies only to external standards the form itself references. A form that refers to DPG qualification, OSI-approved licenses, or any other external framework must specify a conformance threshold for that reference. A form that uses only its own operational definitions and does not reference any external standard does not need a conformance threshold for any field.

When an obligation standard such as CROSS specifies the form, that standard's gate criteria may generate conformance threshold requirements for specific fields because the obligation standard specifies what external standards the program must enforce and how. The other four requirements, criterion intent, operational definition, response form, and evidence form, apply identically whether or not an obligation standard is present.

**Starting point for independent adoption.** Begin with the ideation session described in Part 2. The diagnostic question, "what decision will this data inform, and what is the failure mode if the data is missing or imprecise?", applies regardless of what the form is for.

---

## Part 6: Common Field Specification Failures and How to Fix Them

Six failure patterns appear with sufficient regularity to document by name. Each pattern has a name, a description of what it looks like in practice, an explanation of why it produces bad data, and a repair.

**Failure 1: Label without intent.** A field labeled "Contributions" with no criterion intent statement. In practice, this looks like a dropdown or text field whose label is the only documentation of what it asks.

This pattern produces bad data because applicants and reviewers must each construct their own interpretation of what "contributions" means. One applicant counts financial contributions; another counts volunteer hours; a third counts code commits. The resulting data is nominally consistent (everyone filled in the "Contributions" field) but definitionally incoherent (everyone filled in something different).

The fix is to write a criterion intent statement before the field is published. The intent statement must specify the type of contribution (to what, by whom), the unit of measurement, and the time scope. If different types of contributions need to be captured separately, the field should be split into multiple fields, each with its own criterion intent.

**Failure 2: Single-select for multi-answer questions.** A field labeled "Project type" with one selection allowed from a list of types such as "infrastructure," "research," "tooling," and "community building."

This pattern produces bad data because many projects span multiple categories. When forced to choose one, applicants select different categories for the same project, producing data that reflects individual applicants' classification preferences rather than the actual distribution of project types.

The fix is to change the response form to multi-select when the underlying construct can legitimately take multiple values simultaneously. If the criterion intent genuinely requires a single primary classification, the criterion intent statement must make that explicit ("the primary operational focus of the project, excluding secondary activities") and the operational definition must explain how to determine which category is primary when a project spans multiple categories.

**Failure 3: External standard reference without conformance threshold.** A criterion that reads "the project must be DPG-eligible" or "the project must use an OSI-approved license" without specifying which indicators or requirements apply, what evidence satisfies each, and what the minimum threshold for passage is.

This pattern produces bad data because the external standard's requirements are not binary, and reviewers must construct their own interpretation of what conformance means. Different reviewers apply different thresholds. Outcomes reflect reviewer assignment rather than applicant conformance to the standard.

The fix is to write a conformance threshold that enumerates the applicable indicators or requirements, specifies the evidence that satisfies each, and names the minimum threshold. The DPG Standard case is worked through in detail in Part 3.5 above. For simpler external standards such as an OSI license list, the conformance threshold is also simpler: "The license must appear on the OSI-approved license list at https://opensource.org/licenses, accessed at the version archived on [date]. SPDX identifiers are acceptable in place of full license names provided the identifier maps to an OSI-approved license on that list."

**Failure 4: Evidence form delegated to reviewer judgment.** A field whose evidence form reads "proof of open source" or "documentation of community engagement" or any other phrase that names a category of evidence rather than a specific artifact.

This pattern produces bad data because reviewers make implicit artifact quality judgments that differ across the cohort. One reviewer accepts a GitHub repository link. A second requires a LICENSE file with a specific license type. A third accepts a blog post describing the project's open source philosophy. None of these standards is documented; each reflects the reviewer's prior experience and expectations.

The fix is to name the specific artifact. "A LICENSE file in the root directory of the public repository at the submitted URL, containing an OSI-approved license identifier" is a complete evidence form. "Proof of open source" is not.

**Failure 5: Operational definition without exclusion criteria.** An operational definition that specifies what qualifies but says nothing about what does not qualify.

This pattern produces bad data in a predictable way. Applicants with edge cases that should not qualify include them because nothing in the definition says not to. Reviewers disagree about how to treat those cases because the definition provides no guidance. The variance in the data reflects interpretation style rather than differences in the underlying population.

The fix is to add explicit exclusion criteria to every operational definition. For each qualifying criterion, ask what instances satisfy the surface-level reading of the criterion but should not count for purposes of this measurement. Those instances belong in the exclusion criteria. Edge cases that are genuinely ambiguous should be resolved explicitly in the operational definition rather than left to reviewer judgment.

**Failure 6: Response form mismatch.** A quantitative question answered via a text field ("Describe the number of people reached"), or a categorical question answered via a numeric field ("Rate your project's decentralization level from 1 to 10"), or a binary question that admits genuinely non-binary answers ("Does your project have a governance structure? Yes/No").

This pattern produces bad data structurally. A text field for a quantitative question produces numbers embedded in prose, which cannot be aggregated without a parsing step that introduces additional interpretation variance. A numeric scale for a categorical construct forces a comparison that the underlying construct does not support. A binary field for a construct with genuine intermediate states collapses meaningful variance into a forced dichotomy.

The fix requires matching the response form to the measurement claim in the criterion intent. If the criterion intent is quantitative, the response form is numeric with a defined unit. If the criterion intent is categorical, the response form is single-select or multi-select with defined options. If the criterion intent is genuinely binary, the field is binary; if it is not genuinely binary, the criterion intent needs to be revised before the response form can be specified.

---

## Part 7: Reading a WALKRI Audit Report

A WALKRI audit produces a conformance record: a structured document that records the assessment of each field against each of the five criterion specification requirements.

**What each status means.** Each field-requirement combination receives one of three statuses.

A pass status means the field satisfies that criterion specification requirement. The specification contains the required elements, and those elements are sufficiently specific to constrain reviewer and applicant interpretation. A pass does not mean the field is perfect; it means the requirement is met.

A fail status means the field does not satisfy the criterion specification requirement. The specific failure is documented in the finding: which element is absent or insufficient, and which failure mode (from Part III of the standard) the finding corresponds to. Every fail finding has a documented failure mode and a suggested resolution.

An override-documented status means the field produced a flag that the question-holder has acknowledged and documented a justification for. An override is not a pass; it records a deliberate decision not to resolve a flag, with the reason for that decision. The justification is attached to the conformance record. Downstream data consumers can see what the override was, why it was made, and who authorized it. An override is a conformance choice, not a certification failure, provided the justification is present and substantive.

**What to do with a fail finding.** Not all fail findings block publication; some are advisory.

A blocking failure must be resolved before the form can be published. Blocking failures are those where leaving the flag unresolved would produce data that is definitionally incoherent, unauditable, or misleading. The following are blocking: a field with no criterion intent (Failure 1 from Part 6); a field with an external standard reference but no conformance threshold (Failure 3); and a field whose evidence form is entirely absent. These failures do not admit override because there is no basis for a defensible justification of why the field should be published without the missing element.

An advisory failure should be resolved before the next round but does not block publication. Advisory failures include missing exclusion criteria (Failure 5), response form mismatches that are marginal rather than severe (Failure 6), and evidence form weaknesses where an artifact type is named but insufficiently specified. A form with advisory failures can be published with a documented plan to resolve the failures before the subsequent reporting period. The advisory status must be recorded in the conformance record.

**How to use the gap report to prioritize remediation.** The gap report is a summary of all fail and override-documented findings across the form, organized by severity. Start with the blocking failures; the form cannot move forward until these are resolved. After blocking failures are cleared, address advisory failures in the order that most affects data quality for your primary decisions: begin with fields that feed into gate criteria or high-weight scoring dimensions, and work outward to fields that inform context or supplementary analysis.

When resolving a fail finding, return to the Stage 2 specification for the affected field, not to the form itself. A form field is a rendering of a specification; fixing the form without fixing the specification produces a form that no longer matches its specification document.

---

## Appendix: Quick Reference

### Five Criterion Specification Requirements

**Criterion intent.** What the field actually measures, distinct from its label. Failure mode when absent: reviewers and applicants interpret the same label differently, producing interpretation variance that is treated as real variance in the underlying population.

**Operational definition.** Inclusion criteria, exclusion criteria, unit of analysis, and edge case determinations for each response option or category. Failure mode when absent: nominal consistency conceals definitional variance; the data reflects applicant interpretation style rather than differences in the underlying population.

**Response form.** The response type (single-select, multi-select, binary, numeric, text, URL, or composite) with written justification for why it fits the criterion intent. Failure mode when absent: fields are designed for administrative convenience rather than measurement accuracy, producing data with artificially bounded variance.

**Evidence form.** The specific artifact that satisfies the criterion, with its type, location, access path, and content requirements. Failure mode when absent: reviewers make implicit artifact quality judgments inconsistently across the cohort; the data cannot be audited.

**Conformance threshold.** When an external standard is referenced: which components apply, what evidence satisfies each, and the minimum threshold for passage. Failure mode when absent: reviewer-level interpretation of the external standard becomes the de facto threshold; outcomes reflect reviewer assignment rather than applicant conformance.

### Five Data Quality Standards

**Validity.** Assessment question: is there a documented logical chain from the evidence specified in the evidence form to the result claimed in the criterion intent? Primary connection: criterion intent (3.1).

**Integrity.** Assessment question: is evidence collection separated from the actor who benefits from a favorable outcome? Primary connection: evidence form (3.4).

**Precision.** Assessment question: is the measurement instrument capable of detecting differences at the magnitude relevant to the decisions the data will inform? Primary connection: response form (3.3).

**Reliability.** Assessment question: is the methodology for collecting and interpreting this field consistent across reporting periods and across reviewers within a single reporting period? Primary connection: operational definition (3.2).

**Timeliness.** Assessment question: is the evidence specified in the evidence form current to the decision cycle for which the data is being collected? Primary connection: evidence form (3.4).

### Three Stage Outputs

**Stage 1 output: ideation record.** Contents: each information need the form is intended to satisfy, the decision each need informs, and the failure mode if the information is missing or imprecise. Audience: question-holders and field specification practitioners (not applicants).

**Stage 2 output: field specification.** Contents: all five criterion specification requirements for each field, in JSON Schema or a compatible format. Audience: question-holders, auditors, form rendering tools, and the WALKRI Audit Tool.

**Stage 3 output: applicant guidance document.** Contents: plain-language explanation of what the field asks, a positive example of a complete answer, a negative example of a common incomplete answer, and a brief statement of why the field exists. Audience: applicants completing the form.

---

## Part 8: Working with Identity Fields (Section 3.7)

WALKRI Section 3.7 introduces three applicant identity instrument types. Identity fields are different from other gate fields in one structural respect: they are required for all entry gates regardless of obligation mode, and they carry a cross-field consistency obligation that no other field type carries. This Part explains how to apply them in practice.

### The Three Instrument Types

**Legal entity instrument.** This field asks: who, legally, is answerable for delivering the obligations and receiving disbursement? The criterion intent is identifying the legal person or registered organization. The key design principle is that a legal entity instrument never accepts display names, project names, brand names, or GitHub organization names as satisfying answers unless those names are also the legal name of record. Many programs accept project names in a legal entity field and then find, at completion or continuation, that they have no clear answerability chain. The Stage 2 specification for this field must state the jurisdiction of registration as a required element alongside the legal name.

The failure mode is accepting a display name as a legal entity answer. The Stage 2 specification must include an exclusion criterion stating explicitly: "The following do not satisfy this field: project names, brand names, GitHub organization names, pseudonyms, and display names that are not also the applicant's legal name in the stated jurisdiction."

**Display name instrument.** This field asks: under what public-facing name does the applicant present this work? The criterion intent is continuity and recognition: a display name that a reviewer can query across prior grant histories, public repositories, and program records to establish a track record. The design principle is that a display name must have prior public use: it cannot be a name invented for this application. A display name used only on the current application with no prior public appearances is not a display name in the instrument sense; it is a new identity with no track record.

The failure mode is accepting self-assigned names without requiring evidence of prior use. The evidence form for this field must require at least one public URL where the display name has been used in a prior communication, grant, repository, or publication.

**Prior entity relationship instrument.** This field activates whenever an applicant cites prior work as evidence of capability, track record, or contribution. It asks: under whose governance, employment, or resources was that prior work performed? This instrument is not triggered by the applicant's current entity status; it is triggered by the citation of prior work. An application that does not cite any prior work does not activate this instrument.

The three required elements are: the name of the entity under which the cited work was performed, the applicant's relationship to that entity at the time of the work (employed, contracted, co-founder, contributor), and the current status of that relationship. A departure from the entity is not a disqualifier, but it does generate additional questions: does the applying entity hold the IP, control the codebase, and maintain the user relationship with any users cited as evidence?

The failure mode is allowing applicants to cite prior work without naming the entity under which it was performed. A citation like "I built X" that does not name an organizational context is an unsigned attribution: it makes a contribution claim without establishing where the applicant stood relative to the resources, governance, and decisions that produced X.

### The Self-Reference Consistency Requirement

Section 3.7 adds a cross-field consistency obligation that operates across the entire application, not just within the identity declaration fields. Every self-reference in every field must resolve to the declared legal entity or display name. A project name used in the progress section, a GitHub organization name in the evidence section, or a prior grant recipient name in the funding history section must match one of the two declared identities. Inconsistency between self-references and declared identities is a conformance flag.

In practice, this requirement is a downstream audit step rather than a field-level specification requirement. Auditors applying this check do not assess individual fields for inconsistency; they assess the application as a whole after the field-level audit is complete. The Step 2 specification for the identity declaration fields should include a note that self-reference consistency will be checked as a post-specification audit step.

The most common inconsistency pattern: an applicant lists a legal entity name in the legal entity field but then refers to their work throughout the application under a display name that they did not declare. A reviewer checking only the identity declaration fields would pass the application; a reviewer applying the self-reference consistency check would flag it. Both checks are required.

### Design Notes

Identity fields require more care than most fields because the stakes of getting them wrong compound over time. A form that collects imprecise project names in the first round cannot establish continuity of identity in the second round. The organizational identity declaration is the anchor point for all subsequent gate records, track record assessments, and cross-program queries. The investment in specifying it precisely in Stage 2 compounds across rounds and programs.

When building the ideation record for a program that uses continuation gates, name "establishing cross-round identity continuity" as an explicit information need in Stage 1. This surfaces the continuity requirement at the design stage, where it can be built into the identity field specifications, rather than at the continuation gate, where it has to be reconstructed from inconsistent prior data.

---

## Part 9: Working with Gate Declaration Fields (Section 3.8)

Section 3.8 adds five WALKRI instruments for the CROSS entry gate declarations. These differ from the identity instruments in Section 3.7 in one key respect: each instrument maps to a CROSS primitive that constrains what the applicant can validly claim elsewhere in the application. A revenue architecture declaration of "grant-only" makes a concurrent commercial revenue disclosure inconsistent. A Continuity Capacity state of "single" makes a sustainability stance of "sustained" implausible at completion. The gate declaration instruments are not independent fields; they form a constraint network across the application.

**Revenue architecture instrument:** Guide applicants to classify their revenue architecture honestly by asking them to name their revenue sources, not just their grant needs. The question "What would your project's budget look like if this grant were not awarded?" surfaces the architecture more reliably than "What is your revenue model?" Commercial revenue signals include: active token contracts, service agreements named in the application, product pricing pages, and prior investor disclosures. Grant-only declarations from entities with governance tokens require investigation.

**Disbursement authority instrument:** The three-state structure (Individual, Collective, Delegated) exists because a text field asking "who receives funds" produces unverifiable narrative. The instrument requires naming specific mechanisms and individuals. For Collective state, require the multisig address or governance contract to be named explicitly so it can be resolved on-chain. For Delegated state, require both the receiving entity and the deploying entity to be named. The most common error is applicants selecting Individual when a multisig exists that is not named.

**Continuity Capacity instrument:** The key diagnostic question is: if the named primary contributor stopped working tomorrow, would the project continue? Single state is not a disqualifier but it is a risk factor that affects the sustainability stance assessment. Programs should ask applicants to name their primary contributor explicitly, not just describe their decision-standing structure generically.

**Obligation fulfillment record instrument:** This instrument activates only for returning applicants and applicants citing prior work. The assessment procedure is sequential: check the KarmaGAP API for grants associated with the applicant's wallet address before reading the applicant's self-report. Discovering grants the applicant did not disclose is a material non-disclosure, treated more severely than a disclosed partial fulfillment.

**Development stage instrument:** The five-stage scale anchors what evidence is plausible at each stage. Stage 1 applications with large usage claims are inconsistent. Stage 4 applications in Stage 1-3 rounds are a round configuration mismatch, not an application failure. The most useful diagnostic question is: does the evidence offered match the stage declared?

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 0.1.4 | 2026-06-13 | Frame Language own-voice vocabulary pass. Recasts: "governs/governed" recast to "specifies" or "prevails" in own-voice prose (the ideation record specifies what fields get built; an obligation standard specifies the collection; the operational definition specifies interpretation; CROSS specifies the form; on conflict the standard prevails); own-voice "compliance" recast to "conformance" (Failure 3 prose and the Conformance threshold quick-reference failure-mode line); "accountable (of the legal party)" recast to "answerable" and "accountability chain" to "answerability chain" in the legal entity instrument; "governance structure" recast to "decision-standing structure" in the Continuity Capacity guidance. Kept as admissible: the quoted bad-field example "Does your project have a governance structure? Yes/No" (Failure 6); "under whose governance, employment, or resources" and "resources, governance, and decisions" as the named organizational-context sense of the prior entity relationship instrument; the named technical concepts "governance tokens" and "governance contract"; the historical changelog records naming the prior Governance Resilience primitive. No field, conformance threshold, or mapping changed; vocabulary only. |
| 0.1.3 | 2026-06-08 | Primitive rename cascade propagated: the Governance Resilience instrument is now the Continuity Capacity instrument, and the disbursement-authority Governed state is now Collective (the "For Collective state" guidance). Propagates the Foundation v0.1.7 and v0.2.2 renames. No guidance content or requirement changed; naming only. |
| 0.1.2 | 2026-05-18 | Part 9 added: Working with Gate Declaration Fields (Section 3.8). Covers the five gate declaration instruments: revenue architecture, disbursement authority, governance resilience, obligation fulfillment record, development stage. Constraint network framing between instruments. Activation rule for obligation fulfillment record. Evidence plausibility by stage for development stage instrument. |
| 0.1.1 | 2026-05-17 | Part 8 added: Working with Identity Fields (Section 3.7). Covers the three instrument types (legal entity, display name, prior entity relationship), design principles and failure modes for each, the self-reference consistency requirement, and design notes for programs using continuation gates. |
| 0.1.0 | 2026-05-15 | Initial draft. Seven parts covering the three-stage process, field specification requirements, applicant guidance, common failure modes, and audit report reading. |
