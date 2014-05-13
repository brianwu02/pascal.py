# identifier name, value of tk_identifier
# the information associated with a name

# name -> variable and labels, parameter, constant, record, recordfield, procedure, array & file



class SymbolTable:
    def __init__(self):
        # {'ident_name' => {
        #    'token' => token # just save the entire token for now.
        #    'type'
        #   }
        self.table = {}

    def parse_variable_declaration(self, symbol_array):
        """pretty hacky. sends over a list of tokens where (first, last-1) are
        identifiers and last is type."""
        # loop over all variable identifers and add to identifiers list.
        identifiers = []
        ident_type = None
        type_index = len(symbol_array) - 1
        for index, token in enumerate(symbol_array):
            if index == type_index:
                # the way it's coded, the last element in array MUST be the type or something breaks.
                ident_type = token.get_value()
            else:
                identifiers.append(token)

        # loop over identifiers and add them to the symbol table
        for ident in identifiers:
            self.table[ident] = {'type': ident_type }



    def add(self, token):
        """adds identifier to symbol table"""
        ident_name = token.get_value()
        token_type = token.get_type()

        if token_type != 'TK_IDENTIFIER':
            raise Exception('SymbolTable got wrong TokenType')

        if self.table.has_key(ident_name):
            raise Exception('ident with name already exists.')
        
        # add entire token to symboltable
        self.table[ident_name] = token
        
    def lookup_(self, ident_name):
        """returns value of identifier"""
        pass

    def update(self):
        pass

    def print_table(self):
        for key, value in self.table.iteritems():
            print (key, value)
            


