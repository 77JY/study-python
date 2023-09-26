def solution(s, skip, index):
    dic = {}
    for i in skip:
        dic[ord(i)] = 1
    answer = ""
    for i in range(len(s)):
        wd = ord(s[i])
        for j in range(index):
            wd += 1
            if 122 < wd:
                wd -= 26
            while dic.get(wd):
                wd += 1
                if 122 < wd:
                    wd -= 26
        answer += chr(wd)
    return(answer)