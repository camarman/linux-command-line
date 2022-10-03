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

## Verifying `.iso` files

Obtain the SHA value of the `.iso` file via `sha512sum -b filename.iso` and save it into `produced.sha`. Later copy the online (available) sha512sum key and paste it into `original.sha`. Then run `check_shasum.py`.

Obtain the Key ID(fingerprint) of the `.iso` file via

    gpg --verify filename.iso > produced.asc
