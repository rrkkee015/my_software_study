```python
#info의 staticmethod 질문
class Dog:
    nums=0
    def __init__(self, name, age):
        self.age = age
        self.name = name
        Dog.nums += 1
    
    def bark(self):
        print(f'멍멍 나는 {self.name}이고, {self.age}살 입니다.')
    @staticmethod    
    def info():
        print(f'이 친구는 {name} 강아지입니다.')
    
    def count(self):
        print(f'총 강아지 수는 {self.num}마리 입니다.')
        
york=Dog('요크',4)
poodle=Dog('푸들',7)
maltiz=Dog('말티즈',2)

Dog.info()
york.info()
```

```python
# #붙은 애들 전부 에러, 밑에서 4번째 질문
class Dog:
    nums=0
    def __init__(self, name, age):
        self.age = age
        self.name = name
        Dog.nums += 1
    
    def bark(self):
        print(f'멍멍 나는 {self.name}이고, {self.age}살 입니다.')
    @staticmethod    
    def info():
        print(f'이 친구는 강아지입니다.')
    @classmethod
    def count(cls):
        print(f'총 강아지 수는 {cls.nums}마리 입니다.')
        
york=Dog('요크',4)
poodle=Dog('푸들',7)
maltiz=Dog('말티즈',2)

york.bark()
poodle.bark()
maltiz.bark()
#Dog.bark()
Dog.bark(york)
#york.info()
#poodle.info()
#maltiz.info()

Dog.info()
york.info() #static이 붙기 전엔 얘가 안됐음

york.count() #된다. 그렇다면 얘 인자는 어떤 방식으로 받는 것일까?
#Dog.count(york) #class가 붙기 전엔 얘가 안됐음
#Dog로 클래스를 첫번째 인자로 집어넣었는데 york 하나 더 있네? 
#근데 걔는 넣을 곳이 없다. 그래서 에러
Dog.count() 
```

