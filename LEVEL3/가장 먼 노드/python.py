from collections import deque

def solution(n, edge):
    graph = [[] for i in range(n + 1)]
    visited = [0 for i in range(n + 1)]
    visited[1] = 1
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    vertex = deque([1])
    while vertex:
        idx = vertex.popleft()
        for i in graph[idx]:
            if visited[i] == 0:
                visited[i] = visited[idx] + 1
                vertex.append(i)
                
    return(visited.count(max(visited)))