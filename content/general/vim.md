---
title: "VIM"
draft: false
description: "VIM notes"
---

{{< toc >}}

Enable syntax
_~/.vimrc_

```text
syntax on
```

Enable line numbers
_~/.vimrc_

```text
set number
```

Disable visual mode

```text
:set mouse-=a
```

Jump to column and line

```text
call cursor(15,25)
```

Disable search

```text
:nohl
```

Show hiden characters

```text
:set list
:set nolist
```

Hex mode

```text
:%!xxd
```

Binary mode

```text
vim -b file_name
```

Delete and paste

```bash
ddP
```

## Pluginx

* scrooloose/nerdtree
* itchyny/lightline.vim

## Commands
