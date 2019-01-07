#숫자 a,b가 주어졌을 때 a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력해보세요.
a, b = map(int, input().split(' '))
print("{} {}".format(a//b, a%b))

#더 간단한 방법이 있다.
a,b = map(int, input().split(' '))
print(*divmod(a, b))
