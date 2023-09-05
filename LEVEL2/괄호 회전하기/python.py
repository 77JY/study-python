def solution(str_list):
    result = 0
    for i in range(str_list.__len__()):
        stack = []
        for j in range(i, str_list.__len__()):
            if stack == []:
                stack += str_list[j]
            elif stack[-1] == "[" and str_list[j] == "]":
                stack.pop(-1)
            elif stack[-1] == "(" and str_list[j] == ")":
                stack.pop(-1)
            elif stack[-1] == "{" and str_list[j] == "}":
                stack.pop(-1)
            elif stack[-1] == "}" or stack[-1] == ")" or stack[-1] == "]":
                break
            else:
                stack += str_list[j]
        if stack == []:
            result = result + 1
        str_list = str_list + str_list[i]
    return result