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
