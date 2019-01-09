# 파이썬의 Asterisk(*) 이해

```
1. 곱셈 및 거듭제곱 연산
2. 리스트형 컨테이너 타입의 데이터를 반복 확장하고자 할 때
3. 가변인자를 사용하고자 할 때
4. 컨테이너 타입의 데이터를 Unpacking 할 때
```

## 1. 곱셈 및 거듭제곱 연산

- 이건 다들 알고 있잖니



## 2. 리스트형 컨테이너 타입의 데이터를 반복 확장하고자 할 때

- 파이썬에서는 *을 숫자형 데이터 뿐만 아니라 리스트형 컨테이너 타입에서 데이터를 반복적으로 확장하기 위해 사용 가능하다.

  ```python
  # 길이 100의 제로값 리스트 초기화
  zeros_list = [0] * 100
  # 길이 100의 제로값 튜플 선언
  zeros_tuple = (0,) * 100
  # 리스트 3배 확장 후 연산
  vector_list = [[1,2,3]]
  for i, vector in enumerate(vector_list *3):
      print("{} : {}".format((i + 1),[(i + 1) * for e in vector]))
  ```



## 3. 가변인자(Variadic Parameters)를 사용하고자 할 때

- 가변인자를 사용하는 경우 : 인자의 갯수를 모를 때, 어떤 인자라도 모두 받아서 처리해야 할 때

- 파이썬에서는 인자의 종류가 2가지

  1. positional arguments : 위치가 정해지는 인자
  2. keyword arguments : 키워드를 가진, 이름을 가진 인자

  ```python
  # 2~4명의 주자로 이루어진 달리기 대회 랭킹을 보여주는 함수
  def save_ranking(first, second, third=None, fourth=None):
      rank = {}
      rank[1], rank[2] = first, second
      rank[3] = third if third is not None else 'Nobody'
      rank[4] = fourth if fourrth is not None else 'Nobody'
      print(rank)
  # positional arguments 2개 전달
  save_ranking('ming', 'alice')
  # positional arguments 2개와 keyword argument 1개 전달
  save_ranking('alice','ming', third='mike')
  # positional arguments 2개와 keyword arguments 2개 전달 (단, 하나는 positional argument 형태로 전달)
  save_ranking('alice','ming','mike',fourth='kim')
  ```

- 위의 함수는 `first`,`second`라는 두 개의 positional arguments를 받으며 `third`,`fourth라는 두 개의 keyword arguments를 받고 있다. positional arguments의 경우 생략이 불가능하며 갯수대로 정해진 위치에 인자를 전달해야한다. 그러나 keyword arguments의 경우 함수 선언시 디폴트값을 설정할 수 있으며, 만약 인자를 생략할 시 해당 디폴트값이 인자의 값으로 들어간다. 즉, 이 형태의 인자는 생략이 가능하다. 따라서, 여기서 알 수 있는건 keyword arguments의 경우 생략이 가능하기 때문에, positional arguments 이전에 선언될 수는 없다. 즉, 다음의 코드는 에러를 발생한다.

  ```python
  def save_ranking(first, second=None, third, fourth=None):
      ...
  ```

- 그런데 세 번째를 보면 positional arguments가 3개, keyword argument가 1개 전달되고 있다. 눈치가 빠르면 keyword arguments의 경우 선언된 위치만 동일할 경우 키워드를 제외하고 positional arguments 형태로 전달이 가능하다. 즉, 위에서 `mike`는 자동적으로 `third`라는 키로 전달이 된다.

  근데 최대 4명의 주자가 아닌 10명 또는 그 이상의 정해지지 않는 주자가 생긴다면 너무 불편하다. 이 때 사용하는 것이 가변인자이다.

### positioanl arguments만 받을 때

```python
def save_rankin(*args):
    print(args)
save_ranking('ming','alice','tom','wilson','roy')
```

### keyword arguments만 받을 때

```python
def save_ranking(**kwargs):
    print(kwargs)
save_ranking(first='ming', second='alice', fourth='wilson',third='tom',fifth='roy')
# {'first': 'ming', 'second': 'alice', 'fourth': 'wilson', 'third': 'tom', 'fifth': 'roy'}
```

### positional arguments 와 keyword arguments를 모두 받을 때

```python
def save_ranking(*args, **kwargs):
    print(args)
    print(kwargs)
save_ranking('ming','alice','tom',fourth='wilson',fifth='roy')
# ('ming', 'alice', 'tom')
# {'fourth': 'wilson', 'fifth': 'roy'}
```

- 위에서 `*args`는 임의의 갯수의 positional arguments를 받음을 의미하며, `**kwargs`는 임의의 갯수의 keyword arguments를 받음을 의미한다. 이 때 `*args`,`**kwargs` 형태로 가변인자를 받는걸 packing이라고 한다.

  위의 예시에서 볼 수 있듯이, 임의의 갯수와 임의의 키값을 갖는 인자들을 전달하고 있다. positional 형태로 전달되는 인자들은 `args` 라는 tuple에 저장되며, keyword 형태로 전달되는 인자들은 `kwargs`라는 dict에 저장된다.

  아까 positional과 keyword의 선언 순서를 언급했었는데, keyword는 positional보다 앞에 선언할 수 없기 때문에 다음의 코드는 에러를 발생시킨다.

  ```python
  def save_ranking(**kwargs, *args):
      ...
  ```

  이 가변인자는 매우 일반적으로 사용도는 기능이다.

  보통 오픈소스의 경우 코드의 일관성을 위해 `*args`이나 `**kwargs`와 같이 관례적으로 사용되는 인자명을 사용하지만, `*requiresd`나 `**optional`과 같이 인자명은 일반 변수와 같이 원하는대로 지정이 가능하다.(관례적으로 `*args`와 `**kwargs`와 같이 관례를 따르는게 좋다.)


## 4. 컨테이너 타입의 데이터를 Unpacking 할 때

- *는 컨테이너 타입의 데이터를 unpacking하는 경우에도 사용될 수 있다. 이는 3번과 유사한 원리로, 종종 사용할만한 기능(연산)이다. 가장 쉬운 예로, `list`나 `tuple` 또는 `dict`형태의 데이터를 가지고 있고 어떤 함수가 가변인자를 받는 경우에 사용할 수 있다.

  ```python
  from functools import reduce
  
  primes = [2,3,5,7,11,13]
  ```
