#다음의 결과와 같이 구구단 2단부터 9단의 결과값 중에 3의 배수거나 7의 배수인 수를
#제외한 값을 리스트 객체 result 안에 각 단마다 리스트를 만들어 삽입하고 이를 출력하십시오.
# 1. 1단부터 9단까지 만든다.
# 2. 만든걸 하나의 리스트 안에 집어넣는다.
# 3. 3의 배수 리스트 뺀다.
# 4. 7의 배수 리스트 뺀다.
# 5. 출력한다.
result = []
dan = []
real_result = []
for i in range(2, 10):
    for j in range(1, 10):
        dan.append(i*j)
    result.append(dan)
    dan=[]
for i in result:
    for j in i[:]:
        if j % 3 ==0 or j % 7 == 0:
            i.remove(j)
print(result)
        

