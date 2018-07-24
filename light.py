import nlp


def light_set(text, entities, tts):
    state = nlp.top_confidence(entities = entities, entity_name = 'on_off', min_confidence = .75)
    if state is 'on':
        print('teleradio: light_set on')
        tts.say('Turning light on')
        return
    if state is 'off':
        print('teleradio: light_set off')
        tts.say('Turning light off')
        return
    if state is 'toggle':
        print('teleradio: light_set toggle')
        tts.say('Toggling light')
        return
    print('teleradio warning: light_set state unclear')
    tts.say('Clarify what to do with the light.')
    return
