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
            


