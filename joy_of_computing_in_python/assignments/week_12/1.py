# Dictionary Consistency Checker 

#  Problem Statement
# A system stores data in a dictionary named records, where:
# Each key is a string.
# Each value is a list of integers.

# A key is said to be consistent if the list associated with it satisfies both conditions:
# The list is strictly increasing.
# The difference between every pair of consecutive elements is the same.

# Your task is to:
# Count how many keys in the dictionary are consistent.
# Print the count.

# Notes:
# A list with 0 or 1 element is considered consistent.
# You have to take the input.
# Print only an integer.



import ast

# s = input()
# my_dict = ast.literal_eval(s)
my_dict = ast.literal_eval(input())

count = 0
for value in my_dict.values():
    if len(value)<=1:
        count+=1
        continue
    diff = value[1]-value[0]
    # if diff>0 and sorted(value)==value:
    #     if len(value)==2:  
    #         count+=1
    #     else:
    #         val=0
    #         for i in range(2, len(value)):
    #             if value[i]-value[i-1] == diff:
    #                 val+=1
    #         if val==len(value)-2:
    #             count+=1
    if diff>0 and all(value[i]-value[i-1]==diff for i in range(2,len(value))):
        count+=1

      
print(count,end="")  