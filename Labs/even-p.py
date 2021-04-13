
class State:
    """A state in an automaton."""
    def __init__(self, accept, arrows):
        # True if this is an accept state
        self.accept = accept
        # Arrows (keys are labels) out of state
        self.arrows = arrows

class DFA:
    """An automaton"""
    def __init__(self, start):
        # Start state of the automaton
        self.start = start
    
    def match(self, s):
        """See if s is accepted by the automaton"""
        # Current state.
        current = self.start
        # Loop through the characters in s.
        for c in s:
            # Find the state in arrows with key c.
            current = current.arrows[c]
        # Return whether we're in an accept state.
        return current.accept
    
def compile():
    """Create the automaton."""

    # Create the start state.
    start = State(True, {})
    # Create other state.
    other = State(False, {})

    # The states point to themseves on a 0.
    start.arrows['0'] = start
    other.arrows['0'] = other

    # The states point to themseves on a 0.
    start.arrows['1'] = other
    other.arrows['1'] = start

    # Create an automaton
    parity = DFA(start)

    # Return Automaton
    return parity

# Create automaton instance.
myautomaton = compile()
# A few small tests
for s in ['1100', '11111', '', '1', '0']:
    # Check if s is accepted by the automaton.
    result = myautomaton.match(s)
    # Print the result.
    print(f"{s} -> {result}")

for s in ['000', '001', '010', '011', '100', '110', '111']:
    # Check if s is accepted by the automaton.
    result = myautomaton.match(s)
    # Print the result.
    print(f"{s} -> {result}")