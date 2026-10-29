---
title: "DevSecOps"
date: 2026-09-26T00:00:00+03:00
draft: false
description: "A structured collection of notes on DevSecOps and application security: how maturity models, secure development processes, supply chain controls, threat modeling and risk management fit together."
summary: "Reference notes on application security and DevSecOps: an overview of security frameworks, secure development lifecycle processes, supply chain protection, threat modeling methodologies, risk management and standards."
---

{{< toc >}}

## Overview

Frameworks covered in this note fall into five levels, from abstract to concrete:

- Maturity models — "where we are now and where to move"
    - SAMM, BSIMM, DSOMM, DAF
- Process frameworks / SDL — "how to build a secure development process"
    - MS SDL, NIST SSDF, BSA Framework, SAFECode
- Supply chain security — "integrity and provability of artifacts"
    - SLSA, OpenSSF Scorecard
- Approaches and practices — "how security is embedded into team work"
    - Paved Road + Guardrails, Shift Left
- Standards and checklists — "specific requirements and control lists"
    - ISO/IEC 27034, GOST R 56939-2024, OWASP ASVS, OWASP Top 10, CIS Controls, CWE Top 25


## Maturity models

Assess how mature the secure development processes are within an organization and provide a growth roadmap.

- **OWASP SAMM** — prescriptive, OWASP
    - Holistic AppSec: Governance → Design → Implementation → Verification → Operations (5 functions, 15 practices)
    - 3 maturity levels per practice
- **BSIMM** — descriptive, Synopsys (formerly Cigital)
    - Benchmarking: what other companies actually do (4 domains, 12 practices, 116+ activities)
    - 3 levels per activity
- **DSOMM** — prescriptive, OWASP
    - DevSecOps specifics: integrating security into DevOps pipelines (5 dimensions)
    - 4 levels
- **DAF** — prescriptive, Jet Security (Russia)
    - Combines BSIMM + SAMM + DSOMM + GOST 56939-2024, adapted to Russian realities
    - Includes mapping to other frameworks, FTE calculators, roadmap
    - Levels 0-4 (Basic → Advanced)

Key difference: SAMM says "what should be", BSIMM — "what others actually do", DSOMM focuses on DevOps practices, DAF tries to combine everything and add Russian context. [Source](https://habr.com/ru/companies/owasp/articles/817241/), [DAF repo](https://github.com/Jet-Security-Team/DevSecOps-Assessment-Framework)

## Process frameworks / SDL

Describe how to embed security into the software development lifecycle — from requirements to release and incident response.

### Microsoft SDL

- Original process framework that started the AppSec industry
- 7 components: 5 phases (Requirements → Design → Implementation → Verification → Release) + 2 cross-cutting (Training, Response)
- Includes:
    - Threat modeling ([STRIDE](#stride))
    - Safe deployment process (staged release through "rings")
    - Final Security Review before release
- [Source](https://learn.microsoft.com/en-us/compliance/assurance/assurance-microsoft-security-development-lifecycle), [Wikipedia](https://en.wikipedia.org/wiki/Microsoft_Security_Development_Lifecycle)

### NIST SSDF (SP 800-218)

- NIST recommendations, de facto standard for software supplied to US government customers
- 4 practice groups, 19 practices, 42 tasks
    - **PO** — Prepare the Organization (people, processes, tools)
    - **PS** — Protect the Software (defending code and builds from tampering)
    - **PW** — Produce Well-Secured Software (secure design, code, dependencies, testing)
    - **RV** — Respond to Vulnerabilities (vulnerability response)
- Methodology-agnostic — maps to any SDLC
- Version 1.1 plus supplement SP 800-218A for generative AI
- [Source](https://csrc.nist.gov/projects/ssdf)

### BSA Framework for Secure Software

- Risk-oriented, outcome-based framework from the Business Software Alliance
- 3 directions:
    - Secure Development
    - Security Capabilities
    - Secure Lifecycle Management
- Focused on providing a common language for suppliers, customers, and regulators

### SAFECode

- Set of foundational secure development practices from a non-profit association (Microsoft, Oracle, Adobe, etc.)
- Not a framework per se, but a source of best practices that SSDF and BSA build upon

### GOST R 56939-2024

- Russian standard "Development of secure software. General requirements"
- Used as a checklist for assessing processes, especially in the context of FSTEC
- DAF contains a mapping to this GOST

## Supply chain security

Protecting the software supply chain: build integrity, provability of origin, assessment of dependency risk.

### SLSA (Supply-chain Levels for Software Artifacts)

- Framework from OpenSSF (originally Google) that assesses the maturity of the artifact build process
- Levels:
    - **L0** — no guarantees, builds happen anywhere
    - **L1** — provenance exists (build metadata), but unsigned
    - **L2** — signed provenance, dedicated build infrastructure
    - **L3** — isolated ephemeral environments, signing secret protection, non-repudiation
- [Source](https://jfrog.com/learn/grc/slsa-framework/)

### OpenSSF Scorecard

- Automated tool: scans a GitHub repository and gives a 0-10 score across ~19 checks
- Critical — Branch Protection, Dangerous Workflows, Binary Artifacts, Pinned Dependencies, Token Permissions
- Quality — Code Review, SAST, Fuzzing, CI Tests, Signed Releases
- Maintenance — Maintained, Contributors, Security Policy, Vulnerabilities

### Additional tools

- **in-toto** — specification for supply chain attestations
- **Sigstore** — artifact signing infrastructure (cosign, rekor)
- **CycloneDX / SPDX** — SBOM (Software Bill of Materials) formats
- **GUAC** (Graph for Understanding Artifact Composition) — dependency graph analysis

Relationship: SLSA defines "what the build should be", Scorecard — "how good the repository itself is". Scorecard can be used as a gate when choosing dependencies.

### Containers

- [How to build a custom Java image](https://github.com/lebmax/java-custom-container) — best practices for building minimal and secure Java container images

## Approaches and practices

### Paved Road + Guardrails

- Concept popularized by Netflix and AWS
- Not a framework in the classic sense, but an approach to organizing DevSecOps
- **Paved Road** — "the asphalted road": a set of ready-made tools, templates, and CI/CD pipelines with built-in security. The developer follows it and gets security "out of the box"
- **Guardrails** — rails: automatic controls that prevent insecure actions (policy-as-code, admission controllers, SAST gate, secret scanning in pre-commit)
- **Principle:** security by default, not opt-in. It is easier for developers to follow the secure path than to bypass it
- **Mapping to other frameworks**
    - CISA Secure by Design = paved road as an operational definition
    - SLSA L2/L3 = one of the guardrail contracts
- [Source](https://www.secureworld.io/industry-news/security-guardrails-matter-appsec)

### Shift Left

- Basic principle: move security checks left in the lifecycle — the earlier a vulnerability is found, the cheaper it is to fix
- Not a standalone framework, but the philosophical foundation for all the others

## Standards and checklists

- **OWASP Top 10** (OWASP)
    - Top 10 web application risks. The de facto starting point
- **OWASP ASVS** (OWASP)
    - Detailed application security requirements: 3 levels (basic → standard → advanced), ~130-180 controls
    - Used for verification and pentesting

### OWASP ASVS (Application Security Verification Standard)

Open standard from OWASP — a detailed catalogue of security requirements and controls for verifying the security of web applications and APIs at the development and testing stages. Unlike [OWASP Top 10](#standards-and-checklists), which only names the most common risks, ASVS provides a granular checklist of verifiable requirements that an application "must meet".

- **Purpose** — to serve as:
    - A checklist for developers and architects when designing secure-by-default applications
    - A basis for security code review, pentesting, and acceptance testing
    - A reference for procurement and contracts (the customer can demand "ASVS Level 2 compliance")
    - A baseline for secure CI/CD pipelines (requirements can be turned into automated tests)
- **Structure** — the standard is divided into functional chapters, each containing numbered requirements:
    - **V1** Architecture and Design
    - **V2** Authentication
    - **V3** Session Management
    - **V4** Access Control
    - **V5** Validation, Sanitization and Encoding
    - **V6** Stored Cryptography
    - **V7** Error Handling and Logging
    - **V8** Data Protection
    - **V9** Communications
    - **V10** Malicious Code
    - **V11** Business Logic
    - **V12** Files and Resources
    - **V13** API and Web Service
    - **V14** Configuration
- **Verification levels** — three cumulative levels, each inheriting the requirements of the previous one:
    - **Level 1 — Opportunistic** — basic hygiene, the minimum that any application should meet; verifiable by penetration testing alone (no source access needed). Aligns with the OWASP Top 10.
    - **Level 2 — Standard** — for applications handling sensitive data; requires defense-in-depth and a mix of design review, source review, and pentest.
    - **Level 3 — Advanced** — for the highest-risk applications (finance, healthcare, critical infrastructure); full verification including architecture review, threat modeling, and deep testing of every control.
- **How it relates to other documents**
    - Extends and operationalizes **OWASP Top 10** by mapping each Top-10 risk to concrete ASVS requirements.
    - Forms a pair with **OWASP MASVS** (Mobile Application Security Verification Standard) — the same approach adapted for mobile apps.
    - Used alongside **OWASP Testing Guide (WSTG)** — ASVS says "what to verify", WSTG says "how to test it".
    - Can be embedded into SDL (e.g., Microsoft SDL, NIST SSDF `PW` group) as the verification criteria for the "Verification" phase.
    - Maps to **ISO/IEC 27034** trust levels and Application Security Controls (ASC), and to **NIST SSDF** `PW.6` "Review approved software components" and `RV.1` vulnerability response.
- **Practical use**
    - Turn each requirement into an automated test (unit, integration, or pipeline gate) — this is how ASVS becomes part of the Paved Road.
    - Use the levels as acceptance criteria: the contract states "the application must pass ASVS L2", and the report shows which controls are met/missing.
    - As a scope for [threat modeling](#threat-modeling): the requirements list helps check that countermeasures cover all the standard threats.
- Current version: **ASVS 4.0.x** (the 4.0 line restructured the chapters and aligned them with the Top 10:2021). [Project page](https://owasp.org/www-project-application-security-verification-standard/), [PDF](https://github.com/OWASP/ASVS)
- **OWASP API Security Top 10** (OWASP)
    - Top 10 API risks
- **OWASP LLM Top 10** (OWASP)
    - Generative AI and LLM risks
- **CWE Top 25** (MITRE)
    - Top 25 dangerous software weaknesses
- **CIS Controls** (Center for Internet Security)
    - Prioritized set of protective measures (18 controls)
- **ISO/IEC 27034** (ISO)
    - International application security standard: processes, trust levels, ASC (Application Security Controls)
    - Adopted in Russia as GOST R ISO/IEC 27034-1-2014
- **Russian Federation GOST R 56939-2024**
    - Secure software development, general requirements
- **Russian Federation GOST R 58412-2019**
    - Security threats in software development
- **Russian Federation GOST R ISO/IEC 12207-2010**
    - System and software engineering. Software life cycle processes (IDT)
- **GOST R 50922-2006**
    - Protection of information. Basic terms and definitions
- **Russian Federation GOST R 57628-2017**
    - Information technology. Security techniques. Guide for the production of Protection Profiles and Security Targets
- **CISQ** (Consortium for IT Software Quality)
    - Standards for automated code quality measurement (Security, Reliability, Maintainability, Performance)
- **MISRA C/C++** (MISRA)
    - Secure coding standards for C/C++ (embedded, automotive)

## Threat modeling

Structured process of finding threats, attacks, vulnerabilities, and countermeasures at the design stage — before code is written. Answers four questions:

1. What are we building?
2. What can go wrong?
3. What are we going to do about it?
4. Did we do a good job?

- Part of Shift Left: cheaper to fix a design flaw than a shipped vulnerability
- Not a one-off document — the model is updated when the architecture changes
- Inputs: architecture diagrams, Data Flow Diagrams (DFD), assets, entry points, trust boundaries
- Generic steps
    1. Decompose the system — draw the DFD, mark trust boundaries, entry points, assets
    2. Identify threats — per element and per data flow
    3. Determine countermeasures — map each threat to a control (mitigate, transfer, accept, eliminate)
    4. Assess and prioritize — rank by risk
    5. Validate — verify the model against the implementation, track findings

### STRIDE

Threat classification from Microsoft; each letter maps to a violated security property and to a DFD element where it applies.

- **S**poofing — impersonating a user or component → Authentication
- **T**ampering — unauthorized modification of data or code → Integrity
- **R**epudiation — denying that an action took place → Non-repudiation
- **I**nformation disclosure — exposure of data to unauthorized parties → Confidentiality
- **D**enial of service — making a resource unavailable → Availability
- **E**levation of privilege — gaining more rights than granted → Authorization

DFD mapping (which letter to consider on which element):

- External entity → Spoofing, Repudiation
- Process → all six
- Data store → Tampering, Information disclosure, Repudiation, Denial of service
- Data flow → Tampering, Information disclosure, Denial of service

STRIDE-per-element is the practical variant: walk every DFD element and ask only the relevant letters.

### DREAD

Risk-rating model for already-identified threats (Microsoft, now deprecated). Each criterion is scored 1–10, the risk is the average.

- **D**amage — how bad is the impact if the threat is realized?
- **R**eproducibility — how easy is it to reproduce the attack?
- **E**xploitability — how much skill/effort does the attack require?
- **A**ffected users — how many users are impacted?
- **D**iscoverability — how easy is it to find the vulnerability?

Criticism: highly subjective scores, no clear thresholds, poor reproducibility between teams. Superseded by CVSS and bug bars (severity gates) in modern practice; still useful as a quick, memorable ranking heuristic.

### PASTA

**P**rocess for **A**ttack **S**imulation and **T**hreat **A**nalysis — risk-centric, attacker-centric methodology aligned with business objectives. Seven stages:

1. Define objectives — business goals and risk appetite
2. Define technical scope — technologies, infrastructure, dependencies
3. Application decomposition — DFD, assets, trust boundaries
4. Threat analysis — relevant threat actors, TTPs (ATT&CK/CAPEC)
5. Vulnerability and weakness analysis — CVEs/CWEs, controls gaps
6. Attack modeling and simulation — attack trees, exploitation paths
7. Risk and impact analysis — residual risk, prioritized countermeasures

Key difference from STRIDE: PASTA starts from business impact and simulates real attacker paths, so it produces better prioritization at the cost of more effort.

### Other methodologies

- **Trike** — risk-based, security-centric; emphasizes acceptable-risk levels and a formal requirement model
- **VAST** — Visual, Agile, and Simple Threat modeling; scales to Agile/DevOps, two model types (application and operational)
- **LINDDUN** — privacy threat modeling (Linkability, Identifiability, Non-repudiation, Detectability, Disclosure, Unawareness, Non-compliance)
- **Attack trees** — hierarchical decomposition of an attacker's goal into sub-goals and steps
- **OCTAVE** — organizational, self-directed risk/threat assessment (also listed under risk management)
- **MITRE ATT&CK / CAPEC** — knowledge bases of adversary tactics, techniques, and attack patterns used as input for threat analysis

### Tooling

- Microsoft Threat Modeling Tool — DFD-based, STRIDE-per-element, free
- OWASP Threat Dragon — open-source, DFD + STRIDE/LINDDUN, web and desktop
- IriusRisk, ThreatModeler — commercial, threat libraries plus automation
- pytm — "threat modeling as code" (Python, DFD from code, CI-friendly)

## Risk management

- Calculation
    - The amount of risk = the probability of the event * the amount of damage
    - Probability of an event = the probability of a threat * the magnitude of the vulnerability
    - ALE = SLE * ARO
- Vulnerability registries
    - CVE (Common Vulnerabilities and Exposures) — publicly disclosed security flaws
    - CWE (Common Weakness Enumeration) — catalog of common software weakness types
- Risk analysis
    1. Asset identification — identify all assets within the system scope
    2. Asset valuation — determine the criticality and value of each asset
    3. Threat identification — identify potential threats to each asset
    4. Vulnerability identification — identify weaknesses in the security controls
    5. Risk probability and impact assessment — evaluate the likelihood of threats and their business impact
    6. Cost assessment — estimate potential damage costs and the cost of security measures
    7. Recommendation generation — produce prioritized recommendations for risk mitigation
- Risk assessment
    - CVSS (Common Vulnerability Scoring System) — open standard for scoring vulnerability severity (0–10)
- Approaches to risk analysis
    - Qualitative analysis
        - Risk — identified risk item
        - Description — nature and context of the risk
        - Probability — likelihood of occurrence
        - Impact — consequences if realized
        - Result — overall risk level (e.g., low, medium, high)
        - Risk mitigation measures — actions to reduce or eliminate the risk
    - Quantitative analysis
        - Methods
            - Quantitative risk indicators
                - ALE (Annual Loss Expectancy) — SLE × ARO
                - SLE (Single Loss Expectancy) — asset value × exposure factor
                - EF (Exposure Factor) — percentage of asset loss from a single incident
                - ARO (Annualized Rate of Occurrence) — expected frequency of incidents per year
            - Static analysis
                - Trend Analysis — examining data over time to predict future patterns
                - Regression analysis — modeling relationships between variables
                - Time series analysis — analyzing time-ordered data points
                - Bayesian analysis — updating probabilities as new evidence emerges
            - The Monte-Carlo — simulating risk outcomes through random sampling
    - Combined analysis
        - OCTAVE (Operationally Critical Threat, Asset, and Vulnerability Evaluation) — self-directed risk assessment methodology
        - FAIR (Factor Analysis of Information Risk) — quantitative risk analysis taxonomy
        - RMF (NIST Risk Management Framework) — structured risk management process (categorize, select, implement, assess, authorize, monitor)
        - ISO/IEC 27005 — international standard for information security risk management
        - ENISA Risk Management Framework — European framework for risk assessment and management
        - COBIT (Control Objectives for Information and Related Technologies) — IT governance and management framework
        - Risk IT Framework — IT risk management extension to COBIT
        - ISO 31000 — international standard for generic risk management
- Information Security Architecture
    - access control mechanisms
    - threat monitoring and management systems
    - data protection measures
    - measures to comply with regulatory requirements
