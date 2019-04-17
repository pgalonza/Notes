# LDAP filters

###### Users in group
```
(&(objectClass=group)(|(cn=group_name)(cn=group_name)))
```

###### Users
```
(objectClass=user)(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2))
```

###### Groups
```
(&(objectClass=user)(objectCategory=person)(|(memberOf=cn=group_name,ou=,ou=,dc=,dc=,dc=))(!(userAccountControl:1.2.840.113556.1.4.803:=2)))
```
