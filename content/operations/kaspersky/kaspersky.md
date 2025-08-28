---
title: "Kaspersky"
date: 2025-08-28T22:52:16+03:00
draft: false
description: "Detailed notes and insights about Kaspersky cybersecurity solutions, including antivirus software, endpoint protection, and threat detection technologies. Explore expert analyses, latest updates, and best practices for combating modern cyber threats. Ideal for IT professionals and security enthusiasts."
summary: "Kaspersky Notes: Expert Insights into Cybersecurity Tools & Solutions"
---

{{< toc >}}

## Troubleshooting

### KFL problems on Arch Linux

Problem with docker network

```ini
[Unit]
Description=Run setup_host_firewall.sh
PartOf=docker.service
After=docker.service

[Service]
Type=oneshot
ExecStart=iptables -t raw -I PREROUTING -i lo -j ACCEPT
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

Problem with suspend

```bash
sudo chmod -x /usr/lib/systemd/system-sleep/kfl_hook.sh
```

```ini
[Unit]
Before=sleep.target
StopWhenUnneeded=yes
[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=-/opt/kaspersky/kfl/bin/kfl-control --stop-task 1
ExecStop=-/opt/kaspersky/kfl/bin/kfl-control --start-task 1
[Install]
WantedBy=sleep.target
```





