import nlp
from tts import say


def light_set(text, entities):
    state = nlp.top_confidence(entities = entities, entity_name = 'on_off', min_confidence = .75)
    if state == 'on':
        print('teleradio: light_set on')
        say('Turning light on')
        return
    if state == 'off':
        print('teleradio: light_set off')
        say('Turning light off')
        return
    if state == 'toggle':
        print('teleradio: light_set toggle')
        say('Toggling light')
        return
    print('teleradio warning: light_set state unclear')
    say('Clarify what to do with the light.')
    return
