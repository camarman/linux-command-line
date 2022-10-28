# GNU/Linux Commands

Some useful commands that I have learned from TLCL (The Linux Command Line)

<https://linuxcommand.org/tlcl.php>

## Simple Commands

Note: Use `man` `info` or `help` commands to get an information about the command

`cal` : Shows the calender with todays date marked on

`date` : Shows the date with time

`df -H --sync` : Shows the status of the disk capacity (storage)

`free -ht --si` : Shows the status of the memory

## Navigation

`pwd` : Prints the name of the current working directory

`cd` : Changes directory.
>`cd ..` : Go to parent directory
>
>`cd -` : Go to previous directory
>
>`cd /` : Go to root directory
>
>`cd ~` : Go to home directory

`ls` : Lists the content of the directory.
>`ls -l` : Long format
>
>`ls -a` : Shows hidden files

`file` : Determines file type

`less` : Views the file content
>Options
>
>`b` : Scroll back one page
>
>`space` : Scroll forward one page
>
>`\` : Search for a character
>
>`g` : Move to beginning of a text file
>
>`G` : Move to the end of a text file

`command -options arguments`

## Manipulating Files and Directories

`cp` : Copy files and directories

`mv` : Move or rename files and directories

`mkdir` : Creates a directory

`rm` : removes files and directories

`ln` : Creates hard and symbolic links

You can also look at wildcards if necessary
