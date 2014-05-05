# refactoring out debugger portion of code from scanner

class DebugPrinter:
    def __init__(self):
        pass

    def print_debug(self, s_dict):
        expected_tk_type = s_dict['expected_tk_type']
        total_tokens = s_dict['total_tokens']
        current_tk_count = s_dict['current_tk_count']
        got_tk_val = s_dict['got_tk_val']
        got_tk_type = s_dict['got_tk_type']
        got_tk_cnt = s_dict['got_tk_cnt']
        got_tk_name = s_dict['got_tk_name']
        got_tk_creation_state = s_dict['got_tk_creation_state']
        got_line = s_dict['got_line']
        got_l_ind = s_dict['got_l_ind']
        line_info = s_dict['line_info']
        parse_state = s_dict['parse_state']

        debug_msg = """
        ------- token %s out of %s parsed -------
        parse_state : %s
        type        : %s
        value       : %s
        name        : %s
        line info   : %s
        """ % (
                current_tk_count,
                total_tokens,
                parse_state,
                got_tk_type,
                got_tk_val,
                got_tk_name,
                line_info
                )
        print(debug_msg)

    def tk_match_err(self):
        pass


    def _debug_message(self):
        
        tk_match_err_msg = """TK_MATCH_ERR
        ---tk_match_err on token %s out of %s----
        --> expected match  : %s in parse_state: %s
        --> got type        : %s
        got value   : %s
        got name    : %s
        got line    : %s
        create state: %s
        """ % (
                current_tk_cnt,
                total_tokens,
                expected_tk_type,
                parse_state,
                got_tk_type,
                got_tk_val,
                got_tk_name,
                line_info,
                got_tk_create_state
                )
