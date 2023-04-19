---
title: "Docker"
draft: false
---

```bash
docker run --rm  --name container_name  -p 80:80 -v path_in_host:path_in_container tag/name:tag

docker build -t tag/name:tag -f DockerFile .

docker exec -it container_name bash

docker rmi $(docker images -q -f dangling=true)
```
