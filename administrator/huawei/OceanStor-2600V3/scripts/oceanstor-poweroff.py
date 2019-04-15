import json
import sys
import requests
import urllib3

urllib3.disable_warnings()

_nas_server = 'host'
_nas_port = '8088'
_nas_user = ''
_nas_password = ''
_nas_user_type = '0'
_headers = None
_nas_device_id = None
_nas_rest_url = None


def main():
    session = nas_rest_connector()
    data = json.dumps({'IMPORTANTPSW': '***REMOVED***'})
    #!session.put(_nas_rest_url + '/system/poweroff', data=data, verify=False)!#
    nas_rest_disconnect(session)


def nas_rest_connector():
    session = requests.Session()

    data = json.dumps({'username': _nas_user, 'password': _nas_password, 'scope': _nas_user_type})
    response = session.post('https://' + _nas_server + ':' + _nas_port + '/deviceManager/rest/xxxxx/sessions',
                            data=data, verify=False)

    global _headers
    _headers = {'iBaseToken': response.json()['data']['iBaseToken']}

    global _nas_device_id
    _nas_device_id = response.json()['data']['deviceid']

    global _nas_rest_url
    _nas_rest_url = 'https://' + _nas_server + ':' + _nas_port + '/deviceManager/rest/'+_nas_device_id

    print(response.status_code)

    return session


def nas_rest_disconnect(session):
    result = session.delete(_nas_rest_url + '/sessions', headers=_headers, verify=False)

    print(result.status_code)


if __name__ == "__main__":
    sys.exit(main())
