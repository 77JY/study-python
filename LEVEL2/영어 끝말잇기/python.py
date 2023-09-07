def solution(n, words):
    answer = [0,0]

    for i in range(1, words.__len__()):
        if words[i-1][-1] != words[i][0]:
            return [(i % n) +1, int((i + n) / n)]
        # for i in range(0, words[0:i-1].__len__()):
        #     print(i,"들어감")
        if words[0:i-1].count(words[i]):
            return [(i% n) +1 % n, int((i + n) /n)]
    return answer