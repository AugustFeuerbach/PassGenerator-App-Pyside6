import secrets
from math import log2
from enum import IntEnum

# Модуль генерації пароля. В аргументі довжина і всі символи які викорс. в строці
def create_new(length: int, characters: str) -> str:
    return "".join(secrets.choice(characters) for _ in range(length)) # робимо генератор з випадкових символів і єднаєм їх строку

# получаємо ентропію паролю по формулі H = log2N^L = L x log2N
# N - ксть можливих символів L - ксть символів в паролі Н - вим. в бітах
def get_entropy(length:int, character_number: int) -> float:
    try:
        entropy = length * log2(character_number)
    except ValueError:
        return 0.0
    return round(entropy, 2)

# получаємо перечислення для важкості паролю
class StrengthToEntropy(IntEnum):
    Hopeless = 0
    Weak = 30
    Good = 50
    Strong = 70
    Perfect = 120