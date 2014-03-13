from constants import SYMBOLS
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
        self.current_token = ''

    def __iter__(self):
        return self

    def next(self):
        token = ''

        while True:
            char = self.get_next_character()

            if self.is_quote(char):
                token = self.handle_quote(char)
                break

            if self.is_identifier(char):
                # character is an identifier, so return token
                token += char
                break

            if self.is_num(char):
                # need to handle digits used in strings etc.
                token = char
                nxt_char = self.lookahead_char()
                while self.is_num(nxt_char):
                    token += char
                break

            if self.is_whitespace(char):
                break

            if self.is_newline(char):
                self.current_line += 1
                continue

            if self.is_character(char):
                token += char
                continue

            else:
                # not identifier, whitespace, or newline
                print("The else condition in next() method, should not occur yet.")
                print("the char: %s") % (char)
                pass

        self.current_token = token

        return token

    def get_next_character(self):
        """returns the next character"""
        if self.is_done():
            raise StopIteration

        char = self.source_file[self.current_index]
        self.current_index += 1
        return char 

    def lookahead_char(self):
        return self.source_file[self.current_index+1]

    def handle_quote(self, char):
        """this occurs when a quote is detected. should keep retrieving
        characters until another quote is detected."""
        current_string = char
        while True:
            # until another quote is detected... keep going
            char = self.get_next_character()
            current_string += char
            if self.is_quote(char):
                break
        return current_string

    def is_EOF(self, char):
        # remember to fix this.
        return False

    def is_character(self, char):
        m = re.search("[a-zA-Z]", char)
        if m:
            return True
        return False

    def is_num(self, char):
        m = re.search("[0-9]", char)
        if m:
            return True
        return False

    def is_identifier(self, char):
        """returns boolean for input token"""
        if char in SYMBOLS:
            return True
        return False

    def is_quote(self, char):
        if char == "\'":
            return True
        return False

    def is_whitespace(self, char):
        """boolean. returns true if next_char is whitespace"""
        if char == " ":
            return True
        return False

    def is_newline(self, char):
        """Boolean. returns true if next_char is newline character"""
        if char == "\n":
            return True
        return False

    def is_done(self):
        """will cause a StopIteration to occur"""
        if self.current_index >= len(self.source_file):
            return True
        return False
   
    def open_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()

    def print_string(self):
        print self.source_file

    def __repr__(self):
        return """line number: %s, index: %s, character: %s
        """ % (self.current_line, self.current_index, self.current_token)


if __name__ == "__main__":
    s = Tokenizer()
    s.print_string()
    #iter(s)
    #print next(s)
    for char in s:
        print char
