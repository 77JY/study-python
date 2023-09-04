def solution(s):
    num_cnt = 0
    while_cnt = 0

    while s.__len__() > 1:
        while_cnt = while_cnt + 1
        num_cnt = num_cnt + s.count('0')
        s.replace('0', '')
        s = bin(s.count('1'))[2:]
    return ([while_cnt, num_cnt])


print(solution("110010101001"))
