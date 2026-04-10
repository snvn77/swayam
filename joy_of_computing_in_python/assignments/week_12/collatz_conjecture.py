# Collatz Conjecture 

def check_num(n):
    iterations=0
    while n>1:
        if n%2==0:
            n //= 2
        else:
            n = 3*n + 1
        iterations+=1

    print(n,iterations)

check_num(256)
