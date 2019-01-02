#반지름 정보를 갖고, 원의 면적을 계산하는 메서드를 갖는 Circle 클래스를 정의하고,
#생성한 객체의 원의 면적을 출력하는 프로그램을 작성하십시오.

#입력:없음
#출력:원의 면적: 12.56

#1.Circle 클래스를 만든다.
#2.인풋받은 애를 이용하여 생성자 메서드를 만든다.
#3.객체를 만들고
#4.객체의 면적을 출력한다.

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        return "원의 면적: {}".format(self.radius**2*3.14)

area=Circle(2)
print(area.Area())
