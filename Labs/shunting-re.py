# Adapted from the pseudocode at:
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm

def shunt(infix):
    """Convert infix expressions to postfix."""
    # The eventual output.
    postfix = ""
    # The shunting yard operator stack.
    stack = ""
    # Operator precedence.
    prec = {'*': 100,  '.': 90 ,'|': 80}
    # Loop through the input a character at a time.
    for c in infix:
        # c is a digit.
        if c in {'a', 'b'}:
            # Push it to the output.
            postfix = postfix + c
        # c is an operator.
        elif c in {'*', '.', '|'}:
            # Check what is on the stack.
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >=   prec[c]:
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Push c to stack.
            stack = stack + c
        elif c == '(':
            # Push c to stack.
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Remove open bracket from stack.
            stack = stack[:-1]
    while len(stack) != 0:
        # Append operator at top of stack to output.
        postfix = postfix + stack[-1]
        # Remove operator from stack.
        stack = stack[:-1]
    # Return the postfix
    return postfix

if __name__ == "__main__":
    for infix in ["a.(b.b)*.a"]:
        print(f"infix: {infix}")
        print(f"shunt: {shunt(infix)}")
        print()