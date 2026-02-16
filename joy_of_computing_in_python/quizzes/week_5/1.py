# Dilrez Builds a Smart Student Record System

# Dilrez is a teaching assistant who is asked to create a Smart Student Record System for a small institute.
# The system must store, update, analyze, and report student data efficiently.

# To achieve this, Dilrez chooses Python Dictionaries because:
# Each student has a unique roll number
# Each roll number maps to multiple details
# Data needs to be updated, searched, and processed quickly

# What Is a Dictionary? (Key–Value Mapping)
# A dictionary stores data in key : value form.
student = {
    "roll":101,
    "name":"Aryan",
    "age":20
}

# 2. Accessing Dictionary Data 
print(student["name"])
print(student.get("age"))
# .get() is safer because it does not cause an error if the key is missing.

# 3. Adding & Updating Data in a Dictionary
# Dilrez now wants to add marks.
student["marks"] = 85
student["age"] = 21

# 4. Dictionary of Lists (One Student, Multiple Scores)
# Each student has marks in multiple tests.
student = {
    "roll":101,
    "name":"Aryan",
    "marks":[78,85,90]
}

# Processing the list inside a dictionary 
average = sum(student["marks"])/len(student["marks"])
print(average)

# 5. Dictionary of Dictionaries (Structured Records)
# Now Dilrez stores multiple students.
student = {
    101: {"name":"Aryan", "marks":[78,85,90]},
    102: {"name":"Riya", "marks":[88,92,79]},
    103: {"name":"Kabir", "marks":[70,75,80]}
}

# Accessing nested data 
print(student[102]["name"])
print(student[101]["marks"][1])
# This structure is ideal for databases, JSON, APIs.

# 6. List of Dictionaries (Row-Wise Data)
# Sometimes data comes row-by-row (like Excel).
students = [
    {"roll":101, "name":"Aryan", "marks":[78,85,90]},
    {"roll":102, "name":"Riya", "marks":[88,92,79]},
    {"roll":103, "name":"Kabir", "marks":[70,75,80]}
    ]
# Searching in list of dictionaries
for student in students:
    if student["roll"]==102:
        print(student["name"])
 
# 7. Looping Through Dictionaries
# Keys only
for key in student:
    print(student[key])

# Values only
for value in student.values():
    print(value)
 
# Key–Value pairs
for key,value in student.items():
    print(key,value)
 
# Complete Mini Program
students = {
    101: {"name": "Aryan", "marks": [78,85,90]},
    102: {"name": "Riya", "marks": [88,92,79]}
}

def class_average(students_dict):
    total = 0
    count = 0
    for student in students_dict.values():
        total+=sum(student["marks"])
        count+=len(student["marks"])
    return total/count

print(class_average(students))


# 1 point
# Dilrez wants to extract the first test score of Riya from a nested student record. What will be printed?
students = {
    101: {"name": "Aryan", "marks": [78,85,90]},
    102: {"name": "Riya", "marks": [88,92,79]}
}
print(students[102]["marks"][0])
#  92
#  79
#  88   (Right Answer)
#  Error

# A new test score is added for Kabir. How many marks does Kabir finally have?
student = {
    "name": "Kabir",
    "marks":[70,75,80]
}
student["marks"].append(85)
print(len(student["marks"]))
#  3
#  85
#  4           (Right Answer)
#  Error

# Dilrez modifies a list stored inside a dictionary and then reuses the same reference. What is printed?
data = {"nums":[1,2,3]}
ref = data["nums"]
ref.append(4)
print(data["nums"])
#  [1, 2, 3]
#  [1, 2, 3, 4]     (Right Answer)
#  Error
#  [4]

# Dilrez slices a list obtained from a dictionary and modifies the slice.What happens to the original list?
student = {"marks": [10,20,30,40]}
subset = student["marks"][:2]
subset.append(99)
print(student["marks"])
#  [10, 20, 30, 40]        (Right Answer)
#  [10, 20, 99]
#  Error
#  [10, 20]

# A function reassigns a dictionary parameter instead of mutating it. What value is printed?
def update(d):
    d = {"x":100}
data = {"x":10}
update(data)
print(data["x"])
#  10      (Right Answer)
#  100
#  None
#  Error

# Dilrez modifies a dictionary while iterating over its keys without creating a copy. What happens when the code runs?
# data = {"a":1,"b":2}
# for k in data.keys():
#     if k=="a":
#         data["c"]=3
# print(len(data))
#  2
#  3     
#  1
#  Runtime Error   (Right Answer) -  Changed size during iteration

# Dilrez draws a bar graph to compare students fairly, even though they have attempted a different number of tests. Which student’s bar will be the tallest?
students = {
    "Ayaan": [70,80,90],
    "Riya": [85,90],
    "Kabir": [60,65,70,75]
}
#  Kabir
#  Ayaan
#  Riya    (Right Answer)
#  All bars will be equal

# Dilrez plots a line graph showing performance of each test across all students. Which test appears as the highest point?
students = {
    1: {"marks":[50,60,70]},
    2: {"marks":[60,70,80]},
    3: {"marks":[70,80,90]}
}
#  Test 2
#  Test 1
#  Test 3          (Right Answer)
#  All tests overlap

# Dilrez creates a pie chart showing pass vs fail distribution (pass ≥ 60). Which section occupies more area?
records = [
    {"name":"A","marks":45},
    {"name":"B","marks":75},
    {"name":"C","marks":65},
    {"name":"D","marks":55},
    {"name":"E","marks":85},
]
#  Equal distribution
#  Pass section       (Right Answer)
#  Cannot be inferred
#  Fail section

# Dilrez plots a cumulative trend graph of weekly progress. What overall shape will the graph show?
data = {
    "week1":[10,20],
    "week2":[30],
    "week3":[40,50]
}
#  Decreasing trend
#  Flat line
#  Random fluctuations    (Right Answer)
#  Increasing trend