import os
import sys
from modules.scanner import Scanner
from modules.parser import Parser

# The main component of the Pascal compiler written in Python.

# Scanning => Lexical Analysis: takes characters as input where the syntax is regular.
# Parsing  => Syntax Analysis: takes symbols as input where the syntax is context free.

"""tests to write:
    1. test that read correctly returns a character array
"""

# try to read source file from command line argument
# if it does not exist, use a default pascal file. 
default_source = 'pascal_sample_code/addition.ps'
try:
    if os.path.isfile(sys.argv[1]):
        SOURCE_FILE_PATH = sys.argv[1]
    else:
        SOURCE_FILE_PATH = default_source
        print("file: '%s' does not exist, using '%s' instead.") % (
                sys.argv[1],
                SOURCE_FILE_PATH
                )
except IndexError:
    # default action when no argument is entered.
    SOURCE_FILE_PATH = default_source

def read(path):
    """returns a character array from source file."""
    with open(path, 'r') as f:
        return f.read()

def run():
    """imports all required modules and runs the compiler"""
    source_file = read(SOURCE_FILE_PATH)
    scanner = Scanner(source_file)
    
    list_of_tokens = scanner.get_list_of_tokens()
    print list_of_tokens

    parser = Parser()

def test_run():
    #print read(SOURCE_FILE_PATH)
    print SOURCE_FILE_PATH

if __name__ == "__main__":
    test_run()
    #run()
