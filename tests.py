import shunt
import thompson

# Test match function
def tests():
    tests = [["(a.b|b*)",   ["ab", "b", "bb", "a"]],
            ["a.(b.b)*.a", ["aa", "abba", "aba"]],
            ["1.(0.0)*.1", ["11", "100001", "11001"]],
            ["a?.b?", ["a", "b", "ab", "abb"]],
            ["a.b+.c+", ["abc", "abcc", "abbbbcc", "bc"]]
    ]

    for test in tests:
        infix = test[0]
        print(f"infix:   {infix}")
        postfix = shunt.shunt(infix)
        print(f"postfix: {postfix}")
        nfa = thompson.re_to_nfa(postfix)
        print(f"thompson: {nfa}")
        for s in test[1]:
            match = nfa.match(s)
            print(f"Match '{s}': {match}")
        print()