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
    def __init__(self):
        self.stack = []
        # for debugging etc. shows list of pushed instructions.
        self.instruction_list = []

    def op_add(self):
        """
        s1 = int(stack.pop())
        s2 = int(stack.pop())
        stack.push(s1 + s2) # is this wrong?
        """
        pass

    def generate(self, state, op_type, op1=None, op2=None):
        print state, op_type, op1, op2

    def op_assign(self):
        """

        """

