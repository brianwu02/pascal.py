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

        # number of times a successful tk_match has occured
        self.match_success_count = 0

        # state of current token and expected parsing token
        # Current Token Attributes
        self.got_tk_type = None
        self.got_tk_val = None
        self.got_tk_cnt = None
        self.got_tk_name = None
        self.got_tk_line = None
        self.got_tk_l_index = None
        self.got_tk_create_state = None
        # Expected Token attributes
        #self.expected_tk_cnt = None
        self.expected_tk_type = None
        #self.expected_tk_val = None
        
        self.debug_mode_on = True

    def run(self):
        """
        CompilationUnit --> ProgramModule 
        """
        self._program_module()


    def _program_module(self):
        """
        ProgramModule --> yprogram yident ProgramParameters ';' Block '.' 
        """

        self._match('TK_PROGRAM')
        self._match('TK_IDENTIFIER')
        
        # tokens parsed in _parse_program_paramters
        # var a,b : Integer;
        self._parse_program_parameters() 

        self._match('TK_SEMICOLON')

        # parse tokens betwen tk_begin and tk_end
        self._parse_block()

        self._match('TK_PERIOD')

        print("HOPEFULLY THIS STATEMENT RUNS BECAUSE IT MEANS IT WORKS!")

    def _parse_program_parameters(self):
        """
        ProgramParameters --> '(' IdentList ')' 
        """
        pass

    def _parse_identifier_list(self):
        """
        IdentList --> yident {',' yident} 
        """

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

    def _get_next_token(self):
        self.token_index += 1

    def _update_expected(self, exp_tk_type):
        """updates the class attributes that stores the expected
        token type and token value."""
        # ehh, good habit to do this i guess.
        self.expected_tk_type = exp_tk_type
        self.expected_tk_cnt = self.token_index

    def _update_got(self):
        """updates the class attribute that stores the gotten
        tokens attributes."""
        token = self.tk_list[self.token_index]

        self.got_tk_cnt = self.token_index
        self.got_tk_type = token.get_type()
        self.got_tk_val = token.get_value()
        self.got_tk_line = token.get_line_number()
        self.got_tk_l_index = token.get_line_index()
        self.got_tk_name = token.get_name()

    def _match(self, tk_type):
        """matches the current token with an expected token."""
        tk = self.tk_list[self.token_index]

        # update the global state of expected token type & val
        self._update_expected(tk_type)
        self._update_got()

        expected_type = self.expected_tk_type
        got_tk_type = self.got_tk_type

        if (expected_type == got_tk_type):
            # after a successful token match,
            # 1. increment global token counter
            # 2. if debug mode is on, print all token comparisons.
            if self.debug_mode_on:
                self._display_message('debug')

            #self.match_success_count += 1
            self._get_next_token()
        else:
            self._display_message('tk_match_err')

    def _display_message(self, msg_type):
        """builds and displays error or debug messages."""
        accepted_message_types = [
                'debug',
                'tk_match_err'
                ]
        if msg_type not in accepted_message_types:
            raise Exception("error type " + msg_type + " does not exist")


        expected_tk_type = self.expected_tk_type
        total_tokens = len(self.tk_list) + 1
        current_tk_cnt = self.token_index + 1

        got_tk_type = self.got_tk_type
        got_tk_val = self.got_tk_val
        got_tk_cnt = self.got_tk_cnt
        got_tk_name = self.got_tk_name
        got_tk_create_state = self.got_tk_create_state
        got_line = self.got_tk_line 
        got_l_ind = self.got_tk_l_index
        line_info = "(%s, %s)" % (got_line, got_l_ind)

        debug_msg = """
        ------- token %s out of %s parsed -------
        type        : %s
        value       : %s
        name        : %s
        line info   : %s

        """ % (
                current_tk_cnt,
                total_tokens,
                got_tk_type,
                got_tk_val,
                got_tk_name,
                line_info
                )

        tk_match_err_msg = """TK_MATCH_ERR
        ---tk_match_err on token %s out of %s----
        --> expected type   : %s
        --> got type        : %s
        got value   : %s
        got name    : %s
        got line    : %s
        create state: %s
        """ % (
                current_tk_cnt,
                total_tokens,
                expected_tk_type,
                got_tk_type,
                got_tk_val,
                got_tk_name,
                line_info,
                got_tk_create_state
                )

        if msg_type == 'debug':
            print(debug_msg)

        if msg_type == 'tk_match_err':
            raise Exception(tk_match_err_msg)


        
    # old method, not to be used. only here for reference
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

