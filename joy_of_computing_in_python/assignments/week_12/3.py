# Longest Consecutive Sequence Finder

# Problem Statement
# You are given a list of integers named nums.
# The integers may appear in any order and may include duplicates.

# Your task is to determine the length of the longest sequence of consecutive integers that can be formed using elements from the list.

# Important Notes:
# Consecutive numbers must differ by exactly 1.
# The sequence can be formed regardless of the order of elements in the list.
# Duplicate values should be considered only once.
# You must print only the length of the longest consecutive sequence.
# You need to take input.
# Do not use functions.

#    Input Format
# A list of integers nums (single line input).

# Example:
# [100, 4, 200, 1, 3, 2]

#    Output Format
# Print a single integer — the length of the longest consecutive sequence.


import ast

s = input()
nums = ast.literal_eval(s)

if nums:
    ref = []
    for i in sorted(nums):
        if i not in ref:
            ref.append(i)

    count=1
    res=1
    for i in range(1,len(ref)):
        if ref[i]-ref[i-1] == 1:
            res+=1
            count = max(res,count)
        else:
            res = 1

    print(count,end="")

else:
    print(0,end="")

# ---------------------------------------------------------------------------------------------
import ast

nums = ast.literal_eval(input())

if not nums:
    print(0,end="")

else:  
    ref = set(nums)

    longest = 1
    for num in ref:
        if num-1 not in ref: # Start with the number that does not have a preceding number
            current = num
            length = 1

            while current+1 in ref: # From that num check for the consecutive sequence
                current+=1
                length+=1
            longest = max(length, longest)   

    print(longest,end="")