import math

def base_N(N, k):
    Num = ""
    while N:
        Num += str(N % k)
        N = N // k
    return reverse_word(Num)

def reverse_word(word):
    reverse_word = ""
    for i in range(len(word)-1, -1, -1):
        reverse_word += word[i]
    return reverse_word

def is_prime_number(N):
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return 0
    return 1

def solution(n, k):
    num_list = base_N(n, k).split("0")
    result = 0
    for i in num_list:
        if '1' < i:
            result += is_prime_number(int(i))
    return result
        