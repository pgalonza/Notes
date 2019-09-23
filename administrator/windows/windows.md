# Windows
Enable the developer mode for unsigned drivers
```
bcdedit.exe /set nointegritychecks ON
bcdedit.exe /set TESTSIGNING ON
bcdedit.exe /set loadoptions DDISABLE_INTEGRITY_CHECKS
```

## Registry
Maximum of shadow copies
_HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\VSS\Settings_
```
MaxShadowCopies DWORD
```
