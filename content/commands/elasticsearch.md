---
title: "ElasticSearch"
draft: false
---

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
