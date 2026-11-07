---
title: "Microservices and Micro-frontends"
date: 2024-10-02T21:33:00+03:00
draft: false
description: "Comprehensive guide to microservices and microfrontends architecture, covering design patterns, integration strategies, deployment, and best practices for building scalable distributed systems."
summary: "Explore key concepts, patterns, and implementation details for microservices and microfrontends, from decomposition and communication to monitoring and security."
---

{{< toc >}}

## Micro-frontends

### Advantages

- Organizational flexibility
- Freedom to choose the technology stack
- Easier codebase management
- Controllable scaling
- Fault tolerance
- Time to market

### When It Is Not a Good Fit

- Simple application
- Limited functionality
- Limited development resources
- Tightly coupled components
- MVP (Minimum Viable Product) or PoC (Proof of Concept)
- High performance requirements
- Organizational and cultural constraints of the company
- Insufficient infrastructure, processes, and CI/CD tooling

### Components

#### Microfrontend Modules

#### Composition Layer

- Hybrid composition
- Server-side composition
  - Reverse proxy (Nginx, HAProxy)
  - Backend for Frontend (BFF)
    - Prepares data for the client
    - Simplifies client-side logic
    - Improves performance
    - Improves security
  - API composition
- Client-side composition
  - Single SPA
  - Module Federation

#### Routing

- Hybrid
- Server-side
- Client-side
- Dynamic

#### Communication Layer

- API
  - Interaction exclusively with the backend
  - Simple data exchange
  - High performance and scalability requirements
- Publisher/Subscriber pattern
  - No direct dependencies
  - Event-driven architecture
  - Independent deployment
- Global or shared state
  - Tight coupling between different parts of the application
  - Consistency across the application and a consistent user experience
  - Demanding state management requirements

### Strategies

- Vertical slicing
- Team autonomy
- Isolation

### Integration Methods

- Build time
  - Simplified adoption
  - Tight coupling of features and components
  - Performance
- Run time
  - Independent deployment of modules
  - Dynamic module updates (development)
  - Scaling

## Microservices

### Monolith Separation

- [Migration patterns](architecture-and-infrastructure/#migration-patterns)

#### Roadmap

- Service boundaries
- Interaction methods
  - Synchronous
    - RESTful
    - gRPC
    - OpenAPI
  - Asynchronous
    - Event-Driven Architecture
      1. Domain analysis
      2. Domain model description
      3. Functionality decomposition
      4. Event flow modeling
      5. Event modeling
      6. Event broker selection
      7. Implementation and monitoring
      8. Testing and validation
    - AsyncAPI
- Data management
  - Data consistency strategies
    - Eventual consistency
    - Strong consistency
    - Data partitioning
  - Distributed transactions
    - Two-phase commit protocol (2PC)
    - Saga pattern
      - Eventual consistency
- Deployment strategies
  - Blue-Green
  - Canary
  - Rolling
- Load balancing
  - Strategies
    - Round robin
    - Least connections
    - IP hash, sticky sessions
    - Weighted round robin
    - Random distribution
    - Least response time
    - Least bandwidth
- Fault tolerance
- Scalability
  - Replication
  - Caching
  - Sharding and partitioning
    - Partitioning
      - Vertical
      - Horizontal
    - Sharding
      - Hash-based
      - Range-based
      - Dynamic
      - Geo-sharding
    - Routing
      - DBMS-native
      - Router service
      - Client-side
- Security
- Monitoring and observability
- Data storage
- API management
- Testing and validation
- DevOps practices
- Versioning and compatibility

#### Lifecycle

- Design
- Development
- Testing
- Deployment
- Monitoring and support
- Scaling
- Updating and improvement
- Decommissioning

## Patterns

### Application Patterns

- Database per Service
- Service per Team
- Event Sourcing
- Stream Processing
  - Synchronous micro-batch processing
  - Asynchronous micro-batch processing
  - Streaming model
  - Continuous update model
- Message Queueing
- Publish/Subscribe
- CQRS
  - Commands
  - Queries
  - Implementation
    1. Define commands and queries
    2. Implement the data models
    3. Implement command and query handlers
    4. Adapt consumer systems so they can integrate with various components to send queries and commands
- Saga
  - Implementation types
    - Orchestration — complex business processes, need for centralized management, transactional coordination, complex business logic
    - Choreography — simple interactions, independent microservices, flexibility and scalability as a priority, event-driven architecture
  - Error handling and compensation
    - Compensating transactions
    - Retries
    - Timeouts and deadlines
    - Event-driven error handling
    - Monitoring and alerting systems
  - Implementation
    - Analyze the business process and define the Saga steps
    - Design the microservices
    - Manage the state and interaction of microservices
    - Implement actions and compensating actions
    - Logging and monitoring
    - Testing
- Transactional Outbox
- Transaction Log Tailing

### Application Infrastructure Patterns

- Distributed tracing
- Audit logging
- API Gateway
  - Types
    - Monolithic
    - Distributed
    - Multi-layered
    - Serverless
  - Functions
    - Centralized request routing
    - Authentication and authorization management
    - Load balancing and traffic distribution
    - Security enforcement
    - Request caching
- Front-to-back
  - Client pull
    - Patterns
      - Short polling
      - Long polling
    - Implementations
      - REST
      - GraphQL
  - Server push
    - Implementations
      - WebSockets
      - Server-Sent Events
      - GraphQL Subscriptions
- Back-to-back
  - Patterns
    - Request-Response
    - Publish-Subscribe
  - Implementations
    - REST
    - GraphQL
    - gRPC

### Infrastructure Patterns

- Service Discovery
- Service Mesh
- Service Registry

## Principles

### The Twelve-Factor App

- Codebase
- Dependencies
- Config
- Backing services
- Build, Release, Run
- Processes
- Port binding
- Concurrency
- Disposability
- Dev/Prod parity
- Logs
- Admin processes

### Lightweight Microservices

- Minimalism
- Independence
- Fast startup time
- Efficient resource usage
- Simplified dependencies
- Ensured isolation
- Documentation and automation

### DevOps

- Pipeline as Code
  - Repeatability
  - Flexibility
  - Versioning
  - Transparency
  - Scalability
  - Error-proneness
- Infrastructure as Code
- CI/CD
  - Continuous Integration
  - Continuous Delivery
  - Continuous Deployment

## Identification, Authentication, Authorization

### SSO (Single Sign-On)

#### OAuth (Open Authorization)

- Roles
  - Resource owner
  - Resource server
  - Authorization server
  - Client
  - User agent
- Refresh token storage
  - Server
  - HTTP-only cookie
  - LocalStorage
  - WebWorker
- Flows
  - Authorization code
  - Implicit
  - Resource owner password credentials
  - Client credentials
  - Device authorization
- RFCs
  - [RFC 7519](https://www.rfc-editor.org/rfc/rfc7519)
  - [RFC 6749](https://datatracker.ietf.org/doc/rfc6749/)

#### OpenID Connect

#### SAML (Security Assertion Markup Language)

#### Kerberos
