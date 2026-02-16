# Energy Readings at Solar Valley: 
# At Solar Valley Research Station, engineers record daily energy readings from solar panels. Each reading represents the amount of power generated on a particular day. To assess performance, analysts compare individual readings against the overall average.

# Problem Statement
# Given a sequence of daily energy readings, determine how many readings are strictly greater than the average of all readings.

# Input Format
# A single line containing space-separated positive integers (each integer represents the energy generated on a day).

# Output Format
# Print a single integer:
# the count of numbers strictly greater than the average of the given sequence.

# Constraints
# All input numbers are positive integers.
# At least one number is present in the input.

# Computation Details
# Compute the average of all given numbers.
# Count how many numbers are greater than (not equal to) the average.
# Print the count.

# Sample Input
# 10 20 30 40 50

# Sample Output
# 2

# Explanation
# Average = (10 + 20 + 30 + 40 + 50) / 5 = 30
# Numbers strictly greater than 30 are 40 and 50
# Count = 2

# Private Test cases used for evaluation	Input	         Expected Output
# Test Case 1	                          10 40 50 60             2
# Test Case 2	                            2 4 6 8               2
# Test Case 3	                             9 1 3                1

l_str = input().split()

l_list = []
for i in l_str:
  l_list.append(int(i))
average = sum(l_list)/len(l_list)

count = 0
for i in l_list:
  if i>average:
    count+=1

print(count, end = '')