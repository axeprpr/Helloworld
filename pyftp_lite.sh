#!/bin/bash
ifconfig | grep 192 | egrep -o "\d+\.\d+\.\d+\.[^255]\d+"
echo "username=anonymous;password="
sudo python -m pyftpdlib -p 21

