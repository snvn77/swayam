# Palindrome Number Checker in Python:

# Ravi is learning Python and is currently practicing loops and arithmetic operations.
# As part of his practice, he is given a task to check whether a given number is a palindrome.

# A palindrome number is a number that reads the same forward and backward.
# Examples:
#  121 → Palindrome
#  456 → Not a Palindrome

# Ravi decides not to convert the number into a string, because he wants to strengthen his understanding of:
# while loops
# Modulus (%) operator
# Integer division (//) 

def is_palindrome(n):
    original = n
    reverse = 0

    while n>0:
        reverse = reverse*10 + (n%10)
        n//=10

    return reverse == original

# What is the final value of reverse when the function is called as: is_palindrome(120)
#  210
#  120
#  21 (Right Answer)
#  12

# What will the function return for the input: is_palindrome(7)
#  Error because loop runs only once
#  True (Right Answer)
#  False
#  None

# How many times does the while loop execute when the function is called as: is_palindrome(1001)
#  2
#  4 (Right Answer) 
#  3
#  1

# Suppose the loop condition is changed to: while n>=0
# What will happen when the function is called with is_palindrome(5)?
#  It enters an infinite loop (Right Answer)
#  It returns False after one iteration
#  It correctly returns True
#  It raises a runtime error