from heapq import *

def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while scoville[0] < K and 1 < len(scoville):
        num1 = heappop(scoville)
        num2 = heappop(scoville)
        heappush(scoville, num1 + num2 * 2)
        cnt = cnt + 1
    if scoville[0] < K:
        return -1
    return cnt