#! /usr/bin/env python3
import argparse
import json
import logging
import sys
import csv
import lm_auth
import re

from ldap3 import SUBTREE, MODIFY_REPLACE


def main():
    logging.debug('active directory connection')
    socket = lm_auth.active_derectory_connector()
    logging.debug(f'{socket}')
    ou = lm_auth.ad_ou_tree.get('all')[0]
    logging.debug(f'ou {ou}')
    users = {}

    try:
        logging.debug(f'Open file: {args.csv1}')
        with open(args.csv1, 'r') as csv_file:
            logging.debug(f'Read file: {args.csv1}')
            user_reader = csv.DictReader(csv_file)
            i = 0
            for row in user_reader:
                name = name_normalization(row['name'])
                if name is None:
                    logging.info(f'Bad line {row["name"]}')
                    continue
                else:
                    name = name.group(0).rstrip()
                    logging.debug(f'Group and Rstrip {name}')

                logging.info(f"Search {name}")
                result = get_information_ad(socket, ou, name)
                if not args.dismissed:
                    if len(result) > 1:
                        i = i + 1
                        logging.info(f'Multiple entries: {len(result)}')
                        print("Search returned multiple entries:", i, name)
                    elif not result:
                        i = i + 1
                        logging.info('No entries')
                        print("Search returned no entries:", i, name)
                else:
                    if result:
                        i = i + 1
                        logging.debug(f'Search {name} in dictionary {name not in users}')
                        if name not in users:
                            logging.debug(f'{name} not in the list')
                            branch = re.search(r'domain\.domain\.local\/(\w{2,4})\b', str(result[0].canonicalName))
                            users[name] = [branch.group(1), result[0].lastLogon, result[0].lastLogonTimestamp]
                        else:
                            logging.debug(f'{name} is in the list')
                            continue
                        # print("Search returned entries:", i, name)
                        logging.info('Have entries')
    except FileNotFoundError:
        logging.error('File not found')
        sys.exit(0)

    try:
        with open(args.csv2, 'r') as csv_file:
            logging.debug(f'Read file: {args.csv2}')
            user_reader = csv.DictReader(csv_file)
            for row in user_reader:
                name = name_normalization(row['name'])
                if name is None:
                    logging.info(f'Bad line {row["name"]}')
                    continue
                else:
                    name = name.group(0).rstrip()
                    logging.debug(f'Group and Rstrip {name}')
                logging.debug(f'Search {name} in dictionary {name not in users.keys()}')

                if name in users.keys():
                    logging.info(f'{name} user is working')
                    logging.debug(f'Delete {name}')
                    users.pop(name)
    except FileNotFoundError:
        logging.error('File not found')
        sys.exit(0)

    if users:
        try:
            with open('disabled-users.csv', 'w', newline='') as csvfile:
                fieldnames = ['name', 'branch', 'lastLogon', 'lastLogonTimestamp']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                i = 0
                for user, data in users.items():
                    i = i + 1
                    writer.writerow(
                        {'name': user, 'branch': data[0], 'lastLogon': data[1], 'lastLogonTimestamp': data[2]})
                    print('Dismissed user', i, user, data[0])
        except FileNotFoundError:
            logging.error('No such file')
            sys.exit(0)

        print("Block this users?")
    logging.info('Whait the choice')
    choice = input('Are you sure? (y/n): ').lower().strip()[:1]
    logging.debug(f'The choice is {choice}')
    if choice == "n":
        logging.info('Exit')
        sys.exit(1)
    elif choice == 'y':
        for user in users.keys():
            result = user_disabling(socket, ou, user)
            logging.info(f'Block user user {user} {result}')
        print('Successfully!')

    socket.unbind()


def get_information_ad(connection, origin, user):
    logging.debug(f'Active directory search {user}')
    connection.search(origin,
                      f'(&(objectCategory=person)(displayName={user})(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                      SUBTREE,
                      attributes=['displayName', 'lastLogon', 'lastLogonTimestamp', 'canonicalName'])
    logging.debug(f'Result {connection.entries}')
    return connection.entries


def name_normalization(line):
    logging.debug(f'Normalization {line}')
    if line.islower() or line.isupper():
        line = line.title()
        logging.debug(f'Title {line}')
    if len(line.split()) == 2:
        logging.info(f"Two words {line}")
        return None
    else:
        result = re.search(r'([А-ЯЁ][а-яё]+[\-\s]?){3,}', line)
        logging.debug(f'Regular {result}')
    return result


def user_disabling(connection, origin, user):
    logging.debug('active directory search')
    connection.search(origin,
                      f'(&(objectCategory=person)(displayName={user})(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                      SUBTREE,
                      attributes=['userAccountControl'])
    dn = json.loads(connection.entries[0].entry_to_json())['dn']
    result = connection.modify(dn, {'userAccountControl': [(MODIFY_REPLACE, [66050])]})
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check user in active directory',
                                     formatter_class=argparse.MetavarTypeHelpFormatter)

    parser.add_argument('--log', type=str, help='path to log file', default='')
    parser.add_argument('--debug', type=str, help='debug level', default='info', choices=('info', 'debug'))
    parser.add_argument('--csv1', type=str, help='path to file')
    parser.add_argument('--csv2', type=str, help='path to file')
    parser.add_argument('--dismissed', help='dismissed users', action='store_true')

    args = parser.parse_args()

    debug_match = {'info': logging.INFO, 'debug': logging.DEBUG}

    logging.basicConfig(level=debug_match.get(args.debug), filename=f"{args.log}/check-useser.log",
                        format='%(asctime)s %(process)d %(name)s %(levelname)s %(funcName)s %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    sys.exit(main())
