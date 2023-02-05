#!/bin/bash

CLIENT_ID=<client>
CLIENT_SECRET='<secret>'
URL=https://<keycloak host>/realms/<realm name>/protocol/openid-connect/token
SCOPE=<>
USERNAME=<>
PASSWORD=<>

base_64_string=$(echo -n "$CLIENT_ID:$CLIENT_SECRET" | base64)

curl -v \
--cacert ./rootCA.pem \
--silent \
--request POST \
--url $URL \
--header "accept: application/json" \
--header "authorization: Basic $base_64_string" \
--header "cache-control: no-cache" \
--header "content-type: application/x-www-form-urlencoded" \
--data "grant_type=password" \
--data "scope=$SCOPE" \
--data "username=$USERNAME" \ 
--data "password=$PASSWORD" | jq -r .access_token