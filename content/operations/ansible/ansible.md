---
title: "Ansible"
draft: false
description: "Ansible information"
---

{{< toc >}}

Install ansible for developing on Windows

```bash
git clone -b <branch_name or tag_name> https://github.com/ansible/ansible.git
pip intall -e ansible
```

Other host by index

```text
{{ groups['<group1>'][groups['<group2>'].index(inveentory_hostname)] }}
```

Variable of other host by index

```text
hostvars[groups['<group1>'][groups['<group2>'].index(inveentory_hostname)]].<variable name>
```

Get variable by name

```text
{{ lookup('vars', '<variable_name>') }}
```

Default value if not exist

```text
{{ <variable_name> | default(<value>) }}
```

Search local file

```text
pattern: "<pattern_match>"
file: "{{ lookup('fileglob'), pattern }}"
```

Regexp

```text
{{ <variable> | regex_search('<pattern>') }}
```

Handling errors

[Doc](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_debugger.html)

```yaml
 - name: Handle the error
   block:
    - <tasks>
   rescue:
    - <tasks>
    - name: Run all handlers
      meta: flush_handlers
   always:
     - <tasks>
```

Async

[Doc](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_async.html)

```yaml
  - name: <Job name>
    async: <how long wait>
    poll: <how often to poll>

  - name: Check on an async task
    async_status:
      jid: "{{ yum_sleeper.ansible_job_id }}"
    register: job_result
    until: job_result.finished
    retries: <count of attempts>
    delay: <how often to retry>
```

## Commands

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

Ad-hoc

```bash
ansible -i <host file> -m <module name> -a <module parameters> <host or group>
```

## Module

### Own module

```python
#!/usr/bin/env python
from ansible.moddule_utils.basic import AnsibleModule

def main()
  moddule = AnsibleModule(
    argument_spec=dict(
      <variable_name1>=dict(requred=True, type='str'),
      <variable_name2>=dict(requred=True, type='str',
                            choices=['<choice1>', 'choice2']),
      <variable_name3>=dict(requred=False, type='str', default=None),
    ),
    supports_check_mode=True
  )

  if module.check_mode:
    module.exit_json(changed=False)

  if <result>:
    module.exit_json(
      changed=True,
      msg=<message>
    )
  else:
    module.fail_json(
        changed=False,
        msg=<message>
    )

if __name__ == "__main__":
  main()
```

### Execute sudo in systemd module for work with sudoers

in main function

```python
argument_spec=dict(
    ...
    root_privileges=dict(type='bool'), # <- add parameter
),
```

variable with sudo or empty string, it concatenate with commands below

```bash
if module.params['root_privileges']:
    root_command = "sudo "
else:
    root_command = ""
```

add root_command to all functions module.run_command

```bash
module.run_command("%s%s daemon-reload" % (root_command, systemctl))
module.run_command("%s%s daemon-reexec" % (root_command, systemctl))
module.run_command("%s%s show '%s'" % (root_command, systemctl, unit))
module.run_command("{root_command}{systemctl} list-unit-files '{unit_search}*'".format(systemctl=systemctl, unit_search=unit_search))
module.run_command("{root_command}{systemctl} is-active '{unit}'".format(root_command=root_command, systemctl=systemctl, unit=unit))
module.run_command("%s%s is-enabled '%s'" % (root_command, systemctl, unit))
module.run_command("%s%s list-unit-files '%s'" % (root_command, systemctl, unit))
module.run_command(root_command+systemctl, check_rc=True)
module.run_command("%s%s is-enabled '%s'" % (root_command, systemctl, unit))
module.run_command("%s%s %s '%s'" % (root_command, systemctl, action, unit))
module.run_command("%s%s is-enabled '%s' -l" % (root_command, systemctl, unit))
module.run_command("%s%s %s '%s'" % (root_command, systemctl, action, unit))
module.run_command("%s%s %s '%s'" % (root_command, systemctl, action, unit))
```

## Collections

* [pgalonza.linux](https://github.com/pgalonza/linux-collection)