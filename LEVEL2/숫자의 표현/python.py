# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
text = input()
text_area = ""
for i in range(2, text.__len__()+1, 2):
	# print(text[i-2:i])
	asci = ord(text[i-2]) + int(text[i-1]) * int(text[i-1])
	print(asci)
	print("a아스키",ord("a"),"z아스키코드",ord("z"))
	if int(text[i-1]) * int(text[i-1]) > 25:
		text_area.append(chr(ord(text[i-2] + (int(text[i-1]) * int(text[i-1]) % 26))))
	else :
		text_area.append(chr(ord(text[i-2] + (int(text[i-1]) * int(text[i-1])))))


+ (text[i-1] * text[i-1] % 26)
+ text[i-1] * text[i-1]