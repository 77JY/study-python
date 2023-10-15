import math

def solution(n, k):
    lists = [i for i in range(1, n + 1)]
    answer = []

    while lists:
        n -= 1
        idx = (k - 1) // math.factorial(n)
        answer.append(lists.pop(idx))
        k = k % math.factorial(n)
    return answer