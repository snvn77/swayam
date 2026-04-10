# Academic Date Gap Calculator

# Problem Statement
# You are given two dates through standard input.
# Each date is provided in the format YYYY-MM-DD.
# Your task is to calculate the absolute number of days between the two dates and print the result.
# The order of dates does not matter.
# Leap years must be handled correctly.
# If both dates are the same, the result should be 0.

# Input Format
# First line contains the first date in YYYY-MM-DD format
# Second line contains the second date in YYYY-MM-DD format

# Output Format
# Print a single integer representing the absolute difference in days between the two dates

# Constraints
# Years are in the range supported by the Python datetime module
# Dates are guaranteed to be valid

from datetime import datetime

d1 = input()
d2 = input()

date1 = datetime.strptime(d1,"%Y-%m-%d")
date2 = datetime.strptime(d2,"%Y-%m-%d")

print(abs((date1-date2).days), end="")