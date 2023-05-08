---
title: Ansible
draft: false
description: "CLI commands for Ansible"
---

Start as another user

```bash
ansible-playbook -i hosts.yml, -e 'ansible_ssh_user=<uuser_name> ansible_python_interpreter=/usr/bin/python3' --ask-pass -b --ask-become-pass ansible_user.yaml
```

Test inventory

```bash
ansible -i hosts.yml all --list-hosts
```

Ping the hosts

```bash
ansible all -m ping
```

Create role structure

```bash
ansible-galaxy init -p playbooks/roles <role_name>
```

Get facts:

```bash
ansible all -i hosts.yml --user <ssh_uaser_name> --key-file <ssh_key> -m setup
```
