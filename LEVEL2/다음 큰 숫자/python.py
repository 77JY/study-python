def solution(n):
    num_bin = bin(n)[2:]
    num_cnt = num_bin.count("1")
    i = n
    while(True):
        i += 1 
        if num_cnt == bin(i)[2:].count("1"):
            return i