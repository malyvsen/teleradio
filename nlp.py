import os
from wit import Wit


# environment variables
wit_key_env = 'WIT_KEY'


# initialization
if wit_key_env not in os.environ:
    print('Create environment variable ' + wit_key_env + ' to store your Wit.ai server access token')
    exit()

wit_key = os.environ[wit_key_env]
wit_client = Wit(wit_key)


# message handling
def handle_audio(audio, tts, intent_handlers):
    wit_response = wit_client.speech(audio_file = audio, verbose = None, headers = {'Content-Type': 'audio/wav'})
    entities = wit_response['entities']
    intent = top_confidence(entities, entity_name = 'intent', min_confidence = .9)
    if intent is None:
        print('teleradio warning: intent unclear')
        tts.say('Intent unclear. Please repeat or phrase your request differently.')
        return
    if intent not in intent_handlers:
        print('teleradio warning: intent handler not provided')
        tts.say('No handler provided for intent: ' + intent)
        return
    intent_handlers[intent](text = text, entities = entities, tts = tts)


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
