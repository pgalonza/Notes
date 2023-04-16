import ssl
import socket
import sys
import pprint
from time import sleep
from collections import defaultdict

_CIPHERS = ""
_HOST_NAMES = ""
_PORT = ""

def _format_ciphers(raw_string: str) -> list:
    formated_string = raw_string
    ciphers_list = None

    if formated_string[0].islower: formated_string = formated_string.upper()
    if '_' in formated_string: formated_string = formated_string.replace('_', '-')
    
    for i in ('TLS_', 'WITH_'):
        if i in formated_string: formated_string = formated_string.replace(i, '')

    for i in (':', ','):
        if i in formated_string:
            ciphers_list = formated_string.split(i)
            break
    else:
        ciphers_list = [formated_string,]
    
    return ciphers_list
        
def _format_hostnames(raw_string: str) -> list:
    formated_string = raw_string
    hosnames_list = None

    if formated_string[0].islower: formated_string = formated_string.upper()

    for i in (':', ','):
        if i in formated_string:
            hosnames_list = formated_string.split(i)
            break
    else:
        hosnames_list = [formated_string,]

    return hosnames_list

def main():
    ciphers: list = _format_ciphers(_CIPHERS)
    hosts: list = _format_hostnames(_HOST_NAMES)

    result = defaultdict(list)

    for host_name in hosts:
        for cipher_name in ciphers:
            context = ssl.create_default_context()
            context.set_ciphers(cipher_name)
            try:
                print(host_name, cipher_name)
                with socket.create_connection((host_name, _PORT)) as sock:
                    with context.wrap_socket(sock=sock, server_hostname=host_name) as ssock:
                        result[host_name].append(cipher_name + " SUCCESS")
            except:
                result[host_name].append(cipher_name + " FAILED")

            sleep(1)

    pprint.pprint(result)


if __name__ == "__main__":
    sys.exit(main())
