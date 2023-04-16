---
title: "Windows"
draft: false
---

Enable the developer mode for unsigned drivers

```cmd
bcdedit.exe /set nointegritychecks ON
bcdedit.exe /set TESTSIGNING ON
bcdedit.exe /set loadoptions DDISABLE_INTEGRITY_CHECKS
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
