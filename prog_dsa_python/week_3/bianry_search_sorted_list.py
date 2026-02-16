# Binary search for a sorted list/array - does not  matter if the seq ia an array or a list

def bsearchn(seq, v): #Naive
    for i in range(len(seq)):
        if seq[i]==v:
            return i
    return -1


def bsearch(seq,v):
    low = 0
    high = len(seq)-1
    while low<=high:
        mid = (low+high)//2
        if seq[mid]==v:
            return mid
        elif v>seq[mid]:
            low = mid+1
        else:
            high = mid-1
    return -1

# Basic
a = bsearch([1,2,3,4,5], 3)# 2
b = bsearch([10,20,30], 10)# 0
c = bsearch([10,20,30], 30)# 2
d = bsearch([1,3,5,7], 4)# -1

# Edge
e = bsearch([], 5)# -1
f = bsearch([10], 10)# 0
g = bsearch([10], 5)# -1

# Two elements
h = bsearch([1,2], 1)# 0
i = bsearch([1,2], 2)# 1
j = bsearch([1,2], 3)# -1

# Range
k = bsearch([10,20,30], 5)# -1
l = bsearch([10,20,30], 40)# -1

# Negatives
m = bsearch([-10,-5,0,5,10], -10)# 0
n = bsearch([-10,-5,0,5,10], 0)# 2
o = bsearch([-10,-5,0,5,10], 7)# -1

# Duplicates
p = bsearch([1,2,2,2,3], 2)# any_of_[1,2,3]

print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)