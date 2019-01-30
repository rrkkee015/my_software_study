# 월말 평가를 위한 연습장

## 식별자

- 영문알파벳, _ , 숫자로 구성됨

- **첫 글자에 숫자 못 온다.**

- 밑에 있는 친구들은 못 쓴다. 내장함수나 모듈이니까

  ```python
  False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
  ```

  **assert, yield, while**

  확인하려면 아래에 있는걸 검색하면 된다.

  ```python
  import keyword
  print(keyword.kwlist)
  ```

- 만약 내장함수나 모듈을 사용하면 어떻게 될까?

  ```python
  str = "hi"
  print(str)
  str(5)
  ```

  ```python
  hi
  'str' object is not callable
  ```

  혹시 몰라서 선언을 해버렸다면 `del`로 지워주도록 하자

  ```python
  del str
  ```

## 주석(Comment)

- 주석은 `#`으로 표현한다.

- `docstring`은 `"""`으로 표현한다.

  여러 줄의 주석을 작성할 수 있으며, 보통 함수/클새스 선언 다음에 해당하는 설명을 위해 활용한다.

  docstring은 확인할 수 있다.

  ```python
  def mysum(a, b):
      """이것은 덧셈 함수입니다.
      이 줄도 실행되지 않아요.
      다만 docstring인 이유가 있습니다.
      """
      print(a+b)
  ```

  ```python
  mysum.__doc__
  ```

## 코드 라인

- 파이썬은 `;` 안 씀

- 한 줄로 표기할 땐 `;` 를 작성하여 표기 가능

  ```python
  print('hello');print('world')
  ```

  ```python
  hello
  world
  ```

- 줄을 여러줄 작성할 땐 `\`을 사용

- list, set, tuple,dict은 `\` 없이도 사용 가능

## 변수 및 자료형

- 변수는 `=`을 통해 할당 된다.
- 자료형 확인은 `type()`을 활용, 메모리 주소는 `id()`를 활용한다.

## 수치형

### int (정수)

- 모든 정수는 `int`로 표현된다.
- 8진수 :`0o`,  2진수:`0b`, 16진수:`0x`

### float (부동소수점, 실수)

- 실수는 `float`로 표현

### complex (복소수)

- 복소수는 허수부를 `j`로 표현함

  ```python
  a = 3 - 4j
  print(type(a))
  print(a.imag)
  print(a.real)
  print(a.conjugate())
  ```

  > 결과

  ```python
  -4
  3
  (3+4j)
  ```

### Bool

- 파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있다.
- 0, 0.0, (), [], {}, '', None 은 `False`이다.

### None

- 파이썬에서는 값이 없음을 표현하기 위해 `None` 타입이 존재한다.

### 문자형(String)

- `'`, `"`을 활용하여 표현 가능. 단, 시작과 끝은 같아야 한다.  안에는 같은 따옴표를 사용 못하지만 `\` 이스케이프 문자로 표현이 가능하다.
- 여러 줄에 걸쳐있다면 `"""`을 반드시 써야한다. 얘는 `string interpolation`에서도 사용 가능하다.

### 이스케이프 문자열

`\`를 활용하여 이를 구분한다.

| 예약문자 | 내용(의미) |
| -------- | ---------- |
| \n       | 줄바꿈     |
| \t       | 탭         |
| \r       | 캐리지리턴 |
| \0       | 널(Null)   |
| `\\`     | \          |

### String interpolation

1. `%-formatting`
2. `str.format()`
3. `f-strings` : 파이썬 3.6 이후

## 연산자

### 산술 연산자

| 연산자 | 내용     |
| ------ | -------- |
| +      | 덧셈     |
| -      | 뺄셈     |
| *      | 곱셈     |
| /      | 나눗셈   |
| `//`   | 몫       |
| %      | 나머지   |
| **     | 거듭제곱 |

- divmod는 나눗셈과 관련된 함수이다.

  ```python
  print(divmod(5, 3))
  q, r = divmod(5, 3)
  print(q, r)
  ```

  > 결과

  ```python
  (1, 2)
  1, 2
  ```

### 비교 연산자

| 연산자 | 내용     |
| ------ | -------- |
| a>b    | 초과     |
| a<b    | 미만     |
| a>=b   | 이상     |
| a<=b   | 이하     |
| a==b   | 같음     |
| a!=b   | 같지않음 |

```python
3.0 == 3
"Ho" == "ho"
```

```python
True
False
```

### 논리 연산자

| 연산자  | 내용                         |
| ------- | ---------------------------- |
| a and b | a와 b 모두 True시만 True     |
| a or b  | a와 b 모두 False시만 False   |
| not a   | True -> False, False -> True |

`&`와 `|`은 파이썬에서 비트 연산자이다.

### 복합 연산자

| 연산자 | 내용   |
| ------ | ------ |
| a+=b   | a=a+b  |
| a-=b   | a=a-b  |
| a*=b   | a=a*b  |
| a/=b   | a=a/b  |
| a//=   | a=a//b |
| a%=b   | a=a%b  |
| a**=b  | a=a**b |

```python
count = 0
while count <5:
    print(count)
    count += 1
```

```python
0
1
2
3
4
```

### 기타 연산자

- 자료형을 `+`으로 합칠 수 있기에 `Concatenation` 연산자가 있다.

- `in` 연산자를 통해 속한지 안 속한지 여부를 확인 가능하다. `Containment Test`

  ```python
  5 in list(range(5))
  5 in range(5)
  5 in range(6)
  5 in list(range(6))
  ```

  ```python
  False
  False
  True
  True
  ```

- `is` 연산자를 통해 동일한 object 인지 확인하는 `Identity` 연산자가 있다.

- `Indexing/Slicing`

### 연산자 우선순위

0. `()`을 통한 grouping
1. Slicing
2. Indexing
3. 제곱연산자 **
4. 단항연산자 +,- (음수/양수 부호)
5. 산술연산자 *, /, %
6. 산술연산자 +, -
7. 비교연산자, `in`, `is`
8. `not`
9. `and`
10. `or`

## 형변환

### 기초 형변환

- 암시적 형변환

  - bool

    ```python
    True + 5
    ```

    ```python
    6
    ```

  - Numbers

    ```python
    print(type(int + float))
    print(type(int + complex))
    ```

    ```python
    float
    complex
    ```

- 명시적 형변환

  - string - > intger : 형식에 맞는 숫자만 가능

  - intger -> string : 모두 가능

  - `int()` : string, float을 int로 변환

  - `float()` : string, int를 float로 변환

  - `str()` : int, float, list, tuple, dictionary를 문자열로 변환

    ```python
    a='3.5'
    int(a)
    ```

    ```python
    ValueError
    ```

## 시퀀스(Sequence) 자료형

- `시퀀스`는 데이터의 순서대로 나열된 형식을 나타낸다. (정렬되었다는 뜻은 아니다)

  1. 리스트(list) => mutable

  2. 튜플(tuple) => immutable

  3. 레인지(range) => immutable

     ```python
     list(range(0,-5))
     list(range(0,-5,-1))
     ```

     ```python
     [] #Error가 아니다.
     [0,-1,-2,-3,-4]
     ```

  4. 문자열(string) => immutable

  5. 바이너리(binary) ==> 얘는 안 함

### 시퀀스에서 활용할 수 있는 연산자/함수

| operation  | 설명                    |
| ---------- | ----------------------- |
| x in s     | containment test        |
| x not in s | containment test        |
| s1 + s2    | concatenation           |
| s * n      | n번만큼 반복하여 더하기 |
| s[i]       | indexing                |
| s[i:j]     | slicing                 |
| s[i:j:k]   | k 간격으로 slicing      |
| len(s)     | 길이                    |
| min(s)     | 최솟값                  |
| max(s)     | 최댓값                  |
| s.count(x) | x의 갯수                |

```python
location = ['서울','머전','머구','팡주','부산']
print(location[1:4])
print(location[4:10])
```

```python
['머전','머구','팡주'] # 4는 안 읽는다.
['부산'] # 에러 안남
```

- list에 담긴 애들은 많은 메소드로 관리가 가능하다.

  ```python
  l = [1,2,3,4,5,6,7,8,9]
  del l[3] # 인덱스로 접근
  del l[5:] # slicing 사용 가능
  l.remove(3) # value 값을 직접 접근
  l.insert(1,20) # index 값에다가 value 값을 삽입
  l.append(4) # 원하는 요소 맨 뒤에 추가
  l.pop() # 맨 뒤에 값 반환해주고 (출력은 없다), 그 값 삭제
  k = l.pop() #오류 안 뜸
  l.sort() # 리스트 정렬 (출력은 없다)
  ```

## set, dictionary

- 기본적으로 서순이 없는 친구

### set => mutable

- 집합과 같은 친구 `{}` 중괄호를 통해 만들며, 순서가 없고, 중복된 값이 없다.

| 연산자/함수       | 설명   |
| ----------------- | ------ |
| a-b               | 차집합 |
| a\|b              | 합집합 |
| a&b               | 교집합 |
| a.union(b)        | 합집합 |
| a.intersection(b) | 교집합 |

### dictionary => mutable

- `key`와 `value`가 쌍으로 이뤄져있다. 궁극의 자료구조
- `{}`를 통해 만들며, `dict()`로 만들 수 있다.
- `key`는 immutable한 모든 것이 가능 (string, integer,float,boolean,tuple,range)
- `value`는 `list`, `dictionary`를 포함한 모든 것이 가능



## 조건문

- 제어문은 크게 반복문과 조건문이 있는데 조건문 부터 알아보자
  1. `if`문은 `조건식`과 함께 사용이 되어야한다. `if <조건식>`
  2. 참이면 `:` 이후의 문장을 수행
  3. 거짓이면 `else:` 이후의 문장을 수행

- 조건문을 2개 이상 사용할 거면 `elif <조건식>`을 사용

### 조건 표현식

- if 문을 한 줄로 표현하는 것, 조건에 따라 값을 정할 때 많이 활용된다.
- `true_value if <조건식> else false_value`

## 반복문

- While 문 

  - 참인 경우 반복적으로 코드 실행
  - 반드시 종료조건을 설정해야한다.

- for 문

  - 정해진 범위 내 (시퀀스)에서 순차적으로 코드를 실행한다.

  - `enumerate()`를 활용하면, `index`값과 `value`값을 같이 데리고 올 수 있다.

    - `dict`에도 `enumerate()`를 쓸 수 있는데, 키 값만 가져온다.

      ```python
      fruit = {'apple':'a','orange':'o'}
      for idx,value in enumerate(fruit):
          print(idx, value)
      ```

      ```python
      0 apple
      1 oragne
      ```

    - `enumerate()`의 인덱스 시작 값을 정해줄 수 있다.

      ```python
      print(list(enumerate(fruit, start=2)))
      fruit = {'apple':'a','orange':'o'}
      ```

      ```python
      2 apple
      3 orange
      ```

- dictionary 반복문 활용하기

  - `for`문 그냥 사용하면 키 값만 가져옴. `dict_keys(), dict_values(), dict_items()` 맘대로 쓰자.

- `break`, `continue`, `else`

  - break는 반복문을 끝낸다. 참고로 얘가 속한 반복문 하나만 끝내준다.
  - continue는 이후의 코드를 수행하지않고, 반복문을 한 번 더 실행해준다.
  - else는 반복문이 끝까지 돌고, 그 이후에 실행한다. break로 종료되면 실행 안한다.

## 함수(function) 기초

**활용법**

```python
def func(parameter1, parameter2 ...):
    code line1
    code line2
    return value
```

- 함수 선언은 `def`로 시작하여 `:`로 끝난다.
- 함수는 `매개변수(parameter)`를 넘겨줄 수 있다.
- `return`을 통해 결과값을 전달 할 수 있다. 없으면 `None`
- 함수 호출은 `func(val1, val2 ...)`

### 기본 값

- 함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있다.

**활용법**

```python
def func(p1=v1):
    return p1
```

```python
def hi(a='익명'):
    return f'안녕 {a}야'
print(hi())
print(hi('홍길동'))
```

```python
안녕 익명야
안녕 홍길동야
```

### 키워드 인자

```python
def greeting(age, name='ssafy'):
    print(f'{name}은 {age}살 입니다.')
    
greeting(27,'동훈')
greeting('동훈',27)
greeting(27,name='동훈')
greeting(27)
greeting(age=27,'동훈') #에러
greeting(age=27,name='동훈')
greeting('동훈',age=27) #에러
greeting(name='동훈',27) #에러
```

- print 함수도 키워드 인자가 내포되어 있다.

  `print(*objects, end='\n')`

  end가 default가 되어있다.

### 가변 인자 리스트

- 앞서 `print()`함수처럼 정해지지 않은 임의의 숫자의 인자를 받기 위해선 가변인자를 활용한다.

  가변인자는 `tuple`형태로 처리가 되며, `*`로 표현된다.

**활용법**

```python
def func(*args):
```

### 정의되지 않은 인자들 처리하기

- 정의되지 않은 인자들은 `dict`형태로 처리 되며, `**`로 표현함

  주로 `kwargs`라는 이름을 사용, `**kwargs`를 통해 인자를 받아 처리할 수 있다.

**활용법**

```python
def func(**kwargs):
```

```python
def my_fake_dict(**kwargs):
    return kwargs
print(my_fake_dict(한국어='안녕', 영어='hi', 독일어 ='Guten Tag'))
```

### dictionary를 인자로 넘기기

`**dict`를 통해 함수에 인자를 넘길 수 있다.

```python
def user(password,password_confirmation,username):
    if password==password_confirmation:
        return '회원가입 완료'
    else:
        return '다시 시도 부탁드립니다.'
    
print(user(**{'username':'rrkkee015','password':'1234','password_confirmation':'1235'}))
```

### 이름공간 및 스코프

- LEGB 순으로  변수의 값을 찾아간다. (Local, Enclosed, Global, Built-in)

- `str()` 코드가 실행되면

  str을 Global scope에서 먼저 찾아서 `str=4`를 가져오고

  이는 함수가 아니라 변수이기 때문에 `not callable`하다라는 오류를 뱉는다.

  우리가 원하는 `str()`은 Builit-in scope에 있기 때문이다.

- built-in scope : 파이썬이 실행된 이후부터 끝까지

- Global scope : 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 끝까지

- Local/Enclosed scope : 함수가 실행된 시점 이후부터 리턴할 때까지

## 문자열 메소드 활용하기

### 변형

`.capitalize()` : 앞글자를 대문자로 만들어 반환 (return 값이 있다)

`.title()` : 어포스트로피나 공백 이후를 대문자로 만들어 반환 (return 값이 있다)

`.upper()` : 모두 대문자로 만들어 반환 (return 값이 있다)

`lower()` : 모두 소문자로 만들어 반환 (return 값이 있다)

`swapcase()` : 대<=>소문자로 변경하여 반환 (return 값이 있다)

`.join(iterable)` : 변수를 값 사이에 집어 넣고 반환한다.

```python
a='사이'
a.join('abc')
```

```python
a사이b사이c
```

`.replace(old, new[, count])` : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환한다. count를 지정하면 해당 갯수만큼만 시행한다.

```python
a='aaaabbbbcccc'
a.replace('a','z')
a='aaaabbbbcccc'
a.replace('a','z',2)
```

```python
zzzzbbbbcccc
zzaabbbbcccc
```

`.strip([char])` : 문자를 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나 오른쪽을 제거한다.(lstrip, rstrip)

```python
a='aaabbbaabbaa'
a.strip('a')
```

```python
bbbaabb
```

`.find(x)`, `.index(x)` : x의 첫 번째 위치를 반환한다. find는 없으면 -1 반환 / index는 없으면 오류

`참 / 거짓 반환하는 문자열 메소드`

```
.isalpha(), .isdecimal(), .isdigit(), .isnumerice(), .isspace(), .issupper(), .istitle(), .islower()
```

`split()` : 문자열을 특정한 단위로 나누어 리스트로 반환합니다.

```python
a='1:2:3:4'
a.split(':')
```

```python
['1','2','3','4']
```

## 리스트 메소드 활용하기 (얘들은 대부분 반환값이 없다.)

### 값 추가 및 삭제

`.append(x)` : 리스트에 값을 추가

`.extend(iterable)` : 리스트에 iterable 값을 붙일 수 있다. (for문 돌 수 있는 자료들)

`.insert(i, x)` : 정해진 위치 `i`에 x를 추가합니다. (`i`가 길이를 넘어서면 마지막에 하나 붙음)

`.remove(x)` : 리스트에서 값이 x인 것을 삭제한다. (제일 앞에 있는 거 하나씩 삭제)

`.pop(i)` : 정해진 위치 `i`에 있는 값을 삭제하며, 그 항목을 **반환**한다. `i`가 지정되지 않으면 마지막 항목을 삭제하고 **반환**한다.

`.index(x)` : 원하는 값을 찾아 **index 값**을 **반환**한다.

`.count(x)` : `x`의 값의 갯수를 확인하고 **반환**한다.

`.sort()` : 정렬을 합니다. **sorted()**와는 다르게 원본 list를 변형시키고, **None을 리턴**한다.

`.reverse()` : 뒤집뒤집. 마찬가지로 **reversed()**와는 다르게 원본 list를 변형시키고, **None을 리턴**한다.

### 복사

```python
a=[1,2,3,4]
b=a
a[0]=4
print(b)
```

```python
[4,2,3,4]
```

```python
a=[1,2,3,4]
b=a[:]
a[0]=4
print(b)
```

```python
[1,2,3,4]
```

```python
a=[1,2,[3,4]]
b=a[:] #b=copy.copy(a)
a[2][0] = 'aaa'
print(b)
```

```python
[1,2,['aaa',4]]
```

```python
import copy
a=[1,2,[3,4]]
b=copy.deepcopy(a)
a[2][0]='aaa'
print(b)
```

```python
[1,2,[3,4]]
```

### 삭제 **반환 없다**

```python
numbers = list(range(1,46))
numbers.clear()
print(numbers)
```

```python
[]
```

### List Comprehension

- 한 줄로 표현하는 List
- (x<y<z<50)내에서 피타고라스 방정식의 해를 찾아보세여

```python
pita = [(x,y,z) for x in range(1,50) for y in range(x+1,50) for z in range(y+1,50) if x**2 + y**2 == z**2]
```

## 딕셔너리 메소드 활용

`.pop(key[, default])` : key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다. default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생합니다. **반환 있음**

```python
my_dict = {'apple':'사과','banana':'바나나'}
my_dict.pop('apple')
my_dict.pop('melon','멜론은 안파는데요')
```

```python
사과
멜론은 안파는데요
```

`.update()` : 값을 제공하는 key, value로 덮어씁니다. **반환 없다**

```python
my_dict = {'apple':'사과','banana':'바나나','melon':'멜론'}
my_dict.update(apple='애뽀올')
print(my_dict)
```

```python
{'apple':'애뽀올','banana':'바나나','melon':'멜론'}
```

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
your_dict = {'마틴':'기타','깁슨':'얍'}
my_dict.update(your_dict)
print(my_dict)
```

```python
{'apple': '사과', 'banana': '바나나', 'melon': '멜론', '마틴': '기타', '깁슨': '얍'}
```

`.get(key[, default])` : key를 통해 value를 가져온다. **절대 Key Error가 안난다.**

### Dictionary comprehension

dictionary도 comprehension을 활용하여 만들 수 있습니다.

```python
cubic = {x:x**3 for x in range(1,5)}
print(cubic)
```

```python
{1:1,2:8,3:27,4:64}
```

```python
dusts = {'서울':72,'경기':82,'대전':29,'중국':200}
{key : value for key, value in dusts.items() if value >80}
```

```python
{'경기':82,'중국':200}
```

```python
{key:'매우나쁨' if value >150 else '나쁨' if value > 80 else '보통' if value >30 else '좋음' for key, value in dusts.items()}
```

### map(), zip(), filter()

`map(function, iterable)`

- iterable의 모든 원소에 function을 적용한 후 그 결과를 돌려준다.
- iterable = list, dict, set, str, bytes, tuple, range
- return은 map_object 형태로 된다.

```python
a = [1, 2, 3]
print(''.join(map(str,a)))
type(''.join(map(str,a)))
```

```python
123
str
```

```python
a = ['1', '2', '3']
list(map(int,a))
```

```python
[1, 2, 3]
```

```python
[int(x) for x in a]
```

```python
def cube(n):
    return n**3
a = [1, 2, 3]
print(list(map(cube,a)))
```

```python
[1, 8, 27]
```

`zip(*iterables)`

- 복수 iterable한 것들을 모은다.
- 결과는 튜플의 모음으로 구성된 zip object를 반환한다.

```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']
list(zip(girls, boys))
```

```python
[('jane','justin'),('iu','david'),('mary','kim')]
```

```python
{x:y for x in girls for y in boys}
#이렇게 하면 key는 유일하니까 마지막 값으로 덮어씌어진다.
```

```python
{'jane':'kim','iu':'kim','mary':'kim'}
```

```python
{x:y for x,y in zip(girls, boys)}
```

```python
{'jane':'justin','iu':'david','mary':'kim'}
```

- 이것도 가능하다.

```python
a='123'
b='567'

for digit_a, digit_b in zip(a,b):
    print(digit_a,digit_b)
```

```python
1 5
2 6
3 7
```

- zip은 반드시 길이가 같을 때 사용 가능하다. 아니면 가장 짧은 것을 기준으로 한다. 아닐 때도 할 수 있지만 사용하지말자.

```python
a = [1, 2, 3]
b = ['1', '2']
print(list(zip(a,b)))
```

```python
[(1,'1'),(2,'2')]
```

`filter(function, iterable)`

- iterable에서 function의 반환된 결과가 참인 것들만 구성하여 반환한다.

```python
def even(n):
    return not n%2
a = [1, 2, 3]
print(list(filter(even, a)))
```

```python
[2]
```

```python
[x for x in [1,2,3] if even(x)]
```

```python
[2]
```

## 세트 메소드 활용

### 추가 및 삭제

`.add(elem)` : elem을 세트에 추가합니다. **반환 값 없다**

`.update(*others)` : 여러가지의 값을 순차적으로 추가합니다. 여기서 반드시 iterable한 값을 넣어야합니다. **반환 값 없다.**

`.remove(elem)` : elem을 세트에서 삭제하고, 없으면 KeyError가 발생한다. **반환 값 없다**

`.discard(elem)` : x를 세트에서 삭제하고 없어도 에러가 발생하지 않습니다. **반환 값 없다**

`.pop()` : 제일 마지막 원소를 제거해 **반환**합니다.

## OOP

- 객체 지향 프로그래밍이란?
  - 객체들의 모임을 파악하고자 하는 프로그래밍이다.
- **class**
  - 속성과 행위를 담아서 집단을 만든 데이터형
- **instance**
  - 클래스에서 정의한 행위를 수행할 수 있는 클래스의 속성을 가지는 캐릭터
- **method**
  - 클래스로부터 생성된 객체에 명령을 내리는 것

- Class 예시

  ```python
  name = '성지니'
  birthday = '0206'
  class Person: #클래스 이름을 Person이라고 지었다.
      name = 'HDH'
      birthday = '12/13'
      phone = '01051910337'
      
      def greeting(self): #class 내에서는 self라는 애를 첫번째 인자로 받게 된다. #greeting은 이제 인스턴스가 사용가능한 메소드가 되었다.
          print(f'안녕, 나는 {self.name}이야, 내 생일은 {self.birthday}야')
          #self가 없으면 전역변수인 성지니, 0206을 가지고온다.
          
  me=Person() #이 과정을 intantiate이다. #Person 클래스의 청사진에 맞게 me를 만든 것이다.
  me.greeting()
  ```

  이렇게 된다면 어느 누구를 intantiate 하더라도 name, birthday, phone이 같다. 그 것을 달리 해보고 싶다.

  ```python
  class Person:
      def __init__(self,name,birthday,phone):
          self.name=name
          self.birthday=birthday
          self.phone=phone
          
      def greeting(self):
          print(f'안녕, 나는 {self.name}이야, 내 생일은 {self.birthday}야')
  
  me=Person('HDH','1213','01051910337')
  you=Person('KSJ','0206','010--------')
  me.name
  you.name
  me.greeting()
  you.greeting()
  ```

  ```python
  안녕, 나는 HDH이야, 내 생일은 1213야
  안녕, 나는 KSJ이야, 내 생일은 0206야
  ```

  이렇게 간단하고 편리하기 위해서 만든 것이 OOP이다. 값을 변경하고 싶을 땐 변경도 가능하다.

  ```python
  iu=Person('이지은','0516','01051910337')
  iu.name #이지은
  iu.name='아이유'
  iu.name #아이유
  iu.greeting
  ```
