---
title: "OAuth2"
date: 2025-06-30T20:18:33+03:00
draft: false
description: "Comprehensive collection of OAuth 2.0 notes covering authorization flows, security best practices, and implementation strategies for developers and security professionals. Explore detailed explanations of OAuth concepts, practical guidance, and common pitfalls to master modern authorization protocols effectively."
summary: "OAuth2"
---

{{< toc >}}

- [RFC 6749](https://www.ietf.org/rfc/rfc6749.txt)

## Software

### IAM/idP

- [Keycloak](https://www.keycloak.org/)
- [Supertokens](https://supertokens.com/)
- [Casdoor](https://casdoor.org/)
- [Logto](https://logto.io/)

### Middleware

- [oauth2-proxy](https://github.com/oauth2-signin/oauth2-proxy)
- [oathkeeper](https://github.com/ory/oathkeeper)

## Roles

- Resource Owner
- Client
- Authorization Server
- Resource Server

## Flows

Standart

- Authorization code
- Client credentials
- Implicit
- Resource owner password credentials
- Device authorization


Keycloak

- Browser Authentication Flow
- Client Authentication Flow
- Direct Grant Flow
- Docker Authentication Flow