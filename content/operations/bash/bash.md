---
title: "Bash"
draft: false
---

## Prompt

Label for warn the criticality of the server

```bash
PS1="\@ \[\033[38;5;42m\]<server type>\[$(tput sgr0)\]\n[\[$(tput sgr0)\]\[\033[38;5;75m\]\u\[$(tput sgr0)\]@\[$(tput sgr0)\]\[\033[38;5;42m\]\h\[$(tput sgr0)\] \W]\\$ \[$(tput sgr0)\]"
```
