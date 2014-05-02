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
        'if': 'TK_IF',
        'else': 'TK_ELSE',
        'for': 'TK_FOR',
        'while': 'TK_WHILE',
        'begin': 'TK_BEGIN',
        'var': 'TK_VAR',
        'end': 'TK_END',
        'program': 'TK_PROGRAM',
        'writeln': 'TK_WRITELN'
        }

OPERATOR_DICT = {
        ':=': ('TK_ASSIGNMENT_OP', 'assignment'),
        '+': ('TK_ADDITION_OP', 'addition'),
        '-': ('TK_SUBTRACTION_OP', 'subtraction'),
        '*': ('TK_MULTIPLICATION_OP', 'multiplication'),
        '/': ('TK_DIVISION_OP', 'division'),
        '=': ('TK_EQUALS_OP', 'equals'),
        '>': ('TK_GREATER_THAN_OP', 'greater_than'),
        '<': ('TK_LESS_THAN_OP', 'less_than'),
        '<>': ('TK_UNEQUAL_OP', 'unequal'),
        '<=': ('TK_LTOE', 'less_than_or_equals'),
        '>=': ('TK_GTOE', 'greater_than_or_equals')
        }

SYMBOLS_DICT = {
        '(': ('TK_L_PAREN', 'parenthesis'),
        ')': ('TK_R_PAREN', 'parenthesis'),
        '[': ('TK_L_BRACKET', 'bracket'),
        ']': ('TK_R_BRACKET', 'bracket'),
        '{': ('TK_L_COMMENT_BRACE', 'brace'),
        '}': ('TK_R_COMMENT_BRACE', 'brace'),
        ';': ('TK_SEMICOLON', 'semicolon'),
        ',': ('TK_COMMA', 'comma'),
        '.': ('TK_PERIOD', 'period')
        }


# http://www.freepascal.org/docs-html/ref/refsu1.html#x12-110001.3.1
TURBO_PASCAL_RESERVED_WORDS = []

# Identifiers are defined names for specific constants, types, variables, procedures, units, and programs.
# All identifers consist between 1 and 127 significant characters (letters, digits,
# and underscores), of which the first must be a letter (a-z or A-Z or _)
