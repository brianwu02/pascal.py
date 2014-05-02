# Parsing: the process of syntax analysis. takes a series of
# symbols as input where the syntax is context-free and runs 
# the symbols through a grammar for verification.

class Parser:
    def __init__(self):
        self.tk_list = None
        self.token_index = 0
        #self.current_token = self.tk_list[self.token_index]
        #self.next_token = self.tk_list[self.token_index + 1]
        self.current_token = None
        self.next_token = None
        self.stack = []

    
    def run(self):
        """
        CompilationUnit --> ProgramModule 
        """
        self._program_module()


    def _program_module(self):
        """
        ProgramModule --> yprogram yident ProgramParameters ';' Block '.' 
        """

        self._match("TK_PROGRAM")
        self._match("TK_IDENTIFIER")
        
        # tokens parsed in _parse_program_paramters
        # var a,b : Integer;
        self._parse_program_parameters() 

        self._match("TK_SEMICOLON")

        # parse tokens betwen tk_begin and tk_end
        self._parse_block()

        self._match('TK_PERIOD')

        print("HOPEFULLY THIS STATEMENT RUNS BECAUSE IT MEANS IT WORKS!")

    def _parse_program_parameters(self):
        """
        ProgramParameters --> '(' IdentList ')' 
        """
        pass

    def _parse_block(self):
        """
        """
        pass
        

    def _statement_sequence(self):
        """
        StatementSequence --> ybegin Statement {';' Statement} yend 
        """
        self._match("tk_begin")
        self._E()
        
        # write method to parse Statement, E() in class examples.
        self._match("tk_semicolon")

    def _assignment(self):
        """
        Assignment --> Designator ':=' Expression 
        """
        self._designator()
        self._match("tk_assignment")
        pass
    
    def _E():
        """
        E -> T E
        """
        self._T()
        self._E1()

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
        #tk = self.current_token
        tk = self.tk_list[self.token_index]
        if tk.get_type() == tk_type:
            print("matched: %s with val: %s") % (
                    tk.get_type(),
                    tk.get_value()
                    )
            self._get_next_token()
        else:
            self._token_err(tk_type)

    def _get_next_token(self):
        self.token_index += 1

    def _token_err(self, tk_type):
        """expected token is not next token."""
        tk = self.tk_list[self.token_index]
        expected = tk_type
        #actual = tk.get_type()
        
        msg = """
                expected tk_type: %s. but got the following:
                ----
                tk_type:            %s
                tk_val:             %s
                tk_name:            %s
                line number:        %s
                line index number:  %s
                creation state:     %s
                ----
        """ % (
                expected,
                tk.get_type(),
                tk.get_value(),
                tk.get_name(),
                tk.get_line_number(),
                tk.get_line_index(),
                tk.get_creation_state()
                )
        raise Exception(msg)

    def push(self, obj):
        """sugar"""
        self.stack.append(obj)

    def print_tokens(self):
        print(self.tk_list)

