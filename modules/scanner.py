from constants import SYMBOLS
from constants import DOUBLE_SYMBOLS
from character import Character
from token import Token
from tokenizer import Tokenizer


if __name__ == "__main__":
    s = Tokenizer();
    for char in s:
        print("TOKEN: ( %s )") % (char)
