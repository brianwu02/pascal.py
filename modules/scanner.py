class Scanner():
    """
    Should be able to be called recursively
    Scanner should tokenize 
    """
    def __init__(self, src_file):
        """
        cur_index: keeps track of current position in file array
        last_index: keeps track of last element in the array
        """
        self.current_index = 0
        self.last_index = len(src_file)
        self.current_line = 1
        self.current_column = 0

        self.src_file = src_file
        pass
    
    def get_next_token(self):
        """returns the next token"""
        pass

    def load_src(self, src_file):
        return src_file

    def print_ascii(self):
        print [ord(char) for char in self.src_file]

    def print_enum(self):
        for idx, data in enumerate(self.src_file):
            print("%s %s %s") % (idx, data, ord(data))
        print("length is %s") % (len(self.src_file))

    def print_src(self):
        for c in self.src_file:
            print('%s %s') % (c, ord(c))
