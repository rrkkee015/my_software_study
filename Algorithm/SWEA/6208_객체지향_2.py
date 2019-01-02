#국적을 출력하는 printNationality 정적 메서드를 갖는 Korean 클래스를 정의하고
#메서드를 호출하는 코드를 작성해봅시다.

#입력 : 없음
#출력 : 대한민국
#       대한민국

class Korean:
    
    @staticmethod
    def printNationality():
        return "대한민국\n대한민국"

print(Korean.printNationality())

#근데 굳이 @staticmethod가 없어도 되더라
