import sys
import lm_auth
import csv
from ldap3 import SUBTREE


def main():
    choice = 'all'
    if choice == 'all':
        for ou, origin in lm_auth.ad_ou_tree.items():
            if ou == 'all':
                continue
            user_list = get_information(origin[0])
            create_csv_file(user_list, ou)

    else:
        user_list = get_information(lm_auth.ad_ou_tree.get(choice)[0])
        create_csv_file(user_list, choice)


def get_information(origin):
    conn = lm_auth.active_derectory_connector()
    conn.search(origin,
                '(&(objectCategory=person)(mail=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                SUBTREE,
                attributes=['mail', 'displayName'])
    conn_entries = conn.entries
    conn.unbind()

    return conn_entries


def create_csv_file(user_list, file_name):
    with open(file_name + '.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'mail']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in user_list:
            writer.writerow({'name': entry.displayName, 'mail': entry.mail})


if __name__ == "__main__":
    sys.exit(main())
