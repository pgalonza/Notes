# Asterisk
Start and connect to asterisk CLI
```
asterisk -c
```

Connect to asterisk CLI in background
```
asterisk -r
```

Run asterisk command in linux shell
```
asterisk -x "command"
```

Verbose
```
asterisk -rvvvvv
```

Create the core dump
```
asterisk -rg
```

Show the timestamp
```
asterisk -rT
```

Restart/Stop
* Now
```
core restart now
```

* Prevents new calls
```
core restart gracefull
```

* Does not prevent new calls
```
core restart when convinien
```

* Aborts a shutdown or restart
```
core abort shutdown
```

Reload module
```
module_name reload
module reload module_name
```

Restart module
```
module restart module_name
```

Reload file
```
config reload file_name
```

Reload all
```
core reload
```
