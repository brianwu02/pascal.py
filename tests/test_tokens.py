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
        tk_division_tuple = ('/', 0, 0, 'handle_symbol')
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
        self.assertTrue(self.tk_add.is_unary_operator())

    def test_tk_add_is_mult(self):
        self.assertFalse(self.tk_add.is_mult_operator())
    
    def test_tk_add_is_add(self):
        self.assertTrue(self.tk_add.is_add_operator())

    def test_tk_add_is_relation(self):
        self.assertFalse(self.tk_add.is_relation_operator())

    def test_tk_sub_is_unary(self):
        self.assertTrue(self.tk_sub.is_unary_operator())
    
    def test_tk_sub_is_mult(self):
        self.assertFalse(self.tk_sub.is_mult_operator())

    def test_tk_sub_is_add(self):
        self.assertTrue(self.tk_sub.is_add_operator())

    def test_tk_sub_is_relation(self):
        self.assertFalse(self.tk_sub.is_relation_operator())

    def test_tk_mult_is_unary(self):
        self.assertFalse(self.tk_mult.is_unary_operator())

    def test_tk_mult_is_mult(self):
        self.assertTrue(self.tk_mult.is_mult_operator())

    def test_tk_mult_is_add(self):
        self.assertFalse(self.tk_mult.is_add_operator())

    def test_tk_mult_is_relation(self):
        self.assertFalse(self.tk_mult.is_relation_operator())

    def test_tk_div_is_unary(self):
        self.assertFalse(self.tk_div.is_unary_operator())
            
    def test_tk_div_is_mult(self):
        self.assertTrue(self.tk_div.is_mult_operator())

    def test_tk_div_is_add(self):
        self.assertFalse(self.tk_div.is_add_operator())

    def test_tk_div_is_relation(self):
        self.assertFalse(self.tk_div.is_relation_operator())
