---
title: "RabbitMQ"
draft: false
description: "RabbitMQ notes"
---

Enable metrics

```bash
echo management_agent.disable_metrics_collector = false > /etc/rabbitmq/conf.d/management_agent.disable_metrics_collector.conf
```

Log levels

```text
log_levels [{connection,error},{default,error}]
```

Disk space limit

```text
disk_free_limit <value>
```
