A Pascal LL(1) Compiler written in Python

#### gist

1. Compiler initializes all the necessary components(scanner, parser, runtime)
2. Scanner reads input file as character array & does all the dirty text parsing work and returns a list of tokens. (lexical analysis)
3. Parser parses series of input tokens. since this is a LL(1) compiler, it generates intermediate code same time tokens are being parsed (syntax analysis)
4. Intermediate code is fed to the virtual runtime where instructions are interpreted and executed in python via stack machine. should probably
change the name of StackMachine class since it isn't a stack machine but a stack machine code generator. the v_runtime is the actual stack machine.

#### how to run 
1.

```
git clone git@github.com:brianwu02/pascal.py.git
```

2. python runPascalCompiler.py *optional-filename*.
3. as of now, no control structure instructions are implemented, only assignment and expressions using + - * /.

#### Problems with this compiler:

1. the scanner & character scanner aren't properly tested. They've only been
print statement tested. So far works with fairly simple code.

this parses correcty...

```
program addNumbers;

Var a,b : Integer;
Var c: Integer;

begin
    a := 1 + 1;
    if (a > 0) then
        writeln(a)
    else
        b := a + 1;
        c := a + b;
end.
```

but this doesn't..  grammar doesn't have those begin/ends. dunno if grammar is wrong.


```
program addNumbers;

Var a,b : Integer;
Var c: Integer;

begin
    a := 1 + 1;
    if (a > 0) then
        writeln(a)
    else
        begin
            b := a + 1;
            c := a + b;
    end;
end.
```

both of them are correctly compiled by fpc.

### Todo

    1. DONE. have tokenzier return tk_value alongside current_line, current_line_number for debug purposes

    2. DONE. change tokenizer name to something that better describes it's functionality, say, file_parser?

    3. ehh. clean up constants.py and most likely change name to soemthing htat better describes its 
    functionality as it isn't a list of constants 

    4. DONE. write tests that ensure token object has all correct correspoding attributes 

    5. DONE. get machine instruction generation working for simple expression.
    
    6. if statements, while statements.

```
x := 1 + 2;
``` 

should generate

```
op_pushi, 1
op_pushi, 2
op_add
op_pop, 0
op_halt
```

### File dependency list

too lazy, just look at files.

Scanner/
    CharacterScanner
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

List of Tokens
RESERVERED_WORDS:

IDENTIFIERS:

OPERATORS:
    arithmetic: + - * / Div Mod
    logical: not and or xor shl shr << >>
    boolean: not and or xor
    string: 
    set: 
        + : Union
        - : Difference
        >< : Symmetric Difference
        <= : contains
        include : include an element in the set
        exclude : exclude an element from the set
        in: check whether an element is in the set
    relational:
        = : equal
        <> : Not Equal
        < : strictly less than
        > : strictly greater than
        <= : less than or equal
        >= : greater than or equal
        in : Element of

    class:

seperators: white_space, new_line
constants: float, integer, literal


Literals:
    Integer (TK_INTLIT, value)
    Real (TK_REALLIT, index -> real table)
    Chars (TK_INTLIB | TK_CHARLIT, index -> string table)
    Strings (TK_STRLIT, index -> string table)

Keywords (individual type, --)
Identifiers (TK_ID, --, curname)
EOL? EOF? (TK_EOF, --)

TOKEN:
    int curtoken;
    int curtokenvalue;
    string curname;
    curfile;
    curline;
    curcol;

(TK_ID, --, curvalue) where -- is TK_A_VAR, index -> symtable

use LL parser style.



