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
ssl_ciphers <ciphers>;
ssl_prefer_server_ciphers on;
ssl_session_cache shared:SSL:10m;
ssl_session_timeout 5m;
```

## Reverse Proxy

Proxy

```text
Location

```text
    location /<path> {
        proxy_pass <url>;

        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
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

    underscores_in_headers on;
    limit_conn limitperip 10;
    large_client_header_buffers 2 4k;

    if ($request_method !~ ^(GET|HEAD|POST)$ ) {
        return 444;
    }

    add_header Strict-Transport-Security "max-age=15768000;";
    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Content-Security-Policy "default-src 'self'";

    if ( $http_host_valid == false ) {
        return 418;
    }

    if ( $host_valid == false ) {
        return 418;
    }
}

# Not work with keycloak
location ~ /\. {
    deny all;
    return 404;
}
```

Nginx

```text
    sendfile               on;
    tcp_nopush             on;
    tcp_nodelay            on;
    server_tokens          off;
    ssl_stapling           on;
    ssl_stapling_verify    on;

    keepalive_timeout      10;
    send_timeout           10;
    client_body_timeout    10;
    client_header_timeout  0;

    client_max_body_size        100k;
    types_hash_max_size         4096;
    map_hash_bucket_size        256;
    large_client_header_buffers 2 1k;
    limit_conn_zone $binary_remote_addr zone=limitperip:10m;
```
