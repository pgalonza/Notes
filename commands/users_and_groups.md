# Users and groups

Show real and effective user and group IDs
```
id
```

Show last logged users
```
last
```

Verifies the integrity of the users and authentication information.
```
pwck
```

Verifies the integrity of the groups information.
```
newgrp
```

Change shell of user
```
chsh
```


## User

Create a user with defaul group administrator and add him to the wheel group.
```
useradd -m -N -g primary_group -G other_group user_name
useradd --system --no-create-home -s /sbin/nologin user_name
```

Delete user
```
userdel user_name
```


## Group

Create group
```
groupadd group_name
```

Delete group
```
delgroup group_name
```

Make the default group
```
usermod -g group_name user_name
```

Remove user from group
```
usermod -R group_name user_name
```
