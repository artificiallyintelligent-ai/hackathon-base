from .stubs import *

output = ""


def turn():
    global output
    output = ["R", "P", "S"][get_turn() % 3]
