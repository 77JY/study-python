from collections import Counter

def solution(s):
    s = s.replace("}","").replace("{","").split(",")
    lists = Counter(s)
    result = []
    for i in lists.most_common():
        result.append(int(i[0]))
    return result