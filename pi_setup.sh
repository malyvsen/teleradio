# commands to execute on a fresh Raspberry Pi (rigth after running raspi-config and rebooting)

# basic functionality
sudo apt -y install git python3-dev python3-pip

# clone teleradio
git clone https://github.com/malyvsen/teleradio.git

# speech recognition
sudo apt -y install python3-pyaudio
pip3 install --user wit speechrecognition

# speech synthesis
git clone https://github.com/MycroftAI/mimic.git
cd mimic
./autogen.sh
./configure --prefix='/usr/local'
make
make check
sudo make install
