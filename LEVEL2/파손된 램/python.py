count = int(input())
rem_list = list(map(int, input().split()))
result = 0
error_remlist = []

for i in range(count):
    if (rem_list[i] & (rem_list[i]-1)) != 0:
        result = result + 1
        error_remlist.append(i+1)

print(result)
for i in range(result):
    print(error_remlist[i], end=' ')
