import math


def solution_1(n):
    answer = 0
    for i in list(range(1, n + 1)):
        total = 0
        for num_Cnt in list(range(i, n + 1)):
            total += num_Cnt
            if total == n:
                answer += 1
            elif total > n:
                break
    return answer


def solution_2(n):
    answer = 1 if n % 2 == 1 else 0
    for i in list(range(1, math.floor(n/2) + 1)):
        if n % i == 0 and i % 2 == 1:
            answer = answer + 1
    return answer


number = 105
print("1번째", solution_1(number))
print("2번째", solution_2(number))

""" 
첫번째 방식은 그나마 알아는 볼 수 있게 만들어 볼려고 시도한 방식 [내가 처음에 만들어볼려 했던 방식에서 조금더 느리지만 이해는 할수있게 만들어 본 방식]
두번째 방식은 무엇을 하는지 알순있으나 왜그렇게 하는지 이해하긴 힘들어도 동작은 빠르게 만들어본 방식 [남의 코드를 보며 이해하고 나름 개조한 방식]
 """
