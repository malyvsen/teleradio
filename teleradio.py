import speech_recognition as sr
import nlp

from light import light_set
from music import music_play, music_stop


intent_handlers = {
'light_set': light_set,
'music_play': music_play,
'music_stop': music_stop}


r = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        # obtain audio from the microphone
        print('teleradio: listening for speech')
        audio = r.listen(source)
        print('teleradio: processing speech')
        nlp.handle_audio(audio = audio.get_wav_data(), intent_handlers = intent_handlers)
