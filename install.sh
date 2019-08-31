#!/bin/bash


# install TIL
pushd TerminalImageViewer/src/main/cpp/
make
sudo make install
popd


# install update-motd
sudo apt install update-motd -y

# generate image
./gen_image.py
sudo mv 01-motd /etc/update-motd.d
sudo chmod +x /etc/update-motd.d/01-motd

pushd /etc/update-motd.d
sudo mkdir not-used
mv 10-help-text not-used
mv 50-motd-news not used
popd
