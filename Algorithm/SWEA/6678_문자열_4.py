#다음의 결과와 같이 여러 문장을 입력받아 대문자로 변환해 출력하는 프로그램을 작성합니다.
#아무 것도 입력하지 않고 엔터만 입력하면 입력이 종료됩니다.
#입력 : Hello World
#       hello world
#       Python
#출력 : >> HELLO WORLD
#       >> HELLO WORLD
#       >> PYTHON

# 1. while문을 돌려서 input 받는 갯수를 정할 수 있게한다. 
# 2. upper로 대문자 변환한다.
# 3. 출력한다.

i = 0
lis = []
while i < 50:
    let = input('')
    if let == '':
        break
    lis.append(let)
    i += 1
for j in lis:
    print(">> {}".format(j.upper()))
