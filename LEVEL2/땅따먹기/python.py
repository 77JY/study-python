def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            land[i][j] += max(land[i-1][j+1:] + land[i-1][:j])
    return max(land[-1])