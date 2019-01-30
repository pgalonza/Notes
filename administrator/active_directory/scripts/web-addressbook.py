#! /usr/bin/env python3

import sys

import lm-auth
from ldap3 import SUBTREE


def main():
    for ou, origin in lm_auth.ad_ou_tree.items():
        user_list = get_information(origin)
        path_to_file = ou + '.html'
        create_html_file(user_list, path_to_file)


def get_information(origin):
    conn = lm_auth.active_derectory_connector()

    '''(&(objectCategory=person)(displayName=*)(givenName=*)(sn=*)(|(ipPhone= *)(mobile=*)(mail=*)(title=*)(
        department=*)(physicalDeliveryOfficeName=*)(company=*))(!(userAccountControl:1.2.840.113556.1.4.803:=2)))'''

    conn.search(origin,
                '(&(objectCategory=person)(displayName=*)(givenName=*)(sn=*)(|(ipPhone= *)(mobile=*)(mail=*)('
                'title=*)(department=*)(physicalDeliveryOfficeName=*)(company=*))(!('
                'userAccountControl:1.2.840.113556.1.4.803:=2)))',
                SUBTREE,
                attributes=['company', 'department', 'ipPhone', 'mobile', 'mail', 'mobile', 'title',
                            'physicalDeliveryOfficeName',
                            'displayName'])

    user_list = {}

    for entry in conn.entries:
        user_list[str(entry.displayName)] = [entry.ipPhone, entry.mobile, entry.mail, entry.title, entry.department,
                                             entry.physicalDeliveryOfficeName, entry.company]

    conn.unbind()

    return user_list


def create_html_file(user_info, file_name):
    html_structure_file('head', file_name)

    line = ''
    with open(file_name, 'a') as index_file:
        for name, user_items in sorted(user_info.items()):
            line += '''                <tr>
                    <th>{}</th>\n'''.format(name)
            for i in range(0, 7):
                if not user_items[i]:
                    line += '                    <th></th>\n'
                    continue
                line += '                    <th>{}</th>\n'.format(user_items[i])
            line += '                </tr>\n'
        index_file.write(line)
    html_structure_file('bottom', file_name)


def html_structure_file(position, file_name):
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
                    <th>Рабочий номер</th>
                    <th>E-mail</th>
                    <th>Должность</th>
                    <th>Отдел</th>
                    <th>Кабинет</th>
                    <th>Расположение</th>
                </tr>
            </thead>
            <tbody>\n'''
    _web_bottom = '''       </tbody>
        </table>
    <script>
        $(document).ready(function() {
            $('#table_cu').DataTable( {
            scrollY:        '70vh',
            scrollCollapse: true,
            paging:         false
            } );
        } );
    </script>
    <p><a href="mailto:itinfo@***REMOVED***?subject=Вопрос по web-адресной книге">Нашли ошибку?</a></p>
    </body>
    </html>'''

    if position == 'head':
        with open(file_name, 'w') as web_list:
            web_list.write(_web_header)
    elif position == 'bottom':
        with open(file_name, 'a') as web_list:
            web_list.write(_web_bottom)


if __name__ == "__main__":
    sys.exit(main())
