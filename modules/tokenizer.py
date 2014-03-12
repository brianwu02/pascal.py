from constants import IDENTIFIERS 
import re

class Tokenizer:
    """Everytime Tokenizer is called, it should return the next token"""

    def __init__(self):
        """
        self.source_file: holds the source file as a String
        self.current_index: current index of source_file
        self.current_line: current line
        self.token_list: holds list of all the tokens
        """
        self.source_file = self.open_file('sample.ps')
        self.current_index = 0
        self.current_line = 1
        self.times_called_next = 0
        self.token_list = []

    def __iter__(self):
        return self
    """
    def next(self):
        self.times_called_next += 1
        token = ''
        src_file = self.source_file
        while (src_file[self.current_index] != ' '):
            token += src_file[self.current_index]
            self.current_index += 1
            print(self.current_index)
        self.current_index += 1
        print('you called next() %s times') % (self.times_called_next)
        return token
    """

    def next(self):
        token = ''
        while True:
            char = self.get_next_character()

            if self.is_EOF(char):
                # end of line or file, we are done here.
                pass

            if self.is_identifier(char):
                # character is an identifier, so return token
                token = char
                break

            if self.is_whitespace(char):
                # 
                break

            if self.is_newline(char):

                break

            if self.is_character(char):
                token += char
                continue

            else:
                # not identifier, whitespace, or newline
                print("this isn't suppose to happen yet, figure out why")
                pass
        return token
 
    def is_EOF(self, char):
        # remember to fix this.
        return False


    def is_character(self, char):
        m = re.search("[a-zA-Z]", char)
        if m:
            return True
        else:
            return False

    def is_number(self, char):
        m = re.search("[0-9]", char)
        if m:
            return True
        else:
            return False

    def is_identifier(self, char):
        """returns boolean for input token"""
        if char in IDENTIFIERS:
            return True
        else:
            return False

    def is_whitespace(self, char):
        """boolean. returns true if next_char is whitespace"""
        if char == " ":
            return True
        else:
            return False

    def is_newline(self, char):
        """Boolean. returns true if next_char is newline character"""
        pass

    def get_next_character(self):
        """returns the next character"""
        c = self.source_file[self.current_index]
        self.current_index += 1
        return c
   
    def open_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()

    def print_string(self):
        print self.source_file

    def __repr__(self):
        pass


if __name__ == "__main__":
    s = Tokenizer()
    s.print_string()
    iter(s)
    print next(s)
