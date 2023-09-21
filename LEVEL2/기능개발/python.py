import math

def solution(progresses, speeds):
    idx = math.ceil(100 / speeds[0] - progresses[0] / speeds[0])
    cnt = 1
    answer = []
    for i in range(1, len(progresses)):
        now = math.ceil(100 / speeds[i] - progresses[i] / speeds[i])
        print(now)
        if idx < now:
            answer.append(cnt)
            idx = now
            cnt = 1
        else :
            cnt += 1
    answer.append(cnt)
    return answer