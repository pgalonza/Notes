#! /usr/bin/env python3

import sys
import lm_auth
from ldap3 import SUBTREE
import xml.etree.ElementTree as xml


def main():
    for ou, origin in lm_auth.ad_ou_tree.items():
        user_list = get_information(origin, ou)
        path_to_file = ou + '.xml'
        create_xml_file(user_list, path_to_file, ou)


def get_information(origin, group_name):
    conn = lm_auth.active_derectory_connector()

    conn.search(origin,
                '(&(objectCategory=person)(displayName=*)(givenName=*)(sn=*)(ipPhone=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                SUBTREE,
                attributes=['ipPhone', 'displayName'])

    user_list = {}

    for entry in conn.entries:
        user_list[str(entry.displayName)] = [entry.ipPhone, group_name]

    if not group_name == 'all' | 'co':
        conn.search(origin,
                    '(&(objectCategory=person)(displayName=*)(givenName=*)(sn=*)(ipPhone=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE,
                    attributes=['ipPhone', 'displayName'])

        for entry in conn.entries:
            user_list[str(entry.displayName)] = [entry.ipPhone, group_name]

    conn.unbind()

    return user_list


def create_xml_file(user_info, file_name, group_name):
    line = ''
    line += '''<?xml version=\"1.0\" encoding=\"utf-8\"?>
<root_group>
    <group display_name=\"{}\" />
</root_group>
<root_contact>\n'''.format(group_name)

    for name, number in user_info.items():
        print(name, 'test')
        line += "   <contact display_name=\"{}\" office_number=\"{}\" mobile_number=\"\" other_number=\"\" line=\"1\" "\
                "ring=\"\" group_id_name=\"{}\" />\n".format(name, number, group_name)

    line += "</root_contact>"

    with open(file_name, 'w') as index_file:
        index_file.write(line)


def xml_structure_file(position, file_name):
    _contact_header = '''<?xml version=\"1.0\" encoding=\"utf-8\"?>
        <root_group>
             <group display_name=\"Центральное управление\" />
        </root_group>
        <root_contact>\n'''
    _contact_bottom = "</root_contact>"


if __name__ == "__main__":
    sys.exit(main())
