---
title: "Nintendo Switch"
date: 2024-01-12T01:20:08+03:00
draft: false
description: "Nintendo Switch information about CFW, payloads, homebrew, modchip, sigpatches."
---

{{< toc >}}

* [Gbatemp](https://gbatemp.net/forums/nintendo-switch.283/)
* [4pda](https://4pda.to/forum/index.php?showtopic=900987)
* [SwitchBrew](https://switchbrew.org/wiki/Main_Page)
* [Jits](https://jits.site/)
* [GameBrew](https://www.gamebrew.org/wiki/List_of_Switch_Homebrew_Applications)
---
* RCM - Recovery Mode allows Nintendo to send the switch commands. [GitHub](https://github.com/NVIDIA/tegrarcm)
* sysNand/sysMMC - system NAND, Nintendo Switch internal memory storage.
* emuNAND/emuMMC - emulated NAND. emulating Nintendo Switch “internal memory storage” which contain OS and everything else into a MicroSD card.
* amiibo - interactive figures and cards that work with your games.
* Dongle - method to enter in RCM. (Do not need for Chip Mod)
* ninfs - FUSE filesystem Python scripts. [GitHub](https://github.com/ihaveamac/ninfs)
* nxdumptool - Generates XCI/NSP/HFS0/ExeFS/RomFS/Certificate/Ticket dumps gamecards and installed SD/eMMC titles. [GitHub](https://github.com/DarkMatterCore/nxdumptool)

## Tesla Overlay System

Allows to access a menu of various homebrew applications and plugins.

* Tesla-Menu - overlay menu. [GitHub](https://github.com/WerWolv/Tesla-Menu)
* nx-ovlloader - sys-module, host process for loading overlay OVLs (NROs). [GitHub](https://github.com/WerWolv/nx-ovlloader)

## Overlays

* sys-patch - system module for patches(SigPatche) fs, es, ldr and nifm on boot. [Gbatemp](https://gbatemp.net/download/sys-patch-latest-binary.38492/)
* EdiZon - using cheats. [GitHub](https://github.com/WerWolv/EdiZon)
* sys-clk - overclocking/underclocking system module. [GitHub](https://github.com/retronx-team/sys-clk)

## Payload

Send command or binary file (the payload) to the Nintendo Switch in Recovery mode (RCM). Software writes on C/C++ for AArch64 Cortex A57 CPU SoC Tegra X1.

* Lockpick_RCM - bare metal Nintendo Switch payload that derives encryption keys for use in Switch file handling software without booting HOS. [GitLab](https://gitgud.io/LP/lockpick_rcm) [Codeberg](https://codeberg.org/Lockpick/Lockpick_RCM)
* TegraExplorer - payload-based file manager. [GitHub](https://github.com/suchmememanyskill/TegraExplorer)
* SX Gear/PRO - SX Gear is payload injector dongle for the Nintendo Switch.
* NS-USBloader - Awoo Installer and GoldLeaf uploader of the NSPs, RCM payload injector. [GitHub](https://github.com/developersu/ns-usbloader)
* ArgonNX-SE - GUI payload chainloader. [GitHub](https://github.com/Storm21CH/ArgonNX-SE)


## Homebrew

Unoffical software

* JKSV - JK's Save Manager Switch Edition. [GitHub](https://github.com/J-D-K/JKSV)
* nx-hbmenu - the Nintendo Switch Homebrew Menu. [GitHub](https://github.com/switchbrew/nx-hbmenu)
* hb-appstore - Homebrew App Store. [GitHub](https://github.com/fortheusers/hb-appstore)
* nx-hbloader - host process for loading Homebrew NROs. [GitHub](https://github.com/switchbrew/nx-hbloader)
* nx-hbmenu - the Nintendo Switch Homebrew Menu. [GitHub](https://github.com/switchbrew/nx-hbmenu)
* 90DNS Tester - simple homebrew application to test DNS. [GitHub](https://github.com/meganukebmp/Switch_90DNS_tester/)
* libnx - library for development Homebrew. [GitHub](https://github.com/switchbrew/libnx)
* LayeredFS - homebrew virtual file system for replace games use TitleID.
* Goldleaf - multipurpose homebrew tool. [GitHub](https://github.com/XorTroll/Goldleaf)
* Linkalho - homebrew app that will link NNID accounts offline. [GitHub](https://github.com/rdmrocha/linkalho)
* dbi - install NSP, NSZ, XCI and XCZ from various sources. [GitHub](https://github.com/rashevskyv/dbi)
* Haku33 - perform a hard reset. [GitHub](https://github.com/StarDustCFW/Haku33)
* Goldleaf - multipurpose homebrew tool. [GitHub](https://github.com/XorTroll/Goldleaf)
* AtmoPackUpdater - homebrew which update your CFW/Firmware/Homebrews/Sigpatches. [GitHub](https://github.com/PoloNX/AtmoPackUpdater)

## Firmware

* Caffeine/Nereba - name of excploit and software vulnerability.

### Official

* HOS - Horizon OS or Switch OS

### Bootloader

* Hekate - bootloader with GUI and many features. [GitHub](https://github.com/CTCaer/hekate)
* hekate_boot_dat -create a SX boot.dat from hekate[GitHub](https://github.com/mondul/hekate_boot_dat)

### Custom

* GNX - Brazilian All-in-One CFW package. [GitHub](https://github.com/vncsmnl/GNX)
* Santa-Claus - [Site](https://santa-atmo.ru/nintendo-switch/)
* Atmosphère - customized firmware for the Nintendo Switch. [GitHub](https://github.com/Atmosphere-NX/Atmosphere)
* SX OS - Features like the XCI Loader require an SX OS license.
* Ultra - [GitHub](https://github.com/Ultra-NX/Ultra)
* Switch OC Suite - Overclocking suite running Atmosphere CFW. [GitHub](https://github.com/hanai3Bi/Switch-OC-Suite)
* Kefir - [Codeberg](https://codeberg.org/rashevskyv/kefir)
* 4IFIR - ultimate CFW for overlocking. [GitHub](https://github.com/rashevskyv/4IFIR?tab=readme-ov-file#)
* Hats - pack containing the latest version of Hekate, Atmosphere and its Signature Patches. [Codeberg](https://codeberg.org/sthetix/HATS)
* NeXT - another AIO Pack. [Codeberg](https://codeberg.org/vampitech/NeXT/releases/tag/3.05)
* DeepSea - the new All-in-One CFW package. [GitHub](https://github.com/Team-Neptune/DeepSea)
* ShallowSea - AIO CFW package for the. [Codeberg](https://codeberg.org/carcaschoi/Shallowsea)
* Atmosphere-with-Hekate - Hekate and Atmosphere only. [GitHub](https://github.com/yyoossk/Atmosphere-with-Hekate)
* Arquivos-JNX - additional file. [GitHub](https://github.com/JuniorPassos/Arquivos-JNX)
---
* Kefir Updater - update your CFW, sigpatches, cheat codes, firmwares and more. [GitHub](https://github.com/rashevskyv/kefir-updater)
* AIO-Switch-Updater - update your CFW, cheat codes, firmwares and more. [GitHub](https://github.com/HamletDuFromage/aio-switch-updater)
* emuMMC - SDMMC driver replacement for Nintendo's Filesystem Services. [GitHub](https://github.com/m4xw/emuMMC)
* [sigmapatches](https://sigmapatches.su/)

### SigPatch

Signature patches, es/fs/ips/acid/loader-pathes. Digital signatures that allow unsigned code to run on the horizon operating system. Use sys-patch if problem with it.

* [sigmapatches](https://sigmapatches.su/)

## ModChip and HW

* SX Core/SX Lite - glitch methods GitHublike PicoFly. [GitHub](https://github.com/Spacecraft-NX/firmware)
* HWFLY - glitch methods like PicoFly. [GitHub](https://github.com/hwfly-nx/firmware)
* Erista/Mariko - names of SoC(System on Chip) NVIDIA Tegra X1 revisions.
* Fuses - physical component on the board, that can be physically burned away. It`s security mechanism which preventing downgrade OFW.
---
* Glitching the Switch - CCC - [YouTube](https://www.youtube.com/watch?v=b-SeoIe1sKM), [media.ccc.de](https://media.ccc.de/v/c4.openchaos.2018.06.glitching-the-switch), [YouTube](https://www.youtube.com/watch?v=L3PPWVPg2WI)
* fusee-nano - minimalist re-implementation of the Fusée Gelée exploit, designed to run on embedded Linux devices. [GitHub](https://github.com/DavidBuchanan314/fusee-nano)
* fusee-launcher - reference implementation launcher for the Fusée Gelée Tegra X1 bootROM exploit. [GitHub](https://github.com/Qyriad/fusee-launcher)
* Fusée Gelée - name of excploit and hardware vulnerability. [GitHub](https://github.com/Qyriad/fusee-launcher/blob/master/report/fusee_gelee.md), [SecurityLab](https://www.securitylab.ru/analytics/545182.php)
* Glitch - is an activity in which a person finds and exploits flaws or glitches in programs and devices to achieve something that was not intended by the designers and developers. [Habr](https://habr.com/ru/companies/ntc-vulkan/articles/480500/)
* CVE-2020-15808
* CVE-2018-6242

### PicoFly

RP2040 microcontroller designed here at Raspberry Pi for load Hekate, enter in RCM, transfer payload via Glitch method.

* Load payload.bin from root sd-card
* Not needed transder payload from PC
* Not needed boot.dat and boot.ini it`s for SX Gear.
---
* [GitHub Source](https://github.com/rehius/usk)
* [GitHub Source](https://github.com/Ansem-SoD/Picofly)
* Glitching the CPU to make it fail a check, which allows booting from an unsigned payload that will then run higher level software.

## DNS

Mikrotik

```bash
add address=127.0.0.1 regexp=".*\\.nintendo\\..*"
add address=127.0.0.1 regexp="^nintendo\\..*"
```

EMUMMC

[emummc.txt](https://nh-server.github.io/switch-guide/files/emummc.txt)

```txt
127.0.0.1 *nintendo*
127.0.0.1 receive-%.dg.srv.nintendo.net receive-%.er.srv.nintendo.net
127.0.0.1 *nintendo-europe.com
127.0.0.1 *nintendoswitch.*
```

## Backup

eMMC with DD

1. Enter to Hekate
2. Go to Tools > USb-tools
3. In USB MASS STORAGE press eMMC RAW GPP
4. Run partes -l or fdisk -l and look disk device
5. Execute dd command
    ```bash
    dd if=/dev/sd<a-z> of=/ieMMC.img bs=5M status=progress
    ```
6. Do that for boot0 and boot1

## Games

Witcher 3 saves from PC

1. Intall JKSV
2. Create Backup of game save
3. Enter to directory on computer C:\Users\<user name>\Documents\The Witcher 3\gamesaves
4. Connect SD Card to PC
5. Go to /JKSV/<game dir>/<backup>/ on SD-Card
6. Copy saves
7. Restore backup in JKSV

Install via DBI

1. Edit configuration in SD-Card /switch/DBI/dbi.config
    ```ini
    [Network sources]
    <name>=ApacheHTTP|http://<ip or hostname>/Nintendo/Switch/
    ```
2. Create Nginx configuration switch.conf
    ```conf
    server {
        listen       80 default_server;

        charset UTF-8;
        location /Nintendo/Switch/ {
            root   /Nintendo/Switch;
            index  index.html index.htm;
            autoindex on;
        }
    }
    ```
3. Run Nginx use docker
    ```bash
    docker run --rm --name nginx -p 8000:80 -v <games directiry>:/Nintendo/Switch:ro -v ./switch.conf:/etc/nginx/conf.d/default.conf:ro nginx:<version>
    ```
4. Go to DBI homebrew and select created resource
5. Choose game folder and install