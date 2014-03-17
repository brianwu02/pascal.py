# Pascal Constants

# reserved_words: words which have a fixed meaning in language, cannot be changed or redefined
# identifiers: names of symbols that the programmer defines
# operators: symbols for mathematical or other operations
# seperator: white space
# constants: numerical or character constants used to denote actual values. 

SYMBOLS = [
        '+', '-', '*', '/' ,'=', '<', '>',
        '[' , ']', '.', ',', '(', ')', ':',
        '^', '@', '{', '}', '$', '#', '&',
        '%', '<<' ,'>>','**', '<>', '><', 
        '<=', '>=', ':=', '+=', '-=', '*=',
        '/=', '(*', '*)', '(.', '.)', '//', 
        ';', '='
        ]

DOUBLE_SYMBOLS = [
        # remember, some of these might need to be escaped while parsing
        '<<', '>>', '**', '<>', '><',
        '<=', '>=', ':=', '+=', '-=',
        '-=', '*=', '/=', '(*', '*)',
        '(.', '.)', '//'

        ]

"""
IDENTIFIERS = [
    '<', '<>', '<<', ':', ':=', '>', '>>',
    '<=', '>=', '-', '+', '*', '/', ';', ',',
    '[', ']', '(', ')', '=', '^', '@', '(*'
    ]
"""

RESERVED_WORDS = [
    'program', 'var', 'begin', 'end', 'type',
    'procedure', 'uses', 'function', 'for', 'while', 'repeat',
    'do', 'then', 'downto', 'to','if', 'else', 'array', 'of',
    'not', 'or',  'mod', 'and', 'const', 'div','record', 'exit'
    ]

# http://www.freepascal.org/docs-html/ref/refsu1.html#x12-110001.3.1
TURBO_PASCAL_RESERVED_WORDS = []

# Identifiers are defined names for specific constants, types, variables, procedures, units, and programs.
# All identifers consist between 1 and 127 significant characters (letters, digits,
# and underscores), of which the first must be a letter (a-z or A-Z or _)
