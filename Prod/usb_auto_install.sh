#!/bin/bash

# variable level 1
export usb_boot=http://192.222.1.150:8082/fileserver/jenkins/usb_boot-master/latest/
export iso_iso=http://192.222.1.150:8082/fileserver/isos/CentOS-7-x86_64-Everything-1503-01.iso
export iso_md5=http://192.222.1.150:8082/fileserver/isos/CentOS-7-x86_64-Everything-1503-01.iso.md5
export atcloud_bin=http://192.222.1.150:8082/fileserver/jenkins/astute-cloud-master/latest/

# variable level 2
export usb_boot_file="$usb_boot"$(wget -q -O- $usb_boot | grep -P -o "usb_boot(.*?).tar.gz" | head -1)
export atcloud_bin_file="$atcloud_bin"$(wget -q -O- $atcloud_bin | grep -P -o "atcloud(.*?).bin" | head -1)
export atcloud_bin_file_md5="$atcloud_bin"$(wget -q -O- $atcloud_bin | grep -P -o "atcloud(.*?).bin.md5" | head -1)

function wgetAlog
{
    wget $1 && echo "download $1 successfully!" || exit 1
}

mkdir usb_boot
cd usb_boot

wgetAlog $usb_boot_file

tar -zxvf usb_boot*.tar.gz
cd data

#wgetAlog $iso_iso
wgetAlog $iso_md5
 
wgetAlog $atcloud_bin_file
wgetAlog $atcloud_bin_file_md5

cd .. && sudo ./create.sh
