#다음 결과와 같이 문자열을 입력하면 짝수 인덱스를 가진 문자들을 출력하는 프로그램을 작성하십시오.
# 입력 : H1e2l3l4o5w6o7r8l9d
# 출력 : Helloworld

#1. 입력 받는 놈 만들고
#2. while로 하자, if문으로 짝수 인덱스만 뽑도록하자
#3. 끝

let = input('')
i=0
while i < len(let):
    if i % 2 ==0:
        print(let[i],end='')
    i += 1
