from collections import deque

def bfs(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    
    while queue:
        begin, trance_cnt = queue.popleft()
        
        if begin == target:
            return trance_cnt
        
        for word in words:
            count = 0
            for i in range(len(begin)):
                if begin[i] != word[i]:
                    count += 1
            if count == 1:
                queue.append([word, trance_cnt + 1])
    
    

def solution(begin, target, words):
    if target in words:
        cnt = bfs(begin, target, words)
        if cnt:
            return cnt
    return 0