# Fedora Installation Guide

Fedora Installation Guide, Including special tweaks and settings

## Installing Fedora

### PART 1 (Pre - Installation)

1) Install Fedora to USB (via Fedora Media Writer)
2) :exclamation: **Do not select delete after download in fedora media writer** :exclamation:

### PART 2 (Booting)

1) Adjust the boot option from the UEFI menu

### PART 3 (Live USB - Installation)

1) Download gparted

    sudo dnf install gparted

2) Delete all *ext4* and the main partition
3) **:bangbang: DO NOT DELETE EFI :bangbang:**
4) Install Fedora to hard drive
5) Reboot

### PART 4

1) `sudo dnf upgrade`
2) Wait 10 minutes
3) Reboot
4) Switch to Xorg

### PART 5 (Enabling Nvidia)

1) Enable [RPM Repos](https://rpmfusion.org/Configuration)
2) Enable Multimedia post-install
3) Download [Nvidia](https://rpmfusion.org/Howto/NVIDIA)
4) Wait 10 minutes
5) Reboot
6) Enable Cuda

## Installing Fonts

Download the fonts folder and move them via these commands
    cd /usr/share/fonts/
    sudo cp -r ~/Desktop/coding/fedora_installation_guide/Input .
    sudo cp -r ~/Desktop/coding/fedora_installation_guide/Hasklig .
