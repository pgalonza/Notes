#! /usr/bin/env python3.6
import argparse
import logging
import sys

import lm_auth
from ldap3 import SUBTREE


def main():
    for ou, origin in lm_auth.ad_ou_tree.items():
        logging.info(f'Get information from Active Directory for {ou}')
        user_list = get_information(origin[0])
        path_to_file = f'{args.html}/{ou}.html'
        logging.info(f'Create html file for {ou}')
        create_html_file(user_list, path_to_file)


def get_information(origin):
    conn = lm_auth.active_derectory_connector()
    logging.debug(f'{conn}')
    conn.search(origin,
                '(&(objectCategory=person)(displayName=*)(givenName=*)(sn=*)(|(ipPhone= *)(mobile=*)(mail=*)('
                'title=*)(department=*)(physicalDeliveryOfficeName=*)(company=*))(!('
                'userAccountControl:1.2.840.113556.1.4.803:=2)))',
                SUBTREE,
                attributes=['company', 'department', 'ipPhone', 'telephoneNumber', 'mobile', 'mail', 'title',
                        'physicalDeliveryOfficeName',
                        'displayName'])

    user_list = {}

    for entry in conn.entries:
        logging.debug(f'dictionary:\n{entry.company}\n{entry.department}\n{entry.ipPhone}\n{entry.telephoneNumber}\n'
                      f'{entry.mobile}\n{entry.mail}\n{entry.title}\n{entry.physicalDeliveryOfficeName}'
                      f'\n{entry.displayName}')
        user_list[str(entry.displayName)] = [str(entry.ipPhone).replace('-', ''), entry.mobile, entry.telephoneNumber, entry.mail, entry.title, entry.department,
                                             entry.physicalDeliveryOfficeName, entry.company]

    logging.debug('Active Directory close connection')
    conn.unbind()

    return user_list


def create_html_file(user_info, file_name):
    line = ''
    logging.debug('Create the head of file')
    line += html_structure_file('head', file_name)

    logging.debug('Sort the dictionary')
    for name, user_items in sorted(user_info.items()):
        line += f'''                <tr>
                    <th>{name}</th>\n'''
        for field in user_items:
            if not field or field == '[]':
                line += '                    <th></th>\n'
                continue
            line += f'                    <th>{field}</th>\n'
        line += '                </tr>\n'

    logging.debug('Create the bottom of file')
    line += html_structure_file('bottom', file_name)

    logging.debug('Write to the file')
    with open(file_name, 'w') as index_file:
        index_file.write(line)


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
                    <th>Внешний + добавочный</th>
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
    <p><a href="mailto:itinfo@local?subject=Вопрос по web-адресной книге">Нашли ошибку?</a></p>
    </body>
    </html>'''

    if position == 'head':
        return _web_header
    elif position == 'bottom':
        return _web_bottom


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Web addressbook', formatter_class=argparse.MetavarTypeHelpFormatter)

    parser.add_argument('--log', type=str, help='Path to log file', default='/var/log/scripts')
    parser.add_argument('--debug', type=str, help='debug level', default='info', choices=('info', 'debug'))
    parser.add_argument('--html', type=str, help='Path to html files', default='/data/projects/address_book/www')

    args = parser.parse_args()

    debug_match = {'info': logging.INFO, 'debug': logging.DEBUG}

    logging.basicConfig(level=debug_match.get(args.debug), filename=f"{args.log}/web-addressbook.log",
                        format='%(asctime)s %(process)d %(name)s %(levelname)s %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')

    sys.exit(main())
