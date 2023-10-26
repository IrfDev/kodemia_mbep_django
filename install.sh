#!/bin/bash

TODAYVAl=$1
echo "Installing $2 package in todays directory $($TODAYVAl)"
source $TODAYVAl/.venv/bin/activate
cd $TODAYVAl
pip install $2
pip freeze > requirements.txt