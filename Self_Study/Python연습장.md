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

