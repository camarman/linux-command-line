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
