import unittest
from ..modules.token_creator import TokenCreator
from ..modules.token import Token

default_source = 'pascal_sample_code/addition.ps'

class TestCase(unittest.TestCase):
    """the purpose of these tests are to validate the TokenCreator
    correctly returns token objects with the correct attributes
    given stubbed token parameters."""
    
    def setUp(self):
        path = '/Users/brian/projects/pascal_compiler/pascal_sample_code/addition.ps'

        with open(path, 'r') as f:
            self.source_file = f.read()

        self.tokenCreator = TokenCreator()

    def tearDown(self):
        pass

    def test_assignment_operator(self):
        # values to test against.
        tk_val = ':='
        line_number = 8
        line_index = 6
        state = 'handle_symbol'
        tk_type = 'operator'
        tk_name = 'assignment'

        tk_tuple = (':=', 8, 6, 'handle_symbol')
        token = self.tokenCreator.create(tk_tuple)

        # make sure returned value is a token.
        self.assertIsInstance(token, Token)

        # add test to evaluate attributes of evaluted of token.
        self.assertEqual(tk_val, token.get_value())
        self.assertEqual(line_number, token.get_line_number())
        self.assertEqual(line_index, token.get_line_index())
        self.assertEqual(state, token.get_creation_state())
        self.assertEqual(tk_type, token.get_tk_type())
        self.assertEqual(tk_name, token.get_name())
    
    def test_addition_operator(self):
        op = '+'
        tk_tuple = ('+', 8, 11, 'handle_symbol')
        line_number = 8
        line_index = 8
        state = 'handle_symbol'
        tk_type = 'operator'
        tk_name = 'addition'
        

        token = self.tokenCreator.create(tk_tuple)
        self.assertIsInstance(token, Token)

        self.assertEqual(op, token.get_value())
        self.assertEqual(line_number, token.get_line_number())
        self.assertEqual(line_index, token.get_line_index())
        self.assertEqual(state, token.get_creation_state())


    def test_subtraction_operator(self):
        op = '-'
        tk_tuple = ('-', 0, 0, 'handle_symbol')
        line_number = 0
        line_index = 0
        state = 'handle_symbol'
        tk_type = 'operator'
        tk_name = 'subtraction'

    def test_reserved_word_program(self):
        op = 'program'
        tk_tuple = ('program', 1, 0, 'handle_word')
        line_number = 1
        line_index = 0
        state = 'handle_word'
        tk_type = 'reserved'
        tk_name 'program'



    def test_multiplication_operator(self):
        op = '*'
        pass

    def test_division_operator(self):
        op = '/'
        pass

    def test_equal_operator(self):
        op = '='
        pass

    def test_unequal_operator(self):
        op = '<>'
        pass

    def test_less_than_operator(self):
        op = '<'
        pass
    
    def test_greater_than_operator(self):
        op = '>'
        pass

    def test_less_than_or_equal_to_operator(self):
        op = '<='
        pass

    def test_greater_than_or_equal_to_operator(self):
        op = '>='
        pass

    def test_identifier(self):
        op = 'a'
        pass

    def test_string_literal(self):
        op = "'some string val'"
        pass

    def test_integer_literal(self):
        op = '5' # they are still represented as strings in python
        tk_tuple = ('5', 7, 9, 'handle_number')
        pass

    def test_real_literal(self):
        op = '5.0'
        pass

    def test_keyword(self):
        pass

    def test_EOF(self):
        pass

    def test_comment_string(self):
        pass

    def test_reserved_word_if(self):
        """test that scanner returns a correct token object given
        a reserverd_word tuple."""
        rword = 'if'
        pass

    def test_reserved_word_var(self):
        rword = 'var'
        pass

    def test_reserved_word_else(self):
        rword = 'else'
        pass

    def test_reserved_word_begin(self):
        rword = 'begin'
        pass

    def test_reserved_word_end(self):
        rword = 'end'
        pass

    def test_reserved_word_while(self):
        rword = 'while'
        pass



