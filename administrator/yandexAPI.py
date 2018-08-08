#! /usr/bin/env python3

import sys
import requests
import json
from ldap3 import Connection, Server, ANONYMOUS, SIMPLE, SYNC, ASYNC

_data = {'domain': '***REMOVED***'}
_url = 'http://pddimp.yandex.ru/api2/admin/email/list'
_headers = {'PddToken': '***REMOVED***'}


def main():
    yandex_email()


def yandex_email():
    r = requests.get(_url, headers=_headers, params=_data)
    # print(r.url)
    print(r.text)
    parsed_string = json.loads(r.text)
    accounts = parsed_string['accounts']

    for account in accounts:
        print(account['login'], account['fio'])

def active_directory():



if __name__ == "__main__":
    sys.exit(main())
