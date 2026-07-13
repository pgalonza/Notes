---
title: "Software Development"
date: 2025-02-11T23:08:40+03:00
draft: false
description: "Comprehensive security best practices for developing robust software applications. From coding standards to deployment, learn how to build secure software that protects user data and maintains compliance."
summary: "Guidelines and practices for integrating security into the software development lifecycle, covering threat modeling, risk management, data classification, and access control."
---

{{< toc >}}


## Standards

- Russian Federation GOST R 56939-2024 - Information protection. Secure software development. General requirements
- Russian Federation GOST R ISO/IEC 12207-2010 - System and software engineering, Software life cycle processes(IDT)
- Russian Federation GOST R 58412—2019
- Russian Federation GOST R 50922-2006 - Protection of information. Basic terms and definitions
- Russian Federation GOST R 57628-2017 - Information technology. Security techniques. Guide for the production of Protection Profiles and Security Targets


## Types of threats

- By location
    - Internal — threats originating from within the organization (e.g., employees, insiders)
    - External — threats originating from outside the organization (e.g., hackers, third parties)
- By visibility
    - Active — threats that involve direct interaction with the system (e.g., exploiting a vulnerability)
    - Passive — threats that involve monitoring or eavesdropping without direct interaction
- By access
    - Unauthorized access — gaining access to resources without permission
    - Data leakage or integrity violation — exposure or alteration of sensitive data
- By target
    - Threats to data
    - Threats to components and information services
    - Threats to hardware
    - Threats to supporting infrastructure
- By objectivity
    - Objective — threats independent of human perception (e.g., natural disasters)
    - Subjective — threats caused by human factors (e.g., errors, malicious intent)
    - Accidental — unintentional threats (e.g., mistakes, misconfigurations)


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

## Classification of data

- Standards
    - ISO/IEC 27001, ISO/IEC 27002
        - Public data — no restrictions, freely accessible
        - Internal data — limited to internal use
        - Confidential data — restricted access, moderate harm if disclosed
        - Secret data — highly restricted, severe harm if disclosed
    - NIST SP 800-53, NIST SP 800-60
        - Low impact — limited adverse effect on operations or assets
        - Moderate impact — serious adverse effect
        - High impact — severe or catastrophic adverse effect
    - 152-ФЗ «О персональных данных»
        - Publicly available personal data — accessible from public sources
        - Personal data — any information relating to an identified or identifiable individual
        - Special categories of personal data — sensitive data (health, biometrics, beliefs, etc.)

## Data protection

- Homomorphic encryption — computation on encrypted data without decryption
- Data Loss Prevention (DLP) — monitoring and blocking unauthorized data transfers
- Data Obfuscation Mechanisms
    - Tokenization — replacing sensitive data with non-sensitive placeholders
    - Shuffling — random permutation of values across records
    - Zeroing/Substitution — replacing real values with zeros or dummy data
    - Character Scrambling — randomizing characters within data fields
- Data Masking
    - Static Data Masking — irreversible masking in non-production copies
    - Dynamic Data Masking — real-time masking based on user permissions
    - Deterministic Masking — same input always produces the same masked output
    - Non-Deterministic Masking — each masking operation may produce a different result

## Identity and Access Management

- RBAC (Role-Based Access Control) — access based on roles assigned to users
- ABAC (Attribute-Based Access Control) — access based on attributes (user, resource, environment)
    - [OASIS](https://oasis.connectedcommunity.org/communities/tc-community-home2?CommunityKey=67afe552-0921-49b7-9a85-018dc7d3ef1d#CURRENT)
    - [ALFA](https://alfa.guide/abbreviatedlanguageforauthorization-alfa/)
    - [NIST](https://www.nist.gov/identity-access-management/policy-machine-and-next-generation-access-control)


## Containers

### Java

- [How to build a custom Java image](https://github.com/lebmax/java-custom-container) — best practices for building minimal and secure Java container images

## Cookies

Golden session cookie configuration with security flags. [Information from](https://edu.eversecure.ru/devsecops)

```text
Set-Cookie: session=<session id>; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=3600
```
