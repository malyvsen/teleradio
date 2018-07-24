import speech_recognition as sr
import nlp

from light import light_set
from music import music_play, music_stop


intent_handlers = {
'light_set': light_set,
'music_play': music_play,
'music_stop': music_stop}


r = sr.Recognizer()
with sr.Microphone(sample_rate = 48000) as source:
    print('teleradio: calibrating noise level')
    r.adjust_for_ambient_noise(source)
    print('teleradio: energy threshold at ' + str(r.energy_threshold))
    while True:
        # obtain audio from the microphone
        print('teleradio: listening for speech')
        audio = r.listen(source)
        print('teleradio: writing to file')
        with open('tmp.wav', 'wb') as file:
            file.write(audio.get_wav_data())
        # print('teleradio: processing speech')
        # nlp.handle_audio(audio = audio.get_wav_data(), intent_handlers = intent_handlers)
