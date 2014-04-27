import unittest
from ..modules.scanner import Scanner


default_source = 'pascal_sample_code/addition.ps'

class TestCase(unittest.TestCase):
    
    def setUp(self):
        path = '/Users/brian/projects/pascal_compiler/pascal_sample_code/addition.ps'

        with open(path, 'r') as f:
            self.source_file = f.read()

        self.scanner = Scanner(self.source_file)

    def tearDown(self):
        pass

    def test_assignment_operator(self):
        pass
    
    def test_addition_operator(self):
        pass

    def test_subtraction_operator(self):
        pass

    def test_multiplication_operator(self):
        pass

    def test_division_operator(self):
        pass

    def test_equal_operator(self):
        pass

    def test_unequal_operator(self):
        pass

    def test_less_than_operator(self):
        pass
    
    def test_greater_than_operator(self):
        pass

    def test_less_than_or_equal_to_operator(self):
        pass

    def test_greater_than_or_equal_to_operator(self):
        pass

    def test_identifier(self):
        pass

    def test_string_literal(self):
        pass

    def test_integer_literal(self):
        pass

    def test_real_literal(self):
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
        pass

    def test_reserved_word_var(self):
        pass

    def test_reserved_word_else(self):
        pass

    def test_reserved_word_begin(self):
        pass

    def test_reserved_word_end(self):
        pass

    def test_reserved_word_while(self):
        pass



