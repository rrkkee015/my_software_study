#가로, 세로 정보를 갖고, 사각형의 면적을 계산하는 메서드를 갖는 Rectangle 클래스를 정의하고,
#생성한 객체의 사각형의 면적을 출력하는 프로그램을 작성하십시오.

#입력:없음
#출력:사각형의 면적: 20

class Rectangle:
    def __init__(self,hor,ver):
        self.hor=hor
        self.ver=ver

    def Area(self):
        return self.hor*self.ver

area = Rectangle(5,4)
print("사각형의 면적: {}".format(area.Area()))
