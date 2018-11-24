rem @ECHO OFF
net stop "1C:Enterprise 8.3 Server Agent (x86-64)"
timeout /T 10
taskkill /IM  rphost.exe /F
