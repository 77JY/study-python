answer = 0
length = 0

def dfs(cnt, num_sum, numbers, target):
    global answer
    if num_sum == target and length == cnt:
        answer = answer + 1
    
    if length == cnt:
        return
    dfs(cnt+1, num_sum + numbers[cnt], numbers, target)
    dfs(cnt+1, num_sum - numbers[cnt], numbers, target)

def solution(numbers, target):
    global length
    length = len(numbers)
    dfs(0, 0, numbers, target)
    return answer