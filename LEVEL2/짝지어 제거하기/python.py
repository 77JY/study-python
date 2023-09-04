def solution(s):
    str_list = []
    for i in s:
        str_list.append(i)
        if str_list.__len__() >= 2 and str_list[-1] == str_list[-2]:
            del str_list[-1]
            del str_list[-1]
    if str_list.__len__() == 0:
        return 1
    return 0