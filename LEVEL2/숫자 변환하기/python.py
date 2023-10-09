def solution(x, y, n):
    answer = 0
    stack = [x]
    while stack:
        nums = set()
        if y in stack:
            return answer
        for i in stack:
            if i * 3 <= y:
                nums.add(i * 3)
            if i * 2 <= y:
                nums.add(i * 2)
            if i + n <= y:
                nums.add(i + n)
        stack = nums
        answer += 1
    return -1
    