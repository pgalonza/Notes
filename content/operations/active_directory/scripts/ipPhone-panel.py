#! /usr/bin/env python3.6
import argparse
import sys
import lm_auth
import logging
from ldap3 import SUBTREE
from backports import configparser


def main():
    mac_address = ('805ec0260173', '805ec02602e8', '805ec02601a3', '805ec026030a', '805ec02601ac', '805ec02601a4', '805ec02600dc', '805ec0260310', '805ec0260345')

    for mac in mac_address:
        path_to_file = f'{args.config}'
        logging.info(f'Get information from Active Directory for {mac}')
        config_lines = get_information(f'{path_to_file}/yealink-panel.cfg', mac)
        logging.info(f'Create config file for {mac}')
        create_cfg_file(config_lines, f'{path_to_file}/{mac}.cfg')


def get_information(file_name, mac):
    service_number = {'77911': 'Техподдержка', '77900': 'Охрана'}

    connection = lm_auth.active_derectory_connector()
    logging.debug(f'{connection}')

    logging.info(f'Read the config file {file_name}')
    config = configparser.ConfigParser()
    config.read(file_name)

    line = '#!version:1.0.0.1\n'

    for i in range(0, 30):
        number = config.get(mac, f'linekey.{i + 1}.value', fallback=False)

        logging.debug(f'Get the number from config {number}')

        if not number:
            continue

        connection.search(lm_auth.ad_ou_tree.get('all')[0],
                    f'(&(objectCategory=person)(ipPhone={number})(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE, attributes=['displayName'])
        if not connection.entries:
            line += f'linekey.{i + 1}.label = {"вакант"}\n'

        elif service_number.get(number, False):
            line += f'linekey.{i + 1}.label = {service_number.get(number)}\n'
        else:
            name = str(connection.entries[0].displayName).split()
            logging.debug(f'Get the name from number {name}')
            name = f'{name[0]} {name[1][0]}.{name[2][0]}.'
            line += f'linekey.{i + 1}.label = {name}\n'

        line += f'linekey.{i + 1}.type = 16\n'
        line += f'linekey.{i + 1}.line = 1\n'
        line += f'linekey.{i + 1}.value = {number}\n'

    for i in range(0, 40):
        number = config.get(mac, f"expansion_module.{i + 1}.value", fallback=False)

        logging.debug(f'Get the number from config {number}')

        if not number:
            continue

        connection.search(lm_auth.ad_ou_tree.get('all')[0],
                    f'(&(objectCategory=person)(ipPhone={number})(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE, attributes=['displayName'])

        if not connection.entries:
            line += f'expansion_module.1.key.{i + 1}.label = {"вакант"}\n'
        elif service_number.get(number, False):
            line += f'expansion_module.1.key.{i + 1}.label = {service_number.get(number)}\n'
        else:
            name = str(connection.entries[0].displayName).split()
            logging.debug(f'Get the name from number {name}')
            name = f'{name[0]} {name[1][0]}.{name[2][0]}.'
            line += 'expansion_module.1.key.{}.label = {}\n'.format(i + 1, name)

        line += f'expansion_module.1.key.{i + 1}.type = 16\n'
        line += f'expansion_module.1.key.{i + 1}.line = 1\n'
        line += f'expansion_module.1.key.{i + 1}.value = {number}\n'

    return line


def create_cfg_file(config_lines, file_name):
    logging.debug(f'Write the config {file_name}')
    with open(file_name, 'w') as index_file:
        index_file.write(config_lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Config for Yealink panel',
                                     formatter_class=argparse.MetavarTypeHelpFormatter)

    parser.add_argument('--log', type=str, help='Path to log file', default='/var/log/scripts')
    parser.add_argument('--debug', type=str, help='Debug level', default='info', choices=('info', 'debug'))
    parser.add_argument('--config', type=str, help='Path to xml files',
                        default='/data/provisioning/yealink/configs/co')

    args = parser.parse_args()

    debug_match = {'info': logging.INFO, 'debug': logging.DEBUG}
    logging.basicConfig(level=debug_match.get(args.debug), filename=f"{args.log}/remote-addressbook.log",
                        format='%(asctime)s %(process)d %(name)s %(levelname)s %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    sys.exit(main())
