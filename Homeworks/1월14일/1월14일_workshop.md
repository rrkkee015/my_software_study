# OOP

> Background

- 객체지향프로그래밍
- 클래스, 인스턴스

> Goal

- 클래스에 대한 이해

> Problem

- 다음과 같은 클래스 Circle이 있다.

```python
class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0
    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r
    
    def center(self):
        return (self.x, self.y)
    
    def move(self, x, y):
        self.x = x
        self.y = y
```

- 반지름이 3이고 x,y 좌표가 (2,4)인 원을 만들어 넓이와 둘레를 출력하세요.

```python
class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0
    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r
    
    def center(self):
        return (self.x, self.y)
    
    def move(self, x, y):
        self.x = x
        self.y = y
        
cir=Circle()
#cir.x, cir.y=2,4 #이렇게 따로 좌표를 지정해고 move 안에 
cir.move(2,4)
cir.r=3
print(f'넓이 : {cir.area():.2f}\n둘레 : {cir.circumference():.2f}\n좌표 : {cir.center()}')
```

```python
#성진이 버전
class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0
    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r
    
    def center(self):
        return (self.x, self.y)
    
    def move(self, x, y):
        self.x = x
        self.y = y
```



