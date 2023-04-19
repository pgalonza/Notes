---
title: "Keycloak"
draft: false
---

Get token with Authorization Code

```text
https://<keycloak host>/auth/realms/<realm name>/protocol/openid-connect/auth
?client_id=<client name>&response_type=code&scope=<scope>&redirect_uri=<redirect uri>&state=<generate secret>
```

```bash
curl --location --request POST 'https://<keycloak host>/auth/realms/appsdeveloperblog/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'client_id=<client name>' \
--data-urlencode 'client_secret=<client secret>' \
--data-urlencode 'code=<code>' \
--data-urlencode 'redirect_uri=<redirect uri>'
```

Get token from user

```bash
HOST=<>
REALM=<>
CLIENT_ID=<client>
CLIENT_SECRET='<secret>'
URL=https://$HOST/realms/$REALM/protocol/openid-connect/token
SCOPE=<>
USERNAME=<>
PASSWORD=<>
```

```bash
base_64_string=$(echo -n "$CLIENT_ID:$CLIENT_SECRET" | base64)

curl -v \
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
```

```bash
curl -v \
--silent \
--request POST \
--url $URL \
--header "accept: application/json" \
--header "cache-control: no-cache" \
--header "content-type: application/x-www-form-urlencoded" \
--data "grant_type=password" \
--data "scope=$SCOPE" \
--data "clinet_id=$CLIENT_ID" \
--data "client_secret=$CLIENT_SECRET"
--data "username=$USERNAME" \ 
--data "password=$PASSWORD" | jq -r .access_token
```

Get token from client

```bash
HOST=<>
REALM=<>
CLIENT_ID=<client>
CLIENT_SECRET='<secret>'
URL=https://$HOST/realms/$REALM/protocol/openid-connect/token
SCOPE=<>
```

```bash
base_64_string=$(echo -n "$CLIENT_ID:$CLIENT_SECRET" | base64)

curl -v \
--silent \
--request POST \
--url $URL \
--header "accept: application/json" \
--header "authorization: Basic $base_64_string" \
--header "cache-control: no-cache" \
--header "content-type: application/x-www-form-urlencoded" \
--data "grant_type=client_credentials" \
--data "scope=$SCOPE"| jq -r .access_token
```

```bash
curl -v \
--silent \
--request POST \
--url $URL \
--header "accept: application/json" \
--header "cache-control: no-cache" \
--header "content-type: application/x-www-form-urlencoded" \
--data "grant_type=client_credentials" \
--data "clinet_id=$CLIENT_ID" \
--data "client_secret=$CLIENT_SECRET"
--data "scope=$SCOPE"| jq -r .access_token
```

API request with admin-cli

```bash
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
```

```bash
curl -X GET "${$URL}/admin/realms/${REALM}/users" \
-H "Accept: application/json" \
-H "Authorization: Bearer $TOKEN" 
```

View JWT

[Python](/Notes/development/python/python/#jwt)
