#! /usr/bin/env python3

import csv
import json
import re
import subprocess
import sys
import lm_auth
import argparse
import paramiko
import logging
import time

from ldap3 import SUBTREE, MODIFY_REPLACE

_user_objects = None


class Extension:

    def __init__(self, name, old_number):
        self.name = name
        self.old_number = old_number

    new_number = None
    password = None
    ip = None
    mac = None


def main():
    global _user_objects
    logging.info(f'Database is {args.database}')
    if args.database == 'ad':
        logging.info(f'OU {lm_auth.ad_ou_tree.get(args.ad_ou)[0]}')
        logging.info('Get information ad')
        _user_objects = get_information_ad(lm_auth.ad_ou_tree.get(args.ad_ou)[0])
    elif args.database == 'mysql':
        logging.info('Get information from MySQL')
        _user_objects = get_information_mysql()
    else:
        logging.info('Invalid parameter')

    if args.reboot_yealink:
        logging.info('Reboot yealink phones')
        yealink_reboot()
        sys.exit(0)

    logging.info('Get new numbers from CSV file')
    new_list = get_information_csv_new()

    logging.info('Find new number for users')
    for name_object, user_object in _user_objects.items():
        logging.debug(f'Find user in new list with name: {name_object}')
        result = new_list.get(name_object)
        logging.debug(f'Search result: {result}')
        if result:
            user_object.new_number = result
            user_object.password = args.salt + result
            logging.debug(f'Check data from object:\nNew: {user_object.new_number},\nOld:{user_object.old_number}'
                          f'\nSecret:{user_object.password}')
        else:
            logging.info(f'Have not new number: {name_object}')

    logging.info('Find IP-Phone IP-address')
    find_ip()
    logging.info('Find IP-Phone MAC')
    find_mac()
    logging.debug('Create IP-Phone provision config')
    create_cfg()
    logging.info('Create FreePBX bulk handler')
    create_bulk_file()
    logging.info('Replace number in active directory')
    replace_number_ad(lm_auth.ad_ou_tree.get(args.ad_ou)[0])


def get_information_ad(origin):
    logging.debug('active directory connection')
    conn = lm_auth.active_derectory_connector()
    logging.debug(f'{conn}')
    conn.search(origin,
                '(&(objectCategory=person)(ipPhone=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                SUBTREE,
                attributes=['ipPhone', 'displayName'])
    logging.debug('active directory search')
    conn_entries = conn.entries
    logging.debug(f'{conn_entries}')
    logging.debug('active directory close connection')
    conn.unbind()

    users = {}
    for entry in conn_entries:
        logging.debug(f'dictionary {entry.displayName} {entry.ipPhone}')
        users[entry.displayName] = Extension(entry.displayName, entry.ipPhone)
    return users


def get_information_mysql():
    logging.debug('mysql connection asterisk database')
    mariadb_connection = lm_auth.mariadb_connector('asterisk')
    cursor = mariadb_connection.cursor()
    logging.debug(f'database cursor {cursor}')
    logging.debug('sql select')
    cursor.execute("SELECT extension, name FROM users ORDER BY name ASC")
    logging.debug(f'select result {cursor}')
    users = {}
    for extension, name in cursor:
        logging.debug(f'create object {name} {extension}')
        users[name] = Extension(name, extension)
    return users


def get_information_csv_new():
    logging.debug('Convert csv file')
    convert_csv(args.new_list)
    users = {}
    logging.debug(f'Open file: {args.new_list}')
    try:
        with open(args.new_list) as csv_file:
            logging.debug(f'Read file: {args.new_list}')
            user_reader = csv.DictReader(csv_file)
            for row in user_reader:
                logging.debug(f'Data from file to dictionary: {row}')
                users[row['name']] = row['number']
    except FileNotFoundError:
        logging.info(f'Cannot open the file: {args.new_list}')
        sys.exit(0)
    return users


def convert_csv(file):
    logging.debug(f'Open: {file}')
    try:
        with open(file, 'r') as contacts:
            logging.debug(f'Change \";\" to \",\": {file}')
            convert_data = contacts.read().replace(';', ',')
        with open(file, 'w') as contacts:
            logging.debug(f'Write changes to file: {file}')
            contacts.write(convert_data)
    except FileNotFoundError:
        logging.info(f'Cannot open the file: {file}')
        sys.exit(0)




def find_ip():
    logging.debug('Connect to Asterisk host with SSH')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=args.asterisk_host, port=args.asterisk_port, username=args.asterisk_username, password=args.asterisk_password)
    except paramiko.ssh_exception.AuthenticationException:
        logging.info(f'Cannot connect to remote host: {args.asterisk_host}')
        sys.exit(0)

    logging.debug(f'SSH client {client}')
    logging.debug('Create SSH session')
    logging.debug('Send the command: /usr/sbin/asterisk -rx \"sip show peers\"')
    stdin, stdout, stderr = client.exec_command("/usr/sbin/asterisk -rx \"sip show peers\"")
    stringout = stdout.read().decode('ascii')
    stringerr = stderr.read().decode('ascii')
    logging.debug(f'Output\nSTDOUT: {stringout},\nSTDERR:{stringerr}')
    client.close()

    for name_object, user_object in _user_objects.items():
        for line in stringout.splitlines():
            if line.find(user_object.old_number) == 0:
                logging.debug(f'Search SIP IP: {user_object.old_number}')
                ip_address = re.search(r'([0-9]{1,3}[\\.]){3}[0-9]{1,3}', line)
                logging.debug(f'Search result: {ip_address}')
                if ip_address:
                    user_object.ip = ip_address.group()
                    logging.debug(f'Check data from object:\n{name_object}\n{user_object.ip}')


def find_mac():
    for name_object, user_object in _user_objects.items():
        logging.debug(f'Search mac by IP: {user_object.ip}')
        if user_object.ip:
            result = str(subprocess.check_output(['sudo', 'nmap', '-sP', '-n', user_object.ip]))
            mac = re.search(r'..:..:..:..:..:..', result)
            logging.debug(f'Search result: {mac}')
            if mac:
                logging.debug('Delete symbol: \':\'')
                user_object.mac = mac.group(0).replace(':', '').lower()
                logging.debug(f'Check data from object:\n{name_object}\n{user_object.mac}')


def create_cfg():
    for name_object, user_object in _user_objects.items():
        #logging.debug(f'Check data from object:\nMAC: {user_object.mac}\nNew extension: {user_object.new_number}\n'
        #              f'Old Extension: {user_object.old_number},\nSecret: {user_object.password}')
        try:
            if user_object.mac and user_object.new_number:
                with open(user_object.mac + '.cfg', 'w') as config_file:
                    config = '''#!version:1.0.0.1
account.1.label = {phone}
account.1.display_name = {phone}
account.1.user_name = {phone}
account.1.auth_name = {phone}
account.1.password = {password}'''.format(phone=user_object.new_number,
                                              password=user_object.password)
                    config_file.write(config)
            elif user_object.new_number and user_object.password:
                with open(user_object.new_number + '.cfg', 'w') as config_file:
                    config = '''#!version:1.0.0.1
account.1.label = {phone}
account.1.display_name = {phone}
account.1.user_name = {phone}
account.1.auth_name = {phone}
account.1.password = {password}'''.format(phone=user_object.old_number,
                                              password=user_object.password)
                    config_file.write(config)
        except FileNotFoundError:
            logging.info(f'Cannot open the file: {user_object.mac}')
            sys.exit(0)


def replace_number_ad(origin):
    logging.debug(f'OU {origin}')
    logging.debug('Active directory connection')
    conn = lm_auth.active_derectory_connector()
    logging.debug(f'{conn}')
    logging.debug('Search user in active directory by IP-phone number')
    for name_object, user_object in _user_objects.items():
        conn.search(origin,
                    f'(&(objectCategory=person)(displayName={user_object.name})(!('
                    f'userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE,
                    attributes=['ipPhone', 'displayName', 'telephoneNumber'])
        if not conn.entries:
            continue
        logging.debug(f'Search result ipPhone: {conn.entries[0].displayName}')
        dn = (json.loads(conn.entries[0].entry_to_json())['dn'])
        logging.debug(f'Change number {user_object.old_number} to {user_object.new_number} for {user_object.name}')
        print(conn.modify(dn, {'ipPhone': [(MODIFY_REPLACE, [user_object.new_number])]}))
        print(conn.modify(dn, {'telephoneNumber': [(MODIFY_REPLACE, [user_object.new_number])]}))
    conn.unbind()


def yealink_reboot():
    logging.debug('Connect to Asterisk host with SSH')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=args.asterisk_host, port=args.asterisk_port, username=args.asterisk_username,
                       password=args.asterisk_password)
    except paramiko.ssh_exception.AuthenticationException:
        logging.info(f'Cannot connect to remote host: {args.asterisk_host}')
        sys.exit(0)

    logging.debug(f'SSH client {client}')
    logging.debug('Create SSH session')
    for name_object, user_object in _user_objects.items():
        logging.debug(f'Send the command: /usr/sbin/asterisk -rx \"sip notify reboot-yealink {user_object.old_number}\"')
        stdin, stdout, stderr = client.exec_command(f"/usr/sbin/asterisk -rx \"sip notify reboot-yealink {user_object.old_number}\"")
        stringout = stdout.read().decode('ascii')
        stringerr = stderr.read().decode('ascii')
        logging.debug(f'Output\nSTDOUT: {stringout},\nSTDERR:{stringerr}')
        time.sleep(5)
    client.close()


def create_bulk_file():
    logging.debug(f'Open file: {args.bulk}')
    try:
        with open(args.bulk, 'w') as export_list:
            fieldnames = ['extension', 'password', 'name', 'voicemail', 'ringtimer', 'noanswer', 'recording',
                          'outboundcid',
                          'sipname', 'noanswer_cid', 'busy_cid', 'chanunavail_cid', 'noanswer_dest', 'busy_dest',
                          'chanunavail_dest',
                          'mohclass', 'id', 'tech', 'dial', 'devicetype', 'user', 'description', 'emergency_cid',
                          'hint_override',
                          'recording_in_external', 'recording_out_external', 'recording_in_internal',
                          'recording_out_internal',
                          'recording_ondemand', 'recording_priority', 'answermode', 'intercom', 'cid_masquerade',
                          'concurrency_limit',
                          'accountcode', 'allow', 'avpf', 'callerid', 'canreinvite', 'context', 'defaultuser', 'deny',
                          'disallow', 'dtmfmode',
                          'encryption', 'force_avp', 'host', 'icesupport', 'mailbox', 'namedcallgroup',
                          'namedpickupgroup',
                          'nat', 'permit',
                          'port', 'qualify', 'qualifyfreq', 'rtcp_mux', 'secret', 'sendrpid', 'sessiontimers',
                          'sipdriver',
                          'transport',
                          'trustrpid', 'type', 'videosupport', 'vmexten', 'callwaiting_enable', 'findmefollow_strategy',
                          'findmefollow_grptime',
                          'findmefollow_grppre', 'findmefollow_grplist', 'findmefollow_annmsg_id',
                          'findmefollow_postdest',
                          'findmefollow_dring',
                          'findmefollow_needsconf', 'findmefollow_remotealert_id', 'findmefollow_toolate_id',
                          'findmefollow_ringing',
                          'findmefollow_pre_ring', 'findmefollow_voicemail', 'findmefollow_calendar_id',
                          'findmefollow_calendar_match',
                          'findmefollow_changecid', 'findmefollow_fixedcid', 'findmefollow_enabled', 'voicemail_enable',
                          'voicemail_vmpwd',
                          'voicemail_email', 'voicemail_pager', 'voicemail_options', 'voicemail_same_exten',
                          'disable_star_voicemail',
                          'vmx_unavail_enabled', 'vmx_busy_enabled', 'vmx_temp_enabled', 'vmx_play_instructions',
                          'vmx_option_0_number',
                          'vmx_option_1_number', 'vmx_option_2_number']
            writer = csv.DictWriter(export_list, fieldnames=fieldnames)
            logging.debug(f'Write headers: {fieldnames}')
            writer.writeheader()
            for name_object, user_object in _user_objects.items():
                if not user_object.new_number and not user_object.password:
                    continue
                writer.writerow(
                        {'extension': user_object.new_number, 'password': '', 'name': user_object.name, 'voicemail': 'default',
                         'ringtimer': '18',
                         'noanswer': '',
                         'recording': '', 'outboundcid': '', 'sipname': '', 'noanswer_cid': '', 'busy_cid': '',
                         'chanunavail_cid': '',
                         'noanswer_dest': '', 'busy_dest': '', 'chanunavail_dest': '', 'mohclass': 'default',
                         'id': user_object.new_number,
                         'tech': 'sip',
                         'dial': 'SIP/' + user_object.new_number, 'devicetype': 'fixed', 'user': user_object.new_number,
                         'description': user_object.name,
                         'emergency_cid': '',
                         'hint_override': '', 'recording_in_external': 'dontcare', 'recording_out_external': 'dontcare',
                         'recording_in_internal': 'dontcare', 'recording_out_internal': 'dontcare',
                         'recording_ondemand': 'dontcare',
                         'recording_priority': '10', 'answermode': 'disabled', 'intercom': 'enabled',
                         'cid_masquerade': user_object.new_number,
                         'concurrency_limit': '0', 'accountcode': '', 'allow': '', 'avpf': 'no',
                         'callerid': user_object.name + ' <' + user_object.new_number + '>',
                         'canreinvite': 'no', 'context': 'from-internal', 'defaultuser': '', 'deny': '0.0.0.0/0.0.0.0',
                         'disallow': '',
                         'dtmfmode': 'rfc2833', 'encryption': 'no', 'force_avp': 'no', 'host': 'dynamic', 'icesupport': 'no',
                         'mailbox': user_object.new_number + '@device', 'namedcallgroup': '', 'namedpickupgroup': '',
                         'nat': 'no',
                         'permit': '0.0.0.0/0.0.0.0',
                         'port': '5060', 'qualify': 'yes', 'qualifyfreq': '60', 'rtcp_mux': 'no',
                         'secret': user_object.password,
                         'sendrpid': 'pai',
                         'sessiontimers': 'accept', 'sipdriver': 'chan_sip', 'transport': 'udp,tcp,tls', 'trustrpid': 'yes',
                         'type': 'friend',
                         'videosupport': 'inherit', 'vmexten': '', 'callwaiting_enable': 'ENABLED',
                         'findmefollow_strategy': 'ringallv2-prim',
                         'findmefollow_grptime': '20', 'findmefollow_grppre': '',
                         'findmefollow_grplist': user_object.new_number,
                         'findmefollow_annmsg_id': '0',
                         'findmefollow_postdest': 'ext-local,' + user_object.new_number + ',dest', 'findmefollow_dring': '',
                         'findmefollow_needsconf': '',
                         'findmefollow_remotealert_id': '0', 'findmefollow_toolate_id': '0', 'findmefollow_ringing': 'Ring',
                         'findmefollow_pre_ring': '7', 'findmefollow_voicemail': 'default', 'findmefollow_calendar_id': '',
                         'findmefollow_calendar_match': 'yes', 'findmefollow_changecid': 'default', 'findmefollow_fixedcid': '',
                         'findmefollow_enabled': '', 'voicemail_enable': 'no', 'voicemail_vmpwd': '', 'voicemail_email': '',
                         'voicemail_pager': '',
                         'voicemail_options': 'attach=no|saycid=no|envelope=no|delete=no', 'voicemail_same_exten': 'yes',
                         'disable_star_voicemail': 'no', 'vmx_unavail_enabled': 'blocked', 'vmx_busy_enabled': 'blocked',
                         'vmx_temp_enabled': 'blocked', 'vmx_play_instructions': '1', 'vmx_option_0_number': '',
                         'vmx_option_1_number': '',
                         'vmx_option_2_number': ''})
    except FileNotFoundError:
        logging.info(f'Cannot open the file: {args.bulk}')
        sys.exit(0)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(process)d %(name)s %(levelname)s %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')

    parser = argparse.ArgumentParser(description='Change number', formatter_class=argparse.MetavarTypeHelpFormatter)
    parser.add_argument('--database', type=str, help='mysql, active directory, csv', default='ad',
                        choices=('ad', 'mysql', 'csv'))
    parser.add_argument('--ad-ou', dest='ad_ou', type=str, help='active directory ou', choices=(''))
    parser.add_argument('--salt', type=str, help='salt + number', default='fpbx')
    parser.add_argument('--bulk', type=str, help='bulk handler for freepbx', default='freepbx.csv')
    parser.add_argument('--new-list', dest='new_list', type=str, help='csv file with new number',
                        default='handbook.csv')
    parser.add_argument('--asterisk-host', dest='asterisk_host', type=str, help='asterisk ip', default='127.0.0.1')
    parser.add_argument('--asterisk-username', dest='asterisk_username', type=str, help='asterisk ssh username', default='root')
    parser.add_argument('--asterisk-password', dest='asterisk_password', type=str, help='asterisk ssh password',
                        default='')
    parser.add_argument('--ssh-port', dest='asterisk_port', type=int, help='asterisk ssh port', default=22)
    parser.add_argument('--reboot-yealink', dest='reboot_yealink', help='reboot yealink', action='store_true')

    args = parser.parse_args()

    sys.exit(main())
