from token import Token

# probably does not need to be a class could simply be a module
# recieves a token string and attempts to parse the token string
# and return a token object

class TokenCreator:

    # design patterns say I should require my dependencies in the constructor
    # but I need to return a new token object each time the create function 
    # is called so what do I do?! Probably didnt need a class for this...
    
    def __init__(self):
        pass

    def create(self, token_string):
        """method called by the scanner. takes a tokenizer string value
        as input and returns a token object."""
        token = Token()


