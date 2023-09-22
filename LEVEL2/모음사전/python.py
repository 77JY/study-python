from itertools import product

def solution(word):
    wd_list = []
    for i in range(0, 6):
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            wd_list.append(''.join(j))
    wd_list.sort()
    return wd_list.index(word)