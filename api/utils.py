def min_special_chars(password: str, rule: int):
    characters = '!@#$%^&*()-+\/{}[]'


def min_size(password: str, rule: int):
    if len(password) < rule:
        return "minSize"


def min_uppercase(password: str, rule: int):
    count = 0
    for caracter in password:
        if caracter.isupper():
            count += 1
    if count < rule:
        return "minUppercase"


def min_lowercase(password: str, rule: int):
    count = 0
    for caracter in password:
        if caracter.islower():
            count += 1
    if count < rule:
        return "minLowercase"

def min_digit(password: str, rule: int):
    count = 0
    for caracter in password:
        if caracter.isdigit():
            count += 1
    if count < rule:
        return "minDigit"


def no_repeted(password: str):
    count = 0
    index = 0
    while index < len(password) - 1:
        if password[index] == password[index + 1]:
            count += 1
            break
    if count != 0:
        return "noRepeted"


def verify(password, rules):
    failed = []
    params = ["minSize", "minUppercase", "minLowercase", "minDigit", "noRepeted", "minSpecialChars"]
    for rule in rules:
    
