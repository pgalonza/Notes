---
title: "K8S"
date: 2025-07-25T00:17:34+03:00
draft: false
description: "Comprehensive notes covering Kubernetes architecture, deployment strategies, and advanced cluster management techniques. Dive into container orchestration, scaling practices, and best practices for production environments. Perfect for DevOps engineers and cloud architects seeking to master Kubernetes capabilities."
summary: "Kubernetes (k8s) Notes: Advanced Cluster Management"
---

{{< toc >}}

## Kubernetes

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
      - Pod Scheduling
        - Taints and Tolerations
        - NodeSelector
        - Affinity and Anti-Affinity
    - Pod
        - Init-container
        - Pod Topology Spread Constraints
        - Pod Disruption Budget
    - Service
        - ClusterIP
        - NodePort
        - LoadBalancer
        - ExternalName
    - Deployment
        - Statuses
            - Progressing
            - Replica Failure
            - Complete
    - ConfigMap
    - Secret
    - StatefulSet
    - DaemonSet
    - Ingress
    - Job and CronJob
    - Namespace
        - default
        - kube-node-lease
        - kube-public
        - kube-system
    - Autoscalers
        - Horizontal Pod Autoscaler
        - Vertical Pod Autoscaler
        - Cluster Autoscaler
    - ResourceQuota
    - NetworkPolicy
    - RBAC
        - Role
        - RoleBinding
        - ClusterRole
        - ClusterRoleBinding

## Deployment Tools

- [Werf](https://github.com/werf/werf)
- [Helm](https://github.com/helm/helm)

## Troubleshooting

It is recommended not to set CPU limits to avoid performance problems.