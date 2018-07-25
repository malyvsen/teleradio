import config

from wit import Wit
from tts import say


wit_client = Wit(config.wit_key)


# message handling
def handle_audio(audio, intent_handlers):
    wit_response = wit_client.speech(audio_file = audio, headers = {'Content-Type': 'audio/wav'})
    entities = wit_response['entities']
    intent = top_confidence(entities, entity_name = 'intent', min_confidence = .9)
    if intent is None:
        print('teleradio warning: intent unclear')
        say('Intent unclear. Please repeat or phrase your request differently.')
        return
    if intent not in intent_handlers:
        print('teleradio warning: intent handler not provided')
        say('No handler provided for intent: ' + intent)
        return
    print('teleradio: handling intent ' + intent)
    intent_handlers[intent](text = wit_response['_text'], entities = entities)


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
