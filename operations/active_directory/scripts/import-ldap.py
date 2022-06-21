#! /usr/bin/env python3
import csv
import json
import sys
import requests
from ldap3 import Connection, Server, SUBTREE, MODIFY_ADD, MODIFY_REPLACE
import mysql.connector as mariadb

_data_connect = {'fields': 'name, email, is_dismissed', 'per_page': 1500}
_url_connect = 'https://api.directory.yandex.net/v6/users/'
_headers_connect = {'Authorization': 'OAuth ', 'X-Org-ID': '', 'Accept': 'application/json'}
_ad_server = '
_ad_user = ''
_ad_password = ''
_ad_search_tree = 'ou=, ou=,dc=,dc=,dc='
_mysql_server = ''
_mysql_database = 'asterisk'
_mysql_user = ''
_mysql_password = ''
_csv_file = 'ldap-info.csv'


def main():
    # yandex_email()
    active_directory()
    # active_directory_mysql()
    # active_directory_csv()

def yandex_email():
    r_get = requests.get(_url_connect, headers=_headers_connect, params=_data_connect)
    parsed_string = r_get.json()
    print(parsed_string['per_page'], parsed_string['total'], parsed_string['pages'])
    accounts = parsed_string['result']
    i = 0
    for account in accounts:
        i = i + 1
        print(i, account['email'],  account['id'])
        headers_connect = {'Authorization': 'OAuth ', 'X-Org-ID': '', 'Content-type': 'application/json'}
        print('https://api.directory.yandex.net/v6/users/'+str(account['id'])+'/')
        r_patch = requests.patch('https://api.directory.yandex.net/v6/users/'+str(account['id'])+'/', headers=headers_connect, json={'is_enabled': False})
        print(r_patch)
        print(r_patch.json())


def active_directory_connector():
    server = Server(_ad_server)
    conn = Connection(server, user=_ad_user, password=_ad_password)
    conn.bind()
    return conn


def mysql_connector():
    mariadb_connection = mariadb.connect(user=_mysql_user, password=_mysql_password, database=_mysql_database,
                                         host=_mysql_server)
    cursor = mariadb_connection.cursor()
    return cursor


def active_directory():
    conn = active_directory_connector()
    conn.search(_ad_search_tree,
                '(&(sAMAccountName=*)(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                SUBTREE, attributes=['sAMAccountName', 'mail'])
    print(conn)
    for entry in conn.entries:
        # print(entry)
        dn = (json.loads(entry.entry_to_json())['dn'])
        login = entry.sAMAccountName
        print(login)
        print(conn.modify(dn, {'mail': [(MODIFY_REPLACE, [str(login)+'@'])]}))
        # print(conn.modify(dn, {'mail': [(MODIFY_DELETE, [str(login) + '@'])]}))
        # print(conn.modify(dn, {'mail': [(MODIFY_ADD, [str(login) + '@'])]}))
    conn.unbind()


def active_directory_mysql():
    cursor = mysql_connector()
    conn = active_directory_connector()
    print(conn)

    cursor.execute("SELECT extension, name FROM users ORDER BY name ASC")

    for extension, name in cursor:
        print(name)
        conn.search(_ad_search_tree,
                    '(&(displayName=' + name + ')(objectCategory=person)(!('
                                               'userAccountControl:1.2.840.113556.1.4.803:=2)))', SUBTREE,
                    attributes=['displayName', 'ipPhone', 'telephoneNumber'])
        for entry in conn.entries:
            dn = (json.loads(entry.entry_to_json())['dn'])
            print("ipPhone", conn.modify(dn, {'ipPhone': [(MODIFY_ADD, [extension])]}), sep=' ')
            print("telephoneNumber", conn.modify(dn, {'telephoneNumber': [(MODIFY_ADD, [extension])]}), sep=' ')
    conn.unbind()

def active_directory_csv():
    conn = active_directory_connector()
    with open(_csv_file) as csv_file:
        user_reader = csv.DictReader(csv_file)
        for row in user_reader:
            #print (row['name'])
            status = conn.search(_ad_search_tree,
                        '(&(displayName=' + row[
                            'name'] + ')(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                        SUBTREE,
                        attributes=['displayName', 'mobile', 'company', 'department', 'physicalDeliveryOfficeName',
                                    'title'])
            if not status:
                print(row['name'])
            """"
            for entry in conn.entries:
                dn = (json.loads(entry.entry_to_json())['dn'])
                print('department:', conn.modify(dn, {'department': [(MODIFY_ADD, [row['department']])]}), sep=' ')
                print('title', conn.modify(dn, {'title': [(MODIFY_ADD, [row['position']])]}), sep=' ')
                print('company', conn.modify(dn, {'company': [(MODIFY_ADD, ['Центральное управление'])]}), sep=' ')
                if row['mobile']:
                    print('mobile', conn.modify(dn, {'mobile': [(MODIFY_ADD, [row['mobile']])]}), sep=' ')
                if row['room']:
                    print('physicalDeliveryOfficeName', conn.modify(dn, {'physicalDeliveryOfficeName': [(MODIFY_ADD, [row['room']])]}), sep=' ')
            """
    conn.unbind()

if __name__ == "__main__":
    sys.exit(main())
