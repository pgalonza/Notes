---
title: "Printers"
date: 2026-07-20T22:10:09+03:00
draft: false
description: "How to connect Linux to a shared printer on Windows via SMB and CUPS."
summary: "A guide for connecting Linux to a Windows shared printer using SMB protocol and configuring the DeviceURI in CUPS."
---

{{< toc >}}

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

```text
DeviceURI smb://[username]%40[domain]:[password]@[pass to printer]
```
