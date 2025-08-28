---
title: "Kubernetes"
date: 2025-07-25T00:17:34+03:00
draft: false
description: "Comprehensive notes covering Kubernetes architecture, deployment strategies, and advanced cluster management techniques. Dive into container orchestration, scaling practices, and best practices for production environments. Perfect for DevOps engineers and cloud architects seeking to master Kubernetes capabilities."
summary: "Kubernetes (k8s) Notes: Advanced Cluster Management"
---

{{< toc >}}

- Components
    - Master node(Control plane)
        - API Server
        - Scheduler
        - Controller Manager
        - etcd
    - Worker node
        - Kubelet
        - kube-proxy
        - Container runtime
- Claster objects
    - Node
    - Pod
    - Service
    - Deployment
        - Statuses
            - Progressing
            - Replica Failure
            - Complete
    - ConfigMap
    - Secret
    - Namespace
        - default
        - kube-node-lease
        - kube-public
        - kube-system
