# Fedora Installation Guide

Fedora installation guide, including unique tweaks and settings

## Pre-Installation

### UEFI Firmware Settings

> :exclamation: Learn the key-binding that opens the UEFI Firmware Settings

Aras' Computer & My Computer: F2

Adjust these settings accordingly;

    Boot Mode     [UEFI]
    Fast Boot     [Disabled]
    Secure Boot   [Disabled]
    USB Boot      [Enabled]

> IMPORTANT: Disabling the Secure Boot is optional. However, it is kind of complicated to maintain Linux distributions where the Secure Boot is enabled. You might encounter many errors during the update/upgrade procedures. The safest way to use any Linux distribution (which includes Fedora) is to disable the Secure Boot.

### Fedora Media Writer (FMW)

1) Select the **Image Source** as *Download automatically*
2) Select the **Fedora Release** and adjust the **Write Options**
3) Power OFF

    :exclamation: Do not select *Delete download after writing* in Write Options

## Installation

### Booting

0) Power ON
1) Adjust the **Boot Option Priorities** (order of the EFI) from the UEFI Firmware Settings
2) In the **GNU GRUB** menu, select *Test this media & start Fedora ...*

### Installing Fedora

0) Connect to Network
1) Install `gparted` via

        sudo dnf install gparted

2) Adjust partitions

    Delete **ext4** and **btrfs** (fedora_localhost-live/main partition)

    :bangbang: **DO NOT DELETE EFI** :bangbang:

3) Reboot
4) Install Fedora to Hard Drive

    :exclamation: Select *Automatic* in **Installation Destination/Storage Configuration** (i.e., Automatic partitioning)

5) Power OFF
6) Remove USB

### System Updates

1) Follow the Anaconda Installer
2) Update your system

        sudo dnf upgrade
3) Wait 15 minutes
4) Reboot

## Post-Installation

### Enabling Nvidia

1) Install [Free and Nonfree RPM Repositories](https://rpmfusion.org/Configuration)

        sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

2) Update your system

        sudo dnf upgrade --refresh
3) Reboot
4) Install [Nvidia](https://rpmfusion.org/Howto/NVIDIA)

        sudo dnf install akmod-nvidia

5) :bangbang: Wait 10 minutes and check the driver status via

        modinfo -F version nvidia

6) Reboot
7) Install Cuda Support

        sudo dnf install xorg-x11-drv-nvidia-cuda

8) Wait 10 minutes
9) Reboot

### Installing Multimedia Support

See: <https://rpmfusion.org/Configuration>

    sudo dnf groupupdate multimedia --setop="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin
    sudo dnf groupupdate sound-and-video

### Installing Chrome

See: <https://docs.fedoraproject.org/en-US/quick-docs/installing-chromium-or-google-chrome-browsers/>

### Installing VSCode

See: <https://code.visualstudio.com/docs/setup/linux>

#### Linking Github and VSCode

    git config --global user.name "seVenVo1d"
    git config --global user.email "arman-cam@windowslive.com"

### Middle Step

Clone `linux_black_hole` repository to `~/Desktop/coding`

### Installing Fonts

Install fonts via these commands

    cd /usr/share/fonts/
    sudo cp -r ~/Desktop/coding/linux_black_hole/fedora_installation_guide/Input .
    sudo cp -r ~/Desktop/coding/linux_black_hole/fedora_installation_guide/Hasklug .

### Installing Cool Retro Term

See: <https://github.com/Swordfish90/cool-retro-term>

You can easily install the Cool Retro Term. Just type

    sudo dnf install cool-retro-term

### Managing Python Packages

#### Installing pip

See: <https://packaging.python.org/en/latest/tutorials/installing-packages/>

    python3 -m ensurepip --default-pip
    python3 -m pip install --upgrade pip setuptools wheel

#### Installing python packages

    python3 -m pip install -r python_packages.txt

#### Updating python packages

See: <https://pip.pypa.io/en/stable/cli/pip_install/?highlight=update#examples>

    python3 -m pip install --upgrade SomePackage

If you want to update the packages in the `python_packages.txt` type

    python3 -m pip install -r fedora_installation_guide/python_packages.txt --upgrade

> Do not update every python package. Updating everything might cause system failure/crashes since they might conflict with the Fedora OS's python package version.

#### Creating Virtual Environments

See: <https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments>

In order create a virtual environment, type

    python3 -m venv <DIR>

where `<DIR>` is the name of the virtual environment directory. In order to activate the virtual environment type

    source <DIR>/bin/activate

### Setting Alias

    alias quarks="sudo dnf clean all ; sudo dnf upgrade ; sudo dnf distro-sync ; sudo snap refresh ; sudo dnf autoremove"
    alias cod="cd ~/Desktop/coding"
    alias gs="cd ~/Desktop/coding/SimpleMC/"
    alias mp="module load mpi/openmpi-x86_64"
    alias logserver="ssh -X student@160.75.19.126"
    alias vpninfo='less ~/Desktop/server_info'
    alias cvenv='python3 -m venv venv/'
    alias avenv='source venv/bin/activate'
    alias scopy='scp -r student@160.75.19.126:~/Arman/SimpleMC/simplemc/chains ~/Desktop/coding/model_analysis'

### Installing Gnome Tweaks

    sudo dnf install gnome-tweaks

### Installing Spotify

See: <https://snapcraft.io/spotify>

    sudo dnf install snapd

Reboot

    sudo snap install spotify

### Installing Steam and Enabling Steam Proton for gaming

See: <https://docs.fedoraproject.org/en-US/gaming/proton/>

    sudo dnf install steam

In order to enable Steam Proton follow these steps

    Steam -> Settings -> Steam Play and toggle the option `Enable Steam Play for Supported Titles.

### Installing Latex Fonts

See: <https://docs.fedoraproject.org/en-US/neurofedora/latex/>

    sudo dnf install texlive-scheme-full
