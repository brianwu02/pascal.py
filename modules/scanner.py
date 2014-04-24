from constants import SYMBOLS
from constants import DOUBLE_SYMBOLS
from character import Character
from token import Token
from tokenizer import Tokenizer

# REMEMBER:
#
# context-free: subsitution of the symbols left of the '=' by a sequence derived from
# the expression right of the '=' is always permitted regardless of the context embedded
# witin the sentence.
#
# Scanning => Lexical Analysis: takes characters as input where the syntax is regular.
# Parsing  => Syntax Analysis: takes symbols as input where the syntax is context free.
#
# move this in to the wiki afterwards, leave it here for now.
# TODO:
# 1. Tokenize everything.
#   This process returns no errors. Tokenizer's only job is to return a 
#   valid token. Only during the parsing phase will the compiler return syntax errors.
# 
#   a) RESERVED_WORD => RESERVED_WORD TOKEN
#       - for each token object, determine whether it's a RESERVERD WORD.
#

"""
RESERVED WORD LOGIC:
    - a token is reserved word when the token's string value matches
      a string from the reserved word list found in constants.py
"""

def main():
    s = Tokenizer()
    for char in s:
        print("TOKEN: ( %s )") % char



if __name__ == "__main__":
    main()
