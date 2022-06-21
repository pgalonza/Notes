#! /usr/bin/env python3.6
import argparse
import sys
import logging
import paramiko
import os


def main():
    logging.info(f'Ringing to {args.number} with event {args.body}')

    local_file = f"{args.local_path}/{args.number}.call"
    remote_file = f"{args.remote_path}/{args.number}.call"
    logging.debug(f'{local_file}\n{remote_file}')

    key = paramiko.RSAKey.from_private_key_file(args.ssh_key)
    logging.debug(f'RSA key {key}')

    logging.debug('Connect to Asterisk host with SSH')
    client = paramiko.SSHClient()
    client.load_system_host_keys()

    try:
        client.connect(hostname=args.asterisk_host, port=22, username=args.asterisk_username,
                       password=args.asterisk_password, pkey=key)
    except paramiko.ssh_exception.AuthenticationException:
        logging.info(f'Cannot connect to remote host: {args.asterisk_host}')
        sys.exit(0)

    logging.debug(f'SSH client {client}')

    sftp = client.open_sftp()

    logging.debug(f'SFTP client {client}')

    try:
        with open(local_file, 'w') as file:
            call_file = f'''Channel: SIP/trunk_name/{args.number}
Context: zabbix
MaxRetries: 10
RetryTime: 60
WaitTime: 30
CallerID: Zabbix
Extension: s
Priority: 1
Set: MESSAGE={args.subject}'''

            logging.debug(f'Write file\n{call_file}')

            file.write(call_file)
    except FileNotFoundError:
        logging.info(f'Cannot open the file: {local_file}')
        sys.exit(0)

    logging.debug(f'Put {local_file} to {remote_file}')
    sftp.put(local_file, remote_file)
    logging.debug('Close SFTP')
    sftp.close()

    logging.debug('Chown')
    client.exec_command(f'sudo chown notify:asterisk {remote_file}')
    logging.debug('Move call file to /var/spool/asterisk/outgoing/')
    client.exec_command(f'mv {remote_file} /var/spool/asterisk/outgoing/')
    logging.debug('Close SSH')
    client.close()
    logging.debug('Delete file')
    os.remove(remote_file)

    logging.info(f'Call to {args.number} OK')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Zabbix alert via asterisk',
                                     formatter_class=argparse.MetavarTypeHelpFormatter)

    parser.add_argument('--log', type=str, help='path to log file', default='/var/lib/zabbix')
    parser.add_argument('--debug', type=str, help='debug level', default='info', choices=('info', 'debug'))
    parser.add_argument('--subject', type=str, help='subject',
                        choices=('conditioner', 'temperature', 'power'))
    parser.add_argument('--body', type=str, help='body')
    parser.add_argument('--number', type=str, help='number to notify')
    parser.add_argument('--local-path', dest='local_path', type=str, help='path to create call file', default='/tmp')
    parser.add_argument('--remote-path', dest='remote_path', type=str, help='path to create call file', default='/home/notify')
    parser.add_argument('--asterisk-host', dest='asterisk_host', type=str, help='asterisk ip', default='')
    parser.add_argument('--asterisk-username', dest='asterisk_username', type=str, help='asterisk ssh username',
                        default='notify')
    parser.add_argument('--asterisk-password', dest='asterisk_password', type=str, help='asterisk ssh password',
                        default='')
    parser.add_argument('--ssh-port', dest='asterisk_port', type=int, help='asterisk ssh port', default=22)
    parser.add_argument('--ssh-key', dest='ssh_key', type=str, help='private key file', default='/usr/lib/zabbix/alertscripts/notify_rsa')

    args = parser.parse_args()

    debug_match = {'info': logging.INFO, 'debug': logging.DEBUG}
    logging.basicConfig(level=debug_match.get(args.debug), filename=f"{args.log}/sip-notify.log",
                        format='%(asctime)s %(process)d %(name)s %(levelname)s %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')

    sys.exit(main())
