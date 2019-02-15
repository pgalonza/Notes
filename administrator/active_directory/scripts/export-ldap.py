import sys
import lm_auth
import csv
from ldap3 import SUBTREE


def main():
    user_list = get_information()
    create_csv_file(user_list)


def get_information():
    conn = lm_auth.active_derectory_connector()
    conn.search(lm_auth.ad_ou_tree.get('***REMOVED***')[0],
                '(&(objectCategory=person)(mail=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                SUBTREE,
                attributes=['mail', 'displayName'])
    conn_entries = conn.entries
    conn.unbind()

    return conn_entries


def create_csv_file(user_list):
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'mail']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in user_list:
            writer.writerow({'name': entry.displayName, 'mail': entry.mail})


if __name__ == "__main__":
    sys.exit(main())
