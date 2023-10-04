def solution(n):
    a, b = 0, 1
    for i in range(n):
        swap = a + b
        a = b
        b = swap
    return b % 1000000007