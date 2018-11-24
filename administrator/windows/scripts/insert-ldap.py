#! /usr/bin/env python3
import csv
import json
import sys
import requests
from ldap3 import Connection, Server, SUBTREE, MODIFY_ADD, MODIFY_REPLACE
import mysql.connector as mariadb

_data = {'domain': '***REMOVED***'}
_url = 'http://pddimp.yandex.ru/api2/admin/email/list'
_headers = {'PddToken': '***REMOVED***'}
_ad_server = '***REMOVED***'
_ad_user = '***REMOVED***@***REMOVED***'
_ad_password = '***REMOVED***'
_ad_search_tree = 'ou=ЖКО № 25 (г. МО-3), ou=ZHKO28,dc=corp,dc=***REMOVED***,dc=ru'
_mysql_server = '***REMOVED***'
_mysql_database = 'asterisk'
_mysql_user = '***REMOVED***'
_mysql_password = '***REMOVED***exe2011'
_csv_file = '/home/***REMOVED***/Documents/ldap-info.csv'


def main():
    # yandex_email()
    active_directory()
    # active_directory_mysql()
    # active_directory_csv()

def yandex_email():
    r = requests.get(_url, headers=_headers, params=_data)
    # print(r.url)
    print(r.text)
    parsed_string = json.loads(r.text)
    accounts = parsed_string['accounts']

    for account in accounts:
        print(account['login'], account['fio'])


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
        print(conn.modify(dn, {'mail': [(MODIFY_REPLACE, [str(login)+'@25***REMOVED***.***REMOVED***'])]}))
        # print(conn.modify(dn, {'mail': [(MODIFY_DELETE, [str(login) + '@***REMOVED***'])]}))
        # print(conn.modify(dn, {'mail': [(MODIFY_ADD, [str(login) + '@***REMOVED***.***REMOVED***'])]}))


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


if __name__ == "__main__":
    sys.exit(main())
