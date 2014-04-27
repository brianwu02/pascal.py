from constants import SYMBOLS
from constants import DOUBLE_SYMBOLS
from character import Character
from token import Token 
import pprint

pp = pprint.PrettyPrinter(indent=1)

class Tokenizer:
    """Everytime Tokenizer is called, it should return the next token.
    This class is written as an iterator. Each time the __next() function
    is called, most likely by a for loop, it should return the next token.
    Justification: Even though this is should be a one pass compiler, we may
    need to pause execution of the tokenizer. Writing tokenizer as an iterator
    will prevent us from writing complicated for loop logic. """

    def __init__(self, source_file):
        """
        self.source_file: holds the source file as a String
        self.current_index: current index of source_file
        self.current_line: current line
        self.token_list: holds list of all the tokens
        """
        #self.source_file = self.open_file('sample.ps')
        #self.source_file = source_file
        self.current_token = ''
        self.char = Character(source_file)
        self.list_of_words = []
        self.state = None

    def __iter__(self):
        return self
    
    def next(self):
        c = self.char 
        word = ''
        #file_name = ''
        line_number = ''
        line_index = ''
        #starting_indx = ''

        while True:
            #print("---%s") % (c)

            if c.is_done():
                #self.print_is_done()
                raise StopIteration

            if c.is_current_whitespace():
                self.handle_whitespace(c)
                continue

            if c.is_current_newline():
                self.handle_newline(c)
                continue

            if c.is_current_alpha():
                word = self.handle_word(c)
                break

            if c.is_current_num():
                number = self.handle_number(c)
                word = number
                break

            if c.is_current_quote():
                quote = self.handle_quote(c)
                word = quote
                break

            if c.is_current_symbol():
                symbol = self.handle_symbol(c)
                word = symbol
                break
            
            else:
                # if this happens, it means that a case is not being handled.
                msg = "while parsing"
                self.handle_exception(c, word, msg)
             
        # used for Exception catching
        self.list_of_words.append(word)

        # pass word to token object that will return a new token object
        #token = Token(token)

        return word
        #return token 

    def handle_newline(self, c):
        #print(" handle_newline state ")
        self.state = "handle_newline"
        c.increment_index()
        return 

    def handle_whitespace(self, c):
        #print(" handle_whitespace state ")
        self.state = "handle_whitespace"
        c.increment_index()
        c.increment_line_index()
        return 

    def handle_number(self, c):
        """As of now, this will only handle integers and not floats"""
        #print(" handle_number state ")
        self.state = "handle_number"
        number = ''

        line_number, line_index = c.get_metadata()

        while True:
            if c.is_current_num():
                number += c.get_current_char()
            elif c.is_current_period():
                self.state = "handle_number:Double"
                number += c.get_current_char()
            else:
                break
        return number, line_number, line_index

    def handle_symbol(self, c):
        #print("  handle_symbol state ")
        self.state = "handle_symbol"
        symbol = ''

        line_number, line_index = c.get_metadata()

        if c.is_current_symbol and c.is_next_symbol():
            sym = c.get_char_ahead_by(0) + c.get_char_ahead_by(1)
            if sym in DOUBLE_SYMBOLS:
                symbol += c.get_current_char()
                symbol += c.get_current_char()
            else:
                symbol += c.get_current_char()

        else:
            symbol += c.get_current_char()
        return symbol, line_number, line_index

    def handle_word(self, c):
        """current character is alphabet"""
        #print(" handle_word state ")
        self.state = "handle_word"
        line_num = c.current_line
        line_idx = ''
        starting_idx = ''
        word = ''

        line_number, line_index = c.get_metadata()

        while True:
            if c.is_current_alpha():
                word += c.get_current_char()
            else:
                break

        return word, line_number, line_index

    def handle_quote(self, c):
        """this event occurs when a ' is detected. it will continue
        retrieving characters until another ' is detected"""
        #print(" handle_quote state ")
        self.state = "handle_quote"
        quote = ''

        line_number, line_index = c.get_metadata()

        while True:
            quote += c.get_current_char()
            if c.is_current_quote():
                quote += c.get_current_char()
                break

        return quote, line_number, line_index

    def handle_exception(self, c, word, custom_msg=None):
        low = self.list_of_words
        msg = """
        Something BADDDDD has happened =(
        
        last state   : %s
        line number  : %s
        cur_line idx : %s
        index number : %s
        prev char    : ( %s ) ASCII: %s
        character    : ( %s ) ASCII: %s
        next char    : ( %s ) ASCII: %s
        current word : ( %s )
        token_list   : %s
        
        """ % (
                self.state,
                c.current_line,
                c.current_line_index,
                c.current_index,
                c.get_char_ahead_by(-1), ord(c.get_char_ahead_by(-1)),
                c.data[c.current_index], ord(c.data[c.current_index]),
                c.next_char(), ord(c.next_char()),
                word,
                self.list_of_words
                )
        if custom_msg is not None:
            msg = "%s \n%s" % (custom_msg, msg)
        pp.pprint(low)
        raise Exception(msg)

    def print_string(self):
        print self.source_file

    def print_debug_statement(self):
        low = self.list_of_words
        msg ="**** Sucessfully parsed all words ****"
        print(msg)
        pp.pprint(low)
        return 

    def __repr__(self):
        return """line number: %s, index: %s, character: %s
        """ % (self.current_line, self.current_index, self.current_token)


if __name__ == "__main__":
    def open_file(file_name):
        with open(file_name, 'r') as f:
            return f.read()

    path = 'pascal-sample-code/addition.ps'
    source_file = open_file(path)
    s = Tokenizer(source_file)
    for char in s:
        print("TOKEN: ( %s )") % (char)

