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