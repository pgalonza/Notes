---
title: "OpenSearch"
date: 2024-08-24T15:00:00+03:00
draft: false
description: "The page with notes on OpenSearch is a valuable resource for developers and administrators looking to optimize the search experience on their websites and applications."
aliases:
  - /operations/opensearch/opensearch/
---

## Requests

Add pipeline with grok

```json
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

Get information

```json
GET /_cat/indices?v
GET /_cluster/health
GET /_cluster/settings?include_defaults=true
GET /_cat/shards/<index name>?v
GET /_cat/indices/<index name>?v
```

Set shard limit

```json
PUT /_cluster/settings
{
  "persistent": {
    "cluster.max_shards_per_node" <value>
  }
}
```

Delete indeces by mask

```json
PUT /_cluster/settings
{
  "transient": {
    "action.destructive_requires_name": true
  }
}

DELETE /<mask>

PUT /_cluster/settings
{
  "transient": {
    "action.destructive_requires_name": false
  }
}
```

Open/Close index

```json
POST /<index name>_close
POST /<index name>_open
```

Policy assignment

```json
PORST _plugins/_ism/add/<mask>
{
  "policy_id": "<policy name>"
}
```

Remove the read only lock

```json
GET /<index name>/_settings

PUT /<index name>/_settings
{
  "index": {
    "blocks": {
      "read_only_allow_delete": false
    }
  }
}

PUT /_all/_settings
{
  "index": {
    "blocks": {
      "read_only_allow_delete": false
    }
  }
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