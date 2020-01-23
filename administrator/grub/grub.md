# Grub
## Linux kernel options
Speculation protection disable
```
GRUB_CMDLINE_LINUX="PR_SPEC_DISABLE_NOEXEC nospectre_v2 nospectre_v1"
```

## Problems
No sound after upgrading to linux 5.4.1
```
GRUB_CMDLINE_LINUX="snd_hda_intel.dmic_detect=0"
```
