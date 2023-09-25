def solution(N, stages):
    dic = {i:0 for i in range(1, N + 1)}
    lists = []
    nums = 0
    for i in stages:
        if i <= N:
            dic[i] +=1
        else:
            nums += 1
    for i in range(N , 0 , -1):
        nums += dic[i]
        if dic[i]:
            dic[i] = dic[i] / nums
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(dic)
    for i, j in dic:
        lists.append(i)
    return(lists)