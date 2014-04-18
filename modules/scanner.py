from constants import SYMBOLS
from constants import DOUBLE_SYMBOLS
from character import Character
from token import Token
from tokenizer import Tokenizer

# TODO:
# 1. RESERVED_WORD => RESERVED_WORD TOKEN
#   - for each token object, determine whether it's a RESERVERD WORD.
#
"""
    RESERVED WORD LOGIC:
    - a token is reserved word when the token's string value matches
      a string from the reserved word list found in constants.py

    -
"""
if __name__ == "__main__":
    s = Tokenizer();
    for char in s:
        print("TOKEN: ( %s )") % (char)
