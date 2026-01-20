---
title: "Fish-shell"
draft: false
description: "Fish-shell notes"
aliases:
  - /general/fish/
---

Executable path
_~/.config/fish/config.fish_

```bash
set -a PATH $PATH
```

```bash
set -U fish_user_paths <path> $fish_user_paths
```

Make fish to default

```bash
echo /usr/local/bin/fish | sudo tee -a /etc/shells
chsh -s /usr/local/bin/fish
```

Update man page completions

```bash
fish_update_completions
```

Fish settings

```bash
fish_config
```
