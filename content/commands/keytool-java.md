---
title: Keytool
draft: false
description: "CLI commands for Java keytool"
---

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
