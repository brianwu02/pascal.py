from token import Token 
from constants import SYMBOLS 
from constants import SYMBOLS_DICT
from constants import OPERATOR_DICT
from constants import RESERVED_WORD_DICT
import re

class TokenCreator:

    # design patterns say I should require my dependencies in the constructor
    # but I need to return a new token object each time the create function 
    # is called so what do I do?! Probably didnt need a class for this...
    
    def __init__(self):
        self.current_token = None
        self.previous_token = None
        self.next_token = None
        pass

    def create(self, tk_tuple):
        """method called by the scanner. takes a tokenizer string value
        as input and returns a token object."""
        token = self._parse_and_return_token(tk_tuple)
        return token

    def _parse_and_return_token(self, tk_tuple):
        
        # make init values none
        tk_val = None
        tk_type = None
        line_number = None
        line_index = None
        creation_state = None
        name = None

        tk_val = tk_tuple[0]
        tk_type = self._determine_type(tk_tuple[0])
        line_number = tk_tuple[1]
        line_index = tk_tuple[2]
        creation_state = tk_tuple[3]
        name = self._determine_name(tk_tuple[0])

        token = Token(
                tk_val = tk_val,
                tk_type = tk_type,
                line_num = line_number, 
                line_index = line_index,
                state = creation_state,
                name = name
                )

        return token

    def _determine_type(self, value):
        """ if value is found in symbol then look up it's value
        in hash tables OPERATORS_DICT and SYMBOLS_DICT
        """
        
        if value in RESERVED_WORD_DICT:
            return RESERVED_WORD_DICT[value]

        # if value is a symbol, then look up it's value in symbol lookup
        if value in SYMBOLS:

            if value in SYMBOLS_DICT:
                return SYMBOLS_DICT[value][0]

            if value in OPERATOR_DICT:
                return OPERATOR_DICT[value][0]

        # here, if NOT symbol and NOT reserved word, must be identifier or number literals
        
        # identifier --> letter { letter | digit }

        # number --> integer | real 
        # integer --> digit {digit} 
        
        # real --> integer '.' integer [exponent] 
        # exponent --> expDesignator [ '+' | '-' ] integer 
        # expDesignator --> 'e' | 'E' 

        if self._is_int(value):
            return "TK_INT_LITERAL"
        #else:
        #    if self._is_float(value):
        #        return "TK_REAL_LITERAL"

        if self._is_float(value):
            return "TK_REAL_LITERAL"
    

        # if it fails all the test, it is an identifier.
        return "TK_IDENTIFIER"
        # never reach this, still debugging
        return value

    def _determine_name(self, value):

        if value in SYMBOLS_DICT:
            return SYMBOLS_DICT[value][1]

        if value in OPERATOR_DICT:
            return OPERATOR_DICT[value][1]

        if self._is_int(value) or self._is_float(value):
            return "number"

        # again, if it falls through symbol and number check.
        # return "identifier"

        return value

    def _is_float(self, x):
        """Boolean helper method to determine if a string is TK_REAL_LITERAL"""
        try:
            a = float(x)
        except ValueError:
            return False
        else:
            return True

    def _is_int(self, x):
        """Boolean helper method to determine if a string is TK_INT_LITERAL"""
        try:
            a = float(x)
            b = int(a)
        except ValueError:
            return False
        else:
            return a == b
