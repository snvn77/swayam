# Word Length Comparator:

# Problem Statement:
# Text analysts compare words based on their lengths. Write a program to perform the following steps:
# Accept a comma-separated list of words.
# Calculate the average length of the words.
# Round up the average to the nearest whole number (Ceiling value).
# Count how many words have a length strictly greater than this rounded average.

# Input Format:
# A single line containing comma-separated words.

# Output Format:
# Print a single integer count.

# Example Calculation (for clarity):
# Input: one,two,three,four
# Word Lengths: 3, 3, 5, 4
# Mathematical Average: (3+3+5+4) / 4 = 3.75
# Rounded Average (Ceiling): 4 (Always round up decimal values)

# Comparison: Check which words have length > 4.
# one (3) > 4? No.
# two (3) > 4? No.
# three (5) > 4? Yes.
# four (4) > 4? No.
# Count: 1

# Private Test cases used for evaluation	         Input	            Expected Output
# Test Case 1	                                     x,y,z                     0
# Test Case 2	                                 sun,moon,stars                1
# Test Case 3	                              red,blue,green,yellow            1

import math 

l_str = input().split(',')

l_len = []
for i in l_str:
  if i.strip():
    l_len.append(len(i.strip()))

average = math.ceil(sum(l_len)/len(l_len))

count = 0
for i in l_len:
  if i>average:
    count = count+1

print(count,end='')