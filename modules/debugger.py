# refactoring out debugger portion of code from scanner

class DebugPrinter:
    def __init__(self):
        pass

    def print_debug(self, token, tk_index, tk_count):
        line_info = "(%s, %s)" % (token.get_line_number(), token.get_line_index())
        debug_msg = """
        ------- token %s out of %s parsed -------
        parse_state : %s
        type        : %s
        value       : %s
        name        : %s
        line info   : %s
        """ % (
                tk_index,
                tk_count,
                token.get_creation_state(),
                token.get_type(),
                token.get_value(),
                token.get_name(),
                line_info
                )
        print(debug_msg)

    def raise_match_tk_err(self, token, tk_index, tk_count, expected_tk, got_tk):
        line_info = "(%s, %s)" % (token.get_line_number(), token.get_line_index())
        tk_match_err = """ TK_MATCH_ERR
        ------- token %s out of %s -------
        ---> EXPECTED_MATCH : %s
        ___> GOT_TK_TYPE    : %s
        parse_state : %s
        type        : %s
        value       : %s
        name        : %s
        line info   : %s
        """ % (
                tk_index,
                tk_count,
                expected_tk,
                got_tk,
                token.get_creation_state(),
                token.get_type(),
                token.get_value(),
                token.get_name(),
                line_info
                )
        raise Exception(tk_match_err)


    

