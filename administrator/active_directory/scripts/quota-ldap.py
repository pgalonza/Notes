#! /usr/bin/env python3

import json
import sys
from ldap3 import Connection, Server, SUBTREE

_ad_server = ''
_ad_user = ''
_ad_password = ''
_ad_search_tree = 'dc=,dc=,dc='
_ad_ou = ('CO')


def main():
    active_directory()


def active_directory_connector():
    server = Server(_ad_server)
    conn = Connection(server, user=_ad_user, password=_ad_password)
    conn.bind()
    return conn


def active_directory():
    conn = active_directory_connector()
    print(conn)
    for ou in _ad_ou:
        _ad_search_tree = 'ou='+ou+',dc=,dc=,dc='
        conn.search(_ad_search_tree,
                    '(&(mail=*)(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE, attributes=['sAMAccountName', 'division', 'mail'])

        print('')
        print(ou)
        print('++++++++++++++++')
        for entry in conn.entries:
            # print(entry)
            dn = (json.loads(entry.entry_to_json())['dn'])
            login = entry.sAMAccountName
            division = entry.division
            mail = entry.mail
            if division != "2G":
                print(login, mail, division)
    conn.unbind()


if __name__ == "__main__":
    sys.exit(main())
