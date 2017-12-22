#! /usr/bin/env python3
#Powered by Peter & Alex

#./export-list.py inportfile exportfile
import sys, csv
password = "rJy0hX38"
uListFile = open(sys.argv[2], 'w') #number,name(libreoffice) #number;name(MSexel)

header = "extension,password,name,voicemail,ringtimer,noanswer,recording,outboundcid,sipname,noanswer_cid,busy_cid,chanunavail_cid,noanswer_dest,busy_dest,chanunavail_dest,mohclass,id,tech,dial,devicetype,user,description,emergency_cid,recording_in_external,recording_out_external,recording_in_internal,recording_out_internal,recording_ondemand,recording_priority,answermode,intercom,cid_masquerade,accountcode,allow,avpf,callerid,canreinvite,context,defaultuser,deny,disallow,dtmfmode,encryption,force_avp,host,icesupport,namedcallgroup,namedpickupgroup,nat,permit,port,qualify,qualifyfreq,rtcp_mux,secret,sendrpid,sessiontimers,sipdriver,transport,trustrpid,type,videosupport,callwaiting_enable,findmefollow_strategy,findmefollow_grptime,findmefollow_grppre,findmefollow_grplist,findmefollow_annmsg_id,findmefollow_postdest,findmefollow_dring,findmefollow_needsconf,findmefollow_***REMOVED***alert_id,findmefollow_toolate_id,findmefollow_ringing,findmefollow_pre_ring,findmefollow_voicemail,findmefollow_calendar_id,findmefollow_calendar_match,findmefollow_changecid,findmefollow_fixedcid,findmefollow_enabled,languages_language"+"\n"
uListFile.write(header)
i = 0
with open (sys.argv[1]) as csvfile:
    userReader = csv.DictReader(csvfile)
    for row in userReader:
        i = i + 1
        print(i)
        number=row['number']
        name=row['name']
        line = number+",,"+name+",novm,0,,,,,,,,,,,default,"+number+",sip,SIP/"+number+",fixed,"+number+","+name+",,dontcare,dontcare,dontcare,dontcare,disabled,10,disabled,enabled,"+number+",,,no,\""+name+" <"+number+">\",no,from-internal,,0.0.0.0/0.0.0.0,,rfc2833,no,no,dynamic,no,,,no,0.0.0.0/0.0.0.0,5060,yes,60,no,"+password+",pai,accept,chan_sip,\"udp,tcp,tls\",yes,friend,inherit,ENABLED,ringallv2-prim,20,,"+number+",,\"ext-local,"+number+",dest\",,,,,Ring,7,novm,,yes,default,,,"+"\n"
        uListFile.write(line)
uListFile.close()




#PJsip number+",,"+name+",novm,0,,,,,,,,,,,default,"+number+",pjsip,PJSIP/"+number+",fixed,"+number+","+name+",,dontcare,dontcare,dontcare,dontcare,disabled,10,disabled,enabled,"+number+",,yes,,no,\""+name+" "+"<"+number+">\""+",from-internal,,0,,rfc4733,yes,no,,1,7200,no,no,no,60,auto,,,,60,yes,no,yes,"+password+",pai,accept,chan_pjsip,yes,,yes,ENABLED,ringallv2-prim,20,,"+number+",,\"ext-local,"+number+",dest\",,,,,Ring,7,novm,,yes,default,,,"+"\n"
#chanSip number+",,"+name+",novm,0,,,,,,,,,,,default,"+number+",sip,SIP/"+number+",fixed,"+number+","+name+",,dontcare,dontcare,dontcare,dontcare,disabled,10,disabled,enabled,"+number+",,,no,\""+name+" <"+number+">\",no,from-internal,,0.0.0.0/0.0.0.0,,rfc2833,no,no,dynamic,no,,,no,0.0.0.0/0.0.0.0,5060,yes,60,no,"+password+",pai,accept,chan_sip,\"udp,tcp,tls\",yes,friend,inherit,ENABLED,ringallv2-prim,20,,"+number+",,\"ext-local,"+number+",dest\",,,,,Ring,7,novm,,yes,default,,,"+"\n"

'''
pjSip header
extension,password,name,voicemail,ringtimer,noanswer,recording,outboundcid,sipname,noanswer_cid,busy_cid,chanunavail_cid,noanswer_dest,busy_dest,chanunavail_dest,mohclass,id,tech,dial,devicetype,user,description,emergency_cid,recording_in_external,recording_out_external,recording_in_internal,recording_out_internal,recording_ondemand,recording_priority,answermode,intercom,cid_masquerade,accountcode,aggregate_mwi,allow,avpf,callerid,context,defaultuser,device_state_busy_at,disallow,dtmfmode,force_rport,icesupport,match,max_contacts,maximum_expiration,media_use_received_transport,mediaencryption,mediaencryptionoptimistic,minimum_expiration,mwi_subscription,namedcallgroup,namedpickupgroup,outbound_proxy,qualifyfreq,rewrite_contact,rtcp_mux,rtp_symmetric,secret,sendrpid,sessiontimers,sipdriver,timers,transport,trustrpid,callwaiting_enable,findmefollow_strategy,findmefollow_grptime,findmefollow_grppre,findmefollow_grplist,findmefollow_annmsg_id,findmefollow_postdest,findmefollow_dring,findmefollow_needsconf,findmefollow_***REMOVED***alert_id,findmefollow_toolate_id,findmefollow_ringing,findmefollow_pre_ring,findmefollow_voicemail,findmefollow_calendar_id,findmefollow_calendar_match,findmefollow_changecid,findmefollow_fixedcid,findmefollow_enabled,languages_language


chansip header
extension,password,name,voicemail,ringtimer,noanswer,recording,outboundcid,sipname,noanswer_cid,busy_cid,chanunavail_cid,noanswer_dest,busy_dest,chanunavail_dest,mohclass,id,tech,dial,devicetype,user,description,emergency_cid,recording_in_external,recording_out_external,recording_in_internal,recording_out_internal,recording_ondemand,recording_priority,answermode,intercom,cid_masquerade,accountcode,allow,avpf,callerid,canreinvite,context,defaultuser,deny,disallow,dtmfmode,encryption,force_avp,host,icesupport,namedcallgroup,namedpickupgroup,nat,permit,port,qualify,qualifyfreq,rtcp_mux,secret,sendrpid,sessiontimers,sipdriver,transport,trustrpid,type,videosupport,callwaiting_enable,findmefollow_strategy,findmefollow_grptime,findmefollow_grppre,findmefollow_grplist,findmefollow_annmsg_id,findmefollow_postdest,findmefollow_dring,findmefollow_needsconf,findmefollow_***REMOVED***alert_id,findmefollow_toolate_id,findmefollow_ringing,findmefollow_pre_ring,findmefollow_voicemail,findmefollow_calendar_id,findmefollow_calendar_match,findmefollow_changecid,findmefollow_fixedcid,findmefollow_enabled,languages_language
'''
