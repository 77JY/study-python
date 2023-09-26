def solution(s):
    word_A = 1
    word_B = 0
    answer = 0
    wd = ""
    for i in s:
        if wd == "":
            wd = i
            word_A = 1
            word_B = 0
            continue
        else:
            if i == wd:
                word_A += 1
            else :
                word_B += 1
        if word_A == word_B:
            wd = ""
            answer += 1
    if len(wd) == 1:
        return answer + 1
    return answer