#! /usr/bin/env python3

import mysql.connector as mariadb
import sys
import xml.etree.ElementTree as xml

_contact_list_name = "contacts.xml"

def main():
    structure_file('head')
    mariadb_connection = mariadb.connect(user='***REMOVED***', password='***REMOVED***exe2011', database='asterisk', host='***REMOVED***')
    cursor = mariadb_connection.cursor()

    cursor.execute("SELECT extension, name FROM users ORDER BY name ASC")

    with open(_contact_list_name, 'a') as file:
        i = 0
        for extension, name in cursor:
            i = i + 1
            line = "<contact display_name=\"{name}\" office_number=\"{number}\" mobile_number=\"\" other_number=\"\" " \
                   "line=\"{numeric}\" ring=\"\" group_id_name=\"All Contacts\" />\n".format(numeric=str(i),
                                                                                             name=name,
                                                                                             number=extension)
            file.write(line)

    structure_file('bottom')


def structure_file(position):
    # structure of files
    _contact_header = '''<?xml version=\"1.0\" encoding=\"utf-8\"?>
    <root_group>
         <group display_name=\"All Contacts\" />
    </root_group>
    <root_contact>\n'''
    _contact_bottom = "</root_contact>"

    if position == 'head':
        with open(_contact_list_name, 'w') as contact_list:
            contact_list.write(_contact_header)
    elif position == 'bottom':
        with open(_contact_list_name, 'a') as contact_list:
            contact_list.write(_contact_bottom)


if __name__ == "__main__":
    sys.exit(main())
