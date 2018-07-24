wit_key = None
with open('./config/wit_key', 'w+t') as wit_key_file:
    wit_key = wit_key_file.read()
    if len(wit_key) == 0:
        print('teleradio: enter wit.ai server access token: ', end = '')
        wit_key = input()
    wit_key_file.truncate(0)
    wit_key_file.write(wit_key)
