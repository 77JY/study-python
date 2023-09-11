def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        result += [bin(arr1[i] | arr2[i])[2:].zfill(n).replace('0', ' ').replace('1','#')]
    return result