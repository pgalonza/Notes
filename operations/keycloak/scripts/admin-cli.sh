#!/bin/bash

HOST=<>
REALM=<>
CLIENT_ID=admin-cli
URL=https://$HOST/realms/$REALM/protocol/openid-connect/token
USERNAME=<>
PASSWORD=<>

curl -v \
--cacert ./rootCA.pem \
--silent \
--request POST \
--url $URL \
--header "accept: application/json" \
--header "cache-control: no-cache" \
--header "content-type: application/x-www-form-urlencoded" \
--data "grant_type=password" \
--data "client_id=$CLIENT_ID"
--data "username=$USERNAME" \ 
--data "password=$PASSWORD" | jq -r .access_token

curl -X GET "${$URL}/admin/realms/${REALM}/users" \
-H "Accept: application/json" \
-H "Authorization: Bearer $TOKEN" 