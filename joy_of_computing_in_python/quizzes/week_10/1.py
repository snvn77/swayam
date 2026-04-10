# Relationship Prediction Using Character Elimination Logic

# Background
# A small social-logic application is designed to predict the type of relationship between two individuals based on their names. 
# The program does not rely on predefined rules about people; instead, it uses a character elimination strategy followed by a cyclic 
# counting process to arrive at a final outcome.

# This kind of logic-based application is often used to help learners understand:
# list manipulation
# nested loops
# conditional branching
# iterative elimination logic
# modular arithmetic
# Problem Context

# The system asks two users to enter their names. To ensure fairness and consistency:
# All characters are converted to lowercase
# Spaces are removed
# Each name is converted into a list of characters
# The program then compares both names character by character.

# Core Logic Explained
# 1. Character Matching and Removal
# The program scans both character lists.
# When a matching character is found:
# 		- That character is removed from both lists
# 		- The process restarts immediately
# This continues until no common characters remain
# This step ensures only unmatched characters contribute to the final calculation.

# 2. Counting Remaining Characters
# After all matching letters are removed:
# The total number of remaining characters is calculated
# This count becomes the key value used to determine the relationship

# 3. Relationship Categories
# The application uses a fixed list of relationship outcomes:		
# Using the remaining character count:
# A circular elimination process is applied
# One relationship is removed at each step
# The list keeps shrinking until one final relationship remains
# This mirrors a Josephus-style elimination pattern, commonly used in algorithmic problems.
		
def remove_matching_letter(list_1,list_2):
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                list_1.remove(list_1[i])
                list_2.remove(list_2[j])
                return (list_1+["*"]+list_2, True)

    return (list_1+["*"]+list_2, False)

def main():
    name_1 = input("Enter the name of first person: ").lower().replace(" ","")
    name_2 = input("Enter the name of second person: ").lower().replace(" ","")

    list_1 = list(name_1)
    list_2 = list(name_2)

    proceed = True
    while proceed:
        result, proceed = remove_matching_letter(list_1,list_2)

    count = len(list_1)+len(list_2)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    split_index = (count%len(result))-1

    if split_index>=0:
        right_half = result[split_index+1:]
        left_half = result[:split_index]
        new_result = right_half+left_half
    else:
        new_result = result[:split_index] # Ignore Last Element

    while len(new_result)>1:
        split_index = (count%len(new_result))-1

        if split_index>=0:
            right_half = new_result[split_index+1:]
            left_half = new_result[:split_index]
            new_result = right_half+left_half
        else:
            new_result = new_result[:split_index] # Ignore Last Element

    final_result = new_result[0]
    print(f"The relationship between {name_1} and {name_2} is: {final_result}")

if __name__=="__main__":
    main()


# What is the primary purpose of the function remove_matching_letter?
#  To count common letters between two names
#  To remove only duplicate letters from the first list
#  To remove the first matching character from both lists and signal continuation  (Right Answer)
#  To concatenate both lists using *


# Why does the function remove_matching_letter return immediately after removing one matching character?
#  To reduce time complexity
#  To restart scanning with updated lists and avoid an IndexError   (Right Answer)
#  To avoid index errors only
#  To preserve list order


# What does the proceed variable control in the while loop?
#  Whether both names are non-empty
#  Whether the result list has more than one element
#  Whether a matching character was found in the previous iteration   (Right Answer)
#  Whether user input is valid


# Why are spaces removed and characters converted to lowercase before processing?
#  To improve execution speed
#  To prevent runtime errors
#  To standardize input for fair character comparison   (Right Answer)
#  To reduce memory usage


# What does the value :

#count = len(list_1)+len(list_2)

# represent in the program?
#  The total number of unmatched characters remaining after elimination   (Right Answer)
#  The total number of iterations executed
#  The length of the longer name
#  The number of matching characters removed


# What is the purpose of the expression

# split_index = (count%len(result))-1
		
# in the relationship elimination logic?
#  To calculate the index at which the list should be rotated or reduced   (Right Answer)
#  To sort the relationship list
#  To randomly select a relationship
#  To check whether the list length is even or odd


# Why does the code handle the case when split_index < 0 separately?
#  Because Python does not allow negative indices
#  Because list slicing fails for negative numbers
#  Because it indicates an invalid count value
#  Because an index of -1 breaks the slicing logic used for removal   (Right Answer)


# What ensures that the relationship elimination continues until only one option remains?
#  The for loop inside remove_matching_letter
#  The condition if split_index >= 0
#  The calculation of count
#  The loop condition while len(new_result) > 1   (Right Answer)


# What would happen if the first return statement (inside the if condition) were removed?
#  The program would crash with an IndexError   (Right Answer)
#  Only the first name would be processed
#  Multiple matches would be removed in one iteration
#  The program would raise a syntax error


# Which algorithmic pattern best describes the relationship elimination phase of the program?
#  Divide and Conquer
#  Greedy selection
#  Backtracking
#  Circular counting with iterative elimination   (Right Answer)


# Alternate Version
def remove_matching_letter(list_1,list_2):
    for i in list_1[:]:
        if i in list_2:
            list_1.remove(i)
            list_2.remove(i)

def main():
    name_1 = input("Enter the name of first person: ").lower().replace(" ","")
    name_2 = input("Enter the name of second person: ").lower().replace(" ","")

    list_1 = list(name_1)
    list_2 = list(name_2)

    remove_matching_letter(list_1,list_2)

    count = len(list_1)+len(list_2)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    pointer = 0

    while len(result)>1:
        pointer = (pointer+count-1)%len(result)
        result.remove(result[pointer])

    print(f"The relationship between {name_1} and {name_2} is: {result[0]}")

if __name__=="__main__":
    main()