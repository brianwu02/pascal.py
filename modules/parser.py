# Parsing: the process of syntax analysis. takes a series of
# symbols as input where the syntax is context-free and runs 
# the symbols through a grammar for verification.

class Parser:
    def __init__(self):
        self.tk_list = None
        self.current_token = None
        self.next_token = None
        self.token_index = 0
        self.stack = []

    def _E():
        """
        E -> T E
        """
        self._T()
        self._E1()

        pass

    def _E1():
        """
        E1 -> empty | tk_plus T tk_plus E1 | tk_minus T tk_minus E1
        """
        self._match('TK_PLUS')
        self._T();
        self.E1();
        pass

    def _T():
        """
        T -> F T1
        """
        pass

    def _T1():
        """
        T1 -> empty | tk_mult F tk_mult T1 | tk_div F tk_div T1
        """
        pass

    def _F():
        """
        F -> literal(down_arrow) | ident(down_arrow) | tk_minus F | tk_plus F | not F | '(' F ')
        
        """
        pass



    def load_tokens(self, list_of_tokens):
        self.tk_list = list_of_tokens
        # initialize init vars
        self.current_token = self.tk_list[0]
        self.next_token = self.tk_list[1]

    def _match(self, tk_type):
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
        
        msg = "expected tk_type: %s but got %s instead." % (
                expected,
                actual
                )
        raise Exception(msg)

    def push(self, obj):
        """sugar"""
        self.stack.append(obj)

    def print_tokens(self):
        print(self.tk_list)

