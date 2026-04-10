# Case Study: Automated Academic Schedule Analyzer

# Background
# A university administration system needs to analyze academic schedules for a semester.
# The system should be able to:
# Track important academic dates (semester start, exams, holidays)
# Determine weekdays for given dates
# Identify leap years (important for February schedules)
# Generate monthly calendars for planning purposes
# Compute gaps between important academic events

# To implement this functionality, the developers decide to use Python’s built-in datetime and calendar modules.
# Part 1: Working with Dates and Time (datetime Module)
# The system begins by capturing the current date and time when the administrator logs in.

import datetime
login_time = datetime.datetime.now()
print(login_time) # 2026-04-01 01:19:22.882982
# This timestamp is later used for logging administrative actions.

# Creating Fixed Academic Dates
# The semester officially starts on August 5, 2025, and the mid-semester exam is scheduled for October 12, 2025.

semester_start = datetime.date(2025,8,5)
mid_exam = datetime.date(2025,10,12)
print(semester_start,mid_exam) # 2025-08-05 2025-10-12
# Each of these objects stores only the date, not the time.

# Calculating Duration Between Events
# The system calculates how many days students have between the semester start and the mid-semester exam.

gap = mid_exam-semester_start
print(gap.days) # 68
# This value is later used to ensure syllabus coverage is realistic.

# Extracting Date Components
# For reporting purposes, individual components of a date are extracted:

year = semester_start.year
month = semester_start.month
day = semester_start.day
print(year,month,day) # 2025 8 5
# These values are stored separately in the database.

# Formatting Dates for Reports
# To generate human-readable academic notices, dates are formatted:

formatted_date = semester_start.strftime("%A, %d %B %Y") 
print(formatted_date) # # Tuesday, 05 August 2025

# Part 2: Academic Calendar Analysis (calendar Module)
# To assist with planning lectures and exams, the system generates a monthly calendar.

import calendar

print(calendar.month(2025,8))
#     August 2025
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31
# This helps administrators visualize holidays and weekends.

# Checking Leap Year Constraints
# Since February schedules depend on leap years, the system verifies whether 2024 is a leap year.

print(calendar.isleap(2024)) # True
# This check prevents incorrect date assumptions during scheduling.

# Identifying Weekdays for Exams
# The day of the week for the mid-semester exam is computed:

exam_day = calendar.weekday(2025,10,12)
print(exam_day) # 6
print(calendar.day_name[exam_day]) # Sunday
# This ensures exams are not accidentally scheduled on weekends.

# Counting Days in a Month
# To calculate the total number of lecture days in a month:

days_in_august = calendar.monthrange(2025,8)
print(days_in_august) # (calendar.FRIDAY, 31) ---> (first_weekday, number_of_days)
# This value is later filtered to exclude weekends and holidays.



# The system computes the gap between semester_start and mid_exam using:
gap = mid_exam-semester_start
# What does gap.days logically represent?
#  The number of calendar days between the two academic events   (Right Answer)
#  The number of weekdays between the two dates
#  The number of lecture days excluding holidays
#  The number of months between the two dates




# If semester_start is created as:
semester_start = datetime.date(2025,8,5)
# Which of the following attributes is NOT directly available from this object?
#  semester_start.year
#  semester_start.hour   (Right Answer)
#  semester_start.month
#  semester_start.day




# The following code is used to format a date for notices:
semester_start.strftime("%A, %d %B %Y")
# Which part of the output is produced specifically by %A?
#  Numeric day of the month
#  Full name of the month
#  Full name of the weekday   (Right Answer)
#  Four-digit year




# Why does the system check the following condition?
calendar.isleap(2024)
#  To determine whether weekends change in 2024
#  To confirm February has 29 days in that year   (Right Answer)
#  To find how many weekdays exist in 2024
#  To calculate the total number of academic days





# The system determines the exam weekday using:
exam_day = calendar.weekday(2025,10,12)
calendar.day_name(exam_day)
# Why is this a two-step process?
#  calendar.weekday() returns a string index
#  calendar.weekday() returns a month name
#  calendar.weekday() returns an integer mapped to a weekday   (Right Answer)
#  calendar.day_name only works for leap years





# Consider the code:
days_in_august = calendar.monthrange(2025,8)[1]
# What does the index [1] specifically retrieve?
#  The weekday of the first day of August
#  The number of Sundays in August
#  The total number of days in August    (Right Answer)
#  The number of weekdays in August




# Why is datetime.datetime.now() used instead of datetime.date.today() for login tracking?
#  date.today() is slower
#  Login tracking requires both date and time    (Right Answer)
#  datetime.date cannot be stored in logs
#  datetime.now() works only on servers