# Brian Wu
# Pascal Compiler written in Python
# brianwu02@gmail.com

"""List of Tokens
RESERVERED_WORDS:
    

IDENTIFIERS:

OPERATORS:
    arithmetic:
    logical:
    boolean:
    string:
    set:
    relational:
    class:

seperators: white_space, new_line
constants: float, integer, literal


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
        """all tokens must have these values"""
        
        self.current_tk = current_tk # not sure why this is needed yet.
        self.current_tk_val = current_tk_val
        self.current_name = current_name
        self.current_file = current_file
        self.current_line = current_line
        self.current_column = current_column

        pass

    def get_typeof(self):
        """returns the type of token"""
        pass

    def get_current_val(self):
        """returns the value of the token"""
        return str(self.current_value)

    def get_current_name(self):
        """returns the current name of the token"""
        return str(self.current_name)

    def get_current_file(self):
        """returns the current file the token is in.
        does not make sense yet. multiple files i guess?"""
        return str(self.current_file)

    def get_current_line(self):
        """returns the line of the token"""
        return str(self.current_line)

    def get_current_column(self):
        """returns the current column of the token"""
        return str(self.current_column)


    def __repr__(self):
        """ prety print the token here"""
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

class TK_COMMENT(Token):
    """Comment Token"""
    def __init__(self):
        pass
