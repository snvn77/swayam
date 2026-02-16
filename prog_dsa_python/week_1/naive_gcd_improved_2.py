# Naive GCD algorithm improved
def gcd(m,n):
    fc = []
    for i in range(1, min(m,n)+1):
        if (m%i)==0 and (n%i)==0:
            fc.append(i)
    return fc[-1]