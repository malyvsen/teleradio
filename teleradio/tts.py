import subprocess

from teleradio import log


def say(text):
    log.detail('saying: ' + text)
    subprocess.call(('mimic', '-t', '\'' + text + '\''))


if __name__ == '__main__':
    say('this is a text message')
    log.update('finished talking')
