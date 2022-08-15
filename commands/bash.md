# Bash

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

```nash
echo $!
```

Rename file

```bash
mv /tmp/working-dir/readme.md{,.backup}
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
cat file_name.txt | while read in; do command_line "$in"; done
```

Sequential execution of commands

```bash
command_1; command_2; command_3
```

Parallel execution of commands

```bash
(command_1 &); (command_2 &)
```

Output one command as an argument to another

```bash
command_1 $(command_2)
```

Execute the command without history.

```bash
space command
```

Automatic answer

```bash
yes/no | command
```

Сommand replay

```bash
while true
do
command
done;
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
