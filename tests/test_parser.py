import unittest
import mock
from modules.parser import Parser
from modules.pascal_token import Token

# STUBS => State Verification.
# MOCKS => Behavior Verification.
""" Some Grammar
    G -> E X

    E -> T E^1

    E^1 -> E | + T + E^1 | - T - E^1

    T -> F T^1

    T^1 -> E | x FxT^1 | / F - T^1
    
    F -> Lit

"""


class ParserTest(unittest.TestCase):

    def setUp(self):
        """set up the parser and a whole bunch of mock tokens
        to be run by the parser"""
        self.parser = Parser()
        pass

    def tearDown(self):
        pass

    def test_expression(self):
        pass

    def test_program_token(self):
        pass

    def test_var_token(self):
        pass

    def test_identifier_token(self):
        pass

    def test_begin_token(self):
        pass

    def test_assignment_token(self):
        pass

    def test_integer_literal_token(self):
        pass

    def test_end_token(self):
        pass
