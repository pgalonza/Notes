#! /usr/bin/env python3

import mysql.connector as mariadb
import sys
import xml.etree.ElementTree as xml

_contact_list_name = "contacts.xml"
_web_list_name = "index.html"


def main():
    structure_file('head')
    mariadb_connection = mariadb.connect(user='***REMOVED***', password='***REMOVED***exe2011', database='asterisk', host='***REMOVED***')
    cursor = mariadb_connection.cursor()

    cursor.execute("SELECT extension, name FROM users ORDER BY name ASC")

    with open(_contact_list_name, 'a') as lFile:
        with open(_web_list_name, 'a') as wFile:
            i = 0
            for extension, name in cursor:
                i = i + 1
                l_line = "<contact display_name=\"{name}\" office_number=\"{number}\" mobile_number=\"\" " \
                         "other_number=\"\" line=\"{numeric}\" ring=\"\" group_id_name=\"Центральное управление\" />\n".format(numeric=str(i), name=name, number=extension)
                w_line = '''                                <tr class="row100 body">
                                    <td class="cell100 column1">{name}</td>
                                    <td class="cell100 column2">{number}</td>
                                </tr>\n'''.format(numeric=str(i), name=name, number=extension)

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
    <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
    <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
    <link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">
    <link rel="stylesheet" type="text/css" href="css/util.css">
    <link rel="stylesheet" type="text/css" href="css/main.css">
</head>
<body>
    <div class="limiter">
        <div class="container-table100">
            <div class="wrap-table100">
                <div class="table100 ver1 m-b-110">
                    <div class="table100-head">
                        <table>
                            <thead>
                                <tr class="row100 head">
                                    <th class="cell100 column1">ФИО</th>
                                    <th class="cell100 column2">Внутренний номер</th>
                                </tr>
                            </thead>
                        </table>
                    </div>
                    <div class="table100-body js-pscroll">
                        <table>
                            <tbody>\n'''
    _web_bottom = '''                           </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="vendor/jquery/jquery-3.2.1.min.js"></script>
    <script src="vendor/bootstrap/js/popper.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.min.js"></script>
    <script src="vendor/select2/select2.min.js"></script>
    <script src="vendor/perfect-scrollbar/perfect-scrollbar.min.js"></script>
    <script>
        $('.js-pscroll').each(function(){
            var ps = new PerfectScrollbar(this);
        
            $(window).on('resize', function(){
                ps.update();
            })
        });
    </script>
    <script src="js/main.js"></script>
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
