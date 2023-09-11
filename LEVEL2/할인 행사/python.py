from collections import Counter

def solution(want, number, discount):
    wishlist= {}
    word = {}
    result = 0
    for i in range(len(want)):
        wishlist[want[i]] = number[i]
        print(wishlist)
    wishlist = Counter(wishlist)
    
    for i in range(len(discount)-9):
        word = discount[i:i+10]
        word = Counter(word)
        if word == wishlist:
            result += 1
    return result