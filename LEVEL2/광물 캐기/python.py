import math

def solution(picks, minerals):
    mineral = {"diamond" : 25, "iron" : 5, "stone" : 1}
    lists = [[] for i in range(math.ceil(len(minerals) / 5))]
    answer = 0
    
    for i in range(len(minerals)):
        if sum(picks) <= i//5:
            break
        lists[i//5].append(mineral[minerals[i]])
    lists.sort(key=sum)

    for i in range(len(picks)):
        nums = 25 // (5 ** i)
        while picks[i] and lists:
            picks[i] -= 1
            for j in lists[-1]:
                if 0 < j // nums:
                    answer += j // nums
                else:
                    answer += 1
            lists.pop()
    return answer