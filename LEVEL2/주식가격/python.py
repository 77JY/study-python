def solution(prices):
    answer = [0 for i in range(len(prices))]
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[i] < stack[-1][0]:
            _, idx = stack.pop()
            answer[idx] = i - idx
        stack.append([prices[i], i])
    
    for i in stack:
        answer[i[1]] = len(prices) - i[1] - 1
    return answer