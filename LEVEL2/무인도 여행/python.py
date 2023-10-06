from collections import deque

def solution(maps):
    dy, dx = [1, -1, 0, 0, 0], [0, 0, 1, -1, 0]
    queue = deque()
    answer = []
    column, row = len(maps[0]), len(maps)
    
    for i in range(len(maps)):
        maps[i] = list(map(int, maps[i].replace("X", "0")))

    def bfs():
        cnt = 0
        while queue:
            ny, nx = queue.popleft()
            for i in range(5):
                now_y, now_x = ny + dy[i], nx + dx[i]
                if 0 <= now_y < row and 0 <= now_x < column and maps[now_y][now_x]:
                    cnt += maps[now_y][now_x]
                    maps[now_y][now_x] = 0
                    queue.append([now_y, now_x])
        answer.append(cnt)

    for i in range(row):
        for j in range(column):
            if maps[i][j]:
                queue.append([i, j])
                bfs()
    if answer:
        return sorted(answer)
    return [-1]