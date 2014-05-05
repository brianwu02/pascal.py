from tokenizer import Tokenizer
from token_creator import TokenCreator

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
class Scanner:
    """This is the Lexical Analyzer.
    It takes characters as input and outputs a stream of tokens.
    """
    def __init__(self, source_file):
        self.tokenizer = Tokenizer(source_file)
        self.token_creator = TokenCreator()
        self.token_list = []
        
    def scan(self):
        """main method exposed aside from deubgs to compiler.
        side-effect unfriendly. only run once.
        runs the tokenizer + tokenCreator and pushes all objects in to token_list.
        Reads the string values from tokenizer and attempts to create a token object.
        """

        tokenizer = self.tokenizer
        tk_creator = self.token_creator
        tk_list = self.token_list

        # iterate over token strings in tokenizer and
        # append the token object to tk_list
        #for tuple_val in tokenizer:
        #    tk_list.append(tk_creator.create(tuple_val))

        [tk_list.append(tk_creator.create(tuple_val)) for tuple_val in tokenizer]

        # currently runs as a side-effect but i guess thats the only
        # easy way to write this, this cannot be run twice as it uses
        # an iterator and the tokenizer object will not return any more elements.

    def print_tokens(self):
        i = 1
        for s in self.token_list:
            print "%s %s" % (i, s)
            i += 1

    def get_tokens(self):
        """returns internal list of token objects. used by parser"""
        return self.token_list


if __name__ == "__main__":
    # do nothing.
    pass
