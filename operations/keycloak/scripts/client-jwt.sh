#!/bin/bash

CLIENT_ID=<client>
CLIENT_SECRET='<secret>'
URL=https://<keycloak host>/realms/<realm name>/protocol/openid-connect/token
SCOPE=<>

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
--data "grant_type=client_credentials" \
--data "scope=$SCOPE"| jq -r .access_token