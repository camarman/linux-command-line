# GNU/Linux Commands

Some useful commands that I have learned from TLCL (The Linux Command Line)

<https://linuxcommand.org/tlcl.php>

## Simple Commands

> Use `man`, `info` or `help` commands to get an information about the command

`cal` : shows the calender with todays date marked on

`date` : shows the date with time

`df -H --sync` : shows the status of the disk capacity (storage)

`free -ht --si` : shows the status of the memory

## Navigation

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

`ls` : lists the content of the directory.
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

## Manipulating Files and Directories

`cp` : copy files and directories

`mv` : move or rename files and directories

`mkdir` : create directory/directories

`rm` : removes files and directories

`ln` : creates hard and symbolic links

You can also look at wildcards if necessary

## I/O Redirection

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

## Pipeline

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

## echo

### Expansions

#### Pathname Expansion

To search in terms of wildcards in terminal use `echo`. For instance

    ls | echo *s

will print the folders or files that ends with "s", in the current directory.

#### Arithmetic Expansion

`echo` can be used to do mathematical calculations in the terminal. Such as:

    echo $((expression))

#### Brace Expansion

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

#### Parameter Expansion

`printenv | less` : lists the all environment variables

There is also quoting. Look Chapter 7 for more information.

## Searching History

`history | less` : shows the history in the terminal

There is also some good discussion about running a command from the history.

`!!` : run the previous command
`!#` : repeat history list item number.