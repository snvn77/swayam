# Naive GCD improved no list scanned backwards with while loop
def gcd(m,n):
    i = min(m,n)
    while i > 0:
        if m%i==0 and n%i==0:
            return i
        else:
            i-=1