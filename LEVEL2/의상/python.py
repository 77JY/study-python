from collections import Counter

def solution(clothes):
    c_list = []
    answer = 1

    for i in clothes:
        c_list += [i[1]]
    c_list = Counter(c_list)

    for i in c_list.values():
        answer *= i + 1
        
    
    return answer-1