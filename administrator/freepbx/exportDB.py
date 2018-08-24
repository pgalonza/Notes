#! /usr/bin/env python3

import mysql.connector as mariadb
import sys
import xml.etree.ElementTree as xml

_contact_list_name = "contacts.xml"
_web_list_name = "index.html"


def main():
    structure_file('head')
    mariadb_connection = mariadb.connect(user='', password='', database='asterisk', host='')
    cursor = mariadb_connection.cursor()

    cursor.execute("SELECT extension, name FROM users ORDER BY name ASC")

    with open(_contact_list_name, 'a') as lFile:
        with open(_web_list_name, 'a') as wFile:
            i = 0
            for extension, name in cursor:
                i = i + 1
                l_line = "<contact display_name=\"{name}\" office_number=\"{number}\" mobile_number=\"\" " \
                         "other_number=\"\" line=\"{numeric}\" ring=\"\" group_id_name=\"Центральное управление\" />\n".format(numeric=str(i), name=name, number=extension)
                w_line = '''        <tr>
            <th>{name}</th>
            <th>{number}</th>
        </tr>\n'''.format(name=name, number=extension)

                lFile.write(l_line)
                wFile.write(w_line)

    structure_file('bottom')


def structure_file(position):
    # structure of files
    _contact_header = '''<?xml version=\"1.0\" encoding=\"utf-8\"?>
    <root_group>
         <group display_name=\"Центральное управление\" />
    </root_group>
    <root_contact>\n'''
    _contact_bottom = "</root_contact>"

    _web_header = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <title>Справочник</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
    <link rel="stylesheet" href="Bootstrap-4-4.1.1/css/bootstrap.css">
    <link rel="stylesheet" href="DataTables-1.10.18/css/dataTables.bootstrap4.min.css">
    <script type="text/javascript" src="jQuery-3.3.1/jquery-3.3.1.min.js"></script>
    <script type="text/javascript" src="DataTables-1.10.18/js/jquery.dataTables.min.js"></script>
    <script type="text/javascript" src="DataTables-1.10.18/js/dataTables.bootstrap4.min.js"></script>
</head>
<body>
    <table id="table_cu" class="table table-striped table-bordered" style="width:100%">
        <thead>
            <tr>
                <th>ФИО</th>
                <th>Внутренний номер</th>
            </tr>
        </thead>
        <tbody>\n'''
    _web_bottom = '''       </tbody>
        <tfoot>
            <tr>
                <th>ФИО</th>
                <th>Внутренний номер</th>
            </tr>
        </tfoot>
    </table>
<script>
    $(document).ready(function() {
        $('#table_cu').DataTable( {
        scrollY:        '50vh',
        scrollCollapse: true,
        paging:         false
        } );
    } );
</script>
</body>
</html>'''

    if position == 'head':
        with open(_contact_list_name, 'w') as contact_list:
            contact_list.write(_contact_header)
        with open(_web_list_name, 'w') as web_list:
            web_list.write(_web_header)

    elif position == 'bottom':
        with open(_contact_list_name, 'a') as contact_list:
            contact_list.write(_contact_bottom)
        with open(_web_list_name, 'a') as web_list:
            web_list.write(_web_bottom)


if __name__ == "__main__":
    sys.exit(main())
