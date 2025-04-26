jumin = "990229-1234567"
print("성별 식별번호 : ", jumin[7]) # 인덱스는 0부터 시작
print("범위 식별번호 :", jumin[3:7])
print("식별번호 : ", jumin[:]) # 전체

test = 'abcde'
print(test.lower())
print(test.upper())
print(len(test))

print("문자열 %d살" % 34)

num = 10
text = "테스트"
print(f"나는 {num} 살이고, {text} 입니다.") # f붙이고 대입가능
print("백문이\n불여일타")

exam = "the early bird catches the worm."
print(exam[0].upper() + exam[1:len(exam)])