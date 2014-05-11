import unittest
from modules.parser import Parser

class TestExpressions(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
        token_list = []
        self.parser.load_tokens(token_list)

    def tearDown(self):
        pass
    

    def test_addition_expression(self):
        """5 + 5"""
        pass

    def test_subtraction_expression(self):
        """x := 5 - 5"""
        pass

    def test_division_expression(self):
        """x := 5 / 5"""
        pass
    
    def test_multiplication_expression(self):
        """x := 5 * 5"""
        pass
