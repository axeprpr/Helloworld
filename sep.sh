#!/bin/sh


sep()
{
   str=$(printf  "%${1}s" "")
   echo "${str// /$2}"
}
sep $1 $2
