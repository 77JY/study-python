from collections import deque

def solution(maps):
    len_X = len(maps[0])
    len_Y = len(maps)
    visited = [[False] * len_X for i in range(len_Y)]
    nX, nY = [-1, 1, 0, 0],[0, 0, -1, 1]
    deq = deque([(0, 0)])
    while(deq):
        y, x =deq.popleft()
        for i in range(4):
            now_Y = y + nY[i]
            now_X = x + nX[i]
            if 0 <= now_X < len_X and 0 <= now_Y < len_Y and maps[now_Y][now_X] == 1:
                if not visited[now_Y][now_X]:
                    maps[now_Y][now_X] = maps[y][x] + 1
                    visited[y][x] = True
                    deq.append((now_Y, now_X))
    if maps[-1][-1] == 1:
        return -1
    return(maps[-1][-1])