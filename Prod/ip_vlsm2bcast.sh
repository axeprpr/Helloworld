#!/bin/bash
export str=$1

sep()
{
   str=$(printf  "%${1}s" "")
   echo "${str// /$2}"
}

ip=(`echo $str | awk -F '/' '{print $1}'|tr '.' ' '`)

for((i=0;i<${#ip[@]};i++));do
        ip[$i]=$(printf "%08d\n" `echo "obase=2;${ip[$i]}"|bc`)
done;

ipformat=`echo ${ip[*]}|sed 's/ //g'`
echo `sep 50 '-'`
echo "IP:"$ipformat

vlsm=(`echo $str | awk -F '/' '{print $2}'|tr '.' ' '`)

[ ${#vlsm[@]} -eq 4 ] && {
        for((i=0;i<${#ip[@]};i++));do
                vlsm[$i]=$(printf "%08d\n" `echo "obase=2;${vlsm[$i]}"|bc`)
        done;
        vlsmformat=`echo ${vlsm[*]}|sed 's/ //g'`
}

[ ${#vlsm[@]} -eq 1 ] && {
        vlsm=`echo $(($vlsm))`
#       echo $vlsm
        if [ $vlsm -gt 30 ];then
                vlsmformat=$(echo "obase=2;$vlsm" | bc)
        else
                vlsmformat=$(sep $vlsm "1")$(sep $((32-$vlsm)) "0")
        fi
}

echo "VLSM:"$vlsmformat

ba=()
for((i=0;i<32;++i))
do
        if [[ ${vlsmformat:$i:1} == "1" ]];then
                ba[$i]=${ipformat:$i:1};
        else
                ba[$i]="1"
        fi
done

baformat=`echo ${ba[*]}| sed 's/ //g'`
echo "BCAST:"$baformat
echo `sep 50 '-'`
bcast=`echo $((2#${baformat:0:8}))`"."`echo $((2#${baformat:8:8}))`"."`echo $((2#${baformat:16:8}))`"."`echo $((2#${baformat:24:8}))`
echo "BCAST(ASSCI):"$bcast
