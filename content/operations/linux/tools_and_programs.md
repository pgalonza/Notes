---
title: "Tools and Programs"
draft: false
description: "Comprehensive list of Linux command-line tools and utilities for system administration, monitoring, networking, and recovery tasks."
summary: "A curated reference of essential Linux tools, from tmux and rsync to monitoring utilities and forensic software, to boost your productivity."
---

{{< toc >}}

* **tmux** - terminal multiplexer.
* **rsync** - a fast, versatile, remote (and local) file-copying tool.
* **lsof** - show list open files.
* **dstat** - versatile tool for generating system resource statistics.
* **xrdp** -  a RDP server.
* **PWGEN** - generate pronounceable passwords.
* **MAKEPASSWD** - generate and/or encrypt passwords.
* **aspell** - interactive spell checker
* **hunspell** - spell checker, stemmer and morphological analyzer.
* **screenfetch** - fetches system/theme information in. terminal for Linux desktop screenshots.
* **strings** - print the sequences of printable characters in files.
* **sshpass** - noninteractive ssh password provider.
* **neofetch** - displays information about your operating system, software and hardware in an aesthetic and visually pleasing way.
* **xsel/xclip** - command line interface to the X11 clipboard.
* **jq** - command-line JSON processor.
* **rkhunter** - RootKit Hunter.
* **chkrootkit** - RootKit Hunter.
* **qrencode** - encode input data in a QR Code and save as a PNG image.
* **taskset** - set or retrieve a process's CPU affinity.
* **tr** - translate or delete characters.
* **exec** - execute command in current process.
* **eval** - evaluate the specified commands.
* **tee** - read from standard input and write to standard output and files.
* **script** - record the terminal session.
* **expect** - programmed dialogue with interactive programs.
* **xdotool** - X11 automation tool.
* **wait** - wait for jobs to complete.
* **tty-share** - share terminal.
* **envsubst** - substitutes environment variables in shell format strings.
* **fwupd** - firmware update tool.
* **mktemp** - create a temporary file or directory.
* **flock** - manage locks from shell scripts.
* **enable** - enable and disable shell builtins.
* **lastb** - show last logged users.
* **ttyd** - share terminal in web.
* **findmnt** - find a filesystems.
* **setsid** - run a program in a new session.
* **sleuthkit** - forensics tools for investigate volume and file system.
* **comm** - compare two sorted files line by line.
* **auditctl** - a utility to assist controlling the kernel's audit system.
* **inotifywait** - monitor filesystem change events.
* **getcap** - display the capabilities of a file.
* **notify-send** - send desktop notifications.

## CPU

* **chcpu** - configure CPUs.
* **nproc** - print the number of processing units available.

## RAM

* **vmstat** - report virtual memory statistics.
* **zram** -  linux kernel feature and userspace tools for creating compressible RAM-based block devices.
* **valgrind** - instrumentation framework for building dynamic analysis tools.

## Monitoring

* **iostat(sysstat)** - report (CPU) statistics and I/O statistics for devices, partitions and NFS.
* **htop** - interactive process viewer.
* **atop** - AT Computing's System & Process Monitor.
* **tcptrack** - monitor TCP connections on the network.
* **trafshow** - full screen show network traffic.
* **ifstat** - report InterFace statistics.
* **iftop** - display bandwidth usage on an interface by host.
* **ioping** - simple disk I/O latency monitoring tool.
* **iptraf** - interactive Colorful IP LAN Monitor.
* **nload** - displays the current network usage.
* **nethogs** - net top tool grouping bandwidth per process.
* **bmon** - portable bandwidth monitor and rate estimator.
* **bwm-ng** - a live bandwidth monitor for network and disk io.
* **fswatch** - file change monitoring tool.
* **ttop** - system monitoring tool.

## Processes

* **pidof** - find the process ID of a running program.
* **fuser** - find processes using files or sockets.

## Environment

* **env** - run a program in a modified environment.
* **setenv** - change or add an environment variable.
* **export** - set the export attribute for variables.
* **set** - display and change shell variables.

## Recovery

* **testdisk** - recovery software.
* **photorec** - recovery software.

## Network

* **iPerf** - perform network throughput tests.
* **wget** - the non-interactive network downloader.
* **curl** - transfer data from or to a server.
* **tcpdump** - dump traffic on a network.
* **tshark** - dump and analyze network traffic.
* **mtr** - a network diagnostic tool.

## Disk

* **fio** - flexible I/O tester.
* **cfdisk** - display and manipulate a disk partition table.
* **nvme-cli** -  storage command line interface utility.

## SIP

* **sipp** - SIP testing tool and traffic generator.
* **sngrep** - SIP Messages flow viewer.

## SHELL

* **fish** - friendly interactive shell.
* **fzf** - general-purpose command-line fuzzy finder.
* **whiptail** - display dialog boxes from shell scripts.

## Android

* **adb** - Android Debug Bridge.
* **fastboot** - Android Fastboot.
* **[scrcpy](https://github.com/Genymobile/scrcpy)** - display and control your Android device.
* **[localdesktop](https://localdesktop.github.io/)** - run Linux GUI apps on Android.

## Utilities

* **simple-http-server** - serve files via HTTP (`python -m SimpleHTTPServer` or `python3 -m http.server`).
* **uuidgen** - create a new UUID value.
* **nginx** - HTTP and reverse proxy server.
* **ldconfig** - configure dynamic linker run-time bindings.
* **man** - display system reference manual pages.
* **tree** - display directory tree.

## Chromium

* **chromium** - open-source web browser.

```bash
# Proxy
chromium --proxy-server="socks://host:9050"

# Discards page
browser://discards
chrome://discards

# Task manager
Shift + ESC

# Chrome Flags
browser://flags/

# GPU information
browser://gpu/
```

## Ffmpeg

* **ffmpeg** - multimedia framework.

```bash
# Video from RTSP
ffmpeg -y -re -acodec pcm_s16le -rtsp_transport tcp -i rtsp:// -vcodec copy -af asetrate=22050 -acodec aac -b:a 96k -t 15 tmp/test.mp4

# Screenshot from RTSP
ffmpeg -rtsp_transport tcp -i rtsp:// -f image2 -vf fps=fps=1 -t 0.001 -ss 00:00:3 tmp/image.png

# Use find
FFMPEG_COMMAND="ffmpeg -hide_banner -loglevel error -y"
find . -type f -name "*.mp4" -print0 | while read -r -d '' file_name; do
    echo $file_name
    $FFMPEG_COMMAND -nostdin -i "$file_name" <params> - | $FFMPEG_COMMAND -i - -i "$file_name" <params> "${file_name/.mp4/}-dpni_fixed.mp4"
done
```

## Youtube-dl / yt-dlp

* **youtube-dl / yt-dlp** - download videos from YouTube and other sites.

```bash
# Best video
youtube-dl -f bestvideo+bestaudio 'url'

# Best audio
youtube-dl -f bestaudio 'url'

# List of formats
youtube-dl -F 'url'
```

## Sox

* **sox** - Sound eXchange, audio processing tool.

```bash
# Convert to VoIP format
sox -V vm-intro.wav -r 8000 -c 1 -t ul vm-intro.ulaw
sox -V vm-intro.wav -r 8000 -c 1 -t al vm-intro.alaw
sox -V vm-intro.wav -r 8000 -c 1 -t gsm vm-intro.gsm
```

## Benchmark

* **fio** - flexible I/O tester.

```bash
# Read
fio --name=randread --ioengine=libaio --iodepth=16 --rw=randread --bs=4k --direct=0 --size=512M --numjobs=4 --runtime=240 --group_reporting

# Write
fio --name=randwrite --ioengine=libaio --iodepth=1 --rw=randwrite --bs=4k --direct=0 --size=512M --numjobs=4 --runtime=240 --group_reporting

# Read & Write
fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=random_read_write.fio --bs=4k --iodepth=64 --size=4G --readwrite=randrw --rwmixread=75
```

## Curl

* **curl** - transfer data from or to a server.

```bash
# REST API get
curl --include --location --request GET 'https://site_name/?fields=parameter_name' --header 'Authorization: OAuth id'

# Formatting JSON answer
curl --location --request GET 'https://site_name/?fields=parameter_name' --header 'Authorization: OAuth id' | python -m json.tool

# Download file
curl --location --remote-name https://<url to file>
```

## QEMU

* **qemu** - generic and open source machine emulator and virtualizer.

```bash
# LiveUSB
qemu-system-x86_64 -hda /dev/sdX
```

## Kubectl

* **kubectl** - Kubernetes command-line tool.

```bash
# Network utils
kubectl run -it --rm --image amouat/network-utils test bash
```

## Scl

* **scl** - Software Collections tool.

```bash
# Activate python environment
scl enable rh-python<version_number> bash
```

## Man

* **man** - display system reference manual pages.

```bash
# Description of the filesystem hierarchy
man hier

# ASCII table
man ascii
```

## Certbot

* **certbot** - automatic certificate management from Let's Encrypt.

```bash
# Create certificate
certbot certonly --config ./certbot.ini --email <e-mail address> --work-dir </var/lib/letsencrypt> --config-dir <where save data> --domain <domain_name>

# Renew certificate
certbot renew --work-dir </var/lib/letsencrypt> --config-dir <where save data>
```

_certbot.ini_

```text
authenticator = standalone
noninteractive = true
agree-tos = true
rsa-key-size = 2048
```
