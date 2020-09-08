# Windows commands
## Recovery
### SFC

Scan system files
```
sfc /scannow
```

### DISM

Scan and recovery system files
```
DISM /Online /Cleanup-Image /RestoreHealth
```

## PowerShell

Test TCP connection to a port
```
Test-NetConnection -ComputerName host_name -Port port_number -InformationLevel "Detailed"
```

Route diagnostic
```
Test-NetConnection -ComputerName host_name -DiagnoseRouting -InformationLevel "Detailed"
```

## Encoding

Change code page
```
chcp code_page
```

## Problem steps recorder 

Run problem steps recorder
```
win + R
psr
```
