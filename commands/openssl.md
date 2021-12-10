# OpenSSL

## SSL/TLS
Import Centos
_/etc/pki/ca-trust/source/anchors/_
```
update-ca-trust
```

Import Ubuntu
_/usr/local/share/ca-certificates/_
```
update-ca-certificates
```

Check
```
openssl s_client -tls1_1 -starttls imap -connect host:143 -servername host_name
```

View
* Request CSR
```
openssl req -text -noout -verify -in domain.csr
```

* Public CRT
```
openssl x509 -text -noout -in domain.crt
```

* Private KEY
```
openssl rsa -check -in domain.key
```

Check the membership
```
openssl rsa -noout -modulus -in domain.key | openssl md5
openssl x509 -noout -modulus -in domain.crt | openssl md5
openssl req -noout -modulus -in domain.csr | openssl md5
```

Check CRT via CA
```
openssl verify -verbose -CAfile ca.crt domain.crt
```

Convert DER to PEM
```
openssl x509 -inform der -in <certigicate_name>.der -out <certigicate_name>.pem
```

## Create self signed certifications

Root key
```
openssl genrsa -des3 -out rootCA.key 4096
```

Root certificate
```
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1825 -out rootCA.pem
```

Domain key
```
openssl genrsa -out <domain_name>.key 2048
```

CSR
```
openssl req -new -key <domain_name>.key -out <domain_name>.csr
```

Create certificate
```
openssl x509 -req -in <domain_name>.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out <domain_name>.pem -days 365 -sha256
```

## Encryption & Decryption

Encrypt password
```
echo "<password>" | openssl enc -aes-256-cbc -md sha512 -a -pbkdf2 -iter 100000 -salt -pass pass:<salt> > secret.txt
```

Decryption password
```
cat secret.txt | openssl enc -aes-256-cbc -md sha512 -a -d -pbkdf2 -iter 100000 -salt -pass pass:<salt>
```
