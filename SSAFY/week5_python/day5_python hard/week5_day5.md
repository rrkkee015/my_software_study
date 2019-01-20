# week5_day5

## 문자열 메소드 활용하기

### 변형

**`.capitalize()`**,**`.tilte()`**,**`.upper()`**

`.capitalize()` : 앞글자를 대문자로 만들어 반환합니다.

`.tilte()` : 어포스트로피나 공백 이후를 대문자로 만들어 반환합니다.

`.upper()` : 모두 대문자로 만들어 반환합니다.

```python
a = "hi EveryOne!!!, i'm han"
print(a.capitalize())
print(a.title())
print(a.upper())
```

```python
Hi everyone!!!, i'm han
Hi Everyone!!!, I'M Han
HI EVERYONE!!!, I'M HAN
```

**`.lower()`**,**`.swapcase()`**

`lower()` : 모두 소문자로 만들어 반환합니다.

`swapcase()` : 대 <-> 소문자로 변경하여 반환합니다.

```python
a = "hi EveryOne!!!, i'm han"
print(a.swapcase())
```

```python
HI eVERYoNE!!!, I'M HAN
```

**`join(iterable)`**

특정한 문자열로 만들어 반환합니다.

```python
a= "hi"
a.join(a)
print(":".join(a))
```

```python
'hhii'
'h:i'
```

**`.replace(old, new[, count])`**

바꿀 대상 글자를 새로운 글자로 바꿔서 반환합니다.

count를 지정하면 해당 갯수만큼만 시행합니다. (왼쪽에서부터)

```python
a = "Hello World"
print(a.replace('o', ''))
print(a.replace('o', '', 1))
```

```python
Hell Wrld
Hell World
```

**글씨 제거 (`strip([chars])`)**

특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip) 오른쪽을 제거합니다(rstrip) 지정하지 않으면 공백을 제거합니다.

```python
a = "     oh!  "
print(a.strip())
print(a.lstrip())
print(a.rstrip())
b='hihihihi'
print(b.rstrip('hi'))
```

```python
oh!
oh!  #왼쪽 공백이 있음
     oh!
 #공백 뜸
```

#### 탐색 및 검증

**`.find(x)`** : x의 첫 번째 위치를 반환합니다. 없으면, **-1**을 반환합니다.

**`.index(x)`** : x의 첫 번째 위치를 반환합니다. 없으면, **오류**가 뜹니다.

```python
a='apple'
print(a.find(a))
print(a.find('a'))
print(a.index('p'))
```

```python
0 #'apple'을 찾았음
0
1
#오류를 반환하거나 안하거나의 차이가 find와 index이다.
```

#### 다양한 확인 메소드 : 참/거짓 반환

> **.isalpha()**, .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .issuper(), .istitle(), **.islower()**,**.isupper()**

**`split()`**

문자열을 특정한 단위로 나누어 리스트로 반환합니다.

```python
a="a_b_c"
print(a.split("_"))
```

```python
['a', 'b', 'c']
```



## 리스트 메소드 활용하기

#### 값 추가 및 삭제

**`.append(x)`**

리스트에 값을 추가할 수 있습니다.

```python
caffe = ['starbucks','holly','coffe bean']
caffe.append('tomtom')
print(caffe)
```

```python
['starbucks', 'holly', 'coffe bean', 'tomtom']
```

**`extend(iterable)`**

리스트에 iterable(list, range, tuple, string) 값을 붙일 수가 있습니다.

```python
caffe = ['starbucks','holly','coffe bean']
caffe.extend(['ediya','droptop'])
print(caffe)
caffe.extend(('ediya','droptop'))
print(caffe)
```

```python
['starbucks', 'holly', 'coffe bean', 'ediya', 'droptop']
['starbucks', 'holly', 'coffe bean', 'ediya', 'droptop', 'ediya', 'droptop']
```

**`insert(i, x)`**

정해진 위치 `i`에 값을 추가합니다.

```python
caffe = ['starbucks','holly','coffe bean']
caffe.insert(1,'빽다방')
print(caffe)
caffe.insert(len(caffe),'동훈커피')
print(caffe)
```

```python
['starbucks', '빽다방', 'holly', 'coffe bean']
['starbucks', '빽다방', 'holly', 'coffe bean', '동훈커피']
```

**`remove(x)`**

리스트에서 값이 x인 것을 삭제합니다.

```python
caffe = ['starbucks','holly','coffe bean']
caffe.remove('holly')
print(caffe)
```

```python
['starbucks', 'coffe bean']
```

**`pop(i)`**

정해진 위치 `i`에 있는 값을 삭제하며, 그 항목을 **반환**합니다.

`i`가 지정되지 않으면 마지막 항목을 삭제하고 되돌려줍니다.

```python
caffe = ['starbucks','holly','coffe bean']
print(caffe.pop())
print(caffe)
print(caffe.pop(0))
print(caffe)
```

```python
coffe bean
['starbucks', 'holly']
starbucks
['holly']
```

### 탐색 및 정렬

**`.index(x)`**

원하는 값을 찾아 index 값을 반환합니다.

```python
caffe = ['starbucks','holly','coffe bean']
print(caffe.index('holly'))
```

```python
1
```

**`.count(x)`**

원하는 값의 갯수를 확인할 수 있습니다.

```python
caffe = ['starbucks','holly','coffe bean','holly']
print(caffe.count('holly'))
```

```python
2
```

**`.sort()`**

정렬을 합니다. sorted()와는 다르게 원본 list를 변형시키고, None을 리턴합니다.

```python
import random
lotto = random.sample(range(1,46), 6)
print(lotto)
lotto.sort()
print(lotto)
lotto.sort(reverse = True) # 역순으로 정렬
print(lotto)
```

```python
[9, 39, 5, 29, 8, 20]
[5, 8, 9, 20, 29, 39]
[39, 29, 20, 9, 8, 5]
```

**`reverse()`**

반대로 뒤집습니다. (정렬 아님)

```python
import random
lotto = random.sample(range(1,46), 6)
print(lotto)
lotto.reverse()
print(lotto)
```

```python
[43, 14, 39, 8, 37, 20]
[20, 37, 8, 39, 14, 43]
```

### 복사

> 리스트 하나를 만들어서 리스트를 복사해보자

```python
a = [1,2,3,4]
copy_a = a # copy_a를 수정을 하면 a가 바뀐다.
copy_a[0]=5
print(a)
print(id(a))
print(id(copy_a))
```

```python
[5, 2, 3, 4]
2715587704456
2715587704456
```

*이렇게 복사하기 싫을 땐 어떻게 하면 될까요옷?*

```python
a = [1,2,3,4]
copy_a = a[:] #리스트에 있는 요소들을 복사된다.
copy_a[0]=5
print(a)
print(copy_a)
print(id(a))
print(id(copy_a))
```

```python
[1, 2, 3, 4]
[5, 2, 3, 4]
2590434728392
2590425231560
```

> 딕셔너리도 확인해보자

```python
ab = {'a':'aa','b':'bb'}
print(ab)
copy_ab = ab
copy_ab['a']='ccc'
print(ab)
```

```python
{'a': 'aa', 'b': 'bb'}
{'a': 'ccc', 'b': 'bb'}
```

*이렇게 복사하기 싫을 땐 어떻게 하면 될까요옷?*

```python
import copy
ab = {'a':'aa','b':'bb'}
copy_ab = copy.deepcopy(ab)
copy_ab['a']='ccc'
print(ab)
print(copy_ab)
```

```python
{'a': 'aa', 'b': 'bb'}
{'a': 'ccc', 'b': 'bb'}
```

- 파이썬에서 모든 변수는 객체의 주소를 가지고 있을 뿐입니다.

  num = [1, 2, 3]

- 위와 같이 변수를 생성하면 num이라는 객체를 생성하고, 변수에는 객체의 주소가 저장됩니다.

- 변경가능한(mutable) 자료형과 변경불가능한(immutable) 자료형은 서로 다르게 동작합니다.

따라서, 복사를 하고 싶을 때에는 다음과 같이 해야한다.

```python
# 얕은 복사 예시
a = [1,2,[1,2]]
b = a[:] #shallow copy
b[1] = 3
print(a)
b[2][0] = 3 #얘는 못 지켜 줌
print(a)
```

```python
[1, 2, [1, 2]]
[1, 2, [3, 2]]
```

```python
# 깊은 복사 예시
import copy
a = [1,2,[1,2]]
b = copy.deepcopy(a)
b[1] = 3
print(a)
b[2][0] =3 #얘의 공격에도 지켰다
print(a)
```

```python
[1, 2, [1, 2]]
[1, 2, [1, 2]]
```

### 삭제 **`clear()`**

리스트의 모든 항목을 삭제합니다.

```python
number = list(range(56))
print(number)
number.clear()
print(number)
```

```python
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
[]
```



## List Comprehension

List를 만들 수 있는 간단한 방법이 있습니다.

### 사전 준비

> 다음의 리스트를 만들어보세요.

1. 1~10까지의 숫자 중 짝수만 담긴 리스트 `even_list`
2. 1~10까지의 숫자로 만든 세제곱 담김 리스트 `cubic_list`

```python
even_list = [x*2 for x in range(1,11)]
cubic_list = [x**3 for x in range(1,11)]
```

```python
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

### 활용법

여러개의 `for` 혹은 `if` 문을 중첩적으로 사용 가능합니다.

### 연습 문제

#### 짝짓기 - 곱집합

> 주어진 두 list의 가능한 모든 조합을 담은 `pair` 리스트를 만들어주세요.

1. 반복문 활용
2.  list comprehension 활용

---

```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']
pair = []
for j in boys:
    for i in girls:
        pair += [(j,i)]
print(pair)

pair = [(i,j) for i in girls for j in boys]
print(pair)
```

```python
[('justin', 'jane'), ('justin', 'iu'), ('justin', 'mary'), ('david', 'jane'), ('david', 'iu'), ('david', 'mary'), ('kim', 'jane'), ('kim', 'iu'), ('kim', 'mary')]
[('jane', 'justin'), ('jane', 'david'), ('jane', 'kim'), ('iu', 'justin'), ('iu', 'david'), ('iu', 'kim'), ('mary', 'justin'), ('mary', 'david'), ('mary', 'kim')]
```

#### 피타고라스 정리

> 주어진 조건(x<y<z<50) 내에서 피타고라스 방정식의 해를 찾아보세요.

1. 반복문 활용
2. list comprehension 활용

```python
result = []
for x in range(1,50):
    for y in range(x+1,50):
        for z in range(y+1,50):
            if x**2+y**2 == z**2:
                result.append((x,y,z))
print(result)

result = [(x,y,z) for x in range(1,50) for y in range(x+1, 50) for z in range(y+1, 50) if x**2 + y**2 == z**2]
print(result)
```

```python
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37), (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36, 45)]
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37), (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36, 45)]
```

### 모음 제거하기

> 다음의 문장에서 모음(a, e, i, o, u)를 모두 제거하시오.

1. list comprehension만 사용해보세요.

```python
def df(a):
    return ''.join(i for i in a if i not in 'aeiou')
print(df('Life is too short, you need python!'))
```

```python
Lf s t shrt, y nd pythn!
```



## 딕셔너리 메소드 활용

#### 추가 및 삭제

**`.pop(key[, default])`**

key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다. default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생합니다.

```python
my_dict = {'apple':'사과','banana':'바나나','graoe':'포도'}

a = my_dict.pop('apple')
b = my_dict.pop('melon',0)
print(a)
print(b)
print(my_dict)
```

```python
사과
0
{'banana': '바나나', 'graoe': '포도'}
```

**`.update()`**

값을 제공하는 key, value로 덮어씁니다.

```python
my_dict = {'apple':'사과','banana':'바나나','graoe':'포도'}
mine = {'melon':'멜론','mango':'망고'}
my_dict.update(mine)
my_dict.update(apple = '독사과')
print(my_dict)
```

```python
{'apple': '독사과', 'banana': '바나나', 'graoe': '포도', 'melon': '멜론', 'mango': '망고'}
```

**`.get(key[, default])`**

key를 통해 value를 가져옵니다.

절대로 KeyError가 발생하지 않습니다. default는 기본적으로 None입니다.

```python
my_dict = {'apple':'사과','banana':'바나나','graoe':'포도'}
print(my_dict.get('apple'))
print(my_dict.get('melon'))
print(my_dict.get('melon',0))
```

```python
사과
None
0
```

#### dictionary comprehension

dictionary도 comprehension을 활용하여 만들 수 있습니다.

```python
cubic_list = [x**3 for x in range(1, 11)]
print(cubic_list)

cubic_d = {x:x**3 for x in range(1, 11)}
print(cubic_d)
```

```python
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
```

> 다음의 딕셔너리에서 미세먼지 농도가 80 초과 지역만 뽑아 봅시다.

```python
dusts = {'서울':72,'경기':82,'대전':29,'중국':200}
dusts = {key:value for key, value in dusts.items() if value>80}
print(dusts)
```

```python
{'경기':82,'중국':200}
```

> 다음의 딕셔너리에서 미세먼지 농도가 80초과는 나쁨 80이하는 보통으로 하는 value를 가지도록 바꿔봅시다.

```python
dusts = {'서울':72,'경기':82,'대전':29,'중국':200}
dusts = {key:'나쁨' if value > 80  else '보통' for key, value in dusts.items()}
print(dusts)
```

- 참고로 elif는 안됨 그냥 if로 조건을 늘려가면 된다.

```python
dusts = {'서울':72,'경기':82,'대전':29,'중국':200}
dusts = {key:'매우나쁨' if value > 150 else ('나쁨' if value > 80 else '보통') for key, value in dusts.items()}
print(dusts)
```



### **`map()`**,**`zip()`**,**`filter()`**

**`map(function, iterable)`**

- Iterable의 모든 원소에 function을 적용한 후 그 결과를 돌려줍니다.
- 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range
- return은 map_object 형태로 됩니다.

```python
a = [1, 2, 3]
#map을 활용하여 위의 코드를 문자열 '123'으로 만들어 봅시다.
print(''.join(map(str,a)))
```

```python
123
```

```python
a = [1, 2, 3]
print(''.join(str(x) for x in a))
```

```python
123
```

```python
a = ['1', '2', '3']
print(list(map(int, a)))
```

```python
[1, 2, 3]
```

```python
a = ['1', '2', '3']
[int(x) for x in a]
```

```python
[1, 2, 3]
```

- function은 사용자 정의 함수도 가능하다.

```python
def cube(n):
    return n**3
```

```python
def cube2(l):
    ret = []
    for i in l:
        ret.append(i ** 3)
    return ret
```

```python
a = [1,2,3]
print(list(map(cube, a)))
#print(list(map(cube2,a)))는 에러뜸
```

```python
[1, 8, 27]
```

**`zip(*iterables)`**

- 복수 iterable한 것들을 모아준다.
- 결과는 튜플의 모음으로 구성된 zip object를 반환한다.

```python
girls = ['jane','iu','mary']
boys = ['justin','david','kim']
print(list(zip(girls, boys)))
```

```python
[('jane', 'justin'), ('iu', 'david'), ('mary', 'kim')]
```

```python
girls = ['jane','iu','mary']
boys = ['justin','david','kim']
print({x:y for x in girls for y in boys}) #이렇게 되면 jane의 짝궁이 계속 바뀌게 되고 마지막 kim이 들어간다. 나머지 친구들도 다 마지막 친구인 kim을 만나게 되고 kim은 바람둥이
print({x:y for x,y in zip(girls, boys)})
```

```python
{'jane': 'kim', 'iu': 'kim', 'mary': 'kim'}
{'jane': 'justin', 'iu': 'david', 'mary': 'kim'}
```

```python
a = '123'
b = '456'

for digit_a, digit_b in zip(a,b):
    print(digit_a, digit_b)
```

```python
1 4
2 5
3 6
```

- zip은 반드시 길이가 같을 때 사용한다. 아니면 가장 짧은 것을 기준으로 삼는다.

```python
num = [1, 2, 3]
num2 = [4, 5]
num3 = [1, 2 , 3]
print(list(zip(num,num2,num3)))
```

```python
[(1, 4, 1), (2, 5, 2)]
```

- 물론 길이가 긴 것을 맞춰서 할 수도 있지만, 기억에서 지워버리자

```python
from itertools import zip_longest
num1 = [1,2,3]
num2 = ['1','2']
list(zip_longest(num1, num2, fillvalue = 10)) #fillvalue 없으면 None으로 채워짐
```

```python
[(1, '1'), (2, '2'), (3, None)]
[(1, '1'), (2, '2'), (3, 10)]
```

**`filter(function, iteralbe)`**

- iterable에서 function의 반환된 결과가 참인 것들만 구성하여 반환한다.

```python
def even(n):
    return not n % 2 #0의 not이면 True, 1의 not이면 False
a = [1, 2, 3]
print(list(filter(even, a)))
```

```python
[2]
```

```python
print([x for x in [1,2,3] if even(x)])
```

```python
[2]
```



## 세트 메소드 활용

### 추가 및 삭제

**`.add(elem)`**

elem을 세트에 추가합니다.

```python
a = {1,2,3,4,5}
a.add(5)
print(a)
a.add(6)
print(a)
```

```python
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5, 6}
```

**`update(*others)`**

여러가지의 값을 순차적으로 추가합니다.

여기서 반드시 iterable한 값을 넣어야합니다.

```python
a = {1,2,3,4,5}
a.update({6,7})
print(a)
a.update({5,5,5,2},{7,9})
print(a)
```

```python
{1, 2, 3, 4, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7, 9}
```

**`remove(elem)`**

elem을 세트에서 삭제하고, 없으면 KeyError가 발생합니다.

```python
a = {1,2,3,4,5}
a.remove(5)
print(a)
a.remove(7)
```

```python
{1,2,3,4}
Traceback (most recent call last):
  File "C:\Users\student\Desktop\1.py", line 4, in <module>
    a.remove(7)
KeyError: 7
```

**`discard(elem)`**

elem을 세트에서 삭제하고 없어도 에러가 발생하지 않습니다.

```python
a = {1,2,3,4,5}
a.discard(5)
print(a)
a.discard(5)
print(a)
```

```python
{1, 2, 3, 4}
{1, 2, 3, 4}
```

**`pop()`**

*임의의* 원소를 제거해 반환합니다.

```python
a = {1,2,3,4,5}
a.pop()
a.pop()
a.pop()
print(a)
```

```python
{4, 5} #앞에서부터 빠지네? set이 시퀀스가 아니고 실제로 정렬된 것도 아니기에 그냥 그렇다. 
```

































































































