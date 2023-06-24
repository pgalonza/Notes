---
title: "Windows"
draft: false
description: "CLI commands for Windows"
---

{{< toc >}}

## Recovery

### SFC

Scan system files

```bash
sfc /scannow
```

### DISM

Scan and recovery system files

```bash
DISM /Online /Cleanup-Image /RestoreHealth
```

## PowerShell

Test TCP connection to a port

```powershell
Test-NetConnection -ComputerName host_name -Port port_number -InformationLevel "Detailed"
```

Route diagnostic

```powershell
Test-NetConnection -ComputerName host_name -DiagnoseRouting -InformationLevel "Detailed"
```

## Encoding

Change code page

```powershell
chcp code_page
```

## Problem steps recorder

Run problem steps recorder

```text
win + R
psr
```

## Qwinsta

Show active sessions on remoute host

```cmd
qwinsta /server:host_name
```
