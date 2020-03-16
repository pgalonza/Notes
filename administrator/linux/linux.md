# Linux

Thunderbird check all folders
```
mail.server.default.check_all_folders_for_new true
```

## Linux printers
Connect Linux to a shared printer on Windows!

1. If have driver installer use it
2. Go to the printer Management window and add a new one
3. Connection Protocol choose smb.
4. In the path field, enter the ip/name of the PC or press the find button to find a PC and printer.
5. Select the driver for the printer.
6. Open the printer configuration file
_/etc/cups/printers.conf_
and edit the parameter _DeviceURI_
```
DeviceURI smb://[username]%40[domain]:[password]@[pass to printer]
```
