# commands to execute on a fresh Raspberry Pi
# configure using raspi-config, reboot, install git, clone teleradio and execute this

# python
sudo apt -y install python3-dev python3-pip

# speech recognition
sudo apt -y install python3-pyaudio
sudo pip3 install wit speechrecognition

# speech synthesis
git clone https://github.com/MycroftAI/mimic.git
cd mimic
./autogen.sh
./configure --prefix='/usr/local'
make
make check
sudo make install

# gpio
sudo apt -y install python3-gpiozero
