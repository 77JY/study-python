import math


def solution_1(n):
    answer = 0
    for i in list(range(1, n + 1)):
        total = 0
        for num_Cnt in list(range(i, n + 1)):
            total += num_Cnt
            if total == n:
                answer += 1
            elif total > n:
                break
    return answer


def solution_2(n):
    answer = 1 if n % 2 == 1 else 0
    for i in list(range(1, math.floor(n/2) + 1)):
        if n % i == 0 and i % 2 == 1:
            answer = answer + 1
    return answer


number = 105
print("1번째", solution_1(number))
print("2번째", solution_2(number))
