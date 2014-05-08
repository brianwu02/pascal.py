from collections import deque
from debugger import DebugPrinter
# Parsing: the process of syntax analysis. takes a series of symbols as input 
# where the syntax is context-free and runs the symbols through a grammar for
# verification.
# 
# Bar |: you must have one of the two items it seperates
#  { } : having zero or more items
#  [ ] : optional, zero or one item.

class Parser:
    def __init__(self):
        self.debugger = DebugPrinter()
        self.tk_list = None
        self.token_index = 1
        self.token_list_length = None
        self.current_token = None
        self.next_token = None
        # debug stuff
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
        while self._current_tk_type() == 'TK_COMMA':
            self._match('TK_COMMA')
            self._match('TK_IDENTIFIER')

    def _parse_block(self):
        """ Block --> [Declarations] StatementSequence """
        self.parse_state = 'block'
        # only variable declarations are currently implemented so this works.
        if self._current_tk_type() == 'TK_VAR':
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
        self._match('TK_VAR')
        self._parse_variable_decl()
        self._match('TK_SEMICOLON')
        while self._current_tk_type() == 'TK_VAR':
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

        while self._current_tk_type() == 'TK_SEMICOLON':
            self._match('TK_SEMICOLON')
            self._parse_statement()

        self._match('TK_END')
        
    def _parse_statement(self):
        """ Statement --> Assignment            # implemented
                        | ProcedureCall 
                        | IfStatement           # implemented
                        | CaseStatement         # partial
                        | WhileStatement        # partial
                        | RepeatStatement 
                        | ForStatement    
                        | IOStatement           # implemented
                        | MemoryStatement 
                        | StatementSequence 
                        | empty
        """
        self.state = 'parse_statement'
        if self.current_token.get_type() == 'TK_IDENTIFIER':
            self._parse_assignment()

        self._parse_io_statement()

    def _parse_if_statement(self):
        """ IfStatement --> yif Expression ythen Statement [yelse Statement] """
        pass

    def _parse_case_statement(self):
        """ CaseStatement --> ycase Expression yof Case {';' Case} yend """
        pass

    def _parse_while_statement(self):
        """ WhileStatement --> ywhile Expression ydo Statement """
        pass
    
    def _parse_assignment(self):
        """ Assignment --> Designator ':=' Expression """
        self.state = 'parse_assignment'
        self._parse_designator()
        self._match('TK_ASSIGNMENT')
        self._parse_expression()

    def _parse_designator(self):
        """ Designator --> yident [DesignatorStuff] """
        self.state = 'parse_designator'
        self._match('TK_IDENTIFIER')
        if self._current_tk_type() == 'TK_PERIOD':
            self._parse_designator_stuff()

    def _parse_expression(self):
        """ Expression --> SimpleExpression [ Relation SimpleExpression ] """
        self.state = 'parse_expression'
        self._parse_simple_expression()

        if self.current_token.is_relation_operator():
            self._parse_simple_expression()

    def _parse_simple_expression(self):
        """ SimpleExpression --> [UnaryOperator] Term {AddOperator Term} """
        self.state = 'parse_simple_exression'
        if self.current_token.is_unary_operator():
            self._parse_unary_operator()
        self._parse_term()
        
        while self.current_token.is_add_operator():
            if self._current_tk_type() == 'TK_ADDITION':
                self._match('TK_ADDITION')
            if self._current_tk_type() == 'TK_SUBTRACTION':
                self._match('TK_SUBTRACTION')
            if self._current_tk_type() == 'TK_OR':
                self._match('TK_OR')
            self._parse_term()

    def _parse_unary_operator(self):
        """ UnaryOperator --> '+' | '-' """
        self.state = 'parse_unary_operator'
        if self._current_tk_type() == 'TK_ADDITION':
            self._match('TK_ADDITION')
        if self._current_tk_type() == 'TK_SUBTRACTION':
            self._match('TK_SUBTRACTION')

    def _parse_term(self):
        """ Term --> Factor {MultOperator Factor} """
        self.state = 'parse_term'
        self._parse_factor()

        while self.current_token.is_mult_operator():
            self._parse_mult_operator()
            self._parse_factor()

    def _parse_mult_operator(self):
        """ MultOperator --> '*' | '/' | div | mod | and """
        self.state = 'parse_mult_operator'
        tk_type = self._current_tk_type()
        if tk_type == 'TK_MULTIPLICATION':
            self._match('TK_MULTIPLICATION')
        elif tk_type == 'TK_DIVISION':
            self._match('TK_DIVISION')
        elif tk_type == 'TK_DIV':   # not implemented.
            self._match('TK_DIV')

    def _parse_factor(self):
        """
        Factor --> ynumber 
        | ystring | ytrue | yfalse | ynil 
        | Designator 
        | '(' Expression ')' 
        | ynot Factor 
        | Setvalue      # not implemented
        | FunctionCall  # not implemented
        """
        self.state = 'parse_factor'

        if self._current_tk_type() == 'TK_INT_LITERAL':
            self._match('TK_INT_LITERAL')
        elif self._current_tk_type() == 'TK_STRING_LITERAL':
            self._match('TK_STRING_LITERAL')
        elif self._current_tk_type()  == 'TK_TRUE':
            self._match('TK_TRUE')
        elif self._current_tk_type() == 'TK_NIL':
            self._match('TK_NIL')
        elif self._current_tk_type() == 'TK_L_PAREN':
            self._match('TK_L_PAREN')
            self._parse_expression()
            self._match('TK_R_PAREN')
        elif self._current_tk_type() == 'TK_NOT':
            self._match('TK_NOT')
            self._parse_factor()
        elif self._current_tk_type() == 'TK_IDENTIFIER':
            self._parse_designator()
        else:
            raise Exception('no matches in _parse_factor')

    def _parse_io_statement(self):
        """ IOStatement --> yread '(' DesignatorList ')' 
                        | yreadln [ '(' DesignatorList ')' ] 
                        | ywrite '(' ExpList ')' 
                        | ywriteln [ '(' ExpList ')' ]
        """
        self.state = 'parse_io_statement'

        if self._current_tk_type() == 'TK_READ':
            self._match('TK_L_PAREN')
            self._parse_designator_list()   # not implemented
            self._match('TK_R_PAREN')
        elif self._current_tk_type() == 'TK_READLN':
            self._match('TK_READLN')
            # incomplete.
        elif self._current_tk_type() == 'TK_WRITELN':
            self._match('TK_WRITELN')
            if self._current_tk_type() == 'TK_L_PAREN':
                self._match('TK_L_PAREN')
                self._parse_exp_list()
                self._match('TK_R_PAREN')
    
    def _parse_exp_list(self):
        """ExpList --> Expression { ',' Expression }"""
        self._parse_expression()
        
        while self._current_tk_type() == 'TK_COLON':
            self._match('TK_COLON')
            self._parse_expression()

    def load_tokens(self, list_of_tokens):
        self.tk_list = deque(list_of_tokens)
        self.current_token = self.tk_list.popleft()
        self.token_list_length = len(self.tk_list) + 1

    def _current_tk_type(self):
        return self.current_token.get_type()

    def _get_next_token(self):
        try:
            self.current_token = self.tk_list.popleft()
            self.token_index += 1
        except IndexError:
            print("all tokens popped. finished loading all tokens.")

    def _match(self, expected_tk_type):
        """matches the current token with an expected token."""
        #tk = self.tk_list[self.token_index]
        debugger = self.debugger
        current_token = self.current_token
        # update the global state of expected token type & val

        if (expected_tk_type == current_token.get_type()):
            # pass token to debuggger and print debug statement
            debugger.print_debug(
                    current_token,
                    self.token_index,
                    self.token_list_length
                    )
        else:
            debugger.raise_match_tk_err(
                    current_token, 
                    self.token_index,
                    self.token_list_length,
                    expected_tk_type,
                    current_token.get_type()
                    )
        self._get_next_token()

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




