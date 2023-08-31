import math

nums = list(map(int, (input().split())))
numline = list(map(int, (input().split())))
result = 0


if nums[0] < numline.__len__():
    numline = numline[:nums[0]]
min_num = numline.__len__() - numline.count(min(numline)) + 1
result = math.floor(min_num / (nums[1] - 1))
if min_num % (nums[1]-1) > 1:
    result += 1
if nums[1] == 2:
    result -= 1
print(result)
