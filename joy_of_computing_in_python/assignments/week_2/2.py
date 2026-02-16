# Temperature Alert System
# ClimateWatch monitors daily temperature readings collected from different regions.
# To ensure safety, the system must flag temperatures that exceed the permissible limit.

# Problem Description
# You are given a single line of input containing space-separated integers, where each integer represents a temperature reading for a particular region.
# A temperature is considered unsafe if it is strictly greater than 50.

# Input Format
# A single line containing space-separated integers representing temperature readings.

# Output Format
# If one or more temperatures are strictly greater than 50, print all such temperatures in the same order as input, separated by spaces.

# If no temperature exceeds 50, print 0.

# Private Test cases used for evaluation   	Input	        Expected Output
# Test Case 1	                              51 51              51 51
# Test Case 2	                          80 20 90 80 90      80 90 80 90
# Test Case 3	                            0 100 100           100 100

l_str = input().split()

l_list = []
for i in l_str:
  l_list.append(int(i))

count = 0
for i in l_list:
  if i>50:
    print(i, end=' ')
    count=count+1
 
if count==0:
  print(count)