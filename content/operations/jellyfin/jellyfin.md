---
title: "Jellyfin"
draft: false
description: "Jellyfin notes"
---

{{< toc >}}

## Docker compose + Nvidia

```bash
<install command> nvidia-container-toolkit
nvidia-ctk runtime configure --runtime=docker
```

```yaml
name: MediaServer
services:
  jellyfin:
    image: jellyfin/jellyfin
    container_name: jellyfin
    user: <>:<>
    network_mode: 'bridge'
    ports:
      - 8096:8096
      - 8920:8920
    volumes:
      - jellyfin-config:/config
      - jellyfin-cache:/cache
      - type: bind
        source: /<src-dir>
        target: /<dst dir>
        read_only: true
    restart: 'always'
    environment:
      - JELLYFIN_PublishedServerUrl=http://jellyfin.evaron.local
    runtime: nvidia
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: [gpu]
volumes:
  jellyfin-config:
  jellyfin-cache:
```