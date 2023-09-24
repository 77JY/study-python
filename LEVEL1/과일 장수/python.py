def solution(k, m, score):
    apple_box = [0 for i in range(k + 1)]
    result = 0
    apple = 0

    for i in score:
        apple_box[i] += 1

    for i in range(k, 0, -1):
        apple += apple_box[i]
        if m <= apple:
            result += (apple // m) * i * m
            apple = apple % m

    return(result)