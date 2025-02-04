---
title: "Docker"
date: 2023-07-15T00:15:06+03:00
draft: false
description: "Docker notes"
---

{{< toc >}}

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

## Commands

```bash
docker build --tag <image name> <path to rootfs>
```

```bash
docker run --rm  --name container_name  -p 80:80 -v path_in_host:path_in_container tag/name:tag

docker build -t tag/name:tag -f DockerFile .

docker exec -it container_name bash
```

## Security

```bash
--security-opt=no-new-privileges
--read-only
```

## Tools

* Crane - tool for Docker containers orchestration written in Go.
* Kaniko - build Container Images.

## Cache

[Optimize cache usage in builds](https://docs.docker.com/build/cache/optimize/)

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