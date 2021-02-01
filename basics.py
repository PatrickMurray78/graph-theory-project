# Patrick Murray
# Python basics
# 2021-02-01

def factorial(n):
    """Number to calculate factorial of"""
    # Deal with negative inputs
    if n < 1:
        m = -n
    else:
        m = n
    # The running total = eventually the factorial
    total = 1
    # Loop to do the multiplications
    while m > 1:
        total = total * m
        m = m - 1
    # Return the answer
    if n < 1:
        return -total
    else:
        return total

# Test the function
n = -10
# Calculate the factorial of n
print(f"The factorial of {n} is {factorial(n)}")