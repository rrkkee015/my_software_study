# week6 day2

- **instance**는 예시이다. (사람이라는 분류 체계 안에서 예시가 되듯) **object**도 분류 체계 속의 예시이다. 그럼 이 둘의 차이점은 뭐죠? 

> 없음, 대신 Object 용어를 더 쓸 것이다.

- 선생님은 블록체인도 멀캠에서 강의하고 있다. Hyperledger도 강의하고있다. 시간이 있으면 짬을 내서 가르쳐 주겠다.

---

### Chapter 1

- 어제 `windows + R키`에서 `google 알고리즘`치면 바로 검색 결과창이 떴었다. 오늘 이걸 위젯으로 만들어보자

- **Tkinter**을 이용할 것이다. GUI을 쉽게 제공하는 프로그램. python에 내장되어 있어서 바로 `import`를 해도 된다.

  ```python
  from tkinter import * #*는 쓰면 안되지만 오늘만 쓰도록 하자
  
  root = Tk()
  
  label = Label(root, text="Hello") #Label(어떤 tkinter 윈도우/프로그램에 넣을지, text="")
  								  #클래스에 써서 하나의 instance를 만들었다.
  #위에 정리해보면 
  #class Label:
  #	def __init__(self,root,text)가 있는 것이 유추가 된다.
  label2 = Label(root, text="Dong hun widget")
  
  label.pack() #label안에 pack이라는 메서드를  사용하는 것이다.
  label2.pack()
  
  root.mainloop() #미세먼지 코드를 쓰던가, EduSsafy 홈페이지를 쓰던가 등등
  ```

  ![](image/1.png)

  아래와 같은 코드를 작성하면 버튼이 생성되고 pack의 순서에 따라 버튼의 위치가 달라진다.

  ```python
  from tkinter import *
  
  root = Tk()
  
  label = Label(root, text="Hello")
  label2 = Label(root, text="Dong hun widget")
  
  btn = Button(root, text="This is a button") #버튼을 추가했다.
  
  btn.pack() #버튼을 추가했다.
  
  label.pack()
  label2.pack()
  
  root.mainloop()
  ```

  이제는 버튼을 누르면 웹 브라우저가 열리도록 만들어 봅시다

  ```python
  from tkinter import *
  import webbrowser
  
  def browser():
      webbrowser.open("https://www.naver.com")
      
  root = Tk()
  
  label = Label(root, text="Hello")
  label2 = Label(root, text="Dong hun widget")
  
  btn = Button(root, text="This is a button", command=browser) #3번째 인자로 command를 넣을 수 있다.
  
  label.pack()
  btn.pack()
  label2.pack()
  
  root.mainloop()
  ```

  근데 위젯 키려면 내가 파이썬 들어와서 하기 너무 귀찮다. 그래서 배치 스크립트를 만들어 볼 것이다.

  ```python
  from tkinter import *
  import webbrowser
  
  def browser():
      webbrowser.open("https://www.naver.com")
      
  root = Tk()
  
  label = Label(root, text="Hello",fg="green",bg="blue")#fg는 폰트색, bg는 배경색
  label2 = Label(root, text="Dong hun widget")
  
  btn = Button(root, text="This is a button", command=browser)
  
  label.pack()
  btn.pack()
  label2.pack()
  
  root.mainloop()
  ```

  ----

  ### Chapter 2

  여기서 잠깐 아래를 참고하고 가자(일급 객체 함수)=>함수를 객체로 넘기는 법

  ```python
  def ahnyoung():
      print("ahnyoung")
  def ohiyou():
      print('ohiyou')
  def hello():
      print('hello')
  def greeter(func): #greeter라는 함수는 함수가 담긴 변수명을 인자를 하나 받는다.
      func()
  
  #greeter 함수는 hi=hello 하고 hi() 한거랑 같다.
      
  greeter(ahnyoung) #결과 ahnyoung 근데 어떻게 해서 ahnyoung만 해도 함수가 호출 될까? 그 이유는 ahnyoung이라는 주소값을 찾아가기 때문이다. 즉 함수 내에서 ahnyoung()으로 변했음
  #greeter("ahnyoung")은 "ahnyoung"() 한 것이랑 같아서 호출되지 않는다.
  #greeter(print) 얘도 된다. print()이렇게 된거니까.
  
  greeter(hello) #결과 hello
  greeter(ohiyou) #결과 ohiyou
  #이렇듯 함수 이름만 집어넣어도 쭈루룩 나온다.
  #map(int(),input().split())이라고 안 쓰는 이유가 위에 이유이다.
  
  #이런 기능은 C나 JAVA에서 사용 못 한다. 왜냐면 Python에서 함수는 일급 객체이기 때문이다.
  ```

  ```python
  def hello():
      return 'hello'
  hi = hello #이러면 hi가 hello 함수 주소를 찾아가게 된다.
  hi() #실제로 돌아간 함수는 hello이다.
  
  def add(a,b):
      return a+b
  add_two=add #이러면 add_two가 선언된 add 함수 주소를 찾아가게 된다.
  add_two(5,2) #실제로 돌아간 함수는 add이다.
  
  #결론 : 가르치는 함수 명이 있으면 괄호 없이 인자로 사용이 가능하다. (주소를 가르킨다)
  #호출은 괄호()가 해주는 것이다. (일을 시킨다)
  ```

  ```python
  def hello(): #hello가 이 함수를 가르키고 있는 것이다.
      print('hello') #얘는 그냥 화면에 'hello'를 출력하는 친구이다. 인풋 아웃풋이 없다.
  hi=hello #hi도 hello의 함수를 가르키고 있다.
  
  def greeter(func): #인자를 받는데 글자, 숫자, 분리형이 아니고 함수를 받는 것이다. #hello를 넣어도 되고 hi 넣어도 되고 print도 되고 sum도 되고 다 됨(대신 sum은 안에 내용물이 있어야해서 에러가 나겠지)
      func() #() 붙혀서 실행을 시킴
      #얘는 입력값은 있고 출력은 없음
  ```

  ```python
  def hello():
      return "hello"
  
  def greeter(func):
      func()
      
  print(greeter(hello))
  #이러면 None / greeter 함수에 return이 없으니까
  
  def hello():
      return "hello"
  
  def greeter(func):
      return func()
  #이러면 hello가 된다.
  ```

---

### Chapter 3

- 그렇다면 **lambda**도 알아보자

  ```python
  hi = lambda : "hi"
  print(hi())
  hi
  #이렇게 해도 출력이 된다
  ```

- map 함수를 직접 만들어보자

  ```python
  print(list(map(int, ['1','2'])))
  
  #def my_map(함수, 리스트):
      #0. 빈 리스트를 만들고
      #1. 인자로 받은 리스트를 돌면서
      #2. 인자로 받은 함수를 각각의 요소에 적용한 값을 빈 리스트에 넣어서
      #3. 빈 리스트를 리턴한다.
      #4. 추가적으로 list comprehension으로 만들어보자
  def my_map(func, input_list):
      result = []
      for i in input_list:
          result.append(func(i))
      return result
  
  def my_map(func, input_list):
      return [func(i) for i in input_list]
  ```

- filter 함수를 직접 만들어보자 (조건을 통과한 결과가 True이면 출력하는 함수가 filter)

  ```python
  def my_filter(func, input_list):
      result = []
      for i in input_list:
          if func(i) == i:
              result.append(i)
      return result
  
  def is_even(num):
      return num % 2 == 0
  
  #짝수만 반환
  def my_filter(func, input_list):
      return [i for i in input_list if func(i) == False] #==False가 없으면 True만 반환된다. 홀수를 반환한다.
  
  print(my_filter(lambda x: x%2, [1,2,3,4,5])) #짝수만 출력함
  print(my_filter(is_even,[1,2,3,4,5])) #홀수만 출력함
  ```

- 다른 애를 만들어보쟈

  ```python
  def add_two(num):
      return num + 2
  print(add_two(4))
  #결과 6
  #이런 간단한 함수는 이름을 안 쓰고 할 수 있다.
  ```

  ```python
  import hof #hof 파일에 my_map()이라는 함수가 있다는 것을 가정하자.
  
  print(hof.my_map(add_two, [1,2,3,4]))
  #결과
  [3,4,5,6]
  #print(hof.my_map(lambda 입력:출력, [1,2,3,4]))
  print(hof.my_map(lambda num : num + 2,[1,2,3,4]))
  ```

  `lambda num : num + 2` 이 부분을 하나의 변수를 담아도 된다.

  ```python
  import hof
  add_two = lambda num : num + 2
  print(hof.my_map(add_two,[1,2,3,4]))
  
  #깜짝 과제
  #1.square 하는 변수에 lambda를 통해 제곱하는 함수를 할당
  #2.cube라는 변수에 lambda를 통해 3제곱하는 함수를 할당
  #3.sqrt 변수에 제곱근 (math 활용 가능)
  
  square = lambda num : num**2
  cube = lambda num : num**3
  sqrt = lambda num : round(num**(1/2), 3) #math.sqrt(num) => import math 미리 해야함
  
  import math
  print(hof.my_map(sqrt,[1,2,3,4])) #내가만든 sqrt 함수
  print(list(map(math.sqrt,[1,2,3,4]))) #math 파일에 있는 sqrt 함수
  ```

---

### Chapter 4

#### 클래스-인스턴스간의 이름공간

- 클래스를 정의하면, 클래스 객체가 생성되고 해당되는 이름 공간이 생성된다.

- 인스턴스를 만들게 되면, 인스턴스 객체가 생성되고 해당되는 이름 공간이 생성된다.

- 인스턴스의 어트리뷰트(인스턴스에 속한 변수들)가 변경되면, 변경된 데이터를 인스턴스 객체 이름 공간에 저장한다. (즉, 다른 인스턴스 변수는 변하지 않는다.)

- 즉, 인스턴스에서 특정한 어트리뷰트에 접근하게 되면 인스턴스 -> 클래스 순으로 탐색을 한다. (아래 예시 참고 '호날두'), 인스턴스 스스로가 가지고 있지 않으면 인스턴스를 찍어낸 클래스를 탐색하게된다. 있다면 (`def __init__` 안에 있겠지?)

  ```python
  name = '?'
  
  class Person:
      name = '호날두'
      
      def greeting(self):
          print(f'{name}')
          print(f'{self.name}')
  #결과
  ?
  호날두
  ```

  ```python
  name = '?'
  
  class Person:
      species = '인간'
      def __init__(self, name):
          self.name = name
          
      def greeting(self):
          print(f'{self.name}') #self.name이 없으면 '?'가 출력된다.
          print(f'{self.species}')
  cr=Person('호날두')
  cr.greeting()
  
  #여기에서 있는 인스턴스 변수는 1개임 '호날두', 클래스 변수는 1개임 '인간' 여기서도 못 찾으면 에러임
  ```

  ```python
  class Person:
      population = 0
      
      def __init__(self, name):
          self.name = name
          self.population += 1 #인스턴스 변수를 생성한 것 처럼 만듬
  cr = Person('호날두')
  me = Person('john')
  you = Person('Donghun')
  ```

  ```python
  1
  1
  1
  0
  ```

  ```python
  class Person:
      population = 0
      
      def __init__(self, name):
          self.name = name
          Person.population +=1 #클래스 변수를 접근하여 변경
          
  cr = Person('호날두')
  print(cr.population)
  me = Person('john')
  print(me.population)
  you = Person('Donghun')
  print(you.population)
  print(Person.population)
  ```

  ```python
  1
  2
  3
  3
  ```

  ```python
  class Person:
      population = 0
      
      def __init__(self, name):
          self.name = name
          self.population += 1 #인스턴스 변수를 생성한 것 처럼 만듬
          Person.population +=1 #클래스 변수를 접근하여 변경
          
  cr = Person('호날두')
  me = Person('john')
  you = Person('Donghun')
  print(cr.population)
  print(me.population)
  print(you.population)
  print(Person.population)
  ```

  ```python
  1
  2
  3
  3
  ```

  ```python
  #시험문제
  class Person:
      population = 0
      
      def __init__(self, name):
          self.name = name
          Person.population +=1 #클래스 변수를 접근하여 변경
          
  Person.population = 10 #이것 때문에 population이 0에서 10이된다.
  
  cr = Person('호날두')
  me = Person('john')
  you = Person('Donghun')
  
  print(cr.population)
  print(Person.population)
  #결과
  13
  13
  ```

  ```python
  #시험문제
  class Person:
      population = 0
      
      def __init__(self, name):
          self.name = name
          self.population +=1 #얘는 인스턴스 변수만 가지니까, self.population(얘는 왼쪽 항이 실행 되어서 원래 없던 인스턴스 변수가 만들어 진거임) = self.population(인스턴스 변수에서 찾아보려했는데 클래스 변수를 가져왔음) + 1의 줄임말임 그래서 10 더하기 1이 된거임
          
  Person.population = 10 #이것 때문에 population이 0에서 10이된다.
  
  cr = Person('호날두')
  me = Person('john')
  you = Person('Donghun')
  
  print(Person.population)
  print(cr.population)
  #결과
  10
  11 #왜냐면 
  ```

  ```python
  class Person:
      population = 0
      
      def __init__(self, name):
          self.name = name
          population = 20 #얘는 그냥 지역변수 임시변수
          self.population += 1 #인스턴스 변수를 생성한 것 처럼 만듬
          #age = 20 이러고 print(cr.age라고 하면) 에러가 뜬다. 얘는 생성자 메소드의 변수에 불과함 이닛에서 사용되고 사라지는 친구임 self.age을 해야함 age 값은 못 꺼내온다.
          Person.population +=1 #클래스 변수를 접근하여 변경
          
  cr = Person('호날두')
  me = Person('john')
  you = Person('Donghun')
  print(cr.population)
  print(me.population)
  print(you.population)
  print(Person.population)
  #결과
  1#self.population(왼쪽항 때문에 생김)=self.population(원래 없어서 클래스 변수에서 씀) + 1 그래서 1
  2#self.population=self.population(원래 없는 친구임 me 인스턴스 안엔 값은 1) + 1 그래서 2
  3#self.population=self.population(원래 없는 친구임 you 인스턴스 안엔 값은 2) + 1 그래서 3
  3#클래스 변수의 population 은 3이 되었다
  ```

- 참고로 class에 존재하는 변수는 접근할 수 있지만 메서드 내부에 있는 self (선언되지 않은) 변수들은 찾아 볼 수 없다.

---

### Chapter 5

#### 생성자 / 소멸자

- 생성자는 인스턴스 객체가 생성될 때 호출되는 함수, 소멸자는 객체가 소멸되는 과정에서 호출되는 함수

```python
class Moosang:
    def __init__(self):
        print('저는 생성자입니다.')
    def __del__(self):
        print('저는 소멸자입니다.')
life = Moosang()
study = Moosang()

del life
del study

#결과
저는 생성자입니다
저는 생성자입니다.
저는 소멸자입니다.
저는 소멸자입니다.
```

```python
class Person:
    def __init__(self, name):
        print('사람이 생성되었습니다.')
        self.naem = name
    def __del__(self):
        print('사람이 죽었습니다.')
hong = Person('홍길동')
del hong
#결과
사람이 생성되었습니다.
사람이 죽었습니다.
```

```python
class Person:
    def __init__(self, name):
        print('사람이 생성되었습니다.')
        self.naem = name
    def __del__(self):
        print('사람이 죽었습니다.')
cr = Person('호날두')
cr = Person('우리흥')
#결과
사람이 생성되었습니다.
사람이 생성되었습니다.
사람이 죽었습니다. #del 한적이 없는데..? 왜냐면 겹쳐서 하나가 없어진거다. '호날두'가 사라진거임
```

*지금 굳이 소멸자까지는 할 필요가 없지만, 장고 배우면 그 때 써야한다.*

```python
class Person:
    name = "john"  # 클래스 변수 : 모든 인스턴스가 공유함.

    def __init__(self): # 인스턴스 변수 : 인스턴스별로 각각 가지는 변수
        print('생성될 때 자동으로 호출되는 메서드입니다.')
        
    def __del__(self):
        print('소멸될 때 자동으로 호출되는 메서드입니다.')
        
john = Person()
print(john.name)
#결과
john
```

```python
class Person:
    name = "john"

    def __init__(self,name="no name"): #디폴트(기본값)을 추가했다.
        print('생성될 때 자동으로 호출되는 메서드입니다.')
        self.name = name
        
    def __del__(self):
        print('소멸될 때 자동으로 호출되는 메서드입니다.')
        
john = Person()
print(john.name)
#결과
no name
```

```python
#인구가 증가하고 감소하는 프로그램을 짜보쟈
class Person:
    name = "john"  
    population = 0
    def __init__(self,name="no name"): 
        self.name = name
        Person.population += 3
        self.population += 1
        print(f'인구가 증가하여 {Person.population}명이 되었습니다.')
        
    def __del__(self):
        Person.population -= 1
        print(f'인구가 감소하여 {Person.population}명이 되었습니다.')

jo=Person()
print(jo.population)
print(Person.population)

#결과
인구가 증가하여 3명이 되었습니다.
4
3
```

---

### Chapter 6

```python
#인구가 증가하고 감소하는 프로그램을 짜보쟈
class Person:
    name = "john"  
    population = 0
    def __init__(self,name="no name"): 
        self.name = name
        self.population += 1
        print(f'인구가 증가하여 {Person.population}명이 되었습니다.')
        
    def __del__(self):
        Person.population -= 1
        print(f'인구가 감소하여 {Person.population}명이 되었습니다.')
        
    def greeting(self):
        print(f'안녕하세요 저는 {self.name}입니다.')
john = Person('john')
print(jon.greeting())
#결과
안녕하세요 저는 john입니다.

Person.greeting()
#결과
Error
Person.greeting(john) #얘는 왜 될까?
#결과
안녕하세요 저는 john입니다.
```

```python
class Dog:
    num_of_dogs = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.num_of_dogs +=1

    def bark(self):
        print(f'멍멍, 저는 {self.name}, {self.age}살 입니다.')

puppy = Dog('멍멍이','1살')
poodle = Dog('보송이','3살')
nurung = Dog('누렁이','5살')

print(Dog.num_of_dogs)
nurung.bark() #이렇게 접근하는 방법은 크게 좋은 방법이 아니다. 따라서 새로 메소드를 만들겠다.
#결과
3
멍멍, 저는 누렁이, 5살 입니다.
```

```python
class Dog:
    num_of_dogs = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.num_of_dogs +=1

    def bark(self):
        print(f'멍멍, 저는 {self.name}, {self.age}살 입니다.')
        
    @staticmethod #만약에 이게 없으면 puppy.info()가 Error가 뜬다.
   	def info(): #self를 넣지 않은 메소드 이런 애들은 static 메소드이다. 위에다가 @staticmethod라고 써주는 것이 관례이다.(없어도 됨)
        print("강아지입니다.")

puppy = Dog('멍멍이','1살')
poodle = Dog('보송이','3살')
nurung = Dog('누렁이','5살')

print(Dog.info())
print(puppy.info())
#결과
강아지입니다.
강아지입니다.
```

- 클래스 메서드와 인스턴스 메서드의 차이점

```python
class Dog:
    num_of_dogs = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.num_of_dogs +=1

    def bark(self):
        print(f'멍멍, 저는 {self.name}, {self.age}살 입니다.')
        
    @staticmethod  
   	def info(): #인자가 필요없다.
        print("강아지입니다.")
        
    @classmethod #클래스 메서드가 있으면 Dog.count()를 불러도 앞에 클래스 인자를 자동으로 생성해줘서 Dog.count(Dog)로 실행이 된다.
    def count(cls): #class는 예약어라 못 쓰니까 cls로 쓴거다. 사실 뭐가 되든 상관없다. 클래스 메서드이다.
        #print(Dog.num_of_dogs)라고 접근을 이전에 했었다. 하지만 이젠 다르다 !
		print(f'{cls.num_of_dogs}마리 생존중')
        
puppy = Dog('멍멍이','1살')
poodle = Dog('보송이','3살')
nurung = Dog('누렁이','5살')

Dog.count() #내용물 없어도 상관없다. 파이썬이 알아서 classmethod를 찾아서 채워준다.
#결과
6마리 생존중
```

- 인스턴스 메서드 : 메서드의 첫번째 인자로 **인스턴스,객체**를 받는 메서드

  ```python
  class Person:
      #인스턴스 메서드
      def greeting(self): #첫 번째 인자로 스스로의 인스턴스,객체로 들어온다.
  ```

- 클래스 메서드 : 첫번째 인자로 **클래스**를 받는 메서드

  ```python
  class Person:
      #클래스 메서드
      def count(cls): #첫 번째 인자로 들어가는 친구가 클래스이다.
  ```

- 스태틱 메서드 : 일반적인 조작을 하는 함수를 묶어놓을 때 사용하는 메서드

  ```python
  #인자로 아무것도 받지 않는 메서드 (데이터 조작을 하지 않는 함수/ 메서드)
  class Person:
      def info():
  ```

```python
# 아래에 코드를 작성해주세요.
class Calculator:
    
    def add(a, b):
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b
```

```python
Calculator.add(5, 3)
Calculator.sub(5, 3)

cal = Calculator()
cal.sub(5, 3)#스태틱 메서드는 첫 번째 self 인자가 없어도 두 번째 세 번째 인자로 처리를 다 해준다.
cal.add(5, 3)
#cal.add(cal, 5, 3)과 똑같다. 위에거랑 그래서 첫 번째 인자로 cal을 받을 self가 필요하다.
#결과
2
에러
```

---

### Chapter 7

#### 연산자 오버로딩(중복 정의)

- 파이썬에 기본적으로 정의된 연산자를 직접적으로 정의하여 활용이 가능하다.

```python
+  __add__   
-  __sub__
*  __mul__
<  __lt__
<= __le__
== __eq__
!= __ne__
>= __ge__
>  __gt__
```

```python
'hello' + 'world' #솔직히 '+'가 문자를 더해주는게 말이 안된다. '+'에 기능을 더한 것이다.
#결과
'hello world' #'+'의 적용된 기능을 추가하는 것이 오버라이딩이다.

class Person:
    def __init__(self, name, age, asset, height, gpa):
        self.naem = name
        self.age = age
        self.asset = asset
        self.height = height
        self.gpa = gpa
        
    def __gt__(self,obj):
        if self.age>obj.age:
            return True
        else:
            return False
     
   	def __add__(self, obj):
        print('애기')

minsu = Person('minsu', 28, 700000, 178, 4.2)
insung = Person('insung', 36, 700000000, 189, 2.2)

print(minsu > insung)
print(insung.__gt__(minsu))
print(insung > minsu)
print(insung.__add__(minsu))
print(insung + minsu)
#결과
False
True
True
애기
None
애기
None
```

---

### Chapter 8

#### 상속

#### 기초

- 클래스에서 가장 큰 특징은 '상속' 기능을 가지고 있다.
- 부모 클래스의 모든 속성이 자식 클래스에게 상속 되므로 코드 재사용성이 높아진다.

> 인사만 할 수 있는 간단한 사람 클래스를 만들어보자

```python
class User:
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
    
    def create_post(self, title, content): #글을 작성하는 친구
        print(f'{self.name}님이 {title}라는 제목의 {content}을 작성하였습니다.')

user1 = User('pok_winter@naver.com','01234','Donghun')
print(user1.create_post('제목','내 첫번째 글'))
#결과
Donghun님이 제목라는 제목의 내 첫 번째 글을 작성하였습니다.

class AdminUser: #관리자는 유저랑 스탯이 다 똑같은데 글을 지우는 능력만 추가하고 싶다.
	def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
    
    def create_post(self, title, content): #글을 작성하는 친구
        print(f'{self.name}님이 {title}라는 제목의 {content}을 작성하였습니다.')
        
    def delete_post(self):
        print('글을 삭제했습니다.')
        
class SuperAdminUser: #유저 삭제 능력을 추가했다. Admin에서
	def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
    
    def create_post(self, title, content): #글을 작성하는 친구
        print(f'{self.name}님이 {title}라는 제목의 {content}을 작성하였습니다.')
        
    def delete_post(self):
        print('글을 삭제했습니다.')
        
    def delete_user(self):
        print('유저를 삭제했습니다.')
```

- 코드가 중복되는 부분이 너무 많다 ! 이 것을 지워보쟈 상속을 통해서

```python
class User:
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
    
    def create_post(self, title, content): #글을 작성하는 친구
        print(f'{self.name}님이 {title}라는 제목의 {content}을 작성하였습니다.')

class AdminUser(User): #이를 통해서 중복된 부분은 삭제할 수 있다.
#	def __init__(self, email, password, name):
#        self.email = email
#        self.password = password
#        self.name = name
    
#    def create_post(self, title, content): #글을 작성하는 친구
#        print(f'{self.name}님이 {title}라는 제목의 {content}을 작성하였습니다.')
        
    def delete_post(self):
        print('글을 삭제했습니다.')
```

- 다른 코드를 짜보쟈

```python
class Person:
    def __init__(self, name):
        self.name = name
        
    def sleep(self):
        print('쿨쿨')

class Student: #얘는 사람이기도 하면서 다른 일이 있으니 상속을 할 수 있다.
    def __init__(self, name):
        self.name = name
        
    def sleep(self):
        print('쿨쿨')
        
    def study(self):
        print('공부')
#얘는 중복되는 부분이 많다 ㅠ

class Student(Person): #상속을 통해서 코드 중에 중복된 부분을 줄였다. 생성자도 없는데 실행됨 !
    def study(self):
        print('공부')
        
john = Person('john')
print(john.sleep())
#결과
쿨쿨

donghun = Student('donghun')
print(donghun.sleep())
print(donghun.study())
#결과
쿨쿨
공부

print(john.study())
#결과
Error

#자식은 부모의 것을 할 수 있지만 부모는 자식의 것을 할 수가 없다. (자식 이기는 부모 없다)
#엄마 사랑해요
#아빠두
#형두
```

- 상속관계인지는 어떻게 알 수 있을까여?

```python
issubclass(Person, Student) #앞에는 자식, 뒤에는 부모
#결과
False
issubclass(Student, Person)
#결과
True
```

- 그럼 상속 받은 자식 메서드에 `__init__`을 해보자

```python
class Person:
    def __init__(self, name):
        self.name = name
        
    def sleep(self):
        print('쿨쿨')


class Student(Person):
    def __init__(self, name, student_id):
        self.student_id=student_id #이렇게 하면 Student 인스턴스, 객체 만들 때 자기만의 것을 만들 수 있다.
        
    def study(self):
        print('공부')
        
john = Person('john')
donghun = Student('donghun','123')
john.sleep()
print(donghun.student_id)
#결과
쿨쿨
123
```

- 이 코드의 중복된 부분을 수정해보자

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
        
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        self.student_id = student_id
        
p1 = Person('홍길동', 200, '0101231234', 'hong@gildong')
s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')
```

```python
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name,age,number,email) #이렇게하면 부모 클래스의 인스턴스 변수를 가지고 온다. #Person.__init__(self,name,age,number,email) 해도 된다. #super()라고 하게되면 부모 클래스의 이름과 self가 필요없어진다. #걍 super 써 #슈퍼두퍼
        self.student_id = student_id
```

- 메소드를 오버라이딩 : 메서드를 재정의 할 수 있다.
- 사람은 안녕이라 인사하지만 학생은 조금 더 존중하게 인사하도록 바꾸고 싶다.

```python
class Person:
    def __init__(self, name, age, number, email): #참고로 __init__에는 return 값이 있으면 안된다. 에러 뜬다. del도 마찬가지
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name,age,number,email)
        self.student_id = student_id
        
  	def greeting(self):
        print(f'안녕하세요. 저는 {self.name}입니다.') #이거 없으면 안녕, 학생 이렇게 됨, 자식 클래스에서 뭔가가 없을 땐 부모 클래스에서 찾는다. 즉, 코드를 복제해오는 것이 아니고 부모 클래스에 메소드를 더듬더듬 찾으러 가는 것이다. 있으면 찾을 필요가 없으니 지 꺼 실행하는 거임
        #인스턴스 -> 자식 클래스 -> 부모 클래스 이 순서로 더듬더듬 찾으러 간다.
        
p1 = Person('홍길동', 200, '0101231234', 'hong@gildong')
s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')

p1.greeting()
s1.greeting()

#결과
안녕, 홍길동
안녕하세요. 저는 학생입니다.
```

---

### 실습

> Teacher 클래스를 만들어보고 Student와 Teacher 클래스에 각각 다른 행동의 메소드들을 하나씩 추가해봅시다.

```python
class Person:
    def __init__(self, name, age, email):
        self.name=name
        self.age=age
        self.email=email
    
    def poo(self):
        return f'{self.name} 싼다.'
    def eat(self):
        return f'{self.name} 먹는다.'
    def age(self):
        return f'{self.age} 살이다.'

    def __gt__(self, obj): #작냐, 크냐가 중요한게 아니고 만약 작거나 크거나 비교를 했을 때 무엇을 반환을 하게 만드는지를 만드는 것이 이 놈이다.
        
    
class Student(Person):
    def __init__(self,name,age,email,scores):
        super().__init__(name,age,email)
        self.scores=scores
        
    def study(self):
        return f'{self.name} 공부한다.'

class Teacher(Person):
    def __init__(self,name,age,email,power):
        super().__init__(name,age,email)
        self.power=power
        
    def teach(self):
        return f'{self.name} 가르친다.'
    
donghun = Student('donghun',27,'pok_winter@naver.com',100)
sungjin = Teacher('sungjin',25,'sungjin@naver.com','개쌤')
print(donghun>sungjin)
```

### 실습2

> 사람은 포유류입니다.
>
> Animal Class를 만들고, Person 클래스가 상속받도록 구성해봅시다.
>
> 변수나, 메소드는 자유롭게 만들어봅시다.

```python

```

