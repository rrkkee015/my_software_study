# 다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아
# 이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.
import math

lis=input('').split(', ')
lis=list(map(int,lis))
result = [round(3.141592*a*2, 2) for a in lis]
for i in result:
    if i != result[-1]:
        print(i,end=', ')
    else:
        print(i)
