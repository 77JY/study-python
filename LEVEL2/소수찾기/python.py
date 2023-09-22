from itertools import *
from collections import Counter

def num_cases(numbers):
    dic = {}
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            word = int(''.join(j))

            if j[0] != '0' and not dic.get(word):
                dic[word] = 1
    return dic

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    dic = num_cases(numbers)
    print(len(dic))
    for i in dic.keys():
        if i < 2:
            continue
        check = True
        for j in range(2, int(i**0.5) +1):
            if i % j == 0:
                check = False
                break
        if check:
            answer = answer + 1
    return(answer)

""" 
from itertools import *
from collections import Counter
import math

def num_cases(numbers):
    dic = {}
    
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            word = int(''.join(j))

            if j[0] != '0' and not dic.get(word):
                dic[word] = 1
    return dic

def is_Prime_Number(Prime_list, nums):
    for i in range(2, nums+1):
        for j in range(i * 2, len(Prime_list), i):
            if Prime_list[j] == True:
                Prime_list[j] = False
    return Prime_list

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    dic = num_cases(numbers)
    Prime_list = [True for i in range(max(dic.keys()) + 1)]
    Prime_list = is_Prime_Number(Prime_list, int(math.sqrt(max(dic))))
    
    for i in dic.keys():
        if 1 < i and Prime_list[i] == True:
            answer = answer + 1
    return(answer) 

"""