#! /usr/bin/env python3

import sys
from ldap3 import Server, Connection

_ad_server = ''
_ad_user = ''
_ad_password = ''

_ad_server_vks = ''
_ad_user_vks = ''
_ad_password_vks = ''
_ad_ou_tree_vks = 'dc=,dc=,dc='

ad_ou_tree = {'all': ('dc=,dc=,dc=','Все')}

def active_derectory_connector_vks():
    server = Server(_ad_server_vks)
    conn = Connection(server, user=_ad_user_vks, password=_ad_password_vks)
    conn.bind()
    return conn

def active_derectory_connector():
    server = Server(_ad_server)
    conn = Connection(server, user=_ad_user, password=_ad_password)
    conn.bind()
    return conn


if __name__ == "__main__":
    sys.exit()
