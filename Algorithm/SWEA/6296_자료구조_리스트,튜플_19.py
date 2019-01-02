# 단어를 콤마(,)로 구분해 입력하면 그 단어들을 사전순으로 정렬해 출력하는 프로그램을 작성하시오.

# 1. input 받는 변수를 만든다.
# 2. sort를 이용한다.
# 3. 출력한다.

lis = input('').split(', ')
lis.sort()
for i in lis:
    if i != lis[-1]:
        print(i,end=', ')
    else:
        print(i)
