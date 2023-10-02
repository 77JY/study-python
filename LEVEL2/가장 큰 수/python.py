def solution(numbers):
    str_num = list(map(str, numbers))
    str_num.sort(key=lambda x : x * 3, reverse=True)
    answer = ''.join(str_num)
    if answer[0] == "0":
        return "0"
    return answer