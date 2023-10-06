def solution(sequence, k):
    left = 0
    right = 0
    num_sum = sequence[0]
    answer = []
    
    while True:
        if num_sum == k:
            if answer and answer[1] - answer[0] <= right - left:
                None
            else:
                answer = [left, right]
        if k <= num_sum:
            num_sum -= sequence[left]
            left += 1
        elif right < len(sequence) - 1:
            right += 1
            num_sum += sequence[right]
        else:
            break
    return answer