#다음과 같이 사용자가 입력한 문장에서 대소문을 구별해 각각의 갯수를 출력하는 프로그램을 작성하십시오.
#입력
#Hello World! 123
#출력
#UPPER CASE 2
#LOWER CASE 8

#1. Hello World! 123을 담을 변수를 만든다.
#2. for문으로 돌면서 upper과 lower을 구분한다.
#3. 출력한다.

sen = "Hello World! 123"
UPPER_CASE = 0
LOWER_CASE = 0
for i in sen:
    if i.isupper():
        UPPER_CASE += 1
    elif i.islower():
        LOWER_CASE += 1
print("UPPER CASE {}\nLOWER CASE {}".format(UPPER_CASE,LOWER_CASE))
