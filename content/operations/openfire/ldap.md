---
title: "LDAP"
draft: false
---

Users in group

```text
(&(objectClass=group)(|(cn=group_name)(cn=group_name)))
```

Users

```text
(objectClass=user)(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2))
```

Groups

```text
(&(objectClass=user)(objectCategory=person)(|(memberOf=cn=group_name,ou=,ou=,dc=,dc=,dc=))(!(userAccountControl:1.2.840.113556.1.4.803:=2)))
```
