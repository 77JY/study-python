from collections import Counter

def solution(name, yearning, photo):
    result = []
    for i in photo :
        num_sum = 0
        lists = Counter(i)
        for j in range(len(name)):
            num_sum += lists[name[j]] * yearning[j]
        result.append(num_sum)
    return result