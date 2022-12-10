# Kafka

* File system: XFS
* Mount option: noatime
* vm.swappinness: 1
* vm.dirty_background_ratio: <10
* vm.dirty_ratio: >20
* net.core.wmem_default: 2097152
* net.core.rmem_default: 2097152
* net.ipv4.tcp_wmem: 4096 65536 2048000
* net.ipv4.tcp_rmem: 4096 65536 2048000
* net.core.wmem_max: > net.ipv4.tcp_wmem
* net.core.rmem_max: > net.ipv4.tcp_rmem
* net.ipv4.tcp_window_scaling: 1
* net.ipv4.tcp_max_syn_backlog: > 1024
* net.core.netdev_max_backlog: > 1000

## SSL

Server

```ini
listeners=PLAINTEXT://:9092,SSL://<server name>:9093
advertised.listeners=PLAINTEXT://:9092,SSL://<server name>:9093
ssl.keystore.location=<keystore path>
ssl.keystore.password=<keystore password>
ssl.truststore.location=<truststore path>
ssl.truststore.password=<truststore password>
```

Client

```ini
security.protocol=SSL
ssl.truststore.location=<truststore path>
ssl.truststore.password=<truststore password>
```

## SASL

Server

File _kafka_server_jaas.conf_

```text
KafkaServer {
   org.apache.kafka.common.security.scram.ScramLoginModule required
   username="<user>"
   password="<password>";
};
```

File _server.propeties_

```ini
listeners=SASL_SSL://<server name>:9093
advertised.listeners=SASL_SSL://<server name>:9093

sasl.enabled.mechanisms=SCRAM-SHA-512,SCRAM-SHA-256,PLAIN
sasl.mechanism.inter.broker.protocol=SCRAM-SHA-512
# Configure SASL_SSL if SSL encryption is enabled, otherwise configure SASL_PLAINTEXT
security.inter.broker.protocol=SASL_SSL
```

```bash
export KAFKA_OPTS="-Djava.security.auth.login.config=<path>/kafka_server_jaas.conf"
```

Client

```ini
security.protocol=SASL_SSL
sasl.mechanism=SCRAM-SHA-512

sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required \
  username="<user name>" \
  password="<password>";
```

## ACL`s

```ini
authorizer.class.name=kafka.security.authorizer.AclAuthorizer
allow.everyone.if.no.acl.found=false
super.users=User:admin

# Only if 1st start
zookeeper.set.acl=true
```

## Zookeeper

### Sasl

File _kafka_server_jaas.conf_

```text
Client {
    org.apache.zookeeper.server.auth.DigestLoginModule required
    username="<user>"
    password="<password>";
};
```
