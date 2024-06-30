---
title: "Vector"
draft: false
description: "Vector-agent notes"
---


Convert Json  to fields

```yaml
transforms:
  transform_message:
    type: remap
    inputs:
      - source_*
    source: |-
      . = parse_json(.message)
```

Add tags

```yaml
transforms:
  general_tags:
    type: remap
    inputs:
      - transform_message
    source: |-
      .environment = "development"
      .label = ["app"]
      .hostname = get_hostname!()
      .host_address = get_env_var!("HOST_ADDRESS")
  tags_nginx:
    type: remap
    inputs:
      - general_tags
    source: |-
      .application = "nginx"
```
