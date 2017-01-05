#!/bin/bash
[ $1 ]|| exit 1
sshpass -p "astutepass" ssh astute@192.222.1.${1}





