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
