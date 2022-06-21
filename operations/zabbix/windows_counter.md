# Windows counters
Path in the registry
```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Perflib\009
```

Get the value
```
typeperf -q ""
```

Re-creating counters
```
lodctr /r
```
