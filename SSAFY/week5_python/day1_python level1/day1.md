# Python 기초

## 1.Python 기초

### 식별자

- 변수는 대소문자를 구별한다.

- 첫 글자에 숫자가 올 수 없다.

- 예약어는 사용할 수 없다.

  ```python
  False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
  ```

- 내장함수나 모듈 등의 이름으로도 만들면 안된다.

  ```python
  # 5를 string으로 바꿔봅시다
  type(5)
  #결과
  int
  type(str(5))
  #결과
  str
  str = 'hi'
  print(str)
  #결과
  hi
  type(str(5))
  #결과
  'str' object is not callable
  
  class Person:
      def __init__(self, name):
          self.name=name
  
      def sleep(self):
          print(f'{self.name}')
  
  person1=Person('donghun')
  type(Person('donghun'))
  Person=1
  type(Person('donghun'))
  #위에 예랑 똑같다.
  ```

  *이러면 내가 선언한 변수가 우선순위가 더 높아짐*

### 인코딩 선언

- `# -*- coding: encoding -*-`을 해준다. 주석처럼 보이지만, Python `parser`에 의해 읽혀진다.

### 주석

- 주석은 `#`으로 표현

- `docstring`은 `"""`으로 표현한다.

  - 여러 줄의 주석을 작성할 수 있다. 보통 함수/클래스 선언 다음에 해당하는 설명을 위해 활용한다.

- 주석은 실행에 영향을 주지 않는다.

  ```python
  def print_twice():
      """
      print_twice() 함수의 역할
      "hi"를 두 번 출력합니다.
      
      - created by Han dong hun
      """
      print("hi")
      print("hi")
      
  print_twice.__doc__ #이러면 함수 내에 주석을 출력해준다.
  ```

### 코드 라인

- 파이썬은 `;`을 작성 안한다. 한 줄로 표기할 땐 `;`를 작성하여 표기한다.

- 줄을 여러줄 작성할 땐 역슬래시 `\`를 사용할 수 있다.

  ```python
  print('dfdfdf
  dd')
  #결과
  에러
  print('dfdfdf\
  dd')
  #결과
  dfdfdfdd
  ```

- `[]`,`{}`,`()`는 \ 없이도 가능하다.

### 변수(variable) 및 자료형

- `a=100`이다. 라고 한다면 a라는 박스 안에다가 100을 가져오는데 이 a가 주소값 역할을 해주는데 뭔 소린지도 모르겠고, 이건 뭐 알 필요 없을거 같다. 그냥 a에 100을 저장한다라고 생각하자.

- 변수는 `=`을 통해 할당된다.

- 자료형을 확인하기 위해선 `type()`을 사용하고, 메모리 주소를 확인하기 위해선 `id()`를 사용한다.

  ```python
  x=1004
  print(id(x))
  y=1004
  print(id(y))
  
  #결과
  1974187886512
  1974187886768
  #id값 다르게 나옴, 도플갱어
  ```

- 한꺼번에 싸잡아서 동시에 할당 가능, 가두리 양식

  ```python
  x,y,z=10,20,30
  ```

- 만약 서로 값을 바꾸고 싶은 경우엔 이렇게

  ```python
  x,y = y,x
  ```

### 수치형(Numbers)

- int(정수)

  - 모든 정수는 `int`로 표현된다.

  - `long` 타입은 없고 모두 `int`형으로 표기 된다.

  - 10진수가 아닌 8진수 0o/2진수:0b/16진수:0x로도 표현이 가능하다.

    ```python
    0b10
    2
    0o10
    8
    0x10
    16
    ```

- float(부동소수점, 실수)

  - 실수는 `float`로 표현됨.

    ```python
    b=314e-2
    print(b)
    3.14
    ```

  - 실수의 경우 실제로 값을 처리하기 위해선 조심할 필요가 있다.

    ```python
    3.52 - 3.12
    #결과
    0.399999999999999 #소수점 이하의 자리는 컴퓨터가 제대로 못함, 파이썬 잘못이 아니다.
    #그럴땐 round라는 친구로 반올림이 가능하다.
    round(3.5 - 3.12, 2) #둘째 자리 반올림
    ```

- complex(복소수)

  - 복소수는 허수부를 `j`로 표현한다.

    ```python
    a= 3 - 4j
    print(type(a))
    #결과
    <class 'complex'>
    
    print(a.imag)
    -4.0 #허수 부분만 보여줌
    print(a.real)
    3.0 #실수 부분만 보여줌
    print(a.conjugate())
    (3+4j)
    ```

### Bool

- 파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있다.

- 비교/논리 연산을 수행 등에서 활용된다.

- 다음은 `False`로 변환된다.

  - **0, 0.0, (), [], {}, '', None**

  ```python
  print(type(True))
  <class 'bool'>
  print(type(False))
  <class 'bool'>
  ```

### None

- 파이썬에서는 값이 없음을 표현하기 위해 `None`타입이 존재한다.

### 문자형(String)

- 문자열은 따옴표(`'`)나 큰 따옴표(`"`)를 사용

- 문자열 안에 문장부호(`'`,`"`)가 활용될 경우 이스케이프 문자(`\`)를 앞에다가 사용해야한다.

- 혹은 안에 다른 따옴표를 쓰면 사용이 가능하다.

  ```python
  print("안녕 '동훈아'")
  print('안녕 "동훈아"')
  ```

- 여러줄에 걸친 문장은 `"""`을 사용하게 되어있다.

  ```python
  print("""
  개행문자 없이
  여러줄을 그대로 출력 가능합니다.""")
  ```

### 이스케이프 문자열

- `\`과 결합된 특수문자 혹은 조작
  - `\n, \t, \r, \0, \\ , \', \"`
  - 줄바꿈, 탭, 캐리지리턴, 널(Null), \, ', "

- 짝깜 퀴즈

  다음의 문장을 출력해보세요.

  - `"""` 사용 금지
  - `print` 여러번 사용 금지


  ```
  "파일은 C:\Windows\Users\내문서\Python에 저장이 되어있습니다."
  나는 생각했다. 'cd를 써서 git bash로 들어가봐야지'
  ```

  ```python
  여기에 코드를 작성해주세요.
  print("\"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어있습니다.\"\n나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'")
  ```

### String interpolation

1. %-formatting
2. str.format()
3. f-strings

- 이 중에서 지 편한거 쓰면 됨

  ```python
  name = "han"
  print('hello,%s'%name) #정수이면 %d
  print('{}'.format(name))
  print(f'hello,{name}')
  ```

- 오늘을 표현해보자

  ```python
  import datetime
  today = datetime.datetime.now()
  print (today)
  #이쁘게 만들어보자, 나처럼
  print(f'지금은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}')
  #저기서 y이면 19만 나오고 Y이면 2019 다 나옴
  #시간은 %H
  ```

- 원의 넓이

  ```python
  pi = 3.141592
  print(f'원주율은 {pi:.4}. 반지름이 2일 때 원의 넓이는 {pi*2*2}')
  ```

### 연산자

- `+, -, *, /, //, %, **` 순서대로 덧셈, 뺄셈, 곱셈, 나눗셈, 몫, 나머지, 거듭제곱

- divmod는 `(몫, 나머지)` 형식으로 반환해주는 함수이다.

- 양수/음수도 표현 가능하다.

  ```python
  a = 5
  print(-a)
  #결과
  -5
  ```

### 비교연산자

- 내 쓰던대로 쓰면 됨

### 논리 연산자

- a and b : a와 b 모두 True시만 True

- a or b : a와 b 모두 False시만 False

- not a : True => False, False> True

- `&` `|`은 파이썬에서 비트 연산자이다.

  ```python
  # and와 관련해서 모든 case를 출력해봅시다.
  # a&b
  print(True and True)
  print(True and False)
  print(False and True)
  print(False and False)
  
  True
  False
  False
  False
  ```

  ```python
  # or와 관련해서 모든 case를 출력해봅시다.
  print(True or True)
  print(True or False)
  print(False or True)
  print(False or False)
  
  True
  True
  True
  False
  ```

  ```python
  # not을 활용해봅시다.
  print(not True)
  print(not [])
  
  False
  True
  ```

- `&`, `and` 얘 둘이 결국 하는 일은 똑같다. 근데 그 차이점은 계산하는 방식이 다르다.

  - a & b이면 a가 False더라도 b를 챙기는 섬세한 친구... 그런 친구...
  - a and b에서 a가 False면 b는 뭐 보지도 않고 거들떠도 안 봄 (연산이 빨라지겠죠?)

- `|`,`or` 얘도 마찬가지임.

### 복합 연산자

`+=, ==, *=, /=, //=, %=, **=` 이런 친구들

```python
# 복합연산자는 이럴 때 사용됩니다.
count = 0
while count < 5:
    print(count)
    count +=1
```

### 기타 연산자

- Concatenation

  숫자가 아닌 자료형은 `+` 연산자를 통해 합칠 수 있다.

- Containment Test

  `in` 연산자를 통해 속해있는지 여부를 확인할 수 있다.

- Identity

  `is`연산자를 통해 동일한 object인지 확인할 수 있다. (class 배우고 씀)

- Indexing/Slicing

  `[]`를 통한 값 접근 및 `[:]`을 통한 슬라이싱 (다음 챕터를 배우면서 추가 학습)

### 연산자 우선순위

```
1.()을 통한 grouping
2.Slicing
3.Indexing
4.제곱연산자 **
5.단항연산자 +, - (음수/양수 부호)
6.산술연산자 *, /, %
7.산술연산자 +, -
8.비교연산자, in, is
9.not
10.and
11.or
```

### 암시적 형변환

- 파이썬에서 데이터타입은 서로 변환할 수 있다.

- 사용자가 의도하진 않았지만, 파이썬 내부적으로 자동으로 형변환 하는 경우이다.

  - bool형, Numbers (int, float, complex)

  ```python
  print(True + 3)
  4
  print(type(3+5.0))
  <class 'float'>
  print(type(3+5j))
  <class <'complex'>
  ```

### 명시적 형변환

- 위의 상황을 제외하곤 모두 명시적으로 형 변환을 해주어야한다.

  ```python
  print(1+'1')
  Error
  print(1+int('1'))
  2
  print(1 + '등')
  Error
  print(str(1) + '등')
  1등
  ```

> 혹여나 int를 변수로 썼으면 나중에 del int를 해주어야한다. 안 그럼 int로서 기능 못함

- string 3.5는 int로 변환할 수 없지만 float 3.5는 int로 변환이 가능하다.

  ```python
  int(str(3.5))
  Error
  int(float(3.5))
  3
  ```

### 시퀀스(sequence) 자료형

- `시퀀스`는 데이터의 순서대로 나열된 형식을 나타낸다.
- **주의! 순서대로 나열된 것이 정렬되었다라는 뜻은 아니다.**
- 파이썬에선 기본적인 시퀀스 타입은
-  다음과 같다.
  1. 리스트
  2. 튜플
  3. 레인지(range)
  4. 문자열(string)
  5. 바이너리(binary) : 따로 다루진 않는다.

### list

- `[]`를 사용하고 index 값은 `list[i]`를 통해 접근한다.

  ```python
  li=[0,1,2,3,4]
  li=[1:100]
  #에러 뜰거 같은데 안뜸
  [1,2,3,4]
  ```

### tuple

- `()`을 사용한다. 리스트와 유사하지만, 수정 불가능(immutable)하다. 읽는 것 밖에 안됨

- 괄호가 있든 없든 상관없다.

  ```python
  yap = (1,2,3)
  yabu = 1,2,3
  print(type(yabu))
  <class 'tuple'>
  ```

### range()

- 레인지는 숫자의 시퀀스를 나타낸다.

  기본형 : range(n)

  > 0부터 n-1까지 값을 가진다.

  범위 지정 : range(n, m)

  > n부터 m-1까지 값을 가짐

  범위 및 스텝 지정 : range(n, m, s)

  > n부터 m-1까지 +s만큼 증가한다.

  ```python
  list(range(0,-9))
  Error
  list(range(-9,0))
  [-9, -8, -7, -6, -5, -4, -3, -2, -1]
  ```

### 시퀀스에서 활용할 수 있는 연산자/함수

- x in s

  ```python
  s="string"
  print('a' in s)
  False
  print('a' not in s)
  True
  ```

- `[]*숫자`

  ```python
  [0]*3
  [0,0,0]
  
  [1,2,3]*3
  [1,2,3,1,2,3,1,2,3]
  ```

- slicing

  ```python
  nums=[1,2,3,4,5,6,7,8,9,0]
  nums[1:3]
  [2,3]
  ```

- 리스트 내부에 인자 갯수 세기

  ```python
  [1,2,3,1,2,4,1,2,3,1,4,1,2,4,1,2,5,7,8,9].count(2)
  ```

- 리스트 인자 바꾸기

  ```python
  #인자 바꾸기
  [1,2,3,4,1,2,3]
  l[3] = 30
  #인자 지우기
  [1,2,3,30,1,2,3]
  del l[3]
  #인자 싸그리 지우기
  [1,2,3,1,2,3]
  del l[3:]
  [1,2,3]
  #인자 추가하기
  l.append(4)
  [1,2,3,4]
  #인자 사이에 추가하기
  l.insert(1,20) # list.insert(인덱스번호, 추가할 숫자)
  [1,20,2,3,4]
  #어떤 값을 지우기
  l.remove(20)
  [1,2,3,4]
  #append 반대 개념, 맨 뒤에 숫자 출력하고 지우는
  l.pop()
  [1,2,3]
  ```

- 최대값, 최소값 뽑기

  ```python
  l=[30,2,1,4,1,0]
  max(l)
  30
  min(l)
  0
  ```

- 리스트 정렬

  ```python
  l = [2,3,5,7,1,9,4]
  l.sort()
  print(l)
  ```

### set, dictionary

- `set`과 `dictionary`는 기본적으로 순서가 없습니다.

  **set**

  - 세트는 `{}`를 통해 만들며, 순서가 없고 중복된 값이 없다.

  - 수학에서 집합과 동일하게 처리된다.

    ```python
    set_a={1,2,3}
    set_b={3,6,9}
    
    print(set_a - set_b)
    {1,2}
    print(set_a | set_b)
    {1,2,3,6,9}
    print(set_a & set_b)
    {3}
    ```

  - 중복된 값을 제거해보자

    ```python
    lis = [1,2,3,1,2,3]
    set(lis)
    print(lis)
    {1,2,3}
    ```

  **dictionary**

  - 딕셔너리는 `key`와 `value`가 쌍으로 이뤄져있으며, 궁극의 자료구조이다.
  - `{}`를 통해 만들며, `dict()`로 만들 수도 있다.
  - `key`는 immutable한 모든 것이 가능하다. (불변값 : string, tuple, range())
  - `value`는 `list, dictionary`를 포함한 모든 것이 가능하다.

