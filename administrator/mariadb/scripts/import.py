import sys
import csv
import copy
import mysql.connector as mariadb

_mysql_server = '***REMOVED***'
_mysql_database = 'asterisk'
_mysql_user = '***REMOVED***'
_mysql_password = '***REMOVED***exe2011'


def main():
    print('echo')
    csv_to_mysql()


def csv_to_mysql():
    mariadb_connection = mariadb.connect(user=_mysql_user, password=_mysql_password, database=_mysql_database,
                                         host=_mysql_server)
    cursor = mariadb_connection.cursor()

    with open('/home/nyanta/Downloads/users.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['name'], row['number'], row['organization'])
            cursor.execute("SELECT first_name,last_name FROM employees WHERE first_name=%s", (some_name,))
            cursor.execute("INSERT INTO accesses SET name=%s, phone=%s, organization=%s", (row['name'], row['number'], row['organization']))
    mariadb_connection.close()


if __name__ == "__main__":
    sys.exit(main())
