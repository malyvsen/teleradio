from wit import Wit
from wit.wit import WitError

from teleradio import log
from teleradio.tts import say
from teleradio import config
from teleradio import handlers


wit_client = Wit(config.wit_key)


# message handling
def handle_audio(audio):
    try:
        wit_response = wit_client.speech(audio_file = audio, headers = {'Content-Type': 'audio/wav'})
    except WitError:
        dump_path = '/tmp/teleradio_error.wav'
        read_audio = audio.read()
        log.error('wit error, dumping ' + str(len(read_audio)) + ' bytes of audio to ' + dump_path)
        with open(dump_path, 'wb') as dump_file:
            dump_file.write(read_audio)
        return
    entities = wit_response['entities']
    intent = top_confidence(entities, entity_name = 'intent', min_confidence = .9)
    if intent is None:
        log.warning('intent unclear')
        say('Intent unclear. Please repeat or phrase your request differently.')
        return
    if not hasattr(handlers, intent):
        log.error('intent handler not provided')
        say('No handler provided for intent: ' + intent)
        return
    log.update('handling intent ' + intent)
    getattr(hanlders, intent)(text = wit_response['_text'], entities = entities)


def confidence_order(entities, entity_name):
    if entity_name not in entities:
        return []
    return sorted(entities[entity_name], key = lambda entity: -entity['confidence']) # sorted by decresing confidence


def top_confidence(entities, entity_name, min_confidence = 0):
    ordered = confidence_order(entities = entities, entity_name = entity_name)
    if len(ordered) == 0:
        return None
    if ordered[0]['confidence'] < min_confidence:
        return None
    return ordered[0]['value']
