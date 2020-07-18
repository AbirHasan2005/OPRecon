#!/bin/bash
# Update Script for OPRecon v2.1-Stable
# Script created by @AbirHasan2005


dependencies() {

command -v git > /dev/null 2>&1 || { echo >&2 "Package GIT is not installed ... Unable to update ..."; exit 1; }

}

script() {

clear
printf "\n \e[1;92mUpdating \e[1;94mOPRecon\e[1;92m ...\n\n"
sleep 1.5
cd ..
rm -rf OPRecon
git clone https://github.com/AbirHasan2005/OPRecon
cd OPRecon
chmod +x run.sh
printf "\n\e[1;92mRestarting ...\n\e[0m"
bash run.sh
cd ..

}

dependencies
script

