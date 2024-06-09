from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from enum import Enum


class Characters(Enum):
    pushButton_lower = ascii_lowercase
    pushButton_upper = ascii_uppercase
    pushButton_digits = digits
    pushButton_symbols = punctuation
