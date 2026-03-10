---
title: "PIP"
draft: false
description: "Python PIP configuration notes for using private package repositories like Nexus, including trusted-host and index-url settings."
summary: "Quick reference for configuring pip to work with private artifact repositories, ensuring secure and efficient Python package management."
---

Nexus
_pip.ini_ _pip.conf_

```ini
[global]
trusted-host = <host name>
index = https://<host>/<path>/simple
index-url = https://<host>/<path>/simple
