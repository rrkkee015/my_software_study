# 1월 21일 주간 평가 Review

### Class 생성자 문제

- 어떤 친구가 올바르게 객체를 만드는 걸까요?

```python
class Person:
    def __init__(self,name,age):
        self.name = name
```

```python
p1 = Person(p1, 'hong', 100) => p1 왜 넣음
p2 = Person('kim') => age 어디감
p3 = Person(age = 3, name = 'kim') => 굿
p4 = Person() => name, age 어디감
```

### Update 문제

```python
d = {'a' : 1, 'b' : 2}
a1 = d.update(c=3)
a2=a1
```

```python
len(a1)은 2이다. => None이다.
a1과 a2는 같은 딕셔너리를 가리키고 있다. => 둘 다 None이다.
에러가 발생한다. => 안 한다.
보기 중에 답이 없다. ==> 답이 없네?
```

### Function 문제

```python
def func(a, b=1, c=2, *args, **kwargs):
    d = sum([n*2 for n in args if n>2])
    e = sum([v*v for k, v in kwargs.items()])
    return a + b + c + d + e

print(func(9, 4, 2, 3, 1, 7, d=3, e=6))
```

```python
9 + 4 + 2 + 6 + 14 + 9 + 36
```

### Another Function 문제

```python
a = 1

def my_func_1():
    a = 5
    my_func_2()
    
def my_func_2():
    print(a, end='')
    
my_func_1()
print(a)
```

```python
11
# 처음에 my_func_1이 실행되고 그 안에 있는 my_func_2가 실행이 또 된다. 그 안에서 a를 출력하게 되는데 my_func_2 방에는 자기 방에 있는 친구만 데리고 올 수 있고 없으면 전역에서 찾게 된다. 전역에 있는 친구는 1이기 때문에 1을 출력하게 되고 마지막 print(a)가 실행되어 11이 되는 것이다.
```

```python
a = 1

def my_func_1():
    a = 5
    my_func_2()
    
	def my_func_2():
    	print(a, end='')
    
my_func_1()
print(a)
```

```python
51
# 이렇게 되면 말이 다른게 my_func_1 방 안에 my_func_2 방이 있다고 생각하면 된다. 위에껀 각자 방을 가졌다고 생각하고 그렇기에 my_func_2는 방 밖으로 나가니 my_func_1 방이 있었고 거기에 a가 있어서 집어 온거다.
```

```python
a = 1
def my_func_1():
    a = 5
    def my_func_2():
        a = 7
        print(a+1)
        def my_func_3():
            print(a)
            print('my_func_3 실행 종료')
        my_func_3()
        print('my_func_2 실행 종료')
    my_func_2()
    print('my_func_1 실행 종료')
my_func_1()
```

```python
8
7 ==> 1이 아니라 7이다. #my_func_3가 a를 찾으려고 자기 안에서 뒤졌지만 있지 않았고 방 문을 열어보니 my_func_2에 a가 있어서 그걸 가져와서 print 했다.
my_func_3 실행 종료
my_func_2 실행 종료
my_func_1 실행 종료
```

### Copy

- 어떤 친구가 틀렸을 까?

```python
import copy

list1 = [3, 'a', 'b']
list2 = [1, 2, list1]
list3 = list1[:] #얕은 복사
list4 = copy.copy(list2) #얕은 복사
list5 = copy.deepcopy(list2) #깊은 복사
```

```python
list1 == list3의 결과는 True이다.
list4[2][0] = 4라는 코드 입력 후, 'print(list2[2][0])'의 출력 값은 4이다.
list4[2] = 5라는 코드 입력 후, 'print(list2[2])'의 출력 값은 5이다.
list5[2][1] = 3라는 코드 입력 후, 'print(list2[2][1])'의 결과값은 'a'이다.
```

### String slicing

```python
word = 'Python'
a = word[3:8]
print(a)
```

```python
hon
```

### List

```python
L = [0 for i in range(5)]
print(L)
```

```PYTHON
[0,0,0,0,0]
```

### Dictionary

```python
d1 = {'d':dict()}
d2 = dict(d = {})
```

```python
두 개가 같다.
{'d':{}}
```

### 뭔지 몰라

```python
@app.route('/')
def index():
    a='hello'
    b='world'
    return render_template('index.html', a=a, b=b)

#flask.py
def render_template(XXXXX, **kwargs):
    
#index.html
{{a}}
```

### my_sum

```python
def my_sum(a, b):
    c = a + b
    print(c)
    
result = my_sum(5, 8)
print(result)
```

```python
13
None
```

### .real

```python
complex_num = 3 + 4j
complex_num.real()
```

```python
#오류 뜬다.
TypeError
```

### type 확인

```python
num = 1
type(num) == int
```

```python
True
```

### args

```python
def func(c = '5', *args):
    a, c, b = args
    return a + b + c
print(func('3', '4', '1', '2'))
```

```python
421
```

### 내장 함수 아닌 친구

```python
sqrt() ==> 얘는 import math하고 사용해야하는 친구다.
```

