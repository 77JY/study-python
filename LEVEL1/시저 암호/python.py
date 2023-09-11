def solution(s, n):
    answer = ""
    for i in s:
        if i != " ":
            text = ord(i) + n
            if (text >= 97 and text <= 122) and (i >= 'a' and i <= 'z'):
                answer += chr(text)
            elif (text >= 65 and text <= 90) and (i >= 'A' and i <= 'Z'):
                answer += chr(text)
            else:
                answer += chr(text - 26)
        else:
            answer += " "
    return answer