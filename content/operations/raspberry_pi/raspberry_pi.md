---
title: "RaspberryPI"
draft: false
---

Grid of cameras

```bash
#!/bin/bash
setterm -cursor off
#stream1
st1=`ps -ef | grep omxplayer | grep stream1 | cut -d'-' -f2 | cut -d' ' -f2`
echo "Checking & Starting Screen 1";
if [ "$st1" = "stream1" ];
 then
  echo "Running Stream1..";
 else
  echo "Starting Stream1..";
  screen -dmS stream1 sh -c 'omxplayer --adev hdmi --aidx -1 --live --refresh --video_queue 8 --fps 20 --win "0 0 1440 810" rtsp://'; #x1 y1 x2 y2
fi
```
