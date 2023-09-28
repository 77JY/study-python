from collections import deque

def solution(cacheSize, cities):
    cashe_box = deque(maxlen=cacheSize)
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    
    for i in cities:
        city = i.lower()
        if city in cashe_box:
            cashe_box.remove(city)
            cashe_box.append(city)
            answer += 1
        else :
            cashe_box.append(city)
            answer += 5

    return answer


""" from collections import deque

def solution(cacheSize, cities):
    cashe_box = deque()
    answer = 0

    if cacheSize == 0:
        return len(cities) * 5
    
    for i in cities:
        wd = i.lower()
        if wd in cashe_box:
            cashe_box.remove(wd)
            cashe_box.append(wd)
            answer += 1
        else:
            cashe_box.append(wd)
            answer += 5

        if cacheSize < len(cashe_box):
            cashe_box.popleft()

    return(answer) 
"""