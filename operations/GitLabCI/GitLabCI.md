# GitLab CI

## Add new runner for project

Create runner for project
```
cd /bin
cp gitlab-runner gitlab-runner-<project_name>
chmod 755 /usr/bin/gitlab-runner-<project_name>
```

Create user
```
sudo useradd --comment 'GitLab Runner' --create-home <project_name>-build --shell /bin/bash
```

Check user
```
sudo su - <project_name>-build
```

Install gitlab runner
```
gitlab-runner-<project_name> install --user=<project_name>-build --working-directory=/home/<project_name>-build --service gitlab-runner-<project_name> --config /etc/gitlab-runner/gitlab-runner-<project_name>.toml
```

Register runner
```
gitlab-runner-<project_name> register --config /etc/gitlab-runner/gitlab-runner-<project_name>.toml
```

Start runner
```
systemctl start gitlab-runner-<project_name>
```

## Ansible

SSH key
```
script:
  - eval $(ssh-agent -s)
  - echo "$SSH_PRIVATE_KEY" | tr -d '\r' | ssh-add -
  - mkdir -p ~/.ssh
  - chmod 700 ~/.ssh
  - echo "$SSH_KNOWN_HOSTS" >> ~/.ssh/known_hosts
  - chmod 644 ~/.ssh/known_hosts
```

SSH key no docker
```
script:
  - eval $(ssh-agent -s)
  - echo $SSH_AGENT_PID > ssh_agent.pid
  - echo "$SSH_PRIVATE_KEY" | tr -d '\r' | ssh-add -
  - mkdir -p ~/.ssh
  - chmod 700 ~/.ssh
  - echo "$SSH_KNOWN_HOSTS" >> ~/.ssh/known_hosts
  - chmod 644 ~/.ssh/known_hosts
after_script:
  - kill $(cat ssh_agent.pid)
```

## Troubleshooting

Skipping cache extraction due to empty cache
_config.toml_
```
cache_dir =
```

Value type file
```
open(file_name, encoding='utf-8-sig')
```
