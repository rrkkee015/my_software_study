## 파이썬

-  a=[1,2,3,4,5 ....]

  이처럼 끝을 알기 어려운 리스트가 있다면 a[-1]이 마지막 인덱스이다.

- a=[1,2,3,4,5,6]

  for i in a:

  ​	print(i)

  위에를 출력하면

  1

  2

  3

  4

  5

  6

  이렇게 나오는데

  for i in a:

  ​	print(i,end='') # end =''를 추가하면

  123456 이렇게 한 줄로 출력된다

- reverse() 얘 reverse 한 값을 주는게 아니라 그냥 바꿔주는 애다. x.reverse() 하더라도 출력 해주는 값은 없다. 그걸 주의하도록

```python
x=[1,2,3,4]
y=x
z=x.reverse()

x=[4,3,2,1]
y=[4,3,2,1]
z=None
```

- 10진수를 2진수로 바꿀 떈 10진수를 2를 나눈 몫과 나머지를 주의하면 되고 1을 2로 나눈 몫은 0이 되니까 그걸 주의해서 풀면 쉬운문제다. 밑에 예제는 reverse()의 예제도 되니까 주의 깊게 보도록

```python
a=int(input("10진수:"))
b=[]
while a !=0:
    b.append(a%2)
    a=a//2
b.reverse() #만약 z=b.reverse()로 z에 값을 넣었다면 z는 None이 되어서 for문을 돌릴 수 없었을 것이다.
for i in b:
    print(i,end="")
```

- 우측정렬할 때 {:>} 하면되고 5자리의 값에 우측정렬 하려면 {:>5}로 하면 된다.
- while과 if 문은 조건문이 참이면 실행하는 구조이다. (이거 많이 헷갈림)
- str 뒤집는 방법

```python
x='a string'
print(x[::-1])

####결과값####
gnirts a
```

- 한꺼번에 많은 input 받는 법

```python
a,b,c,d = input().split(" ")
print(a)
print(b)
print(c)
print(d)

#입력값:이순신 가위 원빈 바위
#결과값
이순신
가위
원빈
바위
```

- set 함수

```python
# set 함수는 중복된 리스트 밸류를 솎아내주고 set 타입으로 변경시키는 애이다.
# set 함수를 적용하면 list에 정수형만 있으면 알아서 오름차순으로 바꿔준다.
# 정수형이랑 문자형이 섞여져있으면 정수형은 순서대로 바꿔주지만 문자형은 순서대로 바꿔주지 않는다.
# set 적용 후 다시 list 형식으로 바꿔주고 싶다면 list(set())을 써주면 된다.

lis=[1,2,3,2,4,1,2,3,1]
print(set(lis))
type(set(lis))
#결과값
{1,2,3,4}
<class 'set>'
```

- ### 리스트 안에 있는 문자열애들을 정수로 바꾸는 법 !

map(function, iterable)은 함수(function)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소가 함수(function)에 의해 수행 된 결과를 묶어서 리턴하는 함수이다.

```python
number = ['1','2','3','4','3','2','1']
result = list(map(int, number)) # 파이썬 3 이상부턴 map의 결과를 list로 바꿔야한다.
print(result)

# 결과
[1,2,3,4,3,2,1]

def two_times(x):
    return x*2

list(map(two_times,[1,2,3,4]))

#결과
[2,4,6,8]
```

- input 한꺼번에 받는법

```python
a,b = input().split(' ') # 이까지 하면 a, b가 각각 문자열로 나온다.
a,b = [int(a),int(b)] # 이러면 a,b 가 정수형으로 뽑힌다.
c = [int(a),int(b)]
print(a)
print(b)
print(c)
print(type(c))

#결과값
2
3
[2,3]
<class list>

#그렇다면 3개도 될까? 된다 !
a,b,c = input().split(' ')
a,b,c=[int(a),int(b),int(c)]
print(a)
print(b)
print(c)
```

- list의 위치와 값을 동시에 뽑는 법

```python
data = [1,2,3]
for i in enumerate(data):
    print("data[{}] : {}".format(*i)) #*i는 i의 값 2개를 순서대로 {} 집어넣는거
    
#결과 값
data[0] : 1
data[1] : 2
data[2] : 3
```

- lambda 함수로 다중 if문 작성하는 법

```python
a=list(map(lambda x: '4' if x=='A' else ('3' if x=='B' else ('2' if x=='C' else '1' if x=='D' else 0)), lis))
```

![](/image/11.png)

- 사용자의 입력이 숫자인지 문자인지 확인이 가능한가?

![](/image/13.png)

- isdigit은 숫자 문자인지 검사하는 함수이다. 숫자 문자의 경우 True를 반환하고 문자열이 입력된 경우 False를 반환한다.

- 각각 떨어져있는 리스트 내부의 문자열을 하나로 합치는 법

```python
sen =['P','y','t','h','o','n']
result = [''.join(sen[:])]
print(result[0])

#결과
Python

items = ['a','b','c','d','e','f','g','h']
items[3:6] = [''.join(items[3:6])]
items = ['a','b','c','def','g','h']
result = [''.join(items[3:6])]
result = ['def']
```

- **파이썬 리스트 인덱스 삭제하면 변화하는 리스트 어떻게 해결하나요?**

```python
result = [[3,6,9],[2,6,9]]
for i in result:
    for j in i:
        if j%3==0:
            i.remove(j)
print(result)
[[6], [2, 9]] #3이 삭제가 되면서 인덱스가 밀리니까 이 전에 두 번째인 6이 삭제 안되고 이 후의 두 번째인 9가 삭제되었다.

result = [[3,6,9],[2,6,9]]
for i in result:
    for j in i[:]: #i의 복사본을 두자 !
        if j%3==0:
            i.remove(j)
print(result)
[[],[2]]
```

- **리스트 내포로 인풋 여러개 받는 방법(되게 간단)**

```python
lis = [int(input('')) for a in range(1,6)]
print("입력된 값은 {}입니다.".format(lis))
#입력 값
10
10
20
30
40
#출력 값
입력된 값은 [10, 10, 20, 30, 40]입니다.
```

