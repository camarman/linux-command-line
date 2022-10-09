# Server

## Connection

>Cisco VPN adress: vpn.itu.edu.tr

Connect the server via

    ssh -X student@160.75.19.126

## File Transfer

In order to transfer files from Server to your computer run

    scp -r student@160.75.19.126:<SERVER_DIR> <MY_DIR>

in your terminal. In order to transfer files from your computer to Server use

    scp -r <MY_DIR> student@160.75.19.126:<SERVER_DIR>

>:bangbang: Use these commands *in your* terminal and *not* in the server terminal.

## Killing a process

To kill a running mpirun process, first run

    ps -ef | grep mpirun

The output should be something like this:

    student    32869   32194  0 18:32 pts/0    00:00:00 mpirun -np 8 python3 run_simplemc.py
    student    33913   32273  0 18:33 pts/1    00:00:00 grep mpirun

Then run

    ps -xw

and compare the PID's.

    PID TTY      STAT   TIME COMMAND
    31345 ?        Ss     0:00 /lib/systemd/systemd --user
    31346 ?        S      0:00 (sd-pam)
    32193 ?        S      0:01 sshd: student@pts/0
    32194 pts/0    Ss     0:00 -bash
    32272 ?        S      0:00 sshd: student@pts/1
    32273 pts/1    Ss     0:00 -bash
    32869 pts/0    S+     0:00 mpirun -np 8 python3 run_simplemc.py
    32870 ?        Ss     0:00 /usr/bin/hydra_pmi_proxy --control-port newton:33465 --rmk user --launcher ssh --demux poll --pgid 0 --ret
    32871 ?        Rsl    5:57 python3 run_simplemc.py
    32872 ?        Rsl    6:49 python3 run_simplemc.py
    32873 ?        Rsl    6:02 python3 run_simplemc.py
    32874 ?        Rsl    5:58 python3 run_simplemc.py
    32875 ?        Rsl    5:59 python3 run_simplemc.py
    32876 ?        Rsl    5:55 python3 run_simplemc.py
    32877 ?        Rsl    6:18 python3 run_simplemc.py
    32878 ?        Rsl    6:22 python3 run_simplemc.py
    33914 pts/1    R+     0:00 ps -xw

Note that in both cases **PID 32869** seems to be the main/base process. To kill this process, run

    kill -9 32869

>:bangbang: Make sure to save the **PID** number and the time of the process while running the `nohup`. This is required to kill the process in the future.
