# 1월 7일 Homework

```
학습해야 할 내용
1. 기초 문법
2. 변수 및 자료형
```

- Python에서 사용할 수 없는 식별자(예약어)를 찾아 3개만 작성하세요.

```python
return, raise, pass
```

- 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다. (floating point rounding error)

  따라서, 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.

  ```python
  a = 0.1*3
  b = 0.3
  ```

  ```python
  a=round(0.1*3,2)
  b=0.3
  ```

- "안녕, 철수야"를 String Interpolation을 사용하여 출력하세요.

  ```python
  name="철수"
  print("안녕, {}야".format(name))
  print("안녕, %s야"%name)
  print(f"안녕, {name}야")
  ```

- 다음 중 형변환시 오류가 발생하는 것은?

  ```python
  str(1) #오류 안 나용
  int('30') #오류 안 나용
  int(5) #오류 안 나용
  bool('50') #오류 안 나용
  int('3.5') #오류 나용
  #int 함수 뒤에 base라고 어떤 진수로 표현 될 지 원래 같이 오는데 생략되어 있으면 10진수이다. 그렇기에 앞에는 문자열을 벗겨내도 10진수 혹은 다른 진수로 표현 될 놈이 와야하는데 3.5는 얘 벗겨도 표현이 안됨 그래서 에러 뜬당. (제 생각)
  ```

- 변경할 수 있는(mutable) 것과 변경 불가능한 것(immutable)을 분류하시오.

  ```python
  변경가능한 친구들 = Set, List, Dictionary
  ```

  ```
  변경안되는 친구들 = String, Range, Tuple
  ```
