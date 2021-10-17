# SSH


Executing a command on a remote host
```
ssh user_name@remote_server "comamnd"
```

Copy directory
```
tar -cvj /datafolder | ssh user_name@remote_server "tar -xj -C /datafolder"
```

Wireshark
```
ssh user_name@remote_server 'tcpdump -c 1000 -nn -w - not port 22' | wireshark -k –i
```

Do not execute a remote command
```
ssh -N
```

Allows remote hosts to connect to local forwarded ports
```
ssh -g
```

Requests ssh to go to background just before command execution
```
ssh -f
```

Editing a file via scp
```
vim scp://user_name@remote_server //path_to_file
```

Run remote GUI-application
```
ssh -XYC remote_server program_name
```

Mount local directory to remote host
```
sshfs user_name@remote_serve:/remote_directory /local_directory
```

## SSH Keys

Generate RSA
```
ssh-keygen -f ~/name_key_file_rsa -t rsa -b 2048
```

Generate for paramiko
```
ssh-keygen -m pem -t rsa -C "test"
```

Show RSA host key
```
ssh-keyscan -t rsa host_address
```

Convert for FileZilla
```
puttygen keyname -o keyname.ppk
```

Add fingerprint
```
ssh-keyscan -H <host_name> >> ~/.ssh/known_hosts
```

## SSH Tunneling

### SOCKS-proxy

local host > ssh host > Network
```
ssh -D 0.0.0.0:port_number user_name@remote_server
```

### Port forwarding

local host > ssh host
```
ssh -L 0.0.0.0:port_number:127.0.0.1:port_number user_name@remote_server
```

### Port forwarding to remote host

local host > ssh host > remote host
```
ssh -L 0.0.0.0:port_number:X.X.X.X:port_number user_name@remote_server
```

### Reverse ssh tunnel

ssh host > local host -> (local host > ssh host)
```
ssh -R 0.0.0.0:port_number:127.0.0.1:port_number user_name@remote_server
```

### Reverse ssh tunnel to remote host

remote host < ssh host > local host -> (local host > ssh host > remote host)
```
ssh -R 0.0.0.0:port_number:X.X.X.X:port_number user_name@remote_server
```

### Reverse SOCKS-proxy

Network < ssh host > local host -> (local host > ssh host > Network)
```
ssh -v -R 0.0.0.0:port_number user_name@remote_server
```

### Jumping through the remote hosts

local host > host1 > ssh host
```
ssh -J host1,host2,host3 user_name@remote_server
```

### Dual ssh tunnel
local host > ssh host
remote host > ssh_host

local_host > ssh_host > remote_host
```
ssh -L port_number:127.0.0.1:port_number user_name@remote_server
ssh -R port_number:127.0.0.1:port_number user_name@remote_server
```
