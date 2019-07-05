#! /usr/bin/env python3.6
import argparse
import sys
import lm_auth
import logging
from ldap3 import SUBTREE


def main():
    for ou, origin in lm_auth.ad_ou_tree.items():
        if ou == 'all':
            continue
        logging.info(f'Get information from Active Directory for {ou}')
        user_list = get_information(origin[0], origin[1])
        path_to_file = f'{args.xml}/{ou}.xml'
        logging.info(f'Create xml file for {ou}')
        create_xml_file(user_list, path_to_file, origin[1])


def get_information(origin, group_name):
    connection = lm_auth.active_derectory_connector()
    logging.debug(f'{connection}')
    connection.search(origin,
                '(&(objectCategory=person)(displayName=*)(givenName=*)(ipPhone=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                SUBTREE,
                attributes=['ipPhone', 'displayName'])

    user_list = {}

    for entry in connection.entries:
        user_list[str(entry.displayName)] = [str(entry.ipPhone).replace('-', ''), group_name]

    if not group_name == 'Все' and not group_name == 'ЦУ':
        connection.search('ou=co,dc=corp,dc=zhky,dc=ru',
                    '(&(objectCategory=person)(displayName=*)(givenName=*)(ipPhone=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE,
                    attributes=['ipPhone', 'displayName'])

        for entry in connection.entries:
            logging.debug(f'dictionary:\n{entry.ipPhone}\n{entry.displayName}\n')
            user_list[str(entry.displayName)] = [str(entry.ipPhone).replace('-', ''), 'ЦУ']

    logging.debug('Active Directory close connection')
    connection.unbind()

    return user_list


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

    logging.debug(f'Write to file {file_name}')
    with open(file_name, 'w') as index_file:
        index_file.write(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Xml local Yealink addressbook', formatter_class=argparse.MetavarTypeHelpFormatter)

    parser.add_argument('--log', type=str, help='Path to log file', default='/var/log/scripts')
    parser.add_argument('--debug', type=str, help='Debug level', default='info', choices=('info', 'debug'))
    parser.add_argument('--xml', type=str, help='Path to xml files',
                        default='/data/provisioning/yealink/configs/phone_book')

    args = parser.parse_args()

    debug_match = {'info': logging.INFO, 'debug': logging.DEBUG}
    logging.basicConfig(level=debug_match.get(args.debug), filename=f"{args.log}/remote-addressbook.log",
                        format='%(asctime)s %(process)d %(name)s %(levelname)s %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')

    sys.exit(main())
