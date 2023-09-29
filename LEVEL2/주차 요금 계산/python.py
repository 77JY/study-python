from collections import defaultdict
import math

def solution(fees, records):
    answer = defaultdict(int)

    for i in records:
        time, car_num, state = i.split()
        time = list(map(int, time.split(":")))
        
        if state == "IN":
            answer[car_num] -= time[0] * 60 + time[1]
        else :
            answer[car_num] += time[0] * 60 + time[1]

    for i, j in answer.items():
        if j < 1:
            answer[i] += 23 * 60 + 59
        answer[i] -= fees[0]
    
    for i, j in answer.items():
        if 0 < j:
            answer[i] = fees[1] + fees[3] * math.ceil(j / fees[2])
        else:
            answer[i] = fees[1]

    return(list(map(lambda x: x[1],sorted(answer.items(), key=lambda x: x[0]))))