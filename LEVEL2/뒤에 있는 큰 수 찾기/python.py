def solution(num):
    answer = [-1 for i in range(len(num))]
    stack = []
    for i in range(len(num)):
        while stack and num[stack[-1]] < num[i]:
            answer[stack.pop()] = num[i]
        stack.append(i)
    return(answer)