import os
from parser import Parser
from scanner import Scanner

# The main component of the Pascal compiler written in Python.

# Scanning => Lexical Analysis: takes characters as input where the syntax is regular.
# Parsing  => Syntax Analysis: takes symbols as input where the syntax is context free.

# path to source file. can later make this a command line input.
SOURCE_FILE_PATH = 'pascal-sample-code/addition.ps'

def read(path):
    with open(path, 'r') as f:
        return f.read()

def run():
    """imports all required modules and runs the compiler.
    """
    source_file = read(PATH)
    scanner = Scanner()
    parser = Parser()

def test_run():
    print read(SOURCE_FILE_PATH)


if __name__ == "__main__":
    test_run()
