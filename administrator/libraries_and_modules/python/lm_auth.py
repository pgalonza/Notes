#! /usr/bin/env python3

import sys
from ldap3 import Server, Connection

_ad_server = ''
_ad_user = ''
_ad_password = ''

_ad_server_***REMOVED*** = ''
_ad_user_***REMOVED*** = ''
_ad_password_***REMOVED*** = ''
_ad_ou_tree_***REMOVED*** = 'dc=***REMOVED***,dc=***REMOVED***,dc=ru'

ad_ou_tree = {'all': ('dc=corp,dc=***REMOVED***,dc=ru','Все'), 'co': ('ou=co,dc=corp,dc=***REMOVED***,dc=ru', '.ЦУ'),
               '***REMOVED***': ('ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***'), '***REMOVED***': ('ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***'),
               '***REMOVED***': ('ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***'), '***REMOVED***': ('ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***'),
               '***REMOVED***': ('ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***'), '***REMOVED***': ('ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***'),
               '***REMOVED***': ('ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***'), '***REMOVED***': ('ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***'),
               '***REMOVED***': ('ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***'), '***REMOVED***': ('ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***'),
               '***REMOVED***': ('ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***'), '***REMOVED***': ('ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***'),
               '***REMOVED***': ('ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***'), '***REMOVED***': ('ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***')}

def active_derectory_connector_***REMOVED***():
    server = Server(_ad_server_***REMOVED***)
    conn = Connection(server, user=_ad_user_***REMOVED***, password=_ad_password_***REMOVED***)
    conn.bind()
    return conn

def active_derectory_connector():
    server = Server(_ad_server)
    conn = Connection(server, user=_ad_user, password=_ad_password)
    conn.bind()
    return conn


if __name__ == "__main__":
    sys.exit()
