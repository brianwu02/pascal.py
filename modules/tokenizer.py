from constants import SYMBOLS
from constants import DOUBLE_SYMBOLS
from character import Character
from token import Token 
import pprint

pp = pprint.PrettyPrinter(indent=4)

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
        self.list_of_words = []

    def __iter__(self):
        return self
    
    def next(self):
        c = self.char
        word = ''
        while True:
            print("---%s") % (c)

            if c.is_done():
                self.print_is_done()
                raise StopIteration

            if c.is_current_whitespace():
                self.handle_whitespace(c)
                continue

            if c.is_current_newline():
                self.handle_newline(c)
                continue

            if c.is_current_alpha():
                word += self.handle_word(c)
                break

            if c.is_current_num():
                number = self.handle_number(c)
                word += number
                break

            if c.is_current_quote():
                quote = self.handle_quote(c)
                word += quote
                break

            if c.is_current_symbol() and not c.is_next_symbol():
                # if it is a single symbol.
                symbol = self.handle_symbol(c)
                word += symbol
                break

            if c.is_current_symbol() and c.is_next_symbol():
                # 2 symbols in a row detected. check that there isn't another symbol ahead.
                # check if the character 2 places ahead of index is a symbol.
                if not c.ahead_by_is_symbol(2):
                    symbol = self.handle_double_symbol(c)
                else:
                    msg = "\nthree symbols in a row or more detected\n"
                    self.handle_exception(c, word, msg)
                word += symbol
                break

            else:
                # if this happens, it means that a case is not being handled.
                self.handle_exception(c, word)
                
        # used for Exception catching
        self.list_of_words.append(word)

        # pass word to token object that will return a new token object
        # token = Token(token)
    
        return word
        #return token  

    def handle_newline(self, c):
        print(" handle_newline state ")
        c.increment_index()
        return 

    def handle_whitespace(self, c):
        print(" handle_whitespace state ")
        c.increment_index()
        return 

    def handle_number(self, c):
        """As of now, this will only handle integers and not floats"""
        print(" handle_number state ")
        number = ''
        while True:
            if c.is_current_num():
                number += c.get_current_char()
            else:
                break
        return number

    def handle_symbol(self, c):
        print("  handle_symbol state ")
        symbol = ''
        while True:
            if c.is_current_symbol():
                symbol += c.get_current_char()
            else:
                break
        return symbol 

    def handle_double_symbol(self, c):
        """this needs to be cleaned up"""
        print (" handle_double_symbol state ")
        symbol = ''
        while True:
            if c.is_current_symbol() and c.is_next_symbol():
                sym1 = c.get_char_ahead_by(0)
                sym2 = c.get_char_ahead_by(1)
                sym = sym1 + sym2
                if sym not in DOUBLE_SYMBOLS:
                    # parse as a single symbol
                    symbol += c.get_current_char()
                    break
                else:
                    symbol += c.get_current_char()
                    symbol += c.get_current_char()
                    
                    if symbol not in DOUBLE_SYMBOLS:
                        msg = "double symbol detected is not in DOUBLE_SYMBOL list"
                        self.handle_exception(c, symbol, msg)
                    break
        return symbol 


    def handle_word(self, c):
        """current character is alphabet"""
        print(" handle_word state ")
        word = ''
        while True:
            if c.is_current_alpha():
                word += c.get_current_char()
            else:
                break
        return word

    def handle_quote(self, c):
        """this event occurs when a ' is detected. it will continue
        retrieving characters until another ' is detected"""
        print(" handle_quote state ")
        quote = ''
        while True:
            quote += c.get_current_char()
            if c.is_current_quote():
                quote += c.get_current_char()
                break
        return quote

    def handle_exception(self, c, word, custom_msg=None):
        line = c.current_line
        index = c.current_index
        char = c.data[index]
        low = self.list_of_words
        msg = """
        Error! something bad has happened while trying to parse a char.
        line number : %s
        index number : %s
        character : ( %s ) ASCII: %s
        current_word : ( %s )
        """ % (line, index, char, ord(char), word)
        if custom_msg is not None:
            msg = custom_msg + msg
        pp.pprint(low)
        raise Exception(msg)

    def open_file(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()

    def print_string(self):
        print self.source_file

    def print_is_done(self):
        low = self.list_of_words
        msg ="**** Sucessfully parsed all words %s ****"
        print(msg)
        pp.pprint(low)
        return 



    def __repr__(self):
        return """line number: %s, index: %s, character: %s
        """ % (self.current_line, self.current_index, self.current_token)


if __name__ == "__main__":
    s = Tokenizer()
    #s.print_string()
    #iter(s)
    #print next(s)
    for char in s:
        print("TOKEN: ( %s )") % (char)

