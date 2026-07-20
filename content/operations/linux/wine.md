---
title: Wine
draft: false
description: "Wine (Wine Is Not an Emulator) notes for running Windows applications on Linux."
summary: "A practical reference for managing Wine prefixes and running Windows applications with Wine on Linux."
---

Run application with prefix

Create prefix

```bash
env WINEPREFIX=<path to prefix> winecfg
```

Update prefix

```bash
env WINEPREFIX=<path to prefix> wineboot -u
```

Run application

```bash
env WINEPREFIX=<path to prefix> wine <path to application>
```