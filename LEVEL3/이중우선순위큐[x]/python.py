def solution(operations):
    lists = []
    for i in operations:
        if i != "D 1" and i != "D -1":
            lists += [int(i[2:])]
        elif i == "D 1" and len(lists):
            lists.pop(lists.index(max(lists)))
        elif i == "D -1" and len(lists):
            lists.pop(lists.index(min(lists)))
    if lists == []:
        return [0, 0]
    
    return max(lists), min(lists)
