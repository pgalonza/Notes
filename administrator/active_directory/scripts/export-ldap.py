import csv
import json
import sys

from ldap3 import Server, Connection, SUBTREE

_ad_server = '***REMOVED***'
_ad_user = '***REMOVED***@***REMOVED***'
_ad_password = '***REMOVED***'
_ad_search_tree = 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru'
_export_file_name = "active-directory.csv"


def main():
    get_information()


def active_derectory_connector():
    server = Server(_ad_server)
    conn = Connection(server, user=_ad_user, password=_ad_password)
    conn.bind()
    return conn


def get_information():
    conn = active_derectory_connector()

    conn.search(_ad_search_tree, '(&(mail=*)(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                SUBTREE, attributes=['displayName', 'mail'])

    users_list = {}
    for entry in conn.entries:
        # dn = json.loads(entry.entry_to_json()['dn'])
        # print(entry.sAMAccountName, entry.mail)
        users_list[str(entry.displayName)] = str(entry.mail)
    for name, mail in users_list.items():
        print(name, mail)
    csv_format(users_list)


def csv_format(export_list):
    with open(_export_file_name, 'a') as export_file:
        field_names = ['name', 'mail']
        writer = csv.DictWriter(export_file, fieldnames=field_names)
        writer.writeheader()
        for name, mail in export_list.items():
            writer.writerow({'name': name, 'mail': mail})


if __name__ == "__main__":
    sys.exit(main())
