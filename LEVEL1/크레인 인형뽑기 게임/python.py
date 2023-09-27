def solution(board, moves):
    answer = 0
    stack = []
    answer = 0
    for i in moves:
        cnt = 0
        while cnt < len(board[0]):
            if board[cnt][i - 1]:
                if stack and stack[-1] == board[cnt][i - 1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[cnt][i - 1])
                board[cnt][i - 1] = 0
                break
            cnt += 1
    return answer