A Pascal Compiler written in Python


### Todo

    1. DONE. have tokenzier return tk_value alongside current_line, current_line_number for debug purposes

    2. change tokenizer name to something that better describes it's functionality, say, file_parser?

    3. clean up constants.py and most likely change name to soemthing htat better describes its 
    functionality as it isn't a list of constants 

    4. write tests that ensure token object has all correct correspoding attributes 

### File dependency list

Scanner/
    Tokenizer
    TokenCreator

Tokenizer/
    constants 
    character

Character/
    constants


token: 
what is a token?
what does a token do? 
what is a token used for?


design questions?

should a token object know what to do with attributes once they are initialized?
i.e token = Token(attr1, attr2, attr3), should the object itself determine how
to parse the values or have some other piece figure out what to do with inputs 
and then input it?


