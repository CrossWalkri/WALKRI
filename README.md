# WALKRI: Working Architecture for Legible, Knowable, Reliable Instrumentation

Version 0.1.9 | 2026-07-20 | CC0

**Two standards. One problem.**

Every intake form has questions. No standard has ever required those questions to function as measurement instruments before anyone answers them. WALKRI is the first.

![GIGO pipeline: obligation never specified and questions not designed to measure enter a funnel, producing data that cannot be compared, aggregated, or trusted. No existing tool touches the source.](assets/cross-walkri-gigo-problem.png)

A field that does not specify what it measures is a label. Labels produce responses. They do not produce data. The difference matters at every layer of the grants ecosystem: a reviewer cannot assess what was not defined, an analyst cannot aggregate what was not measured consistently, and a funder cannot verify what was never specified. WALKRI addresses this at the source, before any applicant sees the form.

WALKRI is a companion standard to CROSS (Common Reporting Outcome Standards Schema). Together they are published as CROSS+WALKRI. CROSS specifies the obligation architecture of a grants round: what grantees must demonstrate at each payment gate. WALKRI specifies the quality of the fields through which that demonstration is collected. The two are designed to be used together, but WALKRI is also portable: it works with any obligation standard, not only CROSS.

Across the 95+ frameworks documented in the CROSS+WALKRI compatibility corpus, a consistent pattern emerges: data quality problems in grant programs trace to specification decisions made before the first application was submitted. Form field design is where the obligation architecture meets the applicant. A round that correctly specifies what grantees must demonstrate produces nothing usable if the fields that collect that demonstration are labels rather than instruments. WALKRI addresses this at the surface where it is most consequential and most consistently neglected: the individual field, before anyone answers it.

Round design and form field design allocate decision standing. They determine who can legibly apply, what kinds of work get selected, whose theory of change is rewarded, and whether the data produced can ever be compared, aggregated, or trusted. A funder who treats these as administrative overhead is making decision-standing choices without acknowledging that decision-standing choices are being made. The field that does not specify what it measures is not neutral. It transfers interpretive power to whoever scores it, invisibly, after submission.

---

## The label problem

![Label vs measurement instrument: 'Is this project open source?' shown as a bare label on the left, and as a structured instrument with qualifying licenses, non-qualifying examples, and evidence requirements on the right. The same question. The difference is whether it measures anything.](assets/walkri-label-vs-instrument.png)

The same question can be a label or a measurement instrument depending on how it is specified. The difference determines whether the data it produces is trustworthy.

**Label version:** "Is this project open source?"

This question produces a yes/no response and nothing else. Two programs asking it will produce incomparable answers because "open source" means different things to different applicants. A reviewer cannot assess it consistently. An analyst cannot aggregate across it. An auditor cannot verify it.

**Instrument version:** "Does the primary codebase have a published OSI-approved license in the root directory of the public repository? Qualifying licenses: MIT, Apache 2.0, GPL, AGPL, MPL, or equivalent. Non-qualifying: 'available on request', 'will be open sourced post-launch', business source license. Evidence required: direct URL to the LICENSE file in a publicly accessible repository."

This version measures what the question claims to measure. A reviewer knows exactly what passes. An applicant knows exactly what evidence to provide. Two reviewers reach the same judgment from the same answer. The data is aggregatable across every program that specified the field correctly.

WALKRI applies this transformation to every intake field, for any question in any domain.

---

## What WALKRI specifies

Five requirements apply to every intake field before any applicant sees it.

**Criterion intent:** The field must specify what it measures, not just what it asks. The intent is a written statement, distinct from the label, that names the underlying construct being assessed.

**Operational definition:** The field must define the unit of measurement or the categories of valid response. For a quantitative field, this means the unit and scale. For a qualitative field, this means the qualifying and non-qualifying examples that constrain interpretation.

**Response form:** The field must specify the type of response required and provide a written justification for why that response type is appropriate for the criterion intent. A field asking for a URL when a narrative is needed is measuring the wrong thing in the wrong way.

**Evidence form:** The field must identify the specific artifact type and access path required to answer it. Not "evidence of open source status" but "a URL to the LICENSE file in the root directory of a publicly accessible repository." The evidence form structurally separates what counts as evidence from who benefits from favorable assessment.

**Conformance threshold:** For fields referencing external standards (a DPG Standard, ISO certification, a regulatory requirement), the field must enumerate which components of the standard apply and what minimum passage level constitutes conformance.

A field that satisfies all five is a measurement instrument. A field that fails any one is a label. The distinction is structural, not a matter of degree.

WALKRI also specifies five gate declaration instruments that apply at the program level, before individual fields are designed: the Obligation Mode Declaration, the Evidence Standard Declaration, the Comparison Frame Declaration, the Attribution Claim Declaration, and the Sufficiency Assessment Declaration. These establish the obligation context that field design must satisfy.

---

## What conformant fields produce

Field quality at the specification stage compounds upward through every layer of the grants ecosystem. Here is what each layer gains.

**Grantees** know exactly what a field requires before they write a word. The operational definition includes qualifying and non-qualifying examples. The conformance threshold states what passage looks like. Professional grant writers no longer have a structural advantage over subject matter experts, because the form itself carries the information previously available only to experienced applicants.

**Reviewers** get calibration built into the field rather than requiring separate calibration sessions. Two reviewers reading the same operational definition reach consistent judgments. Scoring variance is a structural consequence of underspecified fields; WALKRI eliminates the source rather than training reviewers to manage it. The conformance threshold makes reviewer disagreement a traceable discrepancy, not an irresolvable difference of opinion.

**Program operators** can audit their own fields before a round opens. A field flagged as a label by the WALKRI rubric can be specified correctly in hours. A label that went live and collected a round of responses cannot be fixed retroactively. The pre-publication audit is the only point in the process where this correction costs nothing.

**Analysts** get data that is structurally comparable across programs. Ten programs asking WALKRI-conformant versions of "is this open source?" produce data that aggregates directly. Ten programs asking label versions of the same question produce ten different constructs that look identical but are not. Portfolio analysis, cross-program benchmarking, and longitudinal tracking all depend on the conformant version.

**AI-assisted review** becomes criterion-referenced rather than pattern-matched. A language model assessing a response against a WALKRI-conformant field specification is working with defined criteria, qualifying examples, an evidence requirement, and a conformance threshold. Without WALKRI, AI review is inferring intent from a label. With it, AI review is applying a specification. The difference is not in the model; it is in whether the field gives the model something precise to assess against.

**Platform providers** gain ecosystem-wide data comparability from a single conformance requirement. Every program running on a WALKRI-conformant platform produces data that is structurally comparable to every other program, regardless of what the programs fund, how they select, or which indicators they use.

**Institutional funders** receive data quality as a structural output of the round being run correctly, not as a separate conformance exercise. USAID data quality criteria, OECD DAC evaluation standards, IRIS+ metadata requirements, and FAIR data principles are all satisfied as consequences of conformance. The same applies in the Web3 ecosystem: DAOIP-5-compatible grant data, EAS-attestable field specifications, and OpenGrants-compatible structured output are all products of the same conformant specification.

---

## Where WALKRI sits in the stack

![CROSS+WALKRI stack: any form builder or grants platform below, CROSS+WALKRI in the middle providing obligation architecture and field quality, Web3 and institutional standards above. One conformant round, both directions, no extra work.](assets/cross-walkri-compatibility-stack.png)

Form builders are the communication layer. Their product is how questions look, how flows work, how data exports. Fillout, Typeform, KoBoToolbox, REDCap, and comparable tools are excellent at this. None of them ask what a field measures before publishing it, because that is a measurement design question, not a form design question. They are not built around it and cannot be retrofitted to require it without changing their foundation.

WALKRI operates at the measurement design layer, which sits above the form builder and below the program's obligation architecture. It specifies what a field must contain before any form builder renders it. Because WALKRI operates on JSON Schema, which underlies every major form builder, a WALKRI-conformant field specification passes through any of those tools unchanged. Programs do not change their stack. They specify their fields correctly before the form goes live, and the form builder renders whatever is specified.

Above the field level, a CROSS+WALKRI-conformant round produces data that is structurally comparable across programs and auditable after the fact. That position in the stack is why compatibility is the primary benefit: it does not require replacing what exists below, and it makes everything built above interoperable with everything else built on the same foundation.

Both CROSS and WALKRI are published CC0. No licensing, no arrangements, no asks.

---

## The evidence path

WALKRI's other family is domain-agnostic. Every system that turns records into decisions has the same anatomy: sources feed in material the system did not create, fields capture that material as data, and a chain of evaluation carries it to a claim someone acts on. Knowing begins honestly, or begins broken, in three places, and one standard stands at each. [ORE](https://github.com/CrossWalkri/ORE) stands at the source boundary: what a chain is allowed to assume about what enters it, graded as uncertainty rather than judged as worth, with every output exposing the grade profile of the sources it rests on. WALKRI stands at the field: what a single capture point must carry before it counts as a measurement rather than a label. [CRAFT](https://github.com/CrossWalkri/craft-meta-standard) holds the whole path: the six conditions under which the claim at the end deserves anyone's trust, with CROSS as its first domain application, built for grants.

<p align="center">
<img alt="CRAFT is the meta-standard for an evaluation chain, drawn as a room whose six conditions (decision context, ontology, instruments, criteria set, decision logic, feedback) run its length from world to decision. ORE is the door in and STRUCK the door out, the two boundary standards CRAFT requires; WALKRI stands at the intake fields." src="assets/standards-family-0_1_0.svg" width="880">
</p>

<p align="center">
<img alt="ORE and STRUCK on their own: the two ends of any chain, independently adoptable, bracketing any process with or without CRAFT in the middle." src="assets/ore-struck-pair-0_1_0.svg" width="820">
</p>

One commitment runs through all three: no silent trust anywhere, and the worth-judgment left visible in the hands, human or automated, that make it. A record can fail at the source or at the field, and neither standard substitutes for the other; a chain can be flawless in every step and still stand on an unexamined feed, which is why the door and the gauge each get their own discipline. Each standard is independently adoptable; the through line is what they hold together.

---

## Who this is built for

![Cascade pyramid: Grantees and Reviewers at the base, Operators and Platform Providers, Analysts and Institutional Funders, Strategic Planners at the apex. Smaller decisions at the base; billions at stake at the top. Strategic level value requires ecosystem-wide adoption to materialise.](assets/cross-walkri-value-cascade.png)

WALKRI serves all six layers of the grants ecosystem without modification. The field quality it requires at the intake layer compounds upward: better specified fields produce better applicant responses, more consistent reviewer assessments, more defensible funding decisions, more trustworthy portfolio data, and eventually better strategic allocation decisions at the top of the stack.

The strategic planning benefit requires ecosystem-wide adoption to materialise. The base-layer benefits, for grantees and reviewers, are immediate from the first conformant round.

---

## Ecosystem position

| Tool / Standard | Layer | Obligation architecture | Field quality | Web3 output | Institutional output |
|:--|:--|:--|:--|:--|:--|
| **WALKRI** | Specification | n/a (see CROSS) | Five pre-publication field requirements | n/a | USAID DQA, FAIR, OECD DAC, IRIS+, Gates Open Access, NIH/NSF/Horizon/Wellcome DMP, SROI, PCORI, SAMHSA NOMs, HRSA UDS, WIOA, Head Start ELOF, and 90+ more |
| **CROSS** | Specification | Three modes, four-gate sequence | n/a (see WALKRI) | DAOIP-5, W3C VCs, OpenGrants, Optimism Retro Funding 2025 | OECD DAC, IRIS+, USAID PIRS, World Bank RF, UNDP IRRF, IMP Five Dimensions, 95+ frameworks |
| [USAID PIRS](https://2017-2020.usaid.gov/sites/default/files/documents/1861/Recommended_PIRS_for_USAID_indicators_0.pdf) | Compliance framework | n/a | Five data quality criteria (retrospective) | n/a | Required indicator documentation |
| [IRIS+](https://iris.thegiin.org/standards/) | Vocabulary | n/a | n/a | n/a | Indicator reference library |
| [Impact Management Norms](https://impactmanagementnorms.com) | Framework | n/a | n/a | n/a | Five Dimensions of Impact |
| [Gates Open Access Policy](https://openaccess.gatesfoundation.org) | Funder requirement | n/a | Data Availability Statement, FAIR | n/a | Data sharing and open access |
| [NIH/NSF/Horizon/Wellcome DMP Standards](https://oir.nih.gov/sourcebook/intramural-program-oversight/intramural-data-sharing/2023-nih-data-management-sharing-policy) | Research funder requirements | n/a | Data Management Plan content as structural output | n/a | Research data open access |
| [SROI / Social Value International](https://www.betterevaluation.org/methods-approaches/approaches/social-return-investment) | Impact methodology | n/a | Principles 2, 4, 5, 6, 7 (materiality, no over-claim, transparency, verification) | n/a | Social value accounting |
| [Core Humanitarian Standard (2024)](https://www.corehumanitarianstandard.org/the-standard) | Accountability framework | n/a | Commitment 9: evidence independence; Commitment 7: measurement precondition | n/a | Humanitarian accountability |
| [ISEAL Code of Good Practice](https://isealcode.org/) | Standards governance | n/a | Part 5 MEL requirements (indicator definition, systematic collection, public disclosure) | n/a | Sustainability standards credibility |
| [Logframe / LFA](https://www.oecd.org/en/topics/sub-issues/development-co-operation-evaluation-and-effectiveness/evaluation-criteria.html) | Methodology | ToC hierarchy only | n/a | n/a | OECD DAC (partial) |
| [KarmaGAP](https://docs.gap.karmahq.xyz/) | Post-funding tracking | n/a | n/a | EAS milestone attestations | n/a |
| [OSO oss-directory](https://docs.opensource.observer) | Impact measurement | n/a | n/a | On-chain and GitHub activity | n/a |
| [DAOIP-5](https://github.com/metagov/daostar/blob/main/DAOIPs/daoip-5.md) | Interoperability | n/a | n/a | Grants data portability | n/a |
| Form builders (Fillout, Typeform, KoBoToolbox, REDCap) | Collection layer | n/a | n/a | JSON Schema output | n/a |

Every tool either collects data after fields are defined, tracks outcomes after work is done, provides indicator vocabulary, or handles interoperability. None specify what makes a field a measurement instrument before it is published. WALKRI is the first standard that does.

---

## Institutional alignment

WALKRI's five requirements encode the same underlying measurement quality principles that dozens of institutional frameworks require, applied at specification time rather than assessed retrospectively. A WALKRI-conformant intake form produces data quality conformance across all of the following frameworks as a structural byproduct of correctly specifying its fields before publication.

**USAID data quality criteria** (Validity, Reliability, Precision, Integrity, Timeliness) map directly to WALKRI's five requirements. USAID applies these as a Data Quality Assessment procedure after data is collected. WALKRI applies them at the field specification stage, before any applicant sees the form. A WALKRI-conformant field satisfies the USAID DQA without a separate assessment.

| USAID criterion | WALKRI requirement | How WALKRI satisfies it |
|:--|:--|:--|
| Validity | Criterion intent + Operational definition | Written statement of what the field measures with qualifying and non-qualifying examples |
| Reliability | Operational definition + Conformance threshold | Precise definition constrains interpretation; calibration requirement ensures consistency across reviewers |
| Precision | Response form | Response type justified as appropriate for the criterion intent; determines measurement resolution |
| Integrity | Evidence form | Specifies artifact type and independent access path, separating evidence from beneficiary |
| Timeliness | Evidence form | Specifies recency requirement and time-period for evidence collection |

**FAIR data principles** (Findable, Accessible, Interoperable, Reusable) are satisfied as a consequence of WALKRI conformance. Conformant field specifications are machine-readable, linked to defined vocabularies, and structurally consistent across programs, making the data they produce FAIR without additional effort.

**OECD DAC evaluation criteria** require that evaluation questions be traceable to defined program logic. WALKRI-conformant fields are designed against the obligation architecture declared in CROSS, ensuring that the measurement surface is coherent with the causal theory being evaluated.

**IRIS+ metadata requirements** for indicator documentation are satisfied by the combination of WALKRI field specifications and CROSS indicator declarations. IRIS+-compatible indicator records are produced as structural outputs of a conformant round.

**Gates Foundation Open Access Policy** (January 2025) requires grantees to publish a Data Availability Statement specifying where primary data, metadata, software, and replication materials can be found, and for grants over $500,000 in global health to prepare a Data Access Plan before activities begin. WALKRI's evidence form requirement, applied at the field specification stage, produces the structural content of both documents: every field in a conformant form specifies its artifact type and access path before any applicant responds. The policy explicitly invokes FAIR principles, which WALKRI satisfies by construction.

**Open Source Observer (OSO)** maintains the oss-directory schema (v7) as the primary registry for open source project identity in the Web3 ecosystem. CROSS Field 6 (on-chain identity anchor) maps directly to the OSO blockchain address registration fields. A WALKRI-conformant recipient profile that includes the on-chain identity anchor, GitHub URL, and npm package identifiers is directly importable as an OSO oss-directory entry. OSO metrics (commit activity, contributor count, on-chain transaction data) are also the natural evidence source for CROSS gate tests in Build and Change obligation programs, providing independent, reproducible verification that does not rely on applicant self-reporting.

**Research funder data management standards** (NIH DMS Policy, NSF DMP Requirements, Horizon Europe Open Science, Wellcome Trust Data and Materials Policy) all require a Data Management Plan specifying data types, metadata standards, repositories, and access paths, prepared before data is collected or at application stage. WALKRI's five field specification requirements produce this DMP content as a structural byproduct: criterion intent documents data types, operational definition documents metadata standards and counting rules, response form justification documents data format, evidence form documents repository and access path, and conformance threshold documents any external classification or vocabulary standard. Programs running WALKRI audit before publishing their forms have produced a DMP before any applicant submits. Formal statement: `Research-Funder-DMP-Standards-WALKRI-compatibility-0_1_0.md`.

**SROI (Social Return on Investment) / Social Value International** seven principles require verification and transparency in impact claims. WALKRI's evidence form requirement, which specifies the artifact type and independent access path for every intake field, structurally satisfies the verification principle by separating evidence from beneficiary self-report.

**Core Humanitarian Standard (2024 revision)** Commitment 7 requires support to be continually adapted based on feedback and learning. WALKRI-conformant field specifications, because they declare what is being measured before collection, create the structural preconditions for Commitment 7 data to be comparable across rounds and adaptable based on what measurement surfaces.

Formal compatibility statements are in the `statements/` directory. See the CROSS README for the full cross-referenced compatibility index covering all international development, impact investing, research funding, open data, and Web3 standards.

---

## Documents

- `WALKRI-standard-0_1_0.md` - Main specification (current: v0.1.7)
- `WALKRI-interface-specification-0_1_0.md` - Three-interface specification (upward, lateral, downstream)
- `WALKRI-CROSS-boundary-0_1_0.md` - Formal boundary between WALKRI and CROSS
- `WALKRI-guidance-0_1_0.md` - Practitioner guidance including gate declaration instrument guidance
- `WALKRI-templates-0_1_0.md` - Field specification templates, worksheets, and gate declaration forms
- `WALKRI-rubric-0_1_0.md` - Audit and certification rubric with gate declaration assessment
- `WALKRI-worked-examples-0_1_0.md` - Worked examples from Epoch 12 and comparable programs

**Cross-standard documents (in root of cross-walkri repository)**

- `CROSS-WALKRI-audience-map-0_1_0.md` - Six-cohort audience guide: what each cohort gains from CROSS and WALKRI specifically
- `CROSS-WALKRI-primitives-framework-index-0_1_0.md` - Maps measurement primitives to 95+ framework exemplars; use for classifying new frameworks

**Program type bundles (bundles/ directory)**

Ten documents combining CROSS runbooks, WALKRI field specifications, and compatibility maps for specific grant program types: Web3/public goods, international development, research grants, community foundation, corporate CSR/impact, challenge prizes, participatory/equity, Islamic/endowment, European philanthropy, and fiscal sponsorship.

---

## AI tools

The CROSS+WALKRI tools repository publishes an MCP server that exposes WALKRI and CROSS as callable tools in Claude Code, Cursor, and any MCP-compatible AI assistant. Install once; the tools are then available in any conversation without copy-pasting prompts or standard text.

**Install:**

```bash
git clone https://github.com/CrossWalkri/tools ~/cross-walkri
```

Then add to your MCP client configuration (Claude Code: `~/.claude/settings.json`; Cursor: `.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "cross-walkri": {
      "command": "node",
      "args": ["/Users/yourname/cross-walkri/server.mjs"]
    }
  }
}
```

Replace the path with wherever you cloned the repository. No build step required.

**WALKRI tools available after install:**

- `walkri_audit_field` - audits a field specification against all five WALKRI requirements; returns a binary verdict (instrument or label), per-criterion gap analysis, and a prompt template for revising the field with a language model
- `walkri_generate_field` - generates a WALKRI-conformant field specification from a plain-language description of what the field should measure; returns a draft specification and a prompt template ready to pass to a language model

The CROSS tools (`cross_check_gate`, `cross_configure_round`, `cross_classify_framework`, `cross_audit_round`) are also included. See the CROSS README for details.

Source and full documentation: github.com/CrossWalkri/tools

---

## License

CC0: dedicated to the public domain under Creative Commons Zero v1.0 Universal. See `LICENSE` for the full dedication.

Any grants ecosystem can adopt WALKRI without adopting CROSS, the Coordination Structural Integrity Suite, or any other standard. The five field requirements and gate declaration instruments stand alone.

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 0.1.9 | 2026-07-20 | Evidence-path section added: places WALKRI in its domain-agnostic family (CRAFT holding the chain, ORE at the source boundary, WALKRI at the field), with the shared evidence-path figure and the through-line statement (no silent trust anywhere; the worth-judgment left visible in the hands, human or automated, that make it). Cross-links to the CRAFT and ORE repositories. No requirement changed. |
| 0.1.8 | 2026-06-13 | Frame Language own-voice vocabulary pass. Recasts: the rhetorical claim "Round design and form field design are governance ... making governance decisions" recast to "allocate decision standing ... making decision-standing choices", preserving the argument in Frame 2; own-voice "compliance" recast to "conformance" (the conformance-threshold sentence "constitutes conformance"; "not as a separate conformance exercise"; "produces data quality conformance across all of the following frameworks"); "the accountability context that field design must satisfy" recast to "the obligation context". Kept as admissible: "transparency" where it names an SROI principle and the SROI principles sentence (citation use of the source framework's term); "Accountability framework" (Core Humanitarian Standard) and the layer descriptors "Compliance framework" (USAID PIRS) and "Standards governance" (ISEAL) as contextual description of those external tools' own category, flagged for author review. No mapping-table cell, framework claim, conformance threshold, or field changed; vocabulary only. |
