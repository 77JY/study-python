def solution(storey):
    answer = 0
    
    while storey:
        num1 = storey % 10
        storey = storey // 10
        if 10 - num1 > 5:
            answer += num1
        else:
            if num1 == 5:
                if 4 < storey % 10:
                    storey += 1
                    answer += 10 - num1
                else:
                    answer += num1
            else:
                storey += 1
                answer += 10 - num1
    return answer
