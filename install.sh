#!/bin/bash

TODAYVAl=$(date +"%d_%m")
echo "Installing $1 package in todays directory $($TODAYVAl)"
source $TODAYVAl/.venv/bin/activate
cd $TODAYVAl
pip install $1
pip freeze > requirements.txt