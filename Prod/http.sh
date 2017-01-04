#!/bin/bash
ifconfig | grep 192 | egrep -o "\d+\.\d+\.\d+\.[^255]\d+"
sudo python -m SimpleHTTPServer 80
