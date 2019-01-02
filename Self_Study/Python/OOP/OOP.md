# 객체지향


- python이 제공하는 기본적인 클래스가 있다. 이 때까지 활용한거는 이 것들을 전부 재사용 한 것인데, 내가 만든 코드도 재사용 할 수 있다면 얼마나 좋을까? 불필요한 작업이 축소되고 효율성이 향상 될 것이다 !

- 객체지향 프로그래밍 : 대규모 프로그램 효율적 코딩 가능. 만약 게임 캐릭터 스텟을 저언부 각자 만들면 접속자 수마다 만들어야 하지만, 객체지향으로 해놓으면 그냥 간단하게 작업 가능

- **객체지향의 이해**

  - 객체지향 프로그래밍
    - 상태와 행위로 이루어진 객체를 만들고, 해당 객체들을 조립하여, 하나의 프로그램을 만드는 것이다.
    - 객체를 만들고 객체를 이용해 문제를 해결하려는 프로그래밍 방법이다.
    - 그럼 객체는 무엇인가요?
      - 객체는 변수와 메서드를 하나로 묶은 것이다. 변수는 값을 가지고 메서드는 실행 코드를 가진다.
      - 변수와 메서드가 서로 연관된 것들끼리 묶어 만든 것이 객체이다. 
    - 자동차를 예를 들어보자
      - 변수 : 연료량, 속도계
      - 메서드 : 주행기능 (변수와 연관된 기능)
      - 메서드는(브레이크, 가속할 경우) 변수에 영향을 끼친다.
    - 서로 연관된 변수와 메서드를 잘 파악하고 묶어 객체를 형성하는 것이 중요하다.
    - 객체는 레고와 비슷하고 이러한 레고는 어느 결과물에 부품이 될 것이고, 한 군데에서만 사용되는 것이 아니라 여러 곳에서 재사용이 가능하다.
    - 객체지향을 만들기 위한 청사진, 설계도, 템플릿을 클래스라고한다. 또한, 클래스는 추상화의 과정을 통해 만들어진다.
    - 자동차를 또 예를 들어보자
      - 자동차 클래스안에 변수와 메서드가 있을 것이다.
      - ![](/image/1.png)
  - 클래스(Class)
    - 같은 문제 도메인에 속하는 속성과 행위를 정의
    - 객체지향 프로그램의 기본적인 사용자 정의 데이터 타입
  - 객체(Object)
    - 메모리에 로딩된 클래스를 통해 클래스를 템플릿으로 하여 메모리 상에 생성된 정보 (인스턴스라고 부르기도 한다)
    - 자신 고유의 속성을 가지며 클래스에서 정의한 행위 수행
    - 객체의 행위는 클래스에서 정의된 행위에 대한 정의를 공유함으로써 메모리를 효율적으로 사용
  - 메서드(Method)
    - 메시지라고도 부름
    - 클래스로부터 생성된 객체 사용 시 객체에 명령을 내리는 행위
      - '객체가 가지고 있는 메서드를 호출한다.'
      - '객체에 메시지를 전달한다.'고 표현한다.
    - 한 객체의 속성을 조작할 목적으로 사용
    - 객체 간의 통신은 메시지 전달을 통해 이루어진다.
  - 객체지향 프로그램의 특징
    - 추상화
      - 객체에서 공통된 속성과 행위를 추출하는 것
      - 홍길동, 이순신, 강감찬 학생이 있다. 이 학생들의 공통된 속성과 행위를 추출하여 학생이라는 타입을 정의할 수 있다. 공통된 속성으로는 '학번, 이름, 주민번호, 학과, 주소, 전화번호'가 있고, 공통된 행위에는 '수강 신청하기, 수강 취소하기, 휴학 신청하기, 복학 신청하기'가 있을 것이다.
      - 이와 같이 공통의 속성과 행위를 찾아서 타입을 정의하는 과정을 추상화라고 한다.
      - 불필요한 정보는 숨기고 중요한 정보만 표현하여 프로그램을 간단히 만드는 것이 목표이다.
      - 추상 데이터 타입
        - 추상화된 데이터 타입을 지칭한다.
        - 데이터 타입의 표현과 연산을 캡슐화한다.
        - 접근 제어를 통해 데이터의 정보를 은닉할 수 있다.
        - 추상 데이터 타입 => 클래스
        - 추상 데이터 타입의 인스턴스 => 객체
        - 추상 데이터 타입에서 정의된 연산 => 메서드라고 한다.
    - 상속
      - 클래스의 속성과 행위를 하위 클래스에 물려주듯, 새로운 클래스가 기존의 클래스의 데이터와 연산을 이용할 수 있게 하는 기능
      - 상속을 받는 새로운 클래스를 자식, 파생, 하위, 서브 클래스라고 한다.
      - 기존의  클래스를 부모, 기반, 상위, 슈퍼 클래스라고 한다.
      - 상속받은 하위 클래스를 이용하여 프로그램의 요구에 맞추어 클래스 수정 가능
      - 클래스 간의 종속 관계를 형성하여 객체 조직화 가능하다.
      - 상속을 하면 어떤 효과가 있을까?
        - 부모로부터 물려받으니 재사용으로 인해 코드가 줄어듦, 하위 클래스에서 속성이나 행위를 다시 정의할 필요가 없기 때문이다.
        - 범용적인 사용 가능하다. (object 타입의 매개변수에는 string이나 int의 객체가 쓰여도 문제가 되지 않는다. 왜냐면 string과 int 모두 object를 상속받기 때문이다.)
        - 자료아 메서드의 자유로운 사용 및 추가가 가능하다.
    - 다형성
      - 다양한 형태로 나타날 수 있는 특징을 의미한다.
      - 객체지향 프로그래밍은 하나의 클래스 내부에 같은 이름의 행위를 여러개를 정의하거나, 상위 클래스의 행위를 하위 클래스에 재정의하여 사용할 수 있기 때문에 다형성의 특징을 가진다.
      - ![](/image/2.png)
      - 다형성이란 어떤 한 요소에 여러 개념을 넣어 놓는 것으로 오버라이딩, 오버로딩을 의미한다.
        - 오버라이딩 : 같은 이름의 메서드가 여러 클래스에서 다른 기능을 하는 것
        - 오버로딩 : 같은 이름의 메서드가 인자의 개수나 자료형에 따라서 다른 기능을 하는 것
        - 메서드 오버라이딩
          - 상속으로 물려 받은 자료나 메서드를 그대로 사용하지 않고 하위 클래스에서 새로 정의해 사용하는 기법
          - 상위 클래스의 메서드와 동일한 서명(매개변수의 타입, 개수, 리턴 타입)을 가져야 함 (코드의 재사용성 향상)
        - 메서드 오버로딩
          - 클래스 내부에 동일한 이름의 행위를 여러 개 정의하는 것
          - 메서드의 이름이 같고, 매개변수의 타입과 수는 서로 달라야 함
          - 리턴 타입은 관계하지 않음
          - 메서드 이름을 하나로 통일 가능하며, 같은 이름의 메서드에 여러 종류의 매개 변수를 받을 수 있다.

- **이 때까지 배운 것을 활용하여, 멤버들의 이름과 나이를 관리하기 위한 객체지향 프로그램을 만들어보자**

  - 멤버의 정보를 관리하려면 우선 이름과 나이를 key로 가지는 딕셔너리 객체가 필요하다. 그리고 더 많은 인원을 관리하기 위해선 이 딕셔너리를 리스트 객체에 항목으로 사용해야한다.

  - ```python
    members = [
        {"name":"홍길동","age":20},
        {"name":"이순신","age":45},
        {"name":"강감찬","age":35}
    ]
    
    for member in members:
        print("{}\t{}".format(member["name"],member["age"]))
    #결과
    홍길동 20
    이순신 45
    강감찬 35
    ```

  - 딕셔너리 객체는 한 명의 멤버 정보만 다룸, 그러니 이런 정보가 여러개 있으면 리스트 객체에 담아서 멤버 관리하는 것이 좋다.

  - 딕셔너리 객체의 생성 및 정보를 출력하는 함수로 정의해보자

  - ```python
    def create(name, age): #멤버 정보 생성이 필요할 때마다 호출하여 사용
        return{"name":name,"age":age}
    #create() 함수 : 매개변수에 인자를 전달 받아 딕셔너리 객체를 생성 및 반환하는 함수
    
    def to_str(person):
        return "{}\t{}".format(person["name"],person["age"])
    #to_str() 함수 : 인자로 전달 받은 딕셔너리 객체의 값을 문자열로 반환하는 함수
    
    members = [
        create("홍길동", 20),
        create("이순신", 45),
        create("강감찬", 35)
    ] #딕셔너리 객체 3개를 항목으로 가진 members 리스트 객체 생성
    
    for member in members:
        print(to_str(member)) #각 멤버 정보에 대한 문자열 값 출력
    ```

- **클래스 정의**

  - 클래스

    - 객체 생성을 위한 청사진 또는 템플릿
    - 앞의 예처럼 멤버와 관련된 추상 데이터 타입이 필요하다면

    1. 멤버 클래스 설계를 하고 (어떤 정보를 관리하고, 어떤 기능을 가져야 하는지 고민)
    2. 멤버 클래스 제작
    3. 객체 생성 (이렇게 만들어진 객체는 프로그램 중심 역할을 한다)

    - ```python
      #클래스 정의
      class 클래스명 :
          ...
          
      #객체 생성
      변수 = 클래스명() #생성자 메서드 : 클래스 이름과 동일한 메서드
      #클래스의 코드 블록 안에 필드와 메서드를 정의해 사용할 수 있다
      ```

    - ```python
      class Person: #클래스 정의
          pass
      
      member = Person() #Person 메서드를 호출하여 member 객체를 생성했다. Person 클래스 이름과 동일한 이름의 메서드를 생성자 메서드라고 한다. (Person() 얘를 생성자 메서드라고 한다)
      
      if isinstance(member, Person): #첫 번째 인자의 객체가 두 번째 인자의 클래스 인스턴스인지 검사하는 isinstance 함수
          print("member는 Person 클래스의 인스턴스입니다.")
          
      #결과
      member는 Person 클래스의 인스턴스입니다.
      ```

  - 객체의 생성과 소멸, 그리고 self

    - 생성자 메서드 : 객체를 생성하기 위해 호출하는 메서드

    - 소멸자 메서드 : 객체가 소멸되기 전에 호출되는 메서드

    - 생성자 메서드가 호출하면 '__ init __메서드'가 실행되고

    - 소멸자 메서드가 호출하면 '__ del __메서드'가 실행된다.

    - ```python
      #클래스 생성자 메서드 정의
      class 클래스명:
          def __init__(self, 매개변수목록):
              ...
      #클래스 소멸자 메서드 정의 (self를 제외한 매개변수는 사용하지 않는다)
      class 클래스명:
          ...
          def __del(self): #self는 클래스에 의해 생성된 객체 공간을 가리키는 식별자 키워드는 아니지만 관습적으로 self라는 이름을 사용한다. 객체공간의 필드와 메서드에 접근할 경우 self.식별자 형식 이용한다.
              ...
      ```

    - ```python
      class Person:
          def __init__(self, name, age): #init 생성자 메서드를 정의한다. 첫 번째 매개변수 self에는 생성된 객체공간의 참조가 전달됨. name, age에 전달된 인자 값을 이용해 self가 가리키는 객체공간에 name, age 필드 생성한다.
              self.name = name
              self.age = age
              print("{} 객체가 생성되었습니다.".format(self.name))
              
          def __del__(self): #매개변수 self에는 객체공간의 참조가 전달됨. 소멸자가 호출되면 name 필드의 정보를 이용해 객체 소멸과 관련된 메시지를 출력한다.
              print("{} 객체가 제거되었습니다.".format(self.name))
              
      member = Person("홍길동" 20) #Person 생성자 메서드를 호출하여 멤버 객체를 생성한다.
      
      print("{}\t{}".format(member.name, member.age))
      
      print(dir(member))
      ```

    - ![](/image/3.png)

- **클래스와 인스턴스의 특징**

  - 인스턴스 메서드

    - 생성된 객체 공간을 가리키는 식별자 self가 가리키는 객체의 필드 정보에 접근해 특정 목적의 기능을 수행하도록 정의된 메서드

    - 인스턴스 메서드 정의

    - ```python
      class Person:
          def __init__(self, name, age):
              self.name = name
              self.age = age
              print("{} 객체가 생성되었습니다.".format(self.name))
              
          def __del__(self):
              print("{} 객체가 제거되었습니다.".format(self.name))
              
          def to_str(self): #인스턴스 메서드인 to_str 메서드를 정의했다. 인스턴스 메서드이기 때문에 첫 번째 self 매개변수를 이용해 name 필드와 age 필드를 문자열로 반환한다.
              return "{}\t{}".format(self.name, self.age)
          
      members = [
          Person("홍길동",20),
          Person("이순신",45),
          Person("강감찬",35)
      ]
      #Person 클래스의 객체 세 개를 항목으로 가진 members 리스트 객체 생성
      
      for member in members:
          print(member.to_str()) #member 객체의 to_str 메서드를 호출해 반환된 문자열 값 출력
      ```

    - ![](/image/4.png)

  - 인스턴스 변수

    - 클래스 내에서 self.변수 형태를 가지는 변수, 객체마다 가지고 있는 객체 고유의 정보이다.

    - 멤버 필드의 접근 제한이 이루어지지 않을 경우

    - ```python
      class Person:
          def __init__(self, name, age):
              self.name = name
              self.age = age #name, age 필드는 캡슐화된 필드로 만드는 것이 필요할 수 있다. 이처럼 외부에 노출된 필드는 입력 시 유효성 검사를 할 수 없으므로 잘못된 값이 저장될 수 있다.
              print("{} 객체가 생성되었습니다.".format(self.name))
              
          def __del__(self):
              print("{} 객체가 제거되었습니다.".format(self.name))
              
          def to_str(self):
              return "{}\t{}".format(self.name, self.age)
          
      
      members = [
          Person("홍길동",20),
          Person("이순신",45),
          Person("강감찬",35)
      ]
      #예를 들어서 지나치게 높은 값이 들어가거나, 음수의 값이 들어가도 실행이 된다. 따라서 입력 데이터의 검증을 위해 적절한 멤버 필드의 접근 제한이 필요하다.
      members[0].age = 200
      
      for member in members:
          print(member.to_str())
      ```

    - 파이썬은 이를 위해서 외부에서 필드에 접근하는 것을 제한해야겠다라고 생각해서 인스턴스 변수의 접근 제한 기능을 제공하고 있다.

    - 인스턴스 변수의 접근 제한 기능

    - ```python
      class Person:
          ...
          	self.__name = name #프라이빗 필드 생성
      ```

    - 이렇게 하면 이 필드에 대해 외부에서 접근할 수 있는 공개된 getter, setter 메서드를 제공할 것인지 아니면 getter만 제공할지 고민을 해봐야한다. (getter/setter 메서드의 제공 여부에 대한 고민이 필요!)

      - getter : 멤버를 읽어오는 메서드
      - setter : 멤버를 변경하는 메서드

    - ```python
      class Person:
          def __init__(self, name, age):
              self.__name = name
              self.__age = age #프라이빗 필드 생성
              print("{} 객체가 생성되었습니다.".format(self.name))
              
          def __del__(self):
              print("{} 객체가 제거되었습니다.".format(self.name))
              
          def to_str(self):
              return "{}\t{}".format(self.name, self.age)
          
          def get_name(self): #__name 필드의 값을 반환하는 getter 메서드
              return self.__name #__name 필드에 대해서는 getter메서드만 제공하는 것을 의미한다.
          
          def get_age(self): #__age 필드의 값을 반환하는 getter 메서드
              return self.__age
          
          def set_age(self, age): #__age 필드의 값을 변경하는 메서드
              if age <0:
                  raise TypeError("나이는 0이상의 값만 허용합니다.")
              self.__age = age
        
      members = [
          Person("홍길동",20),
          Person("이순신",45),
          Person("강감찬",35)
      ]
      
      members[0].set_age(-20)
      
      for member in members:
          print(member.to_str())
      ```

    - ![](/image/5.png)

  - Python은 getter/setter를 대신할 수 있는 기능인 데코레이터(decorator) 기능을 제공한다.

    - ```python
      class Person:
          ...
          	@property #변수 이름과 같은 메서드를 만들어 사용 가능
              def name(self):
                  
      class Person:
          ...
          	@property의 이름.setter
              def name(self):
                  
      #둘 다 사용 가능
      ```

    - 데코레이터 기능

    - ```python
      class Person:
          def __init__(self, name, age):
              self.__name = name
              self.__age = age #프라이빗 필드 생성
              print("{} 객체가 생성되었습니다.".format(self.name))
              
          def __del__(self):
              print("{} 객체가 제거되었습니다.".format(self.name))
              
          def to_str(self):
              return "{}\t{}".format(self.name, self.age)
          
          @property #@property 때문에 모습은 메서드이지만 변수처럼 사용할 수 있고, __name 필드값을 반환하는 getter 메서드의 역할을 수행한다.
          def name(self):
              return self.__name
          
          @property
          def age(self):
              return self.__age
          
          @age.setter #@property 대신 @age.setter를 사용하여서 변수처럼 사용이 가능하고, __name 필드값을 반환하는 setter 메서드의 역할을 한다.
          def age(self, age):
              if age <0:
                  raise TypeError("나이는 0이상의 값만 허용합니다.")
              self.__age = age
              
      members = [
          Person("홍길동",20),
          Person("이순신",45),
          Person("강감찬",35)
      ]
      
      members[0].age = 22 #age@property 데코레이터를 이용해 변수처럼 값 저장
      
      for member in members:
          print(member.to_str())
      ```

    - ![](/image/6.png)

  - 클래스 변수

    - 인스턴스 변수와는 달리 클래스 내에서 self가 아닌 클래스.변수 형식으로 선언된 변수

    - ```python
      #클래스 변수 정의
      class 클래스명:
          클래스변수 = 값
          ...
          
       #클래스 변수 접근
      클래스명.클래스변수
      ```

    - Person 클래스에 생성된 객체에 개수를 담고 있는 클래스 변수의 count 활용법

    - ```python
      class Person:
          count = 0
          
          def __init__(self, name, age): #객체가 생성될 때마다 호출되는 __init__ 메서드
              self.__name = name
              self.__age = age
              Person.count += 1
              print("{} 객체가 생성되었습니다.".format(self.name))
              
          def __del__(self):
              print("{} 객체가 제거되었습니다.".format(self.name))
              
          def to_str(self):
              return "{}\t{}".format(self.name, self.age)
          
          @property
          def name(self):
              return self.__name
          
          @property
          def age(self):
              return self.__age
          
          @age.setter
          def age(self, age):
              if age <0:
                  raise TypeError("나이는 0이상의 값만 허용합니다.")
              self.__age = age
              
      People = [
          Person("홍길동",20),
          Person("이순신",45),
          Person("강감찬",35)
      ]
      
      print("현재 Person 클래스의 인스턴스는 총 {} 개입니다.".format(Person.count)) #클래스 변수 count를 통해 객체가 생성된 총 개수를 알 수 있다.
      ```

    - ![](/image/7.png)

  - 클래스 메서드

    - 클래스 변수는 클래스가 소유한 메서드

    - ```python
      #클래스 메서드의 정의
      class 클래스명:
          ...
          @classmethod
          def 클래스메서드(cls, 매개변수목록): #첫 번째 매개변수로 클래스 자신에 대한 참조 전달받도록 정의한다.
              ...
              
      #클래스 메서드의 사용
      클래스명.클래스메서드(매개변수목록)
      ```

    - 클래스 메서드의 사용

    - ```python
      class Person:
          count = 0
          
          def __init__(self, name, age): #객체가 생성될 때마다 호출되는 __init__ 메서드
              self.__name = name
              self.__age = age
              Person.count += 1
              print("{} 객체가 생성되었습니다.".format(self.name))
              
          def __del__(self):
              print("{} 객체가 제거되었습니다.".format(self.name))
              
          def to_str(self):
              return "{}\t{}".format(self.name, self.age)
          
          @property
          def name(self):
              return self.__name
          
          @property
          def age(self):
              return self.__age
          
          @age.setter
          def age(self, age):
              if age <0:
                  raise TypeError("나이는 0이상의 값만 허용합니다.")
              self.__age = age
              
          @classmethod 
          def get_info(cls): #cls가 클래스 참조 정보가 인자로 넘어올 매개변수
              return "현재 Person 클래스의 인스턴스는 총 {} 개입니다.".format(cls.count) #즉 cls.count는 Person.count정보와 동일하다.
          
      members = [
          Person("홍길동",20),
          Person("이순신",45),
          Person("강감찬",35)
      ]
      
      print(Person.get_info()) #get_info는 Person 클래스가 소유하므로 Person 클래스를 통해 호출하여 결과를 출력한다.
      ```

    - ![](/image/8.png)

  - 연산자 오버로딩

    - 파이썬에서 연산자는 각 클래스의 미리 정의된 메서드들과 맵핑되어 있다.

    - 우리가 제작한 사용자 정의 클래스에 경우에는 연산자들에 대해 맵핑되어있는 메서드가 없으므로 연산자를 사용하려면 연산자를 중복해서 정의해야한다. (이 정의를 연산자 오버로딩이라고 한다)

    - 비교연산자 오버로딩

    - ```python
      class Person:
          count = 0
          
          def __init__(self, name, age):
              self.__name = name
              self.__age = age
              Person.count += 1
              print("{} 객체가 생성되었습니다.".format(self.name))
              
          def __del__(self):
              print("{} 객체가 제거되었습니다.".format(self.name))
              
          def to_str(self):
              return "{}\t{}".format(self.name, self.age)
          
          @property
          def name(self):
              return self.__name
          
          @property
          def age(self):
              return self.__age
          
          @age.setter
          def age(self, age):
              if age <0:
                  raise TypeError("나이는 0이상의 값만 허용합니다.")
              self.__age = age
              
          @classmethod 
          def get_info(cls):
              return "현재 Person 클래스의 인스턴스는 총 {} 개입니다.".format(cls.count)
          
          def __gt__(self, other): #gt 메서드는 첫 번째 매개변수인 self의 __age 필드가 두 번째 매개변수인 other객체의 __age필드보다 크면 true를 반환한다.
              return self.__age > other.__age
          
          def __ge__(self, other): #ge 메서드는 첫 번째 매개변수인 self의 __age 필드가 두 번째 매개변수인 other객체의 __age필드보다 크거나 같으면 true를 반환한다.
              return self.__age >= other.__age
          
          def __lt__(self, other): #lt 메서드는 첫 번째 매개변수인 self의 __age 필드가 두 번째 매개변수인 other객체의 __age필드보다 작으면 true를 반환한다.
              return self.__age < other.__age
          
          def __le__(self, other): #le 메서드는 첫 번째 매개변수인 self의 __age 필드가 두 번째 매개변수인 other객체의 __age필드보다 작거나 같으면 true를 반환한다.
              return self.__age <= other.__age
          
          def __eq__(self, other): #eq 메서드는 첫 번째 매개변수인 self의 __age 필드가 두 번째 매개변수인 other객체의 __age필드와 같으면 true를 반환한다.
              return self.__age = other.__age
          
          def __ne__(self, other): #ne 메서드는 첫 번째 매개변수인 self의 __age 필드가 두 번째 매개변수인 other객체의 __age필드와 다르면 true를 반환한다.
              return self.__age = other.__age
          
      members = [
          Person("홍길동",20),
          Person("이순신",45),
          Person("강감찬",35)
      ]
      
      cnt = len(members)
      i = 0
      while True:
          print("members[{}] > members[{}] => {}".format(i, i+1, members[i] > members[i+1])) #두 객체에 대해 gt 메서드를 호출하고 members 리스트에 첫 번째 항목(20)과 두 번째 항목(45)을 비교하고 (False), 두 번째 항목(45)과 세 번째 항목(35)을 비교하고 (True), 마지막으로 첫 번째 항목(20)과 세 번째 항목(35)을 비교한 다음 (True) 그 결과를 반환하고 반복문을 빠져나온다.
          i +=1
          if i == cnt -1:
              print("members[{}] > members[{}] => {}".format(i, 0, members[i] > members[0]))
              break
      ```

  - __ str()__ 메서드

    - 클래스에서 __ str()__ 메서드를 구현하면 str() 함수에 객체를 전달해 문자열로 변환할 수 있다.

    - ```python
      class Person:
          count = 0
          
          def __init__(self, name, age):
              self.__name = name
              self.__age = age
              Person.count += 1
              print("{} 객체가 생성되었습니다.".format(self.name))
              
          def __del__(self):
              print("{} 객체가 제거되었습니다.".format(self.name))
              
          def to_str(self):
              return "{}\t{}".format(self.name, self.age)
          
          @property
          def name(self):
              return self.__name
          
          @property
          def age(self):
              return self.__age
          
          @age.setter
          def age(self, age):
              if age <0:
                  raise TypeError("나이는 0이상의 값만 허용합니다.")
              self.__age = age
              
          @classmethod 
          def get_info(cls):
              return "현재 Person 클래스의 인스턴스는 총 {} 개입니다.".format(cls.count)
          
          def __gt__(self, other):
              return self.__age > other.__age
          
          def __ge__(self, other):
              return self.__age >= other.__age
          
          def __lt__(self, other):
              return self.__age < other.__age
          
          def __le__(self, other):
              return self.__age <= other.__age
          
          def __eq__(self, other):
              return self.__age = other.__age
          
          def __ne__(self, other):
              return self.__age = other.__age
          
          def __str__(self): #str메서드는 첫 번째 매개변수인 self의 name 필드와 age 필드를 이용해 문자열을 반환한다.
              return "{}\t{}".format(self.__name,self.__age)
          
      members = [
          Person("홍길동",20),
          Person("이순신",45),
          Person("강감찬",35)
      ]
      
      for member in members:
          print(str(member)) #str함수에 Person 클래스의 객체를 전달하면 __str__ 메서드가 호출되어 밑에와 같이 문자열 결과를 반환한다.
      ```

    - ![](/image/9.png)

- **클래스 상속**

  - 클래스 상속

    - 부모 클래스의 동작을 자식 클래스에서 자사용, 확장, 수정하는 것을 의미한다.

    - 부모 클래스는 멤버가 상속되는 클래스이고 자식 클래스는 부모 클래스의 멤버를 상속하는 클래스이다.

    - 파일썬에서는 단일 상속만 지원한다.

    - ```python
      #클래스 상속
      class 클래스명(부모클래스명):
      ```

    - ```python
      class Person:
          def __init__(self, family_name):
              self.__family_name = family_name
              print("Parent 클래스의 __init__() ...")
              
          @property
          def family_name(self):
              return self.__family_name
          
      class Child(Parent): #Parent 클래스 상속
          def __init__(self, first_name, last_name):
              Parent.__init__(self, last_name) #부모 클래스의 __family_name 필드를 매개변수 last_name으로 초기화하였다.
              # super().__init__(last_name)처럼 클래스 이름을 사용하지 않고 부모 클래스를 반환하는 super() 호출과 생성자 호출을 결합해 동일한 효과를 얻을 수 있다.
              self.__first_name = first_name #자식 클래스의 인스턴스 필드 first_name은 매개변수 first_name에 이해 초기화됨
              print("Child 클래스의 __init__() ...")
              
          @property
          def first_name(self):
              return self.__first_name
          
          @first_name.setter
          def first_name(self, first_name):
              self.__first_name = first_name
              
          @property
          def name(self): #name 속성은 부모 속성인 Parent 클래스의 family_name 속성의 반환 값과 Child 클래스의 first_name 속성의 반환 값을 문자열로 만들어 반환
              return "{} {}".format(self.family_name, self.first_name)
          
      child = Child("길동","홍")
      
      print(child.family_name)
      print(child.first_name)
      print(child.name)
      
      #결과
      홍
      길동
      홍 길동
      
      print(child.family_name)
      print(child.first_name)
      print(child.name)
      print("======>")
      child.first_name = "길순" #child 클래스의 first_name 속성에 새로운 값 길순을 저장하고
      print(child.name) #name 속성을 통해 그 변경의 값을 확인
      
      #결과
      홍
      길동
      홍 길동
      ======>
      홍 길순
      ```

  - 메서드 오버라이딩

    - 상속 관계에서 부모 클래스에 있는 메서드와 동일한 서명을 가진 메서드를 자식 클래스에서 다시 정의해 사용하는 것

    - 부모 클래스에서 정의한 메서드가 아닌 자식 클래스에서 정의한 메서드를 사용하게 된다.

    - ```python
      class Person:
          def __init__(self, family_name):
              self.__family_name = family_name
              print("Parent 클래스의 __init__() ...")
              
          @property
          def family_name(self):
              return self.__family_name
          
          def print_info(self): #parent 클래스에서 family_name을 출력한다.
              print("Parent: {}".format(self.family_name))
              
      class Child(Parent):
          def __init__(self, first_name, last_name):
              Parent.__init__(self, last_name)
              # super().__init__(last_name)
              self.__first_name = first_name
              print("Child 클래스의 __init__() ...")
              
          @property
          def first_name(self):
              return self.__first_name
          
          @first_name.setter
          def first_name(self, first_name):
              self.__first_name = first_name
              
          @property
          def name(self):
              return "{} {}".format(self.family_name, self.first_name)
          
          def print_info(self): #Child 클래스에서 print_info 메서드를 오버라이딩 하고
              Parent.print_info(self) #parent 클래스의 print_info 메서드를 호출하고
              # super().print_info()
              print("Child: {}".format(self.name)) #child 클래스에서 name 정보를 출력한다
              
      child = Child("길동", "홍") #Child 객체에 오버로딩된 메서드 print_info를 호출하면
      child.print_info()
      ```

    - ![](/image/10.png)

- **student 클래스에 객체 4개를 생성하여 리스트에 추가하고 각각의 필드값을 이용하여 오름차순/내림차순으로 정렬하기**

  - 해당 프로그램에서는 student 클래스를 정의한다.
    - name, gender, height프라이빗 필드를 가지고 있고
    - 읽기 전용 name, gender의 프로퍼티
    - 읽기, 쓰기 모두 가능한 height 프로퍼티
    - 특수함수 __ repr __에 대한 정의를 가진 프로그램이다.

```python
class Student:
    
    def __init__(self, name, gender, height):
        self.__name = name #프라이빗 속성 name을 매개변수로 들어온 정보를 초기화
        self.__gender = gender
        self.__height = height
        
    #프로퍼티 생성
    @property
    def name(self): #name 프로퍼티는 name을 리턴하면 됨, setter는 만들지 않는다.
        return self.__name
    
    @property
    def gender(self):
        return self.gender
    
    #height는 읽고 쓰기가 가능하도록 만들자
    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self, height): #self와 더불어서 height 정보를 인자로 받도록 했음
        self.__height = height #self.__height를 매개변수로 들어온 height로 변경하도록 했다.
        
    def __repr__(self): #대부분의 객체를 출력할 때 많이 사용하는 함수로서 객체의 표현을 지원해주는 repr 함수, repr 함수는 객체 출력 시 주로 사용한다. repr을 str로 바꿔도 된다.
        return "{0}(name: {1}, gender: {2}, height: {3})".format(self.__class__.__name__,self.name, self.gender, self.height) #클래스 이름을 Student 그대로 가져와도 되지만 객체 self에는 class라는 정보가 있고 class에는 name이라는 정보가 존재한다. name property를 이용해 쓸 수 있다. 여기에 self가 가지고 있는 name property, gender self의 height 정보를 출력할 수 있도록 만들었다.

s1 = Student("홍길동", "남", 176.5)

print(s1)

#결과
Student(name: 홍길동, gender: 남, height: 176.5)
```

```python
class Student:
    
    def __init__(self, name, gender, height):
        self.__name = name #프라이빗 속성 name을 매개변수로 들어온 정보를 초기화
        self.__gender = gender
        self.__height = height
        
    #프로퍼티 생성
    @property
    def name(self): #name 프로퍼티는 name을 리턴하면 됨, setter는 만들지 않는다.
        return self.__name
    
    @property
    def gender(self):
        return self.gender
    
    #height는 읽고 쓰기가 가능하도록 만들자
    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self, height): #self와 더불어서 height 정보를 인자로 받도록 했음
        self.__height = height #self.__height를 매개변수로 들어온 height로 변경하도록 했다.
        
    def __repr__(self): #대부분의 객체를 출력할 때 많이 사용하는 함수로서 객체의 표현을 지원해주는 repr 함수
        return "{0}(name: {1}, gender: {2}, height: {3})".format(self.__class__.__name__,self.name, self.gender, self.height) #클래스 이름을 Student 그대로 가져와도 되지만 객체 self에는 class라는 정보가 있고 class에는 name이라는 정보가 존재한다. name property를 이용해 쓸 수 있다. 여기에 self가 가지고 있는 name property, gender self의 height 정보를 출력할 수 있도록 만들었다.

students = [
    Student("홍길동", "남", 176.5),
    Student("이순신", "남", 188.5),
    Student("유관순", "여", 158.4),
    Student("강감찬", "남", 182.2)   
]

for student in studnets:
    print(student)
```

- name 기준 오름차순 정렬

```python
class Student:
    
    def __init__(self, name, gender, height):
        self.__name = name #프라이빗 속성 name을 매개변수로 들어온 정보를 초기화
        self.__gender = gender
        self.__height = height
        
    #프로퍼티 생성
    @property
    def name(self): #name 프로퍼티는 name을 리턴하면 됨, setter는 만들지 않는다.
        return self.__name
    
    @property
    def gender(self):
        return self.gender
    
    #height는 읽고 쓰기가 가능하도록 만들자
    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self, height): #self와 더불어서 height 정보를 인자로 받도록 했음
        self.__height = height #self.__height를 매개변수로 들어온 height로 변경하도록 했다.
        
    def __repr__(self): #대부분의 객체를 출력할 때 많이 사용하는 함수로서 객체의 표현을 지원해주는 repr 함수
        return "{0}(name: {1}, gender: {2}, height: {3})".format(self.__class__.__name__,self.name, self.gender, self.height) #클래스 이름을 Student 그대로 가져와도 되지만 객체 self에는 class라는 정보가 있고 class에는 name이라는 정보가 존재한다. name property를 이용해 쓸 수 있다. 여기에 self가 가지고 있는 name property, gender self의 height 정보를 출력할 수 있도록 만들었다.

students = [
    Student("홍길동", "남", 176.5),
    Student("이순신", "남", 188.5),
    Student("유관순", "여", 158.4),
    Student("강감찬", "남", 182.2)   
]

for student in students:
    print(student)
    
#sorted를 하기 위해선 이름, 젠더, 키 중 어떤 것으로 정렬할 지 정보가 필요하다. 어떻게 하는지 알아보자

print("name으로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name): #sorted 함수는 반복가능한 객체를 대상으로 한다. 사용자 정의 객체 사용 시 해당 리스트 객체에 있는 각 항목에서 키를 사용한 정보 전달해야한다. 함수는 반복되는 객체의 항목을 인자로 받아 수행한다. x는 student 객체인데 이름으로 오름차순 할 예정이니 이름을 반환하도록 한다.
	print(student)
```

- name 기준 내림차순 정렬

```python
class Student:
    
    def __init__(self, name, gender, height):
        self.__name = name #프라이빗 속성 name을 매개변수로 들어온 정보를 초기화
        self.__gender = gender
        self.__height = height
        
    #프로퍼티 생성
    @property
    def name(self): #name 프로퍼티는 name을 리턴하면 됨, setter는 만들지 않는다.
        return self.__name
    
    @property
    def gender(self):
        return self.gender
    
    #height는 읽고 쓰기가 가능하도록 만들자
    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self, height): #self와 더불어서 height 정보를 인자로 받도록 했음
        self.__height = height #self.__height를 매개변수로 들어온 height로 변경하도록 했다.
        
    def __repr__(self): #대부분의 객체를 출력할 때 많이 사용하는 함수로서 객체의 표현을 지원해주는 repr 함수
        return "{0}(name: {1}, gender: {2}, height: {3})".format(self.__class__.__name__,self.name, self.gender, self.height) #클래스 이름을 Student 그대로 가져와도 되지만 객체 self에는 class라는 정보가 있고 class에는 name이라는 정보가 존재한다. name property를 이용해 쓸 수 있다. 여기에 self가 가지고 있는 name property, gender self의 height 정보를 출력할 수 있도록 만들었다.

students = [
    Student("홍길동", "남", 176.5),
    Student("이순신", "남", 188.5),
    Student("유관순", "여", 158.4),
    Student("강감찬", "남", 182.2)   
]

for student in students:
    print(student)
    
#sorted를 하기 위해선 이름, 젠더, 키 중 어떤 것으로 정렬할 지 정보가 필요하다. 어떻게 하는지 알아보자

print("name으로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name):
	print(student)
    
print("name으로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name, reverse=True): #사용할 키는 lambda 식으로 정의, reverse와 관련된 매개변수의 값을 True로 했다. 즉 역순으로 정렬한다.
	print(student)
```

- height 기준 오름차순, 내림차순 정렬

```python
class Student:
    
    def __init__(self, name, gender, height):
        self.__name = name #프라이빗 속성 name을 매개변수로 들어온 정보를 초기화
        self.__gender = gender
        self.__height = height
        
    #프로퍼티 생성
    @property
    def name(self): #name 프로퍼티는 name을 리턴하면 됨, setter는 만들지 않는다.
        return self.__name
    
    @property
    def gender(self):
        return self.gender
    
    #height는 읽고 쓰기가 가능하도록 만들자
    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self, height): #self와 더불어서 height 정보를 인자로 받도록 했음
        self.__height = height #self.__height를 매개변수로 들어온 height로 변경하도록 했다.
        
    def __repr__(self): #대부분의 객체를 출력할 때 많이 사용하는 함수로서 객체의 표현을 지원해주는 repr 함수
        return "{0}(name: {1}, gender: {2}, height: {3})".format(self.__class__.__name__,self.name, self.gender, self.height) #클래스 이름을 Student 그대로 가져와도 되지만 객체 self에는 class라는 정보가 있고 class에는 name이라는 정보가 존재한다. name property를 이용해 쓸 수 있다. 여기에 self가 가지고 있는 name property, gender self의 height 정보를 출력할 수 있도록 만들었다.

students = [
    Student("홍길동", "남", 176.5),
    Student("이순신", "남", 188.5),
    Student("유관순", "여", 158.4),
    Student("강감찬", "남", 182.2)   
]

for student in students:
    print(student)
    
#sorted를 하기 위해선 이름, 젠더, 키 중 어떤 것으로 정렬할 지 정보가 필요하다. 어떻게 하는지 알아보자

print("name으로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name):
	print(student)
    
print("name으로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name, reverse=True):
	print(student)

print("height로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.height):
	print(student)
    
print("height로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.height, reverse=True):
	print(student)
```

