# Cargo Weight Floor Converter:
# Problem Statement
# At AeroPort-X, cargo weights are recorded as real numbers for logistical operations.
# For standardized loading, each recorded weight must be converted into an integer using a fixed rule.

# Task Description
# You are required to:
# Accept a space-separated sequence of positive real numbers.
# Convert each number to the greatest integer less than or equal to it.
# Print the converted integers separated by commas.

# Input Format
# A single line containing space-separated real numbers.

# Output Format
# A single line containing integers separated by commas.

# Private Test cases used for evaluation	  Input	     Expected Output
# Test Case 1	                           100.0 200.8       100,200
# Test Case 2	                           7.7 8.8 9.9        7,8,9
# Test Case 3	                           3.3 3.3 3.3        3,3,3

l_str = input().split()

print(int(float(l_str[0])),end='')
for i in range(1,len(l_str)):
  print(',',end='')
  print(int(float(l_str[i])),end='')