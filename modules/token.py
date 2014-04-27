# Brian Wu
# Pascal Compiler written in Python
# brianwu02@gmail.com

"""List of Tokens
RESERVERED_WORDS:
    

IDENTIFIERS:

OPERATORS:
    arithmetic: + - * / Div Mod
    logical: not and or xor shl shr << >>
    boolean: not and or xor
    string: 
    set: 
        + : Union
        - : Difference
        >< : Symmetric Difference
        <= : contains
        include : include an element in the set
        exclude : exclude an element from the set
        in: check whether an element is in the set
    relational:
        = : equal
        <> : Not Equal
        < : strictly less than
        > : strictly greater than
        <= : less than or equal
        >= : greater than or equal
        in : Element of

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

    def __init__(self, word):
        """all tokens must have these values"""
        
        self.tk_value = tk_value
        self.tk_type = tk_type

        #self.current_name = current_name
        #self.current_file = current_file
        #self.current_line = current_line
        #self.current_column = current_column

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

    # what does even mean? What was I thinking when I wrote this?
    # Line column where the token is found? Delete this method sometime later.
    def get_current_column(self):
        """returns the current column of the token"""
        return str(self.current_column)

    def __repr__(self):
        """ prety print the token here"""
        pass
