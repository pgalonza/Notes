---
title: "Gradle"
draft: false
description: "Practical Gradle notes and examples for managing dependencies, caching, and custom tasks in Java projects, including Nexus integration."
summary: "A quick reference for Gradle build scripts, focusing on dependency resolution, custom tasks, and repository configuration for efficient Java development."
---

Download dependencies from nexus for cashing

```groovy
plugins {
    id "java"
}

apply plugin: "java"

repositories {
    maven {
        url: "<repository>"
    }
}

dependencies {
    implementation "<group>:<name>:<version>"
}

task getDeps(type: Copy) {
    from sourceSets.main.runtimeClasspath
    into '<path>/'

    duplicatesStrategy = DuplicatesStrategy.Exlude

    doFirst {
        ant.delete(dir: "<path>")
        ant.mkdir(dir: "<path>")
    }

    doLast {
        ant.delete(dir: "<path>")
    }
}
```
