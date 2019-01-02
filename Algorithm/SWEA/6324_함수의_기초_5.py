# 1. 리스트 input 받을 수 있는 변수를 설정하자.
# 2. 그 리스트가 중복된 수가 있는 지 확인하자.
# 3. 중복된 수를 지우자.
# 4. 리스트 정렬하자.
# 5. 리턴 값을 가지는 함수를 넣을 변수를 설정하자.
# 6. 출력하자.

number = input().split()

def function():
    lis =[]
    for i in number:
        lis.append(int(i))
    return list(set(lis))

line = function()
print("{}\n{}".format(list(map(int, number)),line))
