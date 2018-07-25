import os

from teleradio import log
from teleradio.tts import say


def shutdown(text, entities):
    say('Shutting down')
    os.system('shutdown -h now')


def reboot(text, entities):
    say('Rebooting')
    os.system('reboot')
