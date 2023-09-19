from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    lists = deque(goal)
    for i in goal:
        if cards1 and cards1[0] == i:
            cards1.popleft()
            lists.popleft()
        elif cards2 and cards2[0] == i:
            cards2.popleft()
            lists.popleft()
        else:
            break
    if lists:
        return "No"
    return "Yes"