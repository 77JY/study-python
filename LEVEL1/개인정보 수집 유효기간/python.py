def solution(today, terms, privacies):
    dic = {}
    result = []
    for i in terms:
        dic[i[0]] = int(i[2:])
    today = list(map(int, today.split(".")))
    today_day = today[0] * 12 * 28 + today[1] * 28 + today[2]
    for i in range(len(privacies)):
        text = list(map(int, privacies[i][:-2].split(".")))
        day = text[0] * 12 * 28 + text[1] * 28 + dic[privacies[i][-1]] * 28 + text[2]
        if day <= today_day :
            result.append(i+1)
    return(result)