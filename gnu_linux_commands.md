# GNU/Linux Commands

Some useful commands that I have learned from TLCL (The Linux Command Line)

<https://linuxcommand.org/tlcl.php>

## 1) What is Shell?

### Some simple commands

> Use `man`, `info` or `help` commands to get an information about the command

`cal` : shows the calender with todays date marked on

`date` : shows the date with time

`df -H --sync` : shows the status of the disk capacity (storage)

`free -ht --si` : shows the status of the memory

## 2) Navigation

`pwd` : prints the name of the current working directory

`file` : determines the type of the file

`cd` : changes directory.
>`cd ..` : go to parent directory
>
>`cd -` : go to previous directory
>
>`cd /` : go to root directory
>
>`cd ~` : go to home directory

## 3) Exploring the System

`ls` : lists the content ## Navigationof the directory.
>`ls -l` : long format
>
>`ls -a` : shows hidden files
>
>`ls -h` : human readable format
>
>`ls -S` : sort the results w.r.t size

`less` : views the file content
>`b` : scroll backward one page
>
>`space` : scroll forward one page
>
>`\` : search for a character
>
>`g` : move beginning of a text file
>
>`G` : move end of a text file

In the most general case the commands has

    command -options arguments
type of structure

## 4) Manipulating Files and Directories

`cp` : copy files and directories

`mv` : move or rename files and directories

`mkdir` : create directory/directories

`rm` : removes files and directories

`ln` : creates hard and symbolic links

You can also look at wildcards if necessary

## 6) Redirection

### Standard Input, Output, and Error

Shell file descriptors;

    stdin  -> standard input  -> 0
    stdout -> standard output -> 1
    stderr -> standard error  -> 2

To direct stdout, use `>`:

    ls -lh /usr/bin > ls-output.txt

However, if the command has an error, it will display the error in terminal and overwrite the file since we did not redirect the stderr. Thus, to **rewrite** or **create** a file run

    > ls-output.txt
which is much simpler then `touch ls-output.txt`

If you just want to append the results, use `>>`:

    ls -lh /usr/bin >> ls-output.txt

To direct only stderr, use `2>`:

    ls -lh /usr/bin 2> ls-output.txt

To direct both stdout and stderr, use `&>`:

    ls -lh /usr/bin &> ls-output.txt

To append both of stdout and stderr, use `&>>`:

    ls -lh /usr/bin &>> ls-output.txt

If you don't want to display the error or write it to a file, you can send to a *black hole* (/dev/null)

    ls -lh /usr/bin 2> /dev/null

### Pipeline

We can use pipeline `|` to direct from stdout to stdin. This is very useful in some cases, such as;

`command` : stdout in terminal

`command | less` : stdout in `less`

`command | filter` : filters the command and stdout in terminal

`command | filter | less` : filters the command and stdout in `less`

`command | filter &> file` : filters the command and writes the result

`command | tee file | filter` : writes the result, filters the command and stdout in terminal

`command | tee file | filter | less` : writes the result, filters the command and stdout in `less`

Some useful filters: `sort`, `uniq`, `wc`, `grep`, `head -n #` , `tail -n #`, `echo`

`tail`  can be also used to track the **live** change of a file. For example, run:

    tail -f /var/log/kern.log

close this use `CTRL+C`.

## 7) Seeing the World as the Shell Sees It

### Pathname Expansion

To search in terms of wildcards in terminal use `echo`. For instance

    ls | echo *s

will print the folders or files that ends with "s", in the current directory.

### Arithmetic Expansion

`echo` can be used to do mathematical calculations in the terminal. Such as:

    echo $((expression))

### Brace Expansion

    [me@linuxbox ~]$ echo Number_{1..5}
    Number_1 Number_2 Number_3 Number_4 Number_5

    [me@linuxbox ~]$ echo {01..15}
    01 02 03 04 05 06 07 08 09 10 11 12 13 14 15
    [me@linuxbox ~]$ echo {001..15}
    001 002 003 004 005 006 007 008 009 010 011 012 013 014 015

    [me@linuxbox ~]$ echo {Z..A}
    Z Y X W V U T S R Q P O N M L K J I H G F E D C B A

or most importantly it can be used to create folders and files such as:

    [me@linuxbox ~]$ mkdir Photos
    [me@linuxbox ~]$ cd Photos
    [me@linuxbox Photos]$ mkdir {2007..2009}-{01..12}
    [me@linuxbox Photos]$ ls
    2007-01 2007-07 2008-01 2008-07 2009-01 2009-07
    2007-02 2007-08 2008-02 2008-08 2009-02 2009-08
    2007-03 2007-09 2008-03 2008-09 2009-03 2009-09
    2007-04 2007-10 2008-04 2008-10 2009-04 2009-10
    2007-05 2007-11 2008-05 2008-11 2009-05 2009-11
    2007-06 2007-12 2008-06 2008-12 2009-06 2009-12

### Parameter Expansion

`printenv | less` : lists the all environment variables

There is also quoting. Look Chapter 7 for more information.

## 8) Advanced Keyboard Tricks

### Searching History

`history | less` : shows the history in the terminal

There is also some good discussion about running a command from the history.

`!!` : run the previous command

`!#` : repeat history list item number.

## 9) Permissions

### File attributes

    - | --- | --- | ---
    d | rw- | rw- | rw-

#### File type

File type is the first element in the file attributes

`-` : regular file
`d` : directory
`l` : symbolic link
`c` : character special file (such as /dev/null)
`b` : block special file (such as hard drive or DVD drive)

#### File mode

File mode is the other 9 elements which represents owners, groups and worlds read, write and execute permissions.

    Octal   Binary   File Mode
    0        000        ---
    1        001        --x
    2        010        -w-
    3        011        -wx
    4        100        r--
    5        101        r-x
    6        110        rw-
    7        111        rwx

By using the octal representation, we can change the file mode. Such as

    [me@linuxbox ~]$ > foo.txt
    [me@linuxbox ~]$ ls -l foo.txt
    -rw-rw-r-- 1 me me 0 2016-03-06 14:52 foo.txt
    [me@linuxbox ~]$ chmod 600 foo.txt
    [me@linuxbox ~]$ ls -l foo.txt
    -rw------- 1 me me 0 2016-03-06 14:52 foo.txt

where `600` implies `rw- | --- | ---`

Instead of using octal representation, we can use the symbolic representation. See table 9-5 for more detail but the most seen `u+x` represents add execute permission for the owner.

There is also some discussion about `umask`.

### Changing Your Password

In order to change the root password type:

    sudo passwd root

see also `adduser`, `useradd` and `groupadd`

## 10) Processes

### How a Process Works

Initially, the linux kernel starts a program called `init`. Later on `init` launches a series of shell scripts (called *init scripts*), which are located in `/etc`.

### Viewing Processes

`ps` : view processes

    [carman@fedora ~]$ ps x
        PID TTY      STAT   TIME COMMAND
    1797 ?        Ss     0:01 /usr/lib/systemd/systemd --user
    1808 ?        S      0:00 (sd-pam)
    1828 ?        Sl     0:00 /usr/bin/gnome-keyring-daemon --daemonize --login
    1834 tty2     Ssl+   0:00 /usr/libexec/gdm-wayland-session /usr/bin/gnome-session
    1837 ?        Ss     0:00 /usr/bin/dbus-broker-launch --scope user

`TTY/tty` : short for *teletype* and refers to the controlling terminal for the process.

`TIME` : amount of CPU time consumed by the process.

`STATE` : represents the state of the process

    State Meanings
    R -> *Running* :  This means that the process is running or ready to run.
    S -> *Sleeping* : The process is not running; rather, it is waiting for an event, such as a keystroke or network packet.
    D -> *Uninterruptible sleep* : The process is waiting for I/O such as a disk drive.
    T -> *Stopped* : The process has been instructed to stop.
    Z -> *A defunct or “zombie” process* : This is a child process that has terminated but has not been cleaned up by its parent.

`top`: shows the system information

### Controlling Processes
