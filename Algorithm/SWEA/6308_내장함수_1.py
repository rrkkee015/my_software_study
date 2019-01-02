# 1. input으로 이름과 나이를 받는 변수를 설정한다.
# 2. 올해 2018년 기준으로 100 - 나이를 해서 언제 100세가 되는 년도를 찾는다.
# 3. 출력한다.
def function():
    name,age=input().split(' ')
    year_100=2018+(100-int(age))
    return [name, year_100]

result=function()
print("{}(은)는 {}년에 100세가 될 것입니다.".format(*result))

