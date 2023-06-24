---
title: User and Groups
draft: false
description: "CLI commands for get information about users and groups"
---

{{< toc >}}

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
