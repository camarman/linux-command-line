# Fedora Installation Guide

Fedora Installation Guide, Including special tweaks and settings

## Pre-Installation

0) Make sure that fast start up and secure boot is disabled (For Nvidia Drivers. It might be different for AMD)
1) Install Fedora to USB (via Fedora Media Writer)
2) :exclamation: **Do not select delete after download in fedora media writer** :exclamation:

## Installation

### PART 1 (Booting)

1) Adjust the boot option from the UEFI menu

### PART 2 (Live USB - Adjusting Partitions)

1) Download gparted

    sudo dnf install gparted

2) Delete all *ext4* and the main partition
3) :bangbang: **DO NOT DELETE EFI** :bangbang:
4) Reboot (Optional)
5) Install Fedora to hard drive
6) Reboot

### PART 3 (System Updates)

1) Set up username-password
2) Reboot
3) Switch to Xorg
4) `sudo dnf upgrade`
5) Wait 10 minutes
6) Reboot
7) Switch to Xorg

### PART 4 (Enabling Nvidia)

1) Enable [RPM Repos](https://rpmfusion.org/Configuration)
2) Reboot
3) `sudo dnf upgrade --refresh`
4) Download [Nvidia](https://rpmfusion.org/Howto/NVIDIA)
5) Wait 10 minutes
6) Check if the drivers are installed

        modinfo -F version nvidia

7) Reboot
8) Enable Cuda Support
9) Wait 10 minutes
10) Final Reboot

## Post-Installation

### Installing Multimedia Support

See: <https://rpmfusion.org/Configuration>

### Installing VSCode

See: <https://code.visualstudio.com/docs/setup/linux>

#### Linking Github and VSCode

    git config --global user.name "seVenVo1d"
    git config --global user.email "arman-cam@windowslive.com"

### Installing Chrome

See: <https://docs.fedoraproject.org/en-US/quick-docs/installing-chromium-or-google-chrome-browsers/>

### Installing Fonts

Install the fonts via these commands

    cd /usr/share/fonts/
    sudo cp -r ~/Desktop/coding/fedora_installation_guide/Input .
    sudo cp -r ~/Desktop/coding/fedora_installation_guide/Hasklug .

### Installing Oh My Posh

See: <https://ohmyposh.dev/docs/installation/linux>

for installation if necessary

#### Downloading Oh My Posh

    sudo wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O /usr/local/bin/oh-my-posh
    sudo chmod +x /usr/local/bin/oh-my-posh

#### Downloading the Themes

    mkdir ~/.poshthemes
    wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/themes.zip -O ~/.poshthemes/themes.zip
    unzip ~/.poshthemes/themes.zip -d ~/.poshthemes
    chmod u+rw ~/.poshthemes/*.omp.*
    rm ~/.poshthemes/themes.zip

You can look at the themes via: <https://ohmyposh.dev/docs/themes>

and finally open `.bashrc` and type

    eval "$(oh-my-posh init bash --config ~/.poshthemes/jblab_2021.omp.json)"

### Installing pip and python packages

    python3 -m ensurepip --default-pip
    python3 -m pip install --upgrade pip setuptools wheel
    python3 -m pip install numpy
    python3 -m pip install scipy
    python3 -m pip install matplotlib
    python3 -m pip install pandas
    python3 -m pip install sklearn
    python3 -m pip install jupyterlab

### Installing Spotify

See: <https://snapcraft.io/spotify>

    sudo dnf install snapd

Reboot

    sudo snap install spotify

#### Setting Alias

    alias quarks='sudo dnf upgrade --refresh && sudo dnf distro-sync --refresh && sudo snap refresh && sudo dnf autoremove'
    alias gs="cd Desktop/coding/SimpleMC/"
    alias mp="module load mpi/openmpi-x86_64"

### Installing Latex Fonts

See: <https://docs.fedoraproject.org/en-US/neurofedora/latex/>

    sudo dnf install texlive-scheme-full

### Installing Gnome Tweaks

    sudo dnf install gnome-tweaks

### Installing Steam and Enabling Steam Proton for gaming

    sudo dnf install steam

In order to enable Steam Poroton enable `Steam -> Settings -> Steam Play` and toggle the option `Enable Steam Play for Supported Titles`.
