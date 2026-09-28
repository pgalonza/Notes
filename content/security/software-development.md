---
title: "Software Development"
date: 2025-02-11T23:08:40+03:00
draft: false
description: "Comprehensive security best practices for developing robust software applications. From coding standards to deployment, learn how to build secure software that protects user data and maintains compliance."
summary: "Guidelines and practices for integrating security into the software development lifecycle, covering threat modeling, data classification, and access control."
---

{{< toc >}}


## Standards

- See [DevSecOps — Standards and checklists](/security/devsecops/#standards-and-checklists)


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


## Cookies

Golden session cookie configuration with security flags. [Information from](https://edu.eversecure.ru/devsecops)

```text
Set-Cookie: session=<session id>; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=3600
```
