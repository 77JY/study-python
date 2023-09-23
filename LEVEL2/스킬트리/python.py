from collections import Counter

def solution(skill, skill_trees):
    dic = {}
    answer = 0
    for i in range(len(skill)):
        dic[skill[i]] = i

    for i in range(len(skill_trees)):
        stat = 0
        for N in range(len(skill_trees[i])):
            if dic.get(skill_trees[i][N]) == stat:
                stat = stat + 1
            elif dic.get(skill_trees[i][N]) and dic.get(skill_trees[i][N]) != stat:
                stat = -1
                break

        if stat != -1:
            answer = answer + 1
    return answer