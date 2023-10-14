def solution(n):
    dicts = {0 : "4", 1 : "1", 2 : "2"}
    answer = ""
    while n:
        num = n % 3
        if num == 0:
            n -= 1
        answer += dicts[num]
        n = n // 3
    return answer[::-1]