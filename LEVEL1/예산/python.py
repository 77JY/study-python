def solution(d, wallet):
    count = 0
    d.sort()
    for price in d:
        if wallet - price < 0:
            return count
        wallet = wallet - price
        count = count + 1
    return count
        