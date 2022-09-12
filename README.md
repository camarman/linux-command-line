# Fedora Installation Guide

Fedora Installation Guide, Including special tweaks and settings

## Pre-Installation

0) Make sure that fast start up and secure boot is disabled (For Nvidia Drivers. It might be different for AMD)
1) Install Fedora to USB (via Fedora Media Writer)
2) :exclamation: **Do not select "Delete After Download" in Fedora Media Writer** :exclamation:

## Installation

### PART 1 (Booting)

1) Adjust the boot option from the UEFI menu

### PART 2 (Live USB - Adjusting Partitions)

1) Download gparted

        sudo dnf install gparted

2) Delete **ext4** and the main partition
3) :bangbang: **DO NOT DELETE EFI** :bangbang:
4) Reboot (Optional)
5) Install Fedora to hard drive
6) Reboot

### PART 3 (System Updates)

1) Set up username & password
2) Reboot
3) Switch to **Xorg**
4) Update your system

        sudo dnf upgrade
5) Wait 10 minutes
6) Reboot
7) Switch to **Xorg**

### PART 4 (Enabling Nvidia)

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

    alias quarks='sudo dnf clean all && sudo dnf updateinfo && sudo dnf upgrade --refresh && sudo dnf distro-sync --refresh && sudo snap refresh && sudo dnf autoremove'
    alias cod='cd Desktop/coding'
    alias gs="cd Desktop/coding/SimpleMC/"
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

    `Steam -> Settings -> Steam Play` and toggle the option `Enable Steam Play for Supported Titles`.

### Installing Latex Fonts

See: <https://docs.fedoraproject.org/en-US/neurofedora/latex/>

    sudo dnf install texlive-scheme-full
