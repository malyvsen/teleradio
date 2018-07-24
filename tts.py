import subprocess


def say(text):
    subprocess.call(('mimic', '-t', f"'{text}'"))


if __name__ == '__main__':
    say('this is text message')
    print('finished talking')
