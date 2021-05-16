# SSL/TLS
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
