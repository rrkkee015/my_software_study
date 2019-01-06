# 상속(Inheritance)

- 클래스는 코드에서 현실 세계의 개념을 더 쉽게 표현하기 위한 것이다. 그래서 인간 클래스를 만들어서 인간의 동작을 표현했었다.

  ```python
  #사람의 움직임을 나타내는 클래스
  class Human():
      
      def walk(self):
          print("걷는다")
          
      def eat(self):
          print("먹는다")
          
      def wave(self):
          print("손을 흔든다")
          
  #여기서 개의 움직임을 짜보겠다. 근데 개가 손을 흔들진 않지
  class dog():
      
      def walk(self):
          print("걷는다")
          
      def eat(self):
          print("먹는다")
          
      def wag(self):
          print("꼬리를 흔든다")
          
  person = Human() #인스턴스 만들었다.
  person.walk()
  person.eat()
  person.wave()
  
  dog = dog()
  dog.walk()
  dog.eat()
  dog.wag()
  
  #근데 여기서 보면 코드가 낭비되고 있다. human,dog 클래스에서 같은 메소드가 있다. 나중에 고양이도 만들고 닭도 만들면 더 낭비가 되겠지
  ```

  - 위의 문제를 해결하기 위해서 Animal 클래스를 만들자

  ```python
  class Animal():
      def walk(self):
          print("걷는다")
          
      def eat(self):
          print("먹는다")
          
  class Human(Animal): # 클래스 괄호 안에 다른 클래스를 넣는걸 상속한다는 뜻이다.
      
      def walk(self):
          print("걷는다")
          
      def eat(self):
          print("먹는다")
          
      def wave(self):
          print("손을 흔든다")
          
  class dog(Animal): # 상속을 받으면 Animal 클래스가 dog 클래스의 부모가 되고 dog는 자식이 된다. 자식은 부모가 가지고 있는 메소드를 그대로 사용할 수 있다.
      
      def walk(self):
          print("걷는다")
          
      def eat(self):
          print("먹는다")
          
      def wag(self):
          print("꼬리를 흔든다")
          
  person = Human()
  person.walk()
  person.eat()
  person.wave()
  
  dog = dog()
  dog.walk()
  dog.eat()
  dog.wag()
  ```

  - 이렇게 했으니 겹치는 부분을 지워도 된다.

  ```python
  class Animal():
      def walk(self):
          print("걷는다")
          
      def eat(self):
          print("먹는다")
          
  class Human(Animal):
          
      def wave(self):
          print("손을 흔든다")
          
  class dog(Animal):
          
      def wag(self):
          print("꼬리를 흔든다")
          
  person = Human()
  person.walk()
  person.eat()
  person.wave()
  
  dog = dog()
  dog.walk()
  dog.eat()
  dog.wag()
  #이렇게 해도 똑같이 출력이 된다.
  ```



# Override

```python
class Animal():
    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
    # 인사함수를 더해보겠다
    
    def greet(self):
        print("인사한다")
        
class Human(Animal):
        
    def wave(self):
        print("손을 흔든다")
        
class dog(Animal):
        
    def wag(self):
        print("꼬리를 흔든다")
        
person = Human()
person.greet()

dog = dog()
dog.greet()
#결과
인사한다
인사한다
```

- 여기서 아쉬운 점은 모든 동물이 똑같이 인사하진 않는다. 사람은 손을 흔들고 개는 꼬리를 흔든다. 그럴 땐 override가 가능하다.

```python
class Animal():
    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
    # 인사함수를 더해보겠다
    
    def greet(self):
        print("인사한다")
        
class Human(Animal):
        
    def wave(self):
        print("손을 흔든다")
        
    def greet(self):
        self.wave() # 위에 wave 메소드를 실행한다.
        
class dog(Animal):
        
    def wag(self):
        print("꼬리를 흔든다")
        
    def greet(self):
        self.wag()
        
person = Human()
person.greet()

dog = dog()
dog.greet()
#결과
손을 흔든다
꼬리를 흔든다
```

- Animal 클래스의 greet은 출력되지 않았다. 자식 고집 부모가 못 꺾듯이 자식이 덮어 씌울 수 있다.

- 그럼 cow라는 클래스도 만들어보자

```python
class Animal():
    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
    
    def greet(self):
        print("인사한다")
        
#cow 클래스를 만들어보았다.
class Cow(Animal):
    '''소'''
    
class Human(Animal):
        
    def wave(self):
        print("손을 흔든다")
        
    def greet(self):
        self.wave()
        
class dog(Animal):
        
    def wag(self):
        print("꼬리를 흔든다")
        
    def greet(self):
        self.wag()
        
cow = Cow()
cow.greet()
#결과
인사한다
```



# super()

부모의 동작을 불러오는 방법을 알아보겠다. 가끔은 오버라이딩 만으로 충분하지 않을 때가 있다. 부모의 동작은 그대로 하면서 그냥 동작을 끼워넣고 싶을 때가 있다.

```python
class Animal():
    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
    
    def greet(self):
        print("인사한다")
        
class Human(Animal):
        
    def wave(self):
        print("손을 흔들면서")
        
    def greet(self):
        self.wave()
```

- 만약 `인사한다`는 그대로 두고 `손을 흔들면서`를 추가하고 싶으면 어떻게 해야할까?
  - 그럴 땐 `super().greet()`을 해주면된다.

```python
class Animal():
    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
    
    def greet(self):
        print("인사한다")
        
class Human(Animal):
        
    def wave(self):
        print("손을 흔들면서")
        
    def greet(self):
        self.wave()
        super().greet()
        
person = Human()
person.greet()
#결과
손을 흔들면서
인사한다.
```

- 이렇게 자식 클래스를 오버라이딩 하면서 부모 클래스의 메소드를 쓰고 싶을 땐 `super().메소드이름`을 적어주면 된다.
- 이 동작을 많이 쓰는 건 `__init__`에서 많이 쓴다.

```python
class Animal():
    def __init__(self,name):
        self.name = name
        
    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
    
    def greet(self):
        print("{}이/가 인사한다".format(self.name))
        
class Human(Animal):
        
    def wave(self):
        print("손을 흔들면서")
        
    def greet(self):
        self.wave()
        super().greet()
        
person = Human("사람") #init에 name이 들어가있기 때문에
person.greet()
#결과
손을 흔들면서
사람이/가 인사한다
```

- 근데 이 `사람이/가 인사한다.`는 처음 init에서 이름을 받아와서 가져다가 썼다. 근데 사람 같은 경우에는 왼손 잡이 오른손 잡이가 있다. 그래서 그 부분을 추가해보자

```python
class Animal():
    def __init__(self,name):
        self.name = name
        
    def walk(self):
        print("걷는다")
        
    def eat(self):
        print("먹는다")
    
    def greet(self):
        print("{}이/가 인사한다".format(self.name))
        
class Human(Animal):
    
    def __init__(self, name, hand):
        super().__init__(name) #부모 클래스한테 이름 알아서 해라하고
        self.hand = hand #자식 클래스는 손만 관련가지고
        
    def wave(self):
        print("{}을 흔들면서".format(self.hand))
        
    def greet(self):
        self.wave()
        super().greet()
        
person = Human("사람","오른손")
person.greet()
#결과
오른손을 흔들면서
사람이/가 인사한다.
 #오른손은 휴먼의 인스턴스를 만들 때 오른손을 넘겨주고 class Human으로 넘겨진다. super에서 부모클래스에서 name이 처리되고 hand는 자식 클래스에서 처리가 되었다. 그렇게 Animal의 name이 {}가 인사한다에 쓰이고 Human의 손이 어느 손이 쓰이는 지에 대해 쓰인다.
    
 #참고로 super()을 안쓰고 부모의 init을 그대로 들고와서 하면 더 복잡해지니까 부모클래스에서 필요한 정보만 super로 빼오고 나머지는 자식한테 해결을 맡기는게 부모 입장에서 좋다.
```



## 내 예외 만들기

- 지난 번에 예외를 잡는 법과 일으키는 법을 공부했다. 이제는 만들어보자

```python
value = '가'
try:
    if value not in ['가위','바위','보']:
        raise ValueError("가위 바위 보 중에 하나의 값이어야 합니다.")
except ValueError: #위의 ValueError을 받아서 except가 정리를한다.
    print("에러가 발생했습니다.")

#결과
에러가 발생했습니다.

#근데 ValueError는 파이썬에서 되게 흔한 코드이다. 수 많은 함수 중에서 어느 부분에서 ValueError가 나타났는지 찾는건 되게 힘들다. 그래서 우리가 에러를 만들 수 있다.
```

- 이제 에러를 만들어보자
  - 참고로 에러의 최상위 클래스는 Exception Class이다. 그래서 쟤한테 상속받아도 된다.

```python
class UnexpectedRSPValue(Exception):
    '''가위 바위 보 가운데 하나가 아닌값인 경우에 발생하는 에러'''
```

- 여기까지 한 다음에 이 파일을 써보자

```python
from UnexpectedRSPValue'''파일이름''' import UnexpectedRSPValue

value = '가'
try:
    if value not in ['가위','바위','보']:
        raise UnexpectedRSPValue #ValueError 대신에
except UnexpectedRSPValue:
    print("에러가 발생했습니다.")

#결과
에러가 발생했습니다.

#이 전과 결과가 다르진 않지만, 에러 타입을 미리 잡아놨기 때문에 빠른 수정이 가능하다.
```

- 오류를 세밀화 하기

```python
def sign_up():
    '''회원가입 함수'''
    
try:
    sign_up()
except BadUserName:#예외를 많이 둘 수 있다.
    print("이름으로 사용할 수 없는 입력입니다.")
except PasswordNotMatched:
    print("입력한 패스워드가 서로 일치하지 않습니다.")
```

