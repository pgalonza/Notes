# General

###### Disable ignore invalid headers
```
echo "ignore_invalid_headers off;" >> /etc/nginx/nginx.conf
```

# FastCGI

###### Time out
```
fastcgi_read_timeout = 60
```

# SSL
###### Generate the Diffie Hellman certificate
```
openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
```

###### Configuration parameters
```
listen 443 http2 ssl;
listen [::]:443 http2 ssl;
server_name server_IP_address;
ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;
ssl_dhparam /etc/ssl/certs/dhparam.pem;
```
