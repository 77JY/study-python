def solution(n, lost, reserve):
    lost_list = set(lost) - set(reserve)
    reserve_list = set(reserve) - set(lost)
    for i in reserve_list:
        if i-1 in lost_list:
            lost_list.remove(i-1)
        elif i+1 in lost_list:
            lost_list.remove(i+1)
    return n - len(lost_list)