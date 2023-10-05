from collections import defaultdict

def solution(n, results):
    win = defaultdict(set)
    lose = defaultdict(set)
    answer = 0

    for N, M in results:
        win[N].add(M)
        lose[M].add(N)
    
    for i in range(1, n + 1):
        for winner in win[i]:
            lose[winner].update(lose[i])
        for loser in lose[i]:
            win[loser].update(win[i])
    
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer