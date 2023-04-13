from ldap3 import Connection, Server, ALL, ALL_ATTRIBUTES
from pprint import pprint
from getpass import getpass

server = Server('<ldap port>:389', get_info=ALL)

ad_login = input('Login ')
ad_password = getpass()
search_user = input('User login: ')

connection = Connection(server=server, user='<domain>\\'+ad_login, password=ad_password, auto_bind=True)

for dc_name in ('<domain>',):
    connection.search(
        search_base=f'DC={dc_name},<domain>',
        search_filter=f'(&(objectCategory=person)(objectClass=user)(sAMAccountName={search_user}))',
        attributes=[ALL_ATTRIBUTES]
    )

    if connection.entries:
        pprint(connection.entries[0])
