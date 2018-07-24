import subprocess


def say(text):
    # subprocess.call(('mimic', '-t', f"'{text}'"))
    print('teleradio: finished talking')


if __name__ == '__main__':
    say('this is text message')
    print('finished talking')
