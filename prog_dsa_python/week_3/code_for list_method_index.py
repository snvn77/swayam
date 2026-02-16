# code for list method '.index()' - index of first occurence of an element

l = [1,2,3,4]

def findpos(l,v):
    for i in range(len(l)):
        if l[i]==v:
            return i
    return -1

a = findpos(l,2)
b = findpos(l,5)
print(a,b)