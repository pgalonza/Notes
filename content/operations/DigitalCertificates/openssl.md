---
title: "OpenSSL"
draft: false
---

{{< toc >}}

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
openssl s_client -showcerts -connect <host name>:443 -servername <host name>
```

View

* Request CSR

```bash
openssl req -text -noout -verify -in <request name>.csr
```

* Public sertificate

```bash
openssl x509 -text -noout -in <sertificate name>.crt
openssl pkcs12 -in <sertificate name>.p12 -node | openssl x509 -text -noout
```

* Private KEY

```bash
openssl rsa -check -in <key name>.key
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

## Encryption & Decryption

Encrypt password

```bash
echo "<password>" | openssl enc -aes-256-cbc -md sha512 -a -pbkdf2 -iter 100000 -salt -pass pass:<salt> > secret.txt
```

Decryption password

```bash
cat secret.txt | openssl enc -aes-256-cbc -md sha512 -a -d -pbkdf2 -iter 100000 -salt -pass pass:<salt>
```

Encrypt file

```bash
openssl enc -pbkdf2 -eas256 -base64 -in <src file> -out <file name>
```

Decryption file

```bash
openssl enc -d -pbkdf2 -eas256 -base64 -in <encryption file> -out <file name>
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

## Create private key and request

OpenSSL configuration

```ini
[req]
default_bits = 4096
default_md = sha256
distinguished_name = req_distinguished_name
req_extensions = 
x509_extensions = 
prompt = no
utf8 = yes

[req_distinguished_name]
countryName = <RU/EU..>
stateOrProvinceName = <name of city>
localityName = <name of city>
organizationName = <name of organization>
organizationalUnitName = <division name>
commonName = <domain name if have not alternative names. !Required Field!>

[v3_req]
subjectAltName = @alt_names

[alt_names]
IP.1 = <alternative address>
IP.2 = <alternative address>
DNS.1 = <alternative domain named>
DNS.2 = <alternative domain named>

[user_cert]
basicConstraints = CA:FALSE
nsComment = "Client certificates"
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer
keyUsage = critical, nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage = clientAuth

[server_cert]
basicConstraints = CA:FALSE
nsComment = "Server Certificate"
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer:always
keyUsage = critical, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth

[root_ca]
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints = critical, CA:TRUE
keyUsage = critical, digitalSignature, cRLSign, keyCertSign

[intermediate_ca]
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints = critical, CA:TRUE, pathlen:0
keyUsage = critical, digitalSignature, cRLSign, keyCertSign

[code_cert]
basicConstraints = CA:FALSE
nsCertType = server
nsComment = "Code Certificate"
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer:always
keyUsage = digitalSignature
extendedKeyUsage = codeSigning, msCodeInd, msCodeCom
```

Command

```bash
openssl req -new -keyout <key name>.key -config openssl.cfg -out <request name>.csr
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
openssl genrsa -des3 -out <domain_name>.key 2048
```

CSR

```bash
openssl req -new -key <domain_name>.key -out <domain_name>.csr
```

Create certificate

```bash
openssl x509 -req -in <domain_name>.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out <domain_name>.pem -days 365 -sha256
openssl x509 -req -in <domain_name>.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out <domain_name>.pem -days 365 -sha256 -extfile openssl.cfg -extensions 'v3_req'
```

## Scripts

[Check ciphers](https://github.com/pgalonza/Notes-files/blob/main/openssl/scripts/check_ciphers.py)
