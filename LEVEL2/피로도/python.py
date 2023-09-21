answer = 0

def DFS(cnt, visited, k, dungeons):
    global answer
    answer = max(cnt, answer)
    
    for i in range(len(dungeons)):
        if visited[i] == 0 and dungeons[i][0] <= k:
            visited[i] = 1
            DFS(cnt + 1, visited, k - dungeons[i][1], dungeons)
            visited[i] = 0

def solution(k, dungeons):
    visited = [0] * len(dungeons)
    DFS(0, visited, k, dungeons)
    return answer