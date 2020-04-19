#! /usr/bin/env python3

import json
import sys
from ldap3 import Connection, Server, SUBTREE
import lm_auth


def main():
    for ou, origin in lm_auth.ad_ou_tree.items():
        if ou == 'all':
            continue
        get_information(origin[0], origin[1])


def get_information(origin, group_name):
    connection = lm_auth.active_derectory_connector()

    connection.search(origin,
                '(&(mail=*)(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                SUBTREE, attributes=['sAMAccountName', 'division', 'mail'])

    print('')
    print(group_name)
    print('++++++++++++++++')
    for entry in connection.entries:
        # print(entry)
        #dn = (json.loads(entry.entry_to_json())['dn'])
        login = entry.sAMAccountName
        division = entry.division
        mail = entry.mail
        if division != "2G" and division != "2g":
            print(login, mail, division)
    connection.unbind()


if __name__ == "__main__":
    sys.exit(main())
