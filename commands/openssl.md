# OpenSSL

Connect with cipher

```bash
openssl s_client -connect <host name> -cipher <cipher name>
```

## SSL/TLS

Import Centos
_/etc/pki/ca-trust/source/anchors/_

```bash
update-ca-trust
```

Import Ubuntu
_/usr/local/share/ca-certificates/_

```bash
update-ca-certificates
```

Check

```bash
openssl s_client -tls1_1 -starttls imap -connect <host name>:143 -servername <host name>
```

View

* Request CSR

```bash
openssl req -text -noout -verify -in domain.csr
```

* Public CRT

```bash
openssl x509 -text -noout -in domain.crt
```

* Private KEY

```bash
openssl rsa -check -in domain.key
```

Check the membership

```bash
openssl rsa -noout -modulus -in domain.key | openssl md5
openssl x509 -noout -modulus -in domain.crt | openssl md5
openssl req -noout -modulus -in domain.csr | openssl md5
```

Check CRT via CA

```bash
openssl verify -verbose -CAfile ca.crt domain.crt
```

Convert DER to PEM

```bash
openssl x509 -inform der -in <certigicate_name>.der -out <certigicate_name>.pem
```

## Create self signed certifications

Root key

```bash
openssl genrsa -des3 -out rootCA.key 4096
```

Root certificate

```bash
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1825 -out rootCA.pem
```

Domain key

```bash
openssl genrsa -out <domain_name>.key 2048
```

CSR

```bash
openssl req -new -key <domain_name>.key -out <domain_name>.csr
```

Create certificate

```bash
openssl x509 -req -in <domain_name>.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out <domain_name>.pem -days 365 -sha256
```

## Encryption & Decryption

Encrypt password

```bash
echo "<password>" | openssl enc -aes-256-cbc -md sha512 -a -pbkdf2 -iter 100000 -salt -pass pass:<salt> > secret.txt
```

Decryption password

```bash
cat secret.txt | openssl enc -aes-256-cbc -md sha512 -a -d -pbkdf2 -iter 100000 -salt -pass pass:<salt>
```

## Change password

Remove passowrd

```bash
openssl rsa -in <src key>.key -out <dst key>.key
```

Change password

```bash
openssl rsa -aes256 -in <src key>.key -out <dst key>.key
```

## Java Keystore

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
