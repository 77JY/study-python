def solution(arr, divisor):
    arr.sort()
    num_arr = []
    for i in arr:
        if i % divisor == 0:
            num_arr.append(i)
    if num_arr == []:
        return [-1]
    return num_arr