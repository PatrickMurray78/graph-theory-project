# Adapted from the pseudocode at:
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm

def shunt(infix):
    """Convert infix expressions to postfix."""
    # The eventual output.
    postfix = ""
    # The shunting yard operator stack.
    stack = ""
    # Operator precedence.
    prec = {'*': 100,  '/': 90 ,'+': 80 , '-': 70}
    # Loop through the input a character at a time.
    for c in infix:
        # c is a digit.
        if c in {'0','1','2', '3', '4', '5', '6', '7', '8', '9'}:
            # Push it to the output.
            postfix = postfix + c
        # c is an operator.
        elif c in {'+', '-', '*', '/'}:
            # Check what is on the stack.
            while len(stack) > 0 and prec[stack[-1]] > prec(c) and stack[-1] != '(':
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Push c to stack.
            stack = stack + c


        else if the token is a left parenthesis (i.e. "("), then:
            push it onto the operator stack.
        else if the token is a right parenthesis (i.e. ")"), then:
            while the operator at the top of the operator stack is not a left parenthesis:
                pop the operator from the operator stack onto the output queue.
            /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */
            if there is a left parenthesis at the top of the operator stack, then:
                pop the operator from the operator stack and discard it
            if there is a function token at the top of the operator stack, then:
                pop the function from the operator stack onto the output queue.
    /* After while loop, if operator stack not null, pop everything to output queue */
    if there are no more tokens to read then:
        while there are still operator tokens on the stack:
            /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
            pop the operator from the operator stack onto the output queue.
            
    return postfix



infix = "3+4x(2-1)"
postfix = "3421-x+"

if shunt(infix) == postfix:
    print("It seems to work.")