# Processes

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

Show open files of process

```bash
ls -l /proc/<PID>/fd/
lsof | grep <PID>
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

Run in napeespace

```bash
unshare <parameters> <program>
```

Show cgroups

```bash
cat /proc/<PID>/cgroup
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

Batch mode and clouse

```bash
top -b -n 1
```
