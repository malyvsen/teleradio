from teleradio import log
from teleradio import nlp
from teleradio.tts import say


def light_set(text, entities):
    state = nlp.top_confidence(entities = entities, entity_name = 'gpio_state', min_confidence = .75)
    if state == 'on':
        say('Turning light on')
        return
    if state == 'off':
        say('Turning light off')
        return
    if state == 'toggle':
        say('Toggling light')
        return
    log.warning('light_set state unclear')
    say('Clarify what to do with the light.')
    return
