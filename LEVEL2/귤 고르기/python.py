from collections import Counter

def solution(k, tangerine):
    counter = list(Counter(tangerine).values())
    counter.sort(reverse=True)
    num_sum = 0
    for i in range(counter.__len__()):
        num_sum = num_sum + counter[i]
        if k <= num_sum:
            return i + 1