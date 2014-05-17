import os
import sys
from modules.scanner import Scanner
from modules.parser import Parser
from modules.runtime import VirtualRunTime

# Some terminology
# Scanning => Lexical Analysis: takes characters as input where the syntax is regular.
# Symbols => may refer to the symbol table which stores identifiers and reference to their corresponding values
# or a legal lexical character for example " ' , : ; etc.
# Token => an abstract symbol representing a lexical unit. they are input to the parser.
# Parsing  => Syntax Analysis: takes symbols as input where the syntax is context free.

# USAGE:
# python run_PascalCompiler [pascal-file-path]. if no path is provided, a default path is used instead.

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
        5. execute.
        6. profit?
        """
        scanner = self.scanner # because, self.
        parser = self.parser
        v_runtime = self.v_runtime
        
        # scan & print tokens
        scanner.scan()
        scanner.print_tokens()
        
        # return list of parsed tokens
        token_list = scanner.get_tokens()

        # load tokens in to parser.
        parser.load_tokens(token_list)
        #parser.print_tokens()
        parser.run()

        # pass instructions & symbol table to runtime
        instructions = parser.get_instructions()
        symbol_table = parser.get_symbol_table()
        v_runtime.load_instructions(instructions)
        v_runtime.load_symbol_table(symbol_table)
        v_runtime.print_instructions()
        v_runtime.run_dat_code()
        
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

