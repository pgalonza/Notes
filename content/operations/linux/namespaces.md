---
title: "Namespaces"
date: 2026-07-20T18:21:10+03:00
draft: false
description: "Comprehensive guide to Linux namespaces and isolation primitives: unshare, nsenter, lsns, all seven namespace types (mount, PID, net, IPC, UTS, user, cgroup), UID/GID mapping, and practical examples for process isolation and lightweight containerization."
summary: "A practical reference for system administrators and developers covering Linux namespace management commands, kernel isolation mechanisms, and hands-on examples for creating isolated environments with unshare and nsenter."
---

{{< toc >}}

## Unshare

### Mount namespace

Isolates filesystem mount points

```bash
unshare --mount bash
cat /proc/self/mountinfo
mount --bind /some/dir /mnt
```

### PID namespace

Isolates process ID numbering (requires `--fork`)

```bash
unshare --pid --fork bash
mount -t proc proc /proc
ps aux
```

### Network namespace

Isolates network stack (interfaces, routes, iptables)

```bash
unshare --net bash
ip link
ip link set lo up
```

Connect two netns via veth

```bash
ip netns add ns1
ip link add veth0 type veth peer name veth1
ip link set veth1 netns ns1
ip netns exec ns1 ip addr add 10.0.0.1/24 dev veth1
ip netns exec ns1 ip link set veth1 up
ip addr add 10.0.0.2/24 dev veth0
ip link set veth0 up
```

### IPC namespace

Isolates System V IPC and POSIX message queues

```bash
unshare --ipc bash
ipcs
```

### UTS namespace

Isolates hostname and domainname

```bash
unshare --uts bash
hostname <newname>
hostname
```

### User namespace

Isolates UID/GID mappings

```bash
unshare --user bash
whoami
id
```

Map to root inside namespace

```bash
unshare --map-root-user bash
whoami
id
```

### Cgroup namespace

Isolates cgroup root hierarchy

```bash
unshare --cgroup bash
cat /proc/self/cgroup
```

### Time namespace

Isolates system time (boot time, monotonic clocks)

```bash
unshare --time bash
```

### Combined namespaces

Minimal container environment

```bash
unshare --mount --pid --net --ipc --uts --fork --mount-proc bash
hostname container1
ip link set lo up
mount -t proc proc /proc
```

## Nsenter

Join an existing namespace

```bash
nsenter --target <PID> --mount --pid bash
nsenter --target <PID> --net bash
nsenter --target <PID> --all bash
```

## Lsns

List and inspect namespaces

```bash
lsns
lsns -t net
lsns -p <PID>
lsns -J
```

## /proc/\<PID\>/ns/

Inspect namespace membership of a process

```bash
ls -l /proc/<PID>/ns/
cat /proc/<PID>/uid_map
cat /proc/<PID>/gid_map
cat /proc/<PID>/setgroups
```

## User namespace UID/GID mapping

Write mapping to gain privileges inside user namespace

```bash
echo '0 <outside_uid> 1' > /proc/self/uid_map
echo '0 <outside_gid> 1' > /proc/self/gid_map
echo 'deny' > /proc/self/setgroups
```

## Persistent namespaces

Create a named network namespace that outlives the process

```bash
touch /run/netns/<name>
mount --bind /proc/<PID>/ns/net /run/netns/<name>
ip netns exec <name> <command>
```