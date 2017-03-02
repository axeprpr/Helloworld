# config smb
#SMB_DIR="/var/lib/nova/datadisk/sdb/smbshare"
#SMB_DIR=$DATADISK_DIR/smbshare
SMB_CFG_FILE_SECTION="smb"
SMB_CFG_FILE="/etc/samba/smb.conf"

# 1 config smb
function config_smb()
{
    sudo mkdir $SMB_DIR
    sudo chmod o+w $SMB_DIR

    if [ -z "`cat $SMB_CFG_FILE |grep $SMB_DIR`" ]; then
        if [ -z "`cat $SMB_CFG_FILE |grep 'map to guest = bad user'`" ]; then
            sed -i '/^\[global\]$/a map to guest = bad user' $SMB_CFG_FILE
        fi

        sudo cat >> $SMB_CFG_FILE <<-EOF
[$SMB_CFG_FILE_SECTION]
        comment = Home Directories
        path = $SMB_DIR
        browseable = yes
        writable = yes
        guest ok = yes
        read only = no
;       valid users = %S
;       valid users = MYDOMAIN\%S
EOF

    fi
}

# main
if [ -z $SMB_DIR ]; then
    echo "smb dir: $SMB_DIR does not exist."
    exit -1
fi

sudo yum -y install samba samba-client
sudo systemctl enable smb
config_smb
sudo systemctl restart smb
