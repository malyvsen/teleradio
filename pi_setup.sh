# commands to execute on a fresh Raspberry Pi (right after running raspi-config and rebooting)

# basic functionality
sudo apt -y install git python3-dev python3-pip

# clone teleradio
git clone https://github.com/malyvsen/teleradio.git

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

# launch teleradio on startup
sudo sed -i '$ d' /etc/rc.local
echo '(sleep 10;python /home/pi/teleradio/teleradio.py)&' | sudo tee --append /etc/rc.local
echo '' | sudo tee --append /etc/rc.local
echo 'exit 0' | sudo tee --append /etc/rc.local
