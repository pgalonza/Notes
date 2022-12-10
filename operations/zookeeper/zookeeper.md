# Zookeeper

## SSL

Server

```ini
secureClientPort=<secure port>
serverCnxnFactory=org.apache.zookeeper.server.NettyServerCnxnFactory
ssl.keyStore.location=<keystore path>
ssl.keyStore.password=<keystore password>
ssl.trustStore.location=<truststore path>
ssl.trustStore.password=<truststore password>
ssl.clientAuth=none
```

Clent

```bash
export CLIENT_JVMFLAGS="-Dzookeeper.clientCnxnSocket=org.apache.zookeeper.ClientCnxnSocketNetty -Dzookeeper.client.secure=true -Dzookeeper.ssl.trustStore.location=<path>/truststore.jks -Dzookeeper.ssl.trustStore.password=<password>"
```

```ini
zookeeper.client.secure=true
zookeeper.ssl.trustStore.location=/opt/zookeeper/ssl/truststore.jks
zookeeper.ssl.trustStore.password=changeme
```

## SASL

Server

```ini
authProvider.sasl=org.apache.zookeeper.server.auth.SASLAuthenticationProvider
requireClientAuthScheme=sasl
```

File _zookeeper_server_jaas.conf_

```text
Server {
       org.apache.zookeeper.server.auth.DigestLoginModule required
       user_super="<password>"
       user_client="<password>";
};
```

Client

```bash
export SERVER_JVMFLAGS="-Djava.security.auth.login.config=<path>/kafka_server_jaas.conf"
```

```ini
zookeeper.sasl.client=true
zookeeper.clientCnxnSocket=org.apache.zookeeper.ClientCnxnSocketNetty
```
