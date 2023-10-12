from collections import deque

def solution(maps):
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    size_y, size_x = len(maps), len(maps[0])
    graph = [[0 for i in range(size_x)] for j in range(size_y)]
    std_y, std_x, end_y, end_x = 0, 0, 0, 0
    queue = deque()

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                std_y, std_x = i, j
            elif maps[i][j] == "E":
                end_y, end_x = i, j
            elif maps[i][j] == "L":
                queue.append([i, j, 0])

    while queue:
        _y, _x, cnt = queue.popleft()
        for i in range(4):
            ny, nx = _y + dy[i], _x + dx[i]
            if 0 <= ny < size_y and 0 <= nx < size_x:
                if maps[ny][nx] != "X" and not graph[ny][nx]:
                    graph[ny][nx] = cnt + 1
                    queue.append([ny, nx, cnt + 1])

    if graph[std_y][std_x] and graph[end_y][end_x]:
        return graph[std_y][std_x] + graph[end_y][end_x]
    else:
        return -1