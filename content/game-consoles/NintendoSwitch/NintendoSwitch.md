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


## Overlays

* EdiZon - using cheats. [GitHub](https://github.com/WerWolv/EdiZon)
* sys-clk - overclocking/underclocking system module. [GitHub](https://github.com/retronx-team/sys-clk)
* Uberhand-Overlay - fully craft-able overlay executor. [GitHub](https://github.com/efosamark/Uberhand-Overlay)

### Tesla Overlay System

Allows to access a menu of various homebrew applications and plugins.

* Tesla-Menu - overlay menu. [GitHub](https://github.com/WerWolv/Tesla-Menu)
* nx-ovlloader - sys-module, host process for loading overlay OVLs (NROs). [GitHub](https://github.com/WerWolv/nx-ovlloader)

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

## Firmware

* Caffeine/Nereba - name of excploit and software vulnerability.

### Official

* HOS - Horizon OS or Switch OS

### Bootloader

* Hekate - bootloader with GUI and many features. [GitHub](https://github.com/CTCaer/hekate)
* hekate_boot_dat -create a SX boot.dat from hekate[GitHub](https://github.com/mondul/hekate_boot_dat)

### Custom

* **Evaron-AIO** - my own all-in-one build based on existing CFWS. [GitHub](https://github.com/pgalonza/Evaron-AIO)
* [Atmosphère](#atmosphere) - customized firmware for the Nintendo Switch. [GitHub](https://github.com/Atmosphere-NX/Atmosphere)
* DeepSea - the new All-in-One CFW package. [GitHub](https://github.com/Team-Neptune/DeepSea)
* GNX - Brazilian All-in-One CFW package. [GitHub](https://github.com/vncsmnl/GNX)
* Santa-Claus - [Site](https://santa-atmo.ru/nintendo-switch/)
* SX OS - Features like the XCI Loader require an SX OS license.
* Ultra - [GitHub](https://github.com/Ultra-NX/Ultra)
* Switch OC Suite - Overclocking suite running Atmosphere CFW. [GitHub](https://github.com/hanai3Bi/Switch-OC-Suite)
* Kefir - [Bitbucket](https://bitbucket.org/kefir-switch/kefir/src/master/)
* 4IFIR - ultimate CFW for overlocking. [GitHub](https://github.com/rashevskyv/4IFIR?tab=readme-ov-file#)
* 5IFIR - like 4IFIR for semi-stock[GitHub](https://github.com/k1gs/5ifir)
* Hats - pack containing the latest version of Hekate, Atmosphere and its Signature Patches. [Telegram](https://t.me/HATSPACK)
* NeXT - another AIO Pack. [Codeberg](https://codeberg.org/vampitech/NeXT)
* ShallowSea - AIO CFW package for the. [Codeberg](https://codeberg.org/carcaschoi/Shallowsea)
* NX-Venom - the ultimate bundle for overclocking. [GitHub](https://github.com/CatcherITGF/NX-Venom)
* Atmosphere-with-Hekate - Hekate and Atmosphere only. [GitHub](https://github.com/yyoossk/Atmosphere-with-Hekate)
* Arquivos-JNX - additional file. [GitHub](https://github.com/JuniorPassos/Arquivos-JNX)
* Kefirosphere - fork of Atmosphère. [GitHub](https://github.com/rashevskyv/Kefirosphere)
---
* Kefir Updater - update your CFW, sigpatches, cheat codes, firmwares and more. [GitHub](https://github.com/rashevskyv/kefir-updater)
* AIO-Switch-Updater - update your CFW, cheat codes, firmwares and more. [GitHub](https://github.com/HamletDuFromage/aio-switch-updater)
* AtmoPackUpdater - homebrew which update your CFW/Firmware/Homebrews/Sigpatches. [GitHub](https://github.com/PoloNX/AtmoPackUpdater)
* emuMMC - SDMMC driver replacement for Nintendo's Filesystem Services. [GitHub](https://github.com/m4xw/emuMMC)
* [sigmapatches](https://sigmapatches.su/)

### Atmosphere

* [GitHub](https://github.com/Atmosphere-NX/Atmosphere)

#### Build

* [Instruction](https://github.com/Atmosphere-NX/Atmosphere/blob/master/docs/building.md)
* [devkitPro](#devkitpro) - provider of homebrew toolchains for Nintendo
* **devkita64-atmosphere** - my own devkita64-container with everything you need for build atmosphere locally and with CI. [GitHub Packages](https://github.com/pgalonza/Evaron-Atmosphere/pkgs/container/devkita64-atmosphere)

### SigPatch

Signature patches, es/fs/ips/acid/loader-pathes. Digital signatures that allow unsigned code to run on the horizon operating system. Use sys-patch if problem with it.

Atmosphere > 1.7.0
* Hekate use _patches.ini_ file
* Modified fuse use _atmosphere/kip_patches/_

---
* [sigmapatches](https://sigmapatches.su/)
* [Sigpatches for Atmosphere](https://gbatemp.net/threads/sigpatches-for-atmosphere-hekate-fss0-fusee-package3.571543/)
* sigpatch-updater - [Bitbucket](https://bitbucket.org/e1ite007/sigpatch-updater/src/master/)
* sys-patch - system module for patches(SigPatche) fs, es, ldr and nifm on boot.[Gbatemp](https://gbatemp.net/threads/sys-patch-sysmod-that-patches-on-boot.633517/), [GitFlic](https://gitflic.ru/project/impeeza/sys-patch)
* IPS - International Patching System [Patchlib](https://patchlib.readthedocs.io/en/latest/filetype_docs/ips.html), [Zerosoft](https://zerosoft.zophar.net/ips.php)
* [IPS python](https://github.com/friedkeenan/ips.py)
* [patchlib](https://github.com/brette-0/patchlib)
* [Lips](https://github.com/kylon/Lipx)
* AutoIPS-patcher - [Gbatemp](https://gbatemp.net/attachments/autoips-patcher-zip.303087/)
* [SigPatches](https://github.com/btc08gh/SigPatches)


### Logo and spash screen

* [Insert spash screen](https://raw.githubusercontent.com/Atmosphere-NX/Atmosphere/master/utilities/insert_splash_screen.py)
* [Convertfb](https://github.com/zqb-all/convertfb)
* [Switch logo patcher](https://github.com/friedkeenan/switch-logo-patcher)

## devkitPro

* devkitPro pacman - devkitPro provided tools and libraries are managed by the rather wonderful Arch Linux pacman. [devkitpro](https://devkitpro.org/wiki/devkitPro_pacman)
* devkitPro container images - [Dockerfiles](https://github.com/devkitPro/docker/tree/master), [DockerHub](https://hub.docker.com/u/devkitpro)
* Problem with CI - you need to use a container to avoid http error 403. [Issues](https://github.com/devkitPro/pacman/issues/31)

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
* Not needed boot.dat and boot.ini it`s for SX Gear
* .uf2 - flashing when loading into the controller memory
* .bin - flashing using picofly toolbox
---
* [GitHub Source](https://github.com/rehius/usk)
* [GitHub Source](https://github.com/Ansem-SoD/Picofly)
* Glitching the CPU to make it fail a check, which allows booting from an unsigned payload that will then run higher level software.
* UF2 - USB flashing format developed by Microsoft. [GitHub](https://github.com/microsoft/uf2)

## DNS

* 90dns - NX DNS setup. [GitLab](https://gitlab.com/a/90dns)

## Mikrotik

```bash
add address=127.0.0.1 regexp=".*\\.nintendo\\..*"
add address=127.0.0.1 regexp="^nintendo\\..*"
```

## EMUMMC

[emummc.txt](https://nh-server.github.io/switch-guide/files/emummc.txt)

```txt
127.0.0.1 *nintendo*
127.0.0.1 receive-%.dg.srv.nintendo.net receive-%.er.srv.nintendo.net
127.0.0.1 *nintendo-europe.com
127.0.0.1 *nintendoswitch.*
```

## Backup&Restore

### DD backuo

eMMC/emuMMC with DD

1. Enter to Hekate
2. Go to Tools > USB-tools
3. In USB MASS STORAGE press eMMC RAW GPP
4. Run parted -l or fdisk -l and look disk device
5. Execute dd command
    ```bash
    dd if=/dev/sd<a-z> of=/<file name>.img bs=5M status=progress
    ```
6. Do that for boot0 and boot1

### DD restore

eMMC/emuMMC with DD

1. Enter to Hekate
2. Go to Tools > USB-tools
3. Disable Read-Only mode
4. In USB MASS STORAGE press eMMC RAW GPP
5. Run parted -l or fdisk -l and look disk device
6. Execute dd command
    ```bash
    dd if=/<file name>.img of=/dev/sd<a-z> bs=5M status=progress
    ```

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

## SD-Card

### Partition for emuMMC

```bash
parted /dev/sd<>
unit MB
mkpart primary fat32 1M <end - 32768-1>M
mkpart primary fat32 <end - 32768>M <end>M

mkfs.fat /dev/sd<>1
```

## Reverse engineering

* Switch-Ghidra-Guides - [GitHub](https://github.com/borntohonk/Switch-Ghidra-Guides/)