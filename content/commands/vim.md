---
title: "Vim"
draft: false
---

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
