import pprint
# list of stack machine operations
# OP_PUSH
# OP_POP
# OP_ADD
# OP_SUBTRACT
# OP_ADDI
# OP_SUBI
# OP_JMP
# OP_JTRUE
# OP_JFALSE
# OP_CALL
# OP_RETURN
# OP_LT
# OP_GT
# OP_WRITELN

# m_ip; instruction pointer
# m_dp; data pointer
# m_sp; stack pointer
# m_bp; base pointer

## INTEGER 4 BYTES

pp = pprint.PrettyPrinter(indent=1)

class StackMachine:
    def __init__(self, symbol_table):
        self.stack = []
        # for debugging etc. shows list of pushed instructions.
        self.instruction_list = []
        self.symbol_table = symbol_table
        self.instruction_number = 0

    def gen_debug(self, args):
        self._gen_instruction(args)

    def generate(self, state, op_type, op1=None, op2=None):
        print state, op_type, op1, op2
        if op_type == 'TK_ADDITION':
            if op1 == "TK_REAL_LITERAL" or op2 == "TK_REAL_LITERAL":
                instruction = ['OP_FADD']
            elif op1 == "TK_INT_LITERAL" or op2 == "TK_INT_LITERAL":
                instruction = ['OP_ADD']
            else:
                # this works so far...
                instruction = ['OP_ADD']
                #print(op_type, op1, op2)
                #raise Exception('some error here')
            self._gen_instruction(instruction)

        elif op_type == "TK_SUBTRACTION":
            instruction = ['OP_SUB']
            self._gen_instruction(instruction)

        elif op_type == "TK_MULTIPLICATION":
            instruction = ['OP_MULT']
            self._gen_instruction(instruction)

    def generate_pushi(self, token):
        """generates the op_pushi instruction and pushes the instruction
        to the instruction_list list. [pushi, {val}]"""
        # hardcode instruction w/ no validation for now.
        #instruction = ['OP_PUSHI, %s' % (token.get_value())]
        instruction = ['OP_PUSHI', token.get_value()]
        self._gen_instruction(instruction)
        #print instruction

    def generate_pop(self, identifier):
        """generates the op_pop instruction."""
        # lookup memory address in symbol table.
        mem_addr = self.symbol_table.lookup_addr(identifier)
        instruction = ['OP_POP', mem_addr]
        self._gen_instruction(instruction)

    def generate_halt(self):
        """generate the OP_HALT instruction."""
        instruction = ['OP_HALT']
        self._gen_instruction(instruction)

    def generate_writeln(self, identifier):
        """generates the writeln statement for identifier(s)"""
        mem_addr = self.symbol_table.lookup_addr(identifier)
        instruction = ['OP_WRITELN', mem_addr]
        self._gen_instruction(instruction)

    def generate_div(self):
        pass

    def _gen_instruction(self, instruction):
        """pushes instruction to internal instruction list"""
        #instruction = "%s. %s" % (self.instruction_number, instruction)
        self.instruction_list.append(instruction)
        #self.instruction_number += 1 

    def print_instruction_list(self):
        print("---")
        for instruction in self.instruction_list:
            pp.pprint(instruction)
        #print self.instruction_list
        #pp.pprint(self.instruction_list)

    def export_instructions(self):
        return self.instruction_list
