#!/bin/bash

while getopts "m:" opt
do
   case "$opt" in
      m ) parameterA="$OPTARG" ;;
   esac
done

TODAYVAl=$(date +"%d_%m")
git add .
git commit -m "Finished [$TODAYVAl]: $parameterA"
git push origin $(git rev-parse --abbrev-ref HEAD)
