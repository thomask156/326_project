#! /bin/bash

# A script that configures the dev environment from within vagrant.

cd /vagrant/
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install sqlite3
sudo pip3 install virtualenv
virtualenv --always-copy .venv
source .venv/bin/activate
cd /vagrant/src
pip3 install -r requirements.txt
curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install npm
sudo npm install -g gulp
sudo npm config set -g production false
npm install --no-bin-links
nodejs node_modules/node-sass/scripts/install.js
npm rebuild node-sass --no-bin-links
cp argue/settings_secret.py.template argue/settings_secret.py
gulp
sudo python manage.py collectstatic
gulp