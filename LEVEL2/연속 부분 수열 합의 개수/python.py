def solution(elements):
    number = set()
    elements_list = elements + elements
    for i in range(elements.__len__()):
        for j in range(elements.__len__()):
            number.add(sum(elements_list[j:j+i+1]))
    
    return number.__len__()