"""Verifying the Collatz conjecture"""

# Patrick Murray

def f(n):
    # If n is even
    if n % 2 == 0:
        return n // 2
    # If n is odd
    elif n % 2 == 1:
        return (3 * n) + 1
    else:
        return None

def collatz(n):
    so_far = []
    # Loop until n is 1
    while n != 1:
        if n in so_far:
            return False
        so_far.append(n)
        n = f(n)
    so_far.append(n)
    return so_far

#print(collatz(10))
print(collatz(11))