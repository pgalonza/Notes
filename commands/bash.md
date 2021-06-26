# Bash

EOF
```
< dev/null
```

Heredoc
```
cat << EOF
  <text> $PWD
EOF
```

PID of last process
```
echo $!
```

Rename file
```
mv /tmp/working-dir/readme.md{,.backup}
```

Don't save commands of the current session
```
unset HISTFILE
export HISTFILE=/dev/null
export HISTSIZE=0
set +o history
kill -9 $$
```

Clear command history
```
history -cw
rm ~/.bash_history
history -r
```

Show last command execution result
```
echo $?
```

Show last process pid
```
echo $!
```

Executing command for each row
```
cat file_name.txt | while read in; do command_line "$in"; done
```

Sequential execution of commands
```
command_1; command_2; command_3
```

Parallel execution of commands
```
(command_1 &); (command_2 &)
```

Output one command as an argument to another
```
command_1 $(command_2)
```

Execute the command without history.
```
space command
```

Automatic answer
```
yes/no | command
```

Сommand replay
```
while true
do
command
done;
```

Execute the command in another directory and return
```
(cd /tmp && ls)
```

Run the command at the specified time
```
echo "ls -l" | at midnight
```

Evaluate contents of file
```
source <file_name>
. <file_name>
```
