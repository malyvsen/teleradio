import os


wit_key = None
wit_key_path = 'wit_key'

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
