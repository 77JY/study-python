def solution(survey, choices):
    dic = {'RT':0, 'CF':0, 'JM':0, 'AN':0}
    answer = ""
    for i,j in zip(survey,choices):
        if i in dic.keys():
            dic[i] -= j - 4
        else :
            wd = i[-1]+i[0]
            dic[wd] += j - 4
    for i,j in dic.items():
        if 0 <= j:
            answer += i[0]
        else:
            answer += i[-1]
    return(answer)