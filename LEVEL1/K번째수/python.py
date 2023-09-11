def solution(array, commands):
    arr = []
    for i in range(len(commands)):
        text = sorted(array[commands[i][0]-1 : commands[i][1]])
        arr += [text[commands[i][2] - 1]] 
    return (arr)


""" def solution(array, commands):
    text = []
    for i in range(len(commands)):
        text += [sorted(array[commands[i][0]-1 : commands[i][1]])[commands[i][2] - 1]]
    return text 

한줄 줄이기
"""