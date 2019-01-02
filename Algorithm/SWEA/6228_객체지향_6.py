#Shape를 부모 클래스로 Square 자식 클래스를 정의하는 코드를 작성하십시오.
#Square 클래스는 length 필드를 가지며, 0을 반환하는 Shape 클래스의 area 메서드를
#length * length 값을 반환하는 메서드로 오버라이딩합니다.

class Shape:
    def __init__(self,length):
        self.length=length

    def area(self):
        return 0

class Square(Shape):
    def area(self): #동일한 이름을 가진 메서드를 적으면 부모 클래스의 메서드는 없어지는 오버라이딩이 생긴다.
        print("정사각형의 면적: {}".format(self.length**2)) 

area=Square(3)
area.area()

#상속에 대해 알아보자
class Shape:
    def __init__(self,length):
        self.length=length

    def area2(self):
        return "0"

class Square(Shape):
    def area(self): #동일한 이름을 가진 메서드를 적으면 부모 클래스의 메서드는 없어지는 오버라이딩이 생긴다.
        print("정사각형의 면적: {}".format(self.length**2)) 

area=Square(3)
area.area2() #얘를 실행하면 0이 출력이 되는데 분명 자식클래스를 객체로 삼았다. 자식클래스에는 area2가 없지만
#상속받은 Shape 부모한테 area2가 있고 그 정보가 자식놈에게 상속되어 있으니 area2가 실행될 수 있는 것이다.
