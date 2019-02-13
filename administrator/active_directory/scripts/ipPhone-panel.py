#! /usr/bin/env python3

import sys
import lm_auth
from ldap3 import SUBTREE
from backports import configparser


def main():
    mac_address = ('805ec0260173', '805ec02602e8', '805ec02601a3', '805ec026030a', '805ec02601ac', '805ec02601a4', '805ec02600dc', '805ec0260310', '805ec0260345')

    for mac in mac_address:
        config_lines = get_information("yealink-panel.cfg", mac)
        create_cfg_file(config_lines, mac+'.cfg')


def get_information(file_name, mac):
    service_number = {'77911': 'Техподдержка', '77900': 'Охрана'}

    conn = lm_auth.active_derectory_connector()

    config = configparser.ConfigParser()
    config.read(file_name)

    line = '#!version:1.0.0.1\n'

    for i in range(0, 20):
        number = config.get(mac, "linekey.{}.value".format(i + 1), fallback=False)

        if not number:
            continue

        conn.search(lm_auth.ad_ou_tree.get('all')[0],
                    '(&(objectCategory=person)(ipPhone=' + number + ')(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE, attributes=['displayName'])
        if not conn.entries:
            line += 'linekey.{}.label = {}\n'.format(i + 1, 'вакант')
        elif service_number.get(number, False):
            line += 'linekey.{}.label = {}\n'.format(i + 1, service_number.get(number))
        else:
            name = str(conn.entries[0].displayName).split()
            name = name[0] + ' ' + name[1][0] + "." + name[2][0] + "."
            line += 'linekey.{}.label = {}\n'.format(i + 1, name)

        line += 'linekey.{}.type = 16\n'.format(i + 1)
        line += 'linekey.{}.line = 1\n'.format(i + 1)
        line += 'linekey.{}.value = {}\n'.format(i + 1, number)

    for i in range(0, 20):
        number = config.get(mac, "expansion_module.{}.value".format(i + 1), fallback=False)

        if not number:
            continue

        conn.search(lm_auth.ad_ou_tree.get('all')[0],
                    '(&(objectCategory=person)(ipPhone=' + number + ')(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE, attributes=['displayName'])

        if not conn.entries:
            line += 'expansion_module.1.key.{}.label = {}\n'.format(i + 1, 'вакант')
        elif service_number.get(number, False):
            line += 'expansion_module.1.key.{}.label = {}\n'.format(i + 1, service_number.get(number))
        else:
            name = str(conn.entries[0].displayName).split()
            name = name[0] + ' ' + name[1][0] + "." + name[2][0] + "."
            line += 'expansion_module.1.key.{}.label = {}\n'.format(i + 1, name)

        line += 'expansion_module.1.key.{}.type = 16\n'.format(i + 1)
        line += 'expansion_module.1.key.{}.line = 1\n'.format(i + 1)
        line += 'expansion_module.1.key.{}.value = {}\n'.format(i + 1, number)

    return line


def create_cfg_file(config_lines, file_name):
    with open(file_name, 'w') as index_file:
        index_file.write(config_lines)


if __name__ == "__main__":
    sys.exit(main())
