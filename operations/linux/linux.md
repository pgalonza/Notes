# Linux

Thunderbird check all folders

```bash
mail.server.default.check_all_folders_for_new true
```

Hard disk partitions

```bash
/dev/sda1 — boot
/dev/sda2 — root (/)
/dev/sda3 — home
/dev/sda4 — var
/dev/sda5 — tmp
/dev/sda6 — swap
```

Running some program in background

```bash
nohup <program_name> > <program_name>.out 2> <program_name>.err < /dev/null & echo -n "$!" > pid.file &
```

Restore .bashrc, .bash_profile and .bash_logout

```bash
cp /etc/skel/{.bashrc,.bash_profile,.bash_logout} .
```

Shebang indicate an interpreter for execution under UNIX / Linux operating systems

```bash
#!
```

```bash
#!/bin/bash
#!/bin/env bash 
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

```text
DeviceURI smb://[username]%40[domain]:[password]@[pass to printer]
```

## SWAP

### Create SWAP

Swap file

```bash
fallocate -l 1G /swapfile
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
```

## Tools

### Top

* us, user    : time running un-niced user processes
* sy, system  : time running kernel processes
* ni, nice    : time running niced user processes
* id, idle    : time spent in the kernel idle handler
* wa, IO-wait : time waiting for I/O completion
* hi : time spent servicing hardware interrupts
* si : time spent servicing software interrupts
* st : time stolen from this vm by the hypervisor

---

* PID -- Process Id : This is a unique number used to identify the process.
* User -- The username of whoever launched the process.
* PR -- Priority : The priority of the process. Processes with higher priority will be favored by the kernel and given more CPU time than processes with lower priority. Oddly enough, the lower this value, the higher the actual priority; the highest priority on \*nix is -20 and the lowest is 20.
* NI -- Nice value : nice is a way of setting your process' priority. See here for more details.
* VIRT -- Virtual Memory Size (KiB) : The total amount of virtual memory used by the process.
* RES -- Resident Memory Size (KiB) : The non-swapped physical memory a task has used.
* SHR -- Shared Memory Size (KiB) : The amount of shared memory available to a task, not all of which is typically resident. It simply reflects memory that could be potentially shared with other processes.
* S -- Process Status : The status of the task which can be one of:
  * 'D' = uninterruptible sleep
  * 'R' = running
  * 'S' = sleeping
  * 'T' = traced or stopped
  * 'Z' = zombie

* %CPU -- CPU Usage : The percentage of your CPU that is being used by the process. By default, top displays this as a percentage of a single CPU. On multi-core systems, you can have percentages that are greater than 100%. For example, if 3 cores are at 60% use, top will show a CPU use of 180%. See here for more information. You can toggle this behavior by hitting Shifti while top is running to show the overall percentage of available CPUs in use.
* %MEM -- Memory Usage (RES) : A task's currently used share of available physical memory (RAM).
* TIME+ -- CPU Time, hundredths : Total CPU time the task has used since it started.
* COMMAND -- Command Name or Command Line : To see the full command line that launched the process, start top with the -c flag : top -c.

## FSTAB

Do not allow set-user-identifier or set-group-identifier bits to take effect

```text
nosuid
```

Do not allow direct execution of any binaries on the mounted filesystem

```text
noexec
```

## Network

Forward

```bash
echo net.ipv4.ip_forward = 1 >> /etc/sysctl.conf
echo net.ipv6.conf.all.forwarding=1 >> /etc/sysctl.conf
```

IPv6
_/etc/sysconfig/network_

```text
NETWORKING_IPV6=yes
```

### VLAN

Adding new virtual interface

```bash
ip link add link ethX name ethX.vlan_id type vlan id vlan_id
```

Assign ip-address to interface

```bash
ip addr add X.X.X.X/XX dev ethX.vlan_id
```

Enabling the interface

```bash
ip link set dev ethX.vlan_id up
```

### MACVLAN

Adding new makvlan interface

```bash
ip link add link ethX makvlan_name type macvlan mode bridge
```

### Bridge

Adding new bridge interface

```bash
ip link add name bridge_name type bridge
```

Adding interface to bridge

```bash
ip link set interface_name master bridge_name
```

Removing interface

```bash
ip link set interface_name nomaster
```

## Sudoers

Root without asking password

```bash
<user_name> ALL=(ALL) NOPASSWD: ALL
```
