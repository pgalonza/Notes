#! /usr/bin/env python3
import csv
import json
import sys
import requests
from ldap3 import Connection, Server, SUBTREE, MODIFY_ADD
import mysql.connector as mariadb

_data = {'domain': '***REMOVED***'}
_url = 'http://pddimp.yandex.ru/api2/admin/email/list'
_headers = {'PddToken': '***REMOVED***'}
_ad_server = '***REMOVED***'
_ad_user = '***REMOVED***@***REMOVED***'
_ad_password = '***REMOVED***'
_ad_search_tree = 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru'
_mysql_server = ''
_mysql_database = ''
_mysql_user = ''
_mysql_password = ''
_csv_file = ''


def main():
    # yandex_email()
    active_directory()
    # active_directory_mysql()


def yandex_email():
    r = requests.get(_url, headers=_headers, params=_data)
    # print(r.url)
    print(r.text)
    parsed_string = json.loads(r.text)
    accounts = parsed_string['accounts']

    for account in accounts:
        print(account['login'], account['fio'])


def active_directory_connect():
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
    conn = active_directory_connect()
    conn.search(_ad_search_tree,
                '(&(sAMAccountName=*)(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                SUBTREE, attributes=['sAMAccountName', 'mail'])
    print(conn)
    for entry in conn.entries:
        # print(entry)
        dn = (json.loads(entry.entry_to_json())['dn'])
        login = entry.sAMAccountName
        print(login)
        # print(conn.modify(dn, {'mail': [(MODIFY_REPLACE, [str(login)+'@***REMOVED***.***REMOVED***'])]}))
        # print(conn.modify(dn, {'mail': [(MODIFY_DELETE, [str(login) + '@***REMOVED***'])]}))
        # print(conn.modify(dn, {'mail': [(MODIFY_ADD, [str(login) + '@***REMOVED***.***REMOVED***'])]}))


def active_directory_mysql():
    cursor = mysql_connector()
    conn = active_directory_connect()
    print(conn)

    cursor.execute("SELECT extension, name FROM users ORDER BY name ASC")

    for extension, name in cursor:
        print(name)
        conn.search(_ad_search_tree,
                    '(&(displayName=' + name + ')(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE, attributes=['displayName', 'ipPhone'])
        for entry in conn.entries:
            dn = (json.loads(entry.entry_to_json())['dn'])
            print(name, conn.modify(dn, {'ipPhone': [(MODIFY_ADD, [extension])]}), sep=' ')

def active_directory_csv():
    conn = active_directory_connect()
    with open(_csv_file) as csv_file:
        user_reader = csv.DictReader(csv_file)
        for row in user_reader:
            conn.search(_ad_search_tree,
                        '(&(displayName=' + row['name'] + ')(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                        SUBTREE, attributes=['displayName', 'ipPhone'])




if __name__ == "__main__":
    sys.exit(main())
