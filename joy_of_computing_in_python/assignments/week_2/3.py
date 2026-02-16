# Signal Stability Checker
# Signal processors analyze sequences of numerical measurements to determine whether a signal is consistently increasing over time.

# Problem Description
# You are given a sequence of integers representing signal measurements taken over time.
# A signal is said to be strictly increasing if every element is greater than the previous one.

# Input Format
# A single line containing space-separated integers representing signal measurements.

# Output Format
# Print True if the sequence is strictly increasing.
# Otherwise, print False.
# The program must always print exactly one Boolean value.

# Constraints
# Input contains at least one integer.
# All values are integers.

# Private Test cases used for evaluation	    Input	      Expected Output
# Test Case 1	                              1 3 5 7 9          True
# Test Case 2	                               10 20 15          False
# Test Case 3	                               2 4 6 8           True

l_str = input().split()

l_list = []
for i in l_str:
  l_list.append(int(i))

if len(l_list) == 1:
  print(True)
else:
  count = 0
  for i in range(1,len(l_list)):
    if l_list[i]<=l_list[i-1]:
      count+=1
  if count>0:
    print(False)
  else:
    print(True)