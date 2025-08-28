---
title: "K3S"
date: 2025-08-28T23:22:22+03:00
draft: false
description: "Practical notes and insights about deploying and managing lightweight k3s clusters. Explore simplified Kubernetes setup, configuration best practices, and troubleshooting tips for small-scale environments. Ideal for developers and system administrators working with minimal resource requirements."
summary: "k3s Notes: Lightweight Kubernetes Management"
---

{{< toc >}}


## Desktop

Installation

```bash
curl -sfL https://get.k3s.io | K3S_KUBECONFIG_MODE="644" sh -s - --node-external-ip=<ip address of deskctop>
```


## Troubleshooting

If Desktop ip was changed, need reset cluster

```bash
k3s server --cluster-reset
```