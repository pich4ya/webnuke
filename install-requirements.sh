#!/bin/bash
apt-get install python python-pip git -y
pip install pyvirtualdisplay
pip install selenium
pip install requests
wget https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz
sh -c 'tar -x geckodriver -zf geckodriver-v0.20.1-linux64.tar.gz -O > /usr/bin/geckodriver'
chmod +x /usr/bin/geckodriver
rm geckodriver-v0.20.1-linux64.tar.gz
pip install --upgrade selenium
