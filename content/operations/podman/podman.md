---
title: "Podman"
draft: false
description: "Podman notes"
---

{{< toc >}}

Registries
_/etc/containers/registries.conf_

```bash
unqualified-search-registries = ["registry.fedoraproject.org", "registry.access.redhat.com", "registry.centos.org", "docker.io", "quay.io"]
```

Choose storage driver

```bash
export STORAGE_DRIVER=vfs
```

Multiple scripts and services

```bash
#!/usr/bin/env bash

_term() {
  echo "Caught SIGTERM signal!"
}

trap _term SIGTERM

sleep infinity &

wait $!
```

Network configurations
_/etc/cni/net.d/_

Clear testing

```bash
sudo podman rm --all; sudo podman rmi wireguard; sudo buildah rm --all
```

## Troubleshooting

kernel does not support overlay fs: 'overlay' is not supported over extfs at "": backing file system is unsupported for this graph driver

_/etc/containers/storage.conf_
uncomment

```bash
mount_program = "/usr/bin/fuse-overlayfs"
```
