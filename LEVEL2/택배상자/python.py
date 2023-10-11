def solution(order):
    box = []
    idx = 0
    answer = 0
    
    for i in range(1, len(order) + 1):
        box.append(i)
        while box and box[-1] == order[idx]:
            answer += 1
            box.pop()
            idx += 1
    return answer