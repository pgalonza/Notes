---
title: "DevSecOps"
date: 2026-09-26T00:00:00+03:00
draft: false
description: "A structured overview of AppSec/DevSecOps frameworks: maturity models, SDL process frameworks, supply chain security, risk management, approaches and practices, and standards. Learn how SAMM, BSIMM, DSOMM, MS SDL, NIST SSDF, SLSA and others relate to each other."
summary: "Systematized reference on security frameworks and practices: maturity models (SAMM, BSIMM, DSOMM, DAF), secure development lifecycle frameworks (MS SDL, NIST SSDF, BSA, SAFECode), supply chain security (SLSA, Scorecard, SBOM), risk management, approaches (Paved Road, Guardrails, Shift Left), and checklists (OWASP ASVS, Top 10, CIS Controls)."
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
    - Threat modeling (STRIDE)
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
