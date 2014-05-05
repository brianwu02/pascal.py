import unittest
from ..modules.token_creator import TokenCreator
from ..modules.pascal_token import Token 

class TestTokenAttributes(unittest.TestCase):
    """test that attribute methods return correct boolean values"""

    def setUp(self):
        self.tokenCreator = TokenCreator()
        
        # paramters to create tokens.
        tk_add_tuple = ('+', 0, 0, 'handle_symbol')
        tk_sub_tuple = ('-', 0, 0, 'handle_symbol')
        tk_mult_tuple = ('*', 0, 0, 'handle_symbol')
        tk_division_tuple = ('+', 0, 0, 'handle_symbol')
        #tk_div = ('+', 0, 0, 'handle_symbol')
        #tk_mod = ('+', 0, 0, 'handle_symbol')
        #tk_and = ('+', 0, 0, 'handle_symbol')

        self.tk_add = self.tokenCreator.create(tk_add_tuple)
        self.tk_sub = self.tokenCreator.create(tk_sub_tuple)
        self.tk_mult = self.tokenCreator.create(tk_mult_tuple)
        self.tk_div = self.tokenCreator.create(tk_division_tuple)
        #self.tk_add = self.tokenCreator.create(tk_add_tuple)
        
    def tearDown(self):
        pass

    def test_tk_add_is_unary(self):
        pass

    def test_tk_add_is_mult(self):
        pass

    def test_tk_add_is_add(self):
        pass

    def test_tk_add_is_relation(self):
        pass

    def test_tk_sub_is_unary(self):
        pass
    
    def test_tk_sub_is_mult(self):
        pass

    def test_tk_sub_is_add(self):
        pass

    def test_tk_sub_is_relation(self):
        pass

    def test_tk_mult_is_unary(self):
        pass

    def test_tk_mult_is_mult(self):
        pass

    def test_tk_mult_is_add(self):
        pass

    def test_tk_div_is_relation(self):
        pass

    def test_tk_div_is_unary(self):
        pass

    def test_tk_div_is_mult(self):
        pass

    def test_tk_div_is_add(self):
        pass

    def test_tk_div_is_relation(self):
        pass
