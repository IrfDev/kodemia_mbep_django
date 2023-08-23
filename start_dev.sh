#!/bin/bash

echo "Starting your new day!!!"
TODAYVAl=$(date +"%d_%m")
BACKUPDIR=$(ls -td ./*/ | head -1)
echo $BACKUPDIR
echo "Your base app will be $BACKUPDIR"
mkdir $TODAYVAl
echo "Creating $TODAYVAl directory"
python3 -m venv $TODAYVAl/.venv
source $TODAYVAl/.venv/bin/activate
cp -R $BACKUPDIR/first_app $TODAYVAl/first_app 
cp $BACKUPDIR/requirements.txt $TODAYVAl/requirements.txt
echo "Installing pip requirements"
pip install -r ./$TODAYVAl/requirements.txt
touch $TODAYVAl/content.md
rm -rf $BACKUPDIR/.venv
echo "Cleaning up yesterdays virtual environment"