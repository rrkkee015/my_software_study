# 다음과 같이 2차원 배열 구조를 만들기 위한 행, 열 정보를 콤마(,)로 구분해 입력하고,
# 이 리스트 객체의 항목의 값은 행과 열의 인덱스 곱으로 초기화해 출력하는 프로그램을 작성하십시오.

# 1. 입력 값을 받는다.
# 2. 처음 행을 받은 애로 for문을 만들어 돌리고
# 3. 2번 for문 안에 for문을 또 만들어서 각각의 인덱스의 값과 2번의 인덱스 값을 곱한다.

lis = input('').split(', ')
lis = list(map(int, lis))
result_1=[]
result_2=[]
for i in range(0, lis[0]):
    for j in range(0, lis[1]):
        result_1.append(i*j)
    result_2.append(list(result_1))
    result_1 =[]
print(result_2)
