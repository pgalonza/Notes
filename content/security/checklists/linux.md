---
title: "Linux"
date: 2025-04-10T00:15:59+03:00
draft: false
description: "Comprehensive Linux security checklist to help you fortify your system against threats. From basic configurations to advanced hardening techniques, these step-by-step guides ensure your Linux environment remains secure and compliant."
summary: ""
---

{{< toc >}}

- [ ] Access control
    - [ ] Accounts without empty passwords
    - [ ] Disable root login
    - [ ] Restricting access to the SU and SUDO command
    - [ ] Limiting the list of sudo commands for accounts
    - [ ] Restricting access to performance events
    - [ ] System accounting with auditd
    - [ ] No Non-Root accounts have UID 0
    - [ ] Noowner files
    - [ ] Kerberos
    - [ ] World-Writable files
    - [ ] Disable USB/firewire/thunderbolt devices
- [ ] Distributions security
    - [ ] Minimize software to minimize vulnerability
    - [ ] One network service per system or vm instance
    - [ ] Use linux security extensions
    - [ ] Delete X Window Systems (X11)
    - [ ] Configure firewall
    - [ ] Separate Disk Partitions
    - [ ] Disk Quotas
    - [ ] Disable unwanted SUID and SGID binaries
    - [ ] Logging and Auditing
- [ ] Kernel
    - [ ] Keep linux kernel and software up to Date
    - [ ] Restrict access to the kernel log
    - [ ] The core addresses in /proc and other interfaces are zero
    - [ ] Initializing dynamic core memory to zero when allocating it
    - [ ] Disabling mounting the debugfs virtual file system
    - [ ] Disabling the kexec_load system call
    - [ ] Restriction on the use of user namespaces
    - [ ] Prohibiting the bpf system call for unprivileged users
    - [ ] Prohibiting the userfaultfd system call for unprivileged users
    - [ ] Prohibition of automatic loading of kernel modules responsible for maintaining
    - [ ] Disabling Transactional Synchronization Extension (TSX) technology
    - [ ] Configuring user space protection from the Linux kernel
    - [ ] Prohibiting connection to other processes using ptrace
    - [ ] Limitation unsafe symlinks and hardlinks options
    - [ ] Enabling protection against unintentional writes to the FIFO object
    - [ ] Enabling protection against unintentional writing to a file
    - [ ] Prohibiting the creation of coredumps for certain executable files
