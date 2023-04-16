---
title: "SystemD"
draft: false
---

Show problems

```bash
systemctl --failed
```

Get pid

```bash
systemctl status systemd-modules-load
```

## Journalctl

Unit logs in real time

```bash
journalctl -fu <unit_name>
```

Show problems by pid

```bash
journalctl _PID=
```

Show without less

```bash
journalctl --no-pager
```
