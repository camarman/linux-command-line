# Extra

## Secure Boot dbx Configuration Update

If you see this in gnome-software `Secure Boot dbx Configuration Update`, you need to install it via

    sudo fwupdmgr refresh ; sudo fwupdmgr get-updates
    sudo fwupdmgr update

After the update, check the lines via `dbxtool -l`.

If you encounter `tpm.c:148: Unknown TPM error` while trying to start the Fedora, you can try to disable the Secure Boot (*if it has enabled*). Also, ASUS seems to have problems with the `fwupdmgr.`

Check these links for more information.

<https://ask.fedoraproject.org/t/secure-boot-dbx-update/26626/13>
<https://ask.fedoraproject.org/t/grub-core-error-you-need-to-load-the-kernel-first/14405/2>
<https://bugs.launchpad.net/ubuntu/+source/grub2/+bug/1848892>

## Removing Windows from GRUB menu

1) Delete `/boot/efi/EFI/Microsoft` directory on your running system
2) Update grub with `grub2-mkconfig -o /boot/grub2/grub.cfg`

## Verifying `.iso` (or any other) file

See: <https://ubuntu.com/tutorials/how-to-verify-ubuntu#1-overview>

Along with the `.iso` file download the checksum `SHA256SUMS` and GnuPG signature `SHA256SUMS.gpg`. After that run

    gpg --verify SHA256SUMS.gpg SHA256SUMS
to verify the signature. If it says *Can't check signature: No public key* then run

    gpg --keyserver <SITE> --recv-keys <KEY>
where `<KEY>` must be obtained from the previous command. Inspect the key fingerprints by running

    gpg --list-keys --with-fingerprint <KEY>
Finally, verify the signature again and check the checksum

    sha256sum -c SHA256SUMS 2>&1 | grep OK

## Installing Virtual Box

See: <https://www.virtualbox.org/wiki/Linux_Downloads>

1) Make sure that some of the packages are installed

        sudo dnf install kernel-devel kernel-headers gcc gcc-c++ make git

2) Download **SHA256 checksums** and **MD5 checksums** files (via *save page as*) and test the checksums by running

        sha256sum -c SHA256SUMS 2>&1 | grep OK
        md5sum -c MD5SUMS 2>&1 | grep OK

    make sure that both of them returns `OK`.
3) Add repository information to `/etc/yum.repos.d/` via the name `virtualbox.repo`

        [virtualbox]
        name=Fedora $releasever - $basearch - VirtualBox
        baseurl=http://download.virtualbox.org/virtualbox/rpm/fedora/$releasever/$basearch
        enabled=1
        gpgcheck=1
        repo_gpgcheck=1
        gpgkey=https://www.virtualbox.org/download/oracle_vbox.asc

4) Upgrade the system in order to import the keys
        sudo dnf upgrade
5) Reboot
6) Install *Oracle Virtual Box*

        sudo dnf install VirtualBox
7) Reboot

## Installing KVM (Kernel based Virtual Machine)

See_1: <https://fedoramagazine.org/full-virtualization-system-on-fedora-workstation-30/>

See_2: <https://help.ubuntu.com/community/KVM/Installation>

To see if your processor supports Intel VT-x, you can review the output from this command:

    egrep -c '(vmx|svm)' /proc/cpuinfo

If 0 it means that your CPU doesn't support hardware virtualization.

If 1 or more it does - but you still need to make sure that virtualization is enabled in the BIOS. Later on install virtualization via

    sudo dnf install @virtualization

Finally, start and enable the `libvirtd` service

    sudo systemctl start libvirtd
    sudo systemctl enable libvirtd
