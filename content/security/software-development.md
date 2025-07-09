---
title: "Software Development"
date: 2025-02-11T23:08:40+03:00
draft: false
description: "Comprehensive security best practices for developing robust software applications. From coding standards to deployment, learn how to build secure software that protects user data and maintains compliance."
summary: ""
---

{{< toc >}}


## Standards

[Russian Federation GOST R 56939-2024](https://base.garant.ru/410749342/#:~:text=Национальный%20стандарт%20РФ%20ГОСТ%20Р,г.%20Взамен%20ГОСТ%20Р%2056939-2016)


## Types of threats

- Угрозы по месту
    - Внутренние
    - Внешние
- Угрозы по видимости
    - Активные
    - Пассивные
- Угрозы по доступу
    - С несанкционированным доступом
    - С утечкой или нарушением целостности данных
- Угрозы по цели
    - Угрозы данных
    - Угрозы компонентам, информационным сервисам
    - Угрозы по апратному обеспечению
    - Угрозы по обеспечивающей инфраструктуре
- Угрозы по объективности
    - Объективные
    - Субъективные
    - Случайные


## Risk management

- Colculation
    - The amount of risk = the probability of the event * the amount of damage
    - Probability of an event = the probability of a threat * the magnitude of the vulnerability
    - ALE = SLE * ARO
- Risk analysis
    1. Идентификация активов
    2. Определение ценности активов
    3. Идентификация угрозы активам
    4. Идентификация уязвимости в системе защиты
    5. Оценка вероятности реализации угроз и влияние и их влияние на бизнес
    6. Оценка стоимиости возможных негативных последствий и стоимости мер защиты
    7. Формирование конкретных, приоритизированных рекоменгдаций по выявленным рискам и методам их минимизации
- Approaches to risk analysis
    - Qualitative analysis
        - Risk
        - Description
        - Probability
        - Impact
        - Result
        - Risk mitigation measures
    - Quantitative analysis
        - Methods
            - Quantitative risk indicators
                - ALE(Annual Loss Expectancy)
                - SLE(Single Loss Expectancy)
                - EF(Exposure Factor)
                - ARO(Annualized Rate of Occurrence)
            - Static analysis
                - Trend Analysis
                - Regression analysis
                - Time series analysis
                - Bayesian analysis
            - The Monte-Carlo
    - Combined analysis
        - OCTAVE(Operationally Critical Threat, Asset, and Vulnerability Evaluation)
        - FAIR(Factor Analysis of Information Risk)
        - RMF(NIST Risk Management Framework)
        - ISO/IEC 27005
        - ENISA Risk Management Framework
        - COBIT(Control Objectives for Information and Related Technologies)
        - Risk IT Framework
        - ISO 31000
- Information Security Architecture
    - access control mechanisms
    - threat monitoring and management systems
    - data protection measures
    - measures to comply with regulatory requirements

## Classification of data

- Standarts
    - ISO/IEC 27001, ISO/IEC 27002
        - Public data
        - Internal data
        - Confidential data
        - Secret data
    - NIST SP 800-53, NIST SP 800-60
        - Low impact
        - Moderate impact
        - High impact
    - 152-ФЗ «О персональных данных»
        - Publicly available personal data
        - Personal data
        - Special categories of personal data

## Data protection

- Homomorphic encryption
- Data Loss Prevention (DLP)
- Data Obfuscation Mechanisms
    - Tokenization of data
    - Shuffling
    - Zeroing/Substitution
    - Character Scrambling
- Data Masking
    - Static Data Masking
    - Dynamic Data Masking
    - Deterministic Masking
    - Non-Deterministic Masking

## Identity and Access Management

- RBAC(Role-Based Access Control)
- ABAC(Attribute-Based Access Control)
    - [OASIS](https://oasis.connectedcommunity.org/communities/tc-community-home2?CommunityKey=67afe552-0921-49b7-9a85-018dc7d3ef1d#CURRENT)
    - [ALFA](https://alfa.guide/abbreviatedlanguageforauthorization-alfa/)
    - [NIST](https://www.nist.gov/identity-access-management/policy-machine-and-next-generation-access-control)