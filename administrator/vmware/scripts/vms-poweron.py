#! /usr/bin/env python3
import atexit
import ssl
import sys
import pyVmomi
from pyVim.connect import SmartConnect, Disconnect

_vmware_host = ''
_vmeare_user = ''
_vmware_password = ''

def main():
    my_cluster = vmware_connector()

    datacenter = my_cluster.content.rootFolder.chilsEntity[0]


def vmware_connector():
    if hasattr(ssl, '_create_unverified_context'):
        context = ssl._create_unverified_context()
        my_cluster = SmartConnect(host=_vmware_host, user=_vmeare_user, pwd=_vmware_password, port=443,
                                  sslContext=context)

        return my_cluster


if __name__ == "__main__":
    sys.exit(main())
