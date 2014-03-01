""" List of Tokens

Literals:
    Integer (TK_INTLIT, value)
    Real (TK_REALLIT, index -> real table)
    Chars (TK_INTLIB | TK_CHARLIT, index -> string table)
    Strings (TK_STRLIT, index -> string table)

Keywords (individual type, --)
Identifiers (TK_ID, --, curname)
EOL? EOF? (TK_EOF, --)

TOKEN:
    int curtoken;
    int curtokenvalue;
    string curname;
    curfile;
    curline;
    curcol;

(TK_ID, --, curvalue) where -- is TK_A_VAR, index -> symtable

use LL parser style.
"""

class Token():
    """ A token object"""
    def __init__(self):
        self.value = value
        self.current_line = current_line
        self.current_column = current_column
        pass

    def typeof(self):
        """returns the type of token"""
        pass

    def value(self):
        """returns the value of the token"""
        pass

    def __repr__(self):
        pass

class Integer_Token(Token):
    """Integer Token"""
    def __init__(self):
        pass

class RealNum_Token(Token):
    """Real Number token"""
    def __init__(self):
        pass

class String_Token(Token):
    """String Token"""
    def __init__(self):
        pass

class Keyword_Token(Token):
    """Keyword Token"""
    def __init__(self):
        pass

class Identifier_Token(Token):
    """Identifier Token"""
    def __init__(self):
        pass

class EOL_EOF_Token(Token):
    """End of Line, End of File Token"""
    def __init__(self):
        pass
