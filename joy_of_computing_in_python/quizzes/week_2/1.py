# Ravi’s Nested Loop Implementation:

# Ravi is asked to print the following pattern using Python:
# 1
# 22
# 333
# 4444
# 55555

# He knows that a single loop controls the number of lines, so he decides to use nested for loops. Ravi writes the following code: 
for i in range(1,6):
    for j in range(1,i):
        print(i)

# The code runs without errors and prints multiple values on the screen. Ravi assumes that because the inner loop runs multiple times, the digit will automatically appear the required number of times on the same line. However, when the output is observed, the pattern does not match the required format.
# The instructor uses Ravi’s code as a learning case. Learners are expected to analyze how the outer loop controls the number of rows, how the inner loop controls repetition, and why the current placement of the print() statement leads to an incorrect output format.

# How many times does the outer loop execute?
#  4
#  5 (Right Answer)
#  6
#  Depends on the inner loop

# Why does Ravi’s code print each number on a new line instead of the same line?
#  Because print() moves the cursor to the next line by default (Right Answer)
#  Because range() creates new lines.
#  Because the inner loop executes first
#  Because nested loops cannot print patterns 

# Ravi’s program executes without errors but fails to produce the required pattern. Which of the following best explains the cause?
#  The outer loop does not include the final value required for printing the last line
#  The inner loop variable is declared but not explicitly used in the print statement
#  The print statement is placed inside the inner loop instead of after it
#  The inner loop executes one fewer iteration than required for each value of i (Right Answer)

# After correcting the inner loop to execute the required number of times, Ravi observes that the digits are still printed on separate lines. Which change is necessary to ensure that each digit appears on the same line before moving to the next line?
#  Replace print(i) with print() inside the inner loop
#  Move the print(i) statement outside the inner loop
#  Add an empty print() statement at the beginning of the outer loop
#  Modify the print statement to suppress the default newline character (Right Answer)

# In the corrected nested-loop program, why is an additional print() statement required immediately after the inner loop completes?
#  To move the cursor to the next line after printing all digits for the current value of i (Right Answer)
#  To reset the value of the loop variable before the next iteration begins
#  To ensure the inner loop terminates before the outer loop continues
#  To prevent the digits printed in different iterations from overlapping

# Which of the following Python code snippets correctly produces the required output?
# 1
# 22
# 333
# 4444
# 55555
 
for i in range(1,6):
    for j in range(i):
        print(i, end='')
    print()
