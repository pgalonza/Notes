---
title: "Kernel"
draft: false
description: "Linux kernel notes"
---

{{< toc >}}

Set dump directory

```text
kernel.core_pattern = <path>/core.%u.%e.$p
```

## Make and build

Configure

```bash
make menuconfig
```

Make kernel all targets

```bash
make -j(<NUMBER_OF_CORES> + 1) all
```

Make modules

```bash
make modules_install
```

Make headers

```bash
make headers_install
```

Install kernel

```bash
make install
```
