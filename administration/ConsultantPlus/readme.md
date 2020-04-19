# Install ConsultantPlus on linux
1. The script _wine_install.sh_ install Wine, PlayOnLinux and other packages.
2. The script _fstab.sh_ make directory _/etc/cons_ with privileges. After this write in _/etc/fstab_ the parameters for mount, then create the link.

!Important!
For the full functionality of the script you must do:
1. When you create a virtual disk in PlayOnLinux, name it consultant
2. When you add a disc in the wine settings, the disc should be named d:
