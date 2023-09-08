def solution(arr1, arr2):
    answer = [[0 for i in range(arr2[0].__len__())]for _ in range(arr1.__len__()) ]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer
    