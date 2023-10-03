from collections import Counter, defaultdict

def solution(topping):
    Cheolsu = Counter(topping)
    Younghee = defaultdict(int)
    idx = 0
    answer = 0

    while len(Younghee) <= len(Cheolsu):
        cakes = topping[idx]
        idx += 1
        Cheolsu[cakes] -= 1
        Younghee[cakes] += 1

        if Cheolsu[cakes] == 0:
            del Cheolsu[cakes]

        if len(Younghee) == len(Cheolsu):
            answer += 1
    return answer