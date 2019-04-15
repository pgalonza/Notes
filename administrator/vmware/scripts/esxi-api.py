#! /usr/bin/env python3
import atexit
import ssl
import sys
import time

import pyVmomi
from pyVim.connect import SmartConnect, Disconnect

_vmware_host = ''
_vmeare_user = ''
_vmware_password = ''
#_vm_not_suspend = ('co_app1', 'co_app2', 'co_app3', 'co_app4', 'co_db1', 'co_db2', 'co_db3', 'co_db4', 'co_srv_dev')
_vm_suspend = ('co_device1', 'co_elasticsearch1', 'co_helpdesk2', 'co_kibana1', 'co_logstash1', 'co_proxy1', 'Server_test', 'co_test1', 'co_helpdesk1', 'co_rusguard1', 'co_test_win7', 'co_srv_av')
#_vm_suspend = ('co_device1')

def main():
    my_cluster = vmware_connector()

    datacenter = my_cluster.content.rootFolder.childEntity[0]
    vms = datacenter.vmFolder.childEntity

    for vm in vms:
        """
        if vm.config.name in vm_not_suspend:
            continue
        """
        if vm.config.name not in _vm_suspend:
            continue

        if vm.summary.runtime.powerState != 'poweredOn':
            continue
        elif vm.summary.runtime.powerState == 'poweredOn' and vm.summary.guest.toolsStatus != 'toolsOk':
            vm.SuspendVM_Task()
            print("Suspend:        " + vm.config.name)
        else:
            vm.ShutdownGuest()
            print("Poweroff:        " + vm.config.name)

        #print(vm.summary.runtime.powerState)
        #print(vm.summary.guest.toolsStatus)
        # print(vm.config)
        # print("Virtual Machine Name:        " + vm.config.name)
        # print("Virtual Machine OS:          " + vm.config.guestFullName)
        # print("Virtual Machine UUID:        " + vm.config.uuid)
        # print("")
        # !vm.PowerOffVM_Task()!#
        # !vm.SuspendVM_Task()!
        # !vm.ShutdownGuest()!#

    # !datacenter.ShutdownHost_Task()!
    # time.sleep(15)
    print("PowerOff: " + str(datacenter))
    Disconnect(my_cluster)


def vmware_connector():
    if hasattr(ssl, '_create_unverified_context'):
        context = ssl._create_unverified_context()
        my_cluster = SmartConnect(host=_vmware_host, user=_vmeare_user, pwd=_vmware_password, port=443,
                                  sslContext=context)

    return my_cluster


if __name__ == "__main__":
    sys.exit(main())
