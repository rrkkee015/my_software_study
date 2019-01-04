# 메소드 이해하기

- 메소드(Method)
  - 클래스에 포함되어있는 함수를 말하는 또 다른 이름

```python
#먹으면 살이 찌고, 걸으면 살이 빠지는 사람을 표현하겠다.
class Human():
    '''인간'''

def create_human(name, weight):
    person = Human()
    person.name=name
    person.weight=weight
    return person

Human.create=create_human #만들어낸 함수를 클래스 안에 집어넣음.

def eat(person):
    person.weight += 0.1
    pritn("{}가 먹어서 {}kg이 되었습니다.".format(person.name, person.weight))
    
def walk(person):
    person.weight -= 0.1
    pritn("{}가 걸어서 {}kg이 되었습니다.".format(person.name, person.weight))
    
Human.eat = eat #클래스에 함수 담을 때 굳이 () 안하는 듯
Human.walk = walk

person = Human.create("철수",60.5)
person.walk() #인스턴스에다가 함수를 호출하는 것을 메소드를 호출한다라고 한다.
person.eat()
person.walk()

#이렇게 클래스로 현실의 개념을 표현해보았다. =>모델링
```

- 이렇게 위와 같은 코딩이 있는데 클래스 따로 함수 따로 만들면 번거롭다. 그래서 클래스는 메소드를 다루기 위해 문법을 다루고 있다.

```python
class Human():
    '''인간'''
	def create(name, weight):
    	person = Human()
    	person.name=name
    	person.weight=weight
    	return person # 집어넣워줬다.	
    
    def eat(person):
        person.weight += 0.1
        pritn("{}가 먹어서 {}kg이 되었습니다.".format(person.name, person.weight))
    
    def walk(person):
        person.weight -= 0.1
        pritn("{}가 걸어서 {}kg이 되었습니다.".format(person.name, person.weight))
        
person = Human.create("철수",60.5)
person.walk() #인스턴스에다가 함수를 호출하는 것을 메소드를 호출한다라고 한다.
person.eat()
person.walk()

```

- 파이썬에서는 보통 메소드의 첫 번째 인자에는 self를 쓴다. 

```python
class Human():
    '''인간'''
	def create(name, weight):
    	person = Human()
    	person.name=name
    	person.weight=weight
    	return person # 집어넣워줬다.
    
    def eat(self):
        person.weight += 0.1
        pritn("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))
    
    def walk(self):
        person.weight -= 0.1
        pritn("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))
        
person = Human.create("철수",60.5)
person.walk() #인스턴스에다가 함수를 호출하는 것을 메소드를 호출한다라고 한다.
person.eat()
#결과 나옴
철수가 먹어서 68.6kg이 되었습니다.
person.walk()
```

```python
anni = Human.create("철수",60.5)

def eat(self):
    person.weight += 0.1
    print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))
    
eat(person)
#결과 나옴
철수가 먹어서 68.6kg이 되었습니다.

eat()
#결과 안나옴
```

```python
class Human():
    '''인간'''
	def create(name, weight):
    	person = Human()
    	person.name=name
    	person.weight=weight
    	return person # 집어넣워줬다.
    
    def eat(self):
        person.weight += 0.1
        pritn("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))
    
    def walk(self):
        person.weight -= 0.1
        pritn("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))
    
   	def speak(self, message):
        print(message)

anni = Human.create("철수",60.5)
anni.speak("안녕하세요") #self는 안해도됨 인스턴스가 자연스럽게 self로 들어간다.
```

- self
  - 메소드의 첫번째 인자
  - 인스턴스의 매개변수를 전달 할 때는 self 매개변수는 생략하고 전달 !!!

---

### 연습문제

```python
class Car():
    '''자동차'''


def run(car):
    print("{}가 달립니다.".format(car.name))

taxi = Car()
taxi.name = "택시"
taxi.run() # == run(taxi)

#이 친구 맨 마지막 줄이 실행될 수 있도록 수정해 보아라
```

```python
class Car():
    '''자동차'''
	def run(self):
    	print("{}가 달립니다.".format(self.name))

taxi = Car()
taxi.name = "택시"
taxi.run()
```

