# Fedora Installation Guide

Fedora installation guide, including special tweaks and settings

## Pre-Installation

### UEFI Firmware Settings

> :exclamation: Learn the key-binding that opens the UEFI Firmware Settings

Aras's Computer: F2
My Computer: F2

Adjust these settings accordingly;

    Boot Mode     [UEFI]
    Fast Boot     [Disabled]
    Secure Boot   [Disabled]
    USB Boot      [Enabled]

> IMPORTANT: Disabling the secure boot is optional. However, it's kind of complicated to maintain Linux distributions where secure boot is enabled. You might encounter with many error during updates/upgrades etc. The safest way is to disable the Secure Boot.

### Fedora Media Writer (FMW)

1) Select the **Image Source** as *Download automatically*
2) Select the **Fedora Release** and adjust the **Write Options**

    :exclamation: Do not select *Delete download after writing* in Write Options

## Installation

### Booting

1) Adjust the **Boot Option Priorities** (order of the EFI) from the UEFI Firmware Settings
2) In the **GNU GRUB** menu select *Test this media & start Fedora ...*

### Live USB - Adjusting Partitions

1) Install gparted

        sudo dnf install gparted

2) Delete **ext4** and **btrfs** (fedora_localhost-live/main partition)
3) :bangbang: **DO NOT DELETE EFI System Partition** :bangbang:
4) Reboot
5) Install Fedora to hard drive

    exclamation: Select *Automatic* in **Installation Destination/Storage Configuration** (i.e., Automatic partitioning)

6) Power Off
7) Remove USB

### System Updates

1) Set username & password
2) Update your system

        sudo dnf upgrade
3) Wait 10 minutes
4) Reboot
5) Switch to **Xorg**

### Enabling Nvidia

1) Enable [RPM Repos](https://rpmfusion.org/Configuration)
2) Update your system

        sudo dnf upgrade --refresh
3) Reboot
4) Download [Nvidia and Cuda Support](https://rpmfusion.org/Howto/NVIDIA)
5) Wait 10 minutes
6) Check if the drivers are installed

        modinfo -F version nvidia
7) Final Reboot

## Post-Installation

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

Clone `fedora_installation_guide` repository to `~/Desktop/coding`

### Installing Fonts

Install fonts via these commands

    cd /usr/share/fonts/
    sudo cp -r ~/Desktop/coding/fedora_installation_guide/Input .
    sudo cp -r ~/Desktop/coding/fedora_installation_guide/Hasklug .

### Installing Oh My Posh

See: <https://ohmyposh.dev/docs/installation/linux>

After following the steps open `.bashrc` and paste

    eval "$(oh-my-posh init bash --config ~/.poshthemes/thecyberden.omp.json)"

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

if you want to update the packages in the `python_packages.txt` type

    python3 -m pip install -r python_packages.txt --upgrade

> Do not update every python package. Updating everything might cause system failure/crashes due to package version conflict's with the Fedora OS.

### Setting Alias

    alias quarks="sudo dnf clean all && sudo dnf updateinfo && sudo dnf upgrade --refresh && sudo dnf distro-sync --refresh && sudo snap refresh && sudo dnf autoremove"
    alias cod="cd ~/Desktop/coding"
    alias gs="cd ~/Desktop/coding/SimpleMC/"
    alias mp="module load mpi/openmpi-x86_64"

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

## Encountered Errors

If you see this in gnome-software `Secure Boot dbx Configuration Update`, you need to install it via

    sudo fwupdmgr refresh ; sudo fwupdmgr get-updates
    sudo fwupdmgr update

After the update, check the lines via `dbxtool -l`.

If you encounter `tpm.c:148: Unknown TPM error` while trying to start the Fedora, you can try to disable the Secure Boot (*if it's enabled*). Also ASUS seems to have problems with the `fwupdmgr`.

Check these links for more information

<https://ask.fedoraproject.org/t/secure-boot-dbx-update/26626/13>
<https://ask.fedoraproject.org/t/grub-core-error-you-need-to-load-the-kernel-first/14405/2>
<https://bugs.launchpad.net/ubuntu/+source/grub2/+bug/1848892>
