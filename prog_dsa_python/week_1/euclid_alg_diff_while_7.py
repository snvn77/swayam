# Euclid's Algorithm
'''
Let's say that d is a common factor of both m and n
m = ad and n = bd
m-n = d(a-b) assuming m>=n
Therefore if d is a common factor of m and n, it will also be a common factor of the difference m-n as well.

But the drawback is that for some problems like gcd(101,2), it will take around 50 iterations to complete.
'''

def gcd(m,n):
    if m<n:
        (m,n) = (n,m)
    while m%n!=0:
        (m,n) = (max(n,m-n), min(n,m-n))
    return n