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
            print("---%s") % (c)

            if c.is_done():
                raise StopIteration

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

            if c.is_current_num():
                number = self.handle_number(c)
                token = number
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

    def handle_number(self, c):
        """As of now, this will only handle integers and not floats"""
        number = ''
        while True:
            if c.is_current_num():
                number += c.get_current_char()
            else:
                break
        return number

    def handle_symbol(self, c):
        symbol = ''
        while True:
            if c.is_current_symbol():
                symbol += c.get_current_char()
            else:
                break
        return symbol 

    def handle_double_symbol(self, c):
        """this needs to be cleaned up"""
        symbol = ''
        while True:
            if c.is_current_symbol() and c.is_next_symbol():
                symbol += c.get_current_char()
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
        print("---In handle_world state---")
        return word

    def handle_quote(self, c):
        """this event occurs when a ' is detected. it will continue
        retrieving characters until another ' is detected"""
        quote = ''
        while True:
            quote += c.get_current_char()
            if c.is_current_quote():
                quote += c.get_current_char()
                break
        return quote

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

