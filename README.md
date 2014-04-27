A Pascal Compiler written in Python

### Todo

    1. have tokenzier return tk_value alongside current_line, current_line_number for debug purposes
    2. change tokenizer name to something that better describes it's functionality, say, file_parser?
    3. clean up constants.py and most likely change name to soemthing htat better describes its 
    functionality as it isn't a list of constants.

### File dependency list

Scanner/
    Tokenizer
    TokenCreator

Tokenizer/
    constants 
    character

Character/
    constants

