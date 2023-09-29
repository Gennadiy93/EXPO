from random import choice, randint
from string import ascii_letters, digits


def random_string(start: int = 1, end: int = 256) -> str:
    return ''.join(choice(ascii_letters + digits) for _ in range(randint(start, end)))
