def solution(n, m, section):
    section.sort()
    answer = 0
    cnt = 0
    for i in section:
        if cnt < i:
            cnt = i + m - 1
            answer += 1
    return(answer)