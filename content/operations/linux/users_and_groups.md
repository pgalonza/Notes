---
title: User and Groups
draft: false
description: "Essential Linux user and group management commands: creation, deletion, password policies, restricted shells, group membership, and system user setup for administrators."
summary: "A practical reference for managing Linux users and groups, covering common tasks like adding users, setting up restricted shells, and verifying authentication integrity."
---

{{< toc >}}

## Sudoers

[Manual](https://man7.org/linux/man-pages/man5/sudoers.5.html)

Root without asking password

```bash
<user_name> ALL=(ALL) NOPASSWD: ALL
```

_/etc/sudoers_
Write logs

```text
Defaults  log_host, log_year, logfile="/var/log/sudo.log"
```

Run command with sudo without password

```text
notify ALL=(ALL) NOPASSWD:path_to_command, path_to_command
```

Blocks execution of external commands (e.g., shell escape from an editor).

```text
<user_name> ALL=(ALL) NOEXEC: <command>
```

Excludes the specified command/variant from the sudoers rule.

```text
<user_name> ALL=(ALL) <command>
```

## Reset password

### Mount

```bash
sudo mount /dev/<device id> /mnt
chroot /mnt /bin/bash
passwd <user name>
sudo umount -l /mnt
```

Show real and effective user and group IDs

```bash
id
```

Show last logged users

```bash
last
```

Verifies the integrity of the users and authentication information.

```bash
pwck
```

Verifies the integrity of the groups information.

```bash
newgrp
```

Change shell of user

```bash
chsh
```

Show password expiration date

```bash

chage -l <user_name>
```

Restricted Shells

```bash
useadd <user name> –s /bin/rbash
mkdir –p /home/<user name>/bin
cp /bin/ping /home/<user name>/bin
ln –s /bin/ls /home/<user name>/bin
```

## User

Create a user with defaul group and add him to other group.

```bash
useradd -m -N -g primary_group -G other_group user_name
```

Create system user

```bash
useradd --system --no-create-home -s /sbin/nologin user_name
```

Delete user

```bash
userdel <user name>
userdel –rf <user name>
```

## Group

Create group

```bash
groupadd group_name
```

Delete group

```bash
delgroup group_name
```

Make the default group

```bash
usermod -g group_name user_name
```

Add to the group

```bash
usermod -a -G group_name user_name
```

Remove user from group

```bash
usermod -R group_name user_name
```

## Sudo

Run shell as another user

```bash
sudo -iu user_name
sudo su - user_name command
sudo su user_name -s "/bin/bash"
```

Execute the previous command with sudo

```bash
sudo !!
```

Write command results to file with privileges

```bash
echo 1 | sudo tee -a privileged_file > /dev/null
```

## SU

Run shell as another user

```bash
su - user_name
su -l user_name
sudo su - user_name
```
