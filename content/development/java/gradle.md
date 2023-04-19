---
title: "Gradle"
draft: false
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
