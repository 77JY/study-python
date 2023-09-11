def gcd(a, b):
    while b != 0:
        n = a % b
        a = b
        b = n
    return a

def solution(n, m):
    return [gcd(n, m), n * m // gcd(n, m)]

# make gcd function

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(n, m):
    return [gcd(n, m), n * m // gcd(n, m)]

# using recursive functions