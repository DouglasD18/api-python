# Que verifica a regra de caracteres especiais
def min_special_chars(password: str, rule: int):
    characters = "!@#$%^&*()-+\\/{}[]"
    count = 0
    for caracter in password:
        if caracter in characters:
            count += 1
    if count < rule:
        return "minSpecialChars"


# Que verifica a regra do tamanho mínimo da senha
def min_size(password: str, rule: int):
    length = len(password)
    if length < rule:
        return "minSize"


# Que verifica a regra de mínimo de letras maiusculas da senha
def min_uppercase(password: str, rule: int):
    count = 0
    for caracter in password:
        if caracter.isupper():
            count += 1
    if count < rule:
        return "minUppercase"


# Que verifica a regra de mínimo de letras minusculas da senha
def min_lowercase(password: str, rule: int):
    count = 0
    for caracter in password:
        if caracter.islower():
            count += 1
    if count < rule:
        return "minLowercase"


# Que verifica a regra de quantidade mínima de dígitos na senha
def min_digit(password: str, rule: int):
    count = 0
    for caracter in password:
        if caracter.isdigit():
            count += 1
    if count < rule:
        return "minDigit"


# Que verifica se a senha tem caracteres repetidos consecutivos
def no_repeted(password: str):
    count = 0
    index = 0
    while index < len(password) - 1:
        if password[index] == password[index + 1]:
            count += 1
            break
        index += 1
    if count != 0:
        return "noRepeted"
