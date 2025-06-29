---
title: "Design"
date: 2024-10-02T21:33:00+03:00
draft: false
description: "Architecture design"
---

{{< toc >}}

## C4 Model

- [C4-PlantUML](https://github.com/plantuml-stdlib/C4-PlantUML?tab=readme-ov-file#container-diagram)

### How to create

1. Collect Requirements and Define System Boundaries
2. Create Context Diagram (Level 1)
3. Create Container Diagram (Level 2)
4. Create Component Diagram (Level 3)
5. Create Code Diagram (Level 4)
6. Create Dynamic Diagram (Level 5)
7. Create Deployment Diagram (Level 6)

### Diagrams

- Context diagram — provides a high-level overview of the system and its boundaries, shows the system in the context of users and other systems, focuses on system boundaries and external interactions.
- Container diagram — displays the main high-level containers of the system (services, microservices, databases) and interactions between them, shows technology stacks and major data flows.
- Component diagram — delves into one of the containers, showing its components, their dependencies, and interactions, describes functional responsibilities.
- Code/classes diagram — displays the code structure within one of the components, shows classes, interfaces, and their relationships.
- Dynamic diagram (sequence diagram) — shows object interactions in a specific temporal order, focuses on the sequence of messages between objects.
- Deployment diagram — illustrates the physical placement of software artifacts on deployment nodes, displays infrastructure and connections between components.
- System Landscape — provides an overview of the entire system landscape, shows interactions between different systems in the environment, includes environment components and dependencies.
