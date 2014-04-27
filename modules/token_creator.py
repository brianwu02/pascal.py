from token import Token

class TokenCreator:

    # design patterns say I should require my dependencies in the constructor
    # but I need to return a new token object each time the create function 
    # is called so what do I do?! Probably didnt need a class for this...
    
    def __init__(self):
        self.current_token = None
        self.previous_token = None
        self.next_token = None
        pass

    def create(self, token_tuple):
        """method called by the scanner. takes a tokenizer string value
        as input and returns a token object."""
        token = Token()

        self._parse_token(token_tuple)

        return token

    def _parse_token(self):
        pass


