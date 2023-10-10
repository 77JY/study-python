from collections import Counter

def solution(weights):
    count = Counter(weights)
    result = 0
    for i in count:
        result += count[i] * (count[i] - 1) // 2 
        result += count[i * 2] * count[i]
        result += count[i * 3 / 2] * count[i]
        result += count[i * 4 / 3] * count[i]
    return result