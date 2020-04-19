import sys
import socket
import re

def main():
    host = '10.0.207.21'
    port = 3333
    regex = '/CLIP: ".(7\d{10})"/m'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.error as msg:
        sys.exit(msg)

    while True:
        data = s.recv(128)
        if not data:
            continue
        print(data.decode().rstrip('\n'))
        print(data)


if __name__ == "__main__":
    sys.exit(main())