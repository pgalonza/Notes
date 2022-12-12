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

## Change password

Remove passowrd

```bash
openssl rsa -in <src key>.key -out <dst key>.key
```

Change password

```bash
openssl rsa -aes256 -in <src key>.key -out <dst key>.key
```
