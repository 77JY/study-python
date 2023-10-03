from collections import deque 

def solution(priorities, location):
    num_list = deque(sorted(priorities, reverse=True))
    priorities = deque(priorities)
    answer = 0
    while priorities:
        idx = priorities.popleft()

        if idx == num_list[0]:
            num_list.popleft()
            answer += 1
            if location == 0:
                return answer
        else :
            priorities.append(idx)
            if location == 0:
                location = len(priorities)
        location -= 1