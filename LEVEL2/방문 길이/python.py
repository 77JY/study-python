from collections import defaultdict

def solution(dirs):
    answer = 0
    flag = [5, 5]
    dic = defaultdict(str)
    
    for i in dirs:
        if i == "U" and 0 < flag[0]:
            flag[0] -= 1
            dic[flag[1], flag[0]] += "U"
        elif i == "D" and flag[0] < 10:
            dic[flag[1], flag[0]] += "U"
            flag[0] += 1
        elif i == "L" and 0 < flag[1]:
            flag[1] -= 1
            dic[flag[1], flag[0]] += "R"
        elif i == "R" and flag[1] < 10:
            dic[flag[1], flag[0]] += "R"
            flag[1] += 1

    for i in dic.values():
        answer += len(set(list(i)))
    return answer