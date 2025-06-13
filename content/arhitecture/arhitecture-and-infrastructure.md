---
title: "Arhitecture and Infrastructure"
date: 2024-11-30T17:20:22+03:00
draft: false
description: "Arhitecture and Infrastructure"
summary: ""
---

{{< toc >}}

## Cache

- Server
    - Patterns
        - Cache-Aside
            - Advantages
                - Устойчивость к сбоям кеша
                - Модель данных в кеше может отличаться от модели данных в БД
            - Disadvantages
                - Низкая скорость обновления данных
                - Несогласованность данных в кеше с базой данных
        - Read-Through
            - Advantages
                - Меньшая сложность приложения и низкая вероятность ошибок
            - Disadvantages
                - Кеш-промах при первом запросе
                - Ограничения на выбор модели данных в кеше
                - Чувствительность к ошибкам в отличие от Cache-Aside
        - Refresh-ahead
            - Advantages
                - Низкая стоимость чтения данных из БД
                - Согласованность записей кеша, к которым часто обращаются пользователи
                - Высокая чувствительность к задержкам
            - Disadvantages
                - Кеш должен работать без ошибок, поскольку в случае ошибки это будет не сразу определено и приведёт к неконсистентности данных и чтению из базы.
        Write-Through
            - Advantages
                - Данные между кешем и базой данных всегда будут синхронизированы
            - Disadvantages
                - Необходимость ждать, пока кеш обновит базу данных
        - Write-Behind
    - Invalidation
        - Time-based
        - Purge Cache
        - Refresh Cache
        - Time-To-Live(TTL) expiration Cache
        - Key-based
- Client


## Fault tolerance

- Availability
    - Calculation
        - Availability = (Agreed availability time – Downtime) / Agreed availability time * 100
    - Failover Strategy
        - Active-Active
        - Active-Passive (Active-Standby)
        - Active-Cold Standby
    - System maintenance time
        - MTBF, mean time between failure
        - MTTR, mean time to recovery
            - MTTD, mean time to detect
            - Repair time
        - Recovery Time Objective
        - Recovery Point Objective
    - Criticality classes
        - Mission critical
        - Business critical
        - Business operational
        - Office productivity
    - Patterns
        - Backpressure
        - Circuit Breaker
        - Rate limiting
            - Types
                - Blocking
                - Trottling
                - Prioritization
            - Algorithms
                - Tokens Bucket
                - Fixed Window counter
                - Sliding Window counter
                - Sliding Window Log
        - Bulkhead
        - Transactional outbox
            - Polling publishe
            - Transaction log tailing
                - Change Data Capture
- Disaster Recovery Plan
    - Testing
        - D&D game
- Global Server Load Balancer


## Observability

- Monitoring
    - USE
        - Utilization
        - Saturation
        - Errors
- 4 Golden Signals
    - Latency
    - Traffic
    - Errors
    - Saturation
- RED
    - Requests Rate
    - Errors
    - Duration

## Сloud computing

- Types
    - Deployment Model
        - Private Cloud
        - Public Cloud
        - Hybrid Cloud
    - Service Model
        - IaaS
            - Compute
            - Storage
            - Network
        - PaaS
            - Platform
            - Runtime
            - Services
        - SaaS
            - Software
            - Infrastructure
            - Support
- Migration
    - 6R Migration Strategy
        1. Retain. Частичная миграция.
        2. Retire. Замена части функциональности облачными решениями.
        3. Rehost or Lift and Shift. Миграция без изменений.
        4. Repurchase or Drop and Shop. Отказ от текущей реализации и полный переход на обланые решения.
        5. Replatform or Lift and Reshape. Минимальные изменения для использования преимуществ облачных решений.
        6. Refactor or Re-architect. Полная переработка текущей реализации под облачные решения.

## AI

1. Формирование бизнес-требований и технологического стека
2. Сбор данных
3. Подготовка данных
4. Анализ данных
5. Моделирование
6. Оценка модели и решения
7. Принятие решений
8. Мониторинг

CRISP-DM

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Data Modeling
5. Evaluation
6. Deployment


## Data processing

- OLTP(Online Transaction Processing)
    - Problems
        - Lost update
        - Dirty read
        - Non-repeatable read
        - Phantom read
    - Properties
        - ACID
            - Atomicity
            - Consistency
            - Isolation
            - Durability
        - BASE
            - Basically Available
            - Soft state
            - Eventual consistency
    - Isolation levels
        - Read uncommitted
        - Read committed
        - Repeatable read
        - Serializable
- OLAP(Online Analytical Processing)
    - Architecture of data warehouses
        - Data Warehouse
        - Data Lake
        - Data Lakehouse
    - Approaches to data processing
        - ETL(Extract, Transform, Load)
        - ELT(Extract, Load, Transform)
    - OLAP-cube
    - Models
        - Bill Inmon
        - Ralph Kimball
        - DataVault
        - Anchor
    - Schema
        - Star
        - Snowflake
    - Databases
        - Columns
            - MPP(Massive Parallel Processing)
            - MapReduce
            - Apache Spark
        - Rows

|Isolation levels|Lost update|Dirty read|Non-repeatable read|Phantom read|
|---|---|---|---|---|
|Read uncommitted|No|Yes|Yes|Yes|
|Read committed  |No|No|Yes|Yes|
|Repeatable read |No|No|No|Yes|
|Serializable    |No|No|No|No|

## Enterprise architecture

- Business Model Canvas
- TOGAF(Open Group Architecture Framework)
- SAFe(Scaled Agile Framework)

## Systems

- ERP(Enterprise Resource Planning)
    -  Used by CFOs and operations managers to manage enterprise resources, integrate finance, production, and logistics.
- BPMS(Business Process Management System)
    - Utilized by process owners and analysts to model, automate, and optimize business processes.
- CRM(Customer Relationship Management)
    -  Implemented by sales and marketing teams to manage customer relationships and enhance sales performance.
- MDM(Master Data Management)
    - Employed by data governance teams to ensure data consistency and quality across systems.
- BI(Business Intelligence)
    - Used by executives and decision-makers for data analysis, reporting, and strategic decision-making.
- PLM(Product Lifecycle Management)
    - Utilized by product development teams to manage the entire lifecycle of products.
- PDM(Product Data Management)
    - Implemented by engineering and design teams to manage product data and documentation.
- MES(Manufacturing Execution System)
    - Used by production managers to oversee and optimize manufacturing processes.
- SCADA(Supervisory Control and Data Acquisition)
    - Employed by plant operators and engineers to monitor and control industrial processes.
- ABS (Automated Banking System)
    - Utilized by bank employees and customers to process financial transactions, manage accounts, and provide banking services.
- SCM(Supply Chain Management)
    -  Implemented by logistics and supply chain managers to manage and optimize supply chains.

## Landscape

- Map
    - Row - Business Capability
    - Column - Organization unit
    - Intersection - system

## Change management

- FURPS+
    - Functionality
    - Usability
    - Reliability
    - Performance
    - Supportability
    - Restrictions
