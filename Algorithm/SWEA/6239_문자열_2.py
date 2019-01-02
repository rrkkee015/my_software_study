# 다음과 같이 문장을 구성하는 단어를 역순으로 출력하는 프로그램을 작성하십시오.
# 입력 : A better tomorrow
# 출력 : tomorrow better A

# 1. 입력 받을 input 변수를 만들어보자
# 2. 문장을 split으로 쪼개고 뒤집고 str로 출력하자

lett = input("")
lis = lett.split(" ")
lis.reverse()
for i in lis:
    print(i, end= " ")
