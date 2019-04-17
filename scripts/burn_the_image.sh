#! /bin/bash
sudo dd oflag=direct status=progress  if=image.iso of=/dev/sd* bs=1M; sync
