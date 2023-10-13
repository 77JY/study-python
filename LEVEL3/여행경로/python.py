from collections import defaultdict
import copy
answer = []

def dfs(dicts, cnt, airline, flag):
    global answer

    if cnt == flag and not answer:
        answer = airline
    if not answer:
        for i in dicts[airline[-1]]:
            airlines = airline + [i]
            dic = copy.deepcopy(dicts)
            dic[airline[-1]].remove(i)
            dfs(dic, cnt + 1, airlines, flag)

def solution(tickets):
    dic = defaultdict(list)
    tickets.sort(key=lambda x:x[1])
    for i in tickets:
        dic[i[0]].append(i[1])
    dfs(dic, 0, ["ICN"], len(tickets))
    return answer