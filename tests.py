import shunt
import thompson

# Test match function
def tests():
    tests = [["(a.b|b*)",   ["ab", "b", "bb", "a"]],
            ["a.(b.b)*.a", ["aa", "abba", "aba"]],
            ["1.(0.0)*.1", ["11", "100001", "11001"]],
            ["a?.b?", ["a", "b", "ab", "abb"]],
            ["a.b+.c+", ["abc", "abcc", "abbbbcc", "bc"]],
            ["c.o.l.o.u?.r", ["color", "colour", "colorr"]]
    ]

    # For each test in tests
    for test in tests:
        # Set infix to the first field in test
        infix = test[0]
        print(f"infix:   {infix}")
        # Get the postfix of the infix regex using shunt.py
        postfix = shunt.shunt(infix)
        print(f"postfix: {postfix}")
        # Get the nfa of the postfix using thompson.py
        nfa = thompson.re_to_nfa(postfix)
        print(f"thompson: {nfa}")
        # For each string in the second field of test
        for s in test[1]:
            # Match the nfa to the line of the file
            match = nfa.match(s)
            print(f"Match '{s}': {match}")
        print()