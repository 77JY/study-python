import string
from collections import defaultdict

def solution(msg):
    dic = defaultdict(int)
    answer = []
    alphabet = string.ascii_uppercase
    idx = 0
    maxlen = len(msg)
    cnt = 27

    for i in range(len(alphabet)):
        dic[alphabet[i]] = i + 1

    while idx < maxlen:
        word = msg[idx]
        idx += 1

        while idx <= maxlen:

            if idx < maxlen:
                word += msg[idx]
            else :
                answer.append(dic[word])
                break

            if dic[word]:
                idx += 1
            else :
                dic[word] = cnt
                answer.append(dic[word[:-1]])
                cnt += 1
                break
    
    return answer