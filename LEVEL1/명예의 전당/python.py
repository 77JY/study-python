def solution(k, score):
    s_list = []
    answer = []
    for i in score:
        s_list.append(i)
        min_num = min(s_list)
        if k < len(s_list):
            s_list.remove(min_num)
        answer.append(min(s_list))
    return(answer)