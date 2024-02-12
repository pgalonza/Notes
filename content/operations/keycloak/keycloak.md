---
title: "Keycloak"
draft: false
---

{{< toc >}}

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
--data "client_id=$CLIENT_ID" \
--data "client_secret=$CLIENT_SECRET" \
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

## TLS

### Client certification in header with Nginx

Build spi

```bash
<path>/bin/kc.sh build --spi-x509cert-lookup-provider=nginx
```

Add in keycloak configuration

```text
spi-x509cert-lookup-nginx-ssl-client-cert=ssl-client-cert
```

Add in Nginx configuration

```text
ssl_verify_client <on|optional|optional_no_ca>;
proxy_set_header ssl-client-cert $ssl_client_escaped_cert;
```

## Security

Ansible task for configure realm

```yaml
- name: Congigure realm
  comunity.general.keycloak_realm:
  community.general.keycloak_realm:
      auth_client_id: admin-cli
      auth_keycloak_url: <keycloak url>
      auth_realm: master
      auth_username: <user name>
      auth_password: <password>
      id: <realm name>
      realm: <realm name>
      state: present
      access_token_lifespan: 60
      access_token_lifespan_for_implicit_flow: 900
      sso_session_idle_timeout: 900
      sso_session_max_lifespan: 36000
      sso_session_idle_timeout_remember_me: 0
      sso_session_max_lifespan_remember_me: 0
      offline_session_idle_timeout: 2592000
      offline_session_max_lifespan_enabled: true
      offline_session_max_lifespan: 0
      ssl_required: all
      otp_policy_type: totp
      otp_policy_algorithm: HmacSHA256
      otp_policy_digits: 6
      otp_policy_look_ahead_window: 1
      otp_policy_period: 30
      events_enabled: true
      events_expiration: 31536000
      admin_events_enabled: true
      admin_events_details_enabled: true
      events_listeners:
      - email
      default_signature_algorithm: RS256
      browser_security_headers:
          xFrameOptions: SOMEORIGIN
          contentSecurityPolicyReportOnly: ""
          xContentTypeOptions: nosniff
          xRobotsTag: "none"
          contentSecurityPolicy: "frame-src 'self'; frame-ancestors 'self'; object-src 'none';"
          strictTransportSecurity: "max-age=31536000l includeSubDomains"
      password_policy: >
          hashAlgorithm(pbkdf2-sha-256) and digits(1)
          and lowerCase(1) anmd upperCase(1)
          and notUsername(undefined) and notEmail(undefined)
          and forceExpiredPasswordChange(30)
          and password History(4) and lenght(16)
      brute_force_protected: true
      max_failure_wait_seconds: 5400
      failure_factor: 6
      wait_increment_seconds: 1800
      max_delta_time_seconds: 86400
      quick_login_check_milli_seconds: 1000
      minimum_quick_login_wait_seconds: 60
      state: present
  delegate_to: localhost
```
