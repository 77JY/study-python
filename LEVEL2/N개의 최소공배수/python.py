import math

def solution(arr):
    result = arr[0]
    for i in arr:
        result = (i * result) // math.gcd(i,result)
    return result