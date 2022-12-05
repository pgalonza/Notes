# Kafka

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
