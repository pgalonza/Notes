---
title: "Docker"
date: 2023-07-15T00:15:06+03:00
draft: false
description: "Docker manuals"
---

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

```bash
docker build --tag <image name> <path to rootfs>
```
