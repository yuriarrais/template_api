from src.config.locales import strings


# O segundo parametro deve ser setado na sessão do usuário
def msg(parameter, lang="pt_br"):
    return strings.lang[lang][parameter]
