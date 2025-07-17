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

1. Business Requirements & Technology Stack Definition
2. Data Acquisition
3. Data Preprocessing
4. Data Analytics
5. Model Development
6. Model & Solution Validation
7. Decision Deployment
8. Model Monitoring

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
            - Modern Data Warehouse
        - Data Lake
            - Raw Data Store
        - Data Lakehouse
            - Types of storages
                - File storage
                - Block storage
                - Object storage
                    - Amazon Simple Storage Service (S3)
            - Metadata
                - Apache Iceberg
                    - Open File Formats
                    - Open Table Formats
                - Apache Hudi
                - Delta Lake
            - Catalogs
                - Based on files
                    - Hadoop Catalog
                - Based on services
                    - JDBC
                    - Hive Metastore
                    - Nessie
                    - Glue
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
- Methods
    - Batch-Processing Engine
    - Real-Time Processing Engine

|Isolation levels|Lost update|Dirty read|Non-repeatable read|Phantom read|
|---|---|---|---|---|
|Read uncommitted|No|Yes|Yes|Yes|
|Read committed  |No|No|Yes|Yes|
|Repeatable read |No|No|No|Yes|
|Serializable    |No|No|No|No|

## Enterprise architecture

- TOGAF(Open Group Architecture Framework)
- IT Landscape map/diagram
- Business capability map
- Integration diagram
- Digital Transformation Roadmap
    - Project-based approach
        - PRINCE2
        - PmBook
    - Product-based approach

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

### Managing the technical landscape

- Roadmap
    - Types of technical debt
        - Architectural Debt
        - Codebase Debt
        - Infrastructure Debt
        - Software Quality Debt
        - Process Debt
        - Defect Debt
        - Documentation Debt
        - Intentional/Known Debt
        - Unknown Legacy/Accidental Debt
        - Bit Rot/Band-Aid Debt
    - Assessment of technical debt
        - Сost estimation
        - Сriticality assessment
            - Technical Debt Ration(TDR) = (cost of elimination / development cost) * 100%
    - TIME Model
        - Tolerate
        - Invest
        - Eliminate
        - Mitigate
    - Tech Radar
        - Elements
            - Quadrants
                - Languages and Frameworks
                - Tools
                - Platforms & Infrastructure
                - Methods & Patterns
            - Rings
                - Base
                    - Adopt
                    - Trial
                    - Assess
                    - Hold
                - TRL (Technology Readiness Levels)
                    - Contents
                        1. Basic principles observed and reported
                        2. Technology concept formulated
                        3. Experimental proof of concept
                        4. Technology validated in lab environment
                    - Development
                        5. Technology validated in relevant environment
                        6. System/subsystem prototype demonstration in relevant environment
                        7. System prototype demonstration in operational environment
                        8. Actual system completed and qualified through test and demonstration
                    - Implementation
                        9. Actual system proven through successful mission operations
            - Trends
                - New
                - Moved in/out
                - No change

## Architecture design

- FURPS+
    - Functionality
    - Usability
    - Reliability
    - Performance
    - Supportability
    - Restrictions
- Use Case Flow/User Story
    - Basic Flow
    - Alternative Flow
- Alternative Flow
- BPMN
- Mendelow Matrix
- Business Model Canvas
- Lean Canvas
- SAFe(Scaled Agile Framework)
    - Value stream
- Stakeholders
    - Stakeholder matrix
        - High/Low Engagement
        - High/Low Influence
        - Role
        - Tasks
        - Requirements and expectations

## Change management

- Predictive Approach
- Reactive Approach
- Sequential Approach

## Solution architecture

- Architecture vision
    - Architecture Design Record
        - Y-statement
            - Context
            - Facing
            - We decided for
            - Neglected
            - To achieve
            - Accepting that
    - Architecture Decision Log
- Change management
- Design thinking
    - Empathize
    - Define
    - Ideate
    - Prototype
    - Test
    - Storytel

## Data Privacy

- PII(Personally Identifiable Information)
- PHI(Protected Health Information)

- Privacy by Design (PbD)
    - Proactive not Reactive; Preventative not Remedial
        - Privacy Impact Assessment (PIA)
    - Privacy as the Default Setting
    - Privacy Embedded into Design
    - Full Functionality ― Positive-Sum, not Zero-Sum
    - End-to-End Security ― Full Lifecycle Protection
    - Visibility and Transparency
    - Respect for User Privacy
- Privacy-enhancing technologies (PET)
- Data Flow Management (DFM)
    - Data Flow Diagram (DFD)
        - Data Source
        - Processes
        - Data Stores
        - Data Flows
        - External Entities
- Digital Rights Management (DRM)
- Сollective knowledge
- Data Layers
    - Raw data
    - Processed data
    - Golden source
- Data Status
    - At Rest
    - During Transfer Process
    - During Use
- Data Lineage
    - Scope Definition and Planning
    - Data Discovery and Inventory
    - Data Flow Mapping
    - Data Transformation Documentation*
    - Metadata Management
    - Tool Selection and Implementation
    - Regulatory Compliance Assurance
    - Governance Framework and Policy Establishment
    - Continuous Improvement and Monitoring
    - Data governance
- Data Minimization
- [Data Obfuscation Mechanisms](/security/software-development.md/#data-protection)
- [Data Masking](/security/software-development.md/#data-protection)
- Tagging data

## Bottleneck Identification in Existing Solutions

- Conway's law
    - Team Functional Boundaries
    - Cross-functional Collaboration
    - Organizational Social Boundaries
- Ishikawa Diagram (Fishbone Diagram) Methodology
    - Man
    - Machine
    - Material
    - Method
    - Measurement
    - Mother Nature
- Metrics
    - DORA
        - Deployment Frequency
        - Lead Time for Changes
        - Change Failure Rate
        - Time to Restore Service
    - Mean Time to Recovery (MTTR)
    - Error Rate
    - Performance Metrics
    - RTO (Recovery Time Objective) & RPO (Recovery Point Objective)

## Migration Patterns

- Strangler Fig
    - Преимущества
        - Постепенная замена монолита
        - Снижение рисков
        - Инкрементная доствака новых функций
        - Решение проблемы технического долга
    - Реализация
        1. Определение доменной области
            - Техники
                - Domain-Driven Design
                    - Области
                        - Домен
                        - Поддомен
                        - Контекст
                    - Проектирование
                        - Стратегическое
                            - Bounded Context
                            - Context Map
                        - Тактическое
                            - Entities
                            - Value Objects
                            - Aggregates
                            - Repositories
                            - Services
                    - Выделение доменов
                        1. Анализ бизнеса и требований
                        2. Выделение доменов
                        3. Разделение на поддомены
                        4. Определение контекстов
                        5. Создание контекстных карт
                        6. Итеративное уточнение
                - Технический анализ
                - Анализ производительности
            - Приоритизация
                - Бизнес-влияние
                - Техническое влияние
                - Клиентское влияние
                - Методы
                    - MoSCoW
                        - Must have
                        - Should have
                        - Could have
                        - Won't have
                    - Матрица Эйзенхауэра
                        - Срочно и важно
                        - Не срочно, но важно
                        - Срочно, но не важно
                        - Не срочно и не важно
                    - Модель Кано
                        - Must-Have
                        - Performance
                        - Excitement
                        - Indifferent
                        - Reverse
                    - Weighted Scoring Model
                    - ICE Scoring
                        - Impact
                        - Confidence
                        - Effort, ICE
                    - Value vs. Effort
                    - Cost of Delay
                    - RICE
                        - Reach
                        - Impact
                        - Confidence
                        - Effort
                    - WSJF
                        - Weighted
                        - Shortest
                        - Job
                        - First
        2. Проектирование и разработка новых сервисов
        3. Мониторинг и верификация
            - Application perfomance monitoring
            - Централизованное логирование
            - Мониторинг инфраструктуры
            - A/B-тестирование
            - Автоматизированное тестирование
        4. Переклюяение трафика
            - Маршутизация
                - Reverse proxy
                - API Gateway
                - Service Mesh
            - Anti-corruption layer (ACL)
                - Паттерны
                    - Facade
                    - Adapter
                - Преимущества
                    - Изоляция от сложностей и проблем
                    - Управление маршрутизацией запросо
                    - Адапация днных под различные требования
                    - Инкапсуляция монолитной системы
- Parallel Run
- High-Level Design
- Branch by Abstraction

## BigData

- Characteristic
    - Volume
    - Velocity
    - Variety
    - Veracity
    - Value
- [Data processing](/arhitecture/arhitecture-and-infrastructure/#data-processing)
- Data Mesh
    - Principle
        - Domain-Driven Data Contexts
        - Unified Infrastructure Platform
        - Data as a Product Mindset
        - Self-Serve Infrastructure
        - Federated Governance
- Data Ops
- [Data lineage](/arhitecture/arhitecture-and-infrastructure/#data-privacy)
- Data Catalog
