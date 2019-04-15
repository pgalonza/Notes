#! /usr/bin/env python3
import sys

import paramiko

def main():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('', username='', password='')
    stdin, stdout, stderr = ssh .exec_command("vim-cmd vmsvc/getallvms")
    print(stdout.readlines())


if __name__ == "__main__":
    sys.exit(main())
