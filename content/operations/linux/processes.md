---
title: Proccess
draft: false
description: "CLI commands for wotk with linux proccess"
---

{{< toc >}}

Look process by name

```bash
pgrep
```

Kill process by name

```bash
pkill <process name>
killall <process name>
```

Process tree

```bash
pstree
```

Show what process use device

```bash
fuser -m /mnt
```

Kill all user processes

```bash
killall -u user
```

Process information pseudo-filesystem

```bash
/proc
```

Show information about PID

```bash
top -p <PID>
```

Show namespaces

```bash
ls -l /prod/proc/<PID>/ns/
```

Show maps

```bash
cat /proc/<PID>/uid_map
cat /proc/<PID>/gid_map
```

Run in namespaces

```bash
unshare <parameters> <program>
```

Show namespaces

```bash
lsns
ls -al /proc/<PID>/ns
```

Show cgroups

```bash
cat /proc/<PID>/cgroup
```

Execute program in namespace

```bash
nsenter --target <PID> <parameters> <program>
```

## Open files, sockets

Show maximum of open files

```bash
cat /proc/sys/fs/file-max
```

Show open files of process

```bash
ls -l /proc/<PID>/fd/
lsof | grep <PID>
```

Show a list of user processes

```bash
lsof -u <user_name>
```

Show open files of process

```bash
lsof -p <pid>
```

Show openfiles of command

```bash
lsof -c <command>
```

Show what process use port

```bash
lsof -i :<port_number>
```

Show open files in directory

```bash
lsof +D <path_to_directory>
```

Show the number of open files on your system

```bash
lsof | wc -l
lsof <path to dir>
```

Show limits of process start by user

```bash
cat /proc/<pid>/limits
```

Show maximum of objects inotify per user

```bash
/proc/sys/fs/inotify/max_user_instances
```

Show maximum of watch files and directories per object inotify

```bash
/proc/sys/fs/inotify/max_user_watches
```

Show maximum of events in queued

```bash
/proc/sys/fs/inotify/max_queued_events
```

Show shell process of user limits

```bash
ulimit -a
```

Show settings

```bash
sysctl -a
```

Accept changes

```bash
sysctl -p
```

Change process limits

```bash
prlimit --pid PID --nofile=1024:1024
```

## Priority

IO priority

```bash
ionice -c3 coommand
```

Start with priority

```bash
nice -n 15 command
```

Change the priority

```bash
renice renice -n 15 -p pid
```

## PS

Sort by RAM

```bash
ps aux | sort -nk 4
ps aux --sort=%mem | grep -v 'root' | head -n 35
```

Sort by CPU

```bash
ps aux | sort -nk 3
ps aux --sort=%cpu | grep -v 'root' | head -n 35
```

Show processes

```bash
ps -ef
```

Show RAM and CPU

```bash
ps -eo cmd,%cpu,%mem
```

Show processes with ASCII art process tree

```bash
ps -ef --forest
```

Show pids of process

```bash
ps -ef | grep -v grep | grep <process_name> | awk '{ print $2 }'
```

## TOP

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

Batch mode and clouse

```bash
top -b -n 1
```

## Strace

```bash
strace -f -tt -s <number of symbols> -o <log file> <application name>
pgrep <name of application> | awk '{print "-p " $1}' | xargs strace -f -tt -s <number of symbols> -o <log file> 
```

## GDB

```bash
gdb <program or dump>
```

## File descriptors

Show allocated file descriptors, not use file descriptors, maximum of file descriptors

```bash
cat /proc/sys/fs/file-nr
```

Show proccess descriptors

```bash
ls -l /proc/<number of proccess>/fd
```

Truncate file

```bash
: > <path to file>
```

Truncate descriptor

```bash
: > proc/<pid>/fd/$fd
```

Show deleted files

```bash
lsof -nP | grep '(deleted)'
lsof -nP +L1
```
