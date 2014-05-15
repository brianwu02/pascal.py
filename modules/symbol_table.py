# identifier name, value of tk_identifier
# the information associated with a name

# name -> variable and labels, parameter, constant, record, recordfield, procedure, array & file

# lookup table that determines how many bytes to allocate for an identifier.
MEM_LOOKUP = {
        'integer': 4,
        'real': 4
        }

class SymbolTable:
    def __init__(self):
        # {'ident_name' => {
        #    'token' => token # just save the entire token for now.
        #    'type'
        #   }
        self.table = {}
        self.mem_addr = 0

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
                identifiers.append(token.get_value())

        # loop over identifiers and add them to the symbol table
        for ident in identifiers:
            self.table[ident] = {
                    'type': ident_type,
                    'address': self._allocate_memory(ident_type)
                    }

        # add entire token to symboltable
        # self.table[ident_name] = token
        
    def lookup(self, ident_name):
        """returns value of identifier"""
        # let it throw KeyError if the key doesnt exist. means i messed up.
        return self.table[ident_name]

    def lookup_addr(self, ident_name):
        return self.table[ident_name]['address']

    def print_table(self):
        for key, value in self.table.iteritems():
            print (key, value)

    def _allocate_memory(self, ident_type):
        """determine how much memory should be allocated for indent."""
        alloc_size = MEM_LOOKUP[ident_type]
        memory_addr = self.mem_addr 
        self.mem_addr += alloc_size # increment address by amount offset by allocation
        return memory_addr

        


