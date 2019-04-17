###### Create a user with defaul group administrator and add him to the wheel group.
```
useradd -m -N -g primary_group -G other_group user_name

useradd -s /sbin/nologin -d /usr/lib/"service"  user_name
```

###### Create group
```
groupadd group_name
```

###### Delete group
```
delgroup group_name
```

###### Delete user
```
userdel user_name
```

###### Add user to group
```
usermod -a -G group_name user_name
```

###### Make the default group
```
usermod -g group_name user_name
```

###### Remove user from group
```
usermod -R group_name user_name
```
