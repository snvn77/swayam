# Meera and the Community Learning Center

# Meera volunteered at a community learning center that offered short-term courses such as Python Basics, Data Analysis, and Web Development.

# The center faced a recurring problem every month:
# Student registrations came from different sources
# Course details were fixed once announced
# Attendance had to be tracked per student
# Records needed to be stored permanently for audits

#  Meera was asked to build a simple data system in Python that could manage all this information reliably.

# ----------------------------------------------------------------------------------------------------------------------------------------------

# Step 1: Fixed Course Information (Tuples)

# At the start of the month, course details were finalized and never changed afterward.

# Each course had:
# Course ID
# Course Name
# Duration (weeks)

# Meera stored this data as tuples.  

python_course = (101, "Python Basics", 6)
data_course = (102, "Data Analysis", 8)
web_course = (103, "Web Development", 10)

# -----------------------------------------------------------------------------------------------------------------------------------------------

# Step 2: Managing Student Registrations (Lists)

# Student registrations arrived daily, and new names had to be added continuously.

# Meera maintained a list of registered students.

students = ["Aarav", "Neha", "Ishaan"]
students.append("Mehul")
students.append("Neha")

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Step 3: Mapping Students to Courses (Dictionary)

# Each student enrolled in one course only, and Meera needed a clear mapping.

# She used a dictionary where:
# Key → Student name
# Value → Course tuple

enrollments = {
    "Aarav": python_course,
    "Neha": data_course,
    "Ishaan": python_course,
    "Mehul": web_course
}

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Step 4: Tracking Attendance per Student (Dictionary + List)

# Attendance changed every day, so Meera needed a mutable structure.

# She decided:
# Each student would have a list of attended session numbers 

attendance = {
    "Aarav": [1,2,3],
    "Neha": [1,2],
    "Ishaan": [1,3],
    "Mehul": []
}

# Later updates:

attendance["Mehul"].append(1)
attendance["Neha"].append(3)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# Step 5: Saving Records to a File (File Handling)

# At the end of the week, Meera needed to store enrollment data permanently.

# She wrote student-course mappings to a file. 

with open("enrollments.txt", "w") as file:
    for student, course in enrollments.items():
        file.write(f"{student} - {course[1]} ({course[2]} weeks)\n")

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# Step 6: Reading Stored Records Later

# During an audit, Meera retrieved the saved data.

with open("enrollments.txt", "r") as file:
    records = file.readlines()

for line in records:
    print(line.strip())

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Questions:

# Suppose the following change is made before writing to the file:
python_course = (101, "Python Basics", 6)
python_course[2] = 7
# What would be the first issue encountered in the program?
#  The file will store incorrect duration
#  A runtime error will occur due to tuple immutability      (Right Answer)
#  The dictionary enrollments will update automatically
#  The list students will change size



# Consider this code is added after reading from the file:  
records = file.readlines()
records.append("Rohan - Python Basics (6 weeks)\n")
# Which statement is TRUE?  
#  A file write error occurs
#  The file content changes automatically
#  The new record is saved permanently in enrollments.txt
#  Only the in-memory list is modified       (Right Answer)



# Assume this code is executed:
attendance["Aarav"].append(4)
enrollments["Aarav"] = (101, "Python Basics", 6)
# Which statement best explains what happens?  
#  Both operations fail
#  Both operations succeed       (Right Answer)
#  Attendance succeeds, enrollment fails
#  Enrollment succeeds, attendance fails



# If Meera replaces this line:
students = ["Aarav", "Neha", "Ishaan"]
# with:
students = ("Aarav", "Neha", "Ishaan")
students.append("Mehul")
# What is the correct outcome?  
#  The student is added successfully
#  A runtime error occurs due to unsupported operation       (Right Answer)
#  The tuple expands automatically
#  The enrollment file updates



# Which design choice in the case study most directly protects course data from accidental modification?
#  Using formatted strings while writing files
#  Using lists for attendance tracking
#  Reading files using readlines()
#  Storing course details as tuples inside dictionaries       (Right Answer)