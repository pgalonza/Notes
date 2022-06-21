# Filebeat

Add input
```
- type: log
  enabled: true
  paths:
    - <path_to_log>
  tags:
    - <tag>
  pipeline: <pipeline_name>

```
