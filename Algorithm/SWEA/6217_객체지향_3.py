#name 프로퍼티를 가진 Student를 부모 클래스로 major 프로퍼티를 가진
#GraduateStudent 자식 클래스를 정의하고 이 클래스의 객체를
#다음과 같이 문자열로 출력하는 코드를 작성하십시오.

#입력:없음
#출력:이름: 홍길동
#     이름: 이순신, 전공: 컴퓨터

class Student:
    def __init__(self,name):
        self.__name=name
        
    @property
    def name(self):
        return "이름: {}".format(self.__name)

class GraduateStudent(Student):
    def __init__(self, name2, major):
        Student.__init__(self,name2)
        self.__major=major
        
    @property
    def major(self):
        return "{}, 전공: {}".format(self.name,self.__major)

#얘는 안된다.
#    @property
#    def major(self):
#        return "{}, 전공: {}".format(self.__name,self.__major)

#왜 자식클래스에서 부모클래스의 "이름"이 출력되는 걸까? 나는 name 함수 부르지도 않았는데

student = Student("홍길동")
graduate = GraduateStudent("이순신","컴퓨터")
print(student.name)
print(graduate.major)

# 1. 부모 클래스에서 __를 쓰면 private 변수로 선언되기 때문에 외부에서 바로 접근이 안 된다.
# 1-1. 단, self._클래스이름__숨긴변수이름 으로 부를 수 있다.
# 2. 부모 클래스에서 __를 쓰지 않으면 부모.__init()을 한 후에는 부모의 변수들을 바로 접근할 수 있다.
# 3. @property는 private된 것에 접근할 수록 있도록 한다.
