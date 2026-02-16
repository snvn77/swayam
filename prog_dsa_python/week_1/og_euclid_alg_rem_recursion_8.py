# Original Euclid's Algorithm
'''
Let's say that d is a common factor of both m and n
m = ad and n = bd
if m%n!=0, m = nc + r
ad = c(bd) + r
r = d(a-bc), assuming m>=n
Therefore if d is a common factor of m and n, it will also be a common factor of the reminder (m,n) as well.

Advantage is that if m>n and r will always be less than n
'''

def gcd(m,n):
    if m<n:
        (m,n) = (n,m)
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)