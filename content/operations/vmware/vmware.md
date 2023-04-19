---
title: "VMWare ESXI"
draft: false
---

Move swap

* Power off the virtual machine.
* Unregister the virtual machine. Right-click the virtual machine in the Inventory and choose Remove from Inventory.
* Open *.vmx

*/vmfs/volumes/datastore_name/virtual_machine_folder/*

```text
sched.swap.dir = /vmfs/volumes/datastore_name/dir_name
#sched.swap.derivedName = xxx
```

When Veeam make backup the host lost the time

* start ntp service
* host time zone UTC

Max query metrics

```text
config.vpxd.stats.maxQueryMetrics = -1
```

## Virtual Machine

### Configuration parameters

#### Disk

Type = Thick provisioned, eagerly zeroed

Disk mode = Indeoendent - persistent

#### SCSI Controller

SCSI = VMware Pravirtual

#### Network Adapter

Adapter Type = VMXNET 3

## Troubleshooting

Linux virtual machine with lost network

* Set current time

1c aplication server is freeze after hard reboot

* re-register the virtual machine

## Scripts

[VM poweroff on python](https://github.com/pgalonza/Notes-files/vmware/scripts/esxi-poweroff.py)
