---
title: Asterisk
draft: false
description: "CLI commands for Asterisk"
---

Start and connect to asterisk CLI

```bash
asterisk -c
```

Connect to asterisk CLI in background

```bash
asterisk -r
```

Run asterisk command in linux shell

```bash
asterisk -x "command"
```

Verbose

```bash
asterisk -rvvvvv
```

Create the core dump

```bash
asterisk -rg
```

Show the timestamp

```bash
asterisk -rT
```

Restart/Stop

* Now

    ```bash
    core restart now
    ```

* Prevents new calls

    ```bash
    core restart gracefull
    ```

* Does not prevent new calls

    ```bash
    core restart when convinien
    ```

* Aborts a shutdown or restart

    ```bash
    core abort shutdown
    ```

Reload module

```bash
module_name reload
module reload module_name
```

Restart module

```bash
module restart module_name
```

Reload file

```bash
config reload file_name
```

Reload all

```bash
core reload
```
