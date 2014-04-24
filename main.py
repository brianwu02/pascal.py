import os
from modules import scanner
from modules import parser

# The main component of the Pascal compiler written in Python.

# Scanning => Lexical Analysis: takes characters as input where the syntax is regular.
# Parsing  => Syntax Analysis: takes symbols as input where the syntax is context free.

"""tests to write:
    1. test that read correctly returns a character array
"""

SOURCE_FILE_PATH = 'pascal_sample_code/addition.ps'

def read(path):
    """returns a character array from source file."""
    with open(path, 'r') as f:
        return f.read()

def run():
    """imports all required modules and runs the compiler"""
    source_file = read(SOURCE_FILE_PATH)
    scanner = Scanner(source_file)
    parser = Parser()

def test_run():
    print SOURCE_FILE_PATH
    print read(SOURCE_FILE_PATH)

if __name__ == "__main__":
    test_run()
