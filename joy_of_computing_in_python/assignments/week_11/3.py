# Monthly Calendar Generator

# Problem Statement
# You are given a year and a month through standard input.
# Your task is to generate and display the calendar for the given month and year.
# The calendar should follow the standard Gregorian calendar format.
# Weekdays should be displayed from Monday to Sunday.
# The output should match the standard calendar layout.

# Input Format
# First line contains an integer year
# Second line contains an integer month (1 to 12)

# Output Format
# Print the calendar for the given month and year

# Constraints
# 1 ≤ year ≤ 9999
# 1 ≤ month ≤ 12

import calendar

yr = int(input())
mnth = int(input())

print(calendar.month(yr,mnth))