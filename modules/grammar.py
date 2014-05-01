# holds all the grammar rules for pascal. this algorithm uses the 
# recursive descent where each non-terminal symbol will have it's own parser function.


def CompilationUnit(token):
    """ CompilationUnit -> ProgramModule
    """
    pass

def ProgramModule(token):
    """ ProgramModule   -> program ident ProgramParamters ';' Block '.'
    """
    pass

def block(token):
    """ Block   -> [Declarations] StatementSequence
                | [ConstantDefBlock]
                | [TypeDefBlock]
                | [VariableDeclBlock]
                | [SubProgDeclList]
    """
    pass

def ConstantDefBlock(token):
    pass

def VariableDeclBlock(token):
    """
    var -> VariableDecl ';' { VariableDecl ';' }
    """
    pass

def identifier_rule(token):
    """returns True if word is an identifier that follows this grammar:
    identifier  ->  letter
                ->  letter | digit
    """
    pass

def _letter_rule(token):
    """a letter is a terminal symbol."""
    pass

def _digit_rule(token):
    """a digit is a terminal symbol."""
    pass

def factor():
    """
    Factor  -> number
            | string | true | false | nil
            | Designator
            | '(' Expression ')'
            | not Factor
            | Setvalue
            | FunctionCall

    """
    pass


if __name__ == "__main__":
    pass
