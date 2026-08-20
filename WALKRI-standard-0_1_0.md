---
title: WALKRI - Working Architecture for Legible, Knowable, Reliable Instrumentation
version: 0.2.1
date: 2026-08-20
license: CC0
status: Working draft. Reconception landed in v0.2.0: the instrument is the unit of specification (form field as one instantiation), instrument dependency declaration is required (derive-and-attest), and the standard declares its own inheritance and position (Part XI). The filename stem 0_1_0 is the stable series identifier for the WALKRI suite; the version above is authoritative.
companion_standard: CROSS (github.com/CrossWalkri/CROSS)
brand: CROSS+WALKRI
related_documents:
  - WALKRI-interface-specification-0_1_0.md
  - WALKRI-CROSS-boundary-0_1_0.md
companion_documents:
  - WALKRI-guidance-0_1_0.md
  - WALKRI-templates-0_1_0.md
  - WALKRI-rubric-0_1_0.md
  - WALKRI-worked-examples-0_1_0.md
  - WALKRI-runbooks-0_1_0.md
---

# WALKRI - Working Architecture for Legible, Knowable, Reliable Instrumentation

Version 0.2.1 | 2026-08-20 | CC0

---

## Part I: Purpose and Scope

WALKRI (Working Architecture for Legible, Knowable, Reliable Instrumentation) is a standard for epistemic quality at the point of data capture. It specifies how fields and criteria used to collect structured information must be defined, so that the resulting data is valid, consistent, provenance-aware, and reusable by both humans and automated systems.

**Format agnosticism.** WALKRI specifies what field definitions must contain, not what format they must use. Any tool, platform, or infrastructure that satisfies the content requirements of this standard is conformant. WALKRI is designed to be compatible with many data formats and ecosystems. Where this standard references a specific format, protocol, or system as an example of how its requirements can be satisfied, that reference is illustrative, not prescriptive. The compatibility statements published alongside this standard show how WALKRI content maps to specific formats and systems; those mappings do not obligate any program to adopt those formats or systems. A program implementing WALKRI through its own internal systems, a commercial form platform, a research data infrastructure, or any other tool is equally conformant provided the content requirements are met.

### The Unit of Specification: The Instrument

WALKRI's unit of specification is the instrument: the structured device through which one piece of information is captured. A form field is one instantiation of an instrument. So are a prompt constraint given to a language model, an element of a structured-output schema, a rubric item a reviewer applies, and an extraction specification run over a document. These are named renderings of the same underlying thing in different modalities, and the precision an instrument requires does not change when the modality does.

This is a deliberate scoping choice. The form field is not the definition of WALKRI's subject; it is one named instantiation of it. The five specification requirements in Part III attach to the instrument, and a form field satisfies them as the form-modality rendering of an instrument. Where this standard says "field," it names the form-modality instantiation for readability, and the requirement it states applies to an instrument in any modality. This is what makes "Instrumentation" in the standard's name literal: WALKRI specifies instruments, of which form fields are the most familiar but not the only kind.

### The Problem

Funders, organizations, and programs regularly publish intake fields without operationally defining them. A dropdown labeled "Contributions" offers single-select options with no definitions. A gate criterion labeled, for example, "Qualifies as Digital Public Good (DPG)" appears without specifying which of the nine Digital Public Goods Standard indicators apply, which evidence satisfies each, what threshold constitutes passage, or whether registry membership is accepted as a proxy for current indicator qualification. Each gap produces a different failure: one reviewer checks the registry; another assesses indicators directly; a third accepts a self-assessment; none of them is wrong, given what the criterion actually says. These are not edge cases; they are the default condition of most structured data collection in the grant, program, and research evaluation space.

The consequences are predictable. Applicants interpret underspecified fields differently from one another and from reviewer expectations. Reviewers apply inconsistent interpretations across a cohort, producing non-reproducible outcomes. Downstream analysts inherit a dataset whose nominal consistency conceals definitional variance; analysis built on that data is suspect at the foundation, not because the analysis is wrong, but because the instrument was never precise enough to support it.

The precision requirements that apply to what applicants must demonstrate have not been applied to the fields and criteria funders use to collect that demonstration. WALKRI closes that gap. It operates at the instrumentation and collection layer: the point where a question is encoded as a field before any applicant ever sees it.

### What WALKRI Does

WALKRI specifies: what information a field definition must contain before it is considered complete; what process must be followed to produce a conformant field; what quality standards the field must meet; and what provenance information must travel with the data once collected.

WALKRI is not a form builder. It does not render forms, generate user interfaces, or integrate with any specific form platform's API. Form tools (Fillout, Jotform, Typeform, KoBoToolbox, REDCap, and others) are interchangeable rendering layers. WALKRI sits above them as a quality gate, operating on JSON Schema as its native format, which underlies all major form tools. A field that meets WALKRI's specification requirements can be rendered by any conformant tool; the quality of the resulting data is independent of which tool is used.

WALKRI conformance is reachable through three pathways. A technically capable organization can implement WALKRI directly from this standard using any internal system or existing form infrastructure. An organization using a commercial form builder, grants management platform, or research data collection tool can express WALKRI-conformant field specifications in JSON Schema and pass them to that tool for rendering without any change to the tool itself. An organization that wants the specification and audit process guided rather than self-directed can use a guided implementation tool. All three pathways produce equally conformant output. WALKRI conformance is a property of the field specification, not of the tool used to render it.

WALKRI is portable. It functions as a companion to any obligation standard that specifies what data must be collected, or it can be used independently by any organization that wants to improve its own data collection practices without reference to an external obligation framework.

### CROSS and WALKRI

CROSS (Common Reporting Outcome Standards Schema) is one of the obligation standards that formally references WALKRI. CROSS specifies what must be collected; WALKRI specifies how those fields must be defined so that what gets collected matches what was required. Other obligation standards may reference WALKRI in the same way. The two standards are each independently operable.

---

## Part II: The Three Interfaces

WALKRI has three relationships, each requiring a defined connection.

### 2.1 Obligation Standards

An obligation standard specifies what must be collected: the indicators, criteria, and evidence requirements that constitute a complete response. WALKRI specifies how those fields must be defined so that the collection produces the data required by the obligation standard.

A conformant obligation standard provides: a named set of collection requirements; a version identifier that can serve as a reference anchor; and, optionally, a designated mapping to WALKRI's five criterion specification elements.

An obligation standard that formally references WALKRI must specify, for each of its collection requirements, which WALKRI criterion specification elements it requires and at what threshold. Obligation standards may structure this mapping differently; WALKRI accepts any mapping that is explicit, versioned, and auditable.

Organizations using WALKRI without any obligation standard use Part III of this document directly as their specification authority.

### 2.2 Form Rendering Tools

WALKRI works with form tools through any format that can carry the five criterion specification elements as structured metadata. WALKRI does not integrate with any specific tool's API. A field specification produced in any format that preserves criterion intent, operational definition, response form justification, evidence form, and conformance threshold is WALKRI-conformant. The format choice is determined by the program's existing infrastructure and the tool ecosystem it operates in.

Three formats with documented mappings are: JSON Schema (which underlies Fillout, Jotform, Typeform, and many comparable tools), REDCap data dictionaries (widely used in research and humanitarian data collection), and XLSForm (used by KoBoToolbox, ODK, and comparable field data collection tools). These three have detailed mapping specifications in WALKRI-interface-specification-0_1_0.md. Programs using other formats that can carry the five criterion specification elements are equally conformant; the interface specification document covers additional format mappings as they are developed.

WALKRI's quality guarantees are applied at the specification stage, before any form is published.

### 2.3 Data Consumers

Data collected through WALKRI-conformant fields carries the provenance, operational definitions, and schema metadata required by downstream data consumers, analysts, and AI pipelines. WALKRI specifies what metadata must be present; the format in which that metadata is expressed is determined by the program's context and downstream consumers. WALKRI-conformant data is compatible with Croissant (ML-ready dataset metadata), FAIR principles, W3C PROV (provenance tracking), DAOIP-5 (Web3 grants metadata), DDI (social science data documentation), and comparable standards, because all of these formats require the same underlying field-level provenance and specification that WALKRI produces. Programs choose which of these formats their data is expressed in based on their ecosystem and their consumers' infrastructure.

WALKRI's enrichment layer produces output aligned with five external standards and one foundational infrastructure layer:

**Croissant** (ML-ready dataset metadata): A WALKRI-enriched dataset includes field-level metadata sufficient for automated ingestion by machine learning pipelines, including option definitions, evidence form specifications, and version anchors for any referenced external standards.

**FAIR principles** (Findable, Accessible, Interoperable, Reusable): WALKRI-enriched output carries the provenance fields and schema version information required for FAIR conformance. The interoperability requirement is met by using JSON Schema as the native format; the reusability requirement is met by the operational definitions that accompany each field.

**W3C PROV** (provenance data model): WALKRI's provenance fields map to the W3C PROV data model's core entities (Entity, Activity, Agent), enabling the collection history of any data element to be expressed in a standard provenance graph.

**Grants metadata formats**: WALKRI-enriched field specifications are expressible in any grants metadata format that supports field-level documentation. For programs operating within the DAOstar/Metagov ecosystem, field definitions can be expressed within DAOIP-5 Project objects using an extension namespace. For programs using IATI, field metadata maps to variable documentation elements. For programs using DDI, field specifications map to variable-level metadata. The compatibility statements published alongside this standard provide format-specific mappings. No specific grants metadata format is required for WALKRI conformance.

**Conformance record attestation.** WALKRI's conformance record, which documents the audit outcome for each field in a certified program, is a publicly verifiable record. WALKRI specifies what the conformance record must contain, not what format it must use. Required content: the field identifier, the audit outcome for each criterion specification element, any override justifications, the specification timestamp, and the auditor identity. Any format that carries these elements satisfies the requirement. Compatible formats include W3C Verifiable Credentials, EAS attestations, DAOIP-3 VCs (for programs operating within the DAOIP ecosystem), signed audit documents, and formal institutional certification records. Programs should select the format appropriate to their institutional context.

**DAOIP-2 / ERC-4824** (DAOstar Common Interfaces for DAOs): For programs where applicants are DAOs publishing a daoURI per DAOIP-2, the DAOIP-2 identity layer provides the foundational project identity to which WALKRI-enriched field definitions and provenance records are attributed. DAOIP-2 is infrastructure beneath the WALKRI quality layer, not a target for WALKRI output; it is named here so implementers understand the dependency relationship.

The detailed alignment specifications for all targets are in WALKRI-interface-specification-0_1_0.md.

---

## Part III: Field Specification Requirements

A WALKRI-conformant instrument must satisfy five criterion specification requirements. These requirements apply to funders specifying gate criteria, researchers designing survey fields, organizations building intake forms, and any other entity using WALKRI to structure data collection. The requirements are stated below in their form-field instantiation because that is the most familiar one; per Part I, they attach to the instrument, and a prompt constraint, a structured-output schema element, a rubric item, or an extraction specification satisfies them as the rendering of an instrument in its own modality. A field that does not satisfy all five requirements is not WALKRI-conformant, regardless of its label or where it appears in a form.

The five requirements are: criterion intent, operational definition, response form, evidence form, and conformance threshold.

### 3.1 Criterion Intent

**What It Requires:** A written statement of what the field measures, distinct from its label. The criterion intent answers: what does a true response to this field tell us about the applicant or subject?

**Why It Is Required:** A label is a name. An intent is a measurement claim. The label "Community Engagement" can mean the number of community members reached, the depth of co-design processes, the geographic distribution of engagement, or the frequency of contact. Each is a different measurement instrument. Without a written criterion intent, the field designer cannot assess whether the response form can capture what they intended, and reviewers cannot assess responses against a consistent standard.

**Failure Mode When Absent:** Different reviewers interpret the same label differently. Applicants optimize for the interpretation they believe their reviewer holds, producing responses that are locally rational and globally inconsistent. Downstream analysis treats the field as if it measured a single thing, even though it measured several different things across the cohort.

### 3.2 Operational Definition

**What It Requires:** A complete definition of each option or response category in the field, with qualifying examples and non-qualifying examples for each. For binary fields: what conditions produce a "yes" and what conditions produce a "no," with at least one edge case determination. For numeric fields: the unit of measurement, the counting rule, and the boundary conditions. For text fields: the scope of acceptable response content and the minimum content that constitutes a complete response.

**Why It Is Required:** An option without a definition delegates interpretation to applicants. Two applicants with identical circumstances will select different options if their interpretation of the option labels diverges. The resulting data is not comparable; it reflects variation in applicants' interpretations rather than actual differences in the applicant population.

**Failure Mode When Absent:** Nominal consistency (all applicants chose from the same options) conceals actual definitional variance. Analysis of the resulting data yields conclusions that are artifacts of the distribution of interpretations, not of the underlying population.

For text fields and qualitative narrative responses, the operational definition specifies the scope and minimum content requirements rather than exhaustive definitions of options. The additional design challenges posed by inherently qualitative fields are addressed in Appendix A.

### 3.3 Response Form

**What It Requires:** The response type for the field (single-select, multi-select, binary, numeric, text, URL, or composite), with a written justification for why that response type is appropriate for the criterion intent. The justification must address whether the response type can capture the variance in the underlying construct required by the criterion intent.

**Why It Is Required:** Response type is not a formatting decision; it is a measurement decision. A single-select response form assumes that the construct is categorical and has mutually exclusive categories. A numeric response form assumes the construct is quantifiable on a common scale. Using the wrong response form for a construct produces systematic measurement error that cannot be corrected in the analysis.

**Failure Mode When Absent:** Fields are designed for administrative convenience rather than measurement accuracy. The resulting data has bounded variance by construction, masking real differences in the population.

### 3.4 Evidence Form

**What It Requires:** A specification of the artifact that satisfies the criterion, including: the evidence type (drawn from the taxonomy below), the required content within that type, the access path by which a reviewer can independently locate and verify it, and, where the criterion involves a completion claim, whether the evidence type is sufficient to verify completion or serves only as supporting context.

**Why It Is Required:** A criterion without a specified evidence form is an assertion without a verification path. More precisely: without naming the evidence type, a field that accepts "verifiable evidence links or attestations" receives institutional endorsement letters, field photographs, water quality test results, procurement quotations, and social media links as interchangeable responses to the same criterion. They are not interchangeable. Each type proves a different thing. A reviewer cannot assess evidence they cannot locate, and applicants cannot produce evidence they have not been told to collect. The evidence form closes the loop between the measurement claim in the criterion intent and the data that actually supports it.

**Failure Mode When Absent:** Applicants submit different evidence types in response to the same criterion, some of which satisfy the measurement intent and some of which do not. Reviewers apply implicit and inconsistent judgments about evidence quality. For criteria involving technical performance claims (for example, 94-98% nitrate removal efficiency), applicants may substitute institutional attestations that reference the work without verifying the claim. For criteria involving ecological monitoring data, applicants may submit counts without stating the counting protocol, making the numbers non-comparable across the cohort. The resulting data cannot be audited because there is no evidence type specification against which to audit it.

**The Five Evidence Types:**

A WALKRI-conformant evidence form specification must name the evidence type required and the specific elements that type must contain.

**Standing evidence** attests to organizational standing, recognition, institutional membership, or formal programme participation. Standing evidence proves that the organization has been assessed and recognized by a named body. It does not prove that specific outcomes occurred.

Required elements: the attesting body with its domain standing stated (for example, "FAO Near East and North Africa regional office, the UN food and agriculture authority for the region"); the scope of what is specifically attested (programme participation, technology validation, innovation award, humanitarian organization listing, or other named scope); the currency window within which the attestation must have been issued; and the verification path by which a reviewer can independently confirm the attestation without contacting the applicant (named public URL, official registry, published list, or named directory).

Standing evidence is appropriate at entry specification gates to establish track record and organizational standing. It is not sufficient at completion verification gates unless the criterion being verified is specifically about organizational standing rather than project outcomes.

**Activity evidence** attests that named activities occurred at a stated date, location, and scale. Activity evidence proves that work was done. It does not prove that outcomes resulted from that work.

Required elements: the date or date range of the activity; the location; the activity type (for example, coral restoration dive, water distribution event, community training session); a quantity metric (for example, number of participants, volume distributed, area surveyed, coral fragments planted); and the counting methodology for that metric. For field scientific monitoring data, the counting protocol must be named: two organizations counting coral fragments using different methods produce non-comparable numbers even under the same field label. Accepted counting protocol sources include named sector standards (for example, GCRMN Reef Monitoring Protocol), named institutional methodologies, or the organization's own documented protocol stated in full.

Activity evidence is appropriate at progress verification gates. It is not sufficient at completion verification gates for criterion claims about outcomes or impact.

**Outcome evidence** attests that a named condition changed, a performance claim is verified, or a deliverable meets its completion criteria, independently of the applicant's own report. Outcome evidence is the only evidence type that satisfies a completion verification gate for claims about results.

Required elements: the measurement methodology at a level sufficient for independent replication (not just the data source, but the specific procedure used to collect the measurement); the baseline value (what was true before the intervention); the post-intervention value; the identity of the measuring party (the applicant's own report requires named independent corroboration; independent third-party verification is preferred); and, for scientific or technical performance claims, the testing conditions under which the result was obtained. Claims about efficiency rates, ecological conditions, or health outcomes without a named testing methodology and an accessible laboratory or monitoring record do not constitute outcome evidence.

Outcome evidence is required at completion verification gates. Social media posts, institutional endorsement letters, and field activity photographs are not outcome evidence.

**Planning evidence** attests to future intent, procurement arrangements, or structural agreements between parties. Planning evidence proves that plans, commitments, or procurement has been initiated. It is not evidence that outcomes have been achieved.

Required elements: the document type (procurement quotation, memorandum of understanding, partnership agreement, letter of intent); the date; the parties; the scope of the commitment; and an explicit label that this document constitutes planning evidence, not outcome evidence. Procurement quotations for equipment not yet purchased, partnership letters describing intended collaboration, and MoUs establishing future working relationships all constitute planning evidence. They are valid supporting documents but must not be submitted in place of outcome evidence at completion gates.

**Financial accountability evidence** attests to how funding was deployed, categorized by expenditure type. Financial accountability evidence proves that money was spent as stated. It does not prove that the spending produced the stated outcomes.

Required elements: the period covered; total funds deployed in that period; expenditure by named category (for example, personnel, equipment, operations, distribution); the document type (fund utilization report, itemized receipt, audited financial statement, or invoiced supplier confirmation); and the verification path. Financial accountability evidence is required at reporting gates for grant programs that have activated disbursement-linked reporting. It is supporting context at completion gates, not sufficient evidence of outcome achievement on its own.

**Evidence type selection guidance:** The criterion intent determines which evidence type is required. A criterion that asks whether a technical claim has been demonstrated requires outcome evidence. A criterion that asks whether the organization has relevant institutional standing requires standing evidence. A criterion that asks whether activities occurred requires activity evidence. A criterion that asks whether planning or procurement is underway requires planning evidence. A criterion that asks how prior funding was deployed requires financial accountability evidence. A single criterion may require multiple evidence types; each must be named separately with its required elements stated.

**Formatting for independent access:** All evidence links must resolve without requiring the reviewer to log in to any service, request access from the applicant, or contact the applicant for credentials. Evidence stored behind authentication walls (Google account login, Dropbox access requests, service-specific logins) is inaccessible to independent reviewers and does not satisfy the evidence form requirement regardless of how strong the underlying document is. If a document cannot be made publicly accessible, it must be uploaded directly to the submission system in a format readable without proprietary software.

### 3.5 Conformance Threshold

**What It Requires:** For any field or criterion that references an external standard, the referencing party must specify: which components of the external standard apply to this criterion; what evidence satisfies each component; and what the minimum threshold for passage is (e.g., all nine indicators must be met, or at least six of nine indicators must be met with the remaining three requiring documented mitigation plans).

**Why It Is Required:** External standards are rarely binary. The Digital Public Goods (DPG) Standard has nine indicators, each with multiple sub-requirements. A criterion that says "Qualifies as DPG" without a conformance threshold delegates interpretation to reviewers: one reviewer may require all nine indicators; another may require six; a third may accept a DPG nomination as sufficient evidence regardless of indicator status. The conformance threshold eliminates this variance by specifying what the passage means before any application is reviewed.

**Failure Mode When Absent:** Reviewer-level interpretation variance becomes the de facto standard. Outcomes are determined partly by which reviewer a given application receives. The data cannot support cross-cohort comparison because the threshold was not held constant.

**Worked Illustration (Digital Public Goods (DPG) Standard):** A program requiring Digital Public Good status as a gate criterion must specify a conformance threshold that enumerates all nine indicators of the DPG Standard (relevance to a Sustainable Development Goal; use of approved open licenses; clear ownership; platform independence; documentation; non-extraction of data; adherence to privacy and applicable laws; adherence to standards and best practices; and responsible data use policies), states which evidence satisfies each indicator (e.g., "Indicator 2 requires a clearly stated SPDX license identifier in the project repository"), and names the minimum threshold for passage (e.g., "All nine indicators must be satisfied; indicators 1, 2, and 3 are non-waivable"). The conformance threshold must also explicitly address the registry question: the Digital Public Goods Alliance maintains a registry of projects that have previously been assessed against the standard. Registry membership is a record of past assessment, not a guarantee of current qualification. A project in the registry may have changed substantially since assessment; a project not in the registry may currently satisfy all nine indicators. The conformance threshold must state whether registry membership is accepted as sufficient evidence of current qualification, or whether independent indicator assessment is required regardless of registry status. Leaving this unstated produces the most common DPG evaluation failure: reviewers who check the registry as a proxy for indicator assessment, applying a standard the funder did not actually specify. A reference that says "the project must meet the DPG Standard" without this conformance threshold is not a criterion specification; it is a label.

### 3.6 Participatory Specification (Optional)

**What It Requires:** A documented record of whether the field definition was developed or validated with input from the population whose conditions the field measures. Where participatory specification has occurred, the record must name: who participated (described by role or relationship to the measured condition, not necessarily by personal identity), what aspect of the definition they contributed to or validated, and when the participation occurred relative to the field's publication.

**Why It Is Optional:** Not all fields measure conditions in a specific population whose members could provide input. Fields measuring technical system properties, financial structures, or categorical administrative statuses may have no population-level constituency to consult. The participatory specification element applies when the field measures a condition experienced by an identifiable group of people, and when consulting that group would materially affect the accuracy or appropriateness of the operational definition.

**Why It Matters When It Applies:** An operational definition of "community engagement" or "food security" or "water access" developed solely by the funder or program team encodes the program team's model of what those conditions mean. That model may diverge from how the affected population understands and experiences the condition. The divergence does not appear in the data because everyone answered the same field; it appears downstream, when the data fails to reflect what was actually true in the population. Participatory specification does not guarantee accuracy, but it documents whether the definitional basis was developed from inside or outside the experience being measured.

**Relationship to the Grant Maturity Index:** The participatory specification element addresses the community engagement dimension of the Grant Maturity Index (Biedermann and Gibrel, Metagov, arXiv:2410.19828). Programs that document participatory specification across their intake fields are providing structured evidence of community engagement in the design of their measurement instruments, not only in program delivery.

**How to Record It:** A participatory specification record is a brief structured note attached to the field specification document, not a separate publication or ethics review. It names the consultation process, the participants (by role), and what they contributed. It may also note where the program team did not consult the affected population and why. The absence of consultation is not a failure in itself; the absence of documentation about whether consultation occurred is the gap that participatory specification addresses.

---

### 3.7 Applicant Identity Fields as WALKRI Instruments

Identity fields are the most underspecified fields in grants intake. Every application form collects a project name, an organization name, and a contact. None of these fields, in standard practice, carry a criterion intent. The label "Project Name" does not specify what information the field is designed to collect: a legal entity name, a brand name, a repository name, a display name, or a self-assigned descriptor. As a result, applicants use these fields interchangeably with whatever self-reference feels natural in each moment, producing applications that refer to the same entity as "we," "I," "the project," "the organization," and three different proper nouns across consecutive fields. Reviewers cannot determine who is actually applying, and the accountability relationship between funder and funded entity is built on an ambiguous foundation.

WALKRI treats identity fields as instruments subject to the same five criterion specification requirements as measurement fields. The criterion intent for any identity field must state which type of entity the field is designed to identify. WALKRI recognizes three applicant identity instrument types, each with a specified operational definition:

**Legal entity instrument.** Criterion intent: identify the legal person or registered organization responsible for delivering the grant obligations and receiving disbursement. Operational definition: the name of the natural person (if applying as an individual) or the registered organization exactly as it appears in its jurisdiction of registration. The response must include the jurisdiction of registration and, for organizations, the registration number or equivalent public identifier. A trading name, brand name, project name, or GitHub organization name does not satisfy this criterion unless it is the legal name. Where no legal entity exists (an unincorporated collective or informal team), the applicant must state this explicitly and name the individual who assumes personal accountability for the obligation.

**Display name instrument.** Criterion intent: identify the publicly known name the applicant uses when presenting this work, which may differ from the legal entity name. Operational definition: the name used consistently in public communications, repositories, grant histories, and community contexts to refer to this project or organization. The display name must be consistent with the applicant's own prior public use; a name chosen specifically for this application that has not been used publicly before is not a display name, it is an alias.

**Prior entity relationship instrument.** Criterion intent: identify any other legal entity or organization under whose resources, employment, contracting relationship, or decision-standing rules the work claimed in this application was originally performed or developed. Operational definition: where an applicant claims prior work, a track record, a codebase, a user base, or a community as evidence of capability or contribution, the name of the entity under which that work was performed must be stated, along with the applicant's relationship to that entity at the time (employee, contractor, co-founder, contributor) and the current status of the relationship (active, ended, on what terms). This instrument activates whenever prior work is cited in the application. It does not activate for work that was performed entirely under the applying entity's own resources and governance.

**Self-reference consistency requirement.** A WALKRI-conformant application form must resolve every self-reference in every field to the declared legal entity or declared display name. Fields that accept free-text narrative (project description, milestone descriptions, evidence narratives) are not exempt. Where a narrative field uses a different self-reference than the declared legal entity or display name, the inconsistency is a WALKRI conformance flag. The flag is not automatically disqualifying; it must be overridden with a documented explanation of why the inconsistent self-reference is appropriate. An application that uses "we," "I," "the project," and three different proper nouns interchangeably without explanation has not resolved who is applying, and the identity instrument has failed its criterion intent.

**Public record query as evidence form for identity instruments.** For identity fields, the evidence form element of the WALKRI criterion specification may designate a public record query as the verification pathway. A public record query evidence form must specify: the registry, contract, or public database to be queried; the query that returns the relevant identity record; and what a satisfactory query result contains. Conformant examples include an on-chain profile registry query returning the applying entity's anchor address and founding attestation; a publicly queryable funder-signed gate record confirming the applicant's prior grant history; a public organizational registration database confirming the entity name and jurisdiction; or a cross-program grants database returning the applicant's funding history across rounds and programs. Where a public record query is the declared evidence form, the criterion specification must also state what happens when the query returns no result: whether the absence of a record is a gate failure, a flag requiring explanation, or a default-pass for first-time applicants. A public record query evidence form is not an alternative to applicant disclosure; it is an independent verification mechanism for the disclosure the applicant makes.

---

### 3.8 CROSS Entry Gate Declarations as WALKRI Instruments

CROSS v0.3.6 introduced five new required declarations at all entry specification gates, derived from the Revenue Architecture, Disbursement Authority, Continuity Capacity, Obligation Fulfillment Record, and Development Stage primitives (CROSS+WALKRI Primitives Foundation v0.1.2). Each of these declarations collects structured information through an intake field. WALKRI applies to all such fields: every entry gate declaration field in a CROSS-conformant program must satisfy the five criterion specification requirements before any applicant sees it.

This section provides the WALKRI instrument type specifications for each of the five CROSS entry gate declarations. These are reference specifications; a CROSS-conformant program using these declarations may use these specifications directly or may adapt them for their specific context, provided the adapted specification satisfies the five criterion requirements.

**Revenue architecture instrument.** Criterion intent: identify how the applying entity generates income outside of grants and donations, so that the additionality argument can be properly anchored to the entity's commercial position. Operational definition: the response must name one of four revenue architecture types. Grant-only means no commercial revenue model exists and the entity operates entirely from grants and donations; any fee charged for access to outputs, however small, disqualifies this type. Fee-for-service means the entity charges fees that are material to its operations but the entity remains grant-dependent for primary operational funding; the fees do not cover full operating costs without supplemental grants. Commercial means the entity generates income through a revenue model (subscriptions, licensing, transaction fees, advertising, or equivalent) sufficient to sustain operations without grants. Hybrid means the entity operates a commercial revenue stream alongside a separately operated public goods program, and the grant specifically covers the non-commercial scope. Response form: single-select from the four named types with a required short-text field for entities declaring fee-for-service, commercial, or hybrid type, in which the entity briefly describes their revenue model and approximate annual revenue. Justification: a binary yes/no to commercial revenue omits the hybrid case and the fee-for-service case, both of which require different additionality treatment. Evidence form: for commercial and hybrid types, a named public source confirming the commercial revenue model (company website pricing page, published fee schedule, app store listing, or equivalent). For grant-only, no independent evidence is required, but an application that subsequently discloses revenue in the concurrent funding disclosure is inconsistent with a grant-only revenue architecture declaration.

**Disbursement authority instrument.** Criterion intent: identify the named person or mechanism with legal authority to receive grant funds on behalf of the applying entity and approve their deployment, so that the accountability relationship is concretely anchored. Operational definition: the response must declare one of three disbursement authority states. Individual means one named natural person holds full authority to receive and deploy funds. Collective means authority is held collectively by a named mechanism (multisig, board vote, DAO governance) with the current key holders named and the quorum threshold stated. Delegated means authority is held by a named organizational role, with the current holder of that role named and the transfer mechanism stated. For DAO applicants without a legal wrapper, the disbursement authority declaration must name the controlling wallet address and decision-standing mechanism. Response form: single-select state plus structured sub-fields: for Individual, the full legal name of the authority holder; for Collective, the mechanism name, key holder names, and quorum threshold; for Delegated, the role name, current holder, and succession mechanism. Justification: a text field accepting any description produces inconsistent responses; the three-state structure constrains the response to verifiable content. Evidence form: for Individual, the authority holder is named in the applying entity's legal registration or publicly attributed organizational materials; for Collective, the multisig address or governance contract resolves on the declared chain; for Delegated, the role and its current holder are named in publicly accessible organizational documentation.

**Continuity capacity instrument.** Criterion intent: identify the applying entity's capacity to continue operating if the primary contributor becomes unavailable, so that the sustainability stance and continuation gate assessment have a factual basis. Operational definition: one of three states. Single means one person is essential to the entity's continued operation and no succession plan exists; the declaration must name the person and state what would happen to active funded work if that person became unavailable. Partial means the primary contributor is essential for direction but named secondary capacity exists for execution. Resilient means multiple contributors each hold documented responsibility for specific functions and the entity can continue without any single individual. Response form: single-select state with a required short-text field in which the applicant explains the basis for their declared state. Justification: a narrative field without defined states produces incomparable responses across the cohort. Evidence form: the named primary contributor is attributable from GitHub commit history, organizational documentation, or equivalent independent source.

**Obligation fulfillment record instrument.** Criterion intent: document the applying entity's history of meeting prior grant commitments, so that the committee has a factual basis for the track record assessment. This instrument activates only for returning applicants, applicants with prior grants from this funder, and applicants citing prior work as capability evidence. Operational definition: for each prior grant covered by the instrument, the record must state: what was committed (the deliverable specification or FROM-TO state from the prior entry gate); what was produced (named artifact, published report, or measured change with a publicly accessible link); and one of three fulfillment states (fulfilled, partially fulfilled, unfulfilled) with an explanation for any state other than fulfilled. Response form: a structured repeating unit, one instance per prior grant in scope. Justification: a single text field produces narrative that cannot be consistently assessed across the cohort. Evidence form: each claimed deliverable has a publicly accessible link from a source outside the applicant's control; each claimed measurement has a named data source.

**Development stage instrument.** Criterion intent: identify where the applying work sits on the five-stage maturity scale at the time of application, so that the committee can assess stage-obligation mode consistency and the funder can apply stage targeting criteria. Operational definition: one of five stages. Stage 1 (proof of concept): the artifact has been built and tested in controlled conditions; no external users outside the team have used it in production. Stage 2 (early adoption): at least one external user has used it in real conditions; adoption is small but independently verifiable. Stage 3 (growth): a growing user base is independently verifiable; adoption trend is visible in public data. Stage 4 (established infrastructure): sustained operation with documented community value has been confirmed for at least 12 months; the central question is continuation, not validation. Stage 5 (retroactive recognition): the contribution is complete and its value is assessable from historical evidence. Response form: single-select stage number plus two required fields: a brief explanation of why the work is at this stage rather than the adjacent stages, and at least one piece of independently verifiable evidence confirming the declared stage. Justification: a free-text description of maturity without defined stages produces incomparable responses. Evidence form: Stage 1, publicly accessible code repository or artifact with documented test results; Stage 2, named external user or integration with a publicly accessible link; Stage 3, independently accessible usage data (download counts, on-chain transactions from external addresses, public analytics); Stage 4, 12 months of sustained usage data from an independent source; Stage 5, historical documentation of the contribution with independent attribution.

**Self-reference consistency requirement.** All five CROSS entry gate declaration fields are subject to the self-reference consistency requirement from Section 3.7. Every self-reference within each declaration field must resolve to the declared legal entity or declared display name. An application that uses different entity names across the revenue architecture declaration and the organizational identity declaration is a WALKRI conformance flag requiring Block J investigation.

---

### 3.9 Instrument Dependency Declaration

The five criterion specification requirements specify an instrument as a node: what it measures, how its responses are defined, its response form, its evidence, and its conformance threshold. They do not specify how instruments relate to each other. An instrument set carries edges as well as nodes: an instrument may be activated or hidden by an upstream response, its conformance threshold may not be assessable until another instrument resolves, and instruments may be subject to ordering or cross-instrument consistency constraints. A WALKRI certification that assesses only the nodes leaves these edges unassessed, so a certified form can contain conditional logic the certification never examined.

**What It Requires:** For a form or instrument set to be WALKRI-conformant, its dependency graph must be certified alongside its instruments. The dependency graph names, for each instrument: its activation conditions (what upstream response makes it appear or apply), its assessment dependencies (what must resolve before its conformance threshold can be assessed), its ordering constraints, and its cross-instrument consistency constraints.

**Derive, Do Not Re-Author:** The dependency graph is not a separate author-written declaration. An author-written declaration duplicates logic the instrument set already carries, and the duplicate drifts from the live logic, reintroducing the unassessed divergence the requirement exists to prevent. Instead, the graph is derived mechanically from the instrument set's own formal logic. WALKRI is JSON Schema native and the conditional keywords are formal; the form-rendering formats carry the same edge logic natively, and the read-out for each is specified in WALKRI-interface-specification-0_1_0.md. The designer performs a per-instrument trigger evaluation, records an explicit finding for each instrument including the explicit none finding where an instrument has no dependencies, and attests to the derived graph. The attestation is over an artifact an auditor can regenerate from the specification, so there is one source of truth rather than two that can diverge.

**Declared-Absent for Independent Instruments:** An instrument with no dependency edges declares this in one word (independent), using the Declared-Absent convention, so a shallow form with no conditional logic pays almost nothing while a form with branching logic carries its full graph. What is certified is the instrument set together with its derived and attested dependency graph.

**Why It Is Required:** A criterion specification that is precise at every node can still produce non-comparable data if the path through the instruments is unspecified. The edge structure determines what any given respondent actually encounters and is assessed on; leaving it uncertified leaves a soundness hole at the form level that the node-level requirements cannot close.

**Failure Mode When Absent:** A form passes certification on its nodes while carrying skip logic, branching, and ordering constraints that determine what any given applicant actually sees and is assessed on. Two applicants traverse different paths through the same certified form, the path structure was never assessed, and the resulting data mixes responses produced under different effective instruments under a single field label.

---

## Part IV: The Three-Stage Process

WALKRI specifies a three-stage process for producing WALKRI-conformant fields. The stages may be traversed by a funder designing new fields, an auditor reviewing existing fields, or an AI assistant guiding either. All three stages are required for WALKRI certification. A form produced by skipping Stage 1 or Stage 3 may appear complete, but it fails the conditions that make the field work in practice.

### 4.1 Stage 1: Ideation

**What The Stage Produces:** An ideation record: a structured document that names each information need the form is intended to satisfy, the decision that each piece of information will inform, and the failure mode if that information is missing or imprecise. The ideation record is not published to applicants; it governs the field design process in Stage 2.

**Who Performs It:** The question-holder: the funder, program, organization, or researcher who will use the collected data to make decisions.

**How It Connects To Stage 2:** Each piece of information needed in the ideation record becomes the input for one field specification in Stage 2. The criterion intent for each Stage 2 field is derived directly from the ideation record's description of the information need. If a Stage 2 field cannot be traced to an ideation record entry, that field lacks a documented rationale and cannot be certified.

**The Downward Interface To The Chain:** When WALKRI operates inside an evaluation chain, the ideation record is where the chain's decision context enters instrument design. The information needs the ideation record names are the chain's decision context, in CRAFT terms the Condition 1 content (what decision the data informs, for whom, what would make the data a good input, and what would make it invalid), expressed as demands on the instruments that will capture it. This is the downward half of the composition relationship described in Part XI: the chain communicates its decision context down to the instruments through the ideation record, and the instruments communicate their resulting precision back up through the conformance record (Section 8.3). When WALKRI is used standalone, the ideation record carries the question-holder's own decision context in the same structural slot.

**Failure Mode When Skipped:** Fields created without an ideation record are typically labels rather than instruments. The creator encodes what they assumed the question was rather than what they actually needed to know. When the data fails to support the decision it was collected for, there is no ideation record to diagnose where the design broke down.

### 4.2 Stage 2: Specification

**What The Stage Produces:** A WALKRI field specification: a structured document for each field containing all five criterion specification requirements from Part III. The field specification is the artifact that defines the rendered tools and that the WALKRI Audit Tool assesses.

**Who Performs It:** The question-holder, working from the ideation record, or a field specification practitioner working from a brief provided by the question-holder. The WALKRI Ideation Tool and the WALKRI Audit Tool (described in Part IX) support this stage.

**How It Connects To Stage 3:** The operational definition and examples in the Stage 2 specification are the source material for Stage 3 applicant guidance. Stage 3 does not add new definitional content; it translates the Stage 2 specification into applicant-facing language. If the Stage 2 specification is incomplete, the Stage 3 guidance will be incomplete.

**The Pre-publishing Quality Gate:** Before any field is shown to applicants, it must pass an AI-assisted review that assesses the field specification against Parts III through VII of this standard. The review flags any of the five criterion specification requirements that are absent or insufficient. Flags are either resolved (the specification is revised to address the flag) or overridden. An override requires a documented justification explaining why the flag does not apply to this field's context. Overrides are recorded in the conformance record produced at certification; they are not failures, but they are disclosed. A field with unresolved and undocumented flags is not eligible for certification.

**Failure Mode When Skipped:** Fields are built directly from the ideation record, bypassing a formal specification. The intent is embedded in the question-holder's head rather than in a document. Reviewer inconsistency emerges because there is no specification to adjudicate disputes. Downstream data consumers inherit a dataset with no machine-readable field definitions.

### 4.3 Stage 3: Applicant Guidance

**What The Stage Produces:** Applicant-facing documentation accompanying each field. This documentation explains: what the field is asking; what a complete response looks like (with at least one positive example); what common incomplete or incorrect responses look like (with at least one negative example); and why the field exists (briefly, as context, not as justification).

**Who Performs It:** The question-holder or a communications practitioner working from the Stage 2 field specification. The WALKRI Guidance companion document (WALKRI-guidance-0_1_0.md) provides templates and worked examples.

**How It Connects To Stage 2:** Stage 3 documentation is derived from Stage 2's operational definition and examples. No new definitional content is introduced in Stage 3. The translation from specification language (designed for precision) to applicant language (designed for comprehension) is the core work of this stage.

**Failure Mode When Skipped:** Even a precisely specified field produces inconsistent responses if applicants cannot interpret it correctly. The failure mode is structurally identical to that of an underspecified field: interpretation variance in the applicant population produces nominally consistent data with hidden definitional variance.

---

## Part V: Data Quality Standards

Five data quality standards apply to all fields across all obligation modes. They apply whether or not any external obligation standard applies to the collection.

For each standard, the assessment question is what an auditor asks when evaluating a field. The failure mode describes what happens to the data when the standard is not met. The connecting note identifies which criterion specification requirement from Part III the standard most directly enforces.

### 5.1 Validity

**Assessment Question:** Does the measurement instrument have a documented logical chain from the evidence specified in the evidence form to the result claimed in the criterion intent?

**Failure Mode:** The field measures a proxy for the intended construct rather than the construct itself, but the proxy relationship is undocumented. Analysis treats the measurement as a direct observation of the construct and reaches conclusions that are valid for the proxy but not for the construct. The error is invisible because there is no criterion intent statement against which to test the logical chain.

**Application Across Field Types:** For quantitative indicators, validity requires that the construction methodology produce a number that logically represents the criterion's intent measurement claim. For binary completion criteria, validity requires that the evidence form specifies an artifact whose presence or absence logically indicates the criterion. For qualitative narrative fields, validity requires that the scope defined in the operational definition logically captures the dimension the criterion intent claims to measure.

**Connection To Part III:** Validity most directly bears on the criterion intent requirement (3.1), because a validity failure is a failure to connect the evidence form to the criterion intent through a logical chain.

### 5.2 Integrity

**Assessment Question:** Is evidence collection separated from the actor who benefits from a favorable outcome?

**Failure Mode:** Self-reported evidence without third-party verification yields data whose accuracy is systematically biased toward favorable outcomes. The bias is not necessarily dishonest; actors rationally interpret ambiguous situations in ways that favor their position. Without separation between the evidence collector and the beneficiary, the data reflects this rational bias and cannot be used to compare actors on a common scale.

**Application Across Field Types:** For quantitative indicators, integrity requires an independent data source or a verification pathway that separates the reporting actor from the data. For binary completion criteria, integrity requires that the specified artifact can be verified by a reviewer without relying on the applicant's characterization. For qualitative narrative fields, integrity is structurally harder to enforce; the standard applies as a design aspiration and a disclosure requirement (the reviewer must know that the field relies on self-report).

**Connection To Part III:** Integrity most directly bears on the evidence form requirement (3.4), because the evidence form is where the source and verification pathway of the evidence are specified.

### 5.3 Precision

**Assessment Question:** Is the measurement instrument capable of detecting differences at the magnitude relevant to the decisions the data will inform?

**Failure Mode:** A single-select field with three options (low, medium, high) cannot distinguish between a program that reached 10 people and one that reached 100 people if both fall into the "low" bucket. If the decision requires distinguishing between these programs, the instrument is too coarse to support such a distinction. The failure produces a dataset that appears complete but is informationally insufficient for its stated purpose.

**Application Across Field Types:** For quantitative indicators, precision requires that the unit and counting rule are fine-grained enough to detect the relevant differences. For binary completion criteria, precision is binary by construction; the precision question is whether the binary distinction is the right one or whether the decision requires a more granular assessment. For qualitative narrative fields, precision requires that the scope of the operational definition be narrow enough to yield responses that are meaningfully comparable.

**Connection To Part III:** Precision most directly bears on the response form requirement (3.3) because the response form determines the measurement instrument's resolution.

### 5.4 Reliability

**Assessment Question:** Is the methodology for collecting and interpreting this field consistent across reporting periods and across reviewers within a single reporting period?

**Failure Mode:** A field whose interpretation changes across reporting periods produces data that cannot be compared over time. A field whose interpretation varies among reviewers within a reporting period yields data that reflect reviewer assignment rather than applicant characteristics. Both failures produce longitudinal or cross-sectional analyses whose conclusions cannot be attributed to changes in the underlying population.

**Application Across Field Types:** For quantitative indicators, reliability requires that the construction methodology be documented in sufficient detail to be applied consistently across periods without reinterpretation. For binary completion criteria, reliability requires that the evidence form specifies a verifiable artifact rather than a judgment call. For qualitative narrative fields, reliability requires a scoring rubric or codebook that reviewers apply consistently; a field without a rubric is inherently unreliable.

**Connection To Part III:** Reliability most directly bears on the operational definition requirement (3.2), because consistency of interpretation across periods and reviewers depends on the definition being precise enough to constrain interpretation.

**Calibration record requirement:** Where a field has a conformance threshold (Section 3.5), the field specification must include a calibration record documenting how reviewers are expected to reach consistent assessments on borderline cases. The calibration record must contain: at least two worked examples of responses that clearly satisfy the conformance threshold with explanation of why they satisfy it, at least two worked examples of responses that clearly fail the conformance threshold with explanation of why they fail, and at least one worked example of a borderline case with explicit documentation of how the reviewer should resolve the ambiguity. The calibration record is not a training document; it is a specification document. Its purpose is to make the conformance threshold operational for independent reviewers who did not design the field. A conformance threshold that cannot produce a calibration record has not been specified with sufficient operational clarity to satisfy the reliability standard. The calibration record is part of the field specification and is subject to the pre-publishing quality gate.

### 5.5 Timeliness

**Assessment Question:** Is the evidence specified in the evidence form current to the decision cycle for which the data is being collected?

**Failure Mode:** Evidence that is technically present but outdated misleads decisions that depend on the applicant's current state. A three-year-old impact assessment submitted as evidence of current reach produces a favorable data point for a decision that should have been made on current information. The decision is made on stale data, and the failure is invisible because the evidence form did not specify a recency requirement.

**Application Across Field Types:** For quantitative indicators, timeliness requires that the evidence form specify the time period the data must cover relative to the submission date. For binary completion criteria, timeliness requires that the artifact attesting to completion is recent enough to be probative. For qualitative narrative fields, timeliness requires that the scope in the operational definition specify whether responses must reflect current practice or may reflect historical practice.

**Connection To Part III:** Timeliness most directly bears on the evidence form requirement (3.4), because the evidence form is where recency requirements and time-period specifications must appear.

---

## Part VI: External Standard Reference Protocol

Any field or criterion that references an external standard must follow the External Standard Reference Protocol. A reference to an external standard without this protocol is not a criterion specification; it is a delegation of interpretation to whoever reviews the field. The resulting data is unauditable and inconsistent.

### 6.1 Required Reference Elements

A conformant external standard reference must include the following elements.

**Identifier type and identifier value.** The canonical identifier for the external standard, expressed as a type-value pair. Identifier type determines how the standard is resolved and versioned. The recognized types are defined in Section 6.2. A URL alone is not a sufficient identifier for standards that have more stable canonical identifiers (e.g., DOIs, ISO numbers, RFC numbers, SPDX identifiers). Use the most stable identifier type available for the referenced standard.

**Resolution method.** How the standard is accessed, given its identifier type and access model. For open standards, the resolution method is the URL or resolver endpoint. For paid standards, the resolution method is typically a certification body certificate or a licensed copy; direct URL resolution is not possible. The resolution method must be stated so that a reviewer can determine whether they can independently verify the standard text, and if not, what evidence of conformance is accepted in its place.

**Version anchor.** A version number, release tag, commit hash, or date-stamped access record sufficient to identify the exact version of the external standard in effect when the field was designed. External standards evolve; a reference without a version anchor cannot be audited because the auditor cannot determine which version applied. For standards with semantic versioning, the version number is the anchor. For standards versioned by repository commit, the commit SHA is the anchor. For standards with no versioning system, the SHA-256 hash of the accessed document is the anchor, paired with an access date.

**Access model.** A statement of how the standard is accessible to applicants and reviewers. The four recognized access models are defined in Section 6.3. Access model disclosure is required because it determines what counts as valid evidence of compliance: a reviewer cannot verify a standard they cannot access, and the conformance threshold must account for this.

**Scope.** A statement of which part of the external standard applies to this criterion. Many external standards are multi-part documents; the scope statement identifies which indicators, sections, or requirements are germane. A reference to the whole standard when only three indicators apply is not a scope specification; it transfers the scoping decision to reviewers.

**Conformance threshold.** The enumeration of which components of the external standard must be satisfied for passage, what evidence satisfies each component, and the minimum threshold for passage. The conformance threshold is the mechanism that prevents reviewer-level interpretation variance from determining outcomes. See Section 6.4.

**Archival anchor (required for URL-type identifiers; recommended for all others).** A stable archival reference that will remain accessible if the primary URL changes or the standard is updated. Accepted forms: a Perma.cc link, a Wayback Machine URL, or a repository commit SHA. For standards with stable canonical identifiers (DOI, ISO, RFC, SPDX), the canonical identifier itself serves as an archival anchor, and a separate one is not required. For standards accessed via a general URL, an archival anchor is mandatory.

**Licensing notes (required when the conformance threshold reproduces standard text).** A statement of the licensing terms under which the external standard is published, and whether those terms impose any obligation on how the conformance threshold may be written. Referring to a standard for assessment purposes does not create a licensing obligation. A conformance threshold that reproduces indicator text verbatim from a CC-BY-SA standard requires attribution. A conformance threshold referencing an ISO standard may not reproduce ISO text directly and must paraphrase or cite by indicator number; direct reproduction requires a license from the relevant national standards body.

### 6.2 Identifier Types

Different external standards use different identifier systems. Use the most stable identifier type available.

**DOI (Digital Object Identifier).** Stable, persistent identifier registered with a DOI registration agency. Resolves via https://doi.org/[doi-value]. Version-locked: each DOI points to a specific version of the document. Commonly used for academic standards, some government publications, and formal technical specifications.

**ISO number.** International Organization for Standardization document number, including the year of the version (e.g., ISO 27001:2022). ISO standards are not publicly available; resolution requires purchase through the ISO store or a national standards body. The identifier is the canonical reference; the resolution method is certification-body evidence or a licensed copy.

**IETF RFC number.** Internet Engineering Task Force Request for Comments. RFCs are immutable once published; an RFC number unambiguously identifies a specific, unchanging document. Resolves via https://datatracker.ietf.org/doc/html/rfc[number]. No version anchor is needed beyond the RFC number itself.

**SPDX identifier.** Software Package Data Exchange license identifier (e.g., MIT, Apache-2.0, CC-BY-SA-4.0). SPDX identifiers are canonical, immutable, and resolve via https://spdx.org/licenses/[identifier]. Used when the external standard being referenced is a specific open license. No version anchor is needed beyond the SPDX identifier itself.

**W3C dated URL.** World Wide Web Consortium specifications use dated URLs as permanent references (e.g., https://www.w3.org/TR/2023/REC-...). The dated URL is the version anchor; use it rather than the undated /TR/ shortcut URL, which redirects to the current version.

**ELI URI (European Legislation Identifier).** Persistent identifier for European Union legal documents. Resolves via the EU Publications Office. Used when referencing EU regulations, directives, or decisions as external standards.

**Regulatory citation.** Structured citation for national or regional regulatory documents (e.g., 45 CFR Part 46, Article 9 GDPR). No single canonical URL exists for most regulatory documents; the regulatory citation is the identifier, and resolution is via the relevant government portal or legal database. For regulatory citations, the access date and the version of the regulation in effect at that date serve as the version anchor.

**Repository version tag.** For standards published and versioned in a code repository (e.g., GitHub). The identifier is the repository URL plus the version tag (e.g., github.com/DPGAlliance/DPG-Standard, tag v1.1.7). The commit SHA for that tag is the archival anchor. Used for standards that do not have a more stable identifier type.

**IRIS+ indicator identifier.** The GIIN IRIS+ catalog identifier for a specific impact indicator (for example, PI2919 for "Number of individuals who accessed a product or service"). IRIS+ identifiers are stable within a version of the catalog. Resolves via https://iris.thegiin.org/metric/[identifier]. Version anchor: the IRIS+ catalog version (current: v5.3c). Access model: open and free. Used when a field or criterion references a specific IRIS+ indicator as its measurement standard. No archival anchor is needed beyond the catalog version and identifier; IRIS+ maintains a stable catalog registry.

**URL (general).** Used when none of the above apply. A URL alone provides the least version stability; it must be accompanied by an access date and an archival anchor (e.g., Perma.cc or the Wayback Machine). A general URL is the identifier of last resort.

### 6.3 Access Models

The access model determines what evidence of conformance is accepted when a reviewer cannot independently verify the standard text.

**Open and free.** The standard text is publicly accessible without registration, payment, or institutional affiliation. A reviewer can verify the text directly. Evidence of conformance may reference the standard text.

**Open with registration.** The standard text is publicly accessible but requires account creation. Reviewers can register and verify. Evidence of conformance may reference the standard text. The registration requirement should be noted in the reference so reviewers are not surprised.

**Paid and licensed.** The standard text requires purchase. Reviewers generally cannot verify the text independently. Evidence of compliance takes the form of certification body certificates, auditor attestations, or licensed excerpts rather than direct text verification. The conformance threshold must specify what certification evidence is accepted in place of text verification.

**Government and regulatory.** The standard is a legal or regulatory document accessible via government portals. Resolution is by regulatory citation. Evidence of compliance may include regulatory filings, legal attestations, or documentation demonstrating conformance with the named regulation. Availability varies by jurisdiction; some regulatory texts are freely accessible, others require access to legal databases.

### 6.4 The Conformance Threshold Requirement

The conformance threshold is the most frequently omitted element of the external standard reference protocol, and its absence is the most consequential failure. When a threshold is absent, reviewers must construct their own interpretation of what "conformant with the referenced standard" means. Different reviewers construct different interpretations. The data reflects reviewer assignment rather than applicant compliance with the standard.

A conformance threshold is not a summary of the referenced standard. It is a specification of how the referenced standard applies to this specific criterion in this specific context. The threshold must be explicit enough that a reviewer who had never seen the external standard before could apply it consistently with a reviewer who had studied it in depth.

### 6.5 Worked Illustrations

**Illustration 1: The Digital Public Goods Standard**

The Digital Public Goods Standard is a nine-indicator standard used by the Digital Public Goods Alliance to assess whether a digital solution qualifies as a digital public good. It is the most commonly referenced external standard in open-source software and technology grant programs.

Identifier type: repository version tag. Identifier value: github.com/DPGAlliance/DPG-Standard, tag v1.1.7. Version anchor: commit SHA for that tag. Access model: open and free. Archival anchor: commit SHA. Licensing notes: the DPG Standard is published under CC-BY-SA 4.0; a conformance threshold that reproduces indicator text verbatim requires attribution; paraphrased thresholds do not.

A program that uses DPG qualification as a gate criterion must produce a conformance threshold that:

1. Names all nine indicators: (1) relevance to a Sustainable Development Goal, (2) use of an approved open license, (3) clear ownership, (4) platform independence, (5) documentation, (6) non-extraction of data, (7) adherence to privacy and applicable laws, (8) adherence to standards and best practices, and (9) responsible data use policies.

2. States what evidence satisfies each indicator. For example, Indicator 2 requires a clearly stated SPDX license identifier in the project repository's root-level LICENSE file or README; a reference to a license in prose text without an SPDX identifier does not satisfy this indicator.

3. States the minimum threshold for passage. For example, All nine indicators must be satisfied for gate passage. Indicators 1, 2, and 3 are non-waivable. For indicators 4 through 9, an applicant who cannot satisfy an indicator may submit a documented mitigation plan; a maximum of two indicators may be satisfied via a mitigation plan.

A reference that states "the project must meet the DPG Standard" without these elements does not constitute a conformance threshold. It is a label.

**The registry distinction.** The Digital Public Goods Alliance registry records past assessments. Registry membership confirms that a project was assessed at some point in the past and met the standard at that time. It does not confirm current qualification: the project, its dependencies, or the standard itself may have changed. A conformance threshold that accepts registry membership as evidence of current qualification must state this explicitly and accept the limitation. A conformance threshold that requires an assessment of current indicators must specify which indicators apply and what evidence satisfies each, regardless of registry status. Leaving the registry question unstated is the most frequently observed failure of the DPG conformance threshold.

---

**Illustration 2: An ISO Standard**

Programs requiring information security management conformance may reference ISO 27001. This illustrates the paid-and-licensed access model and its implications for conformance threshold design.

Identifier type: ISO number. Identifier value: ISO 27001:2022. Version anchor: the year in the ISO number (2022) is the version anchor; no separate anchor is needed. Access model: paid and licensed. Resolution method: ISO 27001:2022 is available for purchase from ISO or national standards bodies; reviewers cannot verify the text independently without a license. Archival anchor: the ISO number itself is stable; no URL-based archival anchor applies.

Because reviewers cannot independently verify the ISO 27001 text, the conformance threshold must specify what certification evidence is accepted: for example, a current ISO 27001:2022 certification from an accredited certification body, with the certification body named and the certification scope statement provided. The conformance threshold must state the minimum scope required (which systems, processes, or assets must be in scope for the certification to satisfy the criterion) and the maximum acceptable age of the certification at the time of gate assessment.

Conformance thresholds for paid-and-licensed standards may not reproduce the standard's requirement text directly. Paraphrase or cite by clause number.

---

**Illustration 3: An SPDX License Identifier**

Programs requiring open-source licensing must specify which licenses qualify. SPDX identifiers are the correct mechanism.

Identifier type: SPDX identifier. Identifier value: the list of accepted SPDX identifiers (e.g., MIT, Apache-2.0, GPL-3.0-only, AGPL-3.0-only). Version anchor: SPDX identifiers are immutable; no version anchor is needed beyond the identifier itself. Access model: open and free (https://spdx.org/licenses/). Archival anchor: not required; SPDX identifiers are canonical and stable.

The conformance threshold must state whether the criterion accepts any OSI-approved license (in which case the full OSI-approved SPDX identifier list is the scope), a specific list of acceptable identifiers, or a specific list with exclusions. A conformance threshold that says "the project must use an open-source license" without naming the accepted SPDX identifiers is not a threshold; it transfers the interpretation to reviewers who will apply different definitions of "open-source."

---

## Part VII: Provenance and Schema Requirements

WALKRI-conformant data collection produces two categories of obligations: provenance fields that must accompany the data, and schema requirements that set how field definitions change over time.

### 7.1 Provenance Fields

Every WALKRI-enriched dataset must include the following provenance fields at the dataset level and, where technically feasible, at the field level:

**Field Creator Identity:** An organizational identifier or practitioner identifier for the entity that designed the field specification. This field enables downstream consumers to contact the specifying entity for definitional clarification and supports accountability for data quality decisions.

**Specification Timestamps:** ISO 8601 timestamps for when the field specification was created and last modified. These timestamps are distinct from the timestamps on the collected data; they record the history of the instrument, not the history of responses to it.

**Walkri Version:** The version of this standard that governs the field specification. Version differences in the standard may affect the interpretation of conformance; downstream consumers need this information to assess whether a field specification meets the version of the standard they are using.

**Form Tool Identifier:** The class of form tool used to render the field (e.g., "KoBoToolbox," "REDCap," "Fillout"), not the specific instance or deployment. This supports reproducibility assessment: a downstream consumer can determine whether the rendering tool class imposes any known constraints on response capture.

**Field Specification Version:** The version of the field specification itself, distinct from the WALKRI version. Field specifications evolve independently of the standard; the field specification version tracks changes to the definition of a specific field.

### 7.2 Schema Requirements

WALKRI imposes three schema requirements on organizations that collect data under WALKRI-conformant fields:

**Consistency Across Reporting Periods:** Field names and their associated definitions must remain consistent across reporting periods unless a versioned change is documented. A field name that appears in two consecutive reporting periods is assumed to refer to the same construct; if the construct has changed, the field must be versioned rather than silently redefined.

**Versioning Of Changes:** Any change to a field definition produces a new field specification version. The prior definition is retained in the specification record and remains accessible. A downstream consumer aggregating data across reporting periods must be able to access the definition that governed each period's data.

**Comparability Documentation:** Changes that affect comparability across reporting periods must be documented with the date of the change, the nature of the change, and its implications for prior data. If an option was added to a single-select field in a new reporting period, the documentation must state what applicants who selected the nearest equivalent option in prior periods were actually reporting, and whether the new option represents a previously unmeasured category or a refinement of an existing one.

### 7.3 Alignment with Output Standards

WALKRI's provenance fields and schema requirements are designed to produce output that meets three external data standards. The alignment is declared here as a design commitment; the detailed mapping specifications appear in WALKRI-interface-specification-0_1_0.md.

Croissant alignment ensures that WALKRI-enriched datasets are machine-readable by ML pipelines without manual metadata reconstruction. FAIR alignment ensures that WALKRI-enriched datasets are findable, accessible, interoperable, and reusable by any downstream consumer. W3C PROV alignment ensures that the provenance history of any data element can be expressed in a standard, tool-independent provenance graph.

---

## Part VIII: WALKRI Certification

### 8.1 What Certification Means

WALKRI certification means that a form or field set has been audited against Parts III, IV, V, VI, and VII of this standard and meets the minimum conformance threshold. Certification is per form version, not per organization. An organization may hold certification for one version of a form while a concurrent version is under audit.

Certification does not mean that the certified form will produce perfect data. It means that the form's fields are specified with sufficient precision that the sources of variance in the collected data are attributable to real differences in the applicant population rather than to definitional ambiguity in the instrument.

### 8.2 Certification Scope

A change to any field definition triggers re-audit for that field. If a form is modified between reporting periods, the modified fields must be re-audited; fields that were not changed retain their prior certification status. The conformance record documents which fields were audited in which audit cycle, so downstream consumers can determine whether the version of the form used in a given reporting period was certified for that period.

### 8.3 The Conformance Record

Certification produces a conformance record: a structured document that is the primary artifact of the certification process. The conformance record contains:

- The audit date (ISO 8601)
- The WALKRI version applied
- The form version that was audited
- For each field: the field name, the field specification version, and the pass/fail/override status of each of the five criterion specification requirements
- For each override: the text of the flag, the justification for the override, and the name or identifier of the person who authorized it
- For each instrument: the derived and attested dependency declaration (Section 3.9), or the Declared-Absent value (independent) where the instrument has no dependency edges
- For each instrument, when WALKRI operates inside an evaluation chain: the chain condition the instrument serves (its layer attribution), or the Declared-Absent value where WALKRI is used standalone

The conformance record is the artifact that a WALKRI-certified program can produce to demonstrate data quality to downstream data consumers, funders, or research partners. It is the machine-readable proof that the form was designed to a known standard.

**Upward recomposition.** When the chain-condition attribution is present, the conformance record recomposes into condition-satisfaction evidence: the certified instruments serving a given chain condition are the instrument-quality evidence that the condition's capture points are sound, which a chain standard above can receive (in CRAFT terms, through its Section 12 layer attribution). The record carries each instrument's conformance with the resolution its criterion elements specify rather than a bare pass mark, so what travels upward is the precision actually achieved at the capture point. This is the upward half of the composition relationship described in Part XI; the downward half is the ideation record (Section 4.1).

### 8.4 Minimum Conformance Threshold

For a field to pass certification, it must satisfy all five criterion specification requirements. A field that satisfies four of five requirements does not pass; it produces a flag that must be resolved or overridden. The minimum conformance threshold for a form is that all fields pass certification, with overrides permitted where documented. A form with unresolved, undocumented flags cannot be certified.

---

## Part IX: Implementation Architecture

WALKRI is implemented through three product-layer tools. These tools are described in implementation documents; this Part names them and states their relationship to the standard. Any tool that assesses field specifications against Parts III through VII of this standard and produces a conformance record satisfies the WALKRI audit function. A reference implementation is available, but it is not the required implementation.

### 9.1 WALKRI Ideation Tool

The WALKRI Ideation Tool guides question-holders through Stage 1, producing an ideation record. It prompts the question-holder to name each information need, identify the decision it informs, and articulate the failure mode if the information is imprecise or absent. The output is a structured document formatted for direct use as input to the WALKRI Audit Tool in Stage 2. This function may be implemented in any tool that supports structured ideation workflows.

### 9.2 WALKRI Audit Tool

The WALKRI Audit Tool assesses field specifications against Parts III through VII of this standard. It is the pre-publishing quality gate described in Part IV. The tool accepts a field specification in JSON Schema format (or in the secondary compatible formats specified in Part II) and returns a conformance assessment identifying which of the five criterion specification requirements are satisfied and which produce flags. Flags are annotated with the specific failure mode (drawn from Part III) and a suggested resolution. The tool produces the conformance record described in Part VIII when a full form audit is complete. Any tool satisfying these requirements is a conformant WALKRI audit implementation.

### 9.3 WALKRI Enrichment Layer

The WALKRI Enrichment Layer is a post-submission webhook processing system that adds provenance fields to collected data and transforms it into Croissant/FAIR/W3C PROV-aligned output. It operates downstream of the form tool's data collection layer, receiving submitted responses and enriching them with the field-level and dataset-level provenance fields specified in Part VII. The Enrichment Layer does not modify responses; it adds metadata to the dataset. The enriched output is the artifact passed to downstream data consumers, analysts, and AI pipelines.

---

## Part X: Institutional Framework Alignment

WALKRI is designed to be adopted within any grants, research, or program evaluation context. This Part documents how WALKRI's requirements relate to established institutional frameworks, so that organizations already operating under those frameworks can understand what WALKRI conformance produces in terms they recognize.

### 10.1 IRIS+ (Global Impact Investing Network, v5.3c)

IRIS+ specifies metadata requirements for impact indicators: indicator name, definition, data type, unit of measurement, calculation methodology, data collection instructions, evidence rationale, and SDG linkage. WALKRI's five criterion specification requirements produce all of this metadata as a structural consequence of conformance.

WALKRI criterion intent maps to IRIS+ evidence rationale. WALKRI operational definition maps to IRIS+ indicator definition, data type, and unit of measurement. WALKRI response form maps to IRIS+ data type and aggregation guidance. WALKRI evidence form maps to IRIS+ data collection instructions. WALKRI conformance threshold maps to IRIS+ indicator application guidance.

A WALKRI-conformant field specification automatically satisfies IRIS+ indicator metadata requirements. Programs that declare IRIS+ Core Metrics Set alignment as their measurement framework will find that WALKRI-conformant fields within that program carry IRIS+ metadata without additional work. When referencing a specific IRIS+ indicator, programs should use the IRIS+ indicator identifier type defined in Part VI Section 6.2.

### 10.2 OECD DAC Criteria (DCD/DAC(2019)58/FINAL)

The six OECD DAC evaluation criteria (Relevance, Coherence, Effectiveness, Efficiency, Impact, Sustainability) each require different evidence types to assess. WALKRI's evidence form taxonomy (Section 3.4) directly addresses the DAC requirement that evaluation criteria be supported by specified evidence rather than undifferentiated narrative.

Relevance evaluations require standing evidence (does the organization have credible positioning in this domain?) and planning evidence (is the intervention aligned with the population's needs?). Effectiveness and Efficiency evaluations require activity evidence and outcome evidence. Impact evaluations require outcome evidence with a named methodology and an independent verifier. Sustainability evaluations require planning evidence and financial accountability evidence demonstrating post-grant continuation capacity.

Programs conducting DAC-aligned evaluations that use WALKRI-conformant intake fields will find that the evidence type specification in their fields maps directly onto the evidence requirements for each DAC criterion.

### 10.3 Humanitarian Sector Standards (Sphere, JMP, WASH Cluster)

Programs operating in humanitarian or development contexts frequently receive evidence in the form of institutional attestations from UN bodies, INGOs, or sector coordination clusters. WALKRI's standing evidence type (Section 3.4) is designed for this context.

The Sphere Standards (humanitarian response minimum standards), JMP (WHO-UNICEF Joint Monitoring Programme for water and sanitation), and WASH Cluster guidelines each specify evidence requirements for humanitarian outcome claims. Programs that accept evidence from applicants operating in these contexts should specify standing evidence requirements that name the recognized sector bodies whose attestations are accepted, the scope those attestations must cover, and the currency window. An attestation from an FAO regional representative attests to programme participation in an FAO innovation initiative; it does not attest to water quality outcomes. The evidence form conformance threshold must state this distinction explicitly so reviewers apply it consistently.

### 10.4 Grant Maturity Index (Biedermann and Gibrel, Metagov, arXiv:2410.19828)

The GMI evaluates grant programs across four dimensions: governance, transparency, operational efficiency, and community engagement. WALKRI directly advances two of these dimensions.

Transparency: WALKRI requires that field specifications be published before any applicant sees the field. This makes the funder's measurement intent and evidence requirements visible before the round opens, rather than being reconstructed after the fact from reviewer decisions.

Operational efficiency: WALKRI-conformant programs produce consistently structured data that does not require definitional cleanup before analysis. The field specification is the data contract; data collected under it is comparable across the cohort by construction.

The participatory specification element (Section 3.6) directly addresses the community engagement dimension: programs that document participatory specification provide structured evidence of community involvement in measurement instrument design.

### 10.5 DAOIP-5 and the Metagov Grants Ecosystem

WALKRI-enriched field specifications map to DAOIP-5 Project object metadata (see Part II Section 2.3). Programs operating within the Metagov grants ecosystem or exporting to the OpenGrants Gateway API can express their WALKRI-conformant field definitions within DAOIP-5 Project objects using the `x-walkri` extension namespace. WALKRI conformance records are cryptographically attributed, publicly verifiable records; the specific format used (W3C Verifiable Credentials, EAS attestations, DAOIP-3 VCs for programs operating within the DAOIP ecosystem, signed audit documents, or comparable mechanisms) is determined by the program's institutional context, as specified in Part I Section 1.4.

The practical effect: a WALKRI-certified program's field quality is machine-readable by DAOIP-5-aware systems, enabling cross-ecosystem analysis not only of what was reported but of how reliably the reporting instruments were designed.

### 10.6 USAID Data Quality Standards (ADS 201 and Performance Management and Evaluation Policy, 2016)

USAID's data quality standards for performance indicators, codified in ADS 201 and the Performance Management and Evaluation Policy (2016), specify five data quality criteria that all USAID performance indicators must satisfy: validity, reliability, precision, integrity, and timeliness. These five criteria are structurally identical to WALKRI's five data quality standards (Part V of this document), named consistently with the underlying measurement quality principles each standard encodes.

The correspondence is direct. USAID Validity = WALKRI Validity (5.1): the data actually measure what they are intended to measure. USAID Reliability = WALKRI Reliability (5.4): the data collection process is consistent across periods and collectors. USAID Precision = WALKRI Precision (5.3): the measurement instrument can detect differences of the magnitude relevant to the decision. USAID Integrity = WALKRI Integrity (5.2): evidence collection is separated from the entity that benefits from favorable outcomes. USAID Timeliness = WALKRI Timeliness (5.5): data are available in time to inform decisions.

The consequence: a WALKRI-conformant field specification automatically satisfies USAID data quality standards for performance indicators. The five WALKRI standards are not derived from USAID's framework; they encode the same underlying measurement quality principles. The correspondence is therefore exact rather than approximate. Programs reporting to USAID that implement WALKRI-conformant intake fields satisfy the PIRS data quality assessment requirement as a structural consequence of conformance, because the quality is built into the instrument design rather than assessed retrospectively after data collection.

The full mapping, including the complementary CROSS eleven-field indicator specification mapping to PIRS required elements, is documented in the published USAID-PIRS-CROSS-WALKRI compatibility statement (CC0).

### 10.7 Gates Foundation Open Access Policy (January 2025)

The Gates Foundation Open Access Policy requires grantees to publish a Data Availability Statement at the time of publication specifying where primary data, metadata, software, and replication materials can be found. For grants exceeding $500,000 in global health funding, a Data Access Plan must be prepared before activities begin. The policy explicitly invokes FAIR principles and requires data to be "as open as possible."

WALKRI's evidence form requirement, applied at the field specification stage, produces the structural content of both documents. Every WALKRI-conformant field specifies its artifact type and access path before any applicant sees the form; across all fields in a conformant form, these evidence form specifications constitute a Data Availability Statement. WALKRI's three-stage process (ideation, specification, audit), completed before the form is published, produces a Data Access Plan as a structural byproduct of correctly specifying the form. WALKRI satisfies FAIR by construction (Section 7.3). A program that has run WALKRI audit before opening its round has satisfied the Gates Policy's data management requirements at the field design level. The full mapping is in the Gates-Open-Access-WALKRI compatibility statement (CC0).

### 10.8 Research Funder Data Management Plan Standards

Four major research funders require a Data Management Plan (DMP) specifying data types, metadata standards, repositories, access paths, and sharing timelines before research begins or at application stage. All four invoke FAIR principles and require that data be publicly shared at the time of publication.

**NIH Data Management and Sharing Policy** (effective January 2023, strengthened 2025): required for all NIH grant applications generating scientific data. A two-page DMP must specify data types, metadata standards, data format, repository, access considerations, and sharing timeline.

**NSF Data Management Plan Requirements** (updated NSF-26-202): required two-page DMP for all NSF grant proposals. As of January 2025, data supporting NSF-funded publications must be publicly shared at time of publication.

**Horizon Europe Open Science Requirements**: DMP submitted within six months of grant signature and updated at midpoint and project end. Must address FAIR conformance, preferred repository, and metadata standards.

**Wellcome Trust Data and Materials Policy** (updated January 2025): outputs management plan required at application stage, before research begins. FAIR conformance required. Only fully open-access publishing funded from January 2025.

WALKRI's five criterion specification requirements produce DMP content as a structural byproduct. Criterion intent documents the data type being collected. Operational definition documents the metadata standard and counting rule. Response form justification documents the data format and the rationale for its selection. Evidence form documents the repository and access path. Conformance threshold documents any external classification or vocabulary standard the field references. A program that has run WALKRI audit before publishing its form has produced the core DMP content before any applicant submits data.

WALKRI's pre-publication timing aligns most exactly with Wellcome's application-stage requirement. For the NIH, NSF, and Horizon Europe requirements, the WALKRI audit completed before the round opens satisfies the "before data collection begins" requirement. The full mapping covering all four frameworks is in the Research-Funder-DMP-Standards-WALKRI compatibility statement (CC0).

### 10.9 Core Humanitarian Standard on Quality and Accountability (2024 Edition)

The Core Humanitarian Standard (CHS 2024) is the foundational accountability framework for UN agencies, ICRC, and humanitarian NGOs, with nine commitments covering accountability to affected people, quality of assistance, and ethical resource management.

Commitment 7 (support is continually adapted based on feedback and learning) requires that measurement instruments be designed to detect the conditions that signal when adaptation is needed. WALKRI's criterion intent requirement, which requires every field to state what it measures, is the structural precondition for Commitment 7 data to be actionable: data collected without a stated measurement intent cannot reliably trigger adaptation because reviewers cannot agree on what a given response means. WALKRI-conformant fields produce structured, defined, comparable data that can be systematically reviewed and acted upon across reporting periods.

Commitment 9 (resources are managed responsibly and ethically) requires that evidence of resource use not be self-assessed by the benefiting party. WALKRI's integrity requirement (Section 5.2) operationalizes this at the field level: the evidence form must identify an independent access path that structurally separates evidence collection from the entity that benefits from favorable assessment.

### 10.10 Open Source Observer oss-directory

Open Source Observer (docs.opensource.observer) maintains the oss-directory schema (v7) as the primary registry for open source project identity in the Web3 ecosystem. The schema requires or supports fields for project name and display name, GitHub organization URLs, npm packages, and blockchain addresses with network and tag annotations.

WALKRI recipient profile fields map directly to these oss-directory fields. The organizational name maps to display_name. The on-chain identity anchor (inherited from CROSS Field 6 when CROSS and WALKRI are used together) maps to the blockchain address and network fields. GitHub repository URLs specified in evidence form requirements for code-related fields map to the github artifact array. npm package identifiers, where specified as evidence artifacts, map to the npm artifact array.

A WALKRI-conformant recipient profile that includes these fields is directly importable as an OSO oss-directory entry, reducing duplicate registration burden for grantees. OSO metrics (commit activity, contributor count, on-chain transaction data) are compatible evidence sources for WALKRI evidence form specifications in programs where these verifiable signals serve as gate criteria. The full mapping is in the OSO-WALKRI compatibility statement (CC0).

### 10.11 SROI and Social Value International Principles

Social Return on Investment (SROI) methodology uses seven principles (Social Value International): Involve stakeholders, Understand what changes, Value the things that matter, Only include what is material, Do not over-claim, Be transparent, Verify the result. SROI is used by development organizations, impact investors, corporate ESG programs, and nonprofit grant programs to account for social value.

WALKRI addresses five of the seven principles structurally through its field specification requirements. Principle 2 (understand what changes): WALKRI's criterion intent requirement requires that every field state what it measures before any applicant sees it, which is the operational expression of "understand what changes" at the instrument design level. Principle 4 (only include what is material): WALKRI's operational definition requirement specifies qualifying and non-qualifying examples, implementing materiality at the field level by constraining what counts as a valid response. Principle 5 (do not over-claim): WALKRI's conformance threshold requirement, combined with CROSS's causality stance field, prevents overclaiming by requiring that claims be bounded by specified evidence and an explicit attribution stance. Principle 6 (be transparent): WALKRI's pre-publication audit and conformance record satisfy the transparency principle at the specification layer; the field specification is published before any applicant responds, making measurement intent visible. Principle 7 (verify the result): WALKRI's evidence form requirement specifies an independent access path for every claimed measurement, structurally satisfying the verification principle by separating evidence from beneficiary self-report.

Principles 1 (involve stakeholders) and 3 (value the things that matter, including monetization) involve program-level design and affected-party engagement that WALKRI does not specify; these remain the responsibility of the program operator. The full mapping is in the SROI-WALKRI compatibility statement (CC0).

### 10.12 AEA / JCSEE Program Evaluation Standards: Accuracy Property

The Joint Committee on Standards for Educational Evaluation's Program Evaluation Standards (third edition, 2011), endorsed by the American Evaluation Association and the Canadian Evaluation Society, organize evaluation quality into five properties: Utility, Feasibility, Propriety, Accuracy, and Evaluation Accountability. The Accuracy property has the most direct bearing on data collection instruments: it requires that measurement procedures be described with sufficient precision to allow replication, that information-gathering methods be defensible, and that claims be warranted by the evidence collected.

WALKRI's five pre-publication field requirements implement the Accuracy property at the source. Before any applicant sees a form, every field must specify what it measures (criterion intent), how it defines valid responses (operational definition), why the response type is appropriate (response form justification), what evidence is required (evidence form), and what threshold constitutes passage (conformance threshold). These five requirements correspond to the Accuracy standards' requirements for precision, defensibility, and replicability. A WALKRI-conformant field specification is a replicable measurement instrument in the sense the Accuracy standards require: two practitioners working from the same specification would collect comparable data. The full mapping, including the alignment of WALKRI's other field requirements with the Utility, Feasibility, Propriety, and Evaluation Accountability properties, is in the AEA-Program-Evaluation-Standards-CROSS-WALKRI compatibility statement (CC0).

### 10.13 Equitable Evaluation Initiative: Pre-Publication Participation Principle

The Equitable Evaluation Initiative's Equitable Evaluation Framework (EEF; equitableeval.org), co-developed with philanthropy, nonprofit, and evaluation partners from 2017, challenges conventional assumptions about what counts as evidence, who defines success, and how evaluation findings are used. The framework argues that traditional evaluation practice can replicate structural inequities when data collection instruments are designed without community input.

WALKRI's pre-publication audit requirement is the structural implementation of the EEF's core participation principle. By requiring that what each field measures be specified before any applicant sees the form, WALKRI creates the necessary structural pause during which program operators can incorporate community input into evidence design. Without WALKRI's pre-publication stage, evidence design defaults to evaluator preferences determined during or after data collection. Programs that implement the EEF's participation principle can use the WALKRI pre-publication audit window to document community co-design of intake field specifications. The full mapping is in the Equitable-Evaluation-Initiative-CROSS-WALKRI compatibility statement (CC0).

### 10.14 INPAS: International Non-Profit Accounting Standard

The International Non-Profit Accounting Standard (INPAS), launched in October 2025 through an initiative led by Humentum and CIPFA with stewardship by the International Non-Profit Reporting Foundation (INPRF), is the first global accounting standard specifically designed for nonprofit organizations. INPAS covers recognition, measurement, presentation, and disclosure requirements for nonprofit financial reporting, including specific guidance on grant income recognition, restricted versus unrestricted fund presentation, and a Practice Guide for harmonized grant reporting.

WALKRI addresses INPAS requirements at the intake specification layer. INPAS requires that grants be classified by restriction status at recognition, with restriction purpose, period, and evidence documented at the time of recognition. A WALKRI-conformant intake field collecting restricted fund documentation must specify, before any applicant sees the form, what counts as a restricted grant, what evidence of restriction status is required, and what the conformance threshold is for the restriction classification. This is the operational translation of INPAS's grant income recognition requirements into field design requirements. Programs that must produce INPAS-conformant financial reports from their intake data can use WALKRI-conformant field specifications for the restriction status, purpose documentation, and period specification fields that INPAS requires for each grant record. The full mapping is in the INPAS-CROSS-WALKRI compatibility statement (CC0).

---

## Part XI: Inheritance and Position in the Standards Architecture

WALKRI declares its own position in the standards architecture. A standard that conforms to upstream standards without declaring which ones, and in what role, leaves its inheritance illegible. This Part is WALKRI's self-contained statement of what it inherits, how it composes with the standards around it, and why each of its five requirements exists.

### 11.1 Position: A From-Below Instrument-Quality Standard

WALKRI is a domain-general standard for the quality of an instrument at the point of data capture. It stands in two distinct relationships to the standards around it, and the two must not be fused.

The first is inheritance, and it is from the root, not from CRAFT: WALKRI's content descends from the Coordination Structural Integrity Suite, whose root is the Precision-First Design Standard. Its relation to CRAFT's instrument-facing conditions is conformance, WALKRI satisfies them (see 11.2), not inheritance. WALKRI is not a domain application of CRAFT: a domain application (CROSS is the grants one) inherits CRAFT's full chain-framing conditions and adds domain-specific requirements, whereas WALKRI satisfies only the conditions that bear on whether a single captured datum is legible, knowable, and reliable. Where it stands, WALKRI is a sibling of the domain applications under CRAFT, not one of them. That it is not a domain application is its designed role, not a gap.

The second relationship is composition. A domain application composes with WALKRI: the domain standard sets the gates a submission must pass, and WALKRI sets what each instrument inside those gates must satisfy for the data the gate reads to be sound. This is the rigor sandwich, stated as domain-in-the-middle: CRAFT's construction grammar and six conditions set what the domain's chain must satisfy; the domain standard sits in the middle as the gates; WALKRI holds the instrument quality inside each gate. The domain conforms to both at once and communicates its precision in both directions, up to CRAFT in the construction of its chain and down to WALKRI in the definition of its capture points. The dependency runs one way: a domain application references WALKRI, and WALKRI never references a domain application. WALKRI is portable and independently operable through its Part II interfaces, and the composition position engages only when a program composes WALKRI with a chain standard.

These two relationships answer different questions and neither substitutes for the other. The composition relationship is not transclusion. Transclusion in WALKRI concerns only its internal unit (Part I): the form field is one named instantiation of the general instrument, not a stripped-down version of any domain's fields. The composition relationship concerns how a domain application and WALKRI work together. Conflating the two produces the error of saying a domain application transcludes WALKRI, which it does not; it composes with it.

The canonical statement of how CRAFT, CROSS, and WALKRI relate, including the rigor sandwich as a named element, is the interaction-architecture document (`craft-csis-frame-language-walkri-interaction-architecture-0_1_0.md`). This Part declares WALKRI's own position and points there for the cross-standard picture.

### 11.2 Upstream Inheritance Receipt

This receipt declares WALKRI's inheritance from each upstream standard, with every non-conformance labeled as either out of scope (inappropriate to an artifact-quality standard's nature) or appropriate and not yet implemented (a gap to close). Conflating the two would let scope hide real gaps.

Spine: the Precision-First Design Standard, floor direction. WALKRI is the field-definition-level instantiation of the precision-deficit floor; it implements the operational-definition requirement, design-time adoption, the normative-substitution diagnosis, and discretion-point specification. Self-application, previously a named gap, is now closed by an examination of WALKRI's own specification against CRAFT's six conditions. WALKRI's specification is itself a CRAFT-conformant evaluation chain: it satisfies the ontology, instrument, pre-specified-criteria, and decision-logic conditions strongly (its criterion elements are its ontology, its audit and rubric are its instruments, its conformance thresholds are its pre-specified criteria, and its pass-fail-override logic is its decision logic); its ideation stage (Section 4.1) supplies the decision-context condition; and it is single-loop on the feedback condition (its versioning and re-audit, Section 8.2, without loop-depth propagation), which is the same instrument-level-falsifiability gap named below rather than a separate deficiency. So WALKRI is not exempt from the scrutiny it imposes. This is the CRAFT-validates-WALKRI half of the CRAFT-WALKRI mutual-validation loop stated in the interaction-architecture document. Named not-yet-implemented gaps remaining: the precision-imposition ceiling and instrument-level falsifiability.

CRAFT, instrument-facing conditions, satisfied rather than inherited, the one conformance relationship in this receipt: WALKRI satisfies Condition 3 (valid measurement instruments) and Condition 4 (pre-specified criteria) strongly, and Condition 2 (construct definition) on the operational-definition side, with the construct-to-estimand adequacy statement a named gap. This entry is conformance, not content inheritance: WALKRI's content descends from the Precision-First spine and the mediated inheritances above, not from CRAFT, so WALKRI meets CRAFT's instrument-facing conditions rather than drawing its requirements from them. The standalone test confirms it, since WALKRI states each of its requirements with no CRAFT in existence, because it is portable; the verb is satisfies, never inherits. WALKRI is displaced on Condition 1, relocating the decision-context requirement to the program that uses it through the ideation stage and carrying none for itself; out of scope on Condition 5 (decision logic, downstream of capture); and single-loop only on Condition 6 (versioning and re-audit, without loop-depth propagation, which is the instrument-level falsifiability gap). By CRAFT's own construction grammar WALKRI carries no construction-grammar declaration and is therefore a chain-quality standard, not a CRAFT domain application. This is the placement, not a deficiency.

Scoped strong inheritance: the Sensemaking Standard, the Residue invariant and the Witness-Reception scale only. WALKRI's provenance and schema architecture implements these directly. The capacity, inter-personal, and liminal-phase requirements are out of scope where they concern the producing process rather than the artifact.

Mediated inheritances, each an instrument-layer slice that follows from making a field precise and legible before collection: the Information Asymmetry Classification Standard (Classes 3, 5, 6, and Extension Class C, at the instrument layer); the Structural Consent Legibility Standard (the legibility obligation at the field level); the Structural Power Obligation Standard (interpretive-power distribution through field specification); the Adverse-Signal Engagement Principle (the Notice-phase instrument requirements); the Coordination Scaling Standard (structural legibility).

Out of scope, with reason: the Regenerative Obligation Standard (return and extraction direction is a coordination-ethics concern orthogonal to a field-quality instrument; WALKRI makes extraction nameable through provenance and no more); the Four Batteries Capacity Standard (contributor capacity and depletion is an organizational-capacity concern, with the depletion-degrades-specification touchpoint carried in guidance); the Conflict Transformation Standard (dispute process and the human-operator role is a separate domain, carried as a compatibility statement).

The universal boundary across all of these: WALKRI guarantees the output, the well-formed instrument, not the process that produced it, not the operational phase after collection, and not how the standard itself is maintained. The single most consequential gap is that WALKRI carries response-level falsifiability (the conformance threshold) but not yet instrument-level falsifiability (a way to discover from collected data that the instrument specification itself was wrong); that gap is the named upgrade path, not a property the standard claims to have closed.

### 11.3 The Derivation Layer

Each of the five criterion specification requirements (Part III) secures a quality and descends from an upstream commitment. The requirement is the normative obligation, stated so it can be checked from the artifact; the quality is what the requirement secures; the descent names where the obligation comes from. This layer explains why each requirement exists. It is not itself a set of conformance checks: the qualities are predicates that cannot all be read off the artifact alone, and making them into requirements would commit the normative-substitution failure the Precision-First Design Standard forbids. The five criterion elements are the conformant normative layer; the qualities below are what they are for.

- Criterion intent secures validity: a documented logical chain from the evidence to the measurement claim, and a measurement claim legible to one reader distinct from the label. It descends from the Precision-First operational-definition requirement applied to the measurement claim.
- Operational definition secures reliability: two readers resolve the same response the same way. It descends from the Precision-First operational-definition requirement applied to each response category.
- Response form secures precision: the response type resolves differences at the magnitude the decision requires. It descends from the Precision-First requirement that an instrument be capable of the resolution its decision needs.
- Evidence form secures integrity and verifiability: a claim has an independent verification path that separates evidence from the party who benefits from a favorable outcome. It descends from the Information Asymmetry Classification Standard and the Structural Power Obligation Standard at the instrument layer.
- Conformance threshold secures response-level falsifiability: a response can be shown to pass or fail against a pre-declared bar. It descends from the Precision-First falsifiability and pre-specification discipline, which CRAFT Condition 4 also instantiates; it converges with Condition 4 rather than deriving from it, confirmed by the standalone test that WALKRI carries the conformance threshold with no CRAFT present.

The five base quality dimensions explored in the parked per-axis architecture (construct validity, falsifiability, legibility, navigability, coupling-readiness) are the qualities this layer names, not a second set of requirements. Coupling-readiness in particular is configuration-level content, secured by the instrument dependency declaration (Section 3.9), not a per-instrument predicate.

---

## Part XII: Companion Documents

WALKRI v0.1.0 is accompanied by six companion documents.

**WALKRI-guidance-0_1_0.md** provides practitioners with guidance on traversing the three-stage process. It contains worked examples of ideation records, field specifications, and applicant guidance documents for common field types.

**WALKRI-templates-0_1_0.md** provides structured templates for each artifact produced by the three-stage process: the ideation record template, the field specification template, and the applicant guidance document template. Templates are provided in JSON Schema format and in a human-readable structured form.

**WALKRI-rubric-0_1_0.md** provides the scoring rubric used by the WALKRI Audit Tool. It operationalizes each of the five criterion specification requirements as an auditable criterion with pass/fail/override conditions. Practitioners and auditors use it to understand how the Audit Tool arrives at its assessments and to conduct manual audits when the tool is unavailable.

**WALKRI-worked-examples-0_1_0.md** provides full worked examples of WALKRI-conformant and non-conformant fields for six common field types: single-select categorical, multi-select, binary (yes/no), numeric with counting rule, URL with evidence specification, and qualitative narrative. Each example includes the non-conformant version, the diagnosis based on Part III's failure modes, and the conformant, revised version.

**WALKRI-interface-specification-0_1_0.md** provides the detailed technical specifications for the three interfaces described in Part II, including the JSON Schema mapping, the REDCap and XLSForm compatibility mappings, and the detailed alignments with Croissant, FAIR, and W3C PROV.

**WALKRI-CROSS-boundary-0_1_0.md** is retired. It described the CROSS-WALKRI relationship as a division of authority, a framing superseded by composition (the rigor sandwich). The relationship is now specified in the interaction-architecture document (the canonical cross-standard statement), in Part XI of this standard (WALKRI's own position), and in CROSS Part I and the CROSS inheritance receipt (CROSS's own position). The file is retained as a tombstone pointing to those.

**WALKRI-runbooks-0_1_0.md** provides pre-audited field specification packages for common program contexts. Each runbook is a deployable set of WALKRI-conformant field definitions that a program can adopt as a starting configuration and modify. Six runbooks correspond directly to the six CROSS runbooks; three further runbooks address institutional framework requirements (USAID PIRS, OECD DAC, DPG Standard). Runbooks are the primary mechanism for lowering the barrier to WALKRI conformance: programs start with a runbook, review and modify fields for their specific context, and produce a conformant field set without building from the full specification.

---

## Appendix A: Open Design Questions (v0.1.0)

The following questions are genuine open design problems as of v0.1.0. They are recorded here because the correct answer has not yet been settled. The stakes for each question are stated alongside the question.

**Question 1: Tiered minimum conformance threshold.** The current specification requires all five criterion specification elements at Stage 2 certification. A plausible alternative is a tiered minimum: criterion intent and evidence form are required at Stage 1 (ideation audit), and all five elements are required at Stage 2 (publication certification). The rationale for the tier is that Stage 1 is an internal design document, and imposing full specification requirements at that stage may slow down ideation in ways that reduce the quality of the ideation record rather than improving it. The risk is that organizations treat Stage 1 certification as sufficient and never complete Stage 2, resulting in fields that are only partially specified and receiving credit for a partial pass. The requirement for empirical evidence on how organizations actually use the tiered process.

**Question 2: Qualitative and narrative fields.** The five criterion specification requirements were designed primarily for categorical, binary, and quantitative fields. Open-ended narrative fields resist operational definition in the same way: the construct they measure is often inherently multidimensional, and the value of the field is precisely its openness to unanticipated content. Requiring a detailed operational definition for a narrative field may produce a constrained field that defeats the purpose of asking an open question. The design question is whether WALKRI should specify a distinct specification pathway for inherently qualitative fields, or interpret the existing requirements more flexibly in these cases. The risk of flexibility is that it becomes a loophole through which underspecified fields are classified as "inherently qualitative" to avoid the work of specification.

**Question 3: Public vs. private certification registry.** This version of the standard does not specify whether the conformance record produced at certification must be publicly available or may be held privately by the certifying organization. A public registry would allow downstream data consumers to verify certification status independently, which improves the downstream interface described in Part II. It would also create a record of override patterns across the ecosystem, which could improve the standard over time. A private certification model reduces the burden on certifying organizations (who may have proprietary form designs they do not want to publish) and may improve adoption. The question has no single definitive answer; it depends on the ecosystem's trust model in which WALKRI is deployed.

**Question 4: AI-generated field specifications.** The three-stage process described in Part IV is designed for human question-holders assisted by AI tools. A foreseeable use case is AI systems that generate field specifications directly, bypassing Stage 1 (because the AI constructs the ideation record) and Stage 3 (because the AI generates applicant guidance automatically). The design question is whether AI-generated specifications should be treated identically to human-generated specifications for certification purposes, or require a distinct audit pathway that addresses failure modes specific to AI generation (e.g., specifications that are syntactically complete but semantically misaligned with the question-holder's actual intent). This question will become more pressing as AI-assisted form design becomes the norm rather than the exception.

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 0.2.1 | 2026-08-20 | Coherence-pass corrections and the CRAFT-WALKRI mutual loop. Part XI's CRAFT relationship corrected from selective inheritance to conformance: a 2026-06-02 examination finding that WALKRI *satisfies* CRAFT's instrument-facing conditions had been slid into an *inherits* claim and propagated across three documents; WALKRI's content descends from Precision-First, and its relation to CRAFT's instrument-facing Conditions 2, 3, 4 is conformance, not inheritance, with the standalone test carried as the discriminator (Part XI.1, XI.2, XI.3, plus the matching correction in the interaction-architecture and abstraction-layer documents). Self-application closed: WALKRI's own specification is declared a CRAFT-conformant evaluation chain (Part XI.2), which is the CRAFT-validates-WALKRI half of the restored CRAFT-WALKRI mutual-validation loop; the WALKRI-validates-CRAFT-decomposition half is stated in the interaction-architecture document. No change to the five criterion specification requirements or the Part V data-quality standards. |
| 0.2.0 | 2026-06-13 | WALKRI reconception landed. The unit of specification is now the instrument, with a form field, prompt constraint, structured-output schema element, rubric item, and extraction specification as named instantiations in different modalities (Part I, Part III head); the form field is one instantiation rather than the definition. Instrument dependency declaration added as Section 3.9 (derive-and-attest): a form's dependency graph is derived mechanically from the instrument set's own formal logic, attested, and carried in the conformance record, closing the soundness hole where a certified form could contain conditional logic the certification never assessed; independent instruments use the Declared-Absent convention. New Part XI (Inheritance and Position) declares WALKRI's self-contained upstream inheritance receipt (Precision-First Design Standard spine, selective inheritance of CRAFT's instrument-facing conditions, the mediated and out-of-scope statuses), the composition position (the rigor sandwich, domain-in-the-middle, one-way dependency), the transclusion-versus-composition distinction, and the derivation layer pairing each criterion element with the quality it secures and its upstream descent. The downward interface is named in Stage 1 ideation (Section 4.1) and upward recomposition in the conformance record (Section 8.3), the two halves of the composition relationship. The per-axis quality tensor reconception is parked as a candidate architecture, its detections honored by the instrument-as-unit and dependency-declaration moves, reopening only on AI and machine-learning evidence that the unit of specification there is the graph rather than the node. The filename stem 0_1_0 is retained as the WALKRI suite's stable series identifier; the internal version is authoritative. Instrument-level falsifiability and the upward-CRAFT candidates are held for their own session. |
| 0.1.9 | 2026-06-08 | Disbursement-authority instrument (Section 3.8): the Governed state is renamed Collective, completing the Governed-to-Collective disbursement-state rename across the suite (the set is now individual, collective, delegated). The Frame Language own-voice alignment was re-verified clean (em-dash and watchlist), and the document version stamp in the heading, which had lagged at 0.1.6, is corrected to match the frontmatter. No primitive, gate, or requirement changed; vocabulary and naming only. |
| 0.1.8 | 2026-06-03 | Acronym expansion corrected in three locations (frontmatter title, document heading, Part I body sentence): "Working Architecture for Legible, Knowledge-Ready Intake" replaced with "Working Architecture for Legible, Knowable, Reliable Instrumentation". No structural or normative content changed. |
| 0.1.7 | 2026-05-23 | Primitive rename cascade applied. Section 3.8: the Governance Resilience instrument is now the Continuity Capacity instrument; the three-state vocabulary (Single, Partial, Resilient) and all field requirements are preserved. Preamble reference list updated to the new primitive name. Historical changelog entries below retain prior primitive names as they stood at the time of release. |
| 0.1.6 | 2026-05-18 | Part X expanded: Section 10.11 SROI and Social Value International Principles added. Documents structural alignment between WALKRI's five field specification requirements and SROI Principles 2, 4, 5, 6, and 7. Principles 1 and 3 (stakeholder involvement and monetization) are outside specification-layer scope and remain the program operator's responsibility. |
| 0.1.5 | 2026-05-18 | Part X expanded: four new institutional framework alignment sections added. Section 10.7: Gates Foundation Open Access Policy. Section 10.8: Research Funder Data Management Plan Standards covering NIH DMS Policy, NSF DMP Requirements, Horizon Europe Open Science, and Wellcome Trust Data and Materials Policy. Section 10.9: Core Humanitarian Standard on Quality and Accountability (2024 Edition). Section 10.10: Open Source Observer oss-directory. Each section documents how WALKRI's five criterion specification requirements satisfy the framework's data quality and management requirements, grounding the compatibility statements published alongside this standard. |
| 0.1.4 | 2026-05-18 | Section 3.8: Five CROSS entry gate declarations added as WALKRI instruments. Revenue architecture instrument (four-type single-select with evidence form for commercial types). Disbursement authority instrument (three-state with named key holders and evidence form). Governance resilience instrument (three-state with named primary contributor evidence). Obligation fulfillment record instrument (per-grant structured record with three fulfillment states; activates for returning applicants and prior-work-citing applicants). Development stage instrument (five-stage single-select with explanation and independent evidence fields). Self-reference consistency requirement applied to all five instruments. |
| 0.1.3 | 2026-05-18 | Part XII: WALKRI-runbooks-0_1_0.md added as companion document. Nine pre-audited field specification packages covering six CROSS-paired runbook contexts (Discovery Sprint, Staged Development, Community Allocation, Retroactive Impact, Graduated Evidence, Institutional Conformance) and three institutional framework runbooks (USAID PIRS, OECD DAC, DPG Standard). Runbooks are the primary mechanism for lowering the barrier to WALKRI adoption: programs select a runbook as a starting configuration and modify from there. |
| 0.1.2 | 2026-05-18 | Section 10.6: USAID Data Quality Standards added to Part X. WALKRI's five data quality standards (validity, integrity, precision, reliability, timeliness) are documented as structurally identical to USAID's five data quality criteria specified in ADS 201 and the Performance Management and Evaluation Policy (2016). A WALKRI-conformant field specification satisfies the PIRS data quality assessment requirement as a structural consequence of conformance. |
| 0.1.1 | 2026-05-16 | Section 3.7: Public record query added as a named evidence form for identity instruments. A criterion specification may designate a public record query (on-chain profile registry, funder-signed gate record database, organizational registration database, or cross-program grants database) as the verification pathway for any applicant identity field. The specification must name the registry and query, specify what a satisfactory result contains, and state the policy for queries that return no result. Section 10.5 (DAOIP-5 and the Metagov Grants Ecosystem): DAOIP-3 removed from prescriptive position; WALKRI conformance records are now described as cryptographically attributed publicly verifiable records with format determined by program context, consistent with Part I format agnosticism principle. |
| 0.1.0 | 2026-05-15 | Initial release. Five criterion specification requirements (Part III). Three-stage process: ideation, specification, calibration (Part IV). Four measurement quality standards: validity, integrity, reliability, timeliness (Part V). Comparative field quality tool (Part VI). Applicant identity fields as WALKRI instruments, three instrument types, self-reference consistency requirement (Section 3.7). Format agnosticism principle (Part I). JSON Schema as primary interface with REDCap and XLSForm as documented alternatives (Part II). Institutional framework alignments: IRIS+, OECD DAC, FAIR, Croissant, W3C PROV, IATI, DDI, Pluralistic Grants Framework (Part X). Companion documents: guidance, templates, rubric, worked examples, interface specification, CROSS-WALKRI boundary (Part XII). |
