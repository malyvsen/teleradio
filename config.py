import os


wit_key = None

config_dir = 'config/'
wit_key_path = config_dir + 'wit_key'


try:
    os.makedirs(config_dir)
except OSError:
    pass


try:
    with open(wit_key_path, 'r') as wit_key_file:
        wit_key = wit_key_file.read()
except FileNotFoundError:
    pass

if not wit_key:
    print('teleradio: enter wit.ai server access token: ', end = '')
    wit_key = input()
    with open(wit_key_path, 'w') as wit_key_file:
        wit_key_file.write(wit_key)
