#base 진법으로 표기된 숫자를 10진법 숫자로 출력해보세요.
#입력 :
#입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
#첫 번째 숫자는 'num'을 나타내며, 두 번째 숫자는 'base'를 나타냅니다.

num, base = map(int, input().split(' '))
li = []
count = 1
for i in str(num):
    li.append(int(i)*base**(len(str(num))-count))
    count += 1
print(sum(li))

#더 쉬운 방법
num = '3212' #문자열로 해야함
base = 5
answer = int(num, base) #int(값, 진수) 10진수가 생략되어 있다고 생각하면 된다. base 진수로 표현된 값을 10진수로 바꿔준다.
