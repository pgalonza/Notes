# Nginx

Disable ignore invalid headers

```bash
echo "ignore_invalid_headers off;" >> /etc/nginx/nginx.conf
```

Metrics Page

```text
location /nginx_status {
        stub_status;
        allow 127.0.0.1;
        deny all;
}
```

## FastCGI

Time out

```text
fastcgi_read_timeout = 60
```

## SSL

Generate the Diffie Hellman certificate

```bash
openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048/4096
```

Configuration parameters

```text
listen 443 http2 ssl;
listen [::]:443 http2 ssl;
server_name server_IP_address;
ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;
ssl_dhparam /etc/ssl/certs/dhparam.pem;
```
