#!/bin/sh
RESULT=$(mount -v | grep -i -e 'type smb' -e 'type cifs')
if [ -n "$RESULT" ]; then
  exit
else
  mount -a
fi
