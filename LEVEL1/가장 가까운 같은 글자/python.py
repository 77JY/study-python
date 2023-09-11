def solution(s):
    answer = ""
    result = []
    for i in range(len(s)):
        if answer.rfind(s[i]) == -1 :
            result += [-1]
        else :
            result += [int(i - answer.rfind(s[i]))]
        answer +=s[i]

    return result