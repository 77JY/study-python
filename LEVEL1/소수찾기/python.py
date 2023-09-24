import math

def solution(n):
    number_list = [False for i in range(n + 1)]
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if not number_list[i]:
            for j in range(i * 2, n + 1, i):
                number_list[j] = True
    return(number_list[2:].count(False))