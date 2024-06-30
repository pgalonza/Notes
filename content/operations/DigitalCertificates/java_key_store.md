---
title: "Java Keystore"
draft: false
description: "JKS(Java Keystore) notes"
---

{{< toc >}}

## Commands

Import certificate

```bash
keytool -import -alias <alias> -file <file_name>.cer -storetype <type> -keystore <keystore_file>
```

View

```bash
keytool -list -v -keystore <keystore_file>
```

Create keystore

```bash
keytool -genkey -alias tmp -keyalg RSA -keystore <keystore_file> -keysize 2048 -storetype <type>
keytool -delete -alias tmp -keystore <keystore_file>
```

Change key password

```bash
keytool -keypasswd -alias <alias> -keystore <keystore_file>
```

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
