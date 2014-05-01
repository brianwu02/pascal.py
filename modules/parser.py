# Parsing: the process of syntax analysis. takes a series of
# symbols as input where the syntax is context-free and runs 
# the symbols through a grammar for verification.

class Parser:
    def __init__(self):
        self.tk_list = None
        self.current_token = None
        self.next_token = None
        self.token_index = 0

    def load_tokens(self, list_of_tokens):
        self.tk_list = list_of_tokens
        # initialize init vars
        self.current_token = self.tk_list[0]
        self.next_token = self.tk_list[1]

    def _match_token(self, tk_type):
        """matches the current token with an expected token."""
        tk = self.current_token
        if tk.get_type() == tk_type:
            _get_next_token()
        else:
            self._syntax_err(tk_type)

    def _get_next_token(self):
        self.token_index += 1

    def _syntax_err(tk_type):
        """expected token is not next token."""
        tk = self.current_token
        expected = tk_type
        actual = tk.get_type()
        pass
        
    def print_tokens(self):
        print(self.tk_list)

