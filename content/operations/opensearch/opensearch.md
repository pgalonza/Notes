---
title: "OpenSearch"
draft: false
description: "CLI commands and queries for OpenSearch"
aliases:
  - /operations/lasticsearch/elasticsearch/
---

## Requests

Add pipekine with frok

```text
PUT _ingest/pipeline/<pipeline_name>
{
  "description": "<description>",
  "processors": [
    {
      "grok": {
        "field": "message",
        "patterns": [
          "%{MONTHDAY}-%{MONTH}-%{YEAR} %{TIME} %{INT:PID} %{USERNAME} %{LOGLEVEL:loglevel} %{WORD:function} %{URIPATHPARAM:request}"
        ]
      }
    }
  ]
}
```

## DataStream

* [OpenSearch Service for 2TB Daily Ingest](https://gist.github.com/rupeshtiwari/8b741704424967d864141521aad30b98)

## Recomendations

* Java Heap Size <32GB
* <20 shards on 1GB RAM
* <40-50GB on 1 shard
* GB on 1GB of RAM
  * 30GB for HOT
  * 160GB for WARM
  * 500GB for COLD
* Amount of data
  * total amount of data = <GB per day> * <number of days> * <transformation factor 1> * <nember of replication>
  * shared data storage = <total amount of data> * (1 + 0,15 + 0,1)
  * total number of nodes = <shared data storage> / <ram per node> / <GB on 1GB of RAM>
* bandwidth
  * peak value of the threads = <peak number of requests per second> * <average response time to a search query in ms> / 1000ms
  * thread pool volume = (<number of cores per node> * <number of threads per core * 3 / 2> + 1)
  * number of data nodes = <peak value of the threads> / <thread pool volume>