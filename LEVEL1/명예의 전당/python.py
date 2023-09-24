def solution(k, score):
    s_list = []
    answer = []
    for i in score:
        s_list.append(i)
        if k < len(s_list):
            s_list.remove(min(s_list))
        answer.append(min(s_list))
    return(answer)