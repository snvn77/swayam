# Write three Python functions as specified below. Paste the text for all three functions together into the submission window. Your function will be called automatically with various inputs and should return values as specified. Do not write commands to read any input or print any output.
# You may define additional auxiliary functions as needed.

# A positive integer m can be expresseed as the sum of three squares if it is of the form p + q + r where p, q, r ≥ 0, and p, q, r are all perfect squares. For instance, 2 can be written as 0+1+1 but 7 cannot be expressed as the sum of three squares. The first numbers that cannot be expressed as the sum of three squares are 7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71, … (see Legendre's three-square theorem).
# Write a Python function threesquares(m) that takes an integer m as input and returns True if m can be expressed as the sum of three squares and False otherwise. (If m is not positive, your function should return False.)

# Here are some examples of how your function should work.
# >>> threesquares(6)
# True
# >>> threesquares(188)
# False
# >>> threesquares(1000)
# True



# Write a function repfree(s) that takes as input a string s and checks whether any character appears more than once. The function should return True if there are no repetitions and False otherwise.

# Here are some examples to show how your function should work.
# >>> repfree("zb%78")
# True
# >>> repfree("(7)(a")
# False
# >>> repfree("a)*(?")
# True
# >>> repfree("abracadabra")
# False



# A list of numbers is said to be a hill if it consists of an ascending sequence followed by a descending sequence, where each of the sequences is of length at least two. Similarly, a list of numbers is said to be a valley if it consists of an descending sequence followed by an ascending sequence. You can assume that consecutive numbers in the input sequence are always different from each other.
# Write a Python function hillvalley(l) that takes a list l of integers and returns True if it is a hill or a valley, and False otherwise.

# Here are some examples to show how your function should work.
# >>> hillvalley([1,2,3,5,4])
# True
# >>> hillvalley([1,2,3,4,5])
# False
# >>> hillvalley([5,4,1,2,3])
# True
# >>> hillvalley([5,4,3,2,1])
# False




# Private Test cases used for evaluation	   Input	                      Expected Output
# Test Case 1	                          threesquares(8)                          True
# Test Case 2                            threesquares(191)                         False
# Test Case 3	                         threesquares(1001)                        True
# Test Case 4	                         threesquares(199)                         False
# Test Case 5	                        repfree("(x+6)[y-5]")                      True
# Test Case 6	                          repfree("expis1")                        True
# Test Case 7	                         repfree("pingpong")                       False
# Test Case 8	                        repfree("95tumblers")                      True
# Test Case 9	                  hillvalley([5,3,2,1,2,3,5,4,3,2,1])              False
# Test Case 10	                          hillvalley([1,2])                        False
# Test Case 11	                           hillvalley([])                          False
# Test Case 12	                  hillvalley([5,4,3,2,1,0,-3,-2,-1])               True




def threesquares(m):
    for i in range((m//2)+1):
        for j in range((m//2)+1):
            for k in range((m//2)+1):
                if m==((i**2)+(j**2)+(k**2)):
                    return True
                else:
                    continue
    return False
  
def repfree(s):
    l = []
    for i in s:
        if i in l:
            return False
        else:
            l = l + [i]
    return True
  
def hillvalley(l):
  
    def hill(l):
        up = 0
        down = 0
        for i in range(1,len(l)):
            if down==0 and l[i] > l[i-1]:
                up+=1
            elif up>=1 and l[i]<l[i-1]:
                down+=1
            else:
                return False
        if down>=1:
            return True
        else:
            return False
    
    def valley(l):
        up = 0
        down = 0
        for i in range(1,len(l)):
            if up==0 and l[i] < l[i-1]:
                down+=1
            elif down>=1 and l[i]>l[i-1]:
                up+=1
            else:
                return False
        if up>=1:
            return True
        else:
            return False
        
    u = hill(l)
    v = valley(l)
    if u or v:
        return True
    else:
        return False