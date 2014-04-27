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

    def test_reserved_word_token(self):
        """test that scanner returns a correct token object given
        a reserverd_word tuple."""

        pass

