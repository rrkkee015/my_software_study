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



