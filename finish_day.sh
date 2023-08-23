#!/bin/bash


TODAYVAl=$(date +"%d_%m")
git add .
git commit -m "Finished [$TODAYVAl]: $1"
git push origin $(git rev-parse --abbrev-ref HEAD)
