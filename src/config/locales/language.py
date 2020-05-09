from src.config.parameters import lang
from src.config.locales import strings


# O pt_br deve ser setado na sessão do usuário
def msg(parameter):
    return strings.lang[lang][parameter]
