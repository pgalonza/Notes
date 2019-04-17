import sys
import lm_auth
from ldap3 import SUBTREE, Server, Connection
import xml.etree.ElementTree as ET

def main():
    for ou, origin in lm_auth.ad_ou_tree.items():
        if ou == 'all':
            continue
        user_list = get_information(origin[0], origin[1])
        path_to_file = ou + '-remote.xml'



def get_information(origin, group_name):
    if group_name == "ВКС":
        connection = lm_auth.active_derectory_connector_vks()
        connection.search('dc=,dc=,dc=',
                    '(&(objectCategory=person)(displayName=*)(givenName=*)(ipPhone=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE,
                    attributes=['ipPhone', 'displayName'])
    else:
        connection = lm_auth.active_derectory_connector()
        connection.search(origin,
                    '(&(objectCategory=person)(displayName=*)(givenName=*)(ipPhone=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))',
                    SUBTREE,
                    attributes=['ipPhone', 'displayName'])

    user_list = {}

    for entry in connection.entries:
        user_list[entry.displayName] = [str(entry.ipPhone).replace('-', ''), group_name]

    return user_list


def create_xml_file(user_info, file_path, group_name):
    root = ET.Element('YealinkIPPhoneDirectory')
    entry = ET.SubElement(root, 'DirectoryEntry')






if __name__ == "__main__":
    sys.exit(main())
