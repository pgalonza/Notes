---
title: "Java"
draft: false
description: "Practical Java notes covering configuration, logging, and development tips for Java developers. Useful for quick reference and troubleshooting."
summary: "A collection of Java snippets and configuration examples to accelerate your Java projects and improve code quality."
---

set timezone in logback

```xml
<Pattern>
    %d{"yyyy-MM-dd HH:mm:ss.SSS", Europe/Moscow}
</Pattern>
```

## Tunning

[Information from](https://github.com/lebmax/java-custom-container)

```bash
jdeps --ignore-missing-deps -q  \
--recursive  \
--multi-release 25  \
--print-module-deps  \
--class-path 'BOOT-INF/lib/*'  \
target/app.jar > deps.info
```

```bash
jlink \
--add-modules java.base \
--strip-debug \
--compress zip-9 \
--no-header-files \
--no-man-pages \
--output <dir>
```