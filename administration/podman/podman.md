# Podman

Registries
_/etc/containers/registries.conf_
```
unqualified-search-registries = ["registry.fedoraproject.org", "registry.access.redhat.com", "registry.centos.org", "docker.io", "quay.io"]
```

Choose storage driver
```
export STORAGE_DRIVER=vfs
```

Network configurations
_/etc/cni/net.d/_


## Troubleshooting

kernel does not support overlay fs: 'overlay' is not supported over extfs at "": backing file system is unsupported for this graph driver

_/etc/containers/storage.conf_
uncomment
```
mount_program = "/usr/bin/fuse-overlayfs"
```
