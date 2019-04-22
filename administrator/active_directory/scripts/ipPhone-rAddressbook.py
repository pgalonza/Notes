import sys
import lm_auth
from ldap3 import SUBTREE, Server, Connection
import xml.etree.ElementTree as ET


def main():
    path_list = {}
    for ou, origin in lm_auth.ad_ou_tree.items():
        if ou == 'all':
            continue
        user_list = get_information(origin[0], origin[1])
        path_to_file = ou + '-remote.xml'
        path_list[origin[1]] = ou + '-remote.xml'
        create_xml_departament(user_list, path_to_file)
    create_xml_menu(path_list)


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
        user_list[str(entry.displayName)] = str(entry.ipPhone).replace('-', '')

    connection.unbind()
    return user_list


def create_xml_departament(user_info, file_path):
    root = ET.Element('YealinkIPPhoneDirectory')
    for name, number in user_info.items():
        dir_entry = ET.SubElement(root, 'DirectoryEntry')
        name_xml = ET.SubElement(dir_entry, 'Name')
        name_xml.text = name
        number_xml = ET.SubElement(dir_entry, 'Telephone')
        number_xml.text = number

    tree = ET.ElementTree(root)
    tree.write(file_path, encoding="utf-8")


def create_xml_menu(path_list):
    root = ET.Element('YealinkIPPhoneMenu')
    title = ET.SubElement(root, 'Title')
    title.text = "ФГБУ ЦЖКУ"
    for group, path in path_list.items():
        menu_item = ET.SubElement(root, 'MenuItem')
        name = ET.SubElement(menu_item, 'Name')
        name.text = group
        url = ET.SubElement(menu_item, 'URL')
        url.text = path

    tree = ET.ElementTree(root)
    tree.write('menu.xml', encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
