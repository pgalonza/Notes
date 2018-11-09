#! /usr/bin/env python3
import sys
import os
import subprocess


def main():
    # print (subprocess.Popen("regedit", shell = True))
    subprocess.call("net stop \"MSSQLSERVER\"", shell=True)


if __name__ == "__main__":
    sys.exit(main())
