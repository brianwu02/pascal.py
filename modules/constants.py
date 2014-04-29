# Pascal Constants

# reserved_words: words which have a fixed meaning in language, cannot be changed or redefined
# identifiers: names of symbols that the programmer defines
# operators: symbols for mathematical or other operations
# seperator: white space
# constants: numerical or character constants used to denote actual values. 

TOKEN_TYPES = [
        'int_literal',
        'real_literal',
        'char_literal'
        'identifier',
        'operator',
        'datatype'
        ]

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


RESERVED_WORDS = [
    'program', 'var', 'begin', 'end', 'type',
    'procedure', 'uses', 'function', 'for', 'while', 'repeat',
    'do', 'then', 'downto', 'to','if', 'else', 'array', 'of',
    'not', 'or',  'mod', 'and', 'const', 'div','record', 'exit'
    ]


# matches reserverd_word to corresponding token_type
RESERVED_WORD_DICT = {
        'if': 'tk_if',
        'else': 'tk_else',
        'for': 'tk_for',
        'while': 'tk_while',
        'begin': 'tk_begin',
        'var': 'tk_var',
        'end': 'tk_end',
        'program': 'tk_program'
        }

OPERATOR_DICT = {
        ':=': 'tk_assignment_op',
        '+': 'tk_addition_op',
        '-': 'tk_subtraction_op',
        '*': 'tk_multiplication_op',
        '/': 'tk_division_op',
        '=': 'tk_equal_op',
        '>': 'tk_greater_than_op',
        '<': 'tk_less_than_op',
        '<>': 'tk_unequal_op',
        '<=': 'tk_less_than_or_equal_op',
        '>=': 'tk_greater_than_or_equal_op',
        }

SYMBOLS_DICT = {
        '(': ('tk_left_parenthesis', 'parenthesis'),
        ')': ('tk_right_parenthesis', 'parenthesis'),
        '[': ('tk_left_bracket', 'bracket'),
        ']': ('tk_right_bracket', 'bracket'),
        '{': ('tk_left_comment_brace', 'brace'),
        '}': ('tk_right_comment_brace', 'brace'),
        ';': ('tk_semicolon', 'semicolon'),
        ',': ('tk_comma', 'comma')
        }


# http://www.freepascal.org/docs-html/ref/refsu1.html#x12-110001.3.1
TURBO_PASCAL_RESERVED_WORDS = []

# Identifiers are defined names for specific constants, types, variables, procedures, units, and programs.
# All identifers consist between 1 and 127 significant characters (letters, digits,
# and underscores), of which the first must be a letter (a-z or A-Z or _)
