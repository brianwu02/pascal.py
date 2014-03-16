
class Character(object):
    """Character object that is fed to the tokenizer."""

    def __init__(self, src_file):
        self.src = src_fie
        
        self.current_index = 0
        self.current_line = 1
        self.data = self.src[0]
        self.total_len = len(self.src)

    def get_next_char(self):
        """returns the next charcter and increments index count."""
        pass

    def lookahead_char(self):
        """returns the next next character. does not increment index count."""
        pass

    def _increment_index(self):
        pass

    def _increment_line(self):
        pass

    def is_char(self, char):
        pass

    def is_num(self):
        pass

    def is_identifier(self):
        pass

    def is_whitespace(self):
        pass

    def is_quote(self):
        if self.data == "\'":
            return True
        return False


    def __repr__(self):
        return ("char: %s\n ASCII: %s\n index: %s\n line: %s") % (
                self.val, self.val, self.current_index, self. current_line
                )



# debugging purpose
if __name__ == "__main__":
    src_file = None
    file_name = "sample.ps"
    with open(file_name, 'r') as f:
        src_file = f.read()

    char = Character(src_file)
    
