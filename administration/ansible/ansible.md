# Ansible

Install ansible for developing on Windows

```texts
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

```yaml
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
