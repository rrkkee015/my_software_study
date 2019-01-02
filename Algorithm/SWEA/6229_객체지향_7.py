#Person을 부모 클래스로 Male, Female 자식 클래스를 정의하는 코드를 작성하십시오.
#"Unknown"을 반환하는 Person 클래스의 getGender 메서드를 Male 클래스와 Female 클래스는
#"Male", "Female" 값을 반환하는 메서드로 오버라이딩합니다.

#입력:없음
#출력:Male
#     Female

#1.Person 부모 클래스를 만든다.

class Person:
#2. 안에 getGender 메서드를 삽입한다. 반환값은 "Unknown"으로 한다.

    def getGender(self):
        return "Unknown"

#2. 상속받는 자식 클래스 Male과 Female을 만들자. 안에 메서드 만들 땐 getGender 이름을 생성하여 오버라이딩한다.

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"

#3. 객체를 생성한다.
male=Male()
female=Female()
print(male.getGender())
print(female.getGender())
