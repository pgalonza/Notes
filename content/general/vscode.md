---
title: "Visual Studio Code"
draft: false
description: "VSCode(Visual Studio Code) notes"
---

{{< toc >}}

## Extensions

* **Better Comments** - improve your code commenting by annotating with alert, informational, TODOs, and more.
* **TODO Highlight** - highlight TODO, FIXME and other annotations within your code.
* **Highlight Bad Chars** - extension to highlight bad characters such as No-break space ( ) and the Greek question mark (;) in your source files.
* **Trailing Spaces** - highlight trailing spaces and delete them in a flash.
* **DevOps Extension Pack** - adds language support for Go, HCL (HashiCorp Configuration Language), JSON, Jsonnet, Markdown, Ruby, XML and YAML. Integrates with tools like Chef, Docker, Git, GitHub, Gradle, Kubernetes, Logstash, NGINX, Puppet, and Terraform.
* **GitLens** - supercharges the Git capabilities built into Visual Studio Code.
* **Ident-rainbow** - colorizes the indentation in front of your text alternating four different colors on each step.
* **Ansible** - adds language support for Ansible.
* **autoDocstring** - quickly generate docstrings for python functions.
* **Log File Highlighter** - aadds color highlighting to log files to make it easier to follow the flow of log events and identify problems.
* **RayThis: Instant Beautiful Code Screenshots** - instantly deploy beautiful code snippets to Ray.so without leaving your coding environment.

## Troubleshooting

Activating extension 'ms-python.python' failed: Extension 'ms-python.python' CANNOT use API proposal: terminalShellIntegration.

*.vscode-oss/extensions/ms-python.python-2024.14.1-universal/package.json*
```json
"enabledApiProposals": [
        "terminalShellIntegration"
],
```

*vscode-oss/argv.json*(Configure Runtime Arguments)
```json
"enable-proposed-api": ["ms-python.python"]
```