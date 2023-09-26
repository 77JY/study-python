def solution(keymap, targets):
    dic = {}
    answer = []
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            wd = keymap[i][j]
            if dic.get(wd) != None:
                if j < dic[wd]:
                    dic[wd] = j
            else:
                dic[wd] = j

    for i in targets:
        num = 0
        for j in i:
            if dic.get(j) == None:
                num = -1
                break
            else :
                num += dic[j] + 1
        answer.append(num)
    return(answer)