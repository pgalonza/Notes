import sys
import csv
import copy
import mysql.connector as mariadb

_mysql_server = '***REMOVED***'
_mysql_database = 'menagerie'
_mysql_user = 'root'
_mysql_password = 'root'


def main():
    print('echo')
    csv_to_mysql()


def csv_to_mysql():
    mariadb_connection = mariadb.connect(user=_mysql_user, password=_mysql_password, database=_mysql_database,
                                         host=_mysql_server)
    cursor = mariadb_connection.cursor()

    with open('/home/***REMOVED***/Downloads/users.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['name'], '+'+row['number'], row['organization'], row['description'])
            if row['name'] == '':
                cursor.execute(
                    "INSERT INTO accesses SET name=%s, phone=%s, organization=%s, car_brand=%s, state_number=%s, description=%s",
                    ('unknown', '+'+row['number'], row['organization'], 'unknown', 'unknown', row['description']))
            else:
                cursor.execute(
                    "INSERT INTO accesses SET name=%s, phone=%s, organization=%s, car_brand=%s, state_number=%s, description=%s",
                    (row['name'], '+'+row['number'], row['organization'], 'unknown', 'unknown', row['description']))
    mariadb_connection.commit()
    mariadb_connection.close()


if __name__ == "__main__":
    sys.exit(main())
