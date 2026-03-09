# Recursive Digit Sum Calculator

# Problem Statement
# To analyze numeric identifiers, systems often compute the sum of digits of a number. In this task, iterative approaches are restricted.
# You are required to write a Python function as described below.

# digit_sum(n)

# Input:
# A non-negative integer n.

# Output:
# Return the sum of all digits of n.

# Notes:
# The solution must use recursion.
# Loops must NOT be used.
# The number must NOT be converted to a string.

def digit_sum(n):
  if n==0:
    return 0
  else:
    return (n%10)+digit_sum(n//10)