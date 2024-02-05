---
title: "Nginx"
draft: false
---

{{< toc >}}

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

location /heartbeat {
    return 200 "healthy\n";
}
```

Forward local and remote ports

```text
map http_host $f_port {
    "~^.*\:<port number>" $server_port;
    default 443;
}

proxy_set_header X-Forwarded-Port $f_port;
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

ssl_password_files <file with password for private key>;
ssl_certificate <cetfificate file>;
ssl_certificate_key <private key>;
ssl_dhparam <dhparam.pem>;

ssl_protocols TLSv1.2 TLSv1.3;
proxy_ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers <ciphers>;
proxy_ssl_ciphers ciphers>;

ssl_prefer_server_ciphers on;
ssl_stapling on;
ssl_stapling_verify on;
ssl_session_cache shared:SSL:10m;
ssl_session_timeout 5m;
```

## Reverse Proxy

Proxy

Location

```text
add_header X-Request-ID $request_id;

    location /<path> {
        proxy_pass <url>;

        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Request-ID $request_id;
        proxy_redirect default;
    }
```

WebSocket

```text
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

upstream <upstream name> {
    server <server>:<port>;
}

    location /wsapp/ {
        proxy_pass https://<upstream name>;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade; # or Connection "upgrade";
        proxy_set_header Host $host;
    }
```

Select server use header

[Information from](https://t.me/bashdays/26)

```text
map $http_x_backend $backend {
    <server name> <address>:<port>;
    default backend;
}

upstream <upstream name> {
    server <server>:<port>;
}

location / {
  add_header X-Upstream $upstream_addr;
  proxy_pass http://$backend;
}
```

## Security

Virtual domain

```text
map $http_host $http_host_valid {
    default false;
    <host name> true;
}

map $host $host_valid {
    default false;
    <host name> true;
}

server {
    return 404;
}

server {
    listen 443 ssl default_server;

    <SSL>

    return 403
}

server {
    listen 443 ssl;
    server_name <server domain>;

    <SSL>

    if ($request_method !~ ^(GET|HEAD|POST)$ ) {
        return 444;
    }

    limit_except GET HEAD POST {deny all;}

    if ( $http_host_valid == false ) {
        return 418;
    }

    if ( $host_valid == false ) {
        return 418;
    }

    location ~ /\.(?!well-known) {
        deny all;
        return 404;
    }
}

```

Nginx

```text
http {
    sendfile               on;
    tcp_nopush             on;

    gzip off;
    autoindex off;
    dav_methods off;

    add_header Strict-Transport-Security "max-age=15768000; includeSubdomains;";
    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Content-Security-Policy "default-src 'self'";

    proxy_http_version 1.1;
    proxy_hide_header X-powered-By;
    proxy_hide_header Server;
    server_tokens off;

    limit_conn_zone $binary_remote_addr zone=limitperip:10m;
    limit_conn limitperip 10;

    send_timeout 10;
    keepalive_timeout 10;
    client_body_timeout 10;
    client_header_timeout 10;
    client_max_body_size 100k;
    client_body_buffer_size 100k;
    large_client_header_buffers 2 1k;

    proxy_set_timeout 1m;
    proxy_read_timeout 1m;
    proxy_connect_timeout 1m;
    proxy_buffering off;
    expires -1;

    server {
        return 404;
    }
}
```

## Troubleshooting

Duplicate headers when proxy_pass

```text
proxy_hide_header <header name>;
```
