---
title: Bash
draft: false
description: "Bash commands"
aliases:
  - /operations/bash
---

EOF

```bash
< dev/null
```

Heredoc

```bash
cat << EOF
  <text> $PWD
EOF
```

```bash
cat > file_name << EOF
  <text> $PWD
EOF
```

```bash
cat << EOF >> file_name
<text>
EOF
```

PID of last process

```bash
echo $!
```

Rename file

```bash
mv /tmp/working-dir/readme.md{,.backup}
rename <>
```

Don't save commands of the current session

```bash
unset HISTFILE
export HISTFILE=/dev/null
export HISTSIZE=0
set +o history
kill -9 $$
```

Clear command history

```bash
history -cw
rm ~/.bash_history
history -r
```

Show last command execution result

```bash
echo $?
```

Show last process pid

```bash
echo $!
```

Executing command for each row

```bash
cat file_name.txt | while read in; do <command_line> "$in"; done
```

Sequential execution of commands

```bash
<command_1>; <command_2>; <command_3>
```

Parallel execution of commands

```bash
(<command_1> &); (<command_2> &)
```

Output one command as an argument to another

```bash
<command_1> $(<command_2>)
```

Execute the command without history.

```bash
space <command>
```

Automatic answer

```bash
yes/no | <command>
```

Сommand replay

```bash
watch <command>
```

Execute the command in another directory and return

```bash
(cd /tmp && ls)
```

Run the command at the specified time

```bash
echo "ls -l" | at midnight
```

Evaluate contents of file

```bash
source <file_name>
. <file_name>
```

Replace

```bash
${<source text>/<pettern>/<replacement>}
```

Run in a single instance

```bash
[ "$(pidof -x $(basename $0))" != $$ ] && exit
```

```bash
/usr/bin/flock -w 0 /tmp/test.lock -c '<file name or command>' || echo "cannot be executed an instance already runs"
```

Error if variable not exist

```bash
rm -rf /${dirname:?}
```

If in one line

```bash
if [[ <condition> ]]; then <command>; else <command>; fi
[[ <condition> ]] && <command>
test <condition> && <command>
```

For in one line

```bash
for <variable> in <list>; do <command>; done
```

No finish if error

```bash
<command> || true
```

Debug

[Information from](https://t.me/bash_help/104)

```bash
#!/bin/bash

trap 'echo "# $BASH_COMMAND";read' DEBUG
```

Read password in variable

```bash
read -s <variable name>
```

End of argument processing for command

```bash
<command> -- <command> <args>
```

Deactivate alias

[Information from](https://t.me/bashdays/47)

```bash
/<command>
'<command>'
"<command>"
<path to binary file>
unalias <alias>
unalias -a
command <command>
```

Вetaching a process from a session

[Information from](https://t.me/bashdays/160)

```bash
Ctrl + Z
bg <pid>
disown <pid>
```

Cron sctipt template

* [Original](https://habr.com/ru/articles/778922/)
* [Fork](https://github.com/pgalonza/Notes-files/blob/main/bash/scripts/cron-template.sh)

## Variables

Separator

```bash
IFS=$"<value>"
```

[Information from](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html)

- PS0 - value of this parameter is expanded like PS1 and displayed by interactive shells after reading a command and before the command is executed.
- PS1 - primary prompt string.
- PS2 - secondary prompt string.

## File descriptors

Open descriptor.

- write
- read
- read and write

```bash
exec <fd>> <file>
exec <fd>< <file>
exec <fd><> <file>
```

Close descriptor

```bash
exec <fd>>&-
exec <fd><&-
```

Merge descriptor

```bash
exec <fd> >&<fd>
exec <fd> <&<fd>
```

Move descriptor

```bash
exec <fd><&<fd>-
```

Read descriptor

```bash
read input <& <fd> && echo "${input}"
```

Open socket

```bash
exec <fd><>//dev/<protocol>/<ip>/<port number>
```

## I/O redirect

Stderr and stdout in file

```bash
<command> > <file> 2>&1
<command> &> <file>
```

Stderr in stdout of console, stdout in file

```bash
<command> 2>&1 > <file>
```

Pipe

```bash
mkfifo <pipe name>
echo "Text" > <pipe name>
cat < <pipe name>
```

Process Substitution

```bash
cat < (echo "Text" >)
```

## Prompt

Label for warn the criticality of the server

```bash
PS1="\@\[\033[38;5;42m\]<server type>\[$(tput sgr0)\]\n[\[$(tput sgr0)\]\[\033[38;5;75m\]\u\[$(tput sgr0)\]@\[$(tput sgr0)\]\[\033[38;5;42m\]\h\[$(tput sgr0)\] \W]\\$ \[$(tput sgr0)\]"
```

## Bash options

Show bash options

```bash
echo $-
```

Arguments in enviroments

```bash
set -k
command <argument>=<value>
```