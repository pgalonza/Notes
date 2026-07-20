---
title: Proccess
draft: false
description: "Comprehensive guide to Linux process management: monitoring, killing, namespaces, cgroups, priority tuning, file descriptor inspection, and performance analysis with tools like ps, top, strace, bpftrace, and perf."
summary: "A practical reference for system administrators and developers covering essential commands and techniques for analyzing, controlling, and optimizing Linux processes."
---

{{< toc >}}

## Process Discovery

Look up process by name

```bash
pgrep <process name>
```

Show process tree

```bash
pstree
pstree -p <PID>
```

Show information about a specific PID in real time

```bash
top -p <PID>
top -p <PID> -c
```

Batch mode (single snapshot)

```bash
top -b -n 1
```

Process information pseudo-filesystem

```bash
/proc
```

Symlink to the current process

```bash
ls /proc/self
```

Root directory of the current process

```bash
ls /proc/self/root
```

### PS

All processes

```bash
ps -ef
ps aux
```

Show RAM and CPU columns

```bash
ps -eo pid,cmd,%cpu,%mem
```

Sort by RAM

```bash
ps aux --sort=%mem
```

Sort by CPU

```bash
ps aux --sort=%cpu
```

Process tree with ASCII art

```bash
ps -ef --forest
```

Get PIDs of a process by name

```bash
pgrep <process name>
ps -ef | grep -v grep | grep <process name> | awk '{ print $2 }'
```

Print environment variables of a process

```bash
ps ewww
```

### TOP field reference

| Field | Description |
|---|---|
| `us`, user | Time running un-niced user processes |
| `sy`, system | Time running kernel processes |
| `ni`, nice | Time running niced user processes |
| `id`, idle | Time spent in the kernel idle handler |
| `wa`, IO-wait | Time waiting for I/O completion |
| `hi` | Time servicing hardware interrupts |
| `si` | Time servicing software interrupts |
| `st` | Time stolen from this VM by the hypervisor |

| Column | Description |
|---|---|
| `PID` | Process ID |
| `USER` | Username of the process owner |
| `PR` | Priority (lower value = higher priority, range -20 to 20) |
| `NI` | Nice value |
| `VIRT` | Virtual memory size (KiB) |
| `RES` | Resident (physical) memory size (KiB) |
| `SHR` | Shared memory size (KiB) |
| `S` | Status: `D` (uninterruptible sleep), `R` (running), `S` (sleeping), `T` (traced/stopped), `Z` (zombie) |
| `%CPU` | CPU usage (can exceed 100% on multi-core) |
| `%MEM` | Memory usage (RES / total RAM) |
| `TIME+` | Total CPU time since start |
| `COMMAND` | Command name or command line (`-c` for full line) |

## Process Control

Kill process by name

```bash
pkill <process name>
killall <process name>
```

Kill all processes of a user

```bash
killall -u <user name>
```

Show what process is using a device or mount point

```bash
fuser -m /mnt
```

Set or retrieve CPU affinity

```bash
taskset -pc <core> <PID>
```

Batch scheduling policy

```bash
chrt -b -p 0 <PID>
```

Set affinity to a NUMA node

```bash
numactl --cpunodebind=<NUMA node> --membind=<NUMA node> <command>
```

Run with CPU affinity and I/O weight limits

```bash
systemd-run --scope -p CPUAffinity=<core> -p IOWeight=<weight> -- <command>
```

Show limits of a process

```bash
cat /proc/<PID>/limits
```

Show shell limits of the current user

```bash
ulimit -a
```

Change process resource limits

```bash
prlimit --pid <PID> --nofile=<soft>:<hard>
```

Show kernel parameters

```bash
sysctl -a
```

Apply changes from `/etc/sysctl.conf`

```bash
sysctl -p
```

### Priority

Start with a niceness value

```bash
nice -n <value> <command>
```

Change niceness of a running process

```bash
renice -n <value> -p <PID>
```

Set I/O scheduling class and priority

```bash
ionice -c <1-3> -n <0-7> <command>
ionice -c <1-3> -n <0-7> -p <PID>
```

## Namespaces & Cgroups

Run a program in new namespaces

```bash
unshare <parameters> <program>
```

Join an existing namespace

```bash
nsenter --target <PID> <parameters> <program>
```

List namespace objects

```bash
lsns
```

Show namespaces of a process

```bash
ls -l /proc/<PID>/ns/
```

Show user/group ID mappings

```bash
cat /proc/<PID>/uid_map
cat /proc/<PID>/gid_map
```

Show cgroups of a process

```bash
cat /proc/<PID>/cgroup
```

Hide processes from other users (add to `/etc/fstab`)

```bash
proc /proc hidepid=<0-2>,gid=<group> ...
```

## Open Files & Sockets

Show maximum number of open files system-wide

```bash
cat /proc/sys/fs/file-max
```

Show allocated, free, and max file descriptors

```bash
cat /proc/sys/fs/file-nr
```

Show open files of a process

```bash
ls -l /proc/<PID>/fd/
lsof -p <PID>
```

Show processes of a user

```bash
lsof -u <user name>
```

Show open files by command name

```bash
lsof -c <command>
```

Show what process is using a port

```bash
lsof -i :<port number>
```

Show sockets of a process

```bash
lsof -i -p <PID>
lsof -i -a -p <PID>
```

Show open files in a directory

```bash
lsof +D <path to directory>
```

Find a socket by its inode number

```bash
grep <socket number> /proc/net/tcp
```

Count total open files

```bash
lsof | wc -l
```

Show deleted files still held open

```bash
lsof -nP | grep '(deleted)'
lsof -nP +L1
```

Read stdout/stderr of a running process

```bash
cat /proc/<PID>/fd/1
cat /proc/<PID>/fd/2
cat /proc/<PID>/fd/1 > /tmp/stdout.log
cat /proc/<PID>/fd/2 > /tmp/stderr.log
```

Truncate a file by path

```bash
: > <path to file>
```

Truncate an open file descriptor

```bash
: > /proc/<PID>/fd/<fd number>
```

### Inotify limits

Maximum inotify instances per user

```bash
cat /proc/sys/fs/inotify/max_user_instances
```

Maximum watches per inotify instance

```bash
cat /proc/sys/fs/inotify/max_user_watches
```

Maximum queued events

```bash
cat /proc/sys/fs/inotify/max_queued_events
```

## Tracing & Debugging

### Strace

Trace syscalls of a new process

```bash
strace -f -tt -s <number of symbols> -o <log file> <application>
```

Attach to a running process by name

```bash
pgrep <application> | awk '{print "-p " $1}' | xargs strace -f -tt -s <number of symbols> -o <log file>
```

### Bpftrace

Trace file open operations

```bash
bpftrace -e 'tracepoint:syscalls:sys_enter_openat { printf("%s %s\n", comm, str(args->filename)); }'
```

Trace process execution

```bash
bpftrace -e 'tracepoint:syscalls:sys_enter_execve { printf("%s\n", comm); }'
```

Trace signals sent to processes

```bash
bpftrace -e 'tracepoint:syscalls:sys_enter_kill { printf("%s -> PID %d, SIG %d\n", comm, args->pid, args->sig); }'
```

Count syscalls per process (live histogram)

```bash
bpftrace -e 'tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }'
```

Trace TCP connect attempts

```bash
bpftrace -e 'kfunc:tcp_connect { printf("%s -> %s:%d\n", comm, ntop2(args->sk->__sk_common.skc_daddr), args->sk->__sk_common.skc_dport); }'
```

### GDB

Attach to a process or open a core dump

```bash
gdb <program>
gdb <program> <core dump>
gdb -p <PID>
```

## Performance Analysis

Collect performance metrics for a process

```bash
perf stat -d -p <PID> -- sleep 10
```

Monitor process statistics (context switches, CPU, memory)

```bash
pidstat -wstu -p <PID> 1
```

Pressure Stall Information (CPU, IO, memory, IRQ)

```bash
tail -f /proc/pressure/cpu
tail -f /proc/pressure/io
tail -f /proc/pressure/memory
tail -f /proc/pressure/irq
```