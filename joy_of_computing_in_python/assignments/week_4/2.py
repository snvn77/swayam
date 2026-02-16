# Problem Statement
# A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself).

# Write a function is_perfect(n) that:
# - Accepts a positive integer n
# - Returns True if n is a perfect number
# - Returns False otherwise

# Constraints:
# - 1 ≤ n ≤ 10^6
# - n is an integer



def is_perfect(n):
  sum = 0
  for i in range(1,n):
    if n%i==0:
      sum+=i
  if sum==n:
    return True
  else:
    return False