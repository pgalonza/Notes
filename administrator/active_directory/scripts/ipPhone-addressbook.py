#! /usr/bin/env python3

import sys
import lm_auth
from ldap3 import SUBTREE, Server, Connection
import xml.etree.ElementTree as xml


def main():
    for ou, origin in lm_auth.ad_ou_tree.items():
        if ou == 'all':
            continue
        user_list = get_information(origin[0], origin[1])
        path_to_file = ou + '.xml'
        create_xml_file(user_list, path_to_file, origin[1])
    get_all_information()


def get_information(origin, group_name):
    if group_name == "ВКС":
        conn = lm_auth.active_derectory_connector_vks()
        conn.search('dc=vks,dc=zhky,dc=ru',
                    '(&(objectCategory=person)(displayName=*)(givenName=*)(ipPhone=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE,
                    attributes=['ipPhone', 'displayName'])
    else:
        conn = lm_auth.active_derectory_connector()
        conn.search(origin,
                    '(&(objectCategory=person)(displayName=*)(givenName=*)(ipPhone=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE,
                    attributes=['ipPhone', 'displayName'])

    user_list = {}

    for entry in conn.entries:
        user_list[str(entry.displayName)] = [str(entry.ipPhone).replace('-', ''), group_name]

    if not group_name == 'Все' and not group_name == 'ЦУ':
        conn.search('ou=co,dc=corp,dc=zhky,dc=ru',
                    '(&(objectCategory=person)(displayName=*)(givenName=*)(ipPhone=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE,
                    attributes=['ipPhone', 'displayName'])

        for entry in conn.entries:
            user_list[str(entry.displayName)] = [str(entry.ipPhone).replace('-', ''), 'ЦУ']

    conn.unbind()

    return user_list


def get_all_information():
    ou_list = ''
    user_list = ''

    for ou, origin in lm_auth.ad_ou_tree.items():
        if ou == 'all':
            continue

        if origin[1] == "ВКС":
            conn = lm_auth.active_derectory_connector_vks()
            conn.search('dc=,dc=,dc=',
                        '(&(objectCategory=person)(displayName=*)(givenName=*)(ipPhone=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                        SUBTREE,
                        attributes=['ipPhone', 'displayName'])
        else:
            conn = lm_auth.active_derectory_connector()
            conn.search(origin[0],
                        '(&(objectCategory=person)(displayName=*)(givenName=*)(ipPhone=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                        SUBTREE,
                        attributes=['ipPhone', 'displayName'])

        ou_list += '   <group display_name=\"{}\" />\n'.format(origin[1])
        for entry in conn.entries:
            user_list += "  <contact display_name=\"{}\" office_number=\"{}\" mobile_number=\"\" other_number=\"\" line=\"1\" " \
                         "ring=\"\" group_id_name=\"{}\" />\n".format(entry.displayName, str(entry.ipPhone).replace('-', ''), origin[1])

    create_all_xml_file(ou_list, user_list)


def create_xml_file(user_info, file_name, group_name):
    line = ''
    line += '''<?xml version=\"1.0\" encoding=\"utf-8\"?>
<root_group>\n'''

    line += '   <group display_name=\"{}\" />\n'.format(group_name)
    if not group_name == 'Все' and not group_name == 'ЦУ':
        line += '   <group display_name=\"ЦУ\" />\n'
    line += '''</root_group>
<root_contact>\n'''

    for name, number in user_info.items():
        line += "   <contact display_name=\"{}\" office_number=\"{}\" mobile_number=\"\" other_number=\"\" line=\"1\" " \
                "ring=\"\" group_id_name=\"{}\" />\n".format(name, number[0], number[1])

    line += "</root_contact>"

    with open(file_name, 'w') as index_file:
        index_file.write(line)


def create_all_xml_file(ou_list, user_list):
    line = ''
    line += '''<?xml version=\"1.0\" encoding=\"utf-8\"?>
<root_group>\n'''
    line += ou_list
    line += '''</root_group>
<root_contact>\n'''
    line += user_list
    line += "</root_contact>"
    with open('all.xml', 'w') as index_file:
        index_file.write(line)


if __name__ == "__main__":
    sys.exit(main())
