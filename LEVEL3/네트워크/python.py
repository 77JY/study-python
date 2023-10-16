def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if not visited[i]:
            answer += 1
            DFS(n, computers, i, visited)
    return answer

def DFS(n, computers, target, visited):
    visited[target] = True
    for i in range(n):
        if not i == target and computers[target][i]:
            if visited[i] == False:
                DFS(n, computers, i, visited)