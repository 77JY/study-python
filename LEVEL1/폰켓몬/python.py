from collections import Counter

def solution(poke):
    lists = Counter(poke)
    if len(lists.keys()) > len(poke) // 2:
        return len(poke) // 2
    return len(lists.keys())