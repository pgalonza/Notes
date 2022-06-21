# OpenSSL

## Create private key and request

OpenSSL configuration

```ini
[ req ]
default_bits = 2048
distinguished_name= req_distinguished_name
req_extensions = req_ext

[ req_distinguished_name ]
countryName	= Country Name (2 letter code)
countryName_default	= <RU/EU..>
countryName_min	= 2
countryName_max	= 2
localityName = Locality Name (eg, city)
localityName_default = <name of city>
organizationName = Organization Name (eg, company)
organizationName_default = <name of organization>
organizationalUnitName = Organizational Unit Name (eg, section)
organizationalUnitName_default = <division name>
commonName = Common Name (eg, YOUR name)
commonName_default = <domain name if have not alternative names. !Required Field!>
commonName_max = 64
emailAddress = Email Address
emailAddress_default = <contact email>
emailAddress_max = 40

[ req_ext ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = <alternative domain named>
DNS.2 = <alternative domain named>
```

Command

```bash
openssl req -new -newkey rsa:2048 -keyout <key name>.key -config openssl.cfg -out <request name>.csr
```
