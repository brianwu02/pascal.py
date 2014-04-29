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

    def create(self, tk_tuple):
        """method called by the scanner. takes a tokenizer string value
        as input and returns a token object."""
        token = self._parse_and_return_token(tk_tuple)
        return token

    def _parse_and_return_token(self, tk_tuple):
        
        # make init values none
        tk_val = None
        tk_type = None
        line_number = None
        line_index = None
        creation_state = None
        name = None

        tk_val = tk_tuple[0]
        tk_type = self._determine_type(tk_tuple[0])
        line_number = tk_tuple[1]
        line_index = tk_tuple[2]
        creation_state = tk_tuple[3]
        name = self._determine_name(tk_tuple[0])

        token = Token(
                tk_val = tk_val,
                tk_type = tk_type,
                line_num = line_number, 
                line_index = line_index,
                state = creation_state,
                name = name
                )

        return token

    def _determine_type(self, value):
        return value

    def _determine_name(self, value):
        return value

