import random
import string


def hash_generator(length=8, digits=False):
    symbols = string.ascii_lowercase + string.digits if digits is True else string.ascii_lowercase
    return ''.join([random.choice(symbols) for _ in range(length)])
