#!/bin/bash
[ $1 ] || exit 1
sshpass -p astutepass ssh astute@192.222.1.${1} "
sudo chmod +777 /etc/exports
egrep 'opt|home|mnt|usr' /etc/exports ||
{ sudo echo '/opt  *(insecure,rw,no_root_squash,no_all_squash,sync)'  >> /etc/exports
  sudo echo '/home  *(insecure,rw,no_root_squash,no_all_squash,sync)' >> /etc/exports
  sudo echo '/mnt  *(insecure,rw,no_root_squash,no_all_squash,sync)' >> /etc/exports
  sudo echo '/usr  *(insecure,rw,no_root_squash,no_all_squash,sync)' >> /etc/exports
}
sudo chmod o+wx /opt 
sudo chmod o+wx /home 
sudo chmod o+wx /mnt 
sudo chmod o+wx /usr 
sudo service rpcbind start
sudo service nfs start
"
cd ~/nfs
[ ! -d host00${1} ] && mkdir host00${1}
cd host00${1}

export list=("opt" "home" "mnt" "usr")
for i in ${list[@]};do
    [ ! -d $i ] && mkdir $i
    mount -t nfs 192.222.1.${1}:/${i}/ $i/
done
