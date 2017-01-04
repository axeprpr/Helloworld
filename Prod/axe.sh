#!/bin/bash
[ $1 ]|| exit 1
if [ $1 == "vps" ];then
    sshpass -p "XW2fif5#" ssh root@axeprpr.com
elif [ $1 == "troll" ];then
    sshpass -p "XW2fif5#" ssh axe@203.110.138.12
else
    sshpass -p "astutepass" ssh astute@192.222.1.${1}
fi





