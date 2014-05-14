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
class StackMachine:
    def __init__(self, symbol_table):
        self.stack = []
        # for debugging etc. shows list of pushed instructions.
        self.instruction_list = []
        self.symbol_table = symbol_table

    def op_add(self):
        """
        s1 = int(stack.pop())
        s2 = int(stack.pop())
        stack.push(s1 + s2) # is this wrong?
        """
        pass

    def generate(self, state, op_type, op1=None, op2=None):
        print state, op_type, op1, op2

    def generate_pushi(self, token):
        """generates the pushi instruction and pushes the instruction
        to the instruction_list list. [pushi, {val}]"""
        # hardcode instruction w/ no validation for now.
        instruction = 'op_pushi, %s' % (token.get_value())
        print instruction

    def print_instruction_list(self):
        for instruction in self.instruction_list:
            print instruction
