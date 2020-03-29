# Linux

Thunderbird check all folders
```
mail.server.default.check_all_folders_for_new true
```

Hard disk partitions
```
/dev/sda1 — boot
/dev/sda2 — root (/)
/dev/sda3 — home
/dev/sda4 — var
/dev/sda5 — tmp
/dev/sda6 — swap
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
