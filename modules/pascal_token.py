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

    def __init__(self, tk_val, tk_type, line_num, line_index, state, name):
        """all tokens must have these values"""
        
        self.tk_value = tk_val
        self.tk_type = tk_type
        self.line_number = line_num
        self.line_index = line_index
        self.creation_state = state
        self.name = name

    def get_type(self):
        """returns the type of token"""
        return self.tk_type

    def get_value(self):
        """returns the value of the token"""
        return self.tk_value

    def get_name(self):
        """returns the current name of the token"""
        return self.name

    def get_current_file(self):
        """returns the current file the token is in.
        does not make sense yet. multiple files i guess?"""
        return str(self.current_file)

    def get_line_number(self):
        """returns the line of the token"""
        return self.line_number

    def get_line_index(self):
        """returns the index with respect to line"""
        return self.line_index

    def get_creation_state(self):
        return self.creation_state

    # what does even mean? What was I thinking when I wrote this?
    # Line column where the token is found? Delete this method sometime later.
    def get_current_column(self):
        """returns the current column of the token"""
        return str(self.current_column)

    def __repr__(self):
        """ prety print the token here"""
        pass
