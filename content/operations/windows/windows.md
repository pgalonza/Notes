---
title: "Windows"
draft: false
---

{{< toc >}}

Enable the developer mode for unsigned drivers

```cmd
bcdedit.exe /set nointegritychecks ON
bcdedit.exe /set TESTSIGNING ON
bcdedit.exe /set loadoptions DDISABLE_INTEGRITY_CHECKS
```

Stop service

```bash
@ECHO OFF
net stop "1C:<name of service>"
timeout /T 15
taskkill /IM  <name of executable file> /F
exit
```

Stop MSSQL

```bash
@ECHO OFF
net stop SQLSERVERAGENT
net stop MSSQLLAUNCHPAD
net stop MSSQLSERVER
```

Proxy file (proxy.pac)

```text
function FindProxyForURL(url, host)
{
  if (isPlainHostName(host)) {return "DIRECT";}
  if (shExpMatch(host, "127.0.0.1" )) {return "DIRECT";}
  if (shExpMatch(host, "*/localhost*" )) {return "DIRECT";}
  if (dnsDomainIs(host, ".domain")) {return "DIRECT";}
  if (!isInNet(host, "10.0.192.0", "255.255.240.0")) {return "DIRECT";}
  return "PROXY host:3128";
}
```

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

## Registry

Maximum attachment size in outlook
_HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Outlook\Preferences_
_HKEY_CURRENT_USER\Software\Microsoft\Office\15.0\Outlook\Preferences_

```text
MaximumAttachmentSize DWORD
```

## Sadow copies

Maximum of shadow copies
_HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\VSS\Settings_

```text
MaxShadowCopies DWORD
```

List existing volume shadow copies

```cmd
vssadmin list shadows
```

Make symbol link to shadow copy

```cmd
mklink /d %SystemDrive%\shadow \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy\
```
