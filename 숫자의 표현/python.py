def solution(n):
    answer = 0
    i = 1
    while i + i + 1 <= n:
        num_sum = 0
        j = i
        while num_sum < n:
            num_sum = num_sum + j
            if num_sum == n:
                answer = answer + 1
            j = j + 1
        i = i + 1
    return answer + 1
