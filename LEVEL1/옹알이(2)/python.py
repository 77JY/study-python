def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ["aya", "ye", "woo", "ma"]:
            if j * 2 not in i:
                i = i.replace(j, " ")
        if i.strip() == "":
            answer+=1
    return answer

""" ㅋㅋㅋ
def solution(babbling):
    answer = 0
    for i in babbling:
        cnt = 0
        double_ck = 0
        double_ck += i.count("mama") * 2
        double_ck += i.count("yeye") * 2
        double_ck += i.count("ayaaya") * 3
        double_ck += i.count("woowoo") * 3
        if double_ck:
            continue
        cnt += i.count("ma") * 2
        cnt += i.count("ye") * 2
        cnt += i.count("aya") * 3
        cnt += i.count("woo") * 3
        if len(i) == cnt:
            answer += 1
    return answer 
"""