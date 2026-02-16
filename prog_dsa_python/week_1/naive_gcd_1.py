# Naive GCD algorithm
def gcd(m,n):
    # List the factors of m
    fm = []
    for i in range(1,m+n):
        if m%i==0:
            fm.append(i)
    # List the factors of n
    fn = []
    for i in range(1,n+1):
        if n%i==0:
            fn.append(i)
    # List the common factors
    fc = []
    for i in fm:
        if i in fn:
            fc.append(i)
    # Return the largest common factor
    return fc[-1]


