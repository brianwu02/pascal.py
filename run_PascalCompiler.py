import os
import sys
from modules.scanner import Scanner
from modules.parser import Parser
from modules.runtime import VirtualRunTime

# The main component of the Pascal compiler written in Python.

# Scanning => Lexical Analysis: takes characters as input where the syntax is regular.
# Parsing  => Syntax Analysis: takes symbols as input where the syntax is context free.

class PascalCompiler:
    def __init__(self):
        self.source_file = None
        self.scanner = None
        self.parser = None
        self.v_runtime = None

    def _initialize_all_modules(self):
        self.scanner = Scanner(self.source_file)
        self.parser = Parser()
        self.v_runtime = VirtualRunTime()

    def load(self, f):
        """assumes the input is a character array."""
        self.source_file = f
        self._initialize_all_modules()

    def run(self):
        """imports all required modules and runs the compiler.
        1. scan input file and create tokens.
        2. pass token stream to parser.
        3. parse token stream & generate intermediate code.
        4. send intermediate code to virtual run time.
        5. profit?
        """
        scanner = self.scanner # because, self
        parser = self.parser
        assert self.source_file is not None
        assert scanner is not None
        assert parser is not None
        
        # scan & print tokens
        scanner.scan()
        scanner.print_tokens()
        
        # return list of parsed tokens
        token_list = scanner.get_tokens()

        # load tokens in to parser.
        parser.load_tokens(token_list)
        #parser.print_tokens()
        parser.run()

        # pass instructions to runtime
        instructions = parser.get_instructions()
        self.v_runtime.load_instructions(instructions)
        self.v_runtime.print_instructions()
        

    def test_run(self):
        pass

if __name__ == "__main__":

    def read(path):
        with open(path, 'r') as f:
            return f.read()

    default_source = 'pascal_sample_code/addition.pas'
    
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

