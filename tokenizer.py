from constants import SYMBOLS, RESERVED_WORDS

class Tokenizer:
    """Everytime Tokenizer is called, it should return the next token"""

    def __init__(self):
        self.source_file = self.open_file('sample.ps')
        self.current_index = 0
        self.current_line = 1
        self.times_called_next = 0

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
            next_char = self.get_next_character()


    def is_operator(self, character):
        """returns T/F whether or not character is an operator"""
        pass

    def is_reserved_word(self, token):
        """returns boolean for input token"""
        pass

    def is_identifier(self, token):
        """returns boolean for input token"""
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
        print self.file


if __name__ == "__main__":
    s = StringIter()
    s.print_string()
