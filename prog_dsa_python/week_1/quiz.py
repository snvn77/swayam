# What does f(27182818) return, for the following function definition?
def f(x):
  d=0
  while x > 1:
    (x,d) = (x/2,d+1)
  return(d)
# 25

# What is h(60)-h(45), given the definition of h below?
def h(n):
    s = 0
    for i in range(2,n):
        if n%i == 0:
           s = s+i
    return(s)
# 75

# For what value of n would g(375,n) return 4?
def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m/n)
    return(res)
# 4

# Consider the following function mys:
def mys(m):
    if m == 1:
        return(1)
    else:
        return(m*mys(m-1))

# Which of the following is correct?
#  The function always terminates with mys(n) = factorial of n
#  The function always terminates with mys(n) = 1+2+...+n
#  The function terminates for non-negative n with mys(n) = factorial of n
#  The function terminates for positive n with mys(n) = factorial of n    (Right Answer)