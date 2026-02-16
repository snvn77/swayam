# Divisor Archive of Mathoria
# Problem Statement
# In the land of Mathoria, scholars study numbers by analyzing their divisors. You are required to write three Python functions as described below.

# 1. divisors(n)
# Input:
# An integer n where n ≥ 1.
# Output:
# Return a sorted list of all positive divisors of n.
# Notes:
# The list must be in ascending order.
# Each divisor should appear exactly once.

# 2. common_divisors(a, b)
# Input:
# Two integers a and b where a ≥ 1 and b ≥ 1.
# Output:
# Return a sorted list of all common positive divisors of a and b.
# Notes:
# The list must be in ascending order.
# The result must be a list, not a set or tuple.

# 3. divisors_upto(n)
# Input:
# An integer n where n ≥ 1.
# Output:
# Return a dictionary in which:
# Each key is an integer from 1 to n (inclusive).
# Each value is a sorted list of all positive divisors of the key.
# Notes:
# Dictionary keys must appear in increasing order from 1 to n.
# Each value must follow the same rules as the output of divisors(n).

# Example Behaviour (for clarity)
# divisors(6) → [1, 2, 3, 6]
# common_divisors(12, 18) → [1, 2, 3, 6]
# divisors_upto(3) → {1: [1], 2: [1, 2], 3: [1, 3]}


def divisors(n):
  l = []
  for i in range(1,n+1):
    if n%i==0:
      l.append(i)
  return l

def common_divisors(a,b):
  n = min(a,b)
  l = []
  for i in range(1,n+1):
    if a%i==0 and b%i==0:
      l.append(i)
  return l

def divisors_upto(n):
  d = {}
  for i in range(1,n+1):
    d[i] = divisors(i)
  return d