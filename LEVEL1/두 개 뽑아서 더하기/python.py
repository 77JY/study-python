def solution(numbers):
    dic = {}
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            dic[numbers[i] + numbers[j]] = 1
    return(sorted(dic))