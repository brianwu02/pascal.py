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

class PascalCompiler:

    def __init__(self):
        self.source_file = None
        self.scanner = None
        self.parser = None

    def _initialize_all_modules(self):
        self.scanner = Scanner(self.source_file)
        self.parser = Parser()

    def load(self, f):
        """assumes the input is a character array."""
        self.source_file = f
        self._initialize_all_modules()

    def run(self):
        """imports all required modules and runs the compiler."""
        assert self.source_file is not None
        print self.source_file
        pass

    def test_run(self):
        pass

if __name__ == "__main__":

    def read(path):
        with open(path, 'r') as f:
            return f.read()

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
        SOURCE_FILE_PATH = default_source

    file_to_compile = read(SOURCE_FILE_PATH)

    pc = PascalCompiler()
    pc.load(file_to_compile)
    pc.run()

