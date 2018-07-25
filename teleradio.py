from io import BytesIO

import speech_recognition as sr
import nlp

from light import light_set
from music import music_play, music_stop
from power import shutdown, reboot


intent_handlers = {
'light_set': light_set,
'music_play': music_play,
'music_stop': music_stop,
'shutdown': shutdown,
'reboot': reboot}


r = sr.Recognizer()
with sr.Microphone(sample_rate = 48000) as source:
    print('teleradio: calibrating noise level')
    r.adjust_for_ambient_noise(source)
    print('teleradio: energy threshold at ' + str(r.energy_threshold))
    while True:
        # obtain audio from the microphone
        print('teleradio: listening for speech')
        audio = r.listen(source)
        print('teleradio: processing speech')
        audio_bytes = BytesIO(audio.get_wav_data())
        nlp.handle_audio(audio = audio_bytes, intent_handlers = intent_handlers)
