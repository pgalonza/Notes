---
title: "Ansible"
draft: false
---
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

## Module

Own module

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

Execute sudo in systemd module for work with sudoers

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
