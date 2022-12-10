# OpenSSL

## Create private key and request

OpenSSL configuration

```ini
[req]
default_bits = 2048
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
emailAddress = <contact email>

[v3_req]
subjectAltName = @alt_names

[alt_names]
IP.1 = <alternative address>
IP.2 = <alternative address>
DNS.1 = <alternative domain named>
DNS.2 = <alternative domain named>

[ user_cert ]
basicConstraints = CA:FALSE
nsCertType = client, email
nsComment = "Client certificates"
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer
keyUsage = critical, nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage = clientAuth, emailProtection

[ server_cert ]
basicConstraints = CA:FALSE
nsCertType = server
nsComment = "Server Certificate"
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer:always
keyUsage = critical, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth

[ root_ca ]
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints = critical, CA:true
keyUsage = critical, digitalSignature, cRLSign, keyCertSign

[ intermediate_ca ]
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints = critical, CA:true, pathlen:0
keyUsage = critical, digitalSignature, cRLSign, keyCertSign

[ code_cert ]
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
openssl x509 -req -in <domain_name>.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out <domain_name>.pem -days 365 -sha256 -extfile openssl.cfg -extensions 'v3_req'
```
