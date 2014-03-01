# Brian Wu
# Pascal Compiler
# Main File
import sys
from Scanner import *


def read_source(source_file):
    with open(source_file, 'r') as f:
        return f.read().lower()

def main(src_file):
    """main loop.
    """
    scanner = Scanner(src_file)
    scanner.print_src()
    scanner.get_next_token()
    scanner.print_ascii()
    scanner.print_enum()




if __name__ == "__main__":
    src_file = read_source(sys.argv[1])
    main(src_file)
