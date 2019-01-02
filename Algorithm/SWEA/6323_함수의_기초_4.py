# 1. 10을 치면 10개의 피보나치 수열이 리스트 형식으로 나타나게 하자.
# 2. while문을 이용해서 지정한 숫자 횟수만큼 이전의 숫자와 합쳐지게 만들자.
# 3. 합쳐진 숫자를 append하여 리스트를 제작하자.
# 4. 다 했으면 return 값을 받을 수 있는 함수를 제작하고 함수를 만들고 출력하자.

def function():
    number = int(input(''))
    start_number = 1
    lis = [1,1]
    number_new= 0
    while start_number < number-1:
        number_new = lis[-1] + lis[-2]
        lis.append(number_new)
        start_number = start_number + 1
    return lis
result = function()
print(result)
