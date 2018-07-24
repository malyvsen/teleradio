#!/bin/bash
sudo apt -y install git python3-dev python3-pip
sudo apt -y install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
pip3 install --user pyaudio wit speechrecognition
git clone https://github.com/malyvsen/teleradio.git
