from api.utils import (min_special_chars, min_digit, min_lowercase,
                       min_size, min_uppercase, no_repeted)


def characters():
    return "TesteSenhaForte!123&"


def test_min_special():
    "Testa o retorno de min_special_chars"
    value = characters()
    assert min_special_chars(value, 4) == "minSpecialChars"


def test_min_digit():
    "Testa o retorno de min_digit"
    value = characters()
    assert min_digit(value, 4) == "minDigit"


def test_min_lowercase():
    "Testa o retorno de min_lowercase"
    value = characters()
    assert min_lowercase(value, 15) == "minLowercase"


def test_min_size():
    "Testa o retorno de min_size"
    value = characters()
    assert min_size(value, 15) is None


def test_min_uppercase():
    "Testa o retorno de min_uppercase"
    value = characters()
    assert min_uppercase(value, 4) == "minUppercase"


def test_no_repeat():
    "Testa o retorno de no_repeat"
    value = characters()
    assert no_repeted(value) is None
