from io import BytesIO
import speech_recognition as sr

from teleradio import log
from teleradio import nlp


def listen():
    r = sr.Recognizer()
    with sr.Microphone(sample_rate = 48000) as source:
        log.update('calibrating noise level')
        r.adjust_for_ambient_noise(source)
        log.update('energy threshold at ' + str(r.energy_threshold))
        while True:
            # obtain audio from the microphone
            log.update('listening for speech')
            audio = r.listen(source)
            log.update('processing speech')
            audio_bytes = BytesIO(audio.get_wav_data())
            nlp.handle_audio(audio = audio_bytes)
