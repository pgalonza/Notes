#! /usr/bin/env python3
import sys
import time
import subprocess


def main():
    # print (subprocess.Popen("regedit", shell = True))
    subprocess.call("net stop \"1C:Enterprise 8.3 Server Agent (x86-64)\"", shell=True)
    time.sleep(10)
    subprocess.call("taskkill \IM  rphost.exe \F", shell=True)


if __name__ == "__main__":
    sys.exit(main())
