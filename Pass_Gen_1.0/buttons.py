from string import ascii_lowercase, ascii_uppercase, digits, punctuation

from enum import Enum


# робимо перечислення яке привязує кнопки вибору символів до строкових змінних
class Characters(Enum):
    btn_upper = ascii_uppercase
    btn_lower = ascii_lowercase
    bnt_special = punctuation
    btn_digits = digits


# створюємо словник з к-стю символів на кожний пул
Character_Number = {
    'btn_upper': len(Characters.btn_upper.value),
    'btn_lower': len(Characters.btn_lower.value),
    'btn_digits': len(Characters.btn_digits.value),
    'bnt_special': len(Characters.bnt_special.value)
}

#ставимо генерацію паролю на кнопки
Generate_Password = (
    'btn_refresh',  'btn_lower',  'btn_upper',  'btn_digits',  'bnt_special'
)

