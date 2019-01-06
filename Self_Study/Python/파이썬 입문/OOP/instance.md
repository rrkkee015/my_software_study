## 자료형 다루기

- type(변수명) : 그 놈의 정체를 알려줌
- isinstance(값, 자료형) : 값이 그 자료형이 맞는지 알려줌

```python
isinstance(42, int)
True
isinstance(42, float)
False
```



## 인스턴스의 이해

- 클래스

  - 함수나 변수들을 모아 놓은 집합체
  - 1,2,3,4,5,6,7.... 많은 숫자가 있을텐데 얘들은 전부 <class 'int'>이다.

- 인스턴스

  - 클래스에 의해 생성된 객체

  - **인스턴스 각자 자신의 값을 가지고 있다.** 밑에 예제에서 학생과 강사는 같지가 않다. 하지만 모두 똑같은 인간 !

  - 인간 => 학생(학생은 인간의 인스턴스), 인간 => 강사 (강사는 인간의 인스턴스)

  - 즉, 학생과 강사는 인간 클래스의 인스턴스이다. 하지만 강사와 학생은 다르다 할 땐 서로 다른 인스턴스라는 뜻이다.

    ### 프로그래밍 관점에서 보자

  - numbers1 = []이라는 리스트와 numbers2=[1,2]라는 리스트가 있는데 서로 들어있는 값이 다르기에 인스턴스가 다르다. 하지만 둘 다 List 클래스의 인스턴스이다.

  - **인스턴스로서의 리스트와 클래스로서의 리스트가 서로 다르다는 것을 기억해야한다.**

```python
isinstance(42, int)
True
42 == int # 42가 <class 'int'>이지만 int랑 같지 않다.
False # 42는 int의 인스턴스
```

```python
list1=[1,2,3]
list2=[1,2,3]
list1 == list2 #같은 값이다
True
list1 is list2 
False #다른 인스턴스이다.
```

- 클래스 만들기

```python
class 변수명:
    아무거나
```

```python
class Human:
    '''사람''' 
#한 번 만든 클래스는 함수처럼 괄호를 붙혀서 출력할 수 있다.
person1=Human() #person1이라는 인스턴스 생성했다.
person2=Human() #person2라는 인스턴스 생성했다.

person1.language = '한국어'
person2.language = '영어' #같은 사람 클래스지만 인스턴스끼리는 다른 값을 가진다.

person1.name = '서울시민'
person2.name = '인도인'

#아니 이럴거면 클래스 왜 씀?
#클래스와 인스턴스는 코드를 만드는 데 꼭 필요한 것은 아닌 인위적인 도구이다. 쓰면 사람이 이해하기 쉽도록 포장이 가능하다. 이쁘다 ㅎ

def speak(person):
    print("{}이 {}로 말을 합니다.".format(person.name,person.language))
    
Human.speak = speak #클래스 안에 말을 한다는 행동(함수)을 담은거다. 이렇게 되면 Human클래스에서 말할 수 있는 능력이 생김.

speak(person1) == person1.speak() #person1이 Human 클래스의 인스턴스 객체니까 같이 말할 수 있는 능력이 생김
speak(person2) == person2.speak() #person2이 Human 클래스의 인스턴스 객체니까 같이 말할 수 있는 능력이 생김
```

- 모델링 : 클래스로 현실의 개념을 표현하는 것

```python
#먹으면 살이 찌고, 걸으면 살이 빠지는 사람을 표현하겠다.
class Human():
    '''인간'''

person = Human()
person.name = '철수'
person.weight = 60.5 #매번 사람 넣을 때마다 얘들 반복하면 번거롭다. 그래서 사람을 찍어내는 함수를 정의해보자

def create_human(name, weight):
    person = Human()
    person.name=name
    person.weight=weight
    return person

Human.create=create_human #만들어낸 함수를 클래스 안에 집어넣음.

person = Human.create("철수",60.5)

def eat(person):
    person.weight += 0.1
    pritn("{}가 먹어서 {}kg이 되었습니다.".format(person.name, person.weight))
    
def walk(person):
    person.weight -= 0.1
    pritn("{}가 걸어서 {}kg이 되었습니다.".format(person.name, person.weight))
    
Human.eat = eat #클래스에 함수 담을 때 굳이 () 안하는 듯
Human.walk = walk

person.walk()
person.eat()
person.walk()

#이렇게 클래스로 현실의 개념을 표현해보았다. =>모델링
```

