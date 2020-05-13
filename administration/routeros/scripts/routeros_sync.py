#! /usr/bin/env python3
import argparse
import os
import sys
import time

from git import Repo
import datetime
import re
import logging
import paramiko


def main():
    ros_ip = ('', '')
    ros_config = ('ppp', 'interface', 'ip', 'queue', 'radius', 'snmp', 'system')

    ros_master, ros_slave = determine_vrrp_status(ros_ip)
    logging.info(f'Master is:\n{ros_master}\Slave is:\n{ros_slave}')

    logging.info(f'Get config files from master {ros_master}')
    get_master_config(ros_master, ros_config)

    repo = Repo('')
    # print(repo.git.diff('HEAD', '--unified=0', 'co/ppp-sync.cfg.rsc'))
    git_status = repo.git.status('--short', 'co')
    logging.debug(f'Git status:\n{git_status}')
    if not git_status:
        logging.info('Configuration not changed')
        print('Not changed')
        sys.exit()

    logging.info('Configuration is changed')

    commit_time = datetime.datetime.now()

    patch_list = []

    git_diff = repo.git.diff('HEAD', '--unified=0', 'co')
    logging.debug(f'Git diff:\n{git_diff}')

    ros_remove = re.findall('-(/([a-z]*)\s.*\r)', git_diff)
    logging.debug(f'Remove lines:\n{ros_remove}')
    if ros_remove:
        print('Remove\n', ros_remove)
        logging.debug('Convert rows')
        remove_meta_list = line_to_list(ros_remove)

        for meta_config in remove_meta_list:
            logging.debug(f'Meta config {meta_config}')
            result = convert_config(meta_config)
            logging.debug(f'{result}')

            if result:
                patch_list.append(result)

    ros_add = re.findall('\+(/([a-z]*)\s.*\r)', git_diff)
    logging.debug(f'Add lines:\n{ros_remove}')
    if ros_add:
        print('New\n', ros_add)
        for meta_config in ros_add:
            patch_list.append(meta_config[0])

    logging.info('Create the patch file')
    make_patch_file(patch_list)

    logging.info('Add file to the index')
    #repo.git.add('co')
    logging.info('Commit the changes')
    #repo.git.commit(commit_time.strftime("-m Sync %Y-%m-%d %H:%M:%S"))
    logging.info('Push changes to repository')
    # repo.git.push()

    execute_patch(ros_slave)


def line_to_list(roc):
    list_roc = []
    for line_config in roc:
        logging.debug(f'Line {line_config}')
        line_roc = [line_config[0]]
        split_config = re.split('\s', line_config[0].rstrip())
        logging.debug(f'Split {split_config}')

        for item in split_config:
            if item != 'add' and item != 'set':
                line_roc.append(item)
            else:
                list_roc.append(line_roc)
                break
    return list_roc


def make_patch_file(patch):
    try:
        with open('patch.cfg.rsc', 'w') as patch_file:
            for line in patch:
                logging.debug(f'Write line {line}')
                patch_file.write(line)
            patch_file.write('/file remove patch.cfg.rsc\r')
    except FileNotFoundError:
        logging.error(f'Cannot open the file: {patch_file}')
        #sys.exit(0)


def execute_patch(slave_address):
    logging.debug('Connect to routeros host with SSH')
    for ip in slave_address:
        logging.debug(f'Connect to slave {ip}')
        ssh_client = connect_ros(ip)
        if not ssh_client:
            continue

        sftp = ssh_client.open_sftp()

        logging.debug(f'SFTP client {sftp}')

        logging.debug('Upload patch file')
        sftp.put('patch.cfg.rsc', 'patch.cfg.rsc')
        logging.debug('Close SFTP')
        sftp.close()
        time.sleep(1)
        logging.debug(f'Execute patch')
        ssh_client.exec_command('import file=patch.cfg.rsc')
        ssh_stdin, ssh_stdout, ssh_stder = ssh_client.exec_command(':local check [:len [/file find name=patch.cfg.rsc]]; :put (check);')
        #print('exec', int(ssh_stdout.read().decode()))
        if int(ssh_stdout.read().decode()):
            logging.error(f'Execute problem')
            ssh_client.exec_command('/file remove patch.cfg.rsc')

        ssh_client.close()
    logging.debug('Remove patch file')
    #os.remove('patch.cfg.rsc')


def get_master_config(ip, config_path):
    ssh_client = connect_ros(ip)
    for path in config_path:
        logging.debug(f'Export config file {path}')
        ssh_client.exec_command(f'/{path} export terse verbose file={path}-sync.cfg')
        time.sleep(1)
        sftp = ssh_client.open_sftp()
        logging.debug(f'SFTP client {sftp}')

        logging.debug(f'Download file')
        sftp.get(f'{path}-sync.cfg.rsc', f'{path}-sync.cfg.rsc')
        time.sleep(1)
        logging.debug('Close SFTP')
        sftp.close()

        try:
            with open(f'{path}-sync.cfg.rsc', 'r') as config_file:
                config_line = config_file.readlines()
                #print('rw',config_line)
                #config_file.writelines(config_line[4:])
        except FileNotFoundError:
            logging.error(f'Cannot open the file: {config_file}')
            # sys.exit(0)
        try:
            with open(f'{path}-sync.cfg.rsc', 'w') as config_file:
                config_file.writelines(config_line[5:])
        except FileNotFoundError:
            logging.error(f'Cannot open the file: {config_file}')
            # sys.exit(0)


    logging.debug(f'Remove config files')
    ssh_client.exec_command('/file remove [find name~"-sync.cfg.rsc"]')
    logging.debug('Close SSH')
    ssh_client.close()


def connect_ros(ip):
    key = paramiko.RSAKey.from_private_key_file('routeros')
    logging.debug(f'RSA key {key}')

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        logging.debug(f'Connect to {ip}')
        client.connect(hostname=ip, port=args.ssh_port, username='routeros',
                       password='', pkey=key)
    except paramiko.ssh_exception.AuthenticationException:
        logging.info(f'Cannot authentication to remote host: {ip}')
        return None
    except paramiko.ssh_exception.NoValidConnectionsError:
        logging.info(f'Cannot connect to remote host: {ip}')
        return None
    else:
        logging.debug(f'SSH client {client}')
        return client


def determine_vrrp_status(ros_address):
    master_ip = None
    slave_ip = []
    for ip in ros_address:
        client = connect_ros(ip)
        if not client:
            continue

        # ssh_stdin, ssh_stdout, ssh_stder = client.exec_command(':foreach i in=[/interface vrrp find] do={ :put [/interface vrrp get $i name]; }')
        # vrrp_list = re.split('\r\n', ssh_stdout.read().decode().rstrip())
        # for vrrp in vrrp_list:
        ssh_stdin, ssh_stdout, ssh_stder = client.exec_command('put [interface vrrp get vrrp1 master]')
        status = ssh_stdout.read().decode()
        logging.debug(f'VRRP status {status}')
        print(ip, repr(status))

        if status == 'true\r\n':
            logging.debug(f'{ip} is master')
            print('status', ip)
            master_ip = ip
        else:
            logging.debug(f'{ip} is slave')
            slave_ip.append(ip)
        client.close()
    return master_ip, slave_ip


def convert_config(meta_line):
    logging.debug(f'Line {meta_line}')
    path = ''
    for i in range(1, len(meta_line)):
        path += meta_line[i] + ' '
    path = path.rstrip()
    logging.debug(f'Make path {path}')
    if re.search('\sset\s', meta_line[0]):
        return None
    elif re.search('\sadd.*\sname', meta_line[0]):
        logging.debug('Add with name')
        item_name = re.search('\sadd.*name=(\S*)', meta_line[0])
        logging.debug(f'Item name {item_name}')
        print('error', meta_line[0])
        print('error', item_name)
        return f'{path} remove "{item_name.group(1)}"\r'

    # Interface
    elif meta_line[1] == '/interface':
        logging.debug('/interface')
        if meta_line[2] == 'bridge':
            logging.debug('bridge')
            if meta_line[3] == 'port':
                remove_interface = re.search('bridge=(\S*).*interface=(\S*)', meta_line[0])
                logging.debug(f'Remove port {remove_interface}')
                return f'{path} remove [ find bridge={remove_interface.group(1)} interface={remove_interface.group(2)} ]\r'

            elif meta_line[3] == 'vlan':
                remove_vlan = re.search('bridge=(\S*).*vlan-ids=(\S*)', meta_line[0])
                logging.debug(f'Remove vlan {remove_vlan}')
                return f'{path} remove [ find bridge={remove_vlan.group(1)} vlan-ids={remove_vlan.group(2)} ]\r'

        elif meta_line[2] == 'list':
            logging.debug('list')
            if meta_line[2] == 'member':
                remove_interface = re.search('interface=(\S*).*list=(\S*)', meta_line[0])
                logging.debug(f'Remove member {remove_interface}')
                return f'{path} remove [ find interface={remove_interface.group(1)} list={remove_interface.group(2)} ]\r'

    elif meta_line[1] == '/ip':
        logging.debug('/ip')
        if meta_line[2] == 'dhcp-server':
            logging.debug('dhcp-server')
            if meta_line[3] == 'lease':
                # if re.search('\s(address)=', meta_line[0]).group(1) == 'address':
                item_address = re.search('\saddress=(\S*)', meta_line[0])
                logging.debug(f'Remove lease {item_address}')
                return f'{path} remove [ find address={item_address.group(1)} ]\r'

            elif meta_line[3] == 'network':
                remove_network = re.search('address=(\S*).*gateway=(\S*)', meta_line[0])
                logging.debug(f'Remove network {remove_network}')
                return f'{path} remove [ find address={remove_network.group(1)} gateway={remove_network.group(2)} ]\r'

        elif meta_line[2] == 'dhcp-client':
            # if re.search('interface', meta_line[0]).group() == 'interface':
            interface_name = re.search('interface=(\S*)', meta_line[0])
            logging.debug(f'Remove dhcp-client {interface_name}')
            return f'{path} remove [ find interface={interface_name.group(1)} ]\r'

        elif meta_line[2] == 'firewall':
            logging.debug('firewall')
            if meta_line[3] == 'filter':
                logging.debug('Remove filter')
                return f'{path} remove [ find ]\r'

            elif meta_line[3] == 'mangle':
                logging.debug('Remove mangle')
                return f'{path} remove [ find ]\r'

            elif meta_line[3] == 'nat':
                logging.debug('Remove nat')
                return f'{path} remove [ find ]\r'

            elif meta_line[3] == 'raw':
                logging.debug('Remove raw')
                return f'{path} remove [ find ]\r'

            elif meta_line[3] == 'address-list':
                logging.debug('address-list')
                remove_address = re.search('address=(\S*).*list=(\S*)', meta_line[0])
                logging.debug(f'Remove address {remove_address}')
                return f'{path} remove [ find address={remove_address.group(1)} list={remove_address.group(2)} ]\r'

        elif meta_line[2] == 'ipsec':
            logging.debug('ipsec')
            if meta_line[3] == 'identity':
                remove_identity = re.search('peer=(\S*).*policy-template-group=(\S*)', meta_line[0])
                logging.debug(f'Remove identity {remove_identity}')
                return f'{path} remove [ find peer={remove_identity.group(1)} policy-template-group={remove_identity.group(2)} ]\r'

        elif meta_line[2] == 'address':
            remove_address = re.search('address=(\S*).*interface=(\S*)', meta_line[0])
            logging.debug(f'Remove address {remove_address}')
            return f'{path} remove [ find address={remove_address.group(1)} interface={remove_address.group(2)} ]\r'

        elif meta_line[2] == 'route':
            remove_route = re.search('dst-address=(\S*).*gateway=(\S*)', meta_line[0])
            logging.debug(f'Remove route {remove_route}')
            try:
                return f'{path} remove [ find dst-addres={remove_route.group(1)} gateway={remove_route.group(2)} ]\r'
            except AttributeError:
                logging.error(f'Route parse error {meta_line[0]}')
                return None

        elif meta_line[2] == 'traffic-flow':
            logging.debug('traffic-flow')
            if meta_line[3] == 'target':
                remove_target = re.search('dst-address=(\S*)', meta_line[0])
                logging.debug(f'Remove target {remove_route}')
                return f'{path} remove [ find dst-addres={remove_target.group(1)} ]\r'

    elif meta_line[1] == '/system':
        logging.debug('/system')
        if meta_line[2] == 'logging':
            remove_logging = re.search('action=(\S*).*topics=(\S*)', meta_line[0])
            logging.debug(f'Remove logging {remove_logging}')
            try:
                return f'{path} remove [ find action={remove_logging.group(1)} topics={remove_logging.group(2)} ]\r'
            except AttributeError:
                logging.error(f'Logging parse error {meta_line[0]}')
                return None

    elif meta_line[1] == '/radius':
        logging.debug('/radius')
        remove_radius = re.search('address=(\S*).*service=(\S*)', meta_line[0])
        logging.debug(f'Remove logging {remove_radius}')
        return f'{path} remove [ find address={remove_radius.group(1)} service={remove_radius.group(2)} ]\r'

    logging.info(f'No action for {meta_line}')
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Synchronization the configuration for routeros',
                                     formatter_class=argparse.MetavarTypeHelpFormatter)

    parser.add_argument('--log', type=str, help='path to log file', default='/tmp')
    parser.add_argument('--debug', type=str, help='debug level', default='debug', choices=('info', 'debug'))
    parser.add_argument('--ssh-port', dest='ssh_port', type=int, help='routeros ssh port', default=22)
    parser.add_argument('--ssh-ros-key', dest='ssh_ros_key', type=str, help='private key file', default='')
    parser.add_argument('--git-repo', dest='git_repo', type=str, help='path to git repository',
                        default='')
    parser.add_argument('--patch-file', dest='patch-file', type=str, help='path to patch file',
                        default='')

    args = parser.parse_args()

    debug_match = {'info': logging.INFO, 'debug': logging.DEBUG}

    logging.basicConfig(level=debug_match.get(args.debug), filename=f"{args.log}/routeros-sync.log",
                        format='%(asctime)s %(process)d %(name)s %(levelname)s %(funcName)s %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')

    sys.exit(main())
