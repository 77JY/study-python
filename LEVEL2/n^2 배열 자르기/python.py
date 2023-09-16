def solution(n, left, right):
    left_n = left // n+1
    right_n = right // n+2
    num_list = list(range(1, n+1))
    answer = []
    for i in range(left_n, right_n):
        answer += [i] * i 
        answer += num_list[i:]
    last = 1 + right - ((left // n) * n )
    if last == 0:
        return answer[left % n:]
    return(answer[left % n: last])