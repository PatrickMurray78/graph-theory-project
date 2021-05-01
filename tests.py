import shunt
import thompson

# Test match function
def tests():
    tests = [["(a.b|b*)",   ["ab", "b", "bb", "a"]],
            ["a.(b.b)*.a", ["aa", "abba", "aba"]],
            ["1.(0.0)*.1", ["11", "100001", "11001"]],
            ["a.b+.c+", ["abc", "abcc", "abbbbcc", "bc"]],
            ["c.o.l.o.u?.r", ["color", "colour", "colorr"]]
    ]

    print(f"\n\n%20s" % ("Tests"))
    print("====================================\n") #18

    # For each test in tests
    for test in tests:
        # Set infix to the first field in test
        infix = test[0]
        print(f"Infix: {infix}")
        # Get the postfix of the infix regex using shunt.py
        postfix = shunt.shunt(infix)
        # Get the nfa of the postfix using thompson.py
        nfa = thompson.re_to_nfa(postfix)
        # For each string in the second field of test
        for s in test[1]:
            # Match the nfa to the line of the file
            match = nfa.match(s)
            print(f"String: %-15s Match: %-5s" % (s, match))
        print()