#세 정수 A,B,C,가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

#1.map을 통해서 3 수를 받도록 하자.
#2.sort하고
#3.거기서 변수[1]을 뽑도록하자.
#4.출력

nus=list(map(int,input('').split(' ')))
nus.sort()
print(nus[1])
