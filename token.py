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

class Token:
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
        return str(self.value)

    def __repr__(self):
        pass

class TK_INTLIT(Token):
    """Integer Literal Token"""
    def __init__(self):
        pass

class TK_REALLIT(Token):
    """Real Literal token"""
    def __init__(self):
        pass

class TK_STRLIT(Token):
    """String Literal Token"""
    def __init__(self):
        pass

class TK_KEYWORD(Token):
    """Keyword Token"""
    def __init__(self):
        pass

class TK_ID(Token):
    """TK_ID Identifier Token"""
    def __init__(self):
        pass

class TK_EOF(Token):
    """TK_EOF End of Line, End of File Token"""
    def __init__(self):
        pass
