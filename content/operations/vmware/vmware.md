---
title: "VMWare ESXI"
draft: false
---

{{< toc >}}

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

## ESXI

### Network

Up or down

```bash
esxcli network nic up/down -n vmnicX
```

Set speed and duplex

```bash
esxcfg-nics -s 10000 -d full vmnicX
```

### Disk

Convert the Thin disk to Eager Zeroed Thick disk

```bash
vmkfstools --inflatedisk /vmfs/volumes/DatastoreName/VMName/VMName.vmdk
```

Convert the Thick disk to Eager Zeroed Thick disk

```bash
vmkfstools --eagerzero /vmfs/volumes/DatastoreName/VMName/VMName.vmdk
```

Check and repair vmdk

```bash
vmkfstools --fix check file_name.vmdk
vmkfstools -x check file_name.vmdk
vmkfstools -x repair file_name.vmdk
```

## Amavisd

Check the configuration file

```bash
amavisd -u amavis -c /etc/amavisd/amavisd.conf debug
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

[VM poweroff on python](https://github.com/pgalonza/Notes-files/blob/main/vmware/scripts/esxi-poweroff.py)
