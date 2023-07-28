---
title: "Kafka"
draft: false
---

{{< toc >}}

Optimizations

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

View consumer groups

```bash
<path>/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
```

View consumer group infoprmation

```bash
<path>/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group <group name>
<path>/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group <group name> --state
```

Run consumer

```bash
<path>/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic name> --from-beginning
```

Run Producer

```bash
<path>/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic name>
<path>/bin/kafka-console-consumer.sh --broker-list localhost:9092 --topic <topic name>
```

Show dirty pages

```bash
cat /proc/vmstat | egrep "dirty|writeback"
```

Create user

```bash
<path>/bin/kafka-configs --bootstrap-server localhost:9092 --alter --add-config 'SCRAM-SHA-256=[password=<password>],SCRAM-SHA-512=[password=<password>]' --entity-type users --entity-name <user name>
```

## Topics and partiotions

Create topic

```bash
<path>/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic <topic name>
```

View topic

```bash
<path>/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic <topic name>
```

View topics with overrides parameters

```bash
<path>/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topics-with-overrides
```

View partitions that are not consistent with the replica

```bash
<path>/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions
```

View partitions with no master replica

```bash
<path>/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --unavailable-partitions
```

## ACL`s

Parameters

* --group <> - Rules on cunsumer group
* --topic <> - Rules on topic
* --consumer - Rukes on consumer
* --producer - Rules on producer
* --cluster - Rules on  cluster

* View

    ```bash
    <path>/bin/kafka-acls.sh --bootstrap-server localhost:9092 --list --topic <topic name>
    ```

* Add

    ```bash
    <path>/bin/kafka-acls.sh --bootstrap-server localhost:9092 --add --allow-principal User:<user name> --operation <operation> --topic <topic name>
    ```

* Remove

    ```bash
    <path>/bin/kafka-acls.sh --bootstrap-server localhost:9092 --remove --allow-principal User:<user name> --operation <operation> --topic <topic name>
    ```

## TLS

### Connection

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

### Authentication

Certification

* !Generate certification without email if use DN
* If email exist, use principal "1.2.840.113549.1.9.1=#\<email in hex\>,CN=,OU=,O=,L=,ST=,C="

```ini
[req]
default_bits = 2048
default_md = sha256
distinguished_name = req_distinguished_name
prompt = no
utf8 = yes

[req_distinguished_name]
countryName = <RU/EU..>
stateOrProvinceName = <name of city>
localityName = <name of city>
organizationName = <name of organization>
organizationalUnitName = <division name>
commonName = <domain name if have not alternative names. !Required Field!>
```

Server

```ini
ssl.client.auth=required

ssl.principal.mapping.rules= \
RULE:^CN=([a-zA-Z0-9.]*).*$/$1/L ,\
RULE:^CN=(.*?),OU=ServiceUsers.*$/$1/,\
RULE:^CN=(.*?),OU=(.*?),O=(.*?),L=(.*?),ST=(.*?),C=(.*?)$/$1@$2/L,\
RULE:^.*[Cc][Nn]=([a-zA-Z0-9.]*).*$/$1/L,\
DEFAULT
```

Clinet

```ini
security.protocol=SSL
ssl.keystore.location=<keystore path>
ssl.keystore.password=<keystore password>
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

# Only before 1st start
zookeeper.set.acl=true
```

## OAUTHBEARER

[KIP-768: Extend SASL/OAUTHBEARER with Support for OIDC](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=186877575)

Server

File _server.propeties_

```ini
sasl.enabled.mechanisms=SCRAM-SHA-512,SCRAM-SHA-256,OAUTHBEARER

listener.name.sasl_ssl.sasl.enabled.mechanisms=OAUTHBEARER,SCRAM-SHA-512,SCRAM-SHA-256
listener.name.sasl_ssl.oauthbearer.sasl.server.callback.handler.class=org.apache.kafka.common.security.oauthbearer.secured.OAuthBearerValidatorCallbackHandler
listener.name.sasl_ssl.oauthbearer.sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
sasl.oauthbearer.expected.audience=account
sasl.oauthbearer.token.endpoint.url=https://<Keycloak host>:8443/realms/<realm name>/protocol/openid-connect/token
sasl.oauthbearer.jwks.endpoint.url=https://<Keycloak host>:8443/realms/<realm name>/protocol/openid-connect/certs
sasl.oauthbearer.expected.issuer=https://<Keycloak host>:8443/realms/<realm name>
```

Client

```ini
security.protocol=SASL_SSL
sasl.mechanism=OAUTHBEARER
sasl.login.callback.handler.class=org.apache.kafka.common.security.oauthbearer.secured.OAuthBearerLoginCallbackHandler
sasl.oauthbearer.token.endpoint.url=https://<Keycloak host>:8443/realms/<realm name>/protocol/openid-connect/token

sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required \
clientId="<client id>" \
clientSecret="<client secret>";
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

## Replication

```properties
acks = all
min.insync.replicas = <number of replicas < replication.factor>
```
