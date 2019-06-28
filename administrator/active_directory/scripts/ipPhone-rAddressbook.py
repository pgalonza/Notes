#! /usr/bin/env python3.6
import argparse
import sys
import lm_auth
import logging
from ldap3 import SUBTREE
import xml.etree.ElementTree as ET


def main():
    path_list = {}
    for ou, origin in lm_auth.ad_ou_tree.items():
        if ou == 'all':
            continue
        logging.info(f'Get information from Active Directory for {ou}')
        user_list = get_information(origin[0])
        path_to_file = f'{args.xml}/{ou}-remote.xml'
        path_list[origin[1]] = f'{args.url}/{ou}-remote.xml'
        logging.info(f'Create xml file for {ou}')
        create_xml_departament(user_list, path_to_file)
    logging.info('Create xml menu')
    create_xml_menu(path_list)


def get_information(origin):
    connection = lm_auth.active_derectory_connector()
    logging.debug(f'{connection}')
    connection.search(origin,
                      '(&(objectCategory=person)(displayName=*)(givenName=*)(ipPhone=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                      SUBTREE,
                      attributes=['ipPhone', 'displayName'])

    user_list = {}

    for entry in connection.entries:
        logging.debug(f'dictionary:\n{entry.ipPhone}\n{entry.displayName}\n')
        user_list[str(entry.displayName)] = str(entry.ipPhone).replace('-', '')

    logging.debug('Active Directory close connection')
    conn.unbind()
    return user_list


def create_xml_departament(user_info, file_path):
    root = ET.Element('YealinkIPPhoneDirectory')
    for name, number in user_info.items():
        dir_entry = ET.SubElement(root, 'DirectoryEntry')
        name_xml = ET.SubElement(dir_entry, 'Name')
        name_xml.text = name
        number_xml = ET.SubElement(dir_entry, 'Telephone')
        number_xml.text = number

    tree = ET.ElementTree(root)
    logging.debug(f'Write to file {file_path}')
    tree.write(file_path, encoding="utf-8")


def create_xml_menu(path_list):
    root = ET.Element('YealinkIPPhoneMenu')
    title = ET.SubElement(root, 'Title')
    title.text = "ФГБУ ЦЖКУ"
    for group, path in path_list.items():
        menu_item = ET.SubElement(root, 'MenuItem')
        name = ET.SubElement(menu_item, 'Name')
        name.text = group
        url = ET.SubElement(menu_item, 'URL')
        url.text = path

    tree = ET.ElementTree(root)
    logging.debug('Write to menu file')
    tree.write(f'{args.xml}/menu.xml', encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Xml remote Yealink addressbook',
                                     formatter_class=argparse.MetavarTypeHelpFormatter)

    parser.add_argument('--log', type=str, help='Path to log file', default='/var/log/scripts')
    parser.add_argument('--debug', type=str, help='debug level', default='info', choices=('info', 'debug'))
    parser.add_argument('--xml', type=str, help='Path to xml files',
                        default='/data/provisioning/yealink/configs/phone_book')
    parser.add_argument('--url', type=str, help='URL to files',
                        default='http://ip_address/configs/yealink/phone_book/')

    args = parser.parse_args()

    debug_match = {'info': logging.INFO, 'debug': logging.DEBUG}
    logging.basicConfig(level=debug_match.get(args.debug), filename=f"{args.log}/remote-addressbook.log",
                        format='%(asctime)s %(process)d %(name)s %(levelname)s %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')

    sys.exit(main())
