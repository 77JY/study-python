def solution(n, s):
    if n > s:
        return [-1]
    answer = [s // n] * (n - s % n)
    answer += [s // n + 1] * (s % n)
    return answer