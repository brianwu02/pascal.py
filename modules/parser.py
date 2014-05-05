from collections import deque
#from debugger import DebugPrinter
# Parsing: the process of syntax analysis. takes a series of
# symbols as input where the syntax is context-free and runs 
# the symbols through a grammar for verification.

class Parser:
    def __init__(self):
        #self.debugger = DebugPrinter()
        self.tk_list = None
        self.token_index = 1
        self.token_list_length = None
        self.current_token = None

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

        self.expected_tk_type = None
        
        self.debug_mode_on = True
        self.state = None

    def run(self):
        """ CompilationUnit --> ProgramModule """
        self.parse_state = 'run'
        self._program_module()

    def _program_module(self):
        """ ProgramModule --> yprogram yident ProgramParameters ';' Block '.' """
        self.parse_state = 'program_module'
        self._match('TK_PROGRAM')
        self._match('TK_IDENTIFIER')
        # ignoring program parameters for now, dont know what its used for.
        self._parse_program_parameters() 
        self._match('TK_SEMICOLON')
        # parse tokens betwen tk_begin and tk_end
        self._parse_block()
        self._match('TK_PERIOD')
        print("HOPEFULLY THIS STATEMENT RUNS BECAUSE IT MEANS IT WORKS!")

    def _parse_program_parameters(self):
        """ ProgramParameters --> '(' IdentList ')' """
        self.parse_state = 'program_parameters'
        if self._current_tk_type() == 'TK_L_PAREN':
            self._match('TK_L_PAREN')
            self._parse_identifier_list()
            self._match('TK_R_PAREN')

    def _parse_identifier_list(self):
        """IdentList --> yident {',' yident}"""
        self.parse_state = 'identifier_list'
        self._match('TK_IDENTIFIER')
        if self._current_tk_type() == 'TK_COMMA':
            self._match('TK_COMMA')
            self._parse_identifier_list()

    def _parse_block(self):
        """ Block --> [Declarations] StatementSequence """
        self.parse_state = 'block'
        self._parse_declarations()
        self._parse_statement_sequence()

    def _parse_declarations(self):
        """
        Declarations -> [ConstantDefBlock]  # not implemented yet.
                     |  [TypeDefBlock]      # not implemented yet.
                     |  [VariableDeclBlock] 
                     |  [SubprogDeclList]   # not implemented yet.
        """
        self.parse_state = 'declarations'
        self._parse_variable_decl_block()

    def _parse_variable_decl_block(self):
        """ VariableDeclBlock --> yvar VariableDecl ';' {VariableDecl ';'} """
        self.parse_state = 'variable_declaration_block'
        current_tk_type = self.current_token.get_type()
        self._match('TK_VAR')
        self._parse_variable_decl()
        self._match('TK_SEMICOLON')

    def _parse_variable_decl(self):
        """ VariableDecl --> IdentList ':' Type """
        self.parse_state = 'variable_declaration'
        self._parse_identifier_list()
        self._match('TK_COLON')
        self._parse_type()

    def _parse_type(self):
        """ Type    --> yident  
                    | ArrayType     # not implemented yet.
                    | PointerType   # not implemented yet.
                    | RecordType    # not implemented yet.
                    | SetType       # not implmeneted yet.
        """
        self.parse_state = 'type'
        
        self._match('TK_IDENTIFIER')
        
    def _parse_statement_sequence(self):
        """ StatementSequence --> ybegin Statement {';' Statement} yend """
        self.state = 'statement_sequence'
        self._match('TK_BEGIN')
        self._parse_statement()
        self._match('TK_SEMICOLON')
        self._match('TK_END')

    def _parse_statement(self):
        """ Statement --> Assignment            #implemented
                        | ProcedureCall 
                        | IfStatement     
                        | CaseStatement 
                        | WhileStatement  
                        | RepeatStatement 
                        | ForStatement    
                        | IOStatement 
                        | MemoryStatement 
                        | StatementSequence 
                        | empty
        """
        self._parse_assignment()

    def _parse_assignment(self):
        """ Assignment --> Designator ':=' Expression """
        self._parse_designator()
        self._match('TK_ASSIGNMENT')
        self._parse_expression()

    def _parse_designator(self):
        """ Designator --> yident [ DesignatorStuff ] """
        self._match('TK_IDENTIFIER')

    def _parse_expression(self):
        """ Expression --> SimpleExpression [ Relation SimpleExpression ] """
        self._parse_simple_expression()

    def _parse_simple_expression(self):
        """ SimpleExpression --> [UnaryOperator] Term {AddOperator Term} """
        self._parse_unary_operator()
        self._parse_term()
        
        if _current_tk_type() == 'TK_ADDITION':
            self._parse_add_operator()
            self._parse_term()

    def _parse_unary_operator(self):
        """ UnaryOperator --> '+' | '-' """
        if self._current_tk_type() == 'TK_ADDITION':
            self._match('TK_ADDITION')
        if self._current_tk_type() == 'TK_SUBTRACTION':
            self._match('TK_SUBTRACTION')
    
    def load_tokens(self, list_of_tokens):
        self.tk_list = deque(list_of_tokens)
        self.current_token = self.tk_list.popleft()
        self.token_list_length = len(self.tk_list) + 1

    def _get_next_token(self):
        self.current_token = self.tk_list.popleft()
        self.token_index += 1

    def _current_tk_type(self):
        return self.current_token.get_type()

    def _update_expected(self, exp_tk_type):
        """updates the class attributes that stores the expected
        token type and token value."""
        # ehh, good habit to do this i guess.
        self.expected_tk_type = exp_tk_type
        self.expected_tk_cnt = self.token_index

    def _update_got(self, token):
        """updates the class attribute that stores the gotten
        tokens attributes."""

        #self.current_token = self.tk_list[self.token_index]
        #token = self.current_token

        self.got_tk_cnt = self.token_index
        self.got_tk_type = token.get_type()
        self.got_tk_val = token.get_value()
        self.got_tk_line = token.get_line_number()
        self.got_tk_l_index = token.get_line_index()
        self.got_tk_name = token.get_name()
        self.got_tk_create_state = token.get_creation_state()

    def _match(self, tk_type):
        """matches the current token with an expected token."""
        #tk = self.tk_list[self.token_index]
        tk = self.current_token

        # update the global state of expected token type & val
        self._update_expected(tk_type)
        self._update_got(tk)

        expected_type = self.expected_tk_type
        got_tk_type = self.got_tk_type

        if (expected_type == got_tk_type):
            # after a successful token match,
            # 1. increment global token counter
            # 2. if debug mode is on, print all token comparisons.
            if self.debug_mode_on:
                self._display_message('debug')
        else:
            self._display_message('tk_match_err')
        
        self._get_next_token()

    def _display_message(self, msg_type):
        """builds and displays error or debug messages."""
        accepted_message_types = [
                'debug',
                'tk_match_err'
                ]
        if msg_type not in accepted_message_types:
            raise Exception("error type " + msg_type + " does not exist")

        # send this dictionary of current state to DebugPrinter
        parser_state = {
                'expected_tk_type': self.expected_tk_type,
                'total_tokens': self.token_list_length,
                'current_tk_count': self.token_index,
                'got_tk_val': self.got_tk_val,
                'got_tk_type': self.got_tk_type,
                'got_tk_cnt': self.got_tk_cnt,
                'got_tk_name': self.got_tk_name,
                'got_tk_creation_state': self.got_tk_create_state,
                'got_line': self.got_tk_line,
                'got_l_ind': self.got_tk_l_index,
                'line_info': "(%s, %s)" % (self.got_tk_line, self.got_tk_l_index),
                'parse_state': self.parse_state
                }

        #if self.debug_mode_on:
        #    self.debugger.print_debug(parser_state)

        expected_tk_type = self.expected_tk_type
        total_tokens = self.token_list_length
        current_tk_cnt = self.token_index

        got_tk_type = self.got_tk_type
        got_tk_val = self.got_tk_val
        got_tk_cnt = self.got_tk_cnt
        got_tk_name = self.got_tk_name
        got_tk_create_state = self.got_tk_create_state
        got_line = self.got_tk_line 
        got_l_ind = self.got_tk_l_index
        line_info = "(%s, %s)" % (got_line, got_l_ind)
        parse_state = self.parse_state

        debug_msg = """
        ------- token %s out of %s parsed -------
        parse_state : %s
        type        : %s
        value       : %s
        name        : %s
        line info   : %s
        """ % (
                current_tk_cnt,
                total_tokens,
                parse_state,
                got_tk_type,
                got_tk_val,
                got_tk_name,
                line_info
                )

        tk_match_err_msg = """TK_MATCH_ERR
        ---tk_match_err on token %s out of %s----
        --> expected match  : %s in parse_state: %s
        --> got type        : %s
        got value   : %s
        got name    : %s
        got line    : %s
        create state: %s
        """ % (
                current_tk_cnt,
                total_tokens,
                expected_tk_type,
                parse_state,
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
       
    def push(self, obj):
        """sugar"""
        self.stack.append(obj)

    def print_tokens(self):
        print(self.tk_list)

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




