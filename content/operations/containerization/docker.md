---
title: "Docker"
date: 2023-07-15T00:15:06+03:00
draft: false
description: "Practical Docker notes covering container creation from rootfs, essential commands, security best practices, caching optimization, and multi‑process startup scripts for DevOps engineers."
summary: "A collection of Docker tips, command examples, and security configurations to streamline container management and image building."
aliases:
  - /operations/docker/docker/
---

{{< toc >}}

## Commands

Create container from rootfs

```bash
tar --verbose --create --file <file name>.tar --directory <path to rootfs> .
cat <file name>.tar | sudo docker import - <image name>
```

```bash
tar -C <path to rootfs> -c . | docker import - <image name>
```

```text
FROM scratch
ADD <path to rootfs> /
```

Systemd in container

```bash
docker <> --volume /sys/fs/cgroup:/sys/fs/cgroup:rw --cgroupns=host --priveleged --command (/usr)/sbin/init
```

Remove all images

```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q -f dangling=true)
```

Show size of layers

```bash
docker history --human --format '{{.Size}}\t{{.CreatedBy}}' <image>
```

## Security

### Security Options

```bash
--security-opt=no-new-privileges
--read-only
```

### Linux Capabilities

Fine-grained privilege control by adding or dropping individual capabilities.

```bash
--cap-drop=ALL --cap-add=NET_BIND_SERVICE
```

View container capabilities:

```bash
docker inspect <container name> --format '{{.State.Pid}}'
cat /proc/<PID>/status | grep Cap
capsh --decode=$(grep CapEff /proc/<PID>/status | awk '{print $2}')
```

### Seccomp

Seccomp (secure computing mode) filters allowed system calls. Default Docker profiles block ~50 dangerous syscalls.

Use `unconfined` when a container requires blocked syscalls (e.g. systemd containers, debugging, or legacy software):

```bash
--security-opt seccomp=unconfined
```

Pass a custom profile for fine-grained control:

```bash
--security-opt seccomp=/path/to/custom-profile.json
```

### User & Privilege Drop

[gosu](https://github.com/tianon/gosu)

```bash
gosu
```

## Tools

* Crane - tool for building and managing container images, written in Go.
* BuildKit - tool for building container images, written in Go.
* Buildah - tool for building OCI/Docker container images without a daemon, written in Go.

## Cache

[Optimize cache usage in builds](https://docs.docker.com/build/cache/optimize/)

## Configs

Host config path

__/var/lib/docker/containers/<ID>/hostconfig.json__

## Start scripts

Execute commands and start more one process in container

```bash
#!/usr/bin/env bash

_term() {
  echo "Caught SIGTERM signal!"
  <commands>
}

trap _term SIGTERM

<commands>

sleep infinity &

wait $!
```

## Build images

[Example](https://github.com/pgalonza/docker-build-demo)

## Dockerfile

Here-Documents

```dockerfile
RUN <<'EOF'
  <commands>
EOF
```
```dockerfile
COPY <<'EOF' <file name>
  <text>
EOF
```
```dockerfile
COPY <<-EOT <file name>.sh
  "${<variable>}"
EOT
```
```dockerfile
COPY <<-"EOT" <file name>.sh
  echo "${<variable>}"
EOT
```

Multistage builder

```dockerfile
FROM <base image> AS <stage name>
<commands>

FROM <stage name or base image> AS <stage name>
<commands>
```

```bash
docker build --target <stage name> -t <image name> .
```

## Docker compase

```bash
docker-compose up -d -f <file name>.yml -f <file name>.yml
```
