def solution(n,a,b):
    answer = 1
    while True:
        if a % 2:
            a += 1
        if b % 2:
            b += 1
        a = a // 2
        b = b // 2
        if a == b :
            return answer
        answer += 1