def solution(food):
    word = ""
    for i in range(1, len(food)):
        word += str(i) * (int(food[i]) // 2)
    return word + "0" + word[::-1]