#다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
#이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.

#입력 : 89, 90, 100
#출력 : 국어, 영어, 수학의 총점: 279

class scores:
    def __init__(self,kor,eng,mat):
        self.kor=kor
        self.eng=eng
        self.mat=mat

    def total(self):
        return self.kor+self.eng+self.mat

a,b,c=list(map(int,input('').split(', ')))
result=scores(a,b,c)
print("국어, 영어, 수학의 총점: {}".format(result.total()))

# 다른 풀이 (input을 생성자 메서드에서 바로 받는 법)

class scores:
    def __init__(self):
        kor,eng,math = list(map(int,input('').split(', ')))
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return self.kor+self.eng+self.math

student=scores()
print("국어, 영어, 수학의 총점: {}".format(student.total()))
