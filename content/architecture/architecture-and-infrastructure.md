---
title: "Architecture and Infrastructure"
date: 2024-11-30T17:20:22+03:00
draft: false
description: "Comprehensive guide to software architecture and infrastructure covering caching, fault tolerance, observability, cloud computing, data processing, enterprise systems, and migration patterns."
summary: "A detailed reference for architects and engineers, exploring key concepts, patterns, and best practices for designing robust, scalable, and maintainable systems."
---

{{< toc >}}

## Cache

### Server-side caching

#### Patterns

**Cache-Aside**

- Advantages
  - Resilient to cache failures
  - The data model in the cache may differ from the database model
- Disadvantages
  - Slow data updates
  - Data in the cache can become inconsistent with the database

**Read-Through**

- Advantages
  - Less application complexity and a lower chance of errors
- Disadvantages
  - Cache miss on the first request
  - Limited choice of the cache data model
  - More sensitive to errors than Cache-Aside

**Refresh-Ahead**

- Advantages
  - Low cost of reading data from the database
  - Consistency of frequently accessed cache entries
- Disadvantages
  - The cache must work flawlessly: errors are not detected immediately and lead to data inconsistency and reads from the database

**Write-Through**

- Advantages
  - Data between the cache and the database is always synchronized
- Disadvantages
  - Requires waiting for the cache to update the database

**Write-Behind**

#### Invalidation

- Time-based
- Purge cache
- Refresh cache
- TTL (Time-To-Live) expiration
- Key-based

### Client-side caching

## Fault Tolerance

### Availability

#### Calculation

Availability = (Agreed availability time − Downtime) / Agreed availability time × 100

#### Failover Strategies

- Active-Active
- Active-Passive (Active-Standby)
- Active-Cold Standby

#### System Maintenance Time

- MTBF — mean time between failures
- MTTR — mean time to recovery
  - MTTD — mean time to detect
  - Repair time
- RTO (Recovery Time Objective)
- RPO (Recovery Point Objective)
- WRT (Work Recovery Time)
- MTPD (Maximum Tolerable Period of Disruption)

#### Criticality Classes

- Mission critical
- Business critical
- Business operational
- Office productivity

### Patterns

- Backpressure
- Circuit Breaker
- Rate limiting
  - Types
    - Blocking
    - Throttling
    - Prioritization
  - Algorithms
    - Token bucket
    - Fixed window counter
    - Sliding window counter
    - Sliding window log
- Bulkhead
- Transactional outbox
  - Polling publisher
  - Transaction log tailing
    - Change Data Capture

### Disaster Recovery Plan (DRP)

- Testing
  - D&D game

### Global Server Load Balancer

## Observability

### Monitoring Frameworks

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
  - Request rate
  - Errors
  - Duration

## Cloud Computing

### Types

- Deployment models
  - Private cloud
  - Public cloud
  - Hybrid cloud
- Service models
  - IaaS — Compute, Storage, Network
  - PaaS — Platform, Runtime, Services
  - SaaS — Software, Infrastructure, Support

### Migration

#### 6R Migration Strategy

1. **Retain** — partial migration.
2. **Retire** — replace part of the functionality with cloud solutions.
3. **Rehost** (Lift and Shift) — migrate without changes.
4. **Repurchase** (Drop and Shop) — abandon the current implementation and move fully to cloud solutions.
5. **Replatform** (Lift and Reshape) — minimal changes to benefit from cloud solutions.
6. **Refactor** (Re-architect) — completely rework the current implementation for the cloud.

## AI

### AI Project Lifecycle

1. Business requirements & technology stack definition
2. Data acquisition
3. Data preprocessing
4. Data analytics
5. Model development
6. Model & solution validation
7. Decision deployment
8. Model monitoring

### CRISP-DM

1. Business understanding
2. Data understanding
3. Data preparation
4. Data modeling
5. Evaluation
6. Deployment

## Data Processing

### OLTP (Online Transaction Processing)

#### Problems

- Lost update
- Dirty read
- Non-repeatable read
- Phantom read

#### Properties

- ACID
  - Atomicity
  - Consistency
  - Isolation
  - Durability
- BASE
  - Basically available
  - Soft state
  - Eventual consistency

#### Isolation Levels

- Read uncommitted
- Read committed
- Repeatable read
- Serializable

| Isolation level | Lost update | Dirty read | Non-repeatable read | Phantom read |
|---|---|---|---|---|
| Read uncommitted | No | Yes | Yes | Yes |
| Read committed | No | No | Yes | Yes |
| Repeatable read | No | No | No | Yes |
| Serializable | No | No | No | No |

### OLAP (Online Analytical Processing)

#### Data Warehouse Architectures

- Data warehouse
  - Modern data warehouse
- Data lake
  - Raw data store
- Data lakehouse
  - Types of storage
    - File storage
    - Block storage
    - Object storage
      - Amazon Simple Storage Service (S3)
  - Metadata
    - Apache Iceberg — open file formats, open table formats
    - Apache Hudi
    - Delta Lake
  - Catalogs
    - Based on files
      - Hadoop catalog
    - Based on services
      - JDBC
      - Hive Metastore
      - Nessie
      - Glue

#### Approaches to Data Processing

- ETL (Extract, Transform, Load)
- ELT (Extract, Load, Transform)

#### OLAP Cube

#### Models

- Bill Inmon
- Ralph Kimball
- Data Vault
- Anchor

#### Schema

- Star
- Snowflake

#### Databases

- Column-oriented
  - MPP (Massive Parallel Processing)
  - MapReduce
  - Apache Spark
- Row-oriented

### Processing Methods

- Batch-processing engine
- Real-time processing engine

## Enterprise Architecture

- TOGAF (Open Group Architecture Framework)
- IT landscape map/diagram
- Business capability map
- Integration diagram
- Digital Transformation Roadmap
  - Project-based approach
    - PRINCE2
    - PMBOK
  - Product-based approach

## Systems

| System | Used by | Purpose |
|---|---|---|
| ERP (Enterprise Resource Planning) | CFOs, operations managers | Manage enterprise resources, integrate finance, production, and logistics |
| BPMS (Business Process Management System) | Process owners, analysts | Model, automate, and optimize business processes |
| CRM (Customer Relationship Management) | Sales, marketing teams | Manage customer relationships and enhance sales performance |
| MDM (Master Data Management) | Data governance teams | Ensure data consistency and quality across systems |
| BI (Business Intelligence) | Executives, decision-makers | Data analysis, reporting, strategic decision-making |
| PLM (Product Lifecycle Management) | Product development teams | Manage the entire product lifecycle |
| PDM (Product Data Management) | Engineering, design teams | Manage product data and documentation |
| MES (Manufacturing Execution System) | Production managers | Oversee and optimize manufacturing processes |
| SCADA (Supervisory Control and Data Acquisition) | Plant operators, engineers | Monitor and control industrial processes |
| ABS (Automated Banking System) | Bank employees, customers | Process financial transactions, manage accounts, provide banking services |
| SCM (Supply Chain Management) | Logistics, supply chain managers | Manage and optimize supply chains |

## Landscape

### Map

- Row — business capability
- Column — organizational unit
- Intersection — system

### Managing the Technical Landscape

#### Roadmap

##### Types of Technical Debt

- Architectural debt
- Codebase debt
- Infrastructure debt
- Software quality debt
- Process debt
- Defect debt
- Documentation debt
- Intentional/known debt
- Unknown legacy/accidental debt
- Bit rot/band-aid debt

##### Assessment of Technical Debt

- Cost estimation
- Criticality assessment
  - Technical Debt Ratio (TDR) = (cost of elimination / development cost) × 100%

##### TIME Model

- Tolerate
- Invest
- Eliminate
- Mitigate

#### Tech Radar

- Quadrants
  - Languages and frameworks
  - Tools
  - Platforms & infrastructure
  - Methods & patterns
- Rings
  - Base (Adopt, Trial, Assess, Hold)
  - TRL (Technology Readiness Levels)
    - Contents
      1. Basic principles observed and reported
      2. Technology concept formulated
      3. Experimental proof of concept
      4. Technology validated in lab environment
    - Development
      5. Technology validated in relevant environment
      6. System/subsystem prototype demonstrated in relevant environment
      7. System prototype demonstrated in operational environment
      8. Actual system completed and qualified through test and demonstration
    - Implementation
      9. Actual system proven through successful mission operations
- Trends
  - New
  - Moved in/out
  - No change

## Architecture Design

- FURPS+
  - Functionality
  - Usability
  - Reliability
  - Performance
  - Supportability
  - Restrictions
- Use Case Flow / User Story
  - Basic flow
  - Alternative flow
- BPMN
- Mendelow matrix
- Business Model Canvas
- Lean Canvas
- SAFe (Scaled Agile Framework)
  - Value stream
- Stakeholders
  - Stakeholder matrix
    - High/low engagement
    - High/low influence
    - Role
    - Tasks
    - Requirements and expectations

## Change Management

- Predictive approach
- Reactive approach
- Sequential approach

## Solution Architecture

- Architecture vision
  - Architecture Decision Record (ADR)
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
  - Storytelling

## Data Privacy

- PII (Personally Identifiable Information)
- PHI (Protected Health Information)

### Privacy by Design (PbD)

- Proactive not reactive; preventative not remedial
  - Privacy Impact Assessment (PIA)
- Privacy as the default setting
- Privacy embedded into design
- Full functionality — positive-sum, not zero-sum
- End-to-end security — full lifecycle protection
- Visibility and transparency
- Respect for user privacy

### Privacy-Enhancing Technologies (PET)

### Data Flow Management (DFM)

- Data Flow Diagram (DFD)
  - Data source
  - Processes
  - Data stores
  - Data flows
  - External entities

### Related Concepts

- Digital Rights Management (DRM)
- Collective knowledge

### Data Layers

- Raw data
- Processed data
- Golden source

### Data Status

- At rest
- During transfer process
- During use

### Data Lineage

- Scope definition and planning
- Data discovery and inventory
- Data flow mapping
- Data transformation documentation
- Metadata management
- Tool selection and implementation
- Regulatory compliance assurance
- Governance framework and policy establishment
- Continuous improvement and monitoring
- Data governance

### Other Practices

- Data minimization
- [Data obfuscation mechanisms](/security/software-development/#data-protection)
- [Data masking](/security/software-development/#data-protection)
- Tagging data

## Bottleneck Identification in Existing Solutions

### Conway's Law

- Team functional boundaries
- Cross-functional collaboration
- Organizational social boundaries

### Ishikawa (Fishbone) Diagram

- Man
- Machine
- Material
- Method
- Measurement
- Mother nature

### Metrics

- DORA
  - Deployment frequency
  - Lead time for changes
  - Change failure rate
  - Time to restore service
- MTTR (Mean Time to Recovery)
- Error rate
- Performance metrics
- RTO (Recovery Time Objective) & RPO (Recovery Point Objective)

## Migration Patterns

### Strangler Fig

#### Advantages

- Gradual replacement of the monolith
- Reduced risk
- Incremental delivery of new features
- Solving technical debt

#### Implementation Steps

1. Define the domain area
   - Techniques
     - Domain-Driven Design
       - Areas: domain, subdomain, context
       - Design
         - Strategic — Bounded Context, Context Map
         - Tactical — Entities, Value Objects, Aggregates, Repositories, Services
       - Domain identification
         1. Analyze the business and requirements
         2. Identify domains
         3. Split into subdomains
         4. Define contexts
         5. Create context maps
         6. Iterative refinement
     - Technical analysis
     - Performance analysis
   - Prioritization
     - Criteria: business impact, technical impact, customer impact
     - Methods
       - MoSCoW — Must have, Should have, Could have, Won't have
       - Eisenhower matrix — urgent & important, not urgent but important, urgent but not important, not urgent & not important
       - Kano model — Must-have, Performance, Excitement, Indifferent, Reverse
       - Weighted scoring model
       - ICE scoring — Impact, Confidence, Effort
       - Value vs. Effort
       - Cost of Delay
       - RICE — Reach, Impact, Confidence, Effort
       - WSJF — Weighted Shortest Job First
2. Design and develop the new services
3. Monitor and verify
   - Application performance monitoring
   - Centralized logging
   - Infrastructure monitoring
   - A/B testing
   - Automated testing
4. Switch traffic
   - Routing
     - Reverse proxy
     - API Gateway
     - Service Mesh
   - Anti-corruption layer (ACL)
     - Patterns: Facade, Adapter
     - Advantages
       - Isolation from the complexity and problems of the legacy system
       - Control over request routing
       - Adaptation of data to various requirements
       - Encapsulation of the monolithic system

### Other Patterns

- Parallel Run
- High-Level Design
- Branch by Abstraction

## Big Data

### Characteristics

- Volume
- Velocity
- Variety
- Veracity
- Value

### Related Topics

- [Data processing](#data-processing)
- [Data lineage](#data-privacy)
- Data catalog

### Data Mesh

- Principles
  - Domain-driven data contexts
  - Unified infrastructure platform
  - Data as a product mindset
  - Self-serve infrastructure
  - Federated governance

### Data Ops
