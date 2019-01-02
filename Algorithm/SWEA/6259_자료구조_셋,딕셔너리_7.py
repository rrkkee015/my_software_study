#다음과 같이 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성하십시오.
#입력 hello world! 123
#출력 LETTERS 10
#     DIGITS 3

#1. 우선 입력을 받을 변수를 만든다.
#2. for문으로 하나씩 돌리면서 숫자인지 문자인지 판별한다. (isdigit)을 사용

sen = "hello world! 123"
DIGITS = 0
LETTERS = 0
for i in sen:
    if i.isdigit():
        DIGITS += 1
    elif i.isalpha():
        LETTERS += 1
print("LETTERS {}\nDIGITS {}".format(LETTERS,DIGITS))
