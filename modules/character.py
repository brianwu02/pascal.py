from constants import SYMBOLS

class Character(object):
    """Character object that is fed to the tokenizer."""

    def __init__(self):
        self.src = self.open_file()
        
        self.current_index = 0
        self.current_line = 1
        self.data = self.src

    def current_char(self):
        """returns the next charcter and increments index count."""
        c = self.data[self.current_index]
        return c

    def get_current_char(self):
        """return a tuple of (char, index, line_index)"""
        if self.is_done():
            return 'EOF'
        i = self.current_index
        l = self.current_line
        self.current_index += 1
        c = self.data[i]
        #return (c, i, l)
        return c

    def next_char(self):
        """returns the next next character. does not increment index count."""
        c = self.data[self.current_index + 1]
        return c

    def is_current_alpha(self):
        c = self.data[self.current_index]
        return c.isalpha()

    def is_next_alpha(self):
        c = self.data[self.current_index + 1]
        return c.isalpha()

    def is_current_num(self):
        try:
            float(self.data[self.current_index])
            return True
        except ValueError:
            return False

    def is_next_num(self):
        try:
            float(self.data[self.current_index + 1])
            return True
        except ValueError:
            return False

    def is_current_symbol(self):
        if self.data[self.current_index] in SYMBOLS:
            return True
        return False

    def is_next_symbol(self):
        if self.data[self.current_index+1] in SYMBOLS:
            return True
        return False

    def is_current_whitespace(self):
        if self.data[self.current_index] == " ":
            return True
        return False

    def is_next_whitespace(self):
        if self.data[self.current_index + 1] == " ":
            return True
        return False

    def is_current_newline(self):
        if self.data[self.current_index] == "\n":
            return True
        return False

    def is_next_newline(self):
        if self.data[self.current_index + 1] == "\n":
            return True
        return False

    def is_current_quote(self):
        if self.data[self.current_index] == "\'":
            return True
        return False

    def is_current_quote(self):
        if self.data[self.current_index] == "\'":
            return True
        return False

    def is_next_quote(self):
        if self.data[self.current_index + 1] == "\'":
            return True
        return False

    def is_done(self):
        if self.current_index >= len(self.src):
            return True
        return False
    
    def increment_index(self):
        self.current_index += 1
    
    def open_file(self):
        with open('sample.ps', 'r') as f:
            return f.read()

    def print_index(self):
        """debugging"""
        return self.current_index


    def __repr__(self):
        #return ("char: %s\n ASCII: %s\n index: %s\n line: %s") % (
        #        self.val, self.val, self.current_index, self. current_line
        #        )
        return "char: %s ASCII: %s" % (
                self.data[self.current_index], 
                ord(self.data[self.current_index])
                )



# debugging purpose
if __name__ == "__main__":
    src_file = None
    file_name = "sample.ps"
    with open(file_name, 'r') as f:
        src_file = f.read()

    char = Character(src_file)
    
