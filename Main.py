# Patrick Murray - G00344530

# Implement the shunting yard algorithm
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
        # c is an operator.
        if c in {'*', '.', '|'}:
            # Check what is on the stack.
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
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
        # c is a digit.
        else:
            # Push it to the output
            postfix = postfix + c

    while len(stack) != 0:
        # Append operator at top of stack to output.
        postfix = postfix + stack[-1]
        # Remove operator from stack.
        stack = stack[:-1]
    # Return the postfix
    return postfix

# Implement Thompson's construction
# Adapted from https://web.microsoftstream.com/video/4012d43a-bb46-4ceb-8aa9-2ae598539a32

# Thompson's construction.

class State:
    """A state and its arrows in Thompson's construction."""
    def __init__(self, label, arrows, accept):
        """label is the arrow labels, arrow is a list of states to
           point to, accept is a boolean as to whether this is an accept
           state.
        """
        self.label = label
        self.arrows = arrows
        self.accept = accept
    
    def followes(self):
        """The set of states that are gotten from following this state
           and all its e arrows."""
        # Include this state in the returned set.
        states = {self}
        # If  this state has e arrows, i.e label is None.
        if self.label is None:
            # Loop through this state's arrows.
            for state in self.arrows:
                # Incorporate that state's earrow states in states.
                states = (states | state.followes())
        # Returns the set of states.
        return states

class NFA:
    """A non-deterministic finite automaton."""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    """Check if a string matches an infix regular expression"""
    def match(self, s):
        """Return True if this NFA (instance) matches the string s."""
        # A list of previous states that we are in.
        previous = self.start.followes()
        # Loop through thr string, a character at a time.
        for c in s:
            # Start with an empty set of current states.
            current = set()
            # Loop through the previous states
            for state in previous:
                # Check if there is a c arrow from state.
                if state.label == c:
                    # Add followes for next state.
                    current = (current | state.arrows[0].followes())
                # Replace previous with current
                previous = current
        # If the final state is in previous, then return True. False otherwise.
        return (self.end in previous)

def re_to_nfa(postfix):
    # A stack for NFAs
    stack = []
    # Loop through the postfix r.e. left to right.
    for c in postfix:
        # Concatenation.
        if c == '.':
            # Pop top NFA off stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Make accept state of NFA1 non-accept
            nfa1.end.accept = False
            # Make it point at start state of nfa2.
            nfa1.end.arrows.append(nfa2.start)
            # Make a new NFA with nfa1's start state and nfa2's end state.
            nfa = NFA(nfa1.start, nfa2.end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '|':
            # Pop top NFA off stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states.
            start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start states.
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # Make old accept states non-accept
            nfa1.end.accept = False
            nfa2.end.accept = False
            # Point old end states to new one.
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            # Make a new NFA
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '*':
            # Pop one NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states.
            start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start state.
            start.arrows.append(nfa1.start)
            # And at the new end state
            start.arrows.append(end)
            # Make old accept state non-accept
            nfa1.end.accept = False
            # Make old accept state point to new end state.
            nfa1.end.arrows.append(end)
            # Make old accept state point to old start state.
            nfa1.end.arrows.append(nfa1.start)
            # Make a new NFA
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        else:
            # Create an NFA for the non-special character c
            # Create the end state.
            end = State(None, [], True)
            # Create the start state, pointed at the end state.
            start = State(c, [], False)
            # Point new start state at new end state
            start.arrows.append(end)
            # Create the NFA with the start and end state.
            nfa = NFA(start, end)
            # Append the NFA to the NFA stack.
            stack.append(nfa)
    
    # There should only be one NFA on the stack.
    if len(stack) != 1:
        return None
    else:
        return stack[0]


# Test match function
if __name__ == "__main__":
    tests = [["(a.b|b*)",   ["ab", "b", "bb", "a"]],
             ["a.(b.b)*.a", ["aa", "abba", "aba"]],
             ["1.(0.0)*.1", ["11", "100001", "11001"]]
    ]

    for test in tests:
        infix = test[0]
        print(f"infix:   {infix}")
        postfix = shunt(infix)
        print(f"postfix: {postfix}")
        nfa = re_to_nfa(postfix)
        print(f"thompson: {nfa}")
        for s in test[1]:
            match = nfa.match(s)
            print(f"Match '{s}': {match}")
        print()