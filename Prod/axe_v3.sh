#!/bin/sh
[ $1 ] || exit
if [ $1 -eq 1 ];then
  ip=192.221.1.1
elif [ `echo $1|awk '{print length($0)}'` -le 3 ];then
  ip=192.222.1.$1
else
  ip=$1
fi
/Users/axe/WorkGit/pro/Helloworld/Prod/axe_v2.sh 22 root "$ip" 'donotuseroot!'
