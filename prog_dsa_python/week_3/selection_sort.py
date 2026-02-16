# Selection sort

def selectionsort(l):
    for i in range(len(l)):
        min_pos = i
        for j in range(min_pos, len(l)):
            if l[min_pos] > l[j]:
                min_pos = j
        l[min_pos], l[i] = l[i], l[min_pos]

    return l

l = list(range(1000,0,-1))
a=selectionsort(l)
print(a)