#! /usr/bin/env python3

# ./export-list.py inportfile

import csv
import re
import subprocess
import sys

# salt
_base_password = "fpbx"
# name of make files
_contact_list_name = "contacts.xml"
_export_file_name = "freepbx.csv"

try:
    _file_name = sys.argv[1]
except IndexError:
    sys.exit(print("The file name is not specified!"))


def main():
    convert_csv(_file_name)
    structure_files('head')
    with open(_file_name) as csv_file:
        user_reader = csv.DictReader(csv_file)
        i = 0
        for row in user_reader:
            i = i + 1
            if row['address']:
                create_cfg(find_mac(row['address']), row['newNumber'], _base_password + row['newNumber'])
                create_boot(find_mac(row['address']), row['newNumber'], _base_password + row['newNumber'])
            create_contact_list(i, row['userName'], row['newNumber'])
            create_export_file(row['newNumber'], row['userName'], _base_password + row['newNumber'])
    structure_files('bottom')


# create structure of csv, xml files
def structure_files(position):
    # structure of files
    _contact_header = '''<?xml version=\"1.0\" encoding=\"utf-8\"?>
    <root_group>
         <group display_name=\"All Contacts\" />
    </root_group>
    <root_contact>\n'''
    _contact_bottom = "</root_contact>"
    _export_header = "extension,password,name,voicemail,ringtimer,noanswer,recording,outboundcid,sipname,noanswer_cid," \
                     "busy_cid,chanunavail_cid,noanswer_dest,busy_dest,chanunavail_dest," \
                     "mohclass,id,tech,dial,devicetype,user,description,emergency_cid,recording_in_external," \
                     "recording_out_external,recording_in_internal,recording_out_internal,recording_ondemand," \
                     "recording_priority,answermode,intercom,cid_masquerade,accountcode,allow,avpf,callerid,canreinvite," \
                     "context,defaultuser,deny,disallow,dtmfmode,encryption,force_avp,host," \
                     "icesupport,namedcallgroup,namedpickupgroup,nat,permit,port,qualify,qualifyfreq,rtcp_mux,secret," \
                     "sendrpid,sessiontimers,sipdriver,transport,trustrpid,type,videosupport," \
                     "callwaiting_enable,findmefollow_strategy,findmefollow_grptime,findmefollow_grppre," \
                     "findmefollow_grplist,findmefollow_annmsg_id,findmefollow_postdest,findmefollow_dring," \
                     "findmefollow_needsconf,findmefollow_***REMOVED***alert_id,findmefollow_toolate_id,findmefollow_ringing," \
                     "findmefollow_pre_ring,findmefollow_voicemail,findmefollow_calendar_id," \
                     "findmefollow_calendar_match,findmefollow_changecid,findmefollow_fixedcid,findmefollow_enabled," \
                     "languages_language\n "

    if position == 'head':
        with open(_contact_list_name, 'w') as contact_list:
            contact_list.write(_contact_header)
        with open(_export_file_name, 'w') as export_list:
            export_list.write(_export_header)
    elif position == 'bottom':
        with open(_contact_list_name, 'a') as contact_list:
            contact_list.write(_contact_bottom)


# paste contact line
def create_contact_list(numeric, name, number):
    with open(_contact_list_name, 'a') as contact_list:
        line = "    <contact display_name=\"{name}\" office_number=\"{number}\" mobile_number=\"\" other_number=\"\" " \
               "line=\"{numeric}\" ring=\"\" group_id_name=\"All Contacts\" />\n".format(numeric=str(numeric),
                                                                                         name=name, number=number)
        contact_list.write(line)


# paste export line
def create_export_file(number, name, password):
    with open(_export_file_name, 'a') as export_list:
        line = "{number},,{name},novm,0,,,,,,,,,,,default,{number},sip,SIP/{number},fixed,{number},{name},,dontcare," \
               "dontcare,dontcare,dontcare,disabled,10,disabled,enabled,{number},,,no,\"{name} <{number}>\",no," \
               "from-internal,,0.0.0.0/0.0.0.0,,rfc2833,no,no,dynamic,no,,,no,0.0.0.0/0.0.0.0,5060,yes,60,no,{password}," \
               "pai,accept,chan_sip,\"udp,tcp,tls\",yes,friend,inherit,ENABLED,ringallv2-prim,20,,{number},,\"ext-local," \
               "{number},dest\",,,,,Ring,7,novm,,yes,default,,,\n".format(password=password, number=number, name=name)
        export_list.write(line)


# create cfg for each phone
def create_cfg(mac, phone, password):
    with open(mac + '.cfg', 'w') as config_file:
        config = '''#!version:1.0.0.1
account.1.label = {phone}
account.1.display_name = {phone}
account.1.user_name = {phone}
account.1.auth_name = {phone}
account.1.password = {password}'''.format(phone=phone, password=password)
        config_file.write(config)


def convert_csv(file):
    with open(file, 'r') as contacts:
        _convert_data = contacts.read().replace(';', ',')
    with open(file, 'w') as contacts:
        contacts.write(_convert_data)


def find_mac(address):
    print (address)
    result = str(subprocess.check_output(['sudo', 'nmap', '-sP', '-n', address]))
    mac = re.search(r'..:..:..:..:..:..', result)
    return mac.group(0).replace(':', '').lower()


if __name__ == "__main__":
    sys.exit(main())
