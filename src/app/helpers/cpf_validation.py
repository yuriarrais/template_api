# REGRA PARA VALIDAR CPF
#
# O cálculo para validar um CPF é especificado pelo Ministério da Fazenda. O CPF é formado por 11 dígitos numéricos que
# seguem a máscara "###.###.###-##". Sua verificação acontece atraves da realização de um calculo utilizando os 9
# primeiros dígitos. O resultado desse calculo deve corresponder aos dois últimos dígitos(depois do sinal "-").
#
# Como exemplo, um CPF fictício "529.982.247-25"
#
# ----------------------------
# Validação do primeiro dígito
# ----------------------------
# Primeiramente soma-se a multiplicação dos 9 primeiros dígitos pela sequência decrescente de números de 10 à 2.
# 5 * 10 + 2 * 9 + 9 * 8 + 9 * 7 + 8 * 6 + 2 * 5 + 2 * 4 + 4 * 3 + 7 * 2 = 295
#
# Esse resultado deve ser multiplicado por 10 e dividirmos por 11.
# 295 * 10 / 11
#
# O resto da divisão deve ser igual ao primeiro dígito verificador(primeiro dígito depois do '-'). Se o resto da divisão
# for igual a 10, considerar como 0.
#
# Vamos conferir o primeiro dígito verificador do nosso exemplo: O resultado da divisão acima é '268' e o RESTO é 2.
# Isso significa que o nosso CPF exemplo passou na validação do primeiro dígito.
#
# ---------------------------
# Validação do segundo dígito
# ---------------------------
# Soma-se a multiplicação dos 10 primeiros dígitos pela sequência decrescente de números de 11 à 2.
# 5 * 11 + 2 * 10 + 9 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 2 * 5 + 4 * 4 + 7 * 3 + 2 * 2 = 347
#
# Esse resultado deve ser multiplicado por 10 e dividirmos por 11.
# 347 * 10 / 11
#
# O resto da divisão deve ser igual ao segundo dígito verificador(segundo dígito depois do '-').
#
# Com essa verificação, constatamos que o CPF 529.982 .247 - 25 é válido.
#
# NOTA: Existe alguns casos de CPFs que passam nessa validação, mas ainda são inválidos.
#       São os casos dos CPFs com dígitos repetidos(111.111 .111 - 11, 222.222 .222 - 22, ...)


def _check_invalid_cpfs(str_cpf):
    invalid_cpfs = [
        "00000000000",
        "11111111111",
        "22222222222",
        "33333333333",
        "44444444444",
        "55555555555",
        "66666666666",
        "77777777777",
        "88888888888",
        "99999999999"
    ]
    return True if str_cpf in invalid_cpfs else False


def _digits_calculator(str_cpf, qnt_dig, peso):
    dig_sum, mod = [0, 0]
    for i in range(1, qnt_dig + 1):
        dig_sum += int(str_cpf[i - 1]) * (peso - i)
        mod = (dig_sum * 10) % 11
    if mod == 10:
        mod = 0
    return mod


def validation(str_cpf):
    # definir função para retira caracteres inválidos
    if _check_invalid_cpfs(str_cpf):
        return False
    # Check the first digit
    mod = _digits_calculator(str_cpf, 9, 11)
    if mod != int(str_cpf[9]):
        return False
    # Check the second digit
    mod = _digits_calculator(str_cpf, 10, 12)
    if mod != int(str_cpf[10]):
        return False
    return True
