import os
import nlp
from tts import say


def shutdown(text, entities):
    say('Shutting down')
    os.system('shutdown now')


def reboot(text, entities):
    say('Rebooting')
    os.system('reboot')
