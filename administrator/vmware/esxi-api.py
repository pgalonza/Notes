#! /usr/bin/env python3
import atexit
import ssl
import sys

import pyVmomi
from pyVim.connect import SmartConnect, Disconnect


def main():

    vmNotSuspend = ('co_app1', 'co_app2', 'co_app3', 'co_app4', 'co_db1', 'co_db2', 'co_db3', 'co_db4')
    context = None
    if hasattr(ssl, '_create_unverified_context'):
        context = ssl._create_unverified_context()
        my_cluster = SmartConnect(host='***REMOVED***', user='***REMOVED***', pwd='***REMOVED***exe20!!', port=443, sslContext=context)
    if not my_cluster:
        print("Could not connect to the specified host using specified "
              "username and password")
        return -1

    datacenter = my_cluster.content.rootFolder.childEntity[0]
    vms = datacenter.vmFolder.childEntity

    for i in vms:
        print("Virtual Machine Name:        " + i.config.name)
        print("Virtual Machine OS:          " + i.config.guestFullName)
        print("")
        #i.PowerOffVM_Task()

    Disconnect(my_cluster)


if __name__ == "__main__":
    sys.exit(main())
