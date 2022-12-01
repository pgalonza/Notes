# Kafka

Create topic

```bash
<path>/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic <topic name>
```

View topic

```bash
<path>/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic 
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
