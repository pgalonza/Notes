---
title: "Java Keystore"
draft: false
---

{{< toc >}}

## Convert PEM into JKS

Convert PEM into PKCS12

```bash
openssl pkcs12 -export -in <cert name>.pem -inkey <key name>.pem -CAfile <CA name>.pem -out <certificate name>.p12 -name "<alias name>"
```

Create JKS

```bash
keytool -genkey -storetype JKS -keyalg RSA -alias tmp -keystore <keystore>.jks
keytool -delete -alias tmp -keystore keystore.jks
```

Convert PKCS12 into JKS

```bash
keytool -importkeystore -srckeystore <certificate name>.p12 -srcstoretype pkcs12 -storetype JKS -destkeystore <keystore name>.jks
```
