#! /usr/bin/env python3

import sys
from ldap3 import Server, Connection

_ad_server = '***REMOVED***'
_ad_user = '***REMOVED***@***REMOVED***'
_ad_password = '***REMOVED***'
ad_ou_tree = {'all': 'dc=corp,dc=***REMOVED***,dc=ru', 'co': 'ou=co,dc=corp,dc=***REMOVED***,dc=ru',
               '***REMOVED***': 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***': 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru',
               '***REMOVED***': 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***': 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru',
               '***REMOVED***': 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***': 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru',
               '***REMOVED***': 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***': 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru',
               '***REMOVED***': 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***': 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru',
               '***REMOVED***': 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***': 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru',
               '***REMOVED***': 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru', '***REMOVED***': 'ou=***REMOVED***,dc=corp,dc=***REMOVED***,dc=ru'}


def active_derectory_connector():
    server = Server(_ad_server)
    conn = Connection(server, user=_ad_user, password=_ad_password)
    conn.bind()
    return conn


if __name__ == "__main__":
    sys.exit()
