def error(text):
    log('teleradio error: ' + text, level = verbosity_level.error)


def warning(text):
    log('teleradio warning: ' + text, level = verbosity_level.warning)


def update(text):
    log('teleradio update: ' + text, level = verbosity_level.update)


def detail(text):
    log('teleradio detail: ' + text, level = verbosity_level.detail)


class verbosity_level:
    silent = 0
    error = 1
    warning = 2
    update = 3
    detail = 4


verbosity = verbosity_level.update


def get_format(level):
    if level == verbosity_level.error:
        return '\033[91m'
    if level == verbosity_level.warning:
        return '\033[93m'
    if level == verbosity_level.update:
        return '\033[94m'
    if level == verbosity_level.detail:
        return ''


def log(text, level = verbosity_level.update):
    if level > verbosity:
        return
    print(get_format(level) + text + '\033[0m')
