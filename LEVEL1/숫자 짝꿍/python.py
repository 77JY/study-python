from collections import defaultdict

def solution(X, Y):
    base = defaultdict(int)
    dic = {}
    answer = ""
    for i in X:
        base[i] += 1

    for i, j in sorted(base.items(), key=lambda x: x[0], reverse=True):
        dic[i] = 0

    for i in Y:
        if dic.get(i) != None:
            dic[i] += 1

    for i, j in dic.items():
        if base[i] < j:
            answer += i * base[i]
            continue
        answer += i * j
    if answer == "":
        return "-1"
    elif answer[0] == "0":
        return "0"
    return answer