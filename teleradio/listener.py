from io import BytesIO
import speech_recognition as sr

from teleradio import log
from teleradio import nlp
from teleradio.tts import say


def listen():
    r = sr.Recognizer()
    with sr.Microphone(sample_rate = 48000) as source:
        say('Calibrating. Silence, please.')
        log.update('calibrating noise level')
        r.adjust_for_ambient_noise(source)
        log.update('energy threshold at ' + str(r.energy_threshold))

        say('Ready.')
        while True:
            # obtain audio from the microphone
            log.update('listening for speech')
            audio = r.listen(source)
            log.update('processing speech')
            with open('/tmp/teleradio.wav', 'wb') as f:
                f.write(audio.get_wav_data())
            audio_bytes = BytesIO(audio.get_wav_data())
            nlp.handle_audio(audio = audio_bytes)
