---
title: "Minikube"
draft: false
description: "Minicube notes"
---

{{< toc >}}

Activate docker driver

```bash
minikube config set driver docker
```

Listen all interfaces

```bash
minikube start --listen-address=0.0.0.0
```

Port forwarding

```bash
minikube kubectl -- port-forward --address 0.0.0.0 service/<service name> <local port>:<resource port>
```

## Troubleshooting

TARGETS <unknown>/N%

```bash
kubectl get nodes
minikube addons list
minikube addons enable metrics-server
```

Empty ADDRESS kubernetes ingress

```bash
minikube addons list
minikube addons enable ingress
```
