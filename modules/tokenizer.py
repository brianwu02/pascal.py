from constants import SYMBOLS
from character import Character
from token import Token
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
        self.token_list = []
        self.current_token = ''
        self.char = Character()

    def __iter__(self):
        return self

    
    def next(self):
        c = self.char
        token = ''
        while True:
            print("---current char: %s") % (c)

            if c.is_current_whitespace():
                c.increment_index()
                continue

            if c.is_current_newline():
                c.increment_index()
                continue

            if c.is_current_alpha():
                word = self.handle_word(c)
                token = word
                break

            if c.is_current_quote():
                quote = self.handle_quote(c)
                token = quote
                break

            if c.is_current_symbol():
                symbol = self.handle_symbol(c)
                token = symbol 
                break

        return token

    def handle_symbol(self, c):
        symbol = ''
        while True:
            if c.is_current_symbol():
                symbol += c.get_current_char()
                break
        return symbol

    def handle_word(self, c):
        """current character is alphabet"""
        word = ''
        while True:
            if c.is_current_alpha():
                word += c.get_current_char()
            else:
                break
        print("In handle_world state")
        return word

    def handle_quote(self, c):
        quote = ''
        while True:
            quote += c.get_current_char()
            if c.is_current_quote():
                quote += c.get_current_char()
                break
        return word



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

    """
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
    """


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
    #s.print_string()
    #iter(s)
    #print next(s)
    for char in s:
        print char
