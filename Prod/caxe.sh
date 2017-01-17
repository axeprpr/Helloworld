#!/bin/bash
[ $1 ]|| exit 1
sed -n /192\.222\.1\.${1}/d /Users/axe/.ssh/known_hosts
