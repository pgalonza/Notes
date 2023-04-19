---
title: "Roundcube"
draft: false
---

## PLUGINS

_config.inc.php_

```php
$config['plugins'] = array('managesieve', 'enigma');
```

## lobal LDAP address book.

_config.inc.php_

```php
$config['ldap_public']["global_ldap_abook"] = array(
    'name'              => 'Global LDAP Address Book',
    'hosts'             => array('host'),
    'port'              => 389,
    'use_tls'           => false,
    'ldap_version'      => '3',
    'network_timeout'   => 10,
    'user_specific'     => true,
    // Search mail users under same domain.
    //'base_dn'       => 'domainName=%d,o=domains,dc=,dc=,dc=',
    //'bind_dn'       => 'mail=%u@%d,ou=Users,domainName=%d,o=domains,dc=,dc=,dc=',
    'base_dn'       => 'dc=,dc=,dc=',
    'bind_dn'       => 'user',
    'bind_pass'     => 'password',
    'hidden'        => false,
    'searchonly'    => false,
    'writable'      => false,
    'search_fields' => array('mail', 'cn', 'sn', 'givenName', 'street', 'telephoneNumber', 'mobile', 'stree', 'postalCode'),
    // mapping of contact fields to directory attributes
    'fieldmap' => array(
        'name'          => 'cn',
        'surname'       => 'sn',
        'firstname'     => 'givenName',
        'title'         => 'title',
        'email'         => 'mail:*',
        'phone:work'    => 'telephoneNumber',
        'phone:mobile'  => 'mobile',
        'phone:workfax' => 'facsimileTelephoneNumber',
        'street'        => 'street',
        'zipcode'       => 'postalCode',
        'locality'      => 'l',
        'department'    => 'departmentNumber',
        'notes'         => 'description',
        'photo'         => 'jpegPhoto',
    ),
    'sort'          => 'cn',
    'scope'         => 'sub',
    //'filter'        => '(&(enabledService=mail)(enabledService=deliver)(enabledService=displayedInGlobalAddressBook)(|(objectClass=mailUser)(objectClass=mailList)(objectClass=mailAlias))(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
    'filter'        => '(&(mail=*)(objectClass=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
    'fuzzy_search'  => true,
    'vlv'           => false,   // Enable Virtual List View to more efficiently fetch paginated data (if server supports it)
    'sizelimit'     => '0',     // Enables you to limit the count of entries fetched. Setting this to 0 means no limit.
    'timelimit'     => '0',     // Sets the number of seconds how long is spend on the search. Setting this to 0 means no limit.
    'referrals'     => false,  // Sets the LDAP_OPT_REFERRALS option. Mostly used in multi-domain Active Directory setups
```

```php
    'group_filters' => array(
        'departments' => array(
            'name'    => 'Mailing Lists',
            'scope'   => 'sub',
            //'base_dn' => 'domainName=%d,o=domains,dc=,dc=,dc=',
            'base_dn' => 'dc=,dc=,dc=',
            'filter'  => '(&(objectClass=group)(mail=*))',
            'name_attr' => 'cn',
            'email'     => 'mail',
        ),
    ),
);
```

```php
$config['autocomplete_addressbooks'] = array('sql', 'global_ldap_abook');
```

_defaults.inc.php_ _config.inc.php_

```php
$config['drafts_mbox'] = 'Черновики';
$config['junk_mbox'] = 'Нежелательная почта';
$config['sent_mbox'] = 'Отправленные';
$config['trash_mbox'] = 'Удаленные';
$config['create_default_folders'] = yes;
```

## Autocomplete

_rcmail_output_html.php_

```php
$user_attrib = $autocomplete > 0 ? array() : array('autocomplete' => 'on');
$host_attrib = $autocomplete > 0 ? array() : array('autocomplete' => 'on');
$pass_attrib = $autocomplete > 1 ? array() : array('autocomplete' => 'on');
```

_config.inc.php_

```php
$config['login_autocomplete'] = 2;
```
