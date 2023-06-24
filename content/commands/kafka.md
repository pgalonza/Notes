---
title: Kafka
draft: false
description: "CLI commands for Kafka"
---

{{< toc >}}

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
