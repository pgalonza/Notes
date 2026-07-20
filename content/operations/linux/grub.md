---
title: "Grub"
draft: false
description: "Grub notes"
aliases:
  - /operations/grub/grub/
---

{{< toc >}}

## Edit in Grub menu

1. Choose edit in Grub menu
2. Add in linux line `init=/bin/bash`
3. Change ro to rw
4. Remove single, splash and quiet words

## Generate configuration file

```bash
grub-mkconfig -o /boot/grub2/grub.cfg
```

## Linux kernel options

Speculation protection disable

```text
GRUB_CMDLINE_LINUX="mitigations=off"
```

older then5.1.13

```text
GRUB_CMDLINE_LINUX="PR_SPEC_DISABLE_NOEXEC nospectre_v2 nospectre_v1"
```

## Troubleshooting

No sound after upgrading to linux 5.4.1

```text
GRUB_CMDLINE_LINUX="snd_hda_intel.dmic_detect=0"
```
